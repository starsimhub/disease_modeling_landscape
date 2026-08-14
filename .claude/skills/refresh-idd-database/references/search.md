# Search strategy

The rule that generated everything below: **search by vocabulary, never by author or project name.** Naming the projects you already know about only confirms what you know. Every discovery pass here is keyword-, topic-, or venue-based; author and project names are used only afterwards, to look up a candidate you already found.

The canonical axis definitions live in `../scripts/axes.py` and are what `discover.py` executes. This file explains why they are what they are.

## Pass 1 — the original grid (core axis)

Modelling terms × software terms, run against Crossref corpus-wide and restricted to software venues, plus GitHub and CRAN.

- **Modelling terms:** epidemic, infectious disease, outbreak, transmission, metapopulation, agent-based, compartmental, SEIR, nowcasting, phylodynamic
- **Software terms:** package, framework, platform, library, toolkit, simulator, pipeline
- **Venues:** JOSS, *Epidemics*, *Journal of Statistical Software*, *Journal of Open Research Software*, *SoftwareX*, *PLOS Computational Biology*, *Infectious Disease Modelling*
- **GitHub topics:** `epidemiology`, `epidemic-simulation`, `agent-based-model`, `infectious-diseases`, `epidemic-model`, `disease-modeling`, `compartmental-model`, `outbreak-analytics`
- **CRAN:** the [Epidemiology Task View](https://cran.r-project.org/web/views/Epidemiology.html), as a curated index of the R side

This grid recovers epipack and epiworldR from the JOSS-restricted query and flepiMoP from the *Epidemics* query. It found 24 tools the original LLM-recall compilation had missed.

## Pass 2 — the documented blind spot

The grid missed [Naomi](https://doi.org/10.1002/jia2.25788), and it missed it on **both** axes at once:

- Every modelling term was a *transmission-dynamics* word. Naomi infers burden from survey and programme data; it does not simulate spread.
- Every software term was a *developer* word. Naomi calls itself an "interactive web-based software tool".

The blind spot was therefore a whole shape of tool — *estimate the burden from data*, published for a health audience rather than a methods one. Two axes were added, and the second one, serology, turned up an entire missing family, which is the strongest evidence that vocabulary gaps come in clusters rather than singly.

- **estimation axis:** small-area estimation, disease mapping, prevalence mapping, model-based geostatistics, spatial disaggregation, burden estimation, subnational estimates, evidence synthesis, incidence estimation, risk mapping → *found Naomi, first90, disaggregation, prevR*
- **serology axis:** seroprevalence, serological survey, force of infection, serocatalytic, seroincidence, antibody kinetics → *found serofoi, serosolver, serosim, Rsero, serocalculator*
- **widened software terms:** tool, software, application, web-based tool, shiny app, platform, dashboard, calculator — alongside the original six

## Pass 3 — AI extensions

GitHub repo search crossing `epidemiology`/`public-health`/`outbreak`/`disease` with `mcp-server`, `llm`, `agent`, `copilot`, plus Crossref queries for LLM agents and copilots in epidemic modelling.

As of 2026-08-07 nothing qualifies, and the three failure modes are worth re-testing rather than re-deriving: general biomedical MCP servers (not IDD-unique, no publication); IDD-specific MCP servers and dashboards (0–22 stars, no publication, README-only docs); LLM forecasting research code such as PandemicLLM (peer-reviewed but a replication package, not a reusable tool). This category moves fastest and deserves re-checking on a much shorter cycle than the rest.

## Communities and ecosystems

**Communities** were seeded from the eight examples in `details.md`, then extended by systematic search across categories rather than by name: research consortia and modelling networks; funder-convened groups; national and regional public-health modelling networks; scenario and forecast hub consortia; open-source community organisations; disease-specific consortia (malaria, TB, HIV, polio, measles, HPV, NTDs, cholera, rabies, dengue, AMR, hepatitis); training and capacity networks; regional networks in LMICs. Cross-check against GSIDD's own [IDD Orgs page](https://www.gsidd.org/idd-orgs), which surfaced AM2NTD and CEMA.

**Ecosystems** were seeded from the four named in `details.md`, then extended from `database_tools.md` itself, from GitHub org listings for every institution appearing in that file, from web searches for "-verse"-style umbrella branding, and by following dependency edges out of known ecosystem packages. Confirm claimed dependencies by reading `DESCRIPTION`, `pyproject.toml`, `setup.py`, `Project.toml`, `environment.yml` — this is how `epiforecasts` was found to have zero mutual dependencies among `EpiNow2`, `scoringutils`, `socialmixr` and `ringbp`, and how Optima HIV/Nutrition were found not to run on Atomica.

## Known limitations to restate, not rediscover

- Keyword search only finds tools that describe themselves in the vocabulary searched. The most likely remaining misses are tools whose papers avoid the word "model" altogether.
- English-language, and Crossref/GitHub/CRAN/PyPI-indexed. Tools published in other languages, hosted on institutional servers or non-GitHub forges, or documented only in grey literature are under-represented. Nothing was found from China, India, Japan or Francophone Africa — a search artefact, not a picture of the field.
- Institutional ecosystems are trivially discoverable; genuinely distributed ones are not. The `pomp` family was nearly missed on this alone.
- Under-covered domains: NTD modelling, veterinary and livestock modelling outside Europe, within-host and immunological modelling, IDD-specific health economics.
- Crossref bibliographic search is noisy for tools whose papers are written for a health audience; for those, domain-specific web search works better than more Crossref queries.
- WebSearch quota has been exhausted mid-session before. Fall back to WebFetch against lite.duckduckgo.com, Bing or Mojeek, and note in the report that coverage was degraded.
