## 5. Running sixteen seeds

### 5.1 The launcher

```bash
./run_seeds.sh 16 1000 main                          # 16 seeds x 1,000 years into runs/main/
./run_seeds.sh 16 1000 darwin --inherit none         # a second condition, its own folder
./run_seeds.sh 16 1000 main                          # again: every seed carries on another 1,000 years
```

The arguments are the number of seeds, the years to run, a name for the condition, and any `river_world.py` options. The launcher runs one process per physical core (16 on the 5950X), keeps NumPy single-threaded inside each, lowers their priority with `nice` so the desktop stays usable, and appends each seed's output to `runs/<name>/seed-N.out`. When every seed has finished it prints the summary from Section 6. Running it again resumes every seed; options such as `--inherit` only take effect when a seed's world is first created, and the world says so if you pass a different one later.

### 5.2 How long it takes

**Table 3.** Throughput, measured on the laptop and estimated for the desktop.

| | Laptop (i7-8665U, measured) | Desktop (5950X, estimate) |
|---|---|---|
| One process, about 800 agents | 0.99 years/s | about 1.4 years/s |
| All cores busy | 0.32 years/s per process, 8 processes on 4 cores | about 1.1 years/s per process, 16 processes |
| 16 seeds × 1,000 years | about 1.7 hours (8 at a time) | about 15 minutes (all 16 at once) |
| 16 seeds for a week | | about 700,000 simulated years each |

The desktop column assumes each 5950X core is about 1.4 times as fast as one of the laptop's on this single-threaded NumPy work, and that sixteen processes on sixteen cores lose about a fifth of that to shared memory bandwidth and lower all-core clocks. Treat it as a guess until Section 4.1 has given you the real one-process figure; the all-cores figure is the one to measure next, by running `./run_seeds.sh 16 20 speedtest` and reading the `years/s` on each line. Section 11.1 did both on this desktop: 1.095 years/s per process with 16 processes, 16 seeds × 1,000 years in 15.2 minutes, and about 662,000 simulated years a seed in a week (Table 8).

Population sets the pace: the work per tick grows with the number of agents. More `--energy` means more agents, more than proportionally: 2.25 times the energy gave 3.5 times the population (Section 11.5), and the speed falls as the population rises.

### 5.3 Heat and power

A week of sixteen busy cores is a sustained load the 5950X will hold at its power limit. In the first hour:

```bash
watch -n 5 "sensors | grep -E 'Tctl|Tccd'"
```

Under 85 °C is comfortable; the chip throttles itself at 90 °C, which slows the runs but harms nothing. In Section 11 it never passed 53 °C, even at 64 processes. If it runs hot, use `JOBS=12 ./run_seeds.sh ...` to leave four cores idle. The runs do not care about the GPU, so it can be used for Section 9 at the same time.

### 5.4 Surviving the terminal

Run the launcher inside `tmux` so that closing the terminal or logging out does not stop it:

```bash
tmux new -s river            # start a session, then run ./run_seeds.sh inside it
# detach with Ctrl-b then d; reattach later with: tmux attach -t river
```

A reboot stops the runs cleanly (each one saves before it exits). Afterwards, run the same `./run_seeds.sh` line again and every seed resumes. Keep the kit and its `runs/` folder in your home directory, never under `/tmp`, which is emptied at every boot.

### 5.5 Disk

Each seed keeps one checkpoint of about 39 MB, overwritten in place (almost all of it is the 2,000 agent slots' Q-tables), and a log that grows by about 140 bytes a simulated year. Sixteen seeds take about 650 MB whatever the run length, plus their logs. To keep a snapshot of a world at some moment, copy its `checkpoint.pkl` somewhere else; it compresses to about a tenth with `gzip`. Checkpoints are Python pickles, and opening a pickle can run code, so only load checkpoints you made yourself.
