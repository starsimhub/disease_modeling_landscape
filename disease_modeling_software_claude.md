# Epidemiology / Disease Modeling Software Libraries

A list of software libraries specifically designed for infectious-disease and epidemiological modeling. Each entry has evidence of use by more than one group and/or has been published in the peer-reviewed literature.

## General-purpose disease simulation frameworks

- **Starsim** — Agent-based multi-disease modeling framework (Python). https://starsim.org
- **Covasim** — Agent-based COVID-19 model (Python), IDM. https://covasim.org
- **HPVsim** — Agent-based HPV/cervical-cancer model (Python). https://hpvsim.org
- **FPsim** — Agent-based family-planning / reproductive-health model (Python). https://fpsim.org
- **EMOD** — Epidemiological MODeling software, agent-based, multi-disease (C++/Python), IDM. https://github.com/InstituteforDiseaseModeling/EMOD
- **EpiModel** — Mathematical modeling of infectious disease dynamics (R), Statnet. https://epimodel.org
- **OpenMalaria** — Individual-based malaria simulation platform (C++), Swiss TPH. https://github.com/SwissTPH/openmalaria
- **GLEAM / GLEAMviz** — Global Epidemic and Mobility Model. http://www.gleamviz.org
- **FRED** — Framework for Reconstructing Epidemiological Dynamics, University of Pittsburgh. https://fred.publichealth.pitt.edu
- **FluTE** — Stochastic influenza epidemic simulator. https://github.com/dlchao/FluTE
- **CovidSim** — Imperial College agent-based pandemic model. https://github.com/mrc-ide/covid-sim
- **OpenABM-Covid19** — Oxford agent-based COVID-19 model. https://github.com/BDI-pathogens/OpenABM-Covid19
- **EpiABM** — Imperial / Cambridge re-implementation of CovidSim. https://github.com/SABS-R3-Epidemiology/epiabm
- **JUNE** — Individual-based epidemic model (Durham/IHME). https://github.com/IDAS-Durham/JUNE
- **Pandemia** — Stochastic pandemic simulator. https://github.com/PandemiaUK/Pandemia
- **EpiSimS** — Large-scale epidemic simulation system, Los Alamos.
- **ACEMod** — Australian Census-based Epidemic Model. https://github.com/SystemsAndComplexity/ACEMod-COVID-19
- **Episimmer** — Epidemic simulator for institutional reopening. https://github.com/healthbadge/episimmer
- **MicroSim** — Microsimulation framework for COVID-19. https://github.com/mscbio2025-2021/SEIRSPlus

## Compartmental modeling and inference

- **pomp** — Partially Observed Markov Processes (R). https://kingaa.github.io/pomp/
- **odin** — Domain-specific language for ODE models (R), MRC IDE. https://mrc-ide.github.io/odin/
- **dust** — Stochastic simulation engine paired with odin. https://mrc-ide.github.io/dust/
- **mcstate** — Particle filter / pMCMC for odin/dust models. https://mrc-ide.github.io/mcstate/
- **epidemia** — Bayesian semi-mechanistic epidemic models (R, Stan). https://imperialcollegelondon.github.io/epidemia/
- **LEMMA** — Local Epidemic Modeling for Management & Action (UCSF). https://github.com/LocalEpi/LEMMA
- **PyRoss** — Inference, prediction, control of epidemics (Python). https://github.com/rajeshrinet/pyross
- **epipack** — Numerical and symbolic compartmental modeling (Python). https://github.com/benmaier/epipack
- **MMODS** — Multiple Models for Outbreak Decision Support.
- **rstanarm / brms epidemic models** — Bayesian epidemic regression frameworks via Stan.

## Reproduction-number estimation, nowcasting & forecasting

