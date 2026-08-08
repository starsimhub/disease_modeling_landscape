# Disease Modeling Software Ecosystems

This file lists **ecosystems** that exist around interoperable infectious disease dynamics (IDD) software tools. It is a companion to [database_tools.md](database_tools.md), which lists individual tools, and to [database_communities.md](database_communities.md), which lists the communities that develop, host, and curate them. Where the tools database answers "what software exists?", this file answers "which pieces of software were built to work together?".

## What counts as an ecosystem

An entry qualifies as an ecosystem if it is a **family of software tools deliberately designed to interoperate**. In practice at least one of the following must be demonstrable, not merely asserted:

1. **A common core engine or runtime** that the other tools are built on (e.g. every Starsim disease model subclasses the same `ss.Module` API; every Spectrum module runs inside the same host application).
2. **A shared data structure or class contract** that tools pass between each other (e.g. `epi_df` in the Delphi tooling; the `<linelist>` and `<epiparameter>` classes handed between Epiverse-TRACE packages).
3. **A shared file format, schema, or standard** with independent producers and consumers (e.g. the Auspice dataset JSON schema in Nextstrain; the EMOD JSON config/campaign/demographics schema).
4. **A formal suite, meta-package, plugin registry, or umbrella project** that installs, registers, or integration-tests the components together (e.g. the `epiverse` meta-package; the BEAST2 CBAN package registry).

