## 4. First run: four checks

Before committing sixteen cores to a week, spend ten minutes proving that the world works on this machine. Each check has a pass condition you can see.

### 4.1 Smoke test and speed

```bash
cd ~/river-world && source ~/venvs/river/bin/activate
time python3 river_world.py --years 20 --fresh --dir runs/smoke
```

It prints one line, for example:

```text
runs/smoke: year 20  population 800 (west 393, east 407)  max generation 21  (0.99 years/s)  energy conserved to 9.1e-10
```

**Pass:** the run finishes, both banks are populated, and `energy conserved to` is below 10⁻⁶ of the 30,000 total. On the laptop this paper was built on, one process ran 0.99 simulated years a second. Write down your own figure; Section 5 uses it.

### 4.2 Energy is conserved, every tick

There is nothing to do: the check is built in. After every tick the world adds up the nutrients, the detritus, the river's load and every body, and stops with `energy not conserved` if the total has drifted by more than one part in a million. A run that finishes has passed 400 checks a simulated year. The column `energy_drift` in `log.csv` records the drift at each year's end.

### 4.3 Stop, resume and get the same world

```bash
python3 river_world.py --years 6 --fresh --seed 5 --dir runs/straight
python3 river_world.py --years 20 --fresh --seed 5 --dir runs/stopped &
sleep 4; kill -INT %1; wait          # the same as pressing Ctrl-C
python3 river_world.py --years 6 --dir runs/stopped      # carries on from where it stopped
head -n 7 runs/straight/log.csv | cmp - <(head -n 7 runs/stopped/log.csv) && echo identical
```

Ctrl-C (or `kill`, or a shutdown) makes the world finish its current year, save, and exit. A checkpoint holds the whole world, including the random number generator, so a resumed run follows exactly the path an uninterrupted one would have. **Pass:** `identical`. If the machine loses power instead, the next start trims any log rows written after the last checkpoint (every 10 years by default; `--save-every 1` for every year) and carries on from there.

### 4.4 Look at it

```bash
python3 snapshot.py runs/smoke                     # agents coloured by bank
python3 snapshot.py runs/smoke --colour signal     # by each agent's favourite signal
xdg-open runs/smoke/map-year-20-side.png
```

**Pass:** a map like Figure 1: green land, a blue river down the middle, three tan fords, and agents on both banks.
