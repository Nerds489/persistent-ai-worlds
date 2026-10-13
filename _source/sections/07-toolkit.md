## 7. The toolkit in October 2026

Every version below was read from PyPI, GitHub or the vendor's page on 10 October 2026. The reader this section has in mind runs Linux Mint 22.3 (Ubuntu 24.04 base) with Python 3.12 on a laptop with no discrete GPU, and can rent a GPU by the hour.

### 7.1 What changed since February

- **Python 3.12 is the dividing line.** Mesa, mesa-llm, Concordia and JAX 0.11 now *require* Python 3.12 or newer, while CleanRL, the Neural MMO package, Unity ML-Agents, OASIS, MetaGPT and Isaac Lab 2.3 do *not* support it. Keep a separate environment for each family.
- **Mesa 3** (November 2024) replaced schedulers with `AgentSet`, assigns `unique_id` automatically and increments the step counter itself; **Mesa 4** is in alpha and removes the old `space` module and batch runner [@mesa].
- **EvoJAX is archived**, and Brax now maintains only its training code; use MuJoCo Playground and MJX for physics.
- **AutoGen is in maintenance mode**; Microsoft points new users to the Microsoft Agent Framework (1.0 in April 2026).
- **PettingZoo's MPE environments moved** to their own Farama package, `mpe2`.
- **neat-python is maintained again** (2.0.0, March 2026).
- **Protocols consolidated.** Anthropic donated the Model Context Protocol (MCP) to the new Agentic AI Foundation under the Linux Foundation in December 2025, and Google's Agent2Agent (A2A) protocol joined it in August 2026 [@mcpaaif; @a2aaaif].

> **Warning:** On this paper's test laptop, the system's apt-installed matplotlib crashed on import because a newer NumPy 2.5 in the user's `pip --user` site shadows the NumPy it was built for. Do not mix `apt` Python packages with `pip install --user`. Use a virtual environment for every project.

### 7.2 Versions that matter

**Table 6.** Key packages, latest versions on 10 October 2026.

| Package | Version | Date | Python 3.12 | Notes |
|---|---|---|---|---|
| Mesa | 3.5.1 | Mar 2026 | Required | Agent-based modelling; 4.0 in alpha |
| mesa-llm | 0.3.2 | Apr 2026 | Required | LLM agents for Mesa; API may change |
| Gymnasium | 1.4.0 | Oct 2026 | Yes | Single-agent RL API |
| PettingZoo | 1.27.0 | Aug 2026 | Yes | Multi-agent API; MPE now in `mpe2` |
| Stable-Baselines3 | 2.9.0 | Jun 2026 | Yes | PyTorch RL algorithms |
| RLlib (Ray) | 2.59.0 | Oct 2026 | Yes | New API stack is the default |
| TorchRL | 0.14.0 | Sep 2026 | Yes | PyTorch-native RL |
| JAX | 0.11.2 | Sep 2026 | Required | Extras `cpu`, `cuda12`, `cuda13` |
| JaxMARL | 0.2.0 | Sep 2026 | Yes | 11 multi-agent environments in JAX |
| Craftax | 1.6.1 | Jun 2026 | Yes | Open-ended survival benchmark |
| Kinetix | 3.0.2 | Sep 2026 | Yes | Procedural 2D physics tasks |
| MAgent2 | 0.3.4 | May 2026 | Yes | Very large agent populations |
| Melting Pot | 2.4.1 | Sep 2026 | Yes | Social-dilemma substrates |
| evosax | 0.3.1 | Aug 2026 | Yes | Evolution strategies in JAX |
| pyribs | 0.12.0 | Jul 2026 | Yes | Quality-diversity (MAP-Elites and relatives) |
| neat-python | 2.0.0 | Mar 2026 | Yes | Neuroevolution |
| MuJoCo / MJX | 3.15.0 | Oct 2026 | Yes | Physics; MuJoCo Warp for NVIDIA GPUs |
| Genesis | 1.4.3 | Sep 2026 | Yes | GPU physics; install PyTorch first |
| Concordia | 2.4.0 | Mar 2026 | Required | Generative agent-based modelling; Ollama extra |
| LangGraph | 1.2.14 | Oct 2026 | Yes | Agent orchestration (1.0 in Oct 2025) |
| Microsoft Agent Framework | 1.21.0 | Oct 2026 | Yes | Successor to AutoGen |
| CrewAI | 1.15.27 | Oct 2026 | Yes | Role-based LLM agents |
| Ollama | 0.40.2 | Oct 2026 | n/a | Local model server |
| vLLM | 0.31.0 | Oct 2026 | Yes | Batched serving; x86 CPU wheels need AVX-512 for full features |

Source: PyPI and GitHub release pages, read 10 October 2026 [@pypi2026].

**Not on Python 3.12:** CleanRL (below 3.11), Neural MMO 2.1.2 (below 3.11, idle since August 2024), Unity ML-Agents (3.10 only), OASIS and MetaGPT (below 3.12), Isaac Lab 2.3 (3.11 only; the 3.0 early-access release supports 3.12). Use `uv venv --python 3.10` or `3.11` for these.

### 7.3 Small open models for agents

For language-model agents on modest hardware, the useful open-weight models in October 2026 are small and permissively licensed:

**Table 7.** Small open-weight models suited to local agent simulations.

