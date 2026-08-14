"""
Find out when each tool in database_tools.md was last updated.

For tools whose Code column points at a source repository this is the date of
the last commit; for tools distributed only as a package it is the date of the
most recent release on PyPI or CRAN; anything we cannot establish is recorded
as unknown and shown as "N/A" in the table.

Writes docs/data/updated.json, a tool name -> {date, source, url} cache that
build_site.py turns into the Updated column. The cache is committed, so
building the site never needs network access; re-run this to refresh it.

GitHub allows only 60 unauthenticated API calls an hour and the database holds
well over a hundred repositories, so a token is used when one is available:
either $GITHUB_TOKEN or, failing that, whatever `gh auth token` returns.

Usage: python docs/fetch_updated.py [--refresh] [--only NAME]
"""

import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from build_site import ROOT, parse_table

DOCS = Path(__file__).parent
CACHE = DOCS / 'data' / 'updated.json'
SOURCE = ROOT / 'database_tools.md'

HEADERS = {'User-Agent': 'gsidd-idd-tools-landscape/1.0 (mailto:info@gsidd.org)'}

GITHUB_RE = re.compile(r'github\.com/([^/)\s#?]+)(?:/([^/)\s#?]+))?', re.I)
GITHUB_PAGES_RE = re.compile(r'^([^.]+)\.github\.io$', re.I)
# forgemia.inra.fr now redirects to forge.inrae.fr, and the redirect lands on an
# error page rather than the API, so the current host has to be named here.
GITLAB_HOSTS = {
    'gitlab.com': 'gitlab.com',
    'gitlab.inria.fr': 'gitlab.inria.fr',
    'forgemia.inra.fr': 'forge.inrae.fr',
    'forge.inrae.fr': 'forge.inrae.fr',
}
CRAN_RE = re.compile(r'cran\.r-project\.org/.*?(?:package=|packages/)([A-Za-z0-9._]+)', re.I)
PYPI_RE = re.compile(r'pypi\.org/project/([A-Za-z0-9._-]+)', re.I)
URL_RE = re.compile(r'\((https?://[^)\s]+)\)')


def github_token():
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if token:
        return token.strip()
    try:
        out = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip() or None


TOKEN = github_token()


def get_json(url, token=None):
    headers = dict(HEADERS)
    if token:
        headers['Authorization'] = 'Bearer ' + token
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def iso_date(value):
    """The date part of any of the timestamp formats these APIs return."""
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', str(value or ''))
    return match.group(0) if match else None


def from_github(owner, repo):
    """Date of the last push, which tracks activity on branches as well as the default one."""
    repo = repo.removesuffix('.git')
    data = get_json(f'https://api.github.com/repos/{owner}/{repo}', TOKEN)
    return iso_date(data.get('pushed_at') or data.get('updated_at'))


def from_github_account(account):
    """
    Newest push across an organisation's repositories, for the few entries whose
    Code column names a GitHub account or Pages site rather than one repository.
    """
    for kind in ('orgs', 'users'):
        try:
            repos = get_json(
                f'https://api.github.com/{kind}/{account}/repos?sort=pushed&per_page=1', TOKEN)
        except urllib.error.HTTPError as exc:
            if exc.code != 404:
                raise
            continue
        if repos:
            return iso_date(repos[0].get('pushed_at'))
    return None


def from_gitlab(host, path):
    project = urllib.parse.quote(path.strip('/'), safe='')
    commits = get_json(f'https://{host}/api/v4/projects/{project}/repository/commits?per_page=1')
    return iso_date(commits[0]['committed_date']) if commits else None


def from_cran(package):
    """CRAN's `Date/Publication` is when the current version reached the archive."""
    data = get_json('https://crandb.r-pkg.org/' + urllib.parse.quote(package))
    return iso_date(data.get('Date/Publication') or data.get('crandb_file_date') or data.get('Packaged'))


def from_pypi(package):
    data = get_json('https://pypi.org/pypi/' + urllib.parse.quote(package) + '/json')
    files = data.get('urls') or []
    if not files:  # a release with no files left; fall back to the newest upload anywhere
        files = [f for release in data.get('releases', {}).values() for f in release]
    dates = [iso_date(f.get('upload_time_iso_8601') or f.get('upload_time')) for f in files]
    dates = [d for d in dates if d]
    return max(dates) if dates else None


