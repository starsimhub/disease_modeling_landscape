---
name: refresh-idd-database
description: Search for, vet, and add IDD software tools, communities, and ecosystems to the database_*.md files in this repo, or rebuild them from scratch. Use when asked to update/refresh/rebuild the IDD tools database, to find tools the search missed, to re-verify metadata (stars, downloads, licences, last-updated dates), to re-vet entries against the inclusion criteria, or to check whether a specific tool belongs. Encodes the search grids, the operational inclusion/exclusion rules, and the verification recipes established in this repo.
---

# Refresh the IDD tools database

This repo holds the data behind the "IDD tools" section of [gsidd.org](https://www.gsidd.org): `database_tools.md`, `database_communities.md`, `database_ecosystems.md`, with rejections recorded in `excluded_tools.md` and non-software IDD orgs in `gsidd_orgs_suggestions.md`. `details.md` is the spec; `docs/` builds the tables into a static site.

The criteria in `details.md` are the published spec. They have been **operationally refined** through several rounds of review, and those refinements are binding — see `references/criteria.md`. Do not re-derive them from `details.md` alone; applying it literally has twice produced results the user rejected (dropping Spectrum/GLEAM as closed source, dropping most of Epiverse-TRACE over CRAN DOIs).

## Pick a mode

| Mode | When | Go to |
|---|---|---|
| **Refresh metadata** | Stars, downloads, licences, last-updated dates have drifted; no new tools wanted | Step 4 → Step 6 |
| **Gap search** (usual) | Find tools the existing search missed, add the qualifying ones | Steps 1–6 |
| **Re-vet** | Criteria changed, or a batch of entries needs re-checking against them | Steps 3–6 |
| **Single candidate** | "Does X belong?" | Step 3 on X alone, then Step 5 |
| **Rebuild** | Reconstruct a file from scratch | Steps 1–6, and read `references/schemas.md` first |

Read `references/criteria.md` before any mode that decides inclusion. Read `references/search.md` before Step 1. Read `references/verification.md` before Step 4.

## Step 1 — discovery

Run the sweep, which queries Crossref (corpus-wide and software-venue-restricted), GitHub repo/topic search, and the CRAN Epidemiology Task View, then flags hits whose title already matches a known entry:

```bash
python .claude/skills/refresh-idd-database/scripts/discover.py --out /tmp/candidates.tsv
```

Useful flags: `--axis estimation` / `--axis serology` / `--axis core` to run one keyword family; `--since 2024` to limit Crossref by publication year; `--source crossref|github|cran`; `--full` to include hits that matched a known name.

Then read `references/search.md` and ask what vocabulary the grid *still* cannot see. That is the point of the step — the two documented misses (Naomi, then the whole serology family) were both vocabulary blind spots, not ranking failures. If the user brought a specific missed paper, work backwards from its title and keywords to the axis that would have caught it, add that axis to `scripts/axes.py`, and re-run.

## Step 2 — triage

Discovery output is noisy. Discard: replication code for a single study, coursework, general-purpose statistics, datasets and data services, training material. Keep anything that is a reusable, installable, documented IDD tool. Cross-check names against **both** `database_tools.md` and `excluded_tools.md` — a name in the exclusions file may now qualify (activity, a new paper), which is a legitimate addition, but say so explicitly rather than silently reversing an earlier call.

Also reconcile the three data files against each other. `serofoi` was listed as an Epiverse-TRACE component in `database_ecosystems.md` while missing from `database_tools.md`; that cross-check is cheaper than any literature search.

## Step 3 — vet against the criteria

Apply `references/criteria.md` candidate by candidate. Two rules matter more than the rest:

- **Verify, never recall.** Every claim in these files was checked against a primary source. Three past errors all came from asserting rather than checking: `odin`/`dust`/`mcstate` excluded for "no publication" when FitzJohn et al. 2021 names all three in its title; `incidence` the same; four repository URLs invented and returning 404.
- **Read the licence file, not just the API.** FRED ships a University of Pittsburgh EULA and Episimmer a Commons Clause, both behind public GitHub repos that the API reports vaguely.

## Step 4 — gather metadata

```bash
python .claude/skills/refresh-idd-database/scripts/verify.py --name Naomi --repo mrc-ide/naomi --cran serofoi --pypi starsim
python .claude/skills/refresh-idd-database/scripts/verify.py --from-database   # re-check every existing row
python .claude/skills/refresh-idd-database/scripts/verify.py --doi-for "title of the software paper"
```

It reports stars, forks, `pushed_at`, archived status, the licence from the API *and* from the raw `LICENSE`/`DESCRIPTION` file, CRAN/PyPI release dates and download totals, and Crossref matches — then prints a per-criterion verdict, with criterion 3 (documentation) left as a manual judgement because it is.

The `Usage` column itself is generated, not written: score it with

```bash
python docs/fetch_usage.py --dry-run     # what would change
python docs/fetch_usage.py               # rewrite the column, refresh docs/data/usage.json
```

which turns stars, forks, all-time CRAN and PyPI downloads, citations and documented country use into points (rates in `references/criteria.md`) and writes `Established (289★, 238 forks; PyPI 318k; 663 citations)` back into every row. Read the name-only PyPI matches it prints at the end — a wrong package inflates a label — and record any correction in `docs/data/usage_manual.json`, which it never overwrites. A new tool gets its label from the same run; do not invent one.

## Step 5 — write

Match the existing schema and prose conventions exactly (`references/schemas.md`). In particular:

- Rows are alphabetical, case-insensitive, by name; insert in place rather than appending.
- Update the stated count in the prose (`128 tools, sorted alphabetically…`) — `docs/build.py` fails the build if it drifts.
- Every rejection goes into `excluded_tools.md` under the section for the criterion it failed, with a specific reason. Exclusions being reviewable rather than invisible is a deliberate property of this repo.
- Refresh the snapshot date in the methodology sections of any file whose facts you re-checked, and extend the "what was searched" paragraph so the new search is reproducible.
- Never hard-wrap prose. One paragraph, one physical line.

## Step 6 — verify and build

```bash
python .claude/skills/refresh-idd-database/scripts/check_urls.py           # every URL in every .md
python docs/fetch_usage.py                                                 # re-score the Usage column
python docs/build.py                                                       # check → fetch DOIs + update dates → build data.js
```

`build.py --check` runs the structural checks alone; `--refresh` re-fetches all cached publication and last-updated data rather than only what is new. Fix everything it reports; a failing check must not be published.

Leave changes uncommitted and report: counts before/after, what was added, what was excluded and why, any judgement calls the user should overturn, and anything you could not verify. Do not commit unless asked.

## Judgement calls that are the user's, not yours

If a decision would change which tools appear, and `references/criteria.md` does not already settle it, ask rather than guess — the user has overturned this kind of call before (restoring Optima as an ecosystem, relaxing publication from a hard gate, renaming `Adoption` to `Usage`). Conflict-of-interest handling is not optional: the compiler works at IDM and leads Starsim, so IDM-affiliated tools must clear the same bar as everyone else's, and any softening of a rule that admits an IDM tool must be checked for whether it also admits the non-IDM equivalent.
