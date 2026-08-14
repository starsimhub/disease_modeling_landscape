"""
Discovery sweep for IDD software tools the database may be missing.

Queries Crossref (corpus-wide and restricted to software venues), GitHub repository
search, and the CRAN Epidemiology Task View, then drops hits that already match a
name in database_tools.md or excluded_tools.md. What comes out is a triage list, not
an answer: every candidate still has to be vetted by hand against
references/criteria.md.

Usage:
    python discover.py                                  # all axes, all sources
    python discover.py --axis estimation --source crossref
    python discover.py --since 2024 --out /tmp/candidates.tsv
    python discover.py --full                           # keep already-known hits too
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import axes

ROOT = Path(__file__).resolve().parents[4]
HEADERS = {'User-Agent': 'gsidd-idd-tools-landscape/1.0 (mailto:info@gsidd.org)'}
TIMEOUT = 30


def fetch_json(url):
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return json.load(response)
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, TimeoutError) as error:
        print(f'  ! {type(error).__name__} on {url[:90]}', file=sys.stderr)
        return None


def known_names():
    """Every tool name already decided about, included or excluded."""
    names = set()

    tools = (ROOT / 'database_tools.md').read_text(encoding='utf-8')
    for line in tools.split('\n'):
        if line.startswith('| ') and line.count('|') > 8:
            name = line.strip().strip('|').split('|')[0].strip()
            if name and name != 'Name' and not set(name) <= set('- '):
                names.update(part.strip() for part in name.split('/'))

    excluded = (ROOT / 'excluded_tools.md').read_text(encoding='utf-8')
    for match in re.finditer(r'^- \*\*(.+?)\*\*', excluded, re.M):
        names.update(part.strip() for part in match.group(1).split('/'))

    # Short names generate too many false "already known" matches to be useful as filters.
    return {n for n in names if len(n) > 3}


def matches_known(text, known):
    lowered = text.lower()
    return sorted(n for n in known if re.search(rf'\b{re.escape(n.lower())}\b', lowered))


def venue_matches(venue, container):
    """Loose enough to survive 'PLoS'/'PLOS' and subtitle drift, strict enough to reject other journals."""
    if not container:
        return False
    stop = {'of', 'the', 'and', 'in', 'for'}
    tokens = {word for word in re.findall(r'[a-z]+', venue.lower()) if word not in stop}
    container_tokens = set(re.findall(r'[a-z]+', container.lower()))
    return bool(tokens) and tokens <= container_tokens


def crossref(subject, software, venue=None, since=None, rows=20):
    query = urllib.parse.quote(f'{subject} {software}')
    url = f'https://api.crossref.org/works?query.bibliographic={query}&rows={rows}&select=DOI,title,container-title,published'
    if venue:
        url += '&query.container-title=' + urllib.parse.quote(venue)
    if since:
        url += f'&filter=from-pub-date:{since}-01-01'
    data = fetch_json(url)
    if not data:
        return []

    hits = []
    for item in data['message']['items']:
        title = (item.get('title') or [''])[0]
        if not title:
            continue
        container = (item.get('container-title') or [''])[0]
        # query.container-title is a ranking boost, not a filter, so a venue-restricted query
        # still returns unrelated journals. Drop those rather than making them someone's triage.
        if venue and not venue_matches(venue, container):
            continue
        year = (item.get('published', {}).get('date-parts') or [['']])[0][0]
        hits.append({'source': f'crossref:{venue or "all"}', 'name': title,
                     'detail': f'{container} {year}'.strip(), 'url': 'https://doi.org/' + item['DOI'],
                     'query': f'{subject} × {software}'})
    return hits


def github_search(query, sort='stars'):
    encoded = urllib.parse.quote(query)
    path = f'search/repositories?q={encoded}&sort={sort}&order=desc&per_page=25'
    try:
        result = subprocess.run(['gh', 'api', path], capture_output=True, text=True, timeout=TIMEOUT)
        data = json.loads(result.stdout) if result.returncode == 0 else None
    except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError):
        data = None
    if data is None:
        # Unauthenticated fallback: 60 calls/hour, so this will run dry on a full sweep.
        data = fetch_json(f'https://api.github.com/{path}')
    if not data or 'items' not in data:
        return []

    hits = []
    for item in data['items']:
        stars = item['stargazers_count']
        if stars < 10:  # below ~10 stars, results are almost entirely coursework
            continue
        hits.append({'source': 'github', 'name': item['full_name'],
                     'detail': f'★{stars} {item["pushed_at"][:10]} {(item.get("description") or "")[:70]}',
                     'url': item['html_url'], 'query': query})
    return hits


def cran_task_view():
    request = urllib.request.Request(axes.CRAN_TASK_VIEW, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            html = response.read().decode('utf-8', 'replace')
    except (urllib.error.URLError, TimeoutError) as error:
        print(f'  ! {error} on the CRAN task view', file=sys.stderr)
        return []

    packages = sorted(set(re.findall(r'/package=([A-Za-z][A-Za-z0-9._]+)', html)))
    return [{'source': 'cran-taskview', 'name': package, 'detail': 'CRAN Epidemiology Task View',
             'url': f'https://cran.r-project.org/package={package}', 'query': 'task view'}
            for package in packages]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--axis', action='append', choices=sorted(axes.AXES), help='axis to run (repeatable; default all)')
    parser.add_argument('--source', action='append', choices=['crossref', 'github', 'cran'], help='source to query (default all)')
    parser.add_argument('--since', help='earliest Crossref publication year, e.g. 2024')
    parser.add_argument('--out', default='/tmp/idd_candidates.tsv')
    parser.add_argument('--full', action='store_true', help='keep hits that already match a known name')
    parser.add_argument('--max-queries', type=int, default=60, help='cap on Crossref queries per axis')
    args = parser.parse_args()

    selected_axes = args.axis or sorted(axes.AXES)
    sources = args.source or ['crossref', 'github', 'cran']
    known = known_names()
    print(f'{len(known)} names already decided about (included or excluded)\n')

    hits = []

    if 'crossref' in sources:
        jobs = []
        for axis_name in selected_axes:
            axis = axes.AXES[axis_name]
            # Corpus-wide across the full cross product, then a narrower cross product per venue:
            # the venue-restricted queries are what surface software papers specifically.
            for subject in axis['subject']:
                for software in axis['software'][:3]:
                    jobs.append((subject, software, None))
                for venue in axes.VENUES:
                    jobs.append((subject, axis['software'][0], venue))
        jobs = jobs[:args.max_queries * len(selected_axes)]
        print(f'crossref: {len(jobs)} queries')
        with ThreadPoolExecutor(max_workers=6) as pool:
            for result in pool.map(lambda job: crossref(*job, since=args.since), jobs):
                hits.extend(result)

    if 'github' in sources:
        queries = [f'topic:{topic}' for topic in axes.GITHUB_TOPICS] + axes.GITHUB_KEYWORDS
        if 'ai' in selected_axes:
            queries += axes.GITHUB_AI_KEYWORDS
        print(f'github: {len(queries)} queries')
        for query in queries:
            hits.extend(github_search(query))

    if 'cran' in sources:
        print('cran: task view')
        hits.extend(cran_task_view())

    # Deduplicate on url, then annotate with whether we already know about it.
    seen, rows = set(), []
    for hit in hits:
        if hit['url'] in seen:
            continue
        seen.add(hit['url'])
        hit['known'] = ','.join(matches_known(hit['name'], known))
        if hit['known'] and not args.full:
            continue
        rows.append(hit)

    rows.sort(key=lambda hit: (hit['source'], hit['name'].lower()))
    out = Path(args.out)
    with out.open('w', encoding='utf-8') as handle:
        handle.write('source\tname\tdetail\turl\tmatched_known\tquery\n')
        for hit in rows:
            handle.write('\t'.join([hit['source'], hit['name'].replace('\t', ' '),
                                    hit['detail'].replace('\t', ' '), hit['url'],
                                    hit['known'], hit['query']]) + '\n')

    print(f'\n{len(hits)} hits, {len(rows)} after dedupe'
          f'{"" if args.full else " and removing already-known names"} -> {out}')
    print('Triage by hand: discard replication code, coursework, general-purpose statistics,')
    print('datasets and training material. Then vet survivors against references/criteria.md.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
