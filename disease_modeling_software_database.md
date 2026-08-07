# Disease Modeling Software Database

A consolidated inventory of software libraries specifically designed for infectious-disease and epidemiological modeling. Each entry has evidence of multi-group use and/or peer-reviewed publication.

## Schema

| Column | Description |
|---|---|
| Name | Tool name |
| Type | Modeling category (ABM, compartmental, network, phylodynamics, etc.) |
| Language | Implementation language(s) |
| Authors | Originating institution(s) / lab(s) |
| Link | Project page or repo (link text is the bare domain) |
| Usage | A compact adoption metric — GitHub stars, citations, downloads, or country adoption — to indicate scale of use |
| Description | One-sentence summary |

## Methodology & caveats

This database merges two prior compilations (a Claude-authored survey and a GPT-authored survey) into a single deduplicated table. Tools listed have either (a) a peer-reviewed publication, (b) a maintained public repository with external users, or (c) been referenced in two or more independent reviews. The Usage column is best-effort — for repositories without obvious metrics it is left as "—". Star counts and citation totals are point-in-time snapshots (2026-05-06) and will drift.

**Maintenance status** has been verified only for the smaller set of tools covered in the [main summary](README.md), where it is recorded in a dedicated Status column. Elsewhere in this database, entries are annotated as **Unmaintained** only where the maintainers have retired the tool and this is known to us; the absence of such an annotation should not be read as confirmation that a tool is actively maintained.

**Conflicts of interest**: this database was compiled by Cliff Kerr, who works at IDM, leads development of Starsim, and is a co-author on several of the publications referenced. Entries are ordered by category and then arbitrarily within category; no ordering here implies a ranking. Corrections and additions are welcome.

---

