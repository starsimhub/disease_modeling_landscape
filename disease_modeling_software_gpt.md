Here’s a broad (though still not exhaustive) list of infectious disease / epidemiological modeling libraries, frameworks, and platforms that have either published literature, documented use by multiple groups, or sustained community adoption. I’ve focused on tools specifically designed for epidemiology or infectious disease transmission modeling, not generic scientific computing libraries.

## General infectious disease modeling frameworks

| Name                                                                                                  | Description                                                                                                                                 | Link |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| [EpiModel](https://www.epimodel.org/?utm_source=chatgpt.com)                                          | R framework for compartmental, network, and agent-based infectious disease models, especially HIV/STI network modeling. ([epimodel.org][1]) |      |
| [EMOD](https://github.com/EMOD-Hub/emodpy?utm_source=chatgpt.com)                                     | IDM’s large-scale individual-based modeling platform for malaria, HIV, TB, polio, measles, etc. ([Wikipedia][2])                            |      |
| [Covasim](https://covasim.org?utm_source=chatgpt.com)                                                 | Agent-based COVID-19 simulator with interventions, contact networks, and calibration tools. ([PMC][3])                                      |      |
| [Starsim](https://starsim.org?utm_source=chatgpt.com)                                                 | Modular agent-based infectious disease framework supporting dynamic networks and multi-disease interactions.                                |      |
| [GLEAMviz](https://www.gleamviz.org/?utm_source=chatgpt.com)                                          | Global epidemic and mobility metapopulation simulator using airline mobility and spatial coupling. ([gleamviz.org][4])                      |      |
| [FRED](https://fred.publichealth.pitt.edu/?utm_source=chatgpt.com)                                    | Framework for Reconstructing Epidemic Dynamics; synthetic-population ABM platform. ([phdl.pitt.edu][5])                                     |      |
| [STEM (Spatiotemporal Epidemiological Modeler)](https://www.eclipse.org/stem/?utm_source=chatgpt.com) | Eclipse-based spatial infectious disease modeling environment. ([Global Biodefense][6])                                                     |      |
| [Epiabm](https://github.com/SABS-R3-Epidemiology/epiabm?utm_source=chatgpt.com)                       | Modular Python/C++ epidemiological ABM inspired by Imperial College’s CovidSim. ([Journal of Open Research Software][7])                    |      |
| [OpenABM-Covid19](https://github.com/BDI-pathogens/OpenABM-Covid19?utm_source=chatgpt.com)            | COVID-specific agent-based simulator developed at Oxford/BDI.                                                                               |      |
| [FluTE](https://github.com/dlchao/FluTE?utm_source=chatgpt.com)                                       | Influenza-focused stochastic individual-based epidemic simulator. ([ResearchGate][8])                                                       |      |
| [Kendrick](https://github.com/KendrickOrg/kendrick?utm_source=chatgpt.com)                            | Domain-specific epidemiological modeling language/platform. ([ResearchGate][8])                                                             |      |
| [SimInf](https://stewid.github.io/SimInf/?utm_source=chatgpt.com)                                     | R package for large-scale stochastic compartmental disease spread simulation. ([arXiv][9])                                                  |      |
| [EpiILM](https://cran.r-project.org/package=EpiILM?utm_source=chatgpt.com)                            | Bayesian individual-level infectious disease transmission inference models in R. ([arXiv][10])                                              |      |
| [epidemia](https://imperialcollegelondon.github.io/epidemia/?utm_source=chatgpt.com)                  | Bayesian semi-mechanistic infectious disease modeling package from Imperial College. ([arXiv][11])                                          |      |
| [PyRoss](https://github.com/rajeshrinet/pyross?utm_source=chatgpt.com)                                | Age-structured compartmental epidemic inference and forecasting framework.                                                                  |      |
| [SEIRS+](https://github.com/ryansmcgee/seirsplus?utm_source=chatgpt.com)                              | Python framework for network-based stochastic SEIR modeling.                                                                                |      |
| [Epigrass](https://github.com/fccoelho/epigrass?utm_source=chatgpt.com)                               | Spatial epidemic simulation framework in Python.                                                                                            |      |
| [GEMFsim](https://github.com/ayounap/GEMFsim?utm_source=chatgpt.com)                                  | Generalized epidemic mean-field stochastic simulation framework on networks.                                                                |      |
| [Epipy](https://github.com/thoughtworks/epirust?utm_source=chatgpt.com)                               | Various open epidemic simulation projects exist under this name; often lightweight compartmental modeling libraries.                        |      |
| [EpiRust](https://github.com/thoughtworks/epirust?utm_source=chatgpt.com)                             | Rust-based epidemic simulation framework for large-scale ABMs.                                                                              |      |
| [Como-DTC](https://github.com/como-dtc-collaboration/como-models?utm_source=chatgpt.com)              | Disease transmission modeling tools from the COMO consortium.                                                                               |      |

## Rt estimation / outbreak analytics tools

| Name                                                                               | Description                                                                   | Link |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---- |
| [EpiEstim](https://mrc-ide.github.io/EpiEstim/?utm_source=chatgpt.com)             | Widely used R package for estimating time-varying reproduction numbers (R_t). |      |
| [EpiNow2](https://epiforecasts.io/EpiNow2/?utm_source=chatgpt.com)                 | Bayesian real-time estimation and forecasting of cases and Rt.                |      |
| [projections](https://github.com/reconhub/projections?utm_source=chatgpt.com)      | Outbreak projection tools from the R Epidemics Consortium.                    |      |
| [incidence](https://github.com/reconhub/incidence?utm_source=chatgpt.com)          | Incidence curve handling and outbreak analysis utilities.                     |      |
| [outbreaker2](https://github.com/reconhub/outbreaker2?utm_source=chatgpt.com)      | Bayesian outbreak reconstruction from epidemiological/genetic data.           |      |
| [surveillance](https://surveillance.r-forge.r-project.org/?utm_source=chatgpt.com) | Aberration detection and infectious disease surveillance methods.             |      |
| [NobBS](https://github.com/smc77/NobBS?utm_source=chatgpt.com)                     | Bayesian nowcasting for delayed epidemic reporting.                           |      |
| [epitrix](https://github.com/reconhub/epitrix?utm_source=chatgpt.com)              | Epidemiological utility functions and helper methods.                         |      |

## Phylodynamic / genomic epidemiology tools

| Name                                                                              | Description                                                      | Link |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---- |
| [BEAST 2](https://www.beast2.org/?utm_source=chatgpt.com)                         | Bayesian evolutionary and phylodynamic inference framework.      |      |
| [TreeTime](https://github.com/neherlab/treetime?utm_source=chatgpt.com)           | Fast phylogenetic timing and ancestral reconstruction.           |      |
| [Nextstrain / Augur](https://nextstrain.org/?utm_source=chatgpt.com)              | Real-time pathogen evolution and transmission tracking platform. |      |
| [TransPhylo](https://github.com/xavierdidelot/TransPhylo?utm_source=chatgpt.com)  | Transmission tree inference from genomic data.                   |      |
| [phydynR](https://github.com/emvolz-phylodynamics/phydynR?utm_source=chatgpt.com) | Phylodynamic simulation and inference in R.                      |      |
| [Outbreaker](https://github.com/reconhub/outbreaker2?utm_source=chatgpt.com)      | Joint epidemiological + phylogenetic outbreak reconstruction.    |      |

## Vector-borne / malaria-specific frameworks

| Name                                                                                            | Description                                                        | Link |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---- |
| [OpenMalaria](https://github.com/SwissTPH/openmalaria?utm_source=chatgpt.com)                   | Detailed stochastic malaria transmission simulator from Swiss TPH. |      |
| [malariasimulation](https://mrc-ide.github.io/malariasimulation/?utm_source=chatgpt.com)        | Individual-based malaria simulation framework in R/C++.            |      |
| [MicroMoB](https://github.com/dd-harp/micromob?utm_source=chatgpt.com)                          | Modular mosquito-borne disease simulation framework.               |      |
| [MGDrivE](https://marshalllab.github.io/MGDrivE/?utm_source=chatgpt.com)                        | Mosquito gene drive and vector-borne disease simulation framework. |      |
| [VectorSim](https://github.com/InstituteforDiseaseModeling/vector-model?utm_source=chatgpt.com) | Vector-borne transmission modeling tools.                          |      |

## HIV / STI focused platforms

| Name                                                                                           | Description                                              | Link |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ---- |
| [SimpactCyan](https://simpactcyan.readthedocs.io/?utm_source=chatgpt.com)                      | Individual-based HIV epidemiology simulator.             |      |
| [STDSIM](https://www.jstor.org/stable/24048014?utm_source=chatgpt.com)                         | Historical STI/HIV microsimulation model.                |      |
| [CEPAC](https://www.massgeneral.org/medicine/mpec/research/cepac-model?utm_source=chatgpt.com) | HIV clinical and policy simulation model.                |      |
| [Goals / Spectrum](https://www.avenirhealth.org/software-spectrum.php?utm_source=chatgpt.com)  | HIV epidemic projection and intervention planning suite. |      |
| [HPVsim](https://hpvsim.org/?utm_source=chatgpt.com)                                           | Agent-based HPV transmission and intervention simulator. |      |
| [STIsim / STisim](https://github.com/starsimhub/stisim?utm_source=chatgpt.com)                 | STI-focused transmission simulation framework.           |      |

## Public health analysis / teaching tools

| Name                                                                              | Description                                                                    | Link |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---- |
| [OpenEpi](https://www.openepi.com/?utm_source=chatgpt.com)                        | Web-based epidemiology and public health statistics toolkit. ([Wikipedia][12]) |      |
| [Epi Info](https://www.cdc.gov/epiinfo/?utm_source=chatgpt.com)                   | CDC epidemiology/statistics package widely used in field epidemiology.         |      |
| [WinPEPI](https://www.brixtonhealth.com/pepi4windows.html?utm_source=chatgpt.com) | Epidemiological statistics package for Windows.                                |      |
| [Epicalc](https://cran.r-project.org/package=epicalc?utm_source=chatgpt.com)      | Epidemiological analysis helpers for R.                                        |      |
| [epiR](https://cran.r-project.org/package=epiR?utm_source=chatgpt.com)            | Epidemiological analysis and reporting toolkit for R.                          |      |
| [epitools](https://cran.r-project.org/package=epitools?utm_source=chatgpt.com)    | Basic epidemiological calculations and outbreak tools.                         |      |

## Spatial / mobility / metapopulation tools

| Name                                                                       | Description                                                   | Link |
| -------------------------------------------------------------------------- | ------------------------------------------------------------- | ---- |
| [GLEaM](https://www.gleamproject.org/?utm_source=chatgpt.com)              | Global epidemic mobility model using transportation networks. |      |
| [PatchSim](https://github.com/NSSAC/PatchSim?utm_source=chatgpt.com)       | Spatially explicit metapopulation epidemic simulation.        |      |
| [EpiGraph](https://github.com/EpiForeSITE/EpiGraph?utm_source=chatgpt.com) | Network and mobility-based epidemic analysis tools.           |      |
| [GeoEpi](https://github.com/geoepi/geoepi?utm_source=chatgpt.com)          | Geospatial epidemiological analysis framework.                |      |

## General simulation environments often used heavily in epidemiology

These are more general simulation platforms, but have major infectious disease modeling communities and publications:

| Name                                                                    | Description                                                                                 | Link |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ---- |
| [AnyLogic](https://www.anylogic.com/?utm_source=chatgpt.com)            | Commercial multimethod simulation platform heavily used for epidemic ABMs. ([AnyLogic][13]) |      |
| [NetLogo](https://ccl.northwestern.edu/netlogo/?utm_source=chatgpt.com) | Widely used ABM platform with many epidemiological teaching/research models.                |      |
| [GAMA Platform](https://gama-platform.org/?utm_source=chatgpt.com)      | Large-scale agent-based spatial simulation environment.                                     |      |
| [Mesa](https://mesa.readthedocs.io/?utm_source=chatgpt.com)             | Python agent-based modeling framework frequently used for epidemic ABMs.                    |      |

A few observations:

* The ecosystem is heavily split between:

  * **compartmental ODE tools** (EpiEstim, epidemia, PyRoss),
  * **network/agent-based simulators** (EpiModel, Covasim, FRED, EMOD),
  * **spatial/metapopulation systems** (GLEAMviz, STEM),
  * and **phylodynamic tools** (BEAST, Nextstrain).
* R dominates statistical outbreak analysis and inference.
* Python dominates newer ABMs and intervention simulators.
* Many historically influential disease models are *not* reusable libraries, but one-off codebases attached to specific papers.

This list is still incomplete — there are probably hundreds of published infectious disease modeling packages if you include niche pathogen-specific and academic tools.

[1]: https://www.epimodel.org/?utm_source=chatgpt.com "EpiModel"
[2]: https://en.wikipedia.org/wiki/Institute_for_Disease_Modeling?utm_source=chatgpt.com "Institute for Disease Modeling"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8341708/?utm_source=chatgpt.com "Covasim: An agent-based model of COVID-19 dynamics and ..."
[4]: https://www.gleamviz.org/?utm_source=chatgpt.com "GLEAMviz | The Global Epidemic and Mobility Model"
[5]: https://www.phdl.pitt.edu/research/software?utm_source=chatgpt.com "Software | Public Health Dynamics Laboratory"
[6]: https://globalbiodefense.com/2016/01/28/open-source-disease-modeling-a-tool-to-combat-the-next-pandemic/?utm_source=chatgpt.com "Open Source Disease Modeling: A Tool to Combat the ..."
[7]: https://openresearchsoftware.metajnl.com/articles/10.5334/jors.449?utm_source=chatgpt.com "Epidemiological Agent-Based Modelling Software (Epiabm)"
[8]: https://www.researchgate.net/figure/A-Selection-of-Software-Tools-for-Epidemiologic-Modeling_tbl1_257620902?utm_source=chatgpt.com "A Selection of Software Tools for Epidemiologic Modeling"
[9]: https://arxiv.org/abs/1605.01421?utm_source=chatgpt.com "SimInf: An R package for Data-driven Stochastic Disease Spread Simulations"
[10]: https://arxiv.org/abs/2003.04963?utm_source=chatgpt.com "Individual-Level Modelling of Infectious Disease Data: EpiILM"
[11]: https://arxiv.org/abs/2110.12461?utm_source=chatgpt.com "Epidemia: An R Package for Semi-Mechanistic Bayesian Modelling of Infectious Diseases using Point Processes"
[12]: https://en.wikipedia.org/wiki/OpenEpi?utm_source=chatgpt.com "OpenEpi"
[13]: https://www.anylogic.com/?utm_source=chatgpt.com "AnyLogic: Simulation Modeling Software Tools & Solutions"
