# Tools excluded from the IDD tools database

Working file, not part of the website data. It records every tool from the earlier compilation that is **not** in [database_tools.md](database_tools.md), with the reason, so that the decisions are reviewable rather than silent.

Note that the criteria have since been relaxed in three ways, and the entries below have been re-checked against the relaxed rules: closed-source tools are now included and labelled, publication is no longer a hard gate where there is strong evidence of use, and "supported" means any activity in the last three years. What remains excluded therefore fails on availability, on maintenance, on evidence of use, or on scope.

Criterion numbering follows details.md: **(2)** published, **(3)** documented, **(4)** evidence of use, **(5)** supported (any activity since 2023-08-07). **(X)** marks the disqualifying categories: general-purpose tools not unique to IDD, single-group tools, guidance and training material, and datasets. Criterion (1) no longer causes exclusion on its own — closed-source tools are included in the database and labelled in the `Licence` column — so the first group below is tools that could not be **obtained** at all, which is a different problem.

### Not obtainable — no distributable artefact located

- **TreeAge Pro** — commercial proprietary software.
- **SurvNet@RKI** — proprietary national surveillance system.
- **be-FAST / be-CSF** — no public source repository.
- **Multi-target Multi-scale Forecasting Framework (UVA)** — no public source repository.
- **ZikaSpread** — project website only; no maintained open repository.
- **ACEMod** — archived Zenodo snapshot only; no maintained open repository.
- **MOCOS** — no public source repository under an open licence located.
- **WES** — no public source repository or licence located.
- **OpenEpi** — web calculators; no source repository with an open licence located.
- **Eir** — GitHub repository no longer exists; PyPI package last released 2021.

### Unmaintained — fails (5)

- **CovidSim** — last repository push 2023-02, before the 2023-08 cutoff.
- **SEIRS+** — last push 2023-03; also no publication.
- **EpiRust** — repository archived 2024-02.
- **STEM (Spatiotemporal Epidemiologic Modeler)** — Eclipse project dormant; no releases in the support window.
- **Pathogen.jl** — last push 2022-09.
- **epidemia** — last push 2022-06; also no `LICENSE` file in the repository.
- **tsiR** — last repository push 2019, last CRAN release 2021-01.
- **earlyR** — last CRAN release and repository push 2020-10.
- **distcrete** — last CRAN release 2017-11.
- **EpiDynamics** — last CRAN release 2020-02.
- **epitools** — last CRAN release 2020-03; also general-purpose epidemiological statistics.
- **SpatialEpi** — last CRAN release 2023-02, before the cutoff.
- **EpiInvert** — last CRAN release 2022-12.
- **phylodyn** — last push 2021-11; also no `LICENSE` file.
- **PhyDyn** — last push 2022-12.
- **skygrowth** — last push 2020-05.
- **FluTE** — last push 2020-09.
- **malariaEquilibrium** — last push 2022-01.
- **Pandemia** — last push 2023-06, before the cutoff; also 0 stars and no publication.
- **Optima TB** — the `optimamodel/optima-tb` repository was last pushed 2018-09 despite the 2021 publication.
- **EpiSoon** — explicitly deprecated by its authors in favour of EpiNow2.
- **statnet (meta-package)** — last push 2021-06; the component `ergm` is active but is excluded as general-purpose.

### No publication and insufficient independent evidence of use — fails (2) and (4)

Publication alone is no longer required. These entries have neither a publication nor enough independent evidence of use to qualify without one; several are components or duplicates of an entry that *is* included.

- **HIVsim (Starsim)** — not a separately published tool; part of the Starsim ecosystem.
- **TBVx** — no publication located and the `kncvtbplus/tbvx` repository is no longer reachable.
- **LEMMA** — no publication located.
- **CDC NWSS-tools** — no software publication located.
- **epiR** — no software publication; also general-purpose epidemiological statistics.
- **Polio model (IDM)** — not separately published; part of the EMOD platform.
- **EMOD-HIV**, **EMOD-TB**, **EMOD-Malaria** — disease-specific `emodpy-*` wrappers around the EMOD platform, with 1–3 stars each; folded into the single EMOD entry.
- **OpenMalaria-MESA** — a hosted deployment of OpenMalaria, not a separate tool.
- **EARS / Farrington** — algorithms implemented inside the `surveillance` package, not a separate tool; duplicate of the surveillance entry.
- **hhh4 / surveillance** — duplicate of the surveillance entry in the previous compilation.
- **EpiModel-networks module** — duplicate of the EpiModel entry.

### Insufficient evidence of use — fails (4)

Evidence of use is assessed cumulatively, with a publication or a documented programme deployment weighing far more than stars. These entries do not reach that bar on any combination of signals.

- **MicroMoB** — 2 stars, 0 forks; also no publication.
- **GEMFsim** — hosted on an institutional page rather than a forge; no observable use metrics and no update since ~2017.

### General-purpose, not unique to IDD — fails (X)

- **pomp** — general statistical inference framework for partially observed Markov processes; built in and for the IDD community, but not IDD-specific.

- **Mesa** — general agent-based modelling framework.
- **NetLogo** — general agent-based modelling platform.
- **RepastHPC** — general parallel agent-based simulation toolkit.
- **Vahana.jl** — general large-scale agent-based simulation framework.
- **BayesianTools** — general Bayesian calibration and MCMC toolbox.
- **AlgebraicPetri.jl** — general compositional Petri-net modelling library.
- **statnet / ergm** — general exponential random graph modelling for networks.
- **adegenet** — general population-genetics multivariate analysis.
- **RevBayes** — general Bayesian phylogenetics, primarily macroevolutionary.
- **BEAGLE** — general high-performance phylogenetic likelihood library.
- **heemod** — general health-economic Markov modelling.
- **hesim** — general health-economic simulation modelling.
- **Synthea** — general synthetic EHR/FHIR patient generator.
- **Optima Nutrition** — nutrition allocative efficiency; not an infectious disease tool.
- **FPsim** — family planning agent-based model; not an infectious disease tool. See [Open questions](#open-questions).

### Datasets and data services — fails (X)

- **FluSurv-Network / FluSight** — forecast hub and its data, not a tool; the associated tooling is covered by the hubverse entry.
- **RSV-MODEL ensemble** — forecast hub, not a tool.
