"""
Check a candidate tool -- or every tool already in the database -- against primary sources.

Reports GitHub stars/forks/pushed_at/archived, the licence from both the API and the raw
LICENSE or DESCRIPTION file, CRAN and PyPI release dates and download totals, and Crossref
matches for a title. Then prints a per-criterion verdict. Criterion 3 (documented) is left
as a manual judgement, because it is one.

Usage:
    python verify.py --name Naomi --repo mrc-ide/naomi
    python verify.py --name serofoi --repo epiverse-trace/serofoi --cran serofoi
    python verify.py --doi-for "Naomi: a new modelling tool for estimating HIV epidemic indicators"
    python verify.py --from-database              # re-check every row in database_tools.md
    python verify.py --from-database --only Starsim
"""

import argparse
import datetime
import json
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HEADERS = {'User-Agent': 'gsidd-idd-tools-landscape/1.0 (mailto:info@gsidd.org)'}
TIMEOUT = 30
TODAY = datetime.date.today()
SUPPORT_CUTOFF = (TODAY - datetime.timedelta(days=3 * 365)).isoformat()

GITHUB_RE = re.compile(r'github\.com/([^/)\s#?]+)/([^/)\s#?]+)', re.I)
CRAN_RE = re.compile(r'cran\.r-project\.org/package=([A-Za-z][A-Za-z0-9._]+)', re.I)
# Licences the GitHub API reports but cannot be trusted on; read the file instead.
VAGUE = {'NOASSERTION', 'NONE', 'other', None, ''}


def fetch_text(url):
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return response.read().decode('utf-8', 'replace')
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
        return None


def fetch_json(url):
    text = fetch_text(url)
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def gh_api(path):
    """Prefer the gh CLI: unauthenticated GitHub allows only 60 calls an hour."""
    try:
        result = subprocess.run(['gh', 'api', path], capture_output=True, text=True, timeout=TIMEOUT)
        if result.returncode == 0:
            return json.loads(result.stdout)
    except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError):
        pass
    return fetch_json(f'https://api.github.com/{path}')


def raw_file(repo, filename):
    for branch in ('main', 'master', 'HEAD'):
        text = fetch_text(f'https://raw.githubusercontent.com/{repo}/{branch}/{filename}')
        if text:
            return text
    return None


def check_github(repo):
    data = gh_api(f'repos/{repo}')
    if not data or 'full_name' not in data:
        return {'error': f'{repo}: no such repository (or API refused)'}

    api_licence = (data.get('license') or {}).get('spdx_id')
    info = {
        'repo': data['full_name'],
        'stars': data['stargazers_count'],
        'forks': data['forks_count'],
        'pushed': data['pushed_at'][:10],
        'archived': data['archived'],
        'api_licence': api_licence,
    }

    # The two non-open licences hiding behind public repos (FRED, Episimmer) were only ever
    # caught by reading the file, so read it whenever the API is unhelpful.
    if api_licence in VAGUE:
        text = raw_file(repo, 'LICENSE') or raw_file(repo, 'LICENSE.md') or raw_file(repo, 'COPYING')
        info['licence_file'] = ' '.join(text.split())[:200] if text else 'no LICENSE file found'

    description = raw_file(repo, 'DESCRIPTION')
    if description:
        match = re.search(r'^License:\s*(.+)$', description, re.M)
        if match:
            info['description_licence'] = match.group(1).strip()

    citation = raw_file(repo, 'CITATION.cff')
    if citation:
        doi = re.search(r'doi:\s*"?([^\s"]+)', citation)
        if doi:
            info['citation_cff_doi'] = doi.group(1)
    return info


def check_cran(package):
    data = fetch_json(f'https://crandb.r-pkg.org/{urllib.parse.quote(package)}')
    if not data or 'Package' not in data:
        return {'error': f'{package}: not on CRAN'}
    info = {'version': data.get('Version'), 'released': (data.get('Date/Publication') or '')[:10],
            'licence': data.get('License')}
    totals = fetch_json(f'https://cranlogs.r-pkg.org/downloads/total/2000-01-01:{TODAY}/{package}')
    if totals:
        info['downloads_total'] = totals[0].get('downloads')
    return info