The following do **not** qualify, and several well-known projects were excluded on these grounds (see [Candidates considered but not listed](#candidates-considered-but-not-listed)):

- A single package, however modular internally. A monolith with plugins is a *framework*, not an ecosystem.
- A research group's portfolio of individually excellent but technically uncoupled packages — shared authors, a shared house style, and a shared website are not interoperability.
- A GitHub organisation used as a filing cabinet for unrelated project repositories.
- A general-purpose ecosystem that happens to include an epidemiological application.

Ecosystems are listed here even when the individual component tools also appear in [database_tools.md](database_tools.md); the two files are intentionally overlapping views of the same landscape.

## Schema

| Column | Description |
|---|---|
| Name | Ecosystem name, as the project itself uses it |
| Lead institution(s) | Organisation(s) principally responsible for development and governance |
| Language(s) | Primary implementation language(s) |
| Anchor tool | The core engine, class layer, standard, or meta-package that the ecosystem is organised around |
| Interoperability basis | The concrete mechanism by which the components work together — which of tests 1–4 above it satisfies, and how |
| Components | Approximate number of first-party component tools (see the per-ecosystem sections for the enumerated lists) |
| Status | Maintenance verdict as of the snapshot date: **Active**, **Active (early)**, **Mixed**, **Maintenance**, or **Dormant** |
| Description | One-sentence summary of what the ecosystem is for |
| Website | Canonical project page (all verified HTTP 200 on the snapshot date) |

## Ecosystems

18 ecosystems, sorted alphabetically (case-insensitive) by name.

| Name | Lead institution(s) | Language(s) | Anchor tool | Interoperability basis | Components | Status | Description | Website |
|---|---|---|---|---|---|---|---|---|
| BEAST2 | University of Auckland; ETH Zürich; distributed developer community | Java | `beast2` | Plugin registry + core API — a `BEASTObject`/`BEASTInterface` class hierarchy plus a shared XML model-specification format, with a package manager backed by the CBAN registry (200+ registered packages) | 200+ | Active | Bayesian phylogenetic and phylodynamic inference platform, extensible via a curated third-party package ecosystem | [beast2.org](https://www.beast2.org) |
| Delphi Tooling | Carnegie Mellon University Delphi Research Group | R, Python | `epiprocess` | Shared class contract — the `epi_df` and `epi_archive` S3 classes defined in `epiprocess` are consumed by `epipredict` and `epidatasets` — plus a REST API contract (the Delphi Epidata API) shared by the R and Python clients | ~7 | Active | Signal processing, forecasting, and surveillance-data access for real-time epidemiology | [delphi.cmu.edu](https://delphi.cmu.edu/) |
| EMOD | EMOD-Hub (community successor to Institute for Disease Modeling) | C++, Python | `EMOD` | Common engine + shared schema — all models run on the same C++ executable configured by a shared JSON config/campaign/demographics schema; `emod-api` reads and writes it and the `emodpy-*` packages layer disease-specific parameterisation on a common `emodpy` base | ~8 | Active (community), **no longer supported by IDM** | Individual-based multi-disease transmission platform (malaria, HIV, TB, typhoid, generic) with a Python configuration and workflow layer; the originating institution has retired it, and commits since are from the community EMOD-Hub organisation | [emod-hub.github.io](https://emod-hub.github.io/) |
| EpiAware | LSHTM; grew out of a US CDC Center for Forecasting and Outbreak Analytics collaboration | Julia | `ComposableTuringIDModels.jl` | Shared interface — most packages extend the `Distributions.jl` interface so they compose; shared Turing.jl/DynamicPPL substrate; shared cross-package CI and automatic-differentiation test infrastructure | ~12 | Active (early) | Composable Bayesian building blocks (censoring, truncation, delays, scoring) for infectious disease inference in Julia | [epiaware.org](https://epiaware.org/) |
| epiforecasts | London School of Hygiene & Tropical Medicine | R, Stan | none (loosely coupled) | **Loosely coupled** — the packages share authors, house style, and a common Stan/Bayesian idiom, but their DESCRIPTION files declare no mutual dependencies. The one strong dependency edge, from `EpiNow2` to `primarycensored`, points into the epinowcast ecosystem. Listed for completeness because the group is a major producer of IDD software, with the coupling stated honestly. | ~6 | Active | Real-time reproduction number estimation, forecasting, forecast scoring, and contact-matrix tooling | [epiforecasts.io](https://epiforecasts.io/) |
| EpiModel | Emory University; University of Washington | R | `EpiModel` | Common engine + shared data structures — models are assembled from swappable EpiModel modules and run on statnet network objects (`network`, `networkDynamic`, `tergm`), which `EpiModel` declares as hard dependencies | ~11 | Active | Deterministic, stochastic individual-contact, and temporal-ERGM network epidemic models, with HIV/STI and COVID-19 extensions and an HPC layer | [epimodel.org](https://epimodel.org) |
| epinowcast | Community-governed; contributors from LSHTM, US CDC CFA, ETH Zürich | R, Stan | `epinowcast` | Shared statistical kernel — `primarycensored` exposes reusable Stan functions for primary-event-censored, right-truncated delay distributions that `epidist`, `epinowcast`, and (cross-organisation) `EpiNow2` all consume | ~7 | Active | Real-time nowcasting, delay-distribution estimation, and reproduction number estimation from incomplete surveillance data | [epinowcast.org](https://www.epinowcast.org/) |
| Epistorm (Epydemix) | Northeastern University; Fondazione ISI; funded by US CDC Insight Net | Python | `epydemix` | Shared data package + wrapper applications — the `epydemix` model object consumes `epydemix-data` population and contact-matrix bundles for 400+ locations, and the dashboard/API tools wrap the same package | ~4 | Active (early) | Compartmental epidemic modeling with Approximate Bayesian Computation calibration, plus companion scenario and forecast applications | [epistorm.org](https://www.epistorm.org/) |
| Epiverse-TRACE | data.org; LSHTM; Universidad de los Andes and other Latin American partners | R | `epiverse` meta-package | Meta-package + shared classes + integration tests — a meta-package declares the released set, hosts cross-package integration tests in CI, and the packages hand off `<linelist>`, `<epiparameter>`, and `<incidence2>` objects to each other | ~18 | Active | End-to-end outbreak analytics pipeline in R: read, clean, validate, parameterise, simulate, estimate severity and transmission | [epiverse-trace.github.io](https://epiverse-trace.github.io/) |
| malariaverse | MRC Centre for Global Infectious Disease Analysis, Imperial College London | R | `malariasimulation` | Shared parameter and output formats — every package either produces `malariasimulation` parameter inputs (site files, seasonality, net coverage, demography) or consumes its outputs (post-processing, costing, optimization) | ~11 | Active | A constellation of R packages that parameterise, calibrate, run, cost, and optimise the `malariasimulation` individual-based malaria model for specific places | [mrc-ide.github.io](https://mrc-ide.github.io/malariaverse/) |
| Nextstrain | Fred Hutchinson Cancer Center (Bedford lab); Biozentrum, University of Basel (Neher lab) | Python, JavaScript, Rust | `augur` + `auspice` | Published versioned schema — Augur writes an Auspice dataset JSON validated against a public schema that any tool can emit and Auspice will render; plus a unified CLI runtime and a common Snakemake pathogen-workflow template | ~10 core + ~25 pathogen workflows | Active | Real-time pathogen genomic surveillance: bioinformatics pipelines, clade assignment, and interactive phylodynamic visualization | [nextstrain.org](https://nextstrain.org) |
| odin / monty | MRC Centre for Global Infectious Disease Analysis, Imperial College London | R, C++ | `odin2` | Common engine + compilation target — the `odin` DSL compiles model definitions to the `dust` C++ engine interface, and `monty` runs particle filters and MCMC against any `dust` model | ~5 current (+4 legacy) | Active | A domain-specific language for differential-equation and stochastic models, a parallel simulation engine, and a Monte Carlo inference layer that compose into one toolchain | [mrc-ide.github.io](https://mrc-ide.github.io/odin-monty/) |
| Pango / cov-lineages | University of Edinburgh (Rambaut lab); COG-UK | Python | `pangolin` | Shared nomenclature authority + data format — `pango-designation` defines the lineage vocabulary all tools resolve to, `constellations` is the shared JSON variant-definition format consumed by `scorpio`, and model artifacts are versioned separately from code | ~6 | Maintenance | SARS-CoV-2 lineage nomenclature, assignment, and variant-constellation calling | [cov-lineages.org](https://cov-lineages.org/) |
| RECON / reconverse | R Epidemics Consortium (Imperial, LSHTM, Institut Pasteur, MSF, community) | R | `incidence2` + `grates` | Shared class stack — grouped-date classes feed `<incidence2>` objects, which the modelling and evaluation packages consume; plus a common package-development standard | ~9 (reconverse) + ~20 legacy | Dormant | The original interoperable R outbreak-analytics toolkit; historically foundational and largely superseded by Epiverse-TRACE | [reconverse.org](https://www.reconverse.org/) |
| Spectrum | Avenir Health, with the UNAIDS Reference Group, Johns Hopkins and WHO partners | Pascal/Delphi, C++ | Spectrum shell | Common host application + shared projection layer — AIM, EPP, Goals, DemProj, FamPlan, LiST and TIME are modules installed into and run by a single Spectrum application, sharing its demographic projection and country data files | ~8 | Active | Policy modelling suite producing the official UNAIDS HIV estimates and national TB, family planning, demographic and child-survival projections | [avenirhealth.org](https://avenirhealth.org/software-spectrum.php) |
| Starsim | Institute for Disease Modeling; Burnet Institute; Starsim Hub partners | Python | `starsim` | Common engine — every disease model declares a `starsim` version dependency and subclasses the `ss.Module`/`ss.Disease` API to run inside the same `ss.Sim` loop, with shared Sciris utilities | ~12 | Active | Modular agent-based framework for co-circulating diseases on dynamic networks, with disease-specific models for HIV/STIs, HPV, TB, typhoid, rotavirus, and family planning | [starsim.org](https://starsim.org) |
| statnet | University of Washington; Statnet Development Team | R | `ergm` + `network` | Shared data representations + uniform API — the suite's own definition is packages that "share common data representations, API design and a uniform user interface", installed together by the `statnet` meta-package | ~17 | Active | Statistical modeling, simulation, and visualization of static and dynamic networks; the substrate on which EpiModel's network epidemic models are built | [statnet.org](https://statnet.org) |
| Vivarium | Institute for Health Metrics and Evaluation, University of Washington | Python | `vivarium-engine` | Plugin/component architecture — models are assembled from Components that register into a shared simulation context with a common event, value-pipeline, and population-view API; since 2026 all packages ship from one monorepo under a unified `vivarium.*` import namespace | ~13 | Active | Microsimulation framework for health interventions and burden-of-disease modeling, with a public-health component library tied to GBD data | [vivarium-engine.readthedocs.io](https://vivarium-engine.readthedocs.io/en/latest/) |

## Per-ecosystem detail


### BEAST2

**Components.** Core: `beast2`, BEAUti (via `BeastFX`), TreeAnnotator, and the CBAN package registry; `beast3` is in active development. Widely used packages verified in both the registry and as repositories include BDSKY, MASCOT, PhyDyn, CoupledMCMC, SA (sampled ancestors), StarBEAST2/starbeast3, ReMASTER, feast, BEASTLabs, bModelTest, SNAPP/snapper, BICEPS, ORC, OBAMA, MODEL_SELECTION, nested-sampling, and CCD. Tracer, FigTree, and the BEAGLE high-performance likelihood library are shared with BEAST 1.x.

**Caveats.** BEAST 1.x (now branded BEAST X, [beast.community](https://beast.community/)) is a **separate project with a separate codebase and an incompatible XML dialect** — a `beast1to2` converter exists precisely because they do not interoperate. BEAST X is a monolithic program with a companion tool suite rather than an ecosystem, so it is not listed separately here. Individual BEAST2 packages vary widely in maintenance; some registry-listed packages have not been updated in years.

### Delphi Tooling

**Components.** API layer: `delphi-epidata` (server), `epidatr` (R client), `epidatpy` (Python client). Class layer: `epiprocess`, `epipredict`, `epidatasets`. Adjacent: `covidcast-indicators`, `forecast-eval`.

**Caveats.** The coupling is two loosely joined layers rather than one. `epidatr` does **not** return `epi_df` objects and does not depend on `epiprocess` — users convert explicitly with `epiprocess::as_epi_df()`. The Python client shares no class contract with the R side; the only link across languages is the Epidata REST API. There is no R meta-package. The umbrella documentation, the [Delphi Tooling Book](https://cmu-delphi.github.io/delphi-tooling-book/), has not been updated since March 2025 even though the underlying packages ship weekly.

### EMOD

**Components.** `EMOD` and `EMOD-Generic` (C++ cores), `emod-api`, `emodpy`, `emodpy-malaria`, `emodpy-hiv`, `emodpy-workflow`, `EMOD-InputData`, plus `idmtools` (experiment and platform abstraction, maintained by IDM).

**Caveats.** Development has migrated from the original Institute for Disease Modeling repositories, several of which are now archived, to the community-run **EMOD-Hub** organisation. [database_tools.md](database_tools.md) marks EMOD as unmaintained; that reflects the original IDM-hosted project. The EMOD-Hub repositories have real commit activity through mid-2026 (EMOD core, `emodpy-malaria`, `emod-api`, `emodpy-hiv` all committed to within two months of the snapshot date), so the ecosystem is rated **Active** here. This discrepancy between the two files is deliberate and should be reconciled by the user.

### EpiAware

**Components.** Prototype/anchor: `ComposableTuringIDModels.jl`. Distribution building blocks: `CensoredDistributions.jl`, `ComposedDistributions.jl`, `ConvolvedDistributions.jl`, `ModifiedDistributions.jl`, `ReparameterisedDistributions.jl`, `LoweredDistributions.jl`, `DistributionsInference.jl`. Evaluation: `ScoringRules.jl`. Shared infrastructure: `EpiAwareADTools.jl`, `EpiAwarePackageTools.jl`. R interface (prototype): `EpiAwareR`.

**Caveats.** The predecessor is `CDCgov/Rt-without-renewal`, a monorepo containing the original `EpiAware.jl`; the current EpiAware GitHub organisation is a generalisation of that work. The project's own README describes it as at an early stage and actively seeking collaborators, and it has no dedicated funding mechanism. Promising but nascent — do not read the **Active (early)** rating as established production tooling. `ScoringRules.jl` is GPL-2.0 while the rest of the suite is MIT or Apache-2.0.

### epiforecasts

**Components.** `EpiNow2`, `epinowcast` contributions, `scoringutils`, `socialmixr`, `ringbp`, `forecast.vocs`, plus the epiforecasts real-time reporting pipelines.

**Caveats.** This is the weakest coupling in the file and is listed with that stated plainly. Checking the DESCRIPTION files, `EpiNow2`, `scoringutils`, `socialmixr` and `ringbp` declare **no mutual dependencies** — they are a group portfolio unified by authorship and statistical idiom rather than by a shared engine, class contract or schema. The single strong dependency edge runs from `EpiNow2` to `primarycensored`, which belongs to the epinowcast ecosystem. Included because the group is one of the largest producers of IDD software and readers will expect to find it; excluded from the strict interoperability tests above.

### EpiModel

**Components.** `EpiModel` (core), `EpiModelHIV`, `EpiModelHIV-Template`, `EpiModelCOVID`, `EpiModelHPC`, `EpiModel-Gallery`, `ARTnet`, `tergmLite`, `networkLite`, `slurmworkflow`, `swfcalib`.

**Caveats.** EpiModel is built directly on the statnet suite (listed separately below) and cannot be understood independently of it. The core package and the HIV, COVID, and HPC extensions are actively maintained; `tergmLite` has not been updated since 2022, and `EpiModelHIV` itself was last pushed in early 2025 while the newer `EpiModelHIV-Template` is current. The organisation also holds ~40 paper-specific analysis repositories, which are research artifacts rather than components.

### epinowcast

**Components.** `epinowcast` (framework), `primarycensored` (shared Stan kernel), `epidist` (brms delay estimation), `baselinenowcast`, `nowcastdatasets`, plus shared infrastructure `actions`, `enwtheme`, and an R-universe.

**Caveats.** Two components are weaker than the branding suggests: `coerceDT` has been dormant since January 2025 and is **not** in `epinowcast`'s imports, and `baselinenowcast` has no dependency on any other family member — it belongs to the community organisationally rather than technically. The strongest evidence for this ecosystem is cross-organisational: `epiforecasts/EpiNow2` imports `primarycensored`.

### Epistorm (Epydemix)

**Components.** `epydemix` (Python package), `epydemix-data` (population and contact-matrix data for 400+ locations), `epydemix-dashboard`/EpyScenario, `epydemix-webapi`, plus EpyForecast.

**Caveats.** This is the weakest of the four ecosystems named in the project specification, and it should be included only with a clear qualification. **Epistorm is primarily a research consortium** — an 11-institution CDC Insight Net innovation hub — and belongs first in [database_communities.md](database_communities.md). Its wider software portfolio (`Epistorm-Mix`, `RtEval`, `flu-ensemble`, the mobility and forecasting dashboards) consists of separate research outputs that do not interoperate. The genuine ecosystem here is the small, real, and growing `epydemix` package-plus-data-plus-applications family ([epydemix.org](https://epydemix.org)); some of its satellite applications live in personal rather than organisational repositories.

### Epiverse-TRACE

**Components.** Data ingestion and cleaning: `readepi`, `cleanepi`, `numberize`, `linelist`, `safeframe`. Parameters: `epiparameter`, `epiparameterDB`. Simulation: `simulist`, `epichains`, `epidemics`. Estimation: `cfr`, `superspreading`, `finalsize`, `serofoi`, `vaccineff`. Regional: `epiCo`, `sivirep`, `ColOpenData`. Infrastructure: `epiverse` (meta-package), `packagetemplate`, `blueprints`, `tracetheme`, `etdashboard`, and an R-universe.

**Caveats.** The umbrella is thinner than the constituent packages: the `epiverse` meta-package is still v0.0.1, is not on CRAN, and was last pushed in September 2025, whereas most component packages ship monthly. `scenarios` and `quickfit` are marked suspended in their own descriptions. The relationship to RECON is successor-by-rewrite rather than merger — Epiverse-TRACE's `linelist` is an explicit reboot of RECON's, and Epiverse-TRACE *depends on* reconverse's `incidence2` rather than absorbing it. Personnel overlap between the two projects is heavy.



### malariaverse

**Components.** Model: `malariasimulation`, itself built on the `individual` state-and-event toolkit. Parameterisation: `site`, `umbrella` (rainfall and seasonality), `netz` (bed-net metrics), `peeps` (demography). Calibration and optimization: `cali`, `om`. Outputs and scenarios: `postie`, `scene`, `treasure` (costing).

**Notes.** The `individual` package underneath `malariasimulation` is used well beyond malaria and is a general IDD tool in its own right. The malariaverse is one of two distinct ecosystems maintained within the same MRC Centre (the other being odin/monty), which is worth noting when attributing tools to institutions.

### Nextstrain

**Components.** Core: `augur` (bioinformatics toolkit and schema author), `auspice` (visualizer), `nextstrain/cli` (unified runtime across Docker, Conda, Singularity, and AWS Batch), `nextclade` and `nextclade_data`, `auspice.us`, `fauna`, `nextstrain.org`. `treetime` — augur's molecular-clock engine — lives under the `neherlab` organisation rather than `nextstrain`. Roughly 25 maintained pathogen workflow repositories follow a common Snakemake template (`pathogen-repo-guide`), including ncov, seasonal-flu, avian-flu, mpox, dengue, measles, RSV, zika, ebola, rabies, lassa, nipah, WNV, oropouche, norovirus, and TB.

**Notes.** The most consistently maintained ecosystem in this list — essentially every core repository and most pathogen workflows were pushed within a week of the snapshot date. Licensing is mixed: AGPL-3.0 for augur, auspice, and the website; MIT for nextclade and the CLI.

### odin / monty

**Components.** Current generation: `odin2` (DSL), `dust2` (parallel simulation engine), `monty` (Monte Carlo inference), `odin.api`, `wodin` (odin on the web). First generation, now in maintenance: `odin`, `dust`, `odin.dust`, `mcstate`.

**Notes.** The two generations were consolidated in 2024: `odin.dust` and `mcstate` were rationalised into `odin2`/`dust2`/`monty`. Downstream IDD models built on this toolchain include `sircovid`, `squire`, `nimue`, and `mpoxseir`; `squire` (2024) and `mcstate` (2024) are no longer actively developed. The toolchain is general-purpose in principle — it can compile and fit any dynamical model — but was built for and is used almost entirely within IDD.

### Pango / cov-lineages

**Components.** `pangolin` (orchestrator), `pango-designation` (lineage nomenclature authority), `scorpio` (constellation caller), `constellations` (shared JSON variant definitions), `pangolin-data` and `pangolin-assignment` (versioned model and tree artifacts, released independently of code). `civet` is an affiliated consumer maintained by the ARTIC network, not a cov-lineages component.

**Caveats.** Entirely SARS-CoV-2-specific; nothing generalises to other pathogens. In maintenance mode rather than active development: `pango-designation` and `pangolin` still receive updates, but `scorpio` and `constellations` went quiet in early 2026. `pango-designation` and `constellations` carry no SPDX-recognised license, which matters if reuse is being recommended. Superseded components (`pangoLEARN`, `llama`, `grinch`) are excluded.



### RECON / reconverse

**Components.** reconverse (nine repositories): `incidence2`, `grates`, `i2extras`, `trending`, `trendeval`, `reportfactory`, `outbreaks`, `cogs`, and the website. Legacy RECON packages: `incidence` (v1), `epicontacts`, `epitrix`, `earlyR`, `projections`/`projections2`, `outbreaker2`, `epiflows`, `aweek`, `distcrete`, `matchmaker`, `trendbreaker`, `simulacr`, `linelist` (v1).

**Caveats — stated plainly.** RECON is **largely dormant**. Only `incidence2` and `grates` are genuinely maintained; everything else in reconverse has had no commits for one to five years, and roughly 50 repositories in the original RECON organisation are untouched since 2017–2020. The reconverse website's most recent post is dated July 2021. It is listed here because it was the first serious attempt at an interoperable IDD toolkit in R, because `incidence2` and `grates` remain live dependencies of Epiverse-TRACE, and because much of its design and personnel carried forward into Epiverse-TRACE. New users should generally start with Epiverse-TRACE.

### Spectrum

**Components.** AIM (adult HIV), EPP (epidemic projection), Goals and Goals-ART (HIV resource allocation), DemProj (demography), FamPlan (family planning), LiST (Lives Saved Tool, child survival), TIME (TB impact), and the OneHealth Tool costing layer.

**Caveats.** Not open source: the modules are distributed as a free Windows application with no public source repository, so this entry fails the open-source criterion applied to the tools database, where it is included and labelled accordingly. It is listed here because architecturally it is a genuine interoperating suite — the modules install into one host application and share its demographic projection engine and country data files — and because it produces the official UNAIDS HIV estimates for 161+ countries, which makes omitting it a distortion of the landscape.

### Starsim

**Components.** Core: `starsim`. Disease models: `covasim`, `stisim` (including HIVsim), `hpvsim`, `tbsim`, `typhoidsim`, `rotasim`, `mighti`, `zdsim`. Applications and utilities: `fpsim` (family planning), `enroute`, `starsim_ai`. Language ports: `rstarsim` (R), `Starsim.jl` (Julia, early).

**Caveats.** **Covasim** does not yet declare a `starsim` dependency — it is a predecessor that shares the design lineage and the Sciris utility layer, and a port onto the Starsim core is in progress. It is listed as a component on that basis rather than on current code structure. HPVsim and FPsim, also originally standalone, have already been ported and do declare a `starsim` dependency. Component maturity varies widely: `stisim`, `hpvsim`, `fpsim`, and `tbsim` are substantive, while `rotasim`, `typhoidsim`, `zdsim`, `Starsim.jl`, and `rstarsim` are early. See the conflict-of-interest note below.

### statnet

**Components.** `network`, `ergm`, `tergm`, `networkDynamic`, `statnet.common`, `ergm.ego`, `ergm.count`, `ergm.multi`, `ergm.rank`, `ergm.tapered`, `ergm.userterms`, `ergm.components`, `latentnet`, `lolog`, `tsna`, `ndtv`, `networkLite`, `statnetWeb`, plus the `statnet` meta-package.

**Caveats.** statnet is a **general-purpose statistical network modeling suite**, not an IDD-specific one; it is included because it is the interoperability substrate on which EpiModel's network epidemic models are built, and because `statnet`/`ergm` already appear in [database_tools.md](database_tools.md). Whether general-purpose ecosystems of this kind should appear in an IDD list is a judgement call — see the questions in the compiler's report. The core packages are actively maintained; the `statnet` meta-package itself has not been updated since 2021.

### Vivarium

**Components** (all shipped from the `vivarium-suite` monorepo under a unified `vivarium.*` import namespace): `vivarium-engine`, `vivarium-public-health`, `vivarium-artifact`, `vivarium-cluster-tools`, `vivarium-config-tree`, `vivarium-gbd-mapping`, `vivarium-risk-distributions`, `vivarium-validation`, `vivarium-fuzzy-checker`, `vivarium-profiling`, `vivarium-build-utils`, `vivarium-dependencies` (meta-package), `pytest-vivarium`. `pseudopeople` is a separate downstream application built on Vivarium.

**Caveats — important for anyone citing this.** In 2026 IHME consolidated the previously separate repositories (`vivarium`, `vivarium_public_health`, `vivarium_cluster_tools`, `gbd_mapping`, `layered_config_tree`, `risk_distributions`, `vivarium_testing_utils`, `vivarium_build_utils`) into the monorepo and **archived the originals**. The archiving reflects migration, not abandonment, but any link to `github.com/ihmeuw/vivarium` or to the old PyPI name `vivarium` will look dead. Use `github.com/ihmeuw/vivarium-suite` and `vivarium-engine` instead. Vivarium is a general microsimulation framework used for both IDD and non-communicable disease and nutrition modeling.

## Candidates considered but not listed

| Candidate | Reason for exclusion |
|---|---|
| LASER (Institute for Disease Modeling) | Its packages do interoperate — every disease package declares `laser-core` as a versioned dependency — but LASER has no publication and no documented adoption outside IDM, so it does not meet the tool inclusion criteria in [details.md](details.md), and it was previously removed from this repository on those grounds. Listing an unpublished, single-institution toolkit from the compiler's own institution alongside established ecosystems is also hard to justify given the conflict of interest noted below. Reinstate if the criteria for this file are meant to be independent of the tool criteria. |
| Atomica / Optima | Two related Python engines from one institution rather than an interoperable family — and Optima HIV and Optima Nutrition are not in fact built on Atomica, but on separate legacy engines. |
| R4EPIs | Outbreak and survey *reporting* templates rather than transmission modelling; out of scope for IDD tools. |
| epiworld | Four packages from a single university lab. Passes the technical interoperability test but is too small and too single-institution to constitute an ecosystem. |
| hubverse | A genuine interoperable package suite, but forecast and scenario hubs are treated as communities in this project; listed in [database_communities.md](database_communities.md) instead. |
| pomp | The tightest technical coupling of any candidate (`LinkingTo: pomp`), but there is no umbrella site, no meta-package and no shared branding — the maintainers do not present it as an ecosystem, and asserting one on their behalf would be an editorial invention. |
| MEmilio / SciCompMod | A single, genuinely modular framework in one monorepo, released and versioned as one unit — not a family of independently interoperating packages. Only one of its five Python subpackages is published to PyPI. `SciCompMod` as an organisation also holds unrelated software, so it is not the ecosystem boundary. |
| AlgebraicJulia | A genuine ecosystem (ACSets and Catlab as a shared model representation), but a **general applied-category-theory** one rather than an IDD one; only `AlgebraicPetri.jl` and `AlgebraicABMs.jl` are epidemiology-facing, and both have cooled markedly since DARPA ASKEM funding ended (last pushed August 2025). |
| BEAST 1.x / BEAST X | A monolithic program with a companion tool suite; no package manager or plugin registry, and an XML dialect incompatible with BEAST2. Shares only peripheral tools (Tracer, BEAGLE, FigTree) with the BEAST2 ecosystem. |
| JuliaEpi | Not an ecosystem: a GitHub organisation of ~30 repositories, almost all forks of other people's work, dormant since February 2024, with a 404 website. |
| Pathogen.jl | An individually strong standalone package with no ecosystem around it, and unmaintained since 2022. Listed in [database_tools.md](database_tools.md). |
| flepiMoP (Johns Hopkins IDD) | A single monorepo pipeline (`gempyor` plus in-tree R packages), released as one project. A framework, not an ecosystem. |
| summer / AuTuMN (Monash EMU) | A framework (`summer2`) with two supporting packages by the same group (`computegraph`, `estival`). Below the threshold for a distinct ecosystem, and `summer2` has been dormant since 2024 pending the in-development `summer3`. |
| US CDC Center for Forecasting and Outbreak Analytics | An emerging and plausible ecosystem — `PyRenew`, `pyrenew-hew`, and `forecasttools` do compose — but there is currently no umbrella name, public ecosystem site, or meta-package, and the ~40 `cfa-*` repositories are mostly internal infrastructure. Worth revisiting. Belongs for now in [database_communities.md](database_communities.md). |
| VIMC / Montagu | Consortium infrastructure (`montagu-*`, `orderly`, `vimpact`) for running a modelling consortium, not a toolkit for external modellers. Belongs in [database_communities.md](database_communities.md). |
| NTD Modelling Consortium | `endgame-simulations` is a genuine shared base for the onchocerciasis, trachoma, and schistosomiasis pipelines, but the components have near-zero external usage and most have been dormant since 2024–2025. Below the threshold. |
| orderly / outpack / packit (MRC IDE RESIDE) | A real and well-designed ecosystem, but for reproducible research infrastructure in general, not for IDD specifically. |
| GLEAM / GLEAMviz | Closed source, and distributed as a single client application rather than a family of interoperating components — so it fails on architecture, not only on licensing. Listed as a tool in [database_tools.md](database_tools.md). |
| Swiss TPH malaria tooling | `OpenMalaria`, `openMalariaUtilities`, and `AnophelesModel` are related but loosely coupled; below the threshold for a deliberate interoperable suite. |

## Methodology & caveats

**Snapshot date: 2026-08-07.** Every fact in this file that could be checked mechanically was checked on that date and will drift.

**How this was compiled.** Starting from the four ecosystems named in the project specification (Epiverse-TRACE, EpiModel, Epistorm, Starsim), candidates were gathered from [database_tools.md](database_tools.md), from GitHub organisation listings for every institution appearing in that file, from web searches for "-verse"-style umbrella branding in epidemiology, and from following dependency edges out of known ecosystem packages. Each candidate was then tested against the four criteria above using primary evidence: `gh api` queries for repository existence, `pushed_at` dates, commit counts, star counts, archived status, and licenses; direct reads of `DESCRIPTION`, `pyproject.toml`, `setup.py`, `Project.toml`, and `environment.yml` files to confirm that claimed dependencies actually exist; and project documentation for the stated interoperability model. No component tool is listed here that was not confirmed to exist. Every URL in this file was verified to return HTTP 200 following redirects.

**Maintenance status is reported honestly.** Where an ecosystem's components are largely dormant it is rated **Dormant** (RECON / reconverse) or **Mixed** (Atomica / Optima, R4EPIs) and the specifics are given in the per-ecosystem section, rather than presenting the project as thriving. Conversely, some archived repositories reflect deliberate consolidation rather than abandonment (Vivarium), and this is flagged where it applies. Ratings are judgements about the ecosystem as a whole; individual components within an ecosystem often differ.

**Known limitations.**

- **The boundary is fuzzy and the judgement is mine.** Several entries are defensible either way. `pomp` is listed as an ecosystem even though its maintainers do not describe it as one; `statnet` is listed even though it is not IDD-specific; `epiforecasts` is excluded even though most epidemiologists would casually call it an ecosystem; MEmilio is excluded on a framework-versus-ecosystem distinction that some would reject. Where an entry rests on such a judgement, the per-ecosystem section says so.
- **Recall bias toward English-language, GitHub-hosted, R and Python projects.** Ecosystems built in other languages, hosted outside GitHub, or documented mainly in non-English or grey literature are certainly under-represented. Nothing was found from China, India, Japan, or Francophone Africa, which is more likely a search artifact than an accurate picture.
- **Institutional ecosystems are easier to see than distributed ones.** A suite maintained inside a single GitHub organisation is trivially discoverable; a genuinely interoperable set of packages spread across personal accounts is not. The `pomp` family was nearly missed for exactly this reason.
- **"Ecosystem" is partly a marketing term.** Some projects on this list brand themselves as ecosystems and are; a few brand themselves as ecosystems and barely are; at least one is an ecosystem and does not say so. The Interoperability basis column is the intended defence against this — it records the mechanism, so a reader can disagree with the verdict on the evidence.
- **Component counts are approximate.** They exclude analysis repositories, teaching material, website source, and CI templates, but the line between "a component of the ecosystem" and "a project that uses the ecosystem" is not sharp, and different reasonable choices would shift the counts by several either way.
- **Some component tools appear in more than one ecosystem** (for example `individual` underpins malariaverse but is a general IDD toolkit; `primarycensored` is an epinowcast package that `EpiNow2` depends on). Overlap is real and has not been artificially removed.

**Conflicts of interest.** This file was compiled by Cliff Kerr, who works at the Institute for Disease Modeling and leads development of Starsim, which is one of the listed ecosystems. IDM is also associated with EMOD, another listed ecosystem, with LASER, which is listed among the excluded candidates, and with Sciris, a shared dependency of the Starsim and Atomica ecosystems. Ordering within the table is alphabetical and implies no ranking. Corrections and additions are welcome.
