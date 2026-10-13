## 3. Install

Everything in this section runs in a terminal on the desktop. The river world needs only Python 3.10 or newer and NumPy; the GPU stages in Section 9 have their own environments so that nothing here can break them.

### 3.1 The simulation environment

```bash
sudo apt update && sudo apt install -y python3.12-venv lm-sensors tmux
python3 -m venv ~/venvs/river && source ~/venvs/river/bin/activate
pip install -U pip numpy
python3 -c "import numpy, sys; print(sys.version.split()[0], numpy.__version__)"
```

Use the virtual environment rather than the system Python. On the laptop this paper was built on, a NumPy 2 in the user site directory shadowed the distribution's matplotlib, which was built for NumPy 1, and broke it; a venv keeps the two apart. Activate it (`source ~/venvs/river/bin/activate`) in every new terminal before running anything below.

### 3.2 The files

Copy the `river-world/` folder that comes with this paper to the desktop, for example to `~/river-world`. It holds five files and nothing else:

**Table 2.** The river world kit.

| File | What it does |
|---|---|
| `river_world.py` | The world. One process runs one seed and writes `log.csv` and `checkpoint.pkl` in its run folder |
| `run_seeds.sh` | Runs many seeds at once, one per physical core, then summarises them |
| `summarise.py` | One line per seed, the mean and spread across seeds, and a comparison between conditions |
| `snapshot.py` | Draws a checkpoint as a PNG map (Figure 1 was made with it) |
| `README.md` | The commands from this paper, in short |

```bash
cd ~/river-world && chmod +x *.py run_seeds.sh
python3 river_world.py --help
```

### 3.3 Check the graphics driver (only for Section 9)

```bash
nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv
```

This should name the RTX 3070 with 8,192 MiB. Note the driver version: Section 9 installs the JAX build that matches it.
