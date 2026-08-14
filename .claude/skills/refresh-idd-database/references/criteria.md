# Inclusion and exclusion criteria, as actually applied

`details.md` states five criteria. Each has been operationally refined by user decision. The refinement is what to apply; the spec text is what to cite.

## The five criteria

### 1. Open source — **not a gate**

Closed-source tools **are included** and labelled in the `Licence` column. Omitting them misrepresents the landscape: Spectrum produces the official UNAIDS estimates for 160+ countries. Included-but-labelled: Spectrum, GLEAM, LiST, SaTScan, OneHealth, TIME Impact, CEPAC, Thembisa, HIV Synthesis, STDSIM, AADIS, FRED (Pittsburgh EULA), Episimmer (Commons Clause).

What *does* disqualify is being **unobtainable** — no distributable artefact at all. AEM is the test case: published in JAIDS 2024, used in 13 Asian countries, but obtainable only by private arrangement with the East-West Center, so it is excluded, while Spectrum and LiST are closed but freely downloadable and are in.

Determine the licence from the GitHub licence API *or* the CRAN `DESCRIPTION` `License:` field, and **read the raw `LICENSE` file whenever the API reports `NOASSERTION`/`NONE` or anything unfamiliar**. Record the SPDX identifier where open source, an explicit description otherwise ("Closed source", "Closed source (free to use)", "Free download, no open licence", "Not stated"). `Rsero` is recorded as `Not stated` because its `DESCRIPTION` still holds the roxygen placeholder `License: What license is it under?`.

### 2. Published — **not a hard gate**

A tool with substantial independent evidence of use qualifies without a paper. This was the user's reversal of the strictest reading, which had cut the tools file from 195 to 84.

An **auto-minted CRAN or Zenodo DOI is not a publication** — record `—`. It evidences distribution, not peer review. But a package with only a CRAN DOI still qualifies on criterion 4, which is how most of Epiverse-TRACE is in.

Search Crossref by bibliographic query and by title, and check `CITATION.cff`. Peer-reviewed software venues count fully: JOSS, *Epidemics*, *Journal of Statistical Software*, *Journal of Open Research Software*, *SoftwareX*, *PLOS Computational Biology*, *Infectious Disease Modelling*, *Wellcome Open Research*, F1000Research, arXiv/bioRxiv/medRxiv preprints, and conference proceedings (Starsim qualifies on SciPy 2024, `10.25080/ukpu4584`).

### 3. Documented — manual, and the weakest link

Requires installation instructions, at least one getting-started example or vignette, and a technical reference. Assessed by inspection; state that it is a judgement call and that borderline entries could move either way. The NTD Modelling Consortium's ten models were excluded as a block on this ground — the public repos are runners and calibration harnesses, not installable documented models. MBGapp was excluded as teaching material.

### 4. Evidence of use — cumulative, not a threshold

Assess as a weighted whole: GitHub stars and forks, **plus** distribution on CRAN or PyPI, **plus** peer-reviewed publication, **plus** documented adoption by agencies or national programmes. A peer-reviewed paper or a national-programme deployment counts for far more than a comparable number of stars.

Calibration points: ~10 stars+forks, or CRAN/PyPI presence, or multi-group publication use is roughly the floor. Below ~10 GitHub stars, repo search results are almost entirely coursework. Do not apply a hard star cut — `epiworldR` at 14 stars sits above already-listed Atomica (15) and MEmilio (1.8k downloads); excluding it would have been indefensible.

Tools whose users are in government or agency workflows rather than on GitHub are the hardest to assess and the most likely to be under-counted. Say so rather than penalising them.

**The label is scored, not judged.** Since 2026-08-14 every `Usage` cell opens with `Established`, `Emerging` or `Minimal`, computed by `docs/fetch_usage.py` from a points total: 1 point per GitHub star and per fork, 1 per 1,000 all-time CRAN or PyPI downloads, 1 per citation of the foundational paper, 1 per country with documented use; >50 points `Established`, 10–50 `Emerging`, <10 `Minimal`. Do not assign a label by hand and do not restate the points in the file — run the script, which rewrites the column in place and records the breakdown in `docs/data/usage.json`.

`Usage` cell format: `Established (289★, 238 forks; PyPI 318k)`; `Emerging (CRAN 34k)`; `Established (South Africa's official national HIV estimates)`. The parenthetical is the evidence the label came from; prose clauses are preserved across re-runs, star/fork/CRAN/PyPI figures are regenerated. The column was named `Adoption` and was renamed to `Usage` by user instruction.

