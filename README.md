# **Disease modeling software landscape**

## Introduction

The aim of this project is to summarize the current landscape of software tools that are:

1. Focused on dynamical disease modeling (excluding data or statistical tools, or general purpose tools that are used for, but not specific to, disease modeling)
2. Publicly available — open source, or otherwise obtainable and usable by external groups — and in use by the community (excluding one-off models supporting publications, or that have no evidence of reuse)

## Methodology

Both Claude Opus 4.7 and ChatGPT 5.5 were given the following prompt:

> "List all epidemiology / disease modeling software libraries. List as many as you can find, that have evidence of >1 group using or have been published. These should be specific for disease modeling (e.g. EpiEstim), not general-purpose tools that could be used for disease modeling (e.g. NumPy). Include the name, brief description, and link."

Claude was then asked to reconcile the two lists and add additional information (e.g. model type and disease). Full results are listed [here](disease_modeling_software_database.md): a total of 171 software tools were found, although most had limited evidence of use.

### Selection criteria

From that database, the tools below were selected as those in widest current use as general-purpose disease modeling platforms. To be listed, a tool must meet **all three** of:

1. **Scope**: it is a reusable framework or platform for dynamical disease modeling, not a single-purpose model, a statistical/data package, or a general-purpose tool applied to epidemiology.
2. **Availability**: it is publicly obtainable and documented, whether open source or (as for Spectrum and GLEAM) available to external users under another licence.
3. **Evidence of use beyond the originating group**: either a peer-reviewed publication describing the tool, **or** documented application by two or more independent institutions.

Selection is still a judgment call, and other tools in the database could reasonably be included. Corrections and additions are welcome.

### Author and conflicts of interest

This review was compiled by Cliff Kerr, who works at IDM, leads development of Starsim, and is a co-author on the Optima and Atomica publications cited below. Four of the listed tools (Atomica, EMOD, Optima, Starsim) originate wholly or partly from institutions the author is or has been affiliated with. To avoid implying a ranking, tools are listed **alphabetically**; the ordering carries no information about quality or importance.

### How to read the metrics

**Evidence of use is hard to quantify.** "Downloads" vastly *overestimate* users, since the vast majority of downloads are due to automated runs (e.g. GitHub Actions or cluster deployment); these typically comprise perhaps 90-99.9% of downloads. GitHub stars *underestimate* users, since the majority of users (50-99%) download rather than star/fork. Neither metric is comparable across languages or distribution channels: CRAN, PyPI, and installer-based or licensed tools are counted in fundamentally different ways, and tools distributed as GUIs or via national programmes (Spectrum, GLEAM, Optima) have no download counter at all. Citation counts favour older tools. No single number here should be read as a ranking.

Where a tool anchors a family of packages, the related packages are listed separately rather than summed into the parent's total, since the same convention cannot be applied uniformly across all entries.

**Status** is assigned on public evidence, using the same rule for every tool:

* **Active** — substantive development within the past 12 months, or (for closed-source tools) a documented ongoing release cycle.
* **Low activity** — no substantive public development for 12+ months, but not formally retired.
* **Unmaintained** — formally retired, archived, or stated by its maintainers to be no longer supported.

**Snapshot dates**: GitHub stars and repository activity as of 2026-08-07; download counts as of 2026-05-06. All of these drift.

## Findings

