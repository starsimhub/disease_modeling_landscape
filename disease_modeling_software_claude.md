# Epidemiology / Disease Modeling Software Libraries

A global survey of software libraries specifically designed for infectious-disease and epidemiological modeling. Each entry has evidence of multi-group use and/or peer-reviewed publication.

## Methodology & caveats

The first version of this list was compiled from training-data recall, which over-indexed on a small set of well-known groups (IDM, Imperial / MRC IDE, RECON, statnet, BEAST community). This revision was supplemented by web searches across institutional ecosystems (Pasteur, RKI, ECDC, Swiss TPH, Burnet, SACEMA, UVA Biocomplexity, IHME, Eclipse / IBM, Epiverse-TRACE, NTD Modelling Consortium) and across topical sub-fields (veterinary, NTDs, wastewater, AMR, spatial mapping, genomic surveillance). Coverage is broader but still not exhaustive — disease-modeling software is a long tail with many one-off academic codes that don't quite meet the "multi-group reuse" bar. Tools below either (a) have a peer-reviewed publication, (b) have a maintained public repository with external users, or (c) are referenced in two or more independent reviews. URLs verified for primary tools; some are best-effort.

---

## 1. General-purpose / multi-disease frameworks

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| Starsim | Multi-disease agent-based modeling framework | Python | IDM / Starsim Hub | https://starsim.org |
| EMOD | Individual-based multi-disease platform (HIV, TB, malaria, polio, measles, COVID) | C++/Python | IDM | https://github.com/EMOD-Hub |
| EpiModel | Network, IBM, and DCM infectious-disease modeling, 125+ published studies | R | Statnet/Emory | https://epimodel.org |
| EpiHiper | Parallel agent-based socio-epidemic simulator on dynamic networks; CDC Scenario Modeling Hub | C++ | UVA Biocomplexity / NSSAC | https://github.com/NSSAC/EpiHiper |
| Atomica | Compartmental-model simulation engine for disease + cascade modeling (successor to Optima) | Python | Burnet Institute | https://github.com/atomicateam/atomica |
| MEmilio | Modular EpideMIcs simuLatIOn — ODE/SDE/IDE/LCT/metapop/ABM | C++/Python | RKI / DLR (Germany) | https://github.com/SciCompMod/memilio |
| STEM | Spatiotemporal Epidemiologic Modeler (Eclipse plugin platform) | Java | IBM Research / Eclipse Foundation | https://www.eclipse.org/stem/ |
| GLEAM / GLEAMviz | Global Epidemic and Mobility metapopulation simulator | C++/Java/web | ISI Foundation / Northeastern | https://www.gleamviz.org |
| FRED | Framework for Reconstructing Epidemic Dynamics (synthetic-population ABM) | C++ | U. Pittsburgh | https://github.com/PublicHealthDynamicsLab/FRED |
| EMULSION | Multi-level stochastic models with explicit declarative DSL | Python | INRAE | https://sourcesup.renater.fr/projects/emulsion-public/ |
| SimInf | Data-driven stochastic disease spread on networks (Gillespie / events) | R/C | SLU / Linköping (Sweden) | https://github.com/stewid/SimInf |
| Vivarium | Microsimulation framework using GBD distributions | Python | IHME / U. Washington | https://github.com/ihmeuw/vivarium |
| epidemics | Composable compartmental scenario models (curated lit. library) | R | Epiverse-TRACE / LSHTM | https://epiverse-trace.github.io/epidemics/ |
| epidemik | Flexible compartmental modeling | Python | (community) | https://pypi.org/project/epidemik/ |
| MetaCast | Metapopulation broadcasting of epi/eco models | Python | (community) | https://github.com/MetaCast |
| Epydemix | Compartmental modeling with ABC calibration | Python | ISI / Northeastern | https://github.com/ngozzi/epydemix |
| GEMS | General-purpose individual-based simulator | Java | (academic) | (academic refs) |
| Vahana.jl | Large-scale agent-based epi modeling | Julia | U. Bamberg | https://github.com/s-fuerst/Vahana.jl |
| MatSim-EpiSim | Activity-based mobility epidemic model | Java | TU Berlin | https://github.com/matsim-org/matsim-episim-libs |
| RepastHPC | Parallel agent-based simulation toolkit (epi widely used) | C++ | Argonne National Lab | https://repast.github.io |
| OpenCOVID | Spatial agent-based epidemic framework | Julia/Python | Swiss TPH | https://github.com/SwissTPH/OpenCOVID |
| Pathogen.jl | Bayesian individual-level disease modeling | Julia | (academic) | https://github.com/jangevaare/Pathogen.jl |
| Mesa | General ABM framework, widely used for epi models | Python | Project Mesa | https://github.com/projectmesa/mesa |
| NetLogo | General ABM platform with extensive epi-model library | Scala/Java | Northwestern CCL | https://ccl.northwestern.edu/netlogo/ |

