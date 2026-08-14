"""
Check that every URL in the Markdown data files still resolves.

Publisher anti-bot responses are routine and are not failures: OUP, Wiley, the Royal
Society, IEEE and JMIR return 403 to scripted requests, as do cdc.gov and lshtm.ac.uk.
What matters is telling *blocked* apart from *dead*, so anything that does not pass is
re-checked in DNS -- NXDOMAIN is real death, and has happened to tools in this database.

Usage:
    python check_urls.py                       # every tracked .md file
    python check_urls.py database_tools.md
    python check_urls.py --new                 # only URLs added in the working tree
"""

import argparse
import re
import socket
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
URL_RE = re.compile(r'https?://[^)"\s>]+')
HEADERS = {'User-Agent': 'Mozilla/5.0 (compatible; gsidd-idd-tools-landscape/1.0)'}
# 403/405/406/429 are anti-bot; 202 is a queued redirect at some publishers.
ACCEPTABLE = {200, 202, 301, 302, 403, 405, 406, 429}


def collect(paths):
    urls = set()
    for path in paths:
        for match in URL_RE.finditer(path.read_text(encoding='utf-8')):
            urls.add(match.group(0).rstrip('.,;:'))
    return sorted(urls)


def collect_new():
    diff = subprocess.run(['git', '-C', str(ROOT), 'diff', '-U0'], capture_output=True, text=True)
    added = '\n'.join(line for line in diff.stdout.split('\n') if line.startswith('+'))
    return sorted({match.group(0).rstrip('.,;:') for match in URL_RE.finditer(added)})


def status(url):
    request = urllib.request.Request(url, headers=HEADERS, method='GET')
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code
    except (urllib.error.URLError, TimeoutError, socket.timeout, ValueError, ConnectionError):
        return 0


def dns_ok(url):
    host = urllib.parse.urlparse(url).hostname
    try:
        socket.getaddrinfo(host, None)
        return True
    except (socket.gaierror, UnicodeError, TypeError):
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('files', nargs='*', help='Markdown files (default: every .md in the repo root)')
    parser.add_argument('--new', action='store_true', help='only URLs added in the working tree')
    args = parser.parse_args()

    if args.new:
        urls = collect_new()
    else:
        paths = [ROOT / name for name in args.files] if args.files else sorted(ROOT.glob('*.md'))
        urls = collect(paths)
    print(f'{len(urls)} unique URLs to check\n')

    failures = []
    with ThreadPoolExecutor(max_workers=16) as pool:
        for url, code in zip(urls, pool.map(status, urls)):
            if code not in ACCEPTABLE:
                failures.append((url, code))

    if not failures:
        print('All URLs resolve.')
        return 0

    print(f'{len(failures)} to look at:\n')
    for url, code in sorted(failures, key=lambda pair: pair[1]):
        verdict = 'DNS ok -- blocked, moved, or transient' if dns_ok(url) else 'NXDOMAIN -- domain is gone'
        print(f'  {code or "conn":>4}  {url}\n        {verdict}')
    print('\nA dead link in a row you authored is a bug; replace it with a verified location or a '
          'publication link, and say so in the report.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
