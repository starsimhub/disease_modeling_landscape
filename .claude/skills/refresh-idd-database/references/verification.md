# Verification recipes

Nothing in these files is recalled. Every count, date, licence and URL was checked against a primary source on the snapshot date. `scripts/verify.py` automates most of this; the raw recipes are here for the cases it does not cover.

## GitHub

```bash
gh api repos/OWNER/REPO --jq '{full_name,description,stargazers_count,forks_count,pushed_at,archived,license:.license.spdx_id}'
gh api repos/OWNER/REPO/license --jq '.license.spdx_id'
gh api "orgs/ORG/repos?sort=pushed&per_page=30" --jq '.[] | "\(.full_name)\t\(.pushed_at[0:10])\t★\(.stargazers_count)\t\(if .archived then "ARCHIVED" else "" end)"'
gh api "search/repositories?q=topic:epidemiology&sort=stars&per_page=25" --jq '.items[] | "★\(.stargazers_count)\t\(.full_name)\t\(.description)"'
```

Unauthenticated `api.github.com` allows 60 calls/hour and the database holds well over a hundred repos, so use `gh` (or `$GITHUB_TOKEN`). If the API reports the licence as `NOASSERTION`, `NONE`, or anything unfamiliar, **read the file**:

```bash
curl -s "https://raw.githubusercontent.com/OWNER/REPO/main/LICENSE" | head -20   # also try master, HEAD
```

This is the only way FRED's Pittsburgh EULA and Episimmer's Commons Clause were caught.

## CRAN

```bash
curl -s "https://crandb.r-pkg.org/PKG" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('Title'),'|',d.get('Version'),'|',d.get('Date/Publication'),'|',d.get('License'))"
curl -s "https://cranlogs.r-pkg.org/downloads/total/2000-01-01:$(date +%F)/PKG"
curl -s "https://raw.githubusercontent.com/OWNER/REPO/main/DESCRIPTION" | grep -iE '^(Package|Title|Version|License|URL)'
```

The `DESCRIPTION` `License:` field is authoritative over the GitHub API for R packages.

## PyPI

```bash
curl -s "https://pypi.org/pypi/PKG/json" | python3 -c "import json,sys; d=json.load(sys.stdin)['info']; print(d['version'],'|',d.get('license'),'|',d['home_page'])"
curl -s "https://pypistats.org/api/packages/PKG/recent"
```

PyPI publishes no lifetime totals of its own and pypistats serves only the last 180 days, which undercounts a long-lived package against CRAN's all-time figure. Use the public ClickHouse mirror instead — no key, and many projects in one query:

```bash
curl -s 'https://sql-clickhouse.clickhouse.com/?user=demo&default_format=JSON' \
  --data-binary "SELECT project, sum(count) AS total FROM pypi.pypi_downloads WHERE project IN ('covasim','starsim') GROUP BY project"
```

Check the project is the tool's own before counting it: PyPI holds unrelated packages whose names collide with a tool's (`civet` is a Django asset precompiler, `TreeTime` a to-do list manager, `optima` a PyTorch optimiser, `pangolin` a probabilistic inference library). `docs/fetch_usage.py` accepts a guessed name only when the package metadata links back to the tool's repository, and prints the name-only matches for review; rejections and corrections live in `docs/data/usage_manual.json`.

## Usage scores

Do not re-derive the `Usage` column by hand — it is computed:

```bash
python docs/fetch_usage.py --dry-run     # what would change
python docs/fetch_usage.py               # rewrite the column, refresh docs/data/usage.json
python docs/fetch_usage.py --only Naomi  # one tool
```

It fetches stars and forks, all-time CRAN (cranlogs) and PyPI (ClickHouse) downloads, citations (OpenAlex, then Crossref) and country counts read out of the cell's own prose, converts them to points at the rates in `references/criteria.md`, and writes `Label (evidence)` back into `database_tools.md`. `docs/data/usage.json` is the audit trail: every input behind every label, committed.

Citation counts: OpenAlex is the primary source because Crossref's `is-referenced-by-count` does not cover the arXiv and bioRxiv DOIs several entries use.

```bash
curl -s "https://api.openalex.org/works/doi:10.1371/journal.pcbi.1009149?mailto=cliff.kerr@gatesfoundation.org" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['cited_by_count'],'|',d['title'])"
```

Percent-encoded parentheses in a DOI link target (`10.1016/S2352-3018%2817%2930190-X`) must be decoded before either API will resolve them; that one silently returned zero citations until it was fixed.

## Crossref

```bash
curl -s "https://api.crossref.org/works/10.xxxx/yyyy" | python3 -c "import json,sys; m=json.load(sys.stdin)['message']; print(m['DOI'],'|',m['title'][0],'|',(m.get('container-title') or [''])[0])"
curl -s "https://api.crossref.org/works?query.bibliographic=URLENCODED+TITLE&rows=3&select=DOI,title,container-title,published"
```

Send `User-Agent: lit-review/1.0 (mailto:cliff.kerr@gatesfoundation.org)` for the polite pool. **Always resolve the DOI you are about to write** — three of the past errors were invented or mistyped DOIs, and one was a Markdown escaping bug that broke the HIV Synthesis link (parentheses in DOIs such as `10.1016/S2352-3018(17)30190-X` need care inside Markdown link targets).

## URL sweep

`scripts/check_urls.py` does this over every `.md` file; the equivalent one-liner:

```bash
grep -ohE 'https?://[^)" ]+' *.md | sed 's/[.,]$//' | sort -u |
  xargs -P 16 -I{} sh -c 'c=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 15 "{}"); case "$c" in 200|202|403|405|406|429) ;; *) echo "$c  {}";; esac'
```

Treat 403/202/405/406/429 as pass — publisher anti-bot responses from OUP, Wiley, Royal Society, IEEE and JMIR are routine, and `cdc.gov` and `lshtm.ac.uk` return 403 to any scripted request regardless of headers (the tables use `insightnet.us` and `cmmid.github.io` instead). Distinguish blocked from dead with DNS:

```bash
getent hosts DOMAIN || echo NXDOMAIN
```

NXDOMAIN is real death, and it has happened: CEPAC's `mgh-mpec.org`, OMNI-RÉUNIS's `omni-reunis.ca`, `icovid.cl`. Watch for lapsed-and-reregistered domains — `icovidchile.cl` now 301s to an online casino, which is definitive evidence a project is defunct.

## Structural checks

`python docs/build.py --check` validates cell counts per row, case-insensitive alphabetical ordering, duplicate names, DOI formatting in the `Publication` column, and that each file's prose count sentence matches its row count. It exits non-zero on any problem, which stops the build.

Two things it will not catch:

- **Locale collation.** Compare orderings with `LC_ALL=C sort -f`; a plain `sort` disagrees with the checker on punctuation and produces phantom ordering errors.
- **Hard-wrapped prose.** Check that no paragraph, list item or table row has been broken across physical lines.

## Sanity checks worth running after a large edit

- Every ecosystem row has a matching `### Name` detail section, and vice versa.
- Names in `database_tools.md` and `excluded_tools.md` are disjoint.
- Component tools named in `database_ecosystems.md` exist as rows in `database_tools.md` (or their absence is deliberate and stated).
- The three files' snapshot dates agree with what was actually re-checked.