## 2. Compartmental modeling, ODE/SDE solvers, and inference

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| pomp | Partially Observed Markov Processes (state-space epi inference) | R | U. Michigan (Ionides/King) | https://kingaa.github.io/pomp/ |
| odin | DSL for ODE/discrete-time models | R | MRC IDE Imperial | https://mrc-ide.github.io/odin/ |
| dust | Stochastic simulation engine paired with odin | R/C++ | MRC IDE Imperial | https://mrc-ide.github.io/dust/ |
| odin.dust / odin2 | Fast ODE/discrete sims compiled via dust | R | MRC IDE Imperial | https://mrc-ide.github.io/odin2/ |
| mcstate | pMCMC / particle filter for odin/dust | R | MRC IDE Imperial | https://mrc-ide.github.io/mcstate/ |
| epidemia | Bayesian semi-mechanistic epidemic regression (Stan) | R | Imperial (Bhatt/Flaxman) | https://imperialcollegelondon.github.io/epidemia/ |
| LEMMA | Local Epidemic Modeling for Management & Action | R/Stan | UCSF | https://github.com/LocalEpi/LEMMA |
| PyRoss | Inference, prediction, control of epidemics (ODE/SDE) | Python | U. Cambridge | https://github.com/rajeshrinet/pyross |
| epipack | Numerical + symbolic compartmental modeling | Python | HU Berlin | https://github.com/benmaier/epipack |
| BayesianTools | MCMC tooling commonly used for epi inference | R | (academic) | https://github.com/florianhartig/BayesianTools |
| rstanarm / brms | Bayesian regression backbones used by many epi packages | R/Stan | Stan team | https://mc-stan.org |
| greta | TF-based Bayesian inference, used for epi | R | (community) | https://greta-stats.org |

## 3. Rt estimation, nowcasting, and forecasting

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| EpiEstim | Time-varying Rt from incidence (Cori method) | R | MRC IDE Imperial | https://mrc-ide.github.io/EpiEstim/ |
| EpiNow2 | Real-time Rt + short-term forecasts | R/Stan | epiforecasts / LSHTM | https://epiforecasts.io/EpiNow2/ |
| epinowcast | Hierarchical nowcasting of right-truncated data | R/Stan | epiforecasts | https://package.epinowcast.org |
| estimateR | Rt with deconvolution; clinical or wastewater | R | ETH Zurich | https://github.com/covid-19-Re/estimateR |
| ern | Rt from clinical or wastewater surveillance | R | PHAC / academic | https://cran.r-project.org/package=ern |
| EpiSewer | Bayesian Rt from wastewater concentrations | R/Stan | ETH Zurich | https://github.com/adrian-lison/EpiSewer |
| R0 | Reproduction-number estimation toolbox | R | Hospices Civils Lyon | https://cran.r-project.org/package=R0 |
| earlyR | Rt during early outbreak phase | R | RECON | https://www.repidemicsconsortium.org/earlyR/ |
| projections | Short-term incidence projections | R | RECON | https://www.repidemicsconsortium.org/projections/ |
| EpiSoon | Short-term Rt forecasting | R | epiforecasts | https://epiforecasts.io/EpiSoon/ |
| EpiLPS | Laplacian-P-splines for Rt | R | UCLouvain | https://cran.r-project.org/package=EpiLPS |
| scoringutils | Probabilistic forecast scoring | R | epiforecasts | https://epiforecasts.io/scoringutils/ |
| hubverse / hubUtils | Forecast-hub infrastructure (FluSight, COVID-Forecast Hub, Scenario Modeling Hub) | R/Python | CDC / Reich Lab | https://hubverse.io |
| Multi-target Multi-scale Forecasting Framework | Ensemble (AR, Kalman, LSTM, compartmental) — UVA hub submissions | Python/R | UVA Biocomplexity | http://covid19-forecast.uvadsos.io/ |
| PatchSim | National-scale metapopulation forecasting | Python | UVA NSSAC | https://github.com/nssac/patchsim |

