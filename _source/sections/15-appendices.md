## Appendix A: Corrections to the February 2026 edition

Each row gives the first edition's claim, the verdict of the October 2026 audit and the corrected statement. Twelve of the 25 audited claims were correct and are not repeated here except where precision was added. The first column is the audit's claim number; the two rows marked "Other" are errors found elsewhere in the research.

**Table A1.** Corrections to the first edition.

| Claim | First edition said | Verdict | Correct statement | Where |
|---|---|---|---|---|
| 4 | Hide-and-seek took "132.3 million episodes (31.7 billion frames)"; phases began with "random" and ended with "lock everything" | Imprecise | 132.3 million episodes was the cost of reaching phase 4 in a batch-size experiment; box surfing came after about 380 million. Phase 1 is "running and chasing", phase 6 "surf defense" [@baker2020] | 2.1 |
| 5 | Capture the Flag testers "could only win 25% of matches" | Correct, with detail | Two professional testers against a fixed pair of agents, 25% wins plus 6.3% draws [@jaderberg2019] | 2.2 |
| 7 | XLand "3.4 million unique tasks" | Correct, with detail | Per agent in the final generation, not the size of the task space [@xland2021] | 2.3 |
| 10 | Avida "populations of 10,000 organisms can process 20,000 generations per day"; complex functions evolved "through initially deleterious mutations" | Imprecise | The throughput is a 2009 desktop figure [@ofria2009]; EQU evolved in 23 of 50 populations, and deleterious stepping stones mattered in some cases (3 of 23) [@lenski2003] | 2.6 |
| 11 | "Flow-Lenia (2025)"; Lenia's 400 species showed self-replication | Imprecise | Flow-Lenia was posted in 2022 and won the ALIFE 2023 best paper; 2025 is the journal version [@plantec2022; @plantec2025]. Self-replication came with Expanded Lenia (2020) [@chan2020] | 2.7 |
| 12, 23 | JaxMARL "up to 12,500x speedup via GPU" and "12,500x faster on a single consumer GPU" | Out of date | About 14 times faster per run; up to 12,500 times only when many runs are vectorised; the hardware for the larger figure is not stated [@rutherford2023] | 7.5 |
| 12 | MAgent2 has a "C++ core" for "100s to millions" | Imprecise | "Up to 1 million on one GPU server" comes from the original MAgent paper (2017) [@zheng2017]; MAgent2's README says only "very large numbers" | 7.2 |
| 13 | Generative Agents repository has 20,600+ stars | Out of date | About 22,200 stars (October 2026) | 4.1 |
| 15 | Survival-only reward "produces the most open-ended outcomes, as demonstrated by Tierra and Polyworld" | Wrong | Tierra has no fitness function at all; PolyWorld began with an ad hoc fitness function. Neither achieved unbounded open-endedness [@ray1991; @yaeger1994] | 8.2 |
| 16 | "Polyworld demonstrated evolved signalling" | Wrong | Yaeger: "no evidence of their use of this form of communication has yet been found" [@yaeger1994] | 2.6 |
| 16 | Neural MMO "for up to 128 concurrent agents" | Imprecise | Experiments capped populations at 16 to 128 per world; version 2.0 supports 1 to 1,024 [@suarez2019; @nmmo2] | 2.5 |
| 18 | ASAL "discovered rules more open-ended than Conway's Game of Life" | Imprecise | It found rules open-ended *like* Life; Life ranked in the top 5% of 262,144 rules on the authors' metric. ASAL is by MIT, Sakana AI, OpenAI and IDSIA [@kumar2025asal] | 3, 2.7 |
| 19 | Darwin Gödel Machine rose "from 20% to 50% on SWE-bench"; introduced as "their" (Sakana AI's) system | Correct, with detail | Right numbers, measured on subsets of SWE-bench Verified; Polyglot rose from 14.2% to 30.7%. Built by UBC, the Vector Institute and Sakana AI [@zhang2025dgm] | 3.3 |
| 21 | Generative agents of 1,052 people replicated survey responses "with 85% accuracy" | Wrong | 85% is *normalised* accuracy, relative to people's own two-week consistency; the 2026 revision reports 83% to 86% [@park2024] | 4.1 |
| 21 | Park's team "raised $100M from Index Ventures" as Simile | Out of date | US$100M Series A (February 2026), then US$200M Series B at a reported US$2B valuation (July 2026) [@simileA; @simileB] | 4.1 |
| 22 | "Polarization only appears at scale, requiring 10,000+ agents" (OASIS) | Wrong | Polarisation was reproduced with 196 users; it is the herd effect that is absent at 100 agents and clear at 10,000 [@yang2024oasis] | 4.3 |
| 24 | `pip install jax jaxlib jaxmarl` for GPU training | Imprecise | That installs CPU-only JAX; use `pip install "jax[cuda13]"` or `"jax[cuda12]"` first | App. C |
| Other | Population-based evolution "sidesteps the problem entirely" (forgetting) | Wrong | Evolved learners still forget; evolution shapes the learner but does not replace replay or plasticity maintenance [@ellefsen2015] | 6.2 |
| Other | Project Sid ran "10 to 1,000+" agents | Imprecise | Analysed results stop at 500 agents; larger runs exceeded the server [@sid2024] | 4.2 |

## Appendix B: The reference simulations

Both programs need only Python 3.10 or newer and NumPy, write their state atomically so that a crash never corrupts a checkpoint, and resume automatically.

**`forest_world.py`** (Section 9). Two tabular Q-learners in a 64 × 64 seasonal forest.

```
python3 forest_world.py --ticks 400000 --fresh     # new world: 33 simulated years
python3 forest_world.py --ticks 400000             # resume and continue
```

It logs, every 10,000 ticks, energy, food eaten, deaths, mean lifetime, the number of Q-table states visited, how often the agents are near each other, and the entropy of their signals.

**`sealed_box.py`** (Section 10). An evolving population in a closed energy budget.

```
python3 sealed_box.py --years 1000 --fresh                        # 1,000 years, ~4.5 min
python3 sealed_box.py --years 300 --fresh --energy 24000 --capacity 3000   # energy-limited
```

The core of the conservation guarantee is a single assertion that runs after every tick:

```python
drift = box.total() - box.E          # nutrients + detritus + all living bodies
assert abs(drift) < 1e-6 * box.E, f"energy not conserved: drift {drift}"
```

Every flow (metabolism, feeding, decomposition, death and reproduction) moves energy between pools; none creates or destroys it. If you add a mechanic, keep the assertion: it catches accounting bugs that would otherwise show up years later as impossible population booms.

**Measured performance** on an Intel i7-8665U laptop (4 cores, 16 GB, no GPU), 10 October 2026: forest world about 3,400 ticks per second; sealed box 3.7 simulated years per second with 1,200 agents, and 8.2 with about 450.

## Appendix C: Install commands for Linux Mint 22.3 and Python 3.12

These commands were resolved against Python 3.12.3 on 10 October 2026 with `pip install --dry-run`. All seven package groups below resolved without conflicts; they were not installed. Use one virtual environment per family.

```bash
# System prerequisites
sudo apt update && sudo apt install -y python3.12-venv python3-dev build-essential cmake git curl
curl -LsSf https://astral.sh/uv/install.sh | sh          # for tools pinned to older Python

# 1. Agent-based modelling, multi-agent RL and evolution (CPU)
python3 -m venv ~/venvs/sim && source ~/venvs/sim/bin/activate && pip install -U pip
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install "mesa[rec]" mesa-llm
pip install "gymnasium[classic-control]" "pettingzoo[all]" mpe2 supersuit stable-baselines3
pip install neat-python deap "ribs[visualize]" evotorch

# 2. JAX, kept in its own environment
python3 -m venv ~/venvs/jax && source ~/venvs/jax/bin/activate && pip install -U pip
pip install -U jax                     # CPU build; on an NVIDIA GPU: pip install -U "jax[cuda13]"
pip install evosax jaxmarl craftax kinetix-env xminigrid

# 3. Local language-model agents
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen3.5:2b && ollama pull gemma4:e2b
pip install "gdm-concordia[ollama]" langgraph agent-framework openai-agents

# 4. Tools that need an older Python
uv venv --python 3.10 ~/venvs/cleanrl && source ~/venvs/cleanrl/bin/activate
git clone https://github.com/vwxyzjn/cleanrl && cd cleanrl && uv pip install -e ".[pettingzoo]"
uv venv --python 3.11 ~/venvs/oasis && source ~/venvs/oasis/bin/activate && uv pip install camel-oasis
```

Notes: `jax[cuda13]` needs NVIDIA driver 580 or newer (525 or newer for `cuda12`). Ollama serves one request at a time unless `OLLAMA_NUM_PARALLEL` is raised, and memory use scales with it. RLlib's documentation still shows a Gymnasium extra, `accept-rom-license`, that Gymnasium 1.4 no longer has; leave it out.

## Appendix D: Artificial-life simulators you can run

A verified selection, as of October 2026. The companion file `artificial-life-simulators.md` in this folder lists more than 100 further titles; those were not re-verified for this edition.

**Table D1.** Artificial-life simulators and games, with their October 2026 status.

| Name | Kind | Status (October 2026) |
|---|---|---|
| Lenia, Flow-Lenia | Continuous cellular automata | Open source; Flow-Lenia journal version 2025 [@plantec2025] |
| ALIEN | GPU particle-based artificial life (CUDA) | Last tagged release v4.12 (December 2024); development branch active October 2026 [@alien] |
| Thrive | Open-source evolution game | 1.0 in 2025; 1.6.0 on 30 August 2026, working on the multicellular stage [@thrive] |
| The Bibites | Evolving neural-network creatures | Version 0.6.3.1, March 2026; also on Steam [@bibites] |
| biosim4 | Evolving creatures with neural genomes | Moving to maintenance only [@biosim4] |
| Evochora | Open-ended evolution "physics lab" in Java | Open source (MIT), no fitness function [@evochora] |
| Avida, Avida-ED | Digital evolution, research and teaching | Avida-ED is Avida's teaching interface [@ofria2009] |
| Aevol | Bacterial genome evolution | Open source (GPL-3), Inria [@aevol] |
| Sakana Digital Ecosystems | Browser-based neural cellular automata species | April 2026; over 40 tunable parameters [@sakanaeco] |
| The Life Engine, Particle Life, Clusters | Browser-based toys | Free to try; Clusters inspired Particle Life [@ventrella] |

## Appendix E: Glossary

| Term | Meaning |
|---|---|
| Autocurriculum | A curriculum that arises because agents change the problem for each other |
| Catastrophic forgetting | New learning overwriting old knowledge in a neural network |
| Checkpoint | A saved copy of the full state of a simulation, from which it can resume |
| Generative agent | A language-model agent with memory, reflection and planning |
| Loss of plasticity | A network's gradual loss of the ability to learn anything new |
| MAP-Elites | A quality-diversity algorithm that keeps the best solution found for each kind of behaviour |
| MARL | Multi-agent reinforcement learning |
| MODES | A toolbox measuring change, novelty, complexity and ecology in evolving systems |
| Neuroevolution | Evolving neural networks' weights and structure |
| Novelty search | Search that rewards new behaviour instead of progress toward a goal |
| ODD protocol | The standard way to describe an agent-based model: overview, design concepts, details |
| Open-endedness | Producing artifacts that are both novel and learnable to an observer, indefinitely |
| PPO | Proximal policy optimisation, the most common deep RL algorithm in this paper |
| Quality-diversity | Search for a collection of solutions that are both good and different |
| Replay | Training on stored past experience alongside new experience |
| UED | Unsupervised environment design: automatically choosing or generating training environments |
| World model | A learned model that predicts how an environment will respond to actions |
