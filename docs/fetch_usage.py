"""
Score every tool in database_tools.md for usage, and rewrite its Usage cell.

Each tool gets a points total from four commensurable sources:

    1 point   per GitHub star, and per fork
    1 point   per 1,000 package downloads (CRAN total, PyPI total)
    1 point   per citation of the tool's foundational paper
    1 point   per country with documented use

and a label from that total: >50 points `Established`, 10-50 `Emerging`, <10
`Minimal`. The points are deliberately not published -- they combine metrics that
are not really commensurable, and stating them to the unit would claim a
precision the inputs do not have -- so the cell shows the label followed by the
evidence behind it, e.g. `Established (288★, 238 forks; PyPI 318k)`.

Download counts are all-time: CRAN via cranlogs, PyPI via the public ClickHouse
mirror of the PyPI download statistics (pypistats.org serves only the last 180
days, which would undercount long-lived packages against CRAN's lifetime totals).
Citations are Crossref's `is-referenced-by-count` for the DOI in the Publication
column. Country counts are read out of the prose already in the Usage cell
("Used by teams in 40+ countries" -> 40); prose that documents a national or
agency deployment without naming a number counts as one country. Anything the
prose does not state can be set by hand in docs/data/usage_manual.json, which is
merged over the fetched values and never overwritten.

Writes docs/data/usage.json -- the full per-tool breakdown, committed so that a
label can be audited without re-fetching -- and edits the Usage column of
database_tools.md in place. Prose clauses in the existing cell are preserved;
the star, fork, CRAN and PyPI figures in it are regenerated.

Usage:
    python docs/fetch_usage.py               # re-fetch everything and rewrite the table
    python docs/fetch_usage.py --dry-run     # show the cells that would change
    python docs/fetch_usage.py --offline     # re-score and rewrite from the cache, no network
    python docs/fetch_usage.py --only NAME   # one tool (repeatable), cache-merged
"""

import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from build_site import ROOT, parse_table
from fetch_updated import (CRAN_RE, GITHUB_RE, HEADERS, PYPI_RE, TOKEN, URL_RE,
                           get_json)

DOCS = Path(__file__).parent
CACHE = DOCS / 'data' / 'usage.json'
MANUAL = DOCS / 'data' / 'usage_manual.json'
SOURCE = ROOT / 'database_tools.md'

CLICKHOUSE = 'https://sql-clickhouse.clickhouse.com/?user=demo&default_format=JSON'
DOI_RE = re.compile(r'https://doi\.org/(10\.[^)\s]+)')

# Segments of an existing Usage cell that this script regenerates; anything else
# in the cell is prose evidence and is kept.
GENERATED_RE = re.compile(r'★|^(CRAN|PyPI)\s|^(Established|Emerging|Minimal)\b')
COUNTRIES_RE = re.compile(r'(\d+)\s*\+?\s*countries', re.I)
# Prose that documents a deployment somewhere, when it names no number.
DEPLOYMENT_RE = re.compile(
    r'\bnational|\bnationally|\bcountry\b|\bcountries\b|\bministr|\bagenc|\bWHO\b|\bCDC\b'
    r'|\bUNAIDS\b|\bgovernment|\bprogramme|\bguidelines|\bpolicy|\bsurveillance|\bworldwide'
    r'|\bglobally|\bstate\b', re.I)

ESTABLISHED, EMERGING, MINIMAL = 50, 10, 0


def label_for(points):
    """>50 points Established, 10-50 Emerging, <10 Minimal."""
    if points > ESTABLISHED:
        return 'Established'
    if points >= EMERGING:
        return 'Emerging'
    return 'Minimal'


def points_for(record):
    """Total points; see the module docstring for the exchange rates."""
    downloads = (record.get('cran_downloads') or 0) + (record.get('pypi_downloads') or 0)
    return ((record.get('stars') or 0)
            + (record.get('forks') or 0)
            + downloads / 1000
            + (record.get('citations') or 0)
            + (record.get('countries') or 0))


def compact(n):
    """Download counts as they are written in the table: 530, 4.8k, 213k, 1.3M."""
    if n >= 1_000_000:
        return f'{n / 1_000_000:.1f}M'
    if n >= 10_000:
        return f'{round(n / 1000)}k'
    if n >= 1000:  # keep a digit where rounding to the nearest thousand would lose most of it
        return f'{n / 1000:.1f}k'.replace('.0k', 'k')
    return str(n)


