## 8. Reading the log

Each run writes one row a simulated year to `log.csv`. Open it in any spreadsheet, or read it with `summarise.py`.

**Table 6.** The columns of `log.csv`.

| Column | Meaning |
|---|---|
| `year` | Simulated years since the world was created (400 ticks each) |
| `population`, `pop_west`, `pop_east` | Agents alive at the year's end, in total and on each bank |
| `crossings` | Times agents changed bank during the year (only possible at fords) |
| `mean_energy` | Mean energy of a living agent (out of 150) |
| `nutrients`, `detritus`, `river_load` | Energy in each pool; with the agents' bodies they always sum to the total |
| `max_generation` | The deepest lineage alive: generations since the first 300 agents |
| `gene_lifespan`, `gene_repro`, `gene_mutation`, `gene_alpha`, `gene_eps` | Population means of the five genes: lifespan in ticks, energy to reproduce, mutation scale, learning rate, exploration rate |
| `q_states` | Mean number of the 240 situations an agent's Q-table has visited (inherited visits count under `--inherit copy`) |
| `policy_complexity` | Mean number of different actions an agent would choose across the situations it has visited (1 to 20) |
| `signal_entropy` | Entropy of all signals used in the year, in bits (2.0 means all four equally often) |
| `dialect_jsd` | Jensen-Shannon divergence between the two banks' signal use, in bits (0 means identical, 1 means disjoint) |
| `novelty` | Behaviour descriptors seen for the first time this year |
| `ecology_entropy` | Entropy of the population across behaviour descriptors, in bits |
| `change` | How far the mean genome has moved in ten years, in units of each gene's mutation scale |
| `archive_size` | Distinct behaviour descriptors seen since the world began (at most 2,048) |
| `energy_drift` | Total energy minus 30,000 at the year's end: rounding error only |
| `event` | Floods, droughts and fires that started during the year |
