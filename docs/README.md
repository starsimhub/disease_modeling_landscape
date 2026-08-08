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
| `build_site.py` | Regenerates `data/data.js` from the markdown databases |
| `fetch_publications.py` | Refreshes `data/publications.json` from Crossref |

## Rebuilding after editing the databases

```bash
python docs/build_site.py
```

This parses the main table out of each `database_*.md` file (and the per-ecosystem detail sections from `database_ecosystems.md`) and writes `docs/data/data.js`. The data is emitted as a plain script rather than JSON so the site also works when `index.html` is opened directly from disk, with no server.

If publications have been added or their DOIs changed, refresh the title cache first:

```bash
python docs/fetch_publications.py   # --refresh to re-fetch everything
```

This resolves every DOI in `database_tools.md` against Crossref, falling back to DataCite for DOIs Crossref does not hold (arXiv preprints, mostly), and caches the results. `build_site.py` then substitutes the title for the DOI as the link text, appending the journal and year. The cache is committed, so building the site never needs network access; only this script does.

## Previewing locally

```bash
python -m http.server 8000 --directory docs
```

Then open <http://localhost:8000>.

## What the page does

- **Tabs** for Tools (default), Ecosystems and Communities, each backed by its own database file. The active tab is reflected in the URL hash (`#ecosystems`), so tabs are linkable. Filters are remembered per tab while the page is open.
- **Free-text search** across every column, including hidden ones, with matches highlighted.
- **Faceted filters** — checkbox dropdowns per tab (for tools: Type, Discipline, Pathogen, Language, Licence). Counts next to each option reflect the other filters in force, so you can see what a selection would yield before making it; options that would return nothing are dimmed rather than removed. Multi-valued cells such as `R / C++` are indexed under each value. Verbose statuses collapse to a facetable label (`Active (with caveat)`), with the full text on hover and in the detail drawer.
- **Licence grouping.** Filtering by licence uses families rather than exact SPDX identifiers, so versions of one licence stay together: MIT (50), GPL (41, covering GPL-2.0 through GPL-3.0-or-later), BSD (5), Other copyleft (8: LGPL, AGPL, EUPL), Other permissive (6: Apache, Artistic, public domain), Proprietary or closed (14) and Not stated (4). The table cell still shows the exact identifier — the grouping applies to the filter only. `Not stated` is kept separate despite being under five entries, because an undeclared licence is a different fact from a deliberately closed one. The mapping is `licenceGroup()` in `assets/app.js`.
- **Column show/hide**, since the full tables are wider than a page. Each tab starts with the discursive columns hidden — for tools, that means Discipline, Publication, Usage and Licence. The name column stays pinned to the left while scrolling sideways.
- **Sorting** by clicking any column header.
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
- Which columns are faceted, hidden by default, or rendered as coloured tags is hard-coded in `CONFIG` at the top of `assets/app.js`; adding a column to a database file will show it in the table and drawer, but giving it a filter means adding it there.