## 4. Outbreak analytics & data toolkits

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| incidence / incidence2 | Incidence curves from line lists | R | RECON / Epiverse-TRACE | https://www.reconverse.org/incidence2/ |
| linelist | Line-list cleaning + tagged variables | R | Epiverse-TRACE | https://www.reconverse.org/linelist/ |
| epicontacts | Contact-tracing data structures | R | RECON | https://www.repidemicsconsortium.org/epicontacts/ |
| outbreaker2 | Reconstruct who-infected-whom (genomic + epi) | R | RECON | https://github.com/reconhub/outbreaker2 |
| o2geosocial | Outbreaker2 with spatial + age data | R | (academic) | https://github.com/alxsrobert/o2geosocial |
| TransPhylo | Transmission trees from dated phylogenies | R | Oxford (Didelot) | https://github.com/xavierdidelot/TransPhylo |
| outbreaks | Curated outbreak datasets | R | RECON | https://github.com/reconverse/outbreaks |
| epitrix | Small helpers for outbreak analysis | R | RECON | https://github.com/reconhub/epitrix |
| distcrete | Discretised delay distributions | R | RECON | https://github.com/reconhub/distcrete |
| epiparameter | Curated library of epi parameters | R | Epiverse-TRACE | https://epiverse-trace.github.io/epiparameter/ |
| simulist | Simulate line-list & contacts | R | Epiverse-TRACE | https://epiverse-trace.github.io/simulist/ |
| finalsize | Final-size calculations for heterogeneous pops | R | Epiverse-TRACE | https://epiverse-trace.github.io/finalsize/ |
| EpiContactTrace | Network contact tracing for livestock | R | SLU (Sweden) | https://cran.r-project.org/package=EpiContactTrace |

## 5. Network-based epidemic modeling

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| EoN (Epidemics on Networks) | SIS/SIR simulation on networks | Python | Joel Miller / community | https://github.com/springer-math/Mathematics-of-Epidemics-on-Networks |
| NDlib | Network Diffusion library | Python | CNR Italy | https://ndlib.readthedocs.io |
| statnet / ergm | Exponential random graph models for contact nets | R | U. Washington / Statnet | https://statnet.org |
| EpiModel-networks module | Stochastic network epidemic models on tergm | R | Statnet/Emory | https://epimodel.org |
| socialmixr | Contact matrices from POLYMOD-style surveys | R | epiforecasts | https://github.com/epiforecasts/socialmixr |
| contactdata | Prem et al. synthetic contact matrices for 152 countries | R | (community) | https://cran.r-project.org/package=contactdata |
| sispread | Disease spread on contact networks | C/Python | (academic) | (PubMed 17224976) |