The label does not gate inclusion — the criterion is still cumulative judgement, and `Minimal` records thin *public* evidence rather than an unimportant tool. It does make the two under-counted cases visible: a tool distributed through national programmes scores only on citations and country use, and a tool whose paper is recent scores near zero on citations however widely it is used. Where the prose does not state a country count and one is known, set it in `docs/data/usage_manual.json` rather than editing the cell.

### 5. Supported — activity within 3 years, deliberately a low bar

Any repository push, or CRAN/PyPI release, on or after **snapshot date minus 3 years** (2023-08-07 for the current snapshot), and the repository not archived. A quiet repo may simply mean a finished tool.

Two overrides:

- **A maintainer statement beats commit activity.** EMOD is flagged unmaintained in its `Description` despite live pushes, because IDM has confirmed it is unsupported. Note that the community `EMOD-Hub` org does have real commits, and that the ecosystems file rates the EMOD ecosystem Active — that tension is recorded, not hidden.
- **Archived ≠ dead.** `ihmeuw/vivarium` is archived because development consolidated into the active `vivarium-suite` monorepo. Check the org for a successor before declaring anything unmaintained, and **never publicly declare someone else's project dead without a maintainer statement** — FRED was graded "Low activity" rather than "Unmaintained" for exactly this reason.

## Disqualifying categories — criterion (X)

- **General-purpose, not unique to IDD.** tidyverse, pandas, UNPop, Epi Info, `epitools`, BayesianTools, SUMMER/surveyPrev/sae4health/sae, DisMod-MR. Judgement call: `pomp` was kept once (built in and for the IDD community) and later dropped as a general inference engine — it is currently **out**, and out of the ecosystems file too.
- **Single-group tools** — never used outside the author's own group.
- **Guidance and training material** rather than tools.
- **Datasets and data services.** The line: a package that *fetches* data is in (`malariaAtlas`); one that *ships or serves* data is out (`outbreaks`, `contactdata`, Delphi Epidata) — though after the criteria were relaxed the data-access libraries were restored, so check the current file before asserting either way.

## Standing resolutions on repeat questions

- **LASER: excluded entirely.** Never published, not used; and featuring an unpublished single-institution IDM toolkit is precisely the conflict-of-interest pattern this repo has been cleaned up to avoid. It is recorded in the exclusions with reasoning. Do not reinstate without instruction.
- **Covasim** is a Starsim ecosystem component with a note that the port is in progress; it declares no `starsim` dependency. HPVsim and FPsim have been ported and do.
- **FPsim** is family planning, not IDD — scope question the user should settle if it recurs.
- **Suite granularity.** Collapse wrapper/companion families to one row (EMOD's `emodpy-*`, Nextstrain's Augur/Auspice, hubverse's five packages); keep independently used packages separate (EpiEstim, EpiNow2). This is acknowledged as inconsistent.
- **Ecosystems: shared dependency is not a hard gate.** Test 5 admits a deliberate family built to a shared design philosophy and presented as a suite. Entries qualifying only under test 5 must say so in `Interoperability basis`. Optima and `epiworld` are both in on this basis — restoring one without the other would have favoured the compiler's own ecosystem.
- **Communities: the test is software identity.** A research consortium that happens to have produced a model is out; a group whose shared output is a tool, package suite, hub standard or curated toolchain is in. Training networks (ICI3D, SISMID, Applied Epi) are out. Adjacent consortia (CoMSES Net, GRAM, Malaria Atlas Project, Polaris Observatory, COR-NTD) are out. Wound-down bodies are out. Forecast/scenario hubs are communities, not ecosystems (hubverse appears in both). Genuine IDD orgs that are not software communities go to `gsidd_orgs_suggestions.md` rather than being deleted.

## Conflicts of interest

The compiler works at IDM, leads Starsim, and co-authored the Optima and Atomica publications. Consequences that must hold in any edit:

- Ordering is alphabetical everywhere, stated to carry no ranking information.
- Ecosystem download counts are never summed across a family; related packages are broken out and explicitly excluded from the parent total. This applies to everyone equally (Starsim, odin, EpiModel, Epiverse, Vivarium).
- Marketing adjectives get neutralised, not just on other people's tools.
- Funding is not evidence of use.
- Any relaxation of a rule that admits an IDM tool must be tested against the non-IDM equivalent.
- The COI note in each file's methodology section stays current.