def registry_guess(name, language):
    """
    Last resort for a tool with no repository: look for a package of the same
    name on the registry its language implies. Only an exact name match counts,
    since a near-miss would silently report some unrelated package's date.
    """
    lang = language.lower()
    slug = re.sub(r'[^a-z0-9._-]', '-', name.lower()).strip('-')
    if 'python' in lang:
        return from_pypi(slug), f'https://pypi.org/project/{slug}/', 'pypi'
    if re.search(r'\br\b', lang):
        return from_cran(name), f'https://cran.r-project.org/package={name}', 'cran'
    return None, None, None


def resolve(name, code, language):
    """Return (date, source, url); date is None when nothing could be established."""
    match = URL_RE.search(code)
    url = match.group(1) if match else (code.strip() if code.startswith('http') else '')

    gh = GITHUB_RE.search(url)
    if gh and gh.group(2):
        return from_github(gh.group(1), gh.group(2)), 'github', url
    if gh:
        return from_github_account(gh.group(1)), 'github-org', url

    host = urllib.parse.urlparse(url).netloc.lower()
    pages = GITHUB_PAGES_RE.match(host)
    if pages:
        return from_github_account(pages.group(1)), 'github-org', url

    if host in GITLAB_HOSTS:
        path = urllib.parse.urlparse(url).path
        path = re.split(r'/-/', path)[0]  # strip /-/tree/main and friends
        return from_gitlab(GITLAB_HOSTS[host], path), 'gitlab', url

    cran = CRAN_RE.search(url)
    if cran:
        return from_cran(cran.group(1)), 'cran', url

    pypi = PYPI_RE.search(url)
    if pypi:
        return from_pypi(pypi.group(1)), 'pypi', url

    return registry_guess(name, language)


def load_rows():
    lines = SOURCE.read_text(encoding='utf-8').split('\n')
    start = next(i for i, line in enumerate(lines) if re.match(r'^##\s+Tools\s*$', line))
    columns, rows = parse_table(lines, start + 1)
    index = {col: i for i, col in enumerate(columns)}
    return [
        dict(name=row[index['Name']], code=row[index['Code']], language=row[index['Language']])
        for row in rows
    ]


def main():
    refresh = '--refresh' in sys.argv
    only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None

    cache = {} if refresh else (json.loads(CACHE.read_text(encoding='utf-8')) if CACHE.exists() else {})
    tools = load_rows()
    if only:
        tools = [t for t in tools if t['name'].lower() == only.lower()]
    todo = [t for t in tools if only or t['name'] not in cache]
    print(f'{len(tools)} tools; {len(todo)} to fetch'
          f"{' (authenticated)' if TOKEN else ' (no GitHub token -- expect rate limiting)'}")

    unknown = []
    for i, tool in enumerate(todo, 1):
        name = tool['name']
        try:
            date, source, url = resolve(name, tool['code'], tool['language'])
        except (urllib.error.URLError, KeyError, IndexError, ValueError, TimeoutError) as exc:
            date, source, url = None, None, None
            print(f'  [{i}/{len(todo)}] {name} -> FAILED: {exc}')
        if date:
            cache[name] = dict(date=date, source=source, url=url)
            print(f'  [{i}/{len(todo)}] {name} -> {date} ({source})')
        else:
            cache.pop(name, None)
            unknown.append(name)
        time.sleep(0.05)

    keep = {t['name'] for t in load_rows()}
    resolved = {k: v for k, v in cache.items() if k in keep}
    CACHE.write_text(json.dumps(resolved, ensure_ascii=False, indent=1, sort_keys=True) + '\n',
                     encoding='utf-8')
    print(f'\nWrote {CACHE.relative_to(ROOT)}: {len(resolved)}/{len(keep)} dates resolved')
    if unknown:
        print('No date found (shown as N/A):')
        for name in unknown:
            print(f'  {name}')


if __name__ == '__main__':
    main()