## 6. Phylodynamics & genomic epidemiology

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| BEAST | Bayesian Evolutionary Analysis Sampling Trees | Java | U. Edinburgh / Auckland | https://beast.community |
| BEAST2 | Modular successor to BEAST | Java | BEAST2 dev team | https://www.beast2.org |
| Nextstrain (Augur / Auspice) | Real-time pathogen evolution dashboard + pipeline | Python/JS | Bedford / Neher labs | https://nextstrain.org |
| Nextclade | Clade assignment, mutation calling, QC | TypeScript/Rust | Neher Lab | https://clades.nextstrain.org |
| TreeTime | ML phylodynamic inference | Python | Neher Lab | https://github.com/neherlab/treetime |
| Pangolin | SARS-CoV-2 lineage assignment | Python | Cov-Lineages / Edinburgh | https://github.com/cov-lineages/pangolin |
| Civet | Phylogenetic placement reports for outbreaks | Python | Cov-Lineages / Edinburgh | https://github.com/artic-network/civet |
| Scorpio | SNP-based variant constellation calling | Python | Cov-Lineages | https://github.com/cov-lineages/scorpio |
| UShER | Ultrafast Sample placement on Existing tRees | C++ | UCSC | https://github.com/yatisht/usher |
| phylodyn | Bayesian nonparametric phylodynamics | R | (Karcher/Suchard) | https://github.com/mdkarcher/phylodyn |
| PhyDyn | Structured-coalescent phylodynamics (BEAST2) | Java | Imperial (Volz) | https://github.com/mrc-ide/PhyDyn |
| MASCOT | Marginal approximation of structured coalescent | Java | Müller / Stadler (ETH) | https://github.com/nicfel/Mascot |
| skygrowth | Phylodynamic effective-population-size inference | R | Imperial (Volz) | https://github.com/mrc-ide/skygrowth |
| RevBayes | Bayesian phylogenetic inference (incl. epi/diversification) | C++ | (Höhna et al.) | https://revbayes.github.io |
| BEAGLE | High-perf likelihood library used by BEAST/BEAST2/MrBayes | C++ | (community) | https://github.com/beagle-dev/beagle-lib |
| ARTIC pipeline | Reference protocols + Nextflow pipelines for viral genomics | Python/Nextflow | ARTIC network | https://artic.network |
| adegenet | Multivariate genetic analysis (DAPC etc.) | R | Imperial (Jombart) | https://github.com/thibautjombart/adegenet |

## 7. Spatial epidemiology / disease mapping

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| R-INLA | Integrated Nested Laplace Approximation; standard for hierarchical spatial epi | R/C | (Rue et al.) | https://www.r-inla.org |
| SpatialEpi | Cluster detection + disease mapping | R | (community) | https://cran.r-project.org/package=SpatialEpi |
| CARBayes | MCMC for spatial CAR/BYM models | R | U. Glasgow | https://cran.r-project.org/package=CARBayes |
| DClusterm | Model-based detection of disease clusters | R | (Gomez-Rubio) | https://cran.r-project.org/package=DClusterm |
| diseasemapping | Modeling disease maps | R | U. Toronto | https://cran.r-project.org/package=diseasemapping |
| INLA-SPDE | Stochastic PDE approach for geostatistical epi | R | (Lindgren/Rue) | (via R-INLA) |
| hhh4 / surveillance | Spatio-temporal endemic-epidemic count models | R | LMU / RKI | https://cran.r-project.org/package=surveillance |
| sf / spdep / spatstat | Geospatial backbones used widely in epi | R | (community) | (CRAN) |
| MAP / malariaAtlas | Malaria Atlas Project tooling | R/Python | Oxford BDI | https://malariaatlas.org |

## 8. Surveillance, aberration detection, and genomic surveillance

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| surveillance | Temporal/spatio-temporal monitoring of count data | R | LMU / RKI | https://surveillance.r-forge.r-project.org |
| EARS / Farrington | Aberration-detection algorithms (in `surveillance`) | R | CDC / PHE origin | (above) |
| SaTScan | Spatial/space-time scan statistics for clusters | C++/GUI | M. Kulldorff | https://www.satscan.org |
| FluView / DELPHI EpiData | Surveillance-data API for forecasting | Python/R | CMU DELPHI | https://cmu-delphi.github.io/delphi-epidata/ |
| Epi Info | CDC outbreak/field epi platform | C# | CDC | https://www.cdc.gov/epiinfo/ |
| SurvNet@RKI | Notifiable-disease surveillance | (proprietary) | RKI Germany | (RKI ref) |