def check_pypi(package):
    data = fetch_json(f'https://pypi.org/pypi/{urllib.parse.quote(package)}/json')
    if not data:
        return {'error': f'{package}: not on PyPI'}
    version = data['info']['version']
    uploads = data['releases'].get(version) or []
    info = {'version': version, 'licence': data['info'].get('license') or '—',
            'released': (uploads[0]['upload_time'][:10] if uploads else '?')}
    recent = fetch_json(f'https://pypistats.org/api/packages/{package}/recent')
    if recent:
        info['downloads_last_month'] = recent['data'].get('last_month')
    return info


def crossref_search(title, rows=3):
    query = urllib.parse.quote(title)
    data = fetch_json(f'https://api.crossref.org/works?query.bibliographic={query}'
                      f'&rows={rows}&select=DOI,title,container-title,published')
    if not data:
        return []
    out = []
    for item in data['message']['items']:
        year = (item.get('published', {}).get('date-parts') or [['']])[0][0]
        out.append({'doi': item['DOI'], 'title': (item.get('title') or [''])[0],
                    'venue': (item.get('container-title') or [''])[0], 'year': year})
    return out


def verdict(github, cran, pypi):
    """Mechanical criteria only. 2 is a search result, not a proof; 3 is not mechanisable."""
    lines = []

    licences = [github.get('api_licence'), github.get('description_licence'), (cran or {}).get('licence'),
                (pypi or {}).get('licence')]
    stated = [licence for licence in licences if licence and licence not in VAGUE]
    if 'licence_file' in github:
        lines.append(f'(1) licence: API unhelpful -- READ THIS: {github["licence_file"][:120]}')
    elif stated:
        lines.append(f'(1) licence: {stated[0]} -- closed-source tools are included and labelled, '
                     'so this only disqualifies if the tool cannot be obtained at all')
    else:
        lines.append('(1) licence: not determined -- check by hand')

    lines.append('(3) documented: MANUAL -- needs install instructions, a getting-started example, '
                 'and a technical reference')

    evidence = []
    if github.get('stars') is not None:
        evidence.append(f'{github["stars"]}★/{github["forks"]} forks')
    if (cran or {}).get('downloads_total'):
        evidence.append(f'CRAN {cran["downloads_total"]:,}')
    if (pypi or {}).get('downloads_last_month'):
        evidence.append(f'PyPI {pypi["downloads_last_month"]:,}/month')
    lines.append(f'(4) use: {", ".join(evidence) or "none found"} -- assess cumulatively with '
                 'publication and any documented programme adoption; there is no star threshold')

    dates = [github.get('pushed'), (cran or {}).get('released'), (pypi or {}).get('released')]
    latest = max([date for date in dates if date] or [''])
    if github.get('archived'):
        lines.append('(5) supported: repository ARCHIVED -- check the org for a successor monorepo '
                     'before concluding it is dead (cf. ihmeuw/vivarium -> vivarium-suite)')
    elif latest >= SUPPORT_CUTOFF:
        lines.append(f'(5) supported: PASS, last activity {latest} (cutoff {SUPPORT_CUTOFF})')
    elif latest:
        lines.append(f'(5) supported: FAIL, last activity {latest} (cutoff {SUPPORT_CUTOFF})')
    else:
        lines.append('(5) supported: no activity date found')

    lines.append('A maintainer statement overrides commit activity in both directions.')
    return lines