- **EpiEstim** — Rt estimation from incidence (R). https://github.com/mrc-ide/EpiEstim
- **EpiNow2** — Real-time Rt estimation and short-term forecasts (R), epiforecasts. https://epiforecasts.io/EpiNow2/
- **epinowcast** — Hierarchical nowcasting of right-truncated data (R/Stan). https://package.epinowcast.org
- **R0** — Reproduction-number estimation (R). https://cran.r-project.org/package=R0
- **earlyR** — Rt during early outbreak phase (R, RECON). https://www.repidemicsconsortium.org/earlyR/
- **projections** — Short-term incidence projections (R, RECON). https://www.repidemicsconsortium.org/projections/
- **EpiSoon** — Short-term Rt forecasting (R). https://epiforecasts.io/EpiSoon/
- **scoringutils** — Probabilistic forecast scoring (R). https://epiforecasts.io/scoringutils/
- **hubUtils / hubverse** — Forecast hub infrastructure (CDC FluSight, COVID-19 Forecast Hub). https://hubverse.io
- **EpiLPS** — Laplacian-P-splines for Rt estimation. https://cran.r-project.org/package=EpiLPS

## Outbreak analytics (RECON suite and related)

- **incidence / incidence2** — Incidence curves from line lists (R). https://www.reconverse.org/incidence2/
- **distcrete** — Discretised delay distributions (R). https://github.com/reconhub/distcrete
- **epitrix** — Small helpers for epidemic analysis (R). https://github.com/reconhub/epitrix
- **linelist** — Line-list data cleaning (R). https://www.reconverse.org/linelist/
- **outbreaks** — Curated outbreak datasets (R). https://github.com/reconverse/outbreaks
- **epicontacts** — Contact-tracing data structures (R). https://www.repidemicsconsortium.org/epicontacts/
- **outbreaker2** — Reconstruction of who-infected-whom (R). https://github.com/reconhub/outbreaker2
- **o2geosocial** — Outbreaker2 with spatial/age data. https://github.com/alxsrobert/o2geosocial
- **EpiContactTrace** — Network analysis of livestock movements (R). https://cran.r-project.org/package=EpiContactTrace

## Phylodynamics & molecular epidemiology

- **BEAST / BEAST2** — Bayesian Evolutionary Analysis Sampling Trees. https://www.beast2.org
- **Nextstrain (Augur / Auspice)** — Real-time pathogen evolution tracking. https://nextstrain.org
- **TreeTime** — Maximum-likelihood phylodynamic inference. https://github.com/neherlab/treetime
- **phylodyn** — Bayesian nonparametric phylodynamics (R). https://github.com/mdkarcher/phylodyn
- **PhyDyn** — Phylodynamic structured-population models (BEAST2). https://github.com/mrc-ide/PhyDyn
- **MASCOT** — Marginal approximation of structured coalescent (BEAST2). https://github.com/nicfel/Mascot
- **skygrowth** — Phylodynamic effective-population-size inference. https://github.com/mrc-ide/skygrowth
- **adegenet** — Multivariate genetic analysis (R). https://github.com/thibautjombart/adegenet
- **TransPhylo** — Inference of transmission trees from phylogenies (R). https://github.com/xavierdidelot/TransPhylo

## Networks and contact structure

- **EoN (Epidemics on Networks)** — Simulation of SIS/SIR on networks (Python). https://github.com/springer-math/Mathematics-of-Epidemics-on-Networks
- **NDlib** — Network Diffusion library (Python). https://ndlib.readthedocs.io
- **statnet / ergm** — Exponential random graph models for contact networks (R). https://statnet.org
- **EpiModel networks module** — Stochastic network epidemic models (R).
- **socialmixr** — Contact-matrix tools using POLYMOD-style data (R). https://github.com/epiforecasts/socialmixr

## Surveillance and aberration detection

- **surveillance** — Temporal/spatio-temporal monitoring of count data (R). https://surveillance.r-forge.r-project.org
- **rotaR / FarringtonFlexible** — Outbreak detection algorithms (R).
- **EpiTools / Epi Info** — CDC outbreak investigation tools. https://www.cdc.gov/epiinfo/

## Disease-specific modeling tools