## 9. Disease-specific: HIV

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| Spectrum / EPP | UNAIDS HIV estimates & projections (national) | C++/GUI | Avenir Health / UNAIDS | https://avenirhealth.org/software-spectrum.php |
| Goals / Goals-ART | Resource-allocation HIV model | Spectrum module | Avenir Health | (above) |
| Thembisa | South African HIV epidemic model (basis for UNAIDS SA estimates) | R/Excel | U. Cape Town (Johnson) | https://thembisa.org |
| MicroCOSM | ABM of social/structural drivers of HIV in SA | C++ | SACEMA / UCT | (bioRxiv 310763) |
| ECDC HIV Modelling Tool / hivPlatform | Back-calculation of HIV incidence from surveillance | R | ECDC | https://github.com/EU-ECDC/hivPlatform |
| HIV Synthesis | Individual-based HIV model | (custom) | UCL (Phillips) | (PubMed refs) |
| PopART-IBM | Individual-based HIV model | C | Imperial / UCT | https://github.com/p-robot/POPART-IBM |
| EMOD-HIV | IDM HIV agent-based model | C++ | IDM | https://github.com/EMOD-Hub/emodpy-hiv |
| HIVsim (Starsim) | Starsim-based HIV model | Python | Starsim Hub | https://github.com/starsimhub/hivsim |
| Optima HIV | Allocative-efficiency HIV model | Python | Optima Consortium | http://optimamodel.com |
| HIV-CDM | HIV cost-effectiveness microsimulation (CEPAC) | C++ | MGH / Harvard | https://www.massgeneral.org/medicine/mpec/research/cepac |
| ARTcost | Cost projection model | Excel/R | (academic) | (refs) |
| AIDS Epidemic Model (AEM) | Model used in Asia-Pacific projections | Spectrum module | East-West Center | (UNAIDS docs) |

## 10. Disease-specific: Tuberculosis

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| TIME Impact | TB intervention impact (Spectrum module) | C++/GUI | Avenir Health / LSHTM | https://avenirhealth.org/software-time.php |
| EMOD-TB | IDM TB agent-based model | C++ | IDM | (EMOD-Hub) |
| TBVx | Vaccine-impact TB model | Python | KNCV / TB Modelling | https://github.com/kncvtbplus/tbvx |
| TBMAC suite | Modeling consortium curated TB models | various | TB MAC | https://tb-mac.org |

## 11. Disease-specific: Malaria

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| OpenMalaria | Individual-based P. falciparum simulator | C++ | Swiss TPH | https://github.com/SwissTPH/openmalaria |
| malariasimulation | Imperial individual-based malaria model | R/C++ | Imperial MRC IDE | https://github.com/mrc-ide/malariasimulation |
| malariaEquilibrium | Equilibrium solver for Imperial model | R | Imperial MRC IDE | https://github.com/mrc-ide/malariaEquilibrium |
| AnophelesModel | Vector bionomics for malaria | R | Swiss TPH | https://github.com/SwissTPH/AnophelesModel |
| EMOD-Malaria | IDM malaria ABM with vector compartments | C++ | IDM | https://github.com/EMOD-Hub/emodpy-malaria |
| MultiMalModPy | Comparator harness for EMOD/OpenMalaria/malariasimulation | Python | AHADI / IDM | (AHADI) |
| Skeeter Buster | Spatially explicit Aedes/Anopheles model | C++ | NC State / NSF | (academic) |
| eMOD-MAP | Bridging Map atlas + EMOD malaria | Python | MAP / IDM | (community) |
| OpenMalaria-MESA | MESA Malaria knowledge hub deployment | C++ | MESA | https://mesamalaria.org |