| Tool | Lead institution | Language | Status | Summary |
|---|---|---|---|---|
| [Atomica](#atomica) | Burnet Institute | Python | Active | General-purpose compartmental engine with cascade analysis |
| [EMOD](#emod) | IDM | C++/Python | **Unmaintained** | C++ individual-based multi-disease platform |
| [epidemics](#epidemics) | LSHTM | R | Active | Library of composable compartmental outbreak models |
| [EpiHiper](#epihiper) | University of Virginia | C++ | Active | HPC parallel agent-based simulator for 300M+ agents |
| [EpiModel](#epimodel) | Emory University | R | Active | Stochastic epidemics over dynamic ERGM networks |
| [Epydemix](#epydemix) | Northeastern / ISI | Python | Active | Compartmental modeling with ABC calibration |
| [FRED](#fred) | University of Pittsburgh | C++ | Low activity | Agent-based framework using US census synthetic populations |
| [GLEAM](#gleam) | Northeastern / ISI | C++ | Active | Global metapopulation simulator using air-travel mobility data |
| [MEmilio](#memilio) | DLR / RKI | C++/Python | Active | Modular library combining ODE, ABM, and hybrid models |
| [odin](#odin) | Imperial College London | R | Active | DSL compiling ODE and stochastic models to fast C |
| [Optima](#optima) | Burnet Institute | Python | Active | Compartmental models with allocative-efficiency optimisation |
| [Spectrum](#spectrum) | Avenir Health | Pascal/C++ | Active | Policy suite for official UNAIDS/WHO HIV, TB, and child-survival estimates |
| [Starsim](#starsim) | IDM | Python | Active | Agent-based framework for multi-disease network transmission |
| [Vivarium](#vivarium) | IHME | Python | Active | Microsimulation linked to IHME Global Burden of Disease data |

### Atomica

* **Author**: Burnet Institute (Romesh Abeysuriya et al.)
* **Model type**: General-purpose compartmental modelling engine (with optimisation and cascade-analysis features)
* **Diseases**: General-purpose (applied to HIV care cascades, TB, hepatitis C, malaria, NCDs)
* **Language**: Python
* **Years**: 2018-2026
* **Status**: Active (last commit 2026-08)
* **Links**: [atomica.tools](https://atomica.tools), [code](https://github.com/atomicateam/atomica), [docs](https://atomica.tools/docs/master/index.html)
* **Publication**: Kedziora DJ, Stuart RM, Pearson J, Latypov A, Dierst-Davies R, Duda M, Avaliani N, Wilson DP, Kerr CC. "The Cascade Analysis Tool: software to analyze and optimize care cascades" Gates Open Research 3:1488, 2019
* **Package**: [PyPI (251,750 downloads)](https://pepy.tech/projects/atomica)
* **Evidence of use**: ~15 GitHub stars; powers the Cascade Analysis Tool used by Global Fund and country teams; used in Burnet's Optima TB and follow-on Optima models
* **Description**: A flexible Python framework that lets modellers specify arbitrary compartmental models from a spreadsheet definition, run scenarios and calibrations, and apply built-in budget-optimisation routines; intended as a generalisation and modern successor to the original Optima codebase

### EMOD

* **Author**: IDM
* **Model type**: Individual-based / agent-based stochastic model
* **Diseases**: Malaria and HIV (final public release); historically also TB, polio, measles, typhoid, dengue, COVID-19
* **Language**: C++ core with Python interface
* **Years**: 2010-2026
* **Status**: **Unmaintained** — no longer supported by IDM. The code and documentation remain publicly available, and published results based on EMOD remain valid, but new users should not expect support or further development.
* **Links**: [idmod.org/tools](https://www.idmod.org/tools/), [code](https://github.com/EMOD-Hub/EMOD), [docs](https://docs.idmod.org/projects/emod-generic/en/latest/)
* **Publication**: Bershteyn A, Gerardin J, Bridenbecker D, et al. "[Implementation and applications of EMOD, an individual-based multi-disease modeling platform](https://doi.org/10.1093/femspd/fty059)." Pathogens and Disease, 76(5), fty059, 2018
* **Package**: [PyPI (14,110 downloads)](https://pepy.tech/projects/emodpy) (for emodpy)
* **Evidence of use**: ~107 GitHub stars; used by Nigeria's National Malaria Elimination Programme for the 2021–2025 strategic plan; deployed across multiple sub-Saharan African countries for malaria policy
* **Description**: C++ individual-based multi-disease modeling platform supporting detailed vector dynamics, with shared core code across pathogens

### epidemics

* **Author**: LSHTM, Epiverse-TRACE (Pratik R. Gupte, Rosalind M. Eggo, Adam Kucharski, et al.)
* **Model type**: Compartmental (deterministic and stochastic, discrete-time)
* **Diseases**: Generic respiratory pathogens (influenza-like, COVID-19), Ebola virus disease, diphtheria
* **Language**: R (with C++ backend)
* **Years**: 2023-2026
* **Status**: Active (last commit 2026-08)
* **Links**: [epiverse-trace.github.io/epidemics](https://epiverse-trace.github.io/epidemics/), [code](https://github.com/epiverse-trace/epidemics), [docs](https://epiverse-trace.github.io/epidemics/)
* **Publication**: N/A (no primary peer-reviewed paper identified; included on the basis of multi-institution use within Epiverse-TRACE)
* **Package**: N/A — not on CRAN (distributed via r-universe only)
* **Evidence of use**: ~19 GitHub stars; part of the Wellcome-funded Epiverse-TRACE outbreak analytics ecosystem at LSHTM
* **Related packages**: the wider Epiverse-TRACE ecosystem (epiparameter, cfr, superspreading, and others) has 200+ stars and 4k+ downloads in aggregate
* **Description**: R library of published compartmental epidemic models with composable classes for demographic structure, non-pharmaceutical interventions, and vaccination regimes for outbreak scenario modeling

### EpiHiper

* **Author**: NSSAC / Biocomplexity Institute, University of Virginia (Madhav Marathe et al.)
* **Model type**: Parallel agent-based / network-based stochastic socio-epidemic simulator
* **Diseases**: COVID-19, influenza-like illnesses; supports custom user-defined disease models
* **Language**: C++ (with JSON-schema configuration)
* **Years**: 2020-2026
* **Status**: Active (last commit 2026-07)
* **Links**: [nssac.github.io/modeling_capabilities](https://nssac.github.io/modeling_capabilities/), [code](https://github.com/NSSAC/EpiHiper), [docs](https://github.com/NSSAC/EpiHiper)
* **Publication**: Bhattacharya P. et al., "EpiHiper—A high performance computational modeling framework to support epidemic science," PNAS Nexus, 4(1), pgae557, 2025
* **Package**: N/A — no public package
* **Evidence of use**: Used for US CDC COVID-19 Scenario Modeling Hub at national scale (~300M agents); 2021 ACM Gordon Bell Special Prize finalist; ~6 GitHub stars
* **Description**: HPC parallel agent-based simulator capable of running US-scale (300M+ agents) epidemic simulations on dynamic contact networks, with user-programmable interventions and custom disease models

### EpiModel

* **Author**: Emory University (Samuel M. Jenness, Steven M. Goodreau, Martina Morris, Adrien Le Guillou)
* **Model type**: Compartmental (DCM), individual-contact (ICM), and stochastic network (statnet/ERGM-based) models
* **Diseases**: Generic SI/SIR/SIS framework; extensions for HIV, STIs (EpiModelHIV), and COVID-19 (EpiModelCOVID)
* **Language**: R
* **Years**: 2014-2026
* **Status**: Active (last commit 2026-08)
* **Links**: [epimodel.org](https://www.epimodel.org/), [code](https://github.com/EpiModel/EpiModel), [docs](https://epimodel.github.io/EpiModel/)
* **Publication**: Jenness SM, Goodreau SM, Morris M. "[EpiModel: An R Package for Mathematical Modeling of Infectious Disease over Networks](https://doi.org/10.18637/jss.v084.i08)." Journal of Statistical Software, 84(8), 1–47, 2018
* **Package**: [CRAN (219,212 downloads)](https://cran.r-project.org/package=EpiModel)
* **Evidence of use**: ~277 GitHub stars; cited in 125+ published studies across HIV/STI, COVID-19, and veterinary epidemiology
* **Related packages**: EpiModelHIV, EpiModelCOVID, and the underlying statnet suite are distributed and counted separately
* **Description**: R package providing a general stochastic framework for simulating epidemics over dynamic contact networks, leveraging temporal ERGMs from the statnet suite

### Epydemix

* **Author**: Northeastern, ISI Foundation, Epistorm (Nicolò Gozzi, Matteo Chinazzi, Alessandro Vespignani et al.)
* **Model type**: Stochastic compartmental with Approximate Bayesian Computation (ABC) calibration
* **Diseases**: Generic respiratory/infectious diseases (e.g., COVID-19, influenza); user-defined compartmental structures
* **Language**: Python
* **Years**: 2024-2026
* **Status**: Active (last commit 2026-07)
* **Links**: [epydemix.org](https://www.epydemix.org/), [code](https://github.com/epistorm/epydemix), [docs](https://www.epydemix.org/)
* **Publication**: Gozzi N. et al., "Epydemix: An open-source Python package for epidemic modeling with integrated approximate Bayesian calibration," PLOS Computational Biology, 2025
* **Package**: [PyPI (16,570 downloads)](https://pepy.tech/projects/epydemix)
* **Evidence of use**: ~69 GitHub stars; published in PLOS Comp Bio (2025)
* **Description**: Open-source Python package for building stochastic compartmental epidemic models with built-in age-stratified contact matrices, demographics for 400+ locations, intervention modeling, and integrated ABC calibration

### FRED

* **Author**: University of Pittsburgh Public Health Dynamics Laboratory (Donald S. Burke, John Grefenstette et al.)
* **Model type**: Agent-based model with census-based synthetic populations
* **Diseases**: Influenza, measles, COVID-19, and other infectious / health conditions; also extended to chronic conditions
* **Language**: C++
* **Years**: 2013-2024
* **Status**: Low activity — last public commit 2024-05; the project website and web simulators remain online, and no retirement has been announced
* **Links**: [fred.publichealth.pitt.edu](https://fred.publichealth.pitt.edu/), [code](https://github.com/PublicHealthDynamicsLab/FRED), [docs](https://github.com/PublicHealthDynamicsLab/FRED/wiki)
* **Publication**: Grefenstette JJ et al., "FRED (A Framework for Reconstructing Epidemic Dynamics): an open-source software system for modeling infectious diseases and control strategies using census-based populations," BMC Public Health, 13:940, 2013
* **Package**: N/A
* **Evidence of use**: ~83 GitHub stars; foundational paper cited 200+ times; web simulators deployed for every US state and county; FRED US Measles Simulator widely covered in media
* **Description**: Open-source agent-based modeling framework using synthetic populations that represent every individual in a region with realistic household, school, and workplace contact networks

### GLEAM

* **Author**: Northeastern University, ISI Foundation, Indiana University (Alessandro Vespignani, Vittoria Colizza, Matteo Chinazzi et al.)
* **Model type**: Stochastic metapopulation model on a global mobility network (air travel + commuting)
* **Diseases**: H1N1 influenza, seasonal influenza, Ebola, MERS, Zika, COVID-19/SARS-CoV-2
* **Language**: C++ simulation engine with Java/web-based GLEAMviz client
* **Years**: 2009-2026
* **Status**: Active — closed source, so repository activity cannot be checked; status inferred from continuing publications and forecasting use
* **Links**: [gleamproject.org](https://www.gleamproject.org/), code (N/A, closed-source binary client), [docs](https://www.gleamviz.org/)
* **Publication**: Balcan D. et al., "Modeling the spatial spread of infectious diseases: The GLobal Epidemic and Mobility computational model," Journal of Computational Science, 1(3):132–145, 2010; Van den Broeck W. et al., "The GLEaMviz computational tool…," BMC Infect Dis, 11:37, 2011
* **Package**: N/A
* **Evidence of use**: Used for real-time forecasting of 2009 H1N1, 2014 Ebola, 2016 Zika, and COVID-19 (Chinazzi et al. Science 2020 with 2000+ citations); widely used by WHO, CDC
* **Description**: Stochastic, spatially structured metapopulation epidemic simulator integrating worldwide census and mobility data (3300+ subpopulations) to forecast global pandemic spread

### MEmilio

* **Author**: SciCompMod consortium — German Aerospace Center (DLR) and Robert Koch Institute (RKI) (Martin J. Kühn et al.)
* **Model type**: Modular — ODE/IDE compartmental, SDE, agent-based, graph/metapopulation, and hybrid models
* **Diseases**: COVID-19 (primary), influenza, RSV; extensible to other respiratory infections
* **Language**: C++ core with Python interface
* **Years**: 2020-2026
* **Status**: Active (last commit 2026-08)
* **Links**: [github.com/SciCompMod/memilio](https://github.com/SciCompMod/memilio), [docs](https://memilio.readthedocs.io/en/latest/)
* **Publication**: Kühn MJ et al., "Assessment of effective mitigation and prediction of the spread of SARS-CoV-2 in Germany using demographic information and spatial resolution," Mathematical Biosciences, 2021
* **Package**: [PyPI (1,830 downloads)](https://pepy.tech/projects/memilio-simulation)
* **Evidence of use**: ~71 GitHub stars; used for official German COVID-19 forecasts (RKI); integrated into DLR's panDEmis web app; SPoCK ICU bed occupancy forecasts
* **Description**: Modular epidemic simulation library combining equation-based, agent-based, and hybrid graph-ODE metapopulation models with a C++ core and Python interface

### odin

* **Author**: Rich FitzJohn et al., MRC Centre for Global Infectious Disease Analysis, Imperial College London
* **Model type**: DSL for compartmental ODE / discrete-time stochastic models (transpiles to C)
* **Diseases**: General-purpose (used for malaria, COVID-19, influenza, Ebola)
* **Language**: R (DSL compiles to C/JavaScript)
* **Years**: 2016-2026
* **Status**: Active (odin last commit 2026-01; successor odin2 in active development)
* **Links**: [mrc-ide.github.io/odin](https://mrc-ide.github.io/odin/), [code](https://github.com/mrc-ide/odin), [docs](https://mrc-ide.github.io/odin/)
* **Publication**: FitzJohn et al. "[Reproducible parallel inference and simulation of stochastic state space models using odin, dust, and mcstate](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8552050/)" Wellcome Open Research, 2021
* **Package**: [CRAN (81,065 downloads)](https://cran.r-project.org/package=odin)
* **Evidence of use**: ~106 GitHub stars; underpins Imperial College's malaria transmission model and squire/sircovid COVID-19 models used by WHO and UK SAGE
* **Related packages**: odin2, dust, mcstate, squire, and sircovid are distributed and counted separately
* **Description**: An R-based domain-specific language for concisely specifying and efficiently solving systems of ODEs and discrete-time stochastic models, widely used at MRC IDE for infectious disease modelling

### Optima

* **Author**: Optima Consortium for Decision Science (Burnet Institute lead; plus UNSW and World Bank)
* **Model type**: Compartmental dynamic transmission model with allocative-efficiency optimisation
* **Diseases**: HIV (Optima HIV); tuberculosis (Optima TB); child nutrition/stunting (Optima Nutrition); also malaria and COVID-19 variants
* **Language**: Python
* **Years**: 2014-2026
* **Status**: Active (last commit 2026-03; low commit volume)
* **Links**: [optimamodel.com](https://optimamodel.com), [code](https://github.com/optimamodel), [docs](https://optimamodel.com/hiv/documents.html)
* **Publication**: Kelly SL, Martin-Hughes R, Stuart RM, Kerr CC, Wilson DP, et al. "The global Optima HIV allocative-efficiency model: targeting resources in efforts to end AIDS" Lancet HIV 5(4): e190–e198, 2018
* **Package**: N/A — not on PyPI (distributed via GitHub)
* **Evidence of use**: Applied with national governments in 40+ countries (23+ documented for HIV) for World Bank-supported allocative-efficiency studies; informed national HIV strategic plans across Africa, Asia, Eastern Europe and Latin America
* **Description**: A suite of mathematical optimisation tools that combine epidemic transmission models with mathematical optimisation to recommend how to allocate limited budgets across prevention, treatment and care programmes to maximise impact

### Spectrum

* **Author**: Avenir Health (with UNAIDS Reference Group on Estimates, Modelling and Projections; collaborators including Johns Hopkins for LiST)
* **Model type**: Compartmental / cohort-component projection suite with GUI
* **Diseases**: HIV/AIDS (AIM, Goals, CSAVR), tuberculosis (TIME), child survival (LiST), maternal/child health, family planning (FamPlan), demography (DemProj)
* **Language**: Pascal/Delphi (desktop) and C++; with Spectrum Web
* **Years**: 1997-2026
* **Status**: Active — proprietary, with an annual release cycle tied to the UNAIDS estimates round
* **Links**: [avenirhealth.org/software-spectrum.php](https://avenirhealth.org/software-spectrum.php), code (N/A, proprietary), [docs](https://avenirhealth.org/software-spectrummodels.php)
* **Publication**: Stover J. et al. "Updates to the Spectrum/Estimations and Projections Package model for estimating trends and current values for key HIV indicators" AIDS 31 (Suppl 1): S5–S11, 2017
* **Package**: N/A
* **Evidence of use**: Official tool for UNAIDS HIV estimates in 161+ countries; used annually by national HIV/AIDS programmes; LiST adopted globally for child-survival policy
* **Description**: A long-running suite of policy-modelling tools used by ministries of health and UN agencies (UNAIDS, WHO) to produce official HIV, TB, family-planning, demographic, and child-survival estimates and projections

### Starsim

* **Author**: IDM, with Burnet Institute, Johns Hopkins, APHRC, Makerere, and other contributors
* **Model type**: Agent-based / network framework, plus compartmental and metapopulation modeling
* **Diseases**: Multi-disease (HIV, STIs, measles, TB, COVID-19, HPV, malaria, NCDs, pregnancy)
* **Language**: Python
* **Years**: 2023-2026
* **Status**: Active (last commit 2026-08)
* **Links**: [starsim.org](https://starsim.org/), [code](https://github.com/starsimhub/starsim), [docs](https://docs.starsim.org/)
* **Publication**: Kerr CC et al. "Starsim: A fast, flexible framework for agent-based modeling of health and disease" (in preparation, 2026). As the framework paper is not yet published, Starsim is included on the basis of multi-institution use rather than publication.
* **Package**: [PyPI (63,640 downloads)](https://pepy.tech/projects/starsim)
* **Evidence of use**: ~42 GitHub stars; contributions and applications from Burnet Institute, Johns Hopkins, APHRC, and Makerere in addition to IDM
* **Related packages**: STIsim ([8k](https://pepy.tech/projects/stisim)), HPVsim ([39k](https://pepy.tech/projects/hpvsim)), and FPsim ([18k](https://pepy.tech/projects/fpsim)) are disease-specific packages in the same family; Covasim ([302k](https://pepy.tech/projects/covasim)) is a predecessor codebase. These are counted separately and are not included in the Starsim total above.
* **Description**: Python agent-based modeling framework for simulating multi-disease transmission through dynamic networks, with built-in tools for interventions, scenario analysis, and calibration

### Vivarium

* **Author**: Institute for Health Metrics and Evaluation (IHME), University of Washington
* **Model type**: Discrete-event microsimulation framework
* **Diseases**: General-purpose (with vivarium_public_health for diseases/interventions; integrates with GBD outputs)
* **Language**: Python
* **Years**: 2017-2026
* **Status**: Active — the original `ihmeuw/vivarium` repository was archived in 2026 when development moved to the `vivarium-suite` monorepo, which is actively developed
* **Links**: [vivarium.readthedocs.io](https://vivarium.readthedocs.io/), [code](https://github.com/ihmeuw/vivarium-suite), [docs](https://vivarium.readthedocs.io/)
* **Publication**: N/A (IHME-authored framework; included on the basis of multi-group use within and beyond IHME)
* **Package**: [PyPI (553,580 downloads)](https://pepy.tech/projects/vivarium)
* **Evidence of use**: ~54 GitHub stars on the original repository; used at IHME for GBD-linked microsimulation studies (diarrhea, neonatal, ischemic heart disease, women's health interventions); BSD-3 licensed
* **Related packages**: vivarium_public_health and numerous `vivarium_gates_*` study repositories are distributed separately
* **Description**: Python framework for building modular, component-based microsimulations that link demographic and disease-burden data (notably IHME's Global Burden of Disease estimates) into individual-level simulations of health interventions
