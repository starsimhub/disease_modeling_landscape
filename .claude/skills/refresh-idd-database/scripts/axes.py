"""
Search axes for IDD tool discovery.

Each axis crosses a set of subject terms with a set of software terms. The `core`
axis is the original grid; `estimation` and `serology` were added after that grid
was found to have missed Naomi and the whole serology family -- see
references/search.md for why, and add a new axis here rather than inline in
discover.py when the next blind spot turns up.
"""

SOFTWARE_TERMS_DEV = ['package', 'framework', 'platform', 'library', 'toolkit', 'simulator', 'pipeline']

# Naomi calls itself an "interactive web-based software tool", not a library. Tools written up
# for a health audience rather than a methods one need this wider set to be visible at all.
SOFTWARE_TERMS_USER = ['tool', 'software', 'application', 'web-based tool', 'shiny app', 'dashboard', 'calculator']

AXES = {
    'core': {
        'subject': ['epidemic', 'infectious disease', 'outbreak', 'transmission', 'metapopulation',
                    'agent-based', 'compartmental', 'SEIR', 'nowcasting', 'phylodynamic'],
        'software': SOFTWARE_TERMS_DEV,
    },
    'estimation': {
        'subject': ['small-area estimation', 'disease mapping', 'prevalence mapping',
                    'model-based geostatistics', 'spatial disaggregation', 'burden estimation',
                    'subnational estimates', 'evidence synthesis', 'incidence estimation', 'risk mapping'],
        'software': SOFTWARE_TERMS_DEV + SOFTWARE_TERMS_USER,
    },
    'serology': {
        'subject': ['seroprevalence', 'serological survey', 'force of infection', 'serocatalytic',
                    'seroincidence', 'antibody kinetics'],
        'software': SOFTWARE_TERMS_DEV + SOFTWARE_TERMS_USER,
    },
    'ai': {
        'subject': ['large language model epidemiology', 'LLM agent outbreak', 'AI copilot public health',
                    'MCP server epidemiology'],
        'software': ['agent', 'assistant', 'plugin', 'server'],
    },
}

# Venues that publish software papers. Crossref `query.container-title` is fuzzy, which is fine here:
# a false match costs one line of triage, a missing venue costs a whole family of tools.
VENUES = [
    'Journal of Open Source Software',
    'Epidemics',
    'Journal of Statistical Software',
    'Journal of Open Research Software',
    'SoftwareX',
    'PLOS Computational Biology',
    'Infectious Disease Modelling',
    'Wellcome Open Research',
    'F1000Research',
]

GITHUB_TOPICS = [
    'epidemiology', 'epidemic-simulation', 'agent-based-model', 'infectious-diseases',
    'epidemic-model', 'disease-modeling', 'compartmental-model', 'outbreak-analytics',
]

GITHUB_KEYWORDS = [
    'epidemic simulation', 'infectious disease model', 'outbreak analytics',
    'transmission model', 'seroprevalence', 'disease mapping',
]

# Crossed with epidemiology terms when hunting for the (currently empty) AI extension category.
GITHUB_AI_KEYWORDS = ['mcp-server epidemiology', 'llm public health', 'agent outbreak', 'copilot epidemiology']

CRAN_TASK_VIEW = 'https://cran.r-project.org/web/views/Epidemiology.html'
