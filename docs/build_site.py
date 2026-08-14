"""
Build the static site data from the database_*.md files.

Parses the main table out of each database file in the repository root (plus the
per-ecosystem detail sections) and writes docs/data/data.js, which the site loads
as a plain script so that the pages also work when opened directly from disk.

Usage: python docs/build_site.py
"""

import json
import re
from pathlib import Path

DOCS = Path(__file__).parent
ROOT = DOCS.parent
OUT = DOCS / 'data' / 'data.js'
PUBLICATIONS = DOCS / 'data' / 'publications.json'
UPDATED = DOCS / 'data' / 'updated.json'

# Which file, which section heading holds the main table, and how it's labelled.
SOURCES = [
    dict(key='tools', label='Tools', file='database_tools.md', section='Tools'),
    dict(key='ecosystems', label='Ecosystems', file='database_ecosystems.md', section='Ecosystems'),
    dict(key='communities', label='Communities', file='database_communities.md', section='Communities'),
]


def split_row(line):
    """Split a markdown table row into stripped cells."""
    return [cell.strip() for cell in line.strip().strip('|').split('|')]


def parse_table(lines, start):
    """Parse the first markdown table at or after `start`; return (columns, rows)."""
    i = start
    while i < len(lines) and not lines[i].lstrip().startswith('|'):
        i += 1
    if i >= len(lines):
        raise ValueError('no table found')
    columns = split_row(lines[i])
    i += 2  # skip the |---|---| separator
    rows = []
    while i < len(lines) and lines[i].lstrip().startswith('|'):
        cells = split_row(lines[i])
        cells += [''] * (len(columns) - len(cells))  # tolerate short rows
        rows.append(cells[:len(columns)])
        i += 1
    return columns, rows


def parse_intro(lines):
    """First prose paragraph after the H1."""
    out = []
    started = False
    for line in lines[1:]:
        if line.startswith('#'):
            break
        if line.strip():
            started = True
            out.append(line.strip())
        elif started:
            break
    return ' '.join(out)


def parse_details(lines):
    """Markdown under each `###` heading of the `## Per-ecosystem detail` section."""
    details = {}
    name, buf, inside = None, [], False
    for line in lines:
        if line.startswith('## '):
            if inside and name:
                details[name] = '\n'.join(buf).strip()
            inside = line[3:].strip().lower().startswith('per-ecosystem detail')
            name, buf = None, []
        elif inside and line.startswith('### '):
            if name:
                details[name] = '\n'.join(buf).strip()
            name, buf = line[4:].strip(), []
        elif inside and name is not None:
            buf.append(line)
    if inside and name:
        details[name] = '\n'.join(buf).strip()
    return details


def load_publications():
    if not PUBLICATIONS.exists():
        print(f'note: {PUBLICATIONS.name} missing -- run fetch_publications.py to show titles')
        return {}
    return json.loads(PUBLICATIONS.read_text(encoding='utf-8'))


def load_updated():
    if not UPDATED.exists():
        print(f'note: {UPDATED.name} missing -- run fetch_updated.py to show update dates')
        return {}
    return json.loads(UPDATED.read_text(encoding='utf-8'))


def add_updated(columns, rows, updated):
    """
    Append an Updated column: last commit date for tools with a repository, last
    release date for tools distributed only as a package, N/A for the rest. The
    dates live in the generated cache rather than in the database file, since
    they go stale on their own rather than through anyone editing the database.
    """
    columns.append('Updated')
    hits = 0
    for row in rows:
        record = updated.get(row[0])
        row.append(record['date'] if record else 'N/A')
        hits += bool(record)
    return hits


def title_publications(rows, index, publications):
    """Rewrite `[10.1234/x](https://doi.org/10.1234/x)` cells to use the paper's title."""
    pattern = re.compile(r'^\[[^\]]+\]\(https://doi\.org/(10\.[^)]+)\)$')
    hits = 0
    for row in rows:
        match = pattern.match(row[index])
        record = publications.get(match.group(1)) if match else None
        if not record:
            continue
        suffix = ', '.join(filter(None, [record.get('journal'), str(record.get('year') or '')]))
        # Escape the brackets markdown would otherwise read as a nested link.
        title = record['title'].replace('[', r'\[').replace(']', r'\]')
        row[index] = f'[{title}](https://doi.org/{match.group(1)})'
        if suffix:
            row[index] += f' — *{suffix}*'
        hits += 1
    return hits


def build():
    data = {'sections': []}
    publications = load_publications()
    updated = load_updated()
    for src in SOURCES:
        text = (ROOT / src['file']).read_text(encoding='utf-8')
        lines = text.split('\n')

        heading = re.compile(r'^##\s+' + re.escape(src['section']) + r'\s*$')
        start = next(i for i, line in enumerate(lines) if heading.match(line))
        columns, rows = parse_table(lines, start + 1)

        titled = 0
        if 'Publication' in columns:
            titled = title_publications(rows, columns.index('Publication'), publications)

        dated = add_updated(columns, rows, updated) if src['key'] == 'tools' else 0

        section = dict(
            key=src['key'],
            label=src['label'],
            source=src['file'],
            intro=parse_intro(lines),
            columns=columns,
            rows=rows,
        )
        details = parse_details(lines)
        if details:
            section['details'] = details
        data['sections'].append(section)
        print(f"{src['file']}: {len(rows)} rows x {len(columns)} columns"
              f"{f', {len(details)} detail sections' if details else ''}"
              f"{f', {titled} publication titles' if titled else ''}"
              f"{f', {dated} update dates' if dated else ''}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=1)
    OUT.write_text(
        '// Generated by build_site.py -- do not edit by hand.\n'
        f'window.DB = {payload};\n',
        encoding='utf-8',
    )
    print(f'Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1024:.0f} kB)')



if __name__ == '__main__':
    build()