### HIV
- **Spectrum / EPP** — UNAIDS HIV estimates and projections package. https://avenirhealth.org/software-spectrum.php
- **Goals / Goals-ART** — Avenir Health HIV resource-allocation model.
- **PopART-IBM** — Individual-based model for HIV, Imperial. https://github.com/p-robot/POPART-IBM
- **HIV Synthesis** — Individual-based HIV model, UCL.
- **Optima HIV / TB / Nutrition** — Allocative-efficiency models. http://optimamodel.com
- **EMOD-HIV** — IDM HIV agent-based model.
- **HIVsim** — Starsim-based HIV model.

### TB
- **TIME Impact** — Avenir Health TB model. https://avenirhealth.org/software-time.php
- **EMOD-TB** — IDM TB model.
- **TBVx** — KNCV TB vaccine impact model.

### Malaria
- **OpenMalaria** — (see above).
- **malariasimulation** — Imperial individual-based malaria model (R). https://github.com/mrc-ide/malariasimulation
- **malariaEquilibrium** — Equilibrium solutions for Imperial malaria model (R). https://github.com/mrc-ide/malariaEquilibrium
- **AnophelesModel** — Vector bionomics for malaria, Swiss TPH. https://github.com/SwissTPH/AnophelesModel
- **EMOD-Malaria** — IDM malaria model.

### Polio
- **IDM Polio model** — Agent-based polio transmission model.

### Influenza / RSV / measles
- **FluSurv-Network models / CDC FluSight ensemble**.
- **rsvnet / rsv_immunity** — RSV transmission models (various).

### COVID-19 (additional)
- **CovaSim, OpenABM-Covid19, CovidSim, JUNE, EpiABM, ACEMod, LEMMA** — see above.
- **MOCOS** — Microsimulation of COVID-19 (Wroclaw/Linköping). http://mocos.pl
- **CoMo Consortium model** — Oxford/CoMo COVID-19 model.

### STIs
- **STIsim** — Starsim-based STI model.
- **HPVsim** — (see above).

### Vector-borne / arboviruses
- **denguesim / Skeeter Buster** — Aedes aegypti dynamic models.
- **VectorBase** — Bioinformatics resource (data + tools). https://vectorbase.org

## Synthetic populations / patient generators

- **Synthea** — Synthetic patient generator for health-care simulation. https://synthetichealth.github.io/synthea/
- **SynthPops** — Synthetic populations for agent-based epidemic models (Python), IDM. https://github.com/InstituteforDiseaseModeling/synthpops

## Health-economics / decision-analytic frameworks (disease-focused)

- **heemod** — Health-economic Markov models (R). https://cran.r-project.org/package=heemod
- **hesim** — Health-economic simulation modeling (R). https://hesim-dev.github.io/hesim/
- **TreeAge Pro** — Decision-tree / Markov modeling for disease cost-effectiveness. https://www.treeage.com
- **AMANHI / LiST (Lives Saved Tool)** — Child/maternal mortality intervention impact. https://www.livessavedtool.org

## Other notable tools

- **NetLogo epidemic models** — Educational ABMs (NetLogo). https://ccl.northwestern.edu/netlogo/
- **Berkeley Madonna** — System-dynamics modeling, used widely for SIR models. https://berkeley-madonna.myshopify.com
- **Vensim** — System-dynamics platform used for disease models. https://vensim.com
- **AnyLogic** — Multi-method simulation, includes epidemic templates. https://www.anylogic.com
- **InsightMaker** — Browser-based system dynamics / ABM. https://insightmaker.com
- **Pathogen.jl** — Bayesian individual-level disease modeling (Julia). https://github.com/jangevaare/Pathogen.jl
- **Epidemics.jl / SimpleInfectiousDiseaseModels.jl** — Julia epidemic modeling.
- **Mesa-based epi models** — General ABM framework with widespread epi use (Python). https://github.com/projectmesa/mesa

---

*Compiled 2026-05-06. Listing favors libraries with multi-group adoption or peer-reviewed publication; coverage is broad but not exhaustive.*
