# Prototype website

A static illustration of what the GSIDD "IDD tools" section could look like, built from the `database_*.md` files in the repository root. It is a design mock-up for discussion, not a production site: styling follows [gsidd.org/idd-orgs](https://www.gsidd.org/idd-orgs) loosely (navy/orange palette, Spinnaker display type), and the top navigation bar is inert.

## Contents

| Path | What it is |
|---|---|
| `index.html` | The whole site — one page, three tabs |
| `assets/style.css` | Styling |
| `assets/app.js` | Table browser: filtering, sorting, column visibility, detail drawer, CSV export |
| `data/data.js` | Generated data; do not edit by hand |
| `build_site.py` | Regenerates `data/data.js` from the markdown databases |

## Rebuilding after editing the databases

```bash
python docs/build_site.py
```

This parses the main table out of each `database_*.md` file (and the per-ecosystem detail sections from `database_ecosystems.md`) and writes `docs/data/data.js`. Nothing else needs regenerating. The data is emitted as a plain script rather than JSON so the site also works when `index.html` is opened directly from disk, with no server.

## Previewing locally

```bash
python -m http.server 8000 --directory docs
```

Then open <http://localhost:8000>.

## What the page does

- **Tabs** for Tools (default), Ecosystems and Communities, each backed by its own database file. The active tab is reflected in the URL hash (`#ecosystems`), so tabs are linkable. Filters are remembered per tab while the page is open.
- **Free-text search** across every column, including hidden ones, with matches highlighted.
- **Faceted filters** — checkbox dropdowns per tab (for tools: Type, Discipline, Pathogen, Language, Licence). Counts next to each option reflect the other filters in force, so you can see what a selection would yield before making it; options that would return nothing are dimmed rather than removed. Multi-valued cells such as `R / C++` are indexed under each value. Verbose statuses collapse to a facetable label (`Active (with caveat)`), with the full text on hover and in the detail drawer.
- **Column show/hide**, since the full tables are wider than a page. Each tab starts with the discursive columns hidden — for tools, that means Authors, Publication, Usage and Licence. The name column stays pinned to the left while scrolling sideways.
- **Sorting** by clicking any column header.
- **Detail drawer** — click a row for the complete record, including hidden columns and, for ecosystems, the component list and caveats from the per-ecosystem sections.
- **CSV export** of the current filtered rows and visible columns.

## Deploying to GitHub Pages

In the repository settings, set Pages to deploy from the `main` branch, `/docs` folder. No build step runs on GitHub — `data/data.js` is committed, so whatever is in the folder is what gets served. The empty `.nojekyll` file stops GitHub from running the files through Jekyll.

## Known limitations

- The header navigation is decorative; links go nowhere.
- The intro paragraph for each tab is written in `assets/app.js` (`CONFIG[...].blurb`) rather than pulled from the markdown, because the source intros are full of cross-file links that make no sense on the web.
- Which columns are faceted, hidden by default, or rendered as coloured tags is hard-coded in `CONFIG` at the top of `assets/app.js`; adding a column to a database file will show it in the table and drawer, but giving it a filter means adding it there.
