"""
Resolve the publication DOIs in database_tools.md to titles, via Crossref.

Writes docs/data/publications.json, a DOI -> {title, journal, year} cache that
build_site.py merges into the Publication column so the table shows what the
paper is called rather than an opaque DOI string. The cache is committed, so
building the site never needs network access; re-run this only when new
publications are added.

Usage: python docs/fetch_publications.py [--refresh]
"""

import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

DOCS = Path(__file__).parent
ROOT = DOCS.parent
CACHE = DOCS / 'data' / 'publications.json'

# Crossref asks that scripts identify themselves; this puts us in the polite pool.
MAILTO = 'info@gsidd.org'
HEADERS = {'User-Agent': f'gsidd-idd-tools-landscape/1.0 (mailto:{MAILTO})'}
DOI_RE = re.compile(r'\((https://doi\.org/(10\.[^)]+))\)')

# A few publishers pretty-print JATS markup inside the title, so the newlines that
# separate the tags are indistinguishable from real word spaces once the tags are
# stripped: `MGD<scp>riv</scp>E` should close up to "MGDrivE", but `in <scp>r</scp>`
# must keep its space. Rather than guess, the handful of affected titles are stated.
OVERRIDES = {
    '10.1098/rsos.210506':
        'June: open-source individual-based epidemiology simulation',
    '10.1111/2041-210X.13318':
        'MGDrivE: A modular simulation framework for the spread of gene drives through '
        'spatially explicit mosquito populations',
    '10.1111/2041-210X.13422':
        'nosoi: A stochastic agent-based transmission chain simulation framework in R',
}


def collect_dois():
    text = (ROOT / 'database_tools.md').read_text(encoding='utf-8')
    return sorted({m.group(2) for m in DOI_RE.finditer(text)})


def clean(title):
    """Crossref and DataCite return titles with markup, entities and wrapped whitespace."""
    text = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', title))).strip()
    # stripping a tag before punctuation leaves a stray space: "AMR : An R Package"
    return re.sub(r'\s+([:;,.])', r'\1', text)


def get_json(url):
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def from_crossref(doi):
    message = get_json('https://api.crossref.org/works/' + urllib.parse.quote(doi) +
                       '?mailto=' + MAILTO)['message']
    issued = message.get('issued', {}).get('date-parts', [[None]])[0]

    # Crossref often splits a title at the colon, holding the rest as a subtitle;
    # taking only `title` truncates entries such as "Optima" for the Optima HIV paper.
    title = clean((message.get('title') or [''])[0])
    subtitle = clean((message.get('subtitle') or [''])[0])
    if subtitle and subtitle.lower() not in title.lower():
        title = title.rstrip(': ') + ': ' + subtitle

    return {
        'title': title,
        'journal': clean((message.get('container-title') or [''])[0]),
        'year': issued[0] if issued and issued[0] else None,
    }


def from_datacite(doi):
    """Fallback for DOIs not registered with Crossref, notably arXiv preprints."""
    attrs = get_json('https://api.datacite.org/dois/' + urllib.parse.quote(doi))['data']['attributes']
    return {
        'title': clean((attrs.get('titles') or [{}])[0].get('title', '')),
        'journal': clean(((attrs.get('container') or {}).get('title') or
                          (attrs.get('publisher') if isinstance(attrs.get('publisher'), str) else '') or '')),
        'year': attrs.get('publicationYear'),
    }


def fetch(doi):
    # DOIs are captured from URLs, so parentheses arrive percent-encoded.
    decoded = urllib.parse.unquote(doi)
    try:
        record = from_crossref(decoded)
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise
        record = from_datacite(decoded)
    if decoded in OVERRIDES:
        record['title'] = OVERRIDES[decoded]
    if not record['title']:
        raise ValueError('no title in metadata')
    return record


def main():
    refresh = '--refresh' in sys.argv
    cache = {} if refresh else (json.loads(CACHE.read_text(encoding='utf-8')) if CACHE.exists() else {})
    dois = collect_dois()
    todo = [d for d in dois if d not in cache]
    print(f'{len(dois)} DOIs; {len(todo)} to fetch')

    failures = []
    for i, doi in enumerate(todo, 1):
        try:
            cache[doi] = fetch(doi)
            print(f'  [{i}/{len(todo)}] {doi} -> {cache[doi]["title"][:70]}')
        except (urllib.error.URLError, KeyError, IndexError, ValueError) as exc:
            failures.append((doi, str(exc)))
            print(f'  [{i}/{len(todo)}] {doi} -> FAILED: {exc}')
        time.sleep(0.15)

    resolved = {k: v for k, v in cache.items() if k in dois and v.get('title')}
    CACHE.write_text(json.dumps(resolved, ensure_ascii=False, indent=1, sort_keys=True) + '\n',
                     encoding='utf-8')
    print(f'\nWrote {CACHE.relative_to(ROOT)}: {len(resolved)}/{len(dois)} titles resolved')
    if failures:
        print('Unresolved (the DOI will be shown as-is):')
        for doi, exc in failures:
            print(f'  {doi}: {exc}')


if __name__ == '__main__':
    main()
