## 7. Experiments to run next

Each experiment below is one change against the defaults, run on 16 seeds. Before you start one, write your prediction in a file next to the runs; the paper's first habit applies here more than anywhere: emergence only means something against a prediction.

**Table 5.** Six experiments for the desktop, each a single change.

| # | Question | Command (16 seeds each) | Read these columns |
|---|---|---|---|
| E1 | Does handing learning down help? | `./run_seeds.sh 16 2000 copy` and `./run_seeds.sh 16 2000 none --inherit none` (add `half` as a third) | `population`, `q_states`, `policy_complexity` |
| E2 | Does evolution tune how agents learn (the Baldwin effect [@hinton1987])? | The same two conditions as E1 | `gene_alpha`, `gene_eps`: do they drift apart between conditions? |
| E3 | Is the river a barrier to culture? | Defaults, 5,000 years | `dialect_jsd`, `crossings`, `pop_west`, `pop_east` |
| E4 | Does disturbance keep the world interesting? | `./run_seeds.sh 16 2000 calm --no-events` against the defaults | `novelty`, `ecology_entropy`, `change` |
| E5 | Starvation or crowding? | `--energy 20000`, the default 30,000, and `--energy 45000` | `population`, `gene_repro`, `gene_lifespan`, `mean_energy` |
| E6 | Does a bigger world sustain more variety? | `--size 128 --energy 53000` (the same energy per cell) | `archive_size`, `ecology_entropy`, `dialect_jsd` |

Two experiments need a one-line edit rather than an option, and the code is short enough to make it safely. To change how many fords there are, edit the `self.fords = [...]` line in `World.__init__`; to make the river a wall, give it no fords at all. Make the edit in a copy of the folder, so that the original runs keep resuming with the code they started with.

> **Caution:** A change to the code applies to every world that resumes under it. Never edit `river_world.py` under a running experiment: copy the folder, change the copy, start fresh worlds.

### 7.1 The three habits, applied

1. **Predict first.** For E3, for example: "with three fords, `dialect_jsd` stays under 0.05; with one ford it climbs above 0.2 within 2,000 years." A number you can be wrong about, and this one was, by a factor of about 100 (Section 11.3).
2. **Change one thing, run sixteen seeds.** `summarise.py runs/A runs/B` prints a Welch *t* for every column. With 16 seeds a side, |t| above about 2 is worth a closer look; below that, the difference is within what the seeds do on their own.
3. **Keep everything.** Copy a seed's `checkpoint.pkl` when something odd happens, and take a `snapshot.py` map. The interesting moment in a long run is usually found afterwards, in the log.

### 7.2 Measuring open-endedness, honestly

The log carries simple versions of the four MODES measures (change, novelty, complexity and ecology) [@dolson2019]. They are deliberately crude: each agent is summarised by a six-part behaviour descriptor (learning-rate band, exploration band, reproduction band, favourite signal, mobility band and bank), and `novelty` counts descriptors never seen before in that run. The descriptor space has 2,048 cells, so novelty is bound to fall to zero as a run fills it; that is a property of the measure, not proof that the world has stopped producing anything. Whether any of this counts as open-ended depends on the observer [@hughes2024], and here the observer is these six numbers. Richer descriptors are the obvious first improvement.