| Model | Released | Licence | Size on disk (Ollama) |
|---|---|---|---|
| Qwen3.5 0.8B / 2B / 4B / 9B | Feb 2026 | Apache-2.0 | 1.2 GB / 2.7 GB / 3.3 GB / 6.6 GB |
| Gemma 4 E2B / E4B / 12B | Mar to Jun 2026 | Apache-2.0 | 4.6 GB / 6.6 GB / 7.7 GB |
| Ministral 3 3B / 8B / 14B | Oct 2025 | Apache-2.0 | 3.0 GB / 6.0 GB / 9.1 GB |
| Phi-4-mini (3.8B) | Feb 2025 | MIT | n/a |
| gpt-oss-20b (mixture of experts) | Aug 2025 | Apache-2.0 | 14 GB; "as little as 16GB memory" |
| Qwen-AgentWorld-35B-A3B | Jun 2026 | Apache-2.0 | A "language world model" that simulates agent environments |

Sources: Hugging Face and the Ollama library [@qwen35; @gemma4; @ollamalib].

### 7.4 What a laptop, a GPU and the cloud can each do

**Measured on this paper's test machine** (Intel i7-8665U, 4 cores, 16 GB RAM, no GPU): the two reference simulations in Appendix B ran 3,400 world ticks per second for two learning agents, and 3.7 simulated years per second for an evolving population of 1,200 (1,000 years in about 4.5 minutes). Simple worlds are not compute-bound on any modern computer.

**Language models are the bottleneck.** On a CPU, token generation is limited by memory bandwidth. The i7-8665U has dual-channel DDR4-2400 with a theoretical 37.5 GB/s [@intelark]; at a realistic 22 to 28 GB/s, the estimates in Table 8 follow. They are estimates, not measurements, and halve if the laptop has a single memory module.

**Table 8.** Token generation and agent throughput (estimates for the laptop; GPU figures from the llama.cpp scoreboard).

| Setup | Generation speed | One agent turn (~1,000 prompt + 150 output tokens) | Agent turns per hour |
|---|---|---|---|
| Laptop CPU, 1B model at 4-bit | ~20-30 tokens/s (est.) | ~15 s | ~240 |
| Laptop CPU, 4B model at 4-bit | ~7-12 tokens/s (est.) | ~45 s | ~80 |
| RTX 4090, 7B model at 4-bit | 186 tokens/s (measured) | well under 1 s | thousands |
| RTX 5090, 7B model at 4-bit | 290 tokens/s (measured) | well under 1 s | thousands; more with batching |

GPU figures: llama.cpp scoreboard, Llama 2 7B Q4_0 [@llamacppbench].

On the laptop that means roughly 5 to 25 language-model agents at minutes per simulated tick, which is enough for a Smallville-sized experiment if most agents act by rule and call the model only for important decisions, and if prompts share a cached prefix. Ollama serves one request at a time by default (`OLLAMA_NUM_PARALLEL=1`) [@ollamafaq].

**Renting is cheap for short experiments.** Typical on-demand prices on 10 October 2026, in US dollars per GPU-hour [@runpod; @vast; @lambda]:

| GPU | Typical price | Good for |
|---|---|---|
| RTX 4090 (24 GB) | $0.14 to $0.89 | JAX reinforcement learning; small-model agent societies |
| RTX 5090 (32 GB) | $0.38 to $1.19 | The same, faster; 27B to 35B models |
| A100 (40 or 80 GB) | $0.36 to $2.79 | Large batched model serving |
| H100 (80 GB) | $1.68 to $4.29 | Large models; world models that need datacentre GPUs |

Google Colab's free tier gives GPUs that "vary over time" with unpublished limits and sessions of at most 12 hours [@colabfaq]. For buying, NVIDIA's RTX 5090 (32 GB) launched at US$1,999, the RTX 5080 and 5070 Ti (16 GB) at US$999 and US$749 [@nvidia50].

### 7.5 Recommended stacks

**Table 9.** What to install for each hardware tier.

| Tier | Simulation | Learning | Language models |
|---|---|---|---|
| CPU-only laptop | NumPy, Mesa 3.5 | PettingZoo + SuperSuit + Stable-Baselines3; neat-python, DEAP, pyribs; JAX on CPU for prototypes | Ollama with Qwen3.5 0.8B or 2B, Ministral 3 3B or Gemma 4 E2B |
| One consumer GPU | JAX environments (JaxMARL, Craftax, Kinetix), MuJoCo Playground | `jax[cuda13]`, evosax, TorchRL or RLlib | vLLM or llama.cpp with Qwen3.5 9B or Gemma 4 12B |
| Rented GPU | As above, at scale; PufferLib for very fast C environments | Many vectorised runs in parallel | vLLM batching for hundreds of agents per tick |
| Local LLM society | mesa-llm or Concordia | Optional | Ollama or llama-server; MCP for tools, A2A between agents |

PufferLib deserves a mention: its authors report 15 million environment steps per second on one RTX 5090 in version 4.0 (2026), up from 4 million in version 3.0 [@puffer4]. JAX's headline speed-ups need stating carefully: JaxMARL is about 14 times faster than earlier tools for a single training run, and "up to 12500x" only when many runs are vectorised on one accelerator [@rutherford2023]. The first edition's install line, `pip install jax jaxlib jaxmarl`, installs the CPU-only build; GPU users need `pip install "jax[cuda13]"` (or `cuda12`) first. Appendix C lists the full install commands.