## 1. General-purpose / multi-disease frameworks

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| Starsim | ABM / network | Python | IDM / Starsim Hub | [starsim.org](https://starsim.org) | ★ 35 | Modular agent-based disease modeling framework with dynamic networks and multi-disease support. |
| EMOD | ABM / IBM | C++/Python | IDM | [github.com](https://github.com/EMOD-Hub/EMOD) | ★ 105 | **Unmaintained.** Individual-based multi-disease platform (HIV, TB, malaria, polio, measles, COVID). |
| EpiModel | ABM / network / Compartmental | R | Statnet / Emory | [epimodel.org](https://epimodel.org) | ★ 271 | Deterministic, stochastic individual-contact, and stochastic network epidemic models; 125+ studies. |
| EpiHiper | ABM / network | C++ | UVA Biocomplexity / NSSAC | [github.com](https://github.com/NSSAC/EpiHiper) | ★ 6 | High-performance epidemic simulation over large dynamic contact networks; CDC Scenario Modeling Hub. |
| Atomica | Compartmental | Python | Burnet Institute | [github.com](https://github.com/atomicateam/atomica) | ★ 14 | Compartmental engine for disease + cascade modeling, calibration, and scenarios (successor to Optima). |
| MEmilio | ODE/SDE / ABM / Metapopulation | C++/Python | RKI / DLR (Germany) | [github.com](https://github.com/SciCompMod/memilio) | ★ 67 | Modular EpideMIcs simuLatIOn supporting ODE/SDE/IDE/LCT/metapop/ABM; used for German COVID forecasts. |
| STEM | Spatial / Metapopulation | Java | IBM Research / Eclipse Foundation | [eclipse.org](https://www.eclipse.org/stem/) | — | Spatiotemporal Epidemiologic Modeler (Eclipse plugin platform) with documented global public-health use. |
| GLEAM / GLEAMviz | Metapopulation | C++/Java/web | ISI Foundation / Northeastern | [gleamviz.org](https://www.gleamviz.org) | — | Global epidemic and mobility metapopulation simulator using transportation networks. |
| FRED | ABM | C++ | U. Pittsburgh | [github.com](https://github.com/PublicHealthDynamicsLab/FRED) | ★ 81 | Framework for Reconstructing Epidemic Dynamics — synthetic-population ABM for diseases and control strategies. |
| SimInf | Metapopulation / Stochastic | R/C | SLU / Linköping (Sweden) | [github.com](https://github.com/stewid/SimInf) | ★ 36 | Data-driven stochastic disease spread on networks via Gillespie/events. |
| epidemics | Compartmental | R | Epiverse-TRACE / LSHTM | [epiverse-trace.github.io](https://epiverse-trace.github.io/epidemics/) | ★ 17 | Composable compartmental scenario models with curated literature library. |
| Epydemix | Compartmental / Inference | Python | ISI / Northeastern | [github.com](https://github.com/ngozzi/epydemix) | ★ 23 | Compartmental modeling with ABC calibration. |
| Vahana.jl | ABM | Julia | U. Bamberg | [github.com](https://github.com/s-fuerst/Vahana.jl) | ★ 36 | Large-scale agent-based epi modeling. |
| MatSim-EpiSim | ABM | Java | TU Berlin | [github.com](https://github.com/matsim-org/matsim-episim-libs) | ★ 12 | Activity-based mobility epidemic model. |
| RepastHPC | ABM | C++ | Argonne National Lab | [repast.github.io](https://repast.github.io) | ★ 29 | Parallel agent-based simulation toolkit widely used for epi. |
| OpenCOVID | ABM | Julia/Python | Swiss TPH | [github.com](https://github.com/SwissTPH/OpenCOVID) | ★ 74 | Spatial agent-based epidemic framework. |
| Pathogen.jl | ABM / Inference | Julia | academic | [github.com](https://github.com/jangevaare/Pathogen.jl) | — | Bayesian individual-level disease modeling. |
| Mesa | ABM | Python | Project Mesa | [github.com](https://github.com/projectmesa/mesa) | ★ 3.6k | General ABM framework, widely used for epi models. |
| NetLogo | ABM | Scala/Java | Northwestern CCL | [ccl.northwestern.edu](https://ccl.northwestern.edu/netlogo/) | ★ 1.2k | General ABM platform with extensive epi-model library. |
| flepiMoP | Metapopulation / Inference | Python/R | Johns Hopkins IDD | [github.com](https://github.com/HopkinsIDD/flepiMoP) | ★ 11 | Flexible infectious disease modeling and forecasting framework, used for COVID-19 and influenza. |
| Epiabm | ABM | Python/C++ | Cambridge / Imperial (SABS-R3) | [github.com](https://github.com/SABS-R3-Epidemiology/epiabm) | ★ 20 | Open-source epidemiological ABM reimplementing Imperial's CovidSim approach. |
| OpenABM-Covid19 | ABM / network | C/Python | Oxford BDI | [github.com](https://github.com/BDI-pathogens/OpenABM-Covid19) | ★ 128 | Network agent-based simulator of COVID-19 transmission and contact tracing. |
| Covasim | ABM | Python | IDM | [covasim.org](https://covasim.org) | ★ 287 | Agent-based COVID-19 simulator with interventions, calibration, and policy scenarios. |
| SEIRS+ | Network / Compartmental | Python | community (McGee) | [github.com](https://github.com/ryansmcgee/seirsplus) | ★ 675 | Python stochastic SEIRS/network epidemic modeling framework. |
| EpiRust | ABM | Rust | ThoughtWorks | [github.com](https://github.com/thoughtworks/epirust) | ★ 105 | Rust-based epidemic simulation framework. |
| Kendrick | DSL | Pharo / Smalltalk | KendrickOrg | [github.com](https://github.com/KendrickOrg/kendrick) | ★ 52 | Domain-specific language for epidemiological models. |
| Emulsion | DSL / multi-scale stochastic | Python / YAML DSL | INRAE (Picault, Ezanno et al.) | [sourcesup.renater.fr](https://sourcesup.renater.fr/emulsion-public/) | PLOS Comp Biol 2019 (Picault et al.) | Transparent multi-level multi-scale stochastic modeling framework for human, animal, and plant epidemiology with a YAML-based DSL. |

## 2. Compartmental modeling, ODE/SDE solvers, and inference

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| pomp | Inference / SDE | R | U. Michigan (Ionides/King) | [kingaa.github.io](https://kingaa.github.io/pomp/) | ★ 121 | Partially Observed Markov Processes for state-space epi inference. |
| odin | DSL / ODE | R | MRC IDE Imperial | [mrc-ide.github.io](https://mrc-ide.github.io/odin/) | ★ 106 | DSL for ODE/discrete-time models. |
| dust | ODE/SDE / Stochastic | R/C++ | MRC IDE Imperial | [mrc-ide.github.io](https://mrc-ide.github.io/dust/) | ★ 20 | Stochastic simulation engine paired with odin. |
| odin.dust / odin2 | ODE / Stochastic | R | MRC IDE Imperial | [mrc-ide.github.io](https://mrc-ide.github.io/odin2/) | ★ 9 | Fast ODE/discrete sims compiled via dust. |
| mcstate | Inference | R | MRC IDE Imperial | [mrc-ide.github.io](https://mrc-ide.github.io/mcstate/) | ★ 19 | pMCMC / particle filter for odin/dust. |
| epidemia | Compartmental / Inference | R/Stan | Imperial (Bhatt/Flaxman) | [imperialcollegelondon.github.io](https://imperialcollegelondon.github.io/epidemia/) | ★ 49 | Bayesian semi-mechanistic epidemic regression in Stan. |
| PyRoss | Compartmental / Inference | Python | U. Cambridge | [github.com](https://github.com/rajeshrinet/pyross) | ★ 166 | Inference, prediction, and control of epidemics via ODE/SDE. |
| epipack | Compartmental | Python | HU Berlin | [github.com](https://github.com/benmaier/epipack) | ★ 34 | Numerical and symbolic compartmental modeling. |
| BayesianTools | Inference | R | academic (Hartig) | [github.com](https://github.com/florianhartig/BayesianTools) | ★ 129 | MCMC tooling commonly used for epi inference. |

## 3. Rt estimation, nowcasting, and forecasting

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| EpiEstim | Rt estimation | R | MRC IDE Imperial | [github.com](https://github.com/mrc-ide/EpiEstim) | ★ 102 | Time-varying Rt from incidence data using the Cori et al. method. |
| EpiNow2 | Rt / nowcasting / forecasting | R/Stan | epiforecasts / LSHTM | [epiforecasts.io](https://epiforecasts.io/EpiNow2/) | ★ 134 | Bayesian real-time infection estimation, Rt estimation, and short-term forecasts. |
| epinowcast | Nowcasting / Rt | R/Stan | epiforecasts | [package.epinowcast.org](https://package.epinowcast.org) | — | Hierarchical Bayesian nowcasting of right-truncated infectious-disease surveillance data. |
| estimateR | Rt estimation | R | ETH Zurich | [github.com](https://github.com/covid-19-Re/estimateR) | — | Rt estimation with deconvolution from clinical or wastewater incidence data. |
| R0 | Rt estimation | R | Hospices Civils Lyon | [cran.r-project.org](https://cran.r-project.org/package=R0) | — | Toolbox of methods to estimate basic and real-time reproduction numbers from epidemic curves. |
| earlyR | Rt estimation | R | RECON | [repidemicsconsortium.org](https://www.repidemicsconsortium.org/earlyR/) | — | Likelihood-based Rt estimation during the early stage of an outbreak. |
| projections | Forecasting | R | RECON | [repidemicsconsortium.org](https://www.repidemicsconsortium.org/projections/) | — | Short-term incidence projections from past incidence, serial interval, and R. |
| EpiSoon | Forecasting | R | epiforecasts | [epiforecasts.io](https://epiforecasts.io/EpiSoon/) | — | Short-term Rt-based forecasting framework (deprecated in favor of EpiNow2). |
| EpiLPS | Rt estimation | R | UCLouvain | [cran.r-project.org](https://cran.r-project.org/package=EpiLPS) | — | Laplacian-P-splines Bayesian framework for fast Rt estimation. |
| scoringutils | Forecast scoring | R | epiforecasts | [epiforecasts.io](https://epiforecasts.io/scoringutils/) | ★ 56 | Utilities for evaluating and scoring probabilistic epidemiological forecasts. |
| Multi-target Multi-scale Forecasting Framework | Forecasting (ensemble) | Python/R | UVA Biocomplexity | [covid19-forecast.uvadsos.io](http://covid19-forecast.uvadsos.io/) | — | Ensemble framework (AR, Kalman, LSTM, compartmental) producing UVA hub forecast submissions. |
| PatchSim | Forecasting (metapopulation) | Python | UVA NSSAC | [github.com](https://github.com/NSSAC/PatchSim) | — | National-scale metapopulation SEIR simulator used for influenza and COVID-19 forecasting. |
| NobBS | Nowcasting | R | Harvard / Lipsitch lab | [github.com](https://github.com/sarahhbellum/NobBS) | — | Nowcasting by Bayesian Smoothing for delayed disease reporting (McGough et al. 2020). |

## 4. Outbreak analytics & data toolkits

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| incidence / incidence2 | Line-list tools | R | RECON / Epiverse-TRACE | [reconverse.org](https://www.reconverse.org/incidence2/) | ★ 17 | Compute, handle, and visualize incidence curves from line-list data. |
| linelist | Line-list tools | R | Epiverse-TRACE | [reconverse.org](https://www.reconverse.org/linelist/) | ★ 10 | Tagging, validation, and safeguarding of epidemiological line-list variables. |
| epicontacts | Outbreak analytics | R | RECON | [repidemicsconsortium.org](https://www.repidemicsconsortium.org/epicontacts/) | — | Data structures and visualization for contact-tracing data. |
| outbreaker2 | Outbreak reconstruction | R | RECON | [github.com](https://github.com/reconhub/outbreaker2) | ★ 31 | Bayesian reconstruction of who-infected-whom from epidemiological and genomic data. |
| o2geosocial | Outbreak reconstruction | R | (academic) | [github.com](https://github.com/alxsrobert/o2geosocial) | — | Extension of outbreaker2 incorporating spatial and age data. |
| TransPhylo | Outbreak analytics | R | Oxford (Didelot) | [github.com](https://github.com/xavierdidelot/TransPhylo) | ★ 63 | Inference of transmission trees from dated pathogen phylogenies. |
| outbreaks | Outbreak data | R | RECON | [github.com](https://github.com/reconverse/outbreaks) | — | Curated collection of empirical outbreak datasets for teaching and benchmarking. |
| epitrix | Outbreak analytics | R | RECON | [github.com](https://github.com/reconhub/epitrix) | — | Helper functions and small utilities for outbreak analysis workflows. |
| distcrete | Outbreak analytics | R | RECON | [github.com](https://github.com/reconhub/distcrete) | — | Discretized delay distributions (serial interval, generation time) for epi models. |
| epiparameter | Outbreak analytics | R | Epiverse-TRACE | [epiverse-trace.github.io](https://epiverse-trace.github.io/epiparameter/) | ★ 35 | Curated library plus classes and helpers for working with epidemiological parameters. |
| simulist | Line-list tools | R | Epiverse-TRACE | [epiverse-trace.github.io](https://epiverse-trace.github.io/simulist/) | ★ 10 | Simulate realistic outbreak line-list and contact-tracing data. |
| finalsize | Outbreak analytics | R | Epiverse-TRACE | [epiverse-trace.github.io](https://epiverse-trace.github.io/finalsize/) | ★ 13 | Compute final epidemic size in heterogeneous populations with structured contacts. |

## 5. Network-based epidemic modeling

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| EoN (Epidemics on Networks) | Network ABM | Python | Joel Miller / community | [github.com](https://github.com/springer-math/Mathematics-of-Epidemics-on-Networks) | ★ 165 | SIS/SIR simulation library for spreading processes on networks. |
| NDlib | Network diffusion | Python | CNR Italy (Rossetti et al.) | [ndlib.readthedocs.io](https://ndlib.readthedocs.io) | ★ 296 | Network Diffusion library implementing many epidemic and opinion-dynamics models. |
| statnet / ergm | ERGM | R | U. Washington / Statnet | [statnet.org](https://statnet.org) | ★ 106 | Exponential random graph models for fitting and simulating contact networks. |
| EpiModel-networks module | Network ABM | R | Statnet / Emory (Jenness et al.) | [epimodel.org](https://epimodel.org) | ★ 271 | Stochastic network epidemic models built on temporal ERGMs. |
| socialmixr | Contact matrices | R | epiforecasts | [github.com](https://github.com/epiforecasts/socialmixr) | ★ 43 | Derive age-structured contact matrices from POLYMOD-style surveys. |
| contactdata | Contact matrices | R | community | [cran.r-project.org](https://cran.r-project.org/package=contactdata) | — | Prem et al. synthetic contact matrices for 152 countries. |

## 6. Phylodynamics & genomic epidemiology

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| BEAST | Phylodynamics | Java | U. Edinburgh / Auckland (Drummond, Rambaut) | [beast.community](https://beast.community) | Drummond & Rambaut 2007 >20k citations | Bayesian Evolutionary Analysis Sampling Trees for molecular phylogenetic and phylodynamic inference. |
| BEAST2 | Phylodynamics | Java | BEAST2 dev team (Bouckaert et al.) | [beast2.org](https://www.beast2.org) | Bouckaert 2014 >10k citations | Modular successor to BEAST with a package manager and extensible model platform. |
| Nextstrain (Augur / Auspice) | Genomic epi | Python / JS | Bedford / Neher labs | [nextstrain.org](https://nextstrain.org) | ★ 276 (Augur); Hadfield 2018 widely cited | Real-time pathogen evolution dashboard plus Augur bioinformatics pipeline. |
| Nextclade | Genomic epi | TypeScript / Rust | Neher Lab (Aksamentov et al.) | [clades.nextstrain.org](https://clades.nextstrain.org) | ★ 253 | Clade assignment, mutation calling, and QC for viral genomes. |
| TreeTime | Phylogenetics | Python | Neher Lab (Sagulenko et al.) | [github.com](https://github.com/neherlab/treetime) | ★ 251 | Maximum-likelihood time-tree and ancestral-sequence inference. |
| Pangolin | Genomic epi | Python | Cov-Lineages / Edinburgh (Rambaut, O'Toole et al.) | [github.com](https://github.com/cov-lineages/pangolin) | ★ 453 | SARS-CoV-2 Pango lineage assignment tool. |
| Civet | Genomic epi | Python | Cov-Lineages / Edinburgh | [github.com](https://github.com/artic-network/civet) | ★ 50 | Phylogenetic placement and contextual reports for outbreak sequences. |
| Scorpio | Genomic epi | Python | Cov-Lineages | [github.com](https://github.com/cov-lineages/scorpio) | ★ 39 | SNP-based variant constellation calling. |
| UShER | Phylogenetics | C++ | UCSC (Turakhia et al.) | [github.com](https://github.com/yatisht/usher) | ★ 140; ~455+ citations | Ultrafast Sample placement on Existing tRees for real-time phylogenetics. |
| phylodyn | Phylodynamics | R | Karcher / Suchard | [github.com](https://github.com/mdkarcher/phylodyn) | ★ 20 | Bayesian nonparametric phylodynamic inference of effective population size. |
| phydynR | Phylodynamics | R | Volz lab (Imperial) | [github.com](https://github.com/emvolz-phylodynamics/phydynR) | ★ 14 | R tools for structured-coalescent phylodynamic inference. |
| PhyDyn | Phylodynamics | Java | Imperial (Volz) | [github.com](https://github.com/mrc-ide/PhyDyn) | ★ 21 | BEAST2 package for structured-coalescent phylodynamics. |
| MASCOT | Phylodynamics | Java | Müller / Stadler (ETH) | [github.com](https://github.com/nicfel/Mascot) | ★ 12 | Marginal Approximation of the Structured COalescenT in BEAST2. |
| skygrowth | Phylodynamics | R | Imperial (Volz) | [github.com](https://github.com/mrc-ide/skygrowth) | ★ 22 | Phylodynamic effective-population-size and growth-rate inference. |
| RevBayes | Phylogenetics | C++ | Höhna et al. | [revbayes.github.io](https://revbayes.github.io) | ★ 82 | Bayesian phylogenetic inference using graphical-model specification language. |
| BEAGLE | Phylogenetics | C++ | community | [github.com](https://github.com/beagle-dev/beagle-lib) | ★ 145 | High-performance likelihood library used by BEAST, BEAST2, and MrBayes. |
| ARTIC pipeline | Genomic epi | Python / Nextflow | ARTIC network | [artic.network](https://artic.network) | — | Reference protocols and Nextflow pipelines for amplicon-based viral genomics. |
| adegenet | Phylogenetics | R | Imperial (Jombart) | [github.com](https://github.com/thibautjombart/adegenet) | ★ 201; Jombart 2008 widely cited | Multivariate analysis of genetic markers including DAPC. |

## 7. Spatial epidemiology / disease mapping

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| SpatialEpi | Spatial / cluster detection | R | A. Kim, J. Wakefield (U. Washington) | [cran.r-project.org](https://cran.r-project.org/package=SpatialEpi) | CRAN since 2012 | Methods and example datasets for cluster detection and disease mapping. |
| DClusterm | Cluster detection | R | V. Gomez-Rubio, P. Moraga | [cran.r-project.org](https://cran.r-project.org/package=DClusterm) | — | Model-based detection of disease clusters via GLM model selection over candidate cluster dummies. |
| hhh4 / surveillance | Spatio-temporal endemic-epidemic | R | M. Höhle, S. Meyer, L. Held (LMU / RKI / U. Zurich) | [cran.r-project.org](https://cran.r-project.org/package=surveillance) | Meyer-Held-Höhle JSS 2017 widely cited | Endemic-epidemic multivariate count time-series models for areal infectious-disease surveillance data. |
| MAP / malariaAtlas | Disease mapping / geostatistical | R / Python | Malaria Atlas Project (Oxford BDI) | [malariaatlas.org](https://malariaatlas.org) | ★ 32; underpins WHO malaria estimates | R interface and modeled raster/parasite-rate datasets from the Malaria Atlas Project. |

## 8. Surveillance, aberration detection, and genomic surveillance

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| surveillance | Surveillance / aberration detection | R | M. Höhle, S. Meyer, L. Held (LMU / RKI) | [surveillance.r-forge.r-project.org](https://surveillance.r-forge.r-project.org) | JSS 2017 widely cited | Temporal and spatio-temporal monitoring of count data with outbreak/aberration detection algorithms. |
| EARS / Farrington | Aberration detection | R (within `surveillance`) | CDC (EARS) / PHE (Farrington) | [cran.r-project.org](https://cran.r-project.org/package=surveillance) | Standard algorithms in public-health practice | Classic early-aberration / Farrington-flexible algorithms for outbreak signal detection in routine count series. |
| SaTScan | Cluster detection / scan statistic | C++ / GUI | M. Kulldorff (Harvard / NCI) | [satscan.org](https://www.satscan.org) | Kulldorff 1997 most-cited paper in its journal; widely deployed by public-health agencies | Spatial, temporal, and space-time scan statistics for detecting disease clusters and emerging outbreaks. |
| FluView / DELPHI Epidata | Surveillance data API | Python / R | CMU DELPHI group | [cmu-delphi.github.io](https://cmu-delphi.github.io/delphi-epidata/) | ★ 104 | Open API providing real-time and historical US influenza/COVID surveillance signals for forecasting. |
| Epi Info | Field epi | C# / Web | CDC | [cdc.gov](https://www.cdc.gov/epiinfo/) | >1M users worldwide | Free CDC desktop/web/mobile package for outbreak investigations, surveys, and basic epi analysis. |
| SurvNet@RKI | Surveillance | (proprietary) | Robert Koch Institute, Germany | [rki.de](https://www.rki.de) | ~300k case reports/yr through national system | Multistate electronic notifiable-disease and outbreak reporting system used across all German health departments. |
| OpenEpi | Field epi / public-health statistics | JavaScript (web) | A. Dean, K. Sullivan, M. M. Soe (Emory) | [openepi.com](https://www.openepi.com/) | >1M hits/yr from 155+ countries | Free web-based epidemiologic and statistical calculators for public health summary-data analysis. |
| epiR | Public-health epi statistics | R | M. Stevenson, E. Sergeant (U. Melbourne) | [cran.r-project.org](https://cran.r-project.org/package=epiR) | ~18k CRAN downloads (recent) | Tools for analyzing epidemiological data: measures of association, risk, sample size, and diagnostic-test evaluation. |
| epitools | Public-health epi statistics | R | T. Aragon (UC Berkeley) | [cran.r-project.org](https://cran.r-project.org/package=epitools) | ~10k CRAN downloads (recent) | Basic epidemiological calculations including rate/risk ratios and 2x2 / multi-way contingency-table analyses. |

## 9. Disease-specific: HIV

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| Spectrum / EPP / AIM | Compartmental | C++ / GUI | Avenir Health / UNAIDS | [avenirhealth.org](https://avenirhealth.org/software-spectrum.php) | Used by 161+ countries for UNAIDS estimates (131+ via AIM in 2025 round) | UNAIDS official tool (umbrella suite bundling AIM, Goals, TIME, FamPlan, DemProj, LiST modules) combining surveillance, survey, and program data to produce national HIV estimates and projections. |
| Goals / Goals-ART | Allocative efficiency | Spectrum module | Avenir Health | [avenirhealth.org](https://avenirhealth.org/software-spectrum.php) | Used in 30+ countries via Spectrum | Spectrum-based resource-allocation model for HIV programs and ART scale-up planning. |
| Thembisa | Compartmental | R / Excel | U. Cape Town (Johnson) | [thembisa.org](https://thembisa.org) | Source of UNAIDS South Africa estimates since 2017 | Deterministic compartmental model of the South African HIV epidemic at national and provincial levels. |
| MicroCOSM | HIV ABM | R | SACEMA / UCT (Johnson) | [github.com](https://github.com/leighjohnson/MicroCOSM) | bioRxiv 310763; cited in SA HIV/structural-driver literature | Agent-based model of social and structural drivers of HIV/STIs and reproductive health in South Africa. |
| ECDC HIV Modelling Tool / hivPlatform | Back-calculation | R | ECDC | [github.com](https://github.com/EU-ECDC/hivPlatform) | Used by EU/EEA national HIV surveillance teams | Back-calculation of HIV incidence and undiagnosed populations from surveillance data. |
| HIV Synthesis | HIV ABM | Custom (Fortran-style) | UCL (Phillips) | [ucl.ac.uk](https://www.ucl.ac.uk/global-health/research/z-research/hiv-synthesis-model) | Phillips group has 100k+ citations across HIV work | Individual-based stochastic HIV model used for PrEP, ART resistance, and self-testing policy analyses in sub-Saharan Africa. |
| PopART-IBM | HIV ABM | C | Imperial / Oxford BDI | [github.com](https://github.com/BDI-pathogens/POPART-IBM) | PLOS Comp Biol 2021 (Pickles et al.) | Highly efficient stochastic individual-based simulation developed for the HPTN 071 (PopART) trial. |
| EMOD-HIV | HIV ABM | C++ / Python | IDM | [github.com](https://github.com/EMOD-Hub/emodpy-hiv) | EMOD platform paper widely cited (Bershteyn 2018) | **Unmaintained.** IDM agent-based HIV model with detailed cascade and care pathway support, built on the EMOD platform. |
| HIVsim (Starsim) | HIV ABM | Python | Starsim Hub | [starsim.org](https://starsim.org) | Part of Starsim ecosystem (2024) | Starsim-based individual-based HIV transmission and intervention model. |
| Optima HIV | Allocative efficiency | Python | Optima Consortium / Burnet Institute | [optimamodel.com](https://optimamodel.com/hiv/) | Applied in 40+ countries (23 govt-led analyses with World Bank/UNDP) | Compartmental HIV epidemic and allocative-efficiency model for program prioritization, supported by World Bank, UN, and CDC. |
| CEPAC (HIV-CDM) | Microsimulation | C++ | MGH / Harvard MPEC | [massgeneral.org](https://www.massgeneral.org/medicine/mpec/research/cepac) | Hundreds of cost-effectiveness publications | State-transition Monte Carlo microsimulation of HIV disease progression for clinical and policy cost-effectiveness analysis. |
| AIDS Epidemic Model (AEM) | Compartmental | Spectrum module | East-West Center (Brown) | [eastwestcenter.org](https://www.eastwestcenter.org/projects/improving-hiv-response-impacts-and-building-national-policy-analysis-capacity) | Used by 13 Asian countries | Process-based HIV model for concentrated epidemics, used widely in Asia-Pacific national HIV estimates. |
| SimpactCyan | HIV ABM | C++ / R / Python | Hasselt U. / SACEMA (Liesenborgs) | [github.com](https://github.com/j0r1/simpactcyan) | Sci Rep 2019 (Liesenborgs et al.); ~150+ citations | Open-source individual-based simulator for HIV in dynamic sexual networks. |
| STDSIM | Microsimulation | C++ | Erasmus MC (de Vlas) | [pubsonline.informs.org](https://pubsonline.informs.org/doi/10.1287/inte.28.3.84) | Used since 1998; widely cited in African HIV/STI work | Stochastic microsimulation of heterosexual HIV/STI transmission, developed at Erasmus University Rotterdam. |

## 10. Disease-specific: Tuberculosis

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| TIME Impact | Compartmental | C++ / GUI | Avenir Health / LSHTM / KNCV | [avenirhealth.org](https://avenirhealth.org/software-time.php) | Used in South Africa, Ghana, and other countries for TB investment cases | Spectrum-nested TB transmission model for impact, cost-effectiveness, and strategic planning. |
| EMOD-TB | TB ABM | C++ / Python | IDM | [github.com](https://github.com/EMOD-Hub) | EMOD platform paper widely cited | **Unmaintained.** IDM individual-based TB model with HIV co-infection, drug resistance, and treatment dynamics. |
| TBVx | Vaccine impact | Python | KNCV / TB Modelling | [github.com](https://github.com/kncvtbplus/tbvx) | Used in PLOS Medicine TB vaccine cost-effectiveness studies | Country-level vaccine-impact TB transmission model. |
| Optima TB | Allocative efficiency | Python | Optima Consortium / Burnet Institute | [optimamodel.com](https://optimamodel.com/tb/applications.html) | PLOS Comp Biol 2021; applied in Malawi, Indonesia, South Africa, Mozambique, Belarus, Tajikistan, Kyrgyz Republic | Compartmental TB transmission and allocative-efficiency model for optimizing TB spending. |

## 11. Disease-specific: Malaria

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| OpenMalaria | Malaria ABM | C++ | Swiss TPH / Kids Research Institute Australia | [github.com](https://github.com/SwissTPH/openmalaria) | ★ 84; widely used by malaria modelers worldwide | Stochastic individual-based simulator of P. falciparum transmission, morbidity, and intervention impact. |
| malariasimulation | Malaria ABM | R / C++ | Imperial MRC IDE | [github.com](https://github.com/mrc-ide/malariasimulation) | ★ 21; basis of Imperial WHO/Global Fund analyses | Imperial individual-based model of P. falciparum malaria for vector control and intervention deployment. |
| malariaEquilibrium | Equilibrium solver | R | Imperial MRC IDE | [github.com](https://github.com/mrc-ide/malariaEquilibrium) | ★ 3 | R package solving the equilibrium of the Imperial malaria transmission model. |
| AnophelesModel | Vector model | R | Swiss TPH | [github.com](https://github.com/SwissTPH/AnophelesModel) | ★ 7 | R package modeling Anopheles bionomics and vector control product effects on malaria transmission. |
| EMOD-Malaria | Malaria ABM | C++ / Python | IDM | [github.com](https://github.com/EMOD-Hub/emodpy-malaria) | EMOD platform widely cited | **Unmaintained.** IDM individual-based malaria model with mechanistic vector and within-host components. |
| Skeeter Buster | Vector model | C++ | NC State University | [journals.plos.org](https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0000508) | PLOS NTD 2009; SB2 update 2022 | Stochastic, spatially explicit Aedes aegypti (and Anopheles) population model for vector control and gene-drive studies. |
| OpenMalaria-MESA | Malaria ABM | C++ | MESA Malaria | [mesamalaria.org](https://mesamalaria.org) | MESA knowledge hub deployment | Hosted deployment of OpenMalaria for the MESA malaria modeling community. |
| MicroMoB | Vector-borne | R | dd-harp consortium | [github.com](https://github.com/dd-harp/MicroMoB) | ★ 2 | Modular framework for mosquito-borne disease modeling with pluggable components. |
| MGDrivE | Vector model / gene drive | R / C++ | Marshall Lab, UC Berkeley | [marshalllab.github.io](https://marshalllab.github.io/MGDrivE/) | Three PLOS Comp Biol / Methods Ecol Evol papers (2020, 2021, 2024) | Spatially explicit simulation framework for mosquito gene-drive systems with seasonality and epidemiological dynamics. |

## 12. Disease-specific: Neglected Tropical Diseases (NTD)

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| ONCHOSIM | Stochastic IBM | Pascal/Python | Erasmus MC | [github.com](https://github.com/NTD-Modelling-Consortium) | Foundational onchocerciasis model; used by WHO/OCP since 1990 | Long-running individual-based simulator of onchocerciasis transmission and ivermectin MDA control. |
| EPIONCHO-IBM | Stochastic IBM | R | Imperial / Warwick (MRC GIDA) | [github.com](https://github.com/mrc-ide/EPIONCHO.IBM) | NTD-MC core model; multiple PLoS NTDs publications | Individual-based onchocerciasis model accounting for exposure heterogeneity and density dependence. |
| LYMFASIM | Stochastic IBM | Pascal/Python | Erasmus MC | [github.com](https://github.com/NTD-Modelling-Consortium) | NTD-MC core LF model | Stochastic microsimulation of lymphatic filariasis transmission and MDA. |
| TRANSFIL | Stochastic IBM | C++ | Warwick / NTD-MC | [github.com](https://github.com/NTD-Modelling-Consortium/transfil) | NTD-MC core LF model | Lymphatic filariasis transmission model used for WHO 2030 goal projections. |
| SCHISTOX | Stochastic IBM | Julia | University of Oxford | [github.com](https://github.com/mattg-epi/SCHISTOX) | Published PLoS NTDs / Epidemics | Individual-based schistosomiasis model with R interface, supporting MDA and vaccine scenarios. |
| SCHISTO (Imperial) | Compartmental | R | Imperial College London | [imperial.ac.uk](https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/) | NTD-MC schistosomiasis core model | Compartmental schistosomiasis transmission model used in NTD-MC analyses. |
| TRACHOMA-AMIS | Stochastic IBM | Python/R | LSHTM / Warwick | [github.com](https://github.com/NTD-Modelling-Consortium) | NTD-MC core trachoma model | Stochastic individual-based trachoma model with AMIS calibration framework. |
| WORMSIM | Stochastic IBM | Pascal/Python | Erasmus MC | [github.com](https://github.com/NTD-Modelling-Consortium) | Used for STH WHO 2030 projections | Generalized individual-based modelling framework for soil-transmitted helminths. |
| HAT model (Warwick/Imperial) | Compartmental | R | Warwick (Rock) / Imperial | [warwick.ac.uk](https://warwick.ac.uk/fac/cross_fac/zeeman_institute/new_research/combatting_disease/hat/) | HAT MEPP project; informs DRC strategy | Mechanistic gambiense human African trypanosomiasis model for elimination strategy. |
| LeishMod | Compartmental | R | LSHTM / Warwick | — | NTD-MC visceral leishmaniasis core | Visceral leishmaniasis transmission model for elimination on the Indian subcontinent. |
| Chagas-EpiPath | Compartmental | R | NTD-MC | [github.com](https://github.com/NTD-Modelling-Consortium) | NTD-MC Chagas core | Chagas disease transmission and control models. |

## 13. Disease-specific: COVID-19 / respiratory pathogens

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| CovidSim | Stochastic IBM | C++ | Imperial College (Ferguson group) | [github.com](https://github.com/mrc-ide/covid-sim) | ★ 1.2k; informed UK lockdown policy | Imperial pandemic microsimulation that drove UK/US COVID-19 NPI policy in March 2020. |
| JUNE | ABM | Python/C++ | Durham IPPP / IHME | [github.com](https://github.com/IDAS-Durham/JUNE) | ★ 50; Royal Society Open Sci 2021 | Geographically resolved individual-based epidemic model applied to UK and Cox's Bazar refugee camp. |
| ACEMod | ABM | C++ | University of Sydney | [zenodo.org](https://zenodo.org/records/5773908) | Nat. Comms. 2020; Australian COVID policy | Census-based 19.8M-agent epidemic model used for Australian flu and COVID-19 mitigation. |
| Episimmer | ABM | Python | IIIT Hyderabad / HealthBadge | [github.com](https://github.com/healthbadge/episimmer) | Deployed in Campus RAKSHAK at IITs/IIITs | Modular institutional reopening simulator for testing class scheduling and intervention strategies. |
| Pandemia | Stochastic IBM | Python | PandemiaProject (Luxembourg/UK) | [github.com](https://github.com/PandemiaProject/pandemia) | Successor to ABMlux Luxembourg model | Scalable individual-based pandemic simulator supporting multiple geographical regions. |
| FluTE | Stochastic IBM | C++ | Fred Hutchinson Cancer Research Center (Chao) | [github.com](https://github.com/dlchao/FluTE) | PLoS Comp Biol 2010, ~700+ citations | Influenza individual-based model calibrated to 1957 and 2009 pandemic strains. |
| MOCOS | Microsim | C++/Julia | Wroclaw / international | [mocos.pl](http://mocos.pl) | Informed Polish/Lower Silesia COVID policy | Household-resolved microsimulation of COVID-19 used by Polish, German, and Filipino teams. |
| CoMo Consortium | Compartmental | R | Oxford / Cornell | [como.bsg.ox.ac.uk](https://www.como.bsg.ox.ac.uk) | 40+ countries in consortium | Age-structured SEIR app with web interface used by country-level modelling teams. |
| LEMMA | Bayesian compartmental | R/Stan | UCSF | [github.com](https://github.com/LocalEpi/LEMMA) | California county forecasts during pandemic | Bayesian local-epidemic model fitting hospitalizations, ICU, deaths, cases, and seroprevalence. |
| FluSurv-Network / FluSight | Ensemble forecasting | R/Python | CDC / Reich Lab (UMass) | [reichlab.io](https://reichlab.io/flusightnetwork) | Adopted by CDC as primary flu forecast 2018+ | Multi-team collaborative ensemble forecasts of US influenza adopted by CDC. |
| RSV-MODEL ensemble | Ensemble forecasting | R | CDC / MIDAS / Hopkins IDD | [rsvforecasthub.org](https://rsvforecasthub.org/) | Operational US RSV Forecast Hub | Collaborative weekly RSV hospitalization forecasts feeding CDC RSV-NET. |

## 14. Disease-specific: STIs, vector-borne, vaccine-preventable, other

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| HPVsim | ABM | Python | IDM / Starsim Hub | [hpvsim.org](https://hpvsim.org) | PLoS Comp Biol 2024; PyPI distributed | Agent-based HPV transmission and cervical disease model for vaccination and screening analysis. |
| FPsim | ABM | Python | IDM / Starsim Hub | [fpsim.org](https://fpsim.org) | npj Women's Health 2023 | Woman-centered family planning ABM with contraceptive use, fertility, and empowerment metrics. |
| STIsim | ABM | Python | Starsim Hub | [github.com](https://github.com/starsimhub/stisim) | PyPI distributed; Zimbabwe POC application | Adaptable Starsim-based model of co-transmitting STIs (HIV, syphilis, chlamydia, gonorrhea, BV). |
| Polio model (IDM) | ABM | C++/Python | IDM | [github.com](https://github.com/EMOD-Hub) | Used in Kano state polio analyses | EMOD-based agent simulation of polio transmission and OPV/IPV vaccination campaigns. |
| ZikaSpread | Stochastic metapopulation | Python | Northeastern / ISI Foundation | [zika-model.org](http://www.zika-model.org/) | PNAS 2017 Americas Zika spread study | Data-driven global stochastic metapopulation model of Zika in the Americas. |
| Spectrum FamPlan / DemProj / GBM | Demographic / family-planning projection | C++ | Avenir Health | [avenirhealth.org](https://avenirhealth.org/software-spectrum.php) | 193 countries / regions; UN Population Division integration; FP2030/USAID country planning | Spectrum modules: DemProj (cohort-component demographic projections), FamPlan (contraceptive use and FP service needs), GBM (Goals Burden Model for HIV intervention impact and resource needs). |
| LiST (Lives Saved Tool) | Intervention impact model | C++/GUI | JHSPH / Avenir Health | [livessavedtool.org](https://www.livessavedtool.org) | Default coverage data for ~80 LMICs; BMC Public Health 2011 supplement | Multi-cause MNCH/nutrition/WASH intervention impact model on child and maternal mortality. |

## 15. Veterinary / animal / zoonotic disease modeling

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| NAADSM / ADSM | Veterinary ABM | C / Python | USDA APHIS / CFIA / Colorado State | [github.com](https://github.com/NAVADMC/ADSM) | Open-source under USDA; used in North America for FMD planning | North American Animal Disease Spread Model simulating disease spread and control in livestock herds. |
| AADIS | Hybrid livestock ABM | C# / Java | UNE / CSIRO / DAFF | [aadis.org](https://aadis.org/) | Australia's official EAD decision-support tool (FMD, ASF, LSD, AI) | Hybrid equation-based + agent-based national model of animal disease spread for emergency preparedness. |
| be-FAST / be-CSF | Livestock spread | C++ | UCM Madrid (MOMAT) | [ucm.es](https://www.ucm.es/momat/classical-swine-fever) | Used for CSF/ASF risk assessment in Spain, Bulgaria, EU | Spatial hybrid IBM + SI model for between-farm and within-farm CSF/ASF spread. |
| EpiContactTrace | Contact tracing | R | SLU Sweden (Nöremark, Widgren) | [cran.r-project.org](https://cran.r-project.org/package=EpiContactTrace) | BMC Vet Res 2014 widely cited; on CRAN | R package for forward/backward contact tracing of livestock movements during disease outbreaks. |

## 16. Wastewater & environmental epidemiology

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| EpiSewer | Wastewater Rt | R / Stan | Adrian Lison, ETH Zurich | [github.com](https://github.com/adrian-lison/EpiSewer) | ★ 23 | Bayesian generative model estimating Rt and other epi parameters from wastewater concentration time series. |
| ern | Wastewater Rt | R | PHAC-NML (Champredon et al.) | [cran.r-project.org](https://cran.r-project.org/package=ern) | On CRAN; PLOS One 2024 | Effective reproduction number estimation from wastewater and clinical surveillance data (wraps EpiEstim). |
| WES | Wastewater toolkit | R | community | [r-wes.com](https://www.r-wes.com) | — | Wastewater & environmental sampling analytical toolkit. |
| CDC NWSS-tools | Wastewater pipelines | Python / R | US CDC | [github.com](https://github.com/CDCgov/NWSS) | Used by US National Wastewater Surveillance System; jurisdictions across all 50 states | National wastewater surveillance pipelines (WVAL calculation, Aquascope bioinformatics) for SARS-CoV-2, influenza, RSV. |

## 17. Microsimulation, health-economics, and decision-analytic frameworks

| Name | Type | Language | Authors | Link | Usage | Description |
|---|---|---|---|---|---|---|
| heemod | CEA / Markov | R | Filipović-Pierucci, Zarca, Durand-Zaleski (AP-HP) | [cran.r-project.org](https://cran.r-project.org/package=heemod) | On CRAN; widely used in HE textbooks/teaching | Markov state-transition health-economic evaluation package with PSA, DSA, EVPI. |
| hesim | CEA / simulation | R / C++ (Rcpp) | Devin Incerti, Jeroen Jansen | [hesim-dev.github.io](https://hesim-dev.github.io/hesim/) | On CRAN; arXiv 2102.09437 | Modular fast simulation framework for cohort/individual state-transition and partitioned-survival HE models. |
| TreeAge Pro | Decision tree / Markov | proprietary | TreeAge Software | [treeage.com](https://www.treeage.com) | 30+ years of commercial use; standard tool for HEOR, regulatory submissions | Commercial decision-tree and Markov modeling environment for HE, clinical, and business decision analysis. |
| CEPAC | Microsimulation (HIV) | C++ | MGH / Harvard MPEC | [massgeneral.org](https://www.massgeneral.org/medicine/mpec) | 100+ peer-reviewed publications on HIV/TB CEA in US and LMIC | Cost-Effectiveness of Preventing AIDS Complications microsimulation of HIV disease and care. |
| Vivarium | Microsimulation | Python | IHME | [github.com](https://github.com/ihmeuw/vivarium) | Used by IHME for GBD-linked simulations | GBD-driven microsimulation framework for population-health interventions. |
| Synthea | Synthetic patients | Java | MITRE | [github.com](https://github.com/synthetichealth/synthea) | De facto standard for synthetic FHIR/EHR data in US health IT | Synthetic Patient Population Simulator generating realistic HL7/FHIR EHR data. |
| SynthPops | Synthetic populations | Python | IDM | [github.com](https://github.com/synthpops/synthpops) | ★ 47; used with Covasim, FPsim, Starsim | Generates synthetic populations with household, school, and workplace contact networks for ABMs. |
| OneHealth Tool | Costing platform | C++ / GUI | UN IAWG-Costing / WHO / Avenir Health | [avenirhealth.org](https://avenirhealth.org/software-onehealth.html) | Used in 50–80+ LMICs for national strategic health plans | Integrated strategic health planning, costing, and impact analysis tool. |
| Optima Nutrition | Allocative efficiency | Python | Optima Consortium / World Bank | [optimamodel.com](https://optimamodel.com/nutrition/) | Applied in Bangladesh, Tanzania, Pakistan; ongoing in Benin, DRC, Nigeria, India, Sierra Leone, Tajikistan | Allocative-efficiency tool for childhood-stunting and nutrition-intervention targeting. |

---

*Compiled 2026-05-06. Tools listed have peer-reviewed publication and/or maintained public repositories with multi-group adoption. Star counts and citation totals are point-in-time snapshots; treat the Usage column as an approximate signal of scale rather than a precise figure.*