## 12. Disease-specific: Neglected Tropical Diseases (NTD)

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| ONCHOSIM | Onchocerciasis transmission & control | Pascal/Python | Erasmus MC | https://github.com/NTD-Modelling-Consortium |
| EPIONCHO-IBM | Onchocerciasis individual-based model | R | Imperial / Warwick | https://github.com/NTD-Modelling-Consortium/EPIONCHO-IBM |
| LYMFASIM | Lymphatic filariasis stochastic microsim | Pascal/Python | Erasmus MC | (NTD-MC GitHub) |
| TRANSFIL | LF transmission model | C++ | Warwick / NTD-MC | https://github.com/NTD-Modelling-Consortium/transfil |
| SCHISTOX | Schistosomiasis individual-based model | Julia | Oxford | https://github.com/mattg-epi/SCHISTOX |
| SCHISTO (Imperial) | Compartmental schistosomiasis model | R | Imperial | (NTD-MC) |
| TRACHOMA-AMIS | Trachoma stochastic ind. model | Python/R | LSHTM / Warwick | (NTD-MC) |
| WORMSIM | Soil-transmitted helminth | Pascal/Python | Erasmus MC | (NTD-MC) |
| HAT model (Warwick/Imperial) | Human African trypanosomiasis | R | Warwick / Imperial | (NTD-MC) |
| LeishMod | Visceral leishmaniasis transmission | R | LSHTM / Warwick | (NTD-MC) |
| Chagas-EpiPath | Chagas transmission models | R | (NTD-MC) | (NTD-MC) |

## 13. Disease-specific: COVID-19 / respiratory pathogens

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| Covasim | Agent-based COVID-19 model | Python | IDM | https://covasim.org |
| CovidSim | Imperial College pandemic ABM | C++ | Imperial (Ferguson) | https://github.com/mrc-ide/covid-sim |
| OpenABM-Covid19 | Network ABM of COVID-19 | C/Python | Oxford BDI | https://github.com/BDI-pathogens/OpenABM-Covid19 |
| EpiABM | Re-implementation of CovidSim | Python/C++ | Cambridge / Imperial | https://github.com/SABS-R3-Epidemiology/epiabm |
| JUNE | Individual-based epidemic model | Python/C++ | Durham / IHME | https://github.com/IDAS-Durham/JUNE |
| ACEMod | Australian Census-based Epidemic Model | C++ | U. Sydney | https://github.com/SystemsAndComplexity/ACEMod-COVID-19 |
| Episimmer | Institutional reopening simulator | Python | IIIT Hyderabad / HealthBadge | https://github.com/healthbadge/episimmer |
| Pandemia | Stochastic pandemic simulator | Python | Pandemia UK | https://github.com/PandemiaUK/Pandemia |
| FluTE | Stochastic influenza simulator | C++ | FHCRC | https://github.com/dlchao/FluTE |
| MOCOS | Microsimulation of COVID-19 | C++/Julia | Wroclaw/Linköping | http://mocos.pl |
| CoMo Consortium | CoMo COVID-19 model | R | Oxford / global consortium | https://www.como.bsg.ox.ac.uk |
| LEMMA | UCSF COVID-19 Bayesian model | R/Stan | UCSF | https://github.com/LocalEpi/LEMMA |
| MEmilio (COVID) | Used widely for German COVID-19 forecasts | C++/Python | RKI / DLR | https://github.com/SciCompMod/memilio |
| FluSurv-Network / FluSight | Influenza ensemble forecasting | R/Python | CDC / Reich Lab | https://flusightnetwork.io |
| RSV-MODEL ensemble | RSVnet, immunity models | R | (community) | (CDC RSV hub) |