# ------------------------------------------------------------------ fetching

def github_stats(owner, repo):
    data = get_json(f'https://api.github.com/repos/{owner}/{repo.removesuffix(".git")}', TOKEN)
    return data.get('stargazers_count'), data.get('forks_count')


def github_account_stats(account):
    """
    Stars and forks summed over an account's repositories, for the few entries
    whose Code column names a GitHub organisation rather than one repository
    (hubverse). The account's own `*.github.io` website repository is excluded,
    as in fetch_updated.
    """
    for kind in ('orgs', 'users'):
        try:
            repos = get_json(
                f'https://api.github.com/{kind}/{account}/repos?per_page=100', TOKEN)
        except urllib.error.HTTPError as exc:
            if exc.code != 404:
                raise
            continue
        repos = [r for r in repos if not r['name'].lower().endswith('.github.io')]
        if repos:
            return (sum(r.get('stargazers_count') or 0 for r in repos),
                    sum(r.get('forks_count') or 0 for r in repos))
    return None, None


def cran_downloads(package):
    """All-time CRAN downloads; cranlogs starts in 2012, so any early date works."""
    today = dt.date.today().isoformat()
    url = f'https://cranlogs.r-pkg.org/downloads/total/2000-01-01:{today}/{urllib.parse.quote(package)}'
    data = get_json(url)
    return data[0]['downloads'] if data else None


def pypi_downloads(projects):
    """
    All-time PyPI downloads for many projects in one query, from the public
    ClickHouse mirror (clickpy). PyPI itself publishes no lifetime totals.
    """
    if not projects:
        return {}
    quoted = ', '.join("'" + p.replace("'", "''") + "'" for p in sorted(projects))
    query = (f'SELECT project, sum(count) AS total FROM pypi.pypi_downloads '
             f'WHERE project IN ({quoted}) GROUP BY project')
    request = urllib.request.Request(CLICKHOUSE, data=query.encode(), headers=HEADERS)
    with urllib.request.urlopen(request, timeout=120) as response:
        data = json.load(response)
    return {row['project']: int(row['total']) for row in data['data']}


def pypi_metadata(project):
    try:
        return get_json('https://pypi.org/pypi/' + urllib.parse.quote(project) + '/json')
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return None


def citations(doi):
    """
    Works citing this DOI. OpenAlex first: it indexes preprint DOIs (several
    software papers here are arXiv or bioRxiv) that Crossref's own citation
    count does not cover, and its counts are the more complete of the two.
    """
    quoted = urllib.parse.quote(doi, safe='/')
    try:
        data = get_json(f'https://api.openalex.org/works/doi:{quoted}'
                        '?mailto=cliff.kerr@gatesfoundation.org')
        if data.get('cited_by_count') is not None:
            return data['cited_by_count']
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        pass
    data = get_json('https://api.crossref.org/works/' + quoted)
    return data['message'].get('is-referenced-by-count')


# ------------------------------------------------------- resolving package names

