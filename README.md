# IDD software tools

**WARNING: This repo is in draft form and is public for ease of sharing and collaboration only. Information contained herein is mostly LLM generated and has NOT been thoroughly vetted. The risk of inaccurate or hallucinated content is high.**

This repository holds the data underlying the "IDD tools" section of the Global Society for Infectious Disease Dynamics ([gsidd.org](https://www.gsidd.org)) website. That section lists software packages and tools of use or interest to the infectious disease dynamics (IDD) community, with the aims of building communities of practice around IDD software and improving the visibility of tools so that they get reused.

Start with **[details.md](details.md)**, which sets out the scope, definitions, and inclusion criteria that everything else follows.

## Data files

| File | Contents |
|---|---|
| [database_tools.md](database_tools.md) | The tools themselves — models, utilities, and AI extensions, with type, discipline, pathogen, language, authors, code, publication, usage, and licence |
| [database_communities.md](database_communities.md) | Communities of practice organised around developing, hosting, or curating IDD software |
| [database_ecosystems.md](database_ecosystems.md) | Families of tools built to work together — whether through a shared engine, data structure or standard, or through a common design philosophy — and the basis on which each qualifies |

## Prototype website

**[docs/](docs/)** builds these three tables into a static, filterable site — an illustration of how the data could be presented on gsidd.org, with tabs, faceted filters, column show/hide, and a per-entry detail panel. See [docs/README.md](docs/README.md) for how to preview it and how to regenerate its data after editing the tables.

## Working files

These support review and are not intended for publication.

| File | Contents |
|---|---|
| [excluded_tools.md](excluded_tools.md) | Every tool considered and not included, with the criterion it failed, so that the decisions are reviewable rather than silent |
| [gsidd_orgs_suggestions.md](gsidd_orgs_suggestions.md) | IDD organisations found during this work that are not software communities, proposed as additions to the separate [IDD Orgs](https://www.gsidd.org/idd-orgs) directory |
| [archive/](archive/) | Earlier surveys and drafts, kept as a record of how the compilation developed |
| [.claude/skills/refresh-idd-database/](.claude/skills/refresh-idd-database/) | The search grids, operational inclusion criteria, and verification scripts used to build and update the tables, packaged as a Claude Code skill so a refresh is repeatable rather than reconstructed each time |

## Notes on the data

Entries were verified against primary sources rather than recalled: repository and licence metadata from the GitHub API, package metadata and download totals from CRAN and PyPI, and publication DOIs from Crossref. Every URL in the data files was checked to resolve. Counts, dates, and statuses are a snapshot as of 2026-08-07 and will drift.

The Markdown tables here are a working representation. The intended destination is a filterable database, so columns use controlled vocabularies where practical and each file is a single flat table rather than a set of themed sections.

Inclusion is a judgement against the criteria in `details.md` on a particular date, not a statement about quality or importance. Several widely used and consequential tools are absent for reasons of licensing, maintenance, or scope; the reasoning for each is recorded in `excluded_tools.md`. Corrections and additions are welcome.