## 14. Disease-specific: STIs, vector-borne, vaccine-preventable, other

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| HPVsim | Agent-based HPV / cervical cancer model | Python | IDM / Starsim | https://hpvsim.org |
| FPsim | Agent-based family-planning model | Python | IDM / Starsim | https://fpsim.org |
| STIsim | Starsim-based STI model | Python | Starsim Hub | https://github.com/starsimhub/stisim |
| Polio model (IDM) | Agent-based polio transmission | C++/Python | IDM | (EMOD-Hub) |
| MeaslesModel (Imperial) | Compartmental measles dynamics | R | LSHTM / Imperial | (academic refs) |
| denguesim | Aedes aegypti dengue dynamics | R/C++ | (academic) | (refs) |
| OpenWASH / cholera (JHU) | Cholera transmission | R | JHU | (academic refs) |
| ZikaSpread | Zika spatial model | Python | Northeastern / ISI | (academic) |
| EboVaxSim | Ebola vaccination | R | LSHTM | (academic) |
| Spectrum FamPlan / DemProj / GBM | Demographic & FP projection modules | C++ | Avenir Health | https://avenirhealth.org/software-spectrum.php |
| LiST (Lives Saved Tool) | MNCH intervention impact | C++/GUI | JHSPH / Avenir | https://www.livessavedtool.org |

## 15. Veterinary / animal / zoonotic disease modeling

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| InterSpread Plus (ISP) | Spatial stochastic livestock disease model | C++ | Massey U. (NZ) | (Massey EpiCentre) |
| NAADSM | North American Animal Disease Spread Model (FMD etc.) | C/GUI | USDA/CFIA/Colorado State | https://github.com/NAADSM |
| AusSpread | Australian livestock disease model | C++/GUI | NSW DPI | (DPI docs) |
| AADIS | Australian Animal Disease Spread (hybrid) | C# | CSIRO / DAFF | (academic refs) |
| EpiSAM | Stochastic livestock disease | (custom) | (academic) | (refs) |
| be-FAST / be-CSF | Africa swine fever / CSF spread | C++ | UCM Madrid | (academic refs) |
| ASFV-IBM | African swine fever individual-based | R | (academic) | (refs) |
| HPAIv-spread | Highly-pathogenic avian influenza | R | (academic) | (refs) |
| EpiContactTrace | Livestock movement contact tracing | R | SLU Sweden | https://cran.r-project.org/package=EpiContactTrace |

## 16. Wastewater & environmental epidemiology

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| EpiSewer | Bayesian Rt from wastewater | R/Stan | ETH Zurich | https://github.com/adrian-lison/EpiSewer |
| ern | Rt from wastewater + clinical data | R | PHAC | https://cran.r-project.org/package=ern |
| WES | Wastewater & environmental sampling toolkit | R | (community) | https://www.r-wes.com |
| CDC NWSS-tools | National wastewater surveillance pipelines | Python | CDC | (CDC docs) |

## 17. Microsimulation, health-economics, and decision-analytic frameworks

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| heemod | Markov / state-transition CEA | R | (Antoine Filipović) | https://cran.r-project.org/package=heemod |
| hesim | Health-economic simulation modeling | R | (Devin Incerti) | https://hesim-dev.github.io/hesim/ |
| TreeAge Pro | Decision-tree / Markov modeling | proprietary | TreeAge | https://www.treeage.com |
| Amua | Open-source decision analysis | Java | (Smith) | https://github.com/zward/Amua |
| CEPAC | Cost-Effectiveness of Preventing AIDS Complications | C++ | MGH / Harvard | https://www.massgeneral.org/medicine/mpec |
| Vivarium | GBD-driven microsimulation | Python | IHME | https://github.com/ihmeuw/vivarium |
| Synthea | Synthetic patient generator (HL7/FHIR) | Java | MITRE | https://synthetichealth.github.io/synthea/ |
| SynthPops | Synthetic populations for ABMs | Python | IDM | https://github.com/InstituteforDiseaseModeling/synthpops |

## 18. Domain-general modeling platforms widely used for disease