def report(name, repo=None, cran=None, pypi=None, title=None):
    print(f'\n=== {name} ' + '=' * max(0, 60 - len(name)))
    github_info, cran_info, pypi_info = {}, None, None
    if repo:
        github_info = check_github(repo)
        for key, value in github_info.items():
            print(f'  github.{key:20} {value}')
    if cran:
        cran_info = check_cran(cran)
        for key, value in cran_info.items():
            print(f'  cran.{key:22} {value}')
    if pypi:
        pypi_info = check_pypi(pypi)
        for key, value in pypi_info.items():
            print(f'  pypi.{key:22} {value}')
    if title:
        for hit in crossref_search(title):
            print(f'  crossref  {hit["doi"]}  {hit["venue"]} {hit["year"]}  {hit["title"][:70]}')
    print()
    for line in verdict(github_info, cran_info, pypi_info):
        print(f'  {line}')


def database_rows():
    lines = (ROOT / 'database_tools.md').read_text(encoding='utf-8').split('\n')
    start = next(i for i, line in enumerate(lines) if line.startswith('| Name | Type |'))
    columns = [cell.strip() for cell in lines[start].strip().strip('|').split('|')]
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith('| '):
            break
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        rows.append(dict(zip(columns, cells)))
    return rows


def from_database(only=None):
    rows = [row for row in database_rows() if not only or only.lower() in row['Name'].lower()]
    print(f'{len(rows)} rows to re-check\n')
    print(f'{"Name":<26} {"stars":>6} {"forks":>6} {"pushed":<11} {"licence":<18} note')

    def check(row):
        code = row.get('Code', '')
        repo_match, cran_match = GITHUB_RE.search(code), CRAN_RE.search(code)
        if repo_match:
            info = check_github(f'{repo_match.group(1)}/{repo_match.group(2)}')
            note = 'ARCHIVED' if info.get('archived') else ''
            if info.get('pushed', '9') < SUPPORT_CUTOFF:
                note = (note + ' STALE').strip()
            if 'licence_file' in info:
                note = (note + ' READ-LICENCE').strip()
            return (row['Name'], info.get('stars', '?'), info.get('forks', '?'),
                    info.get('pushed', '?'), str(info.get('api_licence') or '?'),
                    note or info.get('error', ''))
        if cran_match:
            info = check_cran(cran_match.group(1))
            note = 'STALE' if (info.get('released') or '9') < SUPPORT_CUTOFF else ''
            return (row['Name'], '-', '-', info.get('released', '?'),
                    str(info.get('licence') or '?'),
                    f'CRAN {info.get("downloads_total", "?")} {note}'.strip())
        return (row['Name'], '-', '-', '-', '-', 'no repo/CRAN link -- check by hand')

    with ThreadPoolExecutor(max_workers=6) as pool:
        for name, stars, forks, pushed, licence, note in pool.map(check, rows):
            print(f'{name[:26]:<26} {stars:>6} {forks:>6} {pushed:<11} {licence[:18]:<18} {note}')

    print('\nSTALE = no activity within 3 years; READ-LICENCE = API licence unreliable, read the file.')
    print('The Usage column is generated: run `python docs/fetch_usage.py` rather than editing it.')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--name', default='candidate')
    parser.add_argument('--repo', help='owner/repo on GitHub')
    parser.add_argument('--cran', help='CRAN package name')
    parser.add_argument('--pypi', help='PyPI package name')
    parser.add_argument('--title', help='paper title to look up on Crossref')
    parser.add_argument('--doi-for', dest='doi_for', help='Crossref lookup only, no other checks')
    parser.add_argument('--from-database', action='store_true', help='re-check every row of database_tools.md')
    parser.add_argument('--only', help='with --from-database, restrict to names containing this')
    args = parser.parse_args()

    if args.doi_for:
        for hit in crossref_search(args.doi_for, rows=5):
            print(f'{hit["doi"]}  {hit["venue"]} {hit["year"]}  {hit["title"][:90]}')
        return 0
    if args.from_database:
        from_database(args.only)
        return 0
    if not any([args.repo, args.cran, args.pypi, args.title]):
        parser.error('give at least one of --repo, --cran, --pypi, --title, --doi-for, --from-database')

    report(args.name, args.repo, args.cran, args.pypi, args.title)
    return 0


if __name__ == '__main__':
    sys.exit(main())
