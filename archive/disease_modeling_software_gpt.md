### General infectious disease / epidemic modeling frameworks

| Tool                   |                              Type | Brief description                                                                                                                     | Link                                                       |
| ---------------------- | --------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **EpiHiper**           |                     ABM / network | High-performance epidemic simulation over large dynamic contact networks, with programmable interventions. Published in *PNAS Nexus*. | [GitHub](https://github.com/NSSAC/EpiHiper)                |
| **FRED**               |                               ABM | Synthetic-population agent-based simulator for infectious diseases and control strategies.                                            | [FRED](https://fred.publichealth.pitt.edu/)                |
| **EMOD**               |                         ABM / IBM | IDM’s individual-based modeling platform for malaria, HIV, TB, polio, measles, etc.                                                   | [IDM tools](https://www.idmod.org/all-tools/)              |
| **Starsim**            |                    ABM / networks | Modular agent-based disease modeling framework with dynamic networks and multi-disease support.                                       | [Starsim](https://starsim.org/)                            |
| **Covasim**            |                               ABM | COVID-era agent-based simulator with interventions, calibration, and policy scenarios.                                                | [Covasim](https://covasim.org/)                            |
| **EpiModel**           | R / compartmental / network / IBM | R package for deterministic, stochastic individual-contact, and stochastic network epidemic models.                                   | [EpiModel](https://www.epimodel.org/)                      |
| **Atomica**            |                     Compartmental | Python framework for compartmental models, cascades, force-of-infection models, calibration, and scenarios.                           | [GitHub](https://github.com/atomicateam/atomica)           |
| **SimInf**             |     R / stochastic metapopulation | Efficient stochastic compartmental epidemic simulation in R.                                                                          | [SimInf](https://stewid.github.io/SimInf/)                 |
| **STEM**               |          Spatial / metapopulation | Eclipse Foundation open-source spatiotemporal disease modeling tool; documented global public-health use.                             | [STEM](https://www.eclipse.org/stem/)                      |
| **GLEAM / GLEAMviz**   |             Global metapopulation | Global epidemic modeling using mobility and transportation networks.                                                                  | [GLEAMviz](https://www.gleamviz.org/)                      |
| **flepiMoP**           |        Metapopulation / inference | Flexible infectious disease modeling and forecasting framework, used for COVID-19 and influenza.                                      | [GitHub](https://github.com/HopkinsIDD/flepiMoP)           |
| **Epiabm**             |                               ABM | Open-source epidemiological ABM inspired by/reimplementing Imperial’s CovidSim approach.                                              | [GitHub](https://github.com/SABS-R3-Epidemiology/epiabm)   |
| **OpenABM-Covid19**    |                               ABM | COVID-19 agent-based simulator from Oxford/BDI.                                                                                       | [GitHub](https://github.com/BDI-pathogens/OpenABM-Covid19) |
| **PyRoss**             |         Compartmental / inference | Python framework for structured compartmental epidemic modeling and inference.                                                        | [GitHub](https://github.com/rajeshrinet/pyross)            |
| **SEIRS+**             |           Network / compartmental | Python stochastic SEIRS/network epidemic modeling framework.                                                                          | [GitHub](https://github.com/ryansmcgee/seirsplus)          |
| **GEMFsim / FastGEMF** |                 Network spreading | Generalized epidemic mean-field simulation on networks.                                                                               | [GEMFsim](https://github.com/ayounap/GEMFsim)              |
| **Epigrass**           |                           Spatial | Python geospatial epidemic simulation framework.                                                                                      | [GitHub](https://github.com/fccoelho/epigrass)             |
| **EpiRust**            |                               ABM | Rust-based epidemic simulation framework.                                                                                             | [GitHub](https://github.com/thoughtworks/epirust)          |
| **Kendrick**           |           DSL / modeling language | Domain-specific language for epidemiological models.                                                                                  | [GitHub](https://github.com/KendrickOrg/kendrick)          |

EpiHiper, FRED, STEM, Epiabm, EpiModel, Atomica, and flepiMoP all have reasonably clear publication or institutional evidence of reuse. EpiHiper is described as a high-performance epidemic modeling framework for dynamic large-scale networks; FRED is explicitly published as an open-source system for modeling infectious diseases with census-based populations; EpiModel’s JSS paper describes it as an R package for infectious-disease population dynamics; and Atomica is documented as a compartmental modeling engine used for epidemics and health cascades. ([OUP Academic][1])

### Disease-specific or programmatic platforms

| Tool                            |                          Disease area | Brief description                                                               | Link                                                                    |
| ------------------------------- | ------------------------------------: | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **OpenMalaria**                 |                               Malaria | Stochastic malaria transmission and intervention simulator from Swiss TPH.      | [GitHub](https://github.com/SwissTPH/openmalaria)                       |
| **malariasimulation**           |                               Malaria | Individual-based malaria model in R/C++.                                        | [Docs](https://mrc-ide.github.io/malariasimulation/)                    |
| **MicroMoB**                    |                          Vector-borne | Modular mosquito-borne disease modeling.                                        | [GitHub](https://github.com/dd-harp/micromob)                           |
| **MGDrivE**                     |             Vector-borne / gene drive | Mosquito gene-drive and vector population/transmission simulation.              | [MGDrivE](https://marshalllab.github.io/MGDrivE/)                       |
| **Optima HIV**                  |                                   HIV | HIV epidemic analysis, allocative efficiency, and program-prioritization model. | [Optima HIV](https://optimamodel.com/hiv/)                              |
| **Optima TB**                   |                                    TB | TB transmission and allocative-efficiency modeling platform.                    | [Optima TB](https://optimamodel.com/tb/)                                |
| **Spectrum / Goals / AIM**      |                      HIV / demography | UNAIDS/Avenir Health planning and projection suite.                             | [Spectrum](https://www.avenirhealth.org/software-spectrum.php)          |
| **SimpactCyan**                 |                               HIV/STI | Individual-based HIV/STI simulation framework.                                  | [Docs](https://simpactcyan.readthedocs.io/)                             |
| **STDSIM**                      |                               HIV/STI | Long-running microsimulation model for STI/HIV transmission.                    | [Paper](https://www.jstor.org/stable/24048014)                          |
| **CEPAC**                       |                 HIV / clinical policy | HIV clinical and policy simulation model.                                       | [CEPAC](https://www.massgeneral.org/medicine/mpec/research/cepac-model) |
| **HPVsim**                      |                                   HPV | Agent-based HPV transmission and vaccination/screening model.                   | [HPVsim](https://hpvsim.org/)                                           |
| **FPsim**                       | Family planning / reproductive health | Agent-based reproductive-health and family-planning simulator.                  | [FPsim](https://fpsim.org/)                                             |
| **Poliosim / EMOD-polio tools** |                                 Polio | Polio transmission and intervention modeling, often within IDM ecosystem.       | [IDM tools](https://www.idmod.org/all-tools/)                           |

Optima HIV has documented use across more than 40 countries, and Optima TB has a peer-reviewed PLOS Computational Biology methods/application paper. Atomica underlies related compartmental/cascade analysis tooling. ([Optima][2])

### Rt estimation, nowcasting, forecasting, and outbreak analytics

| Tool                       |                          Type | Brief description                                                            | Link                                                           |
| -------------------------- | ----------------------------: | ---------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **EpiEstim**               |                 Rt estimation | Classic R package for estimating time-varying reproduction number.           | [EpiEstim](https://mrc-ide.github.io/EpiEstim/)                |
| **EpiNow2**                | Rt / nowcasting / forecasting | Bayesian real-time infection estimation, Rt estimation, and forecasting.     | [EpiNow2](https://epiforecasts.io/EpiNow2/)                    |
| **epinowcast**             |               Nowcasting / Rt | Modular Bayesian framework for delayed infectious-disease surveillance data. | [epinowcast](https://package.epinowcast.org/)                  |
| **NobBS**                  |                    Nowcasting | Bayesian nowcasting for delayed reporting.                                   | [GitHub](https://github.com/smc77/NobBS)                       |
| **outbreaker2**            |       Outbreak reconstruction | Bayesian reconstruction from epidemiological/genetic data.                   | [GitHub](https://github.com/reconhub/outbreaker2)              |
| **projections**            |        Short-term projections | R Epidemics Consortium outbreak projections package.                         | [GitHub](https://github.com/reconhub/projections)              |
| **incidence / incidence2** |              Incidence curves | Outbreak incidence handling and visualization.                               | [incidence2](https://www.repidemicsconsortium.org/incidence2/) |
| **surveillance**           |                  Surveillance | Aberration detection and infectious disease surveillance methods in R.       | [surveillance](https://surveillance.r-forge.r-project.org/)    |

EpiNow2 and epinowcast are good examples of reusable tooling rather than one-off models: EpiNow2 estimates Rt and infection dynamics using open-source Bayesian methods, while epinowcast focuses on delayed surveillance data and nowcasting. ([Epiforecasts][3])

### Genomic epidemiology / phylodynamics

| Tool                                   |                   Type | Brief description                                               | Link                                                      |
| -------------------------------------- | ---------------------: | --------------------------------------------------------------- | --------------------------------------------------------- |
| **BEAST / BEAST2**                     |          Phylodynamics | Bayesian evolutionary and phylodynamic inference.               | [BEAST2](https://www.beast2.org/)                         |
| **Nextstrain / Augur / Auspice**       |            Genomic epi | Real-time pathogen evolution and genomic epidemiology platform. | [Nextstrain](https://nextstrain.org/)                     |
| **TreeTime**                           |          Phylogenetics | Time-scaled phylogenies and ancestral reconstruction.           | [GitHub](https://github.com/neherlab/treetime)            |
| **TransPhylo**                         | Transmission inference | Transmission tree inference from pathogen phylogenies.          | [GitHub](https://github.com/xavierdidelot/TransPhylo)     |
| **phydynR**                            |          Phylodynamics | R tools for phylodynamic inference.                             | [GitHub](https://github.com/emvolz-phylodynamics/phydynR) |
| **PhyDyn / birth-death skyline tools** |          Phylodynamics | BEAST ecosystem tools for epidemic dynamics from sequence data. | [BEAST2 packages](https://www.beast2.org/packages/)       |

### Public-health epidemiology/statistics tools, less “transmission modeling”

| Tool         |                     Type | Brief description                                                      | Link                                                |
| ------------ | -----------------------: | ---------------------------------------------------------------------- | --------------------------------------------------- |
| **Epi Info** |       Field epi analysis | CDC epidemiology/statistics package, not mainly transmission modeling. | [CDC](https://www.cdc.gov/epiinfo/)                 |
| **OpenEpi**  | Public-health statistics | Web-based epidemiological statistics toolkit.                          | [OpenEpi](https://www.openepi.com/)                 |
| **epiR**     |         R epi statistics | Epidemiological analysis and reporting package.                        | [CRAN](https://cran.r-project.org/package=epiR)     |
| **epitools** |         R epi statistics | Basic epidemiological calculations.                                    | [CRAN](https://cran.r-project.org/package=epitools) |
| **epitrix**  |     R outbreak utilities | Helper functions for infectious-disease/outbreak analysis.             | [GitHub](https://github.com/reconhub/epitrix)       |

## Things I would now exclude or demote from the first list

I would **demote NetLogo, Mesa, AnyLogic, and GAMA** unless the goal is “platforms often used for disease ABMs.” They are not disease-modeling-specific, even if widely used for epidemic models.

I would also avoid ambiguous names like **Epipy** unless tied to a specific maintained package.

## Best “core global” shortlist

For a concise, fairly unbiased core set of reusable disease-modeling software, I’d start with:

**EpiHiper, FRED, EMOD, Starsim, Covasim, EpiModel, Atomica, SimInf, STEM, GLEAMviz, flepiMoP, Epiabm, OpenMalaria, malariasimulation, Optima HIV/TB, Spectrum, EpiEstim, EpiNow2, epinowcast, outbreaker2, BEAST2, Nextstrain.**

[1]: https://academic.oup.com/pnasnexus/article/4/1/pgae557/7921484?utm_source=chatgpt.com "Epihiper—A high performance computational modeling ..."
[2]: https://optimamodel.com/hiv/applications.html?utm_source=chatgpt.com "HIV | Applications"
[3]: https://epiforecasts.io/EpiNow2/?utm_source=chatgpt.com "EpiNow2: Estimate real-time case counts and ..."