| Name | Description | Language | Origin | Link |
|---|---|---|---|---|
| Berkeley Madonna | ODE solver, classic for SIR-class models | proprietary | UC Berkeley | https://berkeley-madonna.com |
| Vensim | System dynamics platform used in epi | proprietary | Ventana Systems | https://vensim.com |
| Stella / iThink | System dynamics modeling | proprietary | isee systems | https://www.iseesystems.com |
| AnyLogic | Multi-method simulation; epi templates | proprietary | AnyLogic North America | https://www.anylogic.com |
| InsightMaker | Browser-based SD / ABM | JavaScript | (community) | https://insightmaker.com |

## 19. Spectrum and Spectrum-family planning tools

| Name | Description | Origin | Link |
|---|---|---|---|
| Spectrum suite | Umbrella for AIM/Goals/TIME/FamPlan/DemProj/LiST | Avenir Health | https://avenirhealth.org/software-spectrum.php |
| AIM | AIDS Impact Model | Avenir Health | (above) |
| FamPlan | Family planning projections | Avenir Health | (above) |
| DemProj | Demographic projections | Avenir Health | (above) |
| GBM | Goals Burden Model | Avenir Health | (above) |
| OneHealth Tool | Costing of national health strategies | UN inter-agency | https://avenirhealth.org/software-onehealth.php |

## 20. Optima family

| Name | Description | Origin | Link |
|---|---|---|---|
| Optima HIV | HIV allocative efficiency | Optima Consortium / Burnet | http://optimamodel.com |
| Optima TB | TB allocative efficiency | Optima Consortium | (above) |
| Optima Nutrition | Nutrition allocation | Optima Consortium / WB | (above) |
| Atomica | Generic compartmental engine (successor) | Burnet Institute | https://github.com/atomicateam/atomica |

---

*Compiled 2026-05-06. Tools listed have peer-reviewed publication and/or maintained public repositories with multi-group adoption. Where a URL was not directly verified during compilation, the entry is annotated as such.*

## Sources used during compilation
- [EpiHiper (PNAS Nexus 2024)](https://academic.oup.com/pnasnexus/article/4/1/pgae557/7921484)
- [MEmilio paper (arXiv)](https://arxiv.org/html/2602.11381) — comparative table of compartmental/ABM/network/mobility frameworks
- [UVA NSSAC modeling capabilities](https://nssac.github.io/modeling_capabilities/index)
- [Atomica GitHub](https://github.com/atomicateam/atomica)
- [Modelling for policy: NTD Modelling Consortium (PLOS NTDs)](https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0008033) and [NTD-MC GitHub](https://github.com/NTD-Modelling-Consortium)
- [ECDC HIV Modelling / Platform Tool](https://www.ecdc.europa.eu/en/publications-data/hiv-platform-tool)
- [Thembisa Project](https://thembisa.org/)
- [MicroCOSM (bioRxiv)](https://www.biorxiv.org/content/10.1101/310763v1.full)
- [Veterinary FMD model comparison (PLOS One)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0092521)
- [Malaria: AHADI comparative analysis](https://www.appliedhealthanalytics.org/analytic/comparative-analysis-of-mathematical-models)
- [Epiverse-TRACE (epidemics, epiparameter, simulist, finalsize)](https://epiverse-trace.github.io/)
- [SimInf](https://github.com/stewid/SimInf)
- [GLEAMviz / GLEAM Project](https://www.gleamviz.org)
- [STEM (Eclipse / IBM Research)](https://research.ibm.com/publications/stem-an-open-source-tool-for-disease-modeling)
- [Pangolin / Civet / Scorpio / Nextclade](https://cov-lineages.org)
- [ern (PLOS One 2024)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0305550)
- [EpiSewer](https://github.com/adrian-lison/EpiSewer)
- [Vivarium (IHME)](https://github.com/ihmeuw/vivarium)
- [socialmixr / POLYMOD / Prem matrices](https://epiforecasts.io/socialmixr/)
- [Publicly available software tools for decision-makers (ScienceDirect 2017)](https://www.sciencedirect.com/science/article/pii/S1755436517300804)
