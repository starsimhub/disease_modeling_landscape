"""
One command to take the database_*.md files to the built site.

Runs, in order: a check that the tables are well formed and internally consistent;
a Crossref lookup for any DOI not already cached and a last-updated lookup for any
tool not already cached; and the data.js build. Anything the checker reports as an
error stops the build, so a malformed table cannot be published silently.

Usage:
    python docs/build.py              # check, fetch what is missing, build
    python docs/build.py --offline    # skip the fetch steps (no network)
    python docs/build.py --refresh    # re-fetch everything, not just what is new
    python docs/build.py --check      # run the checks only, build nothing

Update dates go stale on their own rather than through anyone editing a database
file, so `--refresh` is the way to bring them up to date.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import build_site
import fetch_publications
import fetch_updated

ROOT = Path(__file__).parent.parent

# Each database file's H1 count sentence, e.g. "137 tools, sorted alphabetically".
COUNT_RE = re.compile(r'^(\d+) (tools|ecosystems|communities)\b', re.M)

# Every Usage cell is `Label` or `Label (evidence)`; fetch_usage.py writes them.
USAGE_RE = re.compile(r'^(Established|Emerging|Minimal)( \(.+\))?$')


def check_table(src, columns, rows, problems):
    """Structural checks that the site build itself is too permissive to catch."""
    label = src['file']

    for i, row in enumerate(rows):
        if len(row) != len(columns):
            problems.append(f'{label}: row {i + 1} has {len(row)} cells, expected {len(columns)}')
        if not row[0].strip():
            problems.append(f'{label}: row {i + 1} has an empty name')

    names = [row[0] for row in rows]
    for a, b in zip(names, names[1:]):
        if a.lower() > b.lower():
            problems.append(f'{label}: "{b}" sorts before "{a}" but is listed after it')

    duplicates = {n for n in names if names.count(n) > 1}
    if duplicates:
        problems.append(f'{label}: duplicate names {sorted(duplicates)}')

    # The prose states a count; keep it honest rather than letting it drift.
    text = (ROOT / label).read_text(encoding='utf-8')
    stated = COUNT_RE.search(text)
    if stated and int(stated.group(1)) != len(rows):
        problems.append(f'{label}: prose says {stated.group(1)} {stated.group(2)}, '
                        f'table has {len(rows)}')

    if 'Usage' in columns:
        for row in rows:
            cell = row[columns.index('Usage')]
            if not USAGE_RE.match(cell):
                problems.append(f'{label}: {row[0]} has a Usage cell that does not start with '
                                f'a usage label -- re-run docs/fetch_usage.py')

    if 'Publication' in columns:
        for row in rows:
            cell = row[columns.index('Publication')]
            if cell not in ('', '—') and 'doi.org/' not in cell:
                problems.append(f'{label}: {row[0]} has a Publication that is not a DOI link')


def check():
    problems = []
    for src in build_site.SOURCES:
        lines = (ROOT / src['file']).read_text(encoding='utf-8').split('\n')
        heading = re.compile(r'^##\s+' + re.escape(src['section']) + r'\s*$')
        try:
            start = next(i for i, line in enumerate(lines) if heading.match(line))
        except StopIteration:
            problems.append(f"{src['file']}: no '## {src['section']}' heading")
            continue
        columns, rows = build_site.parse_table(lines, start + 1)
        check_table(src, columns, rows, problems)
        print(f"{src['file']}: {len(rows)} rows, {len(columns)} columns -- ok"
              if not problems else f"{src['file']}: {len(rows)} rows, {len(columns)} columns")
    return problems


def main():
    problems = check()
    if problems:
        print('\nProblems found:')
        for problem in problems:
            print(f'  {problem}')
        return 1
    if '--check' in sys.argv:
        print('\nChecks passed; nothing built (--check).')
        return 0

    if '--offline' not in sys.argv:
        print()
        fetch_publications.main()
        print()
        fetch_updated.main()
    print()
    build_site.build()
    print('\nOpen docs/index.html, or: python -m http.server 8000 --directory docs')
    return 0


if __name__ == '__main__':
    sys.exit(main())