def slug(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def normalise(name):
    return re.sub(r'[^a-z0-9]', '', name.lower())


def resolve_pypi(name, code_url, repo, language):
    """
    The PyPI project for a tool, or None. A name given in the Code column is
    taken as stated; a guessed name counts only if the project's own metadata
    points back at the tool's repository, since PyPI is full of unrelated
    packages whose names collide with a tool's (`civet`, `epi`, `naomi`).
    """
    stated = PYPI_RE.search(code_url or '')
    if stated:
        return stated.group(1), 'stated'
    if 'python' not in (language or '').lower():
        return None, None

    candidates = []
    if repo:
        candidates.append(repo.split('/')[1])
    candidates += [slug(name), normalise(name)]
    fallback = None
    for candidate in dict.fromkeys(c for c in candidates if c):
        data = pypi_metadata(candidate)
        if not data:
            continue
        info = data.get('info') or {}
        project = info.get('name') or candidate
        urls = ' '.join(filter(None, [info.get('home_page') or '', info.get('project_url') or '',
                                      *(info.get('project_urls') or {}).values()]))
        if repo and repo.lower() in urls.lower():
            return project, 'repo-url'
        # A name-only match is weaker: PyPI holds unrelated packages whose names
        # collide with a tool's. Kept, but reported for review, and overridable
        # in usage_manual.json.
        if fallback is None and normalise(project) in (normalise(name), normalise(candidate)):
            fallback = project
    return (fallback, 'name-only') if fallback else (None, None)


def resolve_cran(name, code_url, language):
    """
    The CRAN package for a tool, or None. Named in the Code column, else the
    tool's own name for an R tool -- CRAN names are unique and crandb 404s on a
    name that is not there, so only an exact match survives.
    """
    stated = CRAN_RE.search(code_url or '')
    if stated:
        return stated.group(1)
    if not re.search(r'\br\b', (language or '').lower()):
        return None
    try:
        data = get_json('https://crandb.r-pkg.org/' + urllib.parse.quote(name))
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return None
    return data.get('Package')


# ------------------------------------------------------------------ the table

def prose_clauses(cell):
    """The parts of an existing Usage cell that no API can regenerate."""
    cell = re.sub(r'^(Established|Emerging|Minimal)\s*\((.*)\)$', r'\2', cell.strip())
    parts = [p.strip() for p in cell.split(';')]
    return [p for p in parts if p and p != '—' and not GENERATED_RE.search(p)]


def count_countries(prose):
    """Countries evidenced by the prose: an explicit number, else one for a deployment."""
    numbers = [int(m) for m in COUNTRIES_RE.findall(prose)]
    if numbers:
        return max(numbers)
    return 1 if prose and DEPLOYMENT_RE.search(prose) else 0


def compose(record):
    """`Established (288★, 238 forks; PyPI 318k)`."""
    parts = []
    if record.get('stars') is not None:
        forks = record.get('forks') or 0
        parts.append(f"{record['stars']}★, {forks} fork{'' if forks == 1 else 's'}")
    if record.get('cran_downloads'):
        parts.append('CRAN ' + compact(record['cran_downloads']))
    if record.get('pypi_downloads'):
        parts.append('PyPI ' + compact(record['pypi_downloads']))
    parts += record.get('prose') or []
    detail = '; '.join(parts)
    return f"{record['label']} ({detail})" if detail else record['label']


def load_rows():
    lines = SOURCE.read_text(encoding='utf-8').split('\n')
    start = next(i for i, line in enumerate(lines) if re.match(r'^##\s+Tools\s*$', line))
    columns, rows = parse_table(lines, start + 1)
    index = {col: i for i, col in enumerate(columns)}
    return [
        dict(name=row[index['Name']], code=row[index['Code']], language=row[index['Language']],
             publication=row[index['Publication']], usage=row[index['Usage']])
        for row in rows
    ]


def rewrite_table(cells):
    """Replace the Usage cell of every row named in `cells`; leave the rest alone."""
    lines = SOURCE.read_text(encoding='utf-8').split('\n')
    start = next(i for i, line in enumerate(lines) if re.match(r'^##\s+Tools\s*$', line))
    i = next(j for j in range(start, len(lines)) if lines[j].lstrip().startswith('|'))
    columns = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    usage = columns.index('Usage')
    changed = 0
    for j in range(i + 2, len(lines)):
        if not lines[j].lstrip().startswith('|'):
            break
        row = [c.strip() for c in lines[j].strip().strip('|').split('|')]
        new = cells.get(row[0])
        if new is None or row[usage] == new:
            continue
        row[usage] = new
        lines[j] = '| ' + ' | '.join(row) + ' |'
        changed += 1
    SOURCE.write_text('\n'.join(lines), encoding='utf-8')
    return changed


# ---------------------------------------------------------------------- main

def gather(tool, offline, cached):
    """Fetched facts for one tool, falling back to the cache for anything offline."""
    record = dict(cached) if cached else {}
    prose = prose_clauses(tool['usage'])
    record['prose'] = prose
    record['countries'] = count_countries(' '.join(prose))

    if offline:
        return record

    url_match = URL_RE.search(tool['code'])
    url = url_match.group(1) if url_match else tool['code'].strip()
    gh = GITHUB_RE.search(url)
    repo = f'{gh.group(1)}/{gh.group(2)}' if gh and gh.group(2) else None

    record['repo'] = repo
    record['stars'], record['forks'] = (None, None)
    try:
        if repo:
            record['stars'], record['forks'] = github_stats(*repo.split('/'))
        elif gh:  # an account rather than a repository
            record['stars'], record['forks'] = github_account_stats(gh.group(1))
    except (urllib.error.URLError, KeyError, TimeoutError) as exc:
        print(f"    {tool['name']}: GitHub failed ({exc})")

    record['cran'] = resolve_cran(tool['name'], url, tool['language'])
    record['cran_downloads'] = None
    if record['cran']:
        try:
            record['cran_downloads'] = cran_downloads(record['cran'])
        except (urllib.error.URLError, KeyError, IndexError, TimeoutError) as exc:
            print(f"    {tool['name']}: cranlogs failed ({exc})")

    record['pypi'], record['pypi_match'] = resolve_pypi(tool['name'], url, repo, tool['language'])
    record['pypi_downloads'] = None  # filled in by the batched ClickHouse query

    doi = DOI_RE.search(tool['publication'])
    # Parentheses in a DOI are percent-encoded in the link target (Elsevier's
    # 10.1016/S2352-3018(17)30190-X); the APIs want the decoded form.
    record['doi'] = urllib.parse.unquote(doi.group(1)) if doi else None
    record['citations'] = None
    if record['doi']:
        try:
            record['citations'] = citations(record['doi'])
        except (urllib.error.URLError, KeyError, TimeoutError) as exc:
            print(f"    {tool['name']}: Crossref failed ({exc})")
    return record


def main():
    offline = '--offline' in sys.argv
    dry_run = '--dry-run' in sys.argv
    only = [sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == '--only']

    cache = json.loads(CACHE.read_text(encoding='utf-8')) if CACHE.exists() else {}
    manual = json.loads(MANUAL.read_text(encoding='utf-8')) if MANUAL.exists() else {}

    tools = load_rows()
    todo = [t for t in tools if not only or t['name'].lower() in {o.lower() for o in only}]
    if only and not todo:
        print(f'No tool matches {only}')
        return 1
    print(f'{len(tools)} tools; scoring {len(todo)}'
          f"{' from cache (--offline)' if offline else (' (authenticated)' if TOKEN else ' (no GitHub token -- expect rate limiting)')}")

    records = {}
    for i, tool in enumerate(todo, 1):
        record = gather(tool, offline, cache.get(tool['name']))
        # `_`-prefixed keys are the notes explaining each override, not data.
        overrides = {k: v for k, v in (manual.get(tool['name']) or {}).items()
                     if not k.startswith('_')}
        record.update(overrides)  # hand-set values win over fetched ones
        if 'pypi' in overrides:
            record['pypi_match'] = 'manual'
        records[tool['name']] = record
        if not offline:
            time.sleep(0.05)
        if i % 20 == 0:
            print(f'  {i}/{len(todo)}')

    if not offline:
        wanted = {r['pypi'] for r in records.values() if r.get('pypi')}
        try:
            totals = pypi_downloads(wanted)
        except (urllib.error.URLError, KeyError, ValueError, TimeoutError) as exc:
            print(f'  PyPI download query failed ({exc}); keeping cached totals')
            totals = {}
        for name, record in records.items():
            if record.get('pypi'):
                total = totals.get(record['pypi'], totals.get(record['pypi'].lower()))
                record['pypi_downloads'] = total if total is not None else \
                    (cache.get(name, {}).get('pypi_downloads'))

    cells, tally = {}, {'Established': 0, 'Emerging': 0, 'Minimal': 0}
    for name, record in records.items():
        if not record.get('pypi'):
            record['pypi_downloads'] = None
        record['points'] = round(points_for(record), 1)
        record['label'] = label_for(record['points'])
        tally[record['label']] += 1
        cells[name] = compose(record)
        cache[name] = record

    keep = {t['name'] for t in tools}
    cache = {k: v for k, v in cache.items() if k in keep}

    before = {t['name']: t['usage'] for t in tools}
    changes = [(n, before[n], c) for n, c in cells.items() if before.get(n) != c]
    for name, old, new in sorted(changes):
        print(f'  {name}\n    - {old}\n    + {new}')

    print(f'\n{tally["Established"]} established, {tally["Emerging"]} emerging, '
          f'{tally["Minimal"]} minimal; {len(changes)} cells changed')

    weak = sorted(n for n, r in records.items() if r.get('pypi_match') == 'name-only')
    if weak:
        print('PyPI projects matched on name alone -- check these are the same software, '
              'and set "pypi": null in usage_manual.json for any that are not:')
        for name in weak:
            print(f'  {name} -> pypi.org/project/{records[name]["pypi"]}')
    if dry_run:
        print('Nothing written (--dry-run).')
        return 0

    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True) + '\n',
                     encoding='utf-8')
    changed = rewrite_table(cells)
    print(f'Wrote {CACHE.relative_to(ROOT)} and updated {changed} rows of {SOURCE.name}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
