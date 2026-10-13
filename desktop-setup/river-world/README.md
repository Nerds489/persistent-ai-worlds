# River world

Scenario A (learning agents, terrain, seasons, signals) and Scenario B (a sealed energy budget, heritable genomes,
evolution) in one world, with a river down the middle that can be crossed only at three fords. Python 3.10+ and
NumPy only. The full guide is the setup paper, *River World on the Desktop*.

## Set up

```bash
python3 -m venv ~/venvs/river && source ~/venvs/river/bin/activate && pip install -U pip numpy
cd ~/river-world && chmod +x *.py run_seeds.sh
```

## Check it works (about a minute)

```bash
python3 river_world.py --years 20 --fresh --dir runs/smoke   # energy must be conserved to < 1e-6 of the total
python3 snapshot.py runs/smoke                               # a PNG map of the world
```

## Run it

```bash
./run_seeds.sh 16 1000 main                       # 16 seeds x 1,000 years, one per physical core
./run_seeds.sh 16 1000 darwin --inherit none      # a second condition: children start with a blank Q-table
./run_seeds.sh 16 1000 main                       # run again to continue every seed
python3 summarise.py runs/main runs/darwin        # compare the two, seed by seed
```

Run the launcher inside `tmux` for long runs. Ctrl-C, `kill` or a shutdown make each world finish its year, save
and exit; the same command resumes them exactly.

| File | What it does |
|---|---|
| `river_world.py` | One world, one seed: `log.csv` (a row a simulated year) and `checkpoint.pkl` in its run folder |
| `run_seeds.sh` | Many seeds at once, then a summary. `JOBS=n` sets how many run together |
| `summarise.py` | One line per seed, mean and spread, and a Welch t between two conditions |
| `snapshot.py` | A PNG map of a checkpoint: `--colour side`, `signal` or `generation` |

Options such as `--inherit`, `--no-events`, `--energy` and `--size` are fixed when a world is created. To try a
code change, copy this folder and start fresh worlds in the copy.

Checkpoints are Python pickles, and loading a pickle can run code: only resume or map checkpoints you made
yourself, never ones downloaded from someone else.

## Licence

The code is released under the MIT License (`LICENSE`). It accompanies *River World on the Desktop* by Lachlan
Bremner, DOI [10.5281/zenodo.23337944](https://doi.org/10.5281/zenodo.23337944).
