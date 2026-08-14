# Prototype website

A static illustration of what the GSIDD "IDD tools" section could look like, built from the `database_*.md` files in the repository root. It is a design mock-up for discussion, not a production site: styling follows [gsidd.org/idd-orgs](https://www.gsidd.org/idd-orgs) loosely (navy/orange palette, Spinnaker display type), and the top navigation bar is inert.

## Contents

| Path | What it is |
|---|---|
| `index.html` | The whole site — one page, three tabs |
| `assets/style.css` | Styling |
| `assets/app.js` | Table browser: filtering, sorting, column visibility, detail drawer, CSV export |
| `data/data.js` | Generated data; do not edit by hand |
| `data/publications.json` | Cached DOI → title/journal/year lookups |
| `data/updated.json` | Cached tool → last-updated date, and where it came from |
| `data/usage.json` | Cached tool → usage metrics, points and label; the audit trail for the `Usage` column |
| `data/usage_manual.json` | Hand-set usage values that the fetcher must not overwrite |
| `build.py` | The one command to run: checks, fetches, builds |
| `build_site.py` | Regenerates `data/data.js` from the markdown databases |
| `fetch_publications.py` | Refreshes `data/publications.json` from Crossref |
| `fetch_updated.py` | Refreshes `data/updated.json` from GitHub, GitLab, PyPI and CRAN |
| `fetch_usage.py` | Re-scores the `Usage` column of `database_tools.md` and refreshes `data/usage.json` |

## Rebuilding after editing the databases

```bash
python docs/build.py
```

That is the whole pipeline, in three stages.

1. **Check.** Every table is parsed and tested: cell counts match the header, names are unique and in case-insensitive alphabetical order, each `Publication` cell is a DOI link or `—`, each `Usage` cell starts with `Established`, `Emerging` or `Minimal`, and the count stated in the prose ("137 tools, sorted alphabetically…") matches the number of rows. Any failure stops the build, so a malformed table cannot be published silently.
2. **Fetch.** Every DOI in `database_tools.md` not already in `data/publications.json` is resolved against Crossref, falling back to DataCite for DOIs Crossref does not hold (arXiv preprints, mostly). Then every tool not already in `data/updated.json` gets a last-updated date (see below). Both caches are committed, so only this stage needs the network.
3. **Build.** The main table of each `database_*.md` file — and the per-ecosystem detail sections from `database_ecosystems.md` — is written to `docs/data/data.js`, with each DOI replaced by its title, journal and year and an `Updated` column appended to the tools table. The data is emitted as a plain script rather than JSON so the site also works when `index.html` is opened directly from disk, with no server.

Useful flags: `--check` runs the checks and builds nothing, `--offline` skips both fetch stages, `--refresh` re-fetches everything rather than only what is new. The underlying scripts can still be run on their own if you want one stage without the others.

### Update dates

The `Updated` column is not held in `database_tools.md`, because unlike everything else there it goes stale on its own rather than through anyone editing the file. `fetch_updated.py` derives it from whatever the `Code` column points at:

| Where the code lives | What the date is |
|---|---|
| A GitHub repository (113 tools) | Last push, via the GitHub API |
| A GitHub organisation (1) | Last push to that account's most recently touched repository, ignoring its `*.github.io` website |
| A GitLab instance (1) | Last commit on the default branch |
| CRAN (9) | `Date/Publication` of the current version |
| PyPI | Upload time of the newest release file |
| A DOI, a departmental page or a product site (14) | Nothing to query — recorded as `N/A` |

Where the `Code` column is not a repository, the tool's own name is tried on the registry its language implies (PyPI for Python, CRAN for R) — but only as an exact match, since a near-miss would quietly report some unrelated package's date. The 14 `N/A` entries are tools with no public repository or package: AADIS, CEPAC, the CoMo Consortium model, COVSIM, GLEAM, HIV Synthesis, LiST, OneHealth Tool, SaTScan, Skeeter Buster, Spectrum, STDSIM, Thembisa and TIME Impact. The CoMo entry is the case the `*.github.io` rule exists for — `como-international.github.io` is a site about the model, and the organisation behind it publishes nothing else, so there is no code to date.

GitHub allows 60 unauthenticated API calls an hour, well short of the 113 repositories here, so the script uses `$GITHUB_TOKEN` if it is set and otherwise falls back to `gh auth token`. Re-run `python docs/build.py --refresh` to bring the dates (and the DOI titles) up to date, or `python docs/fetch_updated.py --only NAME` to re-check a single tool.

### Usage scoring

The `Usage` column *is* held in `database_tools.md` — unlike the update dates, it carries prose evidence that no API can reconstruct — but the numeric part of it is generated. `python docs/fetch_usage.py` re-fetches the metrics, re-scores every tool, rewrites the column in place, and writes the full breakdown to `data/usage.json` so a label can be audited without re-fetching.

| Evidence | Source | Points |
|---|---|---|
| GitHub stars and forks | GitHub API, summed across the account's repositories where `Code` names an organisation | 1 each |
| CRAN downloads, all-time | cranlogs | 1 per 1,000 |
| PyPI downloads, all-time | the public ClickHouse mirror of the PyPI download statistics; pypistats serves only the last 180 days, which would undercount long-lived packages against CRAN's lifetime totals | 1 per 1,000 |
| Citations of a paper *about the tool* | OpenAlex, falling back to Crossref; OpenAlex covers the arXiv and bioRxiv DOIs Crossref's own count does not | 1 per 5 |
| Citations of a paper that is not about the tool | as above, classified by `cited_for` (below) | 1 per 20 |
| Countries with documented use | the prose already in the cell ("Used by teams in 40+ countries" → 40); prose describing a national or agency deployment without a number counts as one | 1 each |

Above 200 points is `Established`, 30–200 `Emerging`, below 30 `Minimal`. The points are not published — see the rationale in `database_tools.md` — so the cell reads `Established (289★, 238 forks; PyPI 318k; 663 citations)`: label, then the evidence it came from, with any prose clause in the old cell preserved.

**Whose citations are they?** A `Publication` DOI is not always the software's own paper — `contactdata`'s is Prem et al.'s contact-matrix paper, cited ~1,000 times for the matrices rather than for the R package. Each row is classified `tool`, `science` or `unknown` in `data/usage.json`: `tool` if the title names the tool, describes software, or the venue is a software journal; `science` otherwise. `science` and `unknown` citations count at 1 point per 20 rather than per 5, so a borrowed citation record still counts for something without carrying a label on its own. The run ends by listing the `science` rows with 25 or more citations and the share of their points those citations are. The classification is a title heuristic and a method paper written by the tool's own authors is often its canonical citation, so override it with `"cited_for": "tool"` in `data/usage_manual.json` (or set `"citations": N` outright) where the heuristic is wrong.

Package names are resolved from the `Code` column where it names one, and otherwise guessed from the repository or tool name and accepted only if the package's own metadata points back at that repository. A name-only match is kept but reported at the end of the run, because PyPI is full of unrelated packages whose names collide with a tool's — `civet` is a Django asset precompiler, `TreeTime` a to-do list manager, `optima` a PyTorch optimiser. Corrections go in `data/usage_manual.json`, which is merged over the fetched values and never rewritten: `"pypi": null` rejects a match, a string replaces it, and `countries` can record adoption the prose does not state.

Flags: `--dry-run` prints the cells that would change and writes nothing, `--offline` re-scores from the cache, `--only NAME` (repeatable) does one tool. Sorting the site's `Usage` column sorts by rank, not spelling, so descending runs Established → Emerging → Minimal.

`.github/workflows/build-site.yml` runs the same command in CI: on a push to `main` it rebuilds and commits `data/data.js`, and on a pull request it fails if the tables are malformed or the committed `data.js` is stale. Forgetting to rebuild is therefore caught rather than shipped.

## Previewing locally

```bash
python -m http.server 8000 --directory docs
```

Then open <http://localhost:8000>.

## What the page does

- **Tabs** for Tools (default), Ecosystems and Communities, each backed by its own database file. The active tab is reflected in the URL hash (`#ecosystems`), so tabs are linkable. Filters are remembered per tab while the page is open.
- **Free-text search** across every column, including hidden ones, with matches highlighted.
- **Faceted filters** — checkbox dropdowns per tab (for tools: Type, Discipline, Pathogen, Language, Licence). Counts next to each option reflect the other filters in force, so you can see what a selection would yield before making it; options that would return nothing are dimmed rather than removed. Multi-valued cells such as `R / C++` are indexed under each value. Verbose statuses collapse to a facetable label (`Active (with caveat)`), with the full text on hover and in the detail drawer.
- **Licence grouping.** Filtering by licence uses families rather than exact SPDX identifiers, so versions of one licence stay together: MIT (54), GPL (44, covering GPL-2.0 through GPL-3.0-or-later), BSD (5), Other copyleft (9: LGPL, AGPL, EUPL, CeCILL), Other permissive (6: Apache, Artistic, public domain), Proprietary or closed (14) and Not stated (5). The table cell still shows the exact identifier — the grouping applies to the filter only. `Not stated` is kept separate despite being under five entries, because an undeclared licence is a different fact from a deliberately closed one. The mapping is `licenceGroup()` in `assets/app.js`.
- **Column show/hide**, since the full tables are wider than a page. Each tab starts with its least-used columns hidden — for tools, Discipline and Licence. The name column stays pinned to the left while scrolling sideways.
- **Column reordering** by dragging a header, or by pressing Alt + ← / → on a focused one. The name column is the record's identity, so it stays first and nothing moves in front of it; everything else can go anywhere. Reset in the Columns dropdown restores both the default order and the default visibility. A move applies to the table, the detail drawer, the CSV export and the column list alike, and lasts as long as the page is open.
- **Sorting** by clicking any column header. A sort follows its column when the column moves. Cells saying nothing — blank, `—`, or an `N/A` update date — sink to the bottom whichever way the column is sorted, since a missing answer is not the smallest one: sorting by Updated descending shows the most recently touched tools first and the undatable ones last, rather than leading with them. `Usage` sorts by its label's rank rather than alphabetically — descending is Established, then Emerging, then Minimal — and tools sharing a label keep the table's alphabetical order, since their evidence strings are not comparable with each other.
- **Detail drawer** — click a row for the complete record, including hidden columns and, for ecosystems, the component list and caveats from the per-ecosystem sections.
- **CSV export** of the current filtered rows and visible columns.

## Deploying to GitHub Pages

In the repository settings, set Pages to deploy from the `main` branch, `/docs` folder. No build step runs on GitHub — `data/data.js` is committed, so whatever is in the folder is what gets served. The empty `.nojekyll` file stops GitHub from running the files through Jekyll.

## Data problems this surfaced, and their fixes

Resolving the DOIs to titles exposed six entries in `database_tools.md` whose publication link pointed at an unrelated paper — MicroCOSM's, for instance, resolved to a paper on calcium-binding protein in malignant melanoma. Replacements were found by searching Crossref for the tool name and authors, and have been applied to `database_tools.md`:

| Tool | Was | Now |
|---|---|---|
| AADIS | `10.1016/j.envsoft.2016.02.011` — estuarine carbon cycling | `10.3389/fenvs.2015.00017` — "A hybrid modeling approach to simulating foot-and-mouth disease outbreaks in Australian livestock" (Bradhurst et al., 2015) |
| CoMo Consortium model | `10.1016/j.jinf.2021.02.007` — "The chilly climate may increase the chance of infecting COVID-19" | `10.1136/bmjgh-2020-003126` — "Modelling the COVID-19 pandemic in context: an international participatory approach" (Aguas et al., 2020) |
| MicroCOSM | `10.1371/journal.pone.0256238` — melanoma cell biology | `10.1101/310763` — "MicroCOSM: a model of social and structural drivers of HIV…" (Johnson et al., 2018) |
| OneHealth Tool | `10.1186/1478-7547-12-9` — hospital efficiency in Ghana | `10.12688/f1000research.13824.2` — "Reflections on the use of the WHO OneHealth Tool" (Wong et al., 2018) |
| STDSIM | `10.1097/00007435-199809000-00008` — gonorrhoea drug resistance | `10.1287/inte.28.3.84` — "STDSIM: A Microsimulation Model for Decision Support in STD Control" (Van der Ploeg et al., 1998) |
| Thembisa | `10.1002/jia2.25517` — gendered health institutions | `10.4102/sajhivmed.v18i1.694` — "Progress towards the 2020 targets for HIV diagnosis and antiretroviral treatment in South Africa" (Johnson et al., 2017) |

AADIS has no code repository, so its `Code` column pointed at the same wrong DOI; that was corrected too.

Two caveats on the replacements. **MicroCOSM**'s reference is a bioRxiv preprint — it is the model's own description paper and the canonical citation, but it is not peer reviewed. **OneHealth Tool** has no developer-authored paper; the F1000Research article is a third-party evaluation of the tool rather than a description of it, and is the usual citation in the literature. Both are worth a second opinion.

**Optima HIV was a false alarm** — its DOI was correct all along. Crossref stores that paper's title split across `title` ("Optima") and `subtitle` ("A Model for HIV Epidemic Analysis…"), and the fetcher was reading only the first. Fixed in `fetch_publications.py`, which now joins the two.

A rough check — flagging titles that share almost no vocabulary with the tool's name and description — raised 13 candidates before the fixes and 7 after. The 7 that remain (CEPAC, CoMo, hubverse, MEmilio, OpenMalaria, SynthPops, HIV Synthesis) are correct papers that simply do not repeat the tool's name in their title.

Separately, 14 titles arrive from Crossref with JATS markup embedded. Stripping the tags leaves ambiguous whitespace — `MGD<scp>riv</scp>E` should close up to "MGDrivE" while `in <scp>r</scp>` must keep its space — so `clean()` repairs the unambiguous cases and three titles are stated explicitly in `OVERRIDES`.

## Known limitations

- The header navigation is decorative; links go nowhere.
- The intro paragraph for each tab is written in `assets/app.js` (`CONFIG[...].blurb`) rather than pulled from the markdown, because the source intros are full of cross-file links that make no sense on the web.
- Which columns are faceted, ordered, hidden by default, or rendered as coloured tags is hard-coded in `CONFIG` at the top of `assets/app.js`; adding a column to a database file will show it in the table and drawer, but placing it, or giving it a filter, means adding it there. Columns left out of `CONFIG.order` keep their source order, on the end.
- Update dates are only as fresh as the last `--refresh`, and a repository's last push is a crude proxy for whether a tool is maintained: a README typo counts, and a stable tool that needs no changes looks dormant.
