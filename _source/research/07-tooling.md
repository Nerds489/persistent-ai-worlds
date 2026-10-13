# Toolkit landscape, versions, install paths, hardware and costs (as of 10 Oct 2026)

Every version below was read from PyPI, GitHub or vendor pages on 10 Oct 2026. Search coverage was partial, so later checks fetched primary pages directly; anything still unconfirmed is marked UNVERIFIED. The paper's install lines were checked separately with pip dry-runs on Python 3.12.

## 1. What has changed since the February edition

- **These do not work on Python 3.12:**
  - CleanRL: both the PyPI release and the master `pyproject.toml` say `>=3.8,<3.11`.
  - Neural MMO: `<3.11`, and the repo has had no push since Aug 2024.
  - Unity ML-Agents Python package: `>=3.10.1, <=3.10.12` only.
  - OASIS: `<3.12`, on both PyPI and main.
  - MetaGPT: `<3.12`.
  - Isaac Lab 2.3.x from PyPI: `==3.11.*`.
- **These now require Python 3.12 or newer:** Mesa, mesa-llm, Concordia and JAX 0.11.
- **EvoJAX:** the GitHub repo is archived.
- **neat-python** is maintained again: 1.0.0 in Nov 2025, 2.0.0 on 2 Mar 2026.
- **Brax:** "Only `brax/training` is actively being maintained as of 0.13.0". Use MuJoCo Playground for environments and MJX or MuJoCo Warp for physics ([README](https://github.com/google/brax)).
- **AutoGen:** "AutoGen is now in maintenance mode… New users should start with Microsoft Agent Framework" ([README](https://github.com/microsoft/autogen)).
- **PettingZoo MPE:** "The MPE environments are no longer part of PettingZoo. They now live in their own Farama project, MPE2" ([docs](https://pettingzoo.farama.org/environments/mpe/)).
- **Mesa 3.0 (9 Nov 2024) brought these changes:**
  - Schedulers were replaced by AgentSet.
  - `unique_id` is assigned automatically.
  - `super().__init__()` became mandatory.
  - The step counter increments automatically.
  - SolaraViz now takes a model instance.
- **Mesa 4.0 (alpha) removes:** the Simulator classes, `seed`, `model.steps`, `batch_run`, `mesa.space` and `PropertyLayer`. Their replacements are `rng`, `model.time`, `Scenario`/`run_scenarios()` and `mesa.discrete_space`. Install it with `--pre` ([migration guide](https://mesa.readthedocs.io/latest/migration_guide.html)).

## 2. Version table

| Package | Latest | Date | Status | Py3.12? | Source |
|---|---|---|---|---|---|
| Mesa | 3.5.1 (4.0.0a0 pre-release) | 15 Mar 2026 | Stable; repo moved to github.com/mesa/mesa | Yes (needs ≥3.12) | [PyPI](https://pypi.org/project/mesa/) |
| mesa-llm | 0.3.2 | 26 Apr 2026 | Mesa-org extension; README warns "API… may change significantly" | Yes (≥3.12) | [GH](https://github.com/mesa/mesa-llm) |
| NetLogo | 7.0.4 (7.1.0-alpha1, 14 Aug 2026) | 1 May 2026 | Active; 7.0.0 was 11 Sep 2025 | n/a (JVM) | [GH](https://github.com/NetLogo/NetLogo/releases) |
| AgentPy | 0.1.5 | 21 Dec 2021 | Dormant (last push Feb 2025) | Declares ≥3.6; 3.12 untested, UNVERIFIED | [PyPI](https://pypi.org/project/agentpy/) |
| Agents.jl | 7.0.4 (7.0.0 on 27 Feb 2026) | 15 Sep 2026 | Active | n/a (Julia) | [GH](https://github.com/JuliaDynamics/Agents.jl/releases) |
| Gymnasium | 1.4.0 | 5 Oct 2026 | Active | Yes | [PyPI](https://pypi.org/project/gymnasium/) |
| PettingZoo | 1.27.0 | 13 Aug 2026 | Active; no `mpe` extra | Yes | [PyPI](https://pypi.org/project/pettingzoo/) |
| mpe2 | 1.1.1 | 11 Sep 2026 | Farama | Yes | [PyPI](https://pypi.org/project/mpe2/) |
| SuperSuit | 3.11.0 | 31 May 2026 | Active | Yes | [PyPI](https://pypi.org/project/supersuit/) |
| Stable-Baselines3 | 2.9.0 | 15 Jun 2026 | Active | Yes | [PyPI](https://pypi.org/project/stable-baselines3/) |
| CleanRL | PyPI 1.2.0; master 2.0.0b1 | 22 May 2023 | Repo active (last push 20 Apr 2026) | **NO** | [pyproject](https://raw.githubusercontent.com/vwxyzjn/cleanrl/master/pyproject.toml) |
| RLlib (ray) | 2.59.0 | 2 Oct 2026 | New API stack is the default (switched on in the Ray 2.40 notes) | Yes | [PyPI](https://pypi.org/project/ray/) |
| TorchRL | 0.14.0 | 10 Sep 2026 | Active | Yes | [PyPI](https://pypi.org/project/torchrl/) |
| BenchMARL | 1.5.2 | 7 Feb 2026 | Active | No Python metadata: UNVERIFIED | [PyPI](https://pypi.org/project/benchmarl/) |
| JaxMARL | 0.2.0 | 10 Sep 2026 | Active | Yes (≥3.11) | [PyPI](https://pypi.org/project/jaxmarl/) |
| MAgent2 | 0.3.4 | 23 May 2026 | Stable | Yes | [PyPI](https://pypi.org/project/magent2/) |
| Melting Pot | 2.4.1 (sdist only) | 30 Sep 2026 | Active; dmlab2d 1.0.2 ships cp312 Linux wheels | Yes (≥3.11) | [PyPI](https://pypi.org/project/dm-meltingpot/) |
| Neural MMO | 2.1.2 | 30 Aug 2024 | Idle | **NO** | [PyPI](https://pypi.org/project/nmmo/) |
| Craftax | 1.6.1 | 20 Jun 2026 | Active | Yes | [PyPI](https://pypi.org/project/craftax/) |
| Kinetix (kinetix-env) | 3.0.2 | 24 Sep 2026 | Active | Yes | [PyPI](https://pypi.org/project/kinetix-env/) |
| XLand-MiniGrid (xminigrid) | 0.9.3 | 16 Dec 2025 | Alpha; classifiers stop at 3.10 | Installs; untested, UNVERIFIED | [PyPI](https://pypi.org/project/xminigrid/) |
| neat-python | 2.0.0 | 2 Mar 2026 | Maintained again | Yes | [PyPI](https://pypi.org/project/neat-python/) |
| EvoJAX | 0.2.17 | 18 Jun 2024 | **Repo archived** | Avoid | [GH API](https://api.github.com/repos/google/evojax) |
| evosax | 0.3.1 | 17 Aug 2026 | Active | Yes | [PyPI](https://pypi.org/project/evosax/) |
| QDax | 0.5.0 | 27 May 2025 | Beta; last push 30 Oct 2025 | Yes; compatibility with JAX 0.11 UNVERIFIED | [PyPI](https://pypi.org/project/qdax/) |
| pyribs (ribs) | 0.12.0 | 22 Jul 2026 | Active | Yes | [PyPI](https://pypi.org/project/ribs/) |
| DEAP | 1.4.4 | 17 Apr 2026 | Active; pure-Python wheel | Yes | [PyPI](https://pypi.org/project/deap/) |
| EvoTorch | 0.6.1 | 14 May 2025 | Repo active (pushed 5 Oct 2026) | Yes | [PyPI](https://pypi.org/project/evotorch/) |
| MuJoCo / MJX / MuJoCo Warp | 3.15.0 | 5 Oct 2026 | Warp: "requires an NVIDIA GPU for fast simulation but supports CPU for development" | Yes | [GH](https://github.com/google-deepmind/mujoco/releases), [PyPI](https://pypi.org/project/mujoco-warp/) |
| MuJoCo Playground (playground) | 0.2.0 | 16 Mar 2026 | README recommends installing from source | Yes (≥3.11) | [PyPI](https://pypi.org/project/playground/) |
| Brax | 0.14.2 | 15 Mar 2026 | Only the training code is maintained | Yes (≥3.11) | [PyPI](https://pypi.org/project/brax/) |
| Genesis (genesis-world) | 1.4.3 | 30 Sep 2026 | Install PyTorch first | Yes (3.10-3.13) | [PyPI](https://pypi.org/project/genesis-world/) |
| Isaac Lab | PyPI 2.3.2.post1 / GitHub v3.0.0-EA | 11 Feb / 16 Sep 2026 | 3.0 is early access, built for Isaac Sim 6.1 | 2.3: **NO**; 3.0-EA: Yes | [GH API](https://api.github.com/repos/isaac-sim/IsaacLab/releases/latest) |
| Unity ML-Agents | Release 23 / mlagents 1.1.0 | 2 Sep 2025 / 5 Oct 2024 | Repo active | **NO** (3.10 only) | [PyPI](https://pypi.org/project/mlagents/) |
| CrewAI | 1.15.27 | 9 Oct 2026 | Active | Yes (<3.14) | [PyPI](https://pypi.org/pypi/crewai/1.15.27/json) |
| AutoGen (autogen-agentchat) | 0.7.5 | 30 Sep 2025 | Maintenance mode | Yes, but do not start new work on it | [PyPI](https://pypi.org/project/autogen-agentchat/) |
| Microsoft Agent Framework | 1.21.0 | 8 Oct 2026 | Preview from 1 Oct 2025; GA 1.0.0 on 2 Apr 2026 | Yes | [PyPI](https://pypi.org/project/agent-framework/) |
| LangGraph | 1.2.14 | 6 Oct 2026 | 1.0.0 released 17 Oct 2025 | Yes | [PyPI](https://pypi.org/project/langgraph/) |
| OpenAI Agents SDK | 0.23.1 | 2 Oct 2026 | Still pre-1.0 | Yes | [PyPI](https://pypi.org/project/openai-agents/) |
| Google ADK | 2.11.0 | 2 Oct 2026 | 2.0.0 released 19 May 2026 | Yes | [PyPI](https://pypi.org/project/google-adk/) |
| Concordia (gdm-concordia) | 2.4.0 | 6 Mar 2026 | Extras include `ollama` and `vllm` | Yes (≥3.12) | [PyPI](https://pypi.org/project/gdm-concordia/) |
| CAMEL (camel-ai) | 0.2.90 | 22 Mar 2026 | 0.2.91 alphas since | Yes | [PyPI](https://pypi.org/project/camel-ai/) |
| OASIS (camel-oasis) | 0.2.5 | 4 Dec 2025 | Repo active | **NO** | [pyproject](https://raw.githubusercontent.com/camel-ai/oasis/main/pyproject.toml) |
| AgentScope | 2.0.9 | 28 Sep 2026 | Active | Yes (≥3.11) | [PyPI](https://pypi.org/project/agentscope/) |
| MetaGPT | 0.8.2 | 9 Mar 2025 | Last push Jan 2026 | **NO** | [PyPI](https://pypi.org/project/metagpt/) |
| Ollama | v0.40.2 | 8 Oct 2026 | Python client 0.6.3 (29 Sep 2026) | n/a | [GH API](https://api.github.com/repos/ollama/ollama/releases/latest) |
| llama.cpp | b11540 | 10 Oct 2026 | Rolling builds; ubuntu-x64 CPU and Vulkan binaries | n/a | [GH](https://github.com/ggml-org/llama.cpp/releases) |
| llama-cpp-python | 0.3.36 | 1 Oct 2026 | Active | Yes | [PyPI](https://pypi.org/project/llama-cpp-python/) |
| vLLM | 0.31.0 | 5 Oct 2026 | x86 CPU wheels since 0.17.0; AVX-512 recommended, AVX2 has "limited features" | Yes | [PyPI](https://pypi.org/project/vllm/), [CPU docs](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html) |
| JAX | 0.11.2 | 17 Sep 2026 | Extras `cpu`, `cuda12`, `cuda13` | Yes (needs ≥3.12) | [PyPI](https://pypi.org/project/jax/) |
| PyTorch | 2.14.1 | 30 Sep 2026 | `+cpu` cp312 wheel confirmed on download.pytorch.org | Yes | [PyPI](https://pypi.org/project/torch/) |

**Protocols**
- **MCP:** Anthropic donated it to the Agentic AI Foundation, a directed fund under the Linux Foundation, on 9 Dec 2025.
  - Co-founders: Anthropic, Block and OpenAI.
  - Founding projects: MCP, goose and AGENTS.md ([MCP blog](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/)).
  - The current spec is `2026-07-28` ([spec](https://modelcontextprotocol.io/specification/latest)).
- **A2A:**
  - It became a Linux Foundation project on 23 Jun 2025 (secondary coverage).
  - v1.0 shipped in Mar 2026.
  - It joined AAIF "as a hosted project" on 17 Aug 2026 ([AAIF](https://aaif.io/blog/a2a-joins-aaif)).

**Small open-weight models.** Release dates are Hugging Face creation dates, and licences are from the HF API.

| Model | Date | Licence | Ollama tag (download size) |
|---|---|---|---|
| Qwen3.5 0.8B / 2B / 4B / 9B (multimodal) | 26-28 Feb 2026 | Apache-2.0 | `qwen3.5:0.8b` 1.2-1.3 GB, `:2b` 2.7-3.1 GB, `:4b` 3.3-4.0 GB, `:9b` 6.6-7.6 GB |
| Gemma 4 E2B / E4B (12B added 3 Jun 2026) | 31 Mar 2026 (Google) | Apache-2.0, not gated (Gemma 3 was gated under its own licence) | `gemma4:e2b` 4.6-7.5 GB, `:e4b` 6.6-9.5 GB, `:12b` 7.7-8.0 GB |
| Ministral 3 3B / 8B / 14B ("2512") | 31 Oct 2025 | Apache-2.0 | `ministral-3:3b` 3.0 GB, `:8b` 6.0 GB, `:14b` 9.1 GB |
| Phi-4-mini-instruct (3.8B) | 19 Feb 2025 | MIT | tag UNVERIFIED |
| Llama 3.2 1B / 3B | 18 Sep 2024 | Llama 3.2 licence, gated; no newer small Llama exists | tag UNVERIFIED |
| gpt-oss-20b (MoE, 20.9B) | 4 Aug 2025 | Apache-2.0 | `gpt-oss:20b` 14 GB; Ollama says it runs in "as little as 16GB memory" |
| Qwen3.8-27B dense / Qwen3.6-35B-A3B | 5 Aug / 15 Apr 2026 | Apache-2.0 | For a 24-32 GB GPU |
| Qwen-AgentWorld-35B-A3B | 22 Jun 2026 | Apache-2.0 | A "language world model" that simulates agent environments; directly relevant to the paper |

Sources: [Qwen HF](https://huggingface.co/api/models?author=Qwen&sort=createdAt&direction=-1&limit=60), [Gemma releases](https://ai.google.dev/gemma/docs/releases), [Ollama library](https://ollama.com/library/qwen3.5).

## 3. Recommended stacks

**(a) CPU-only laptop (i7-8665U, 16 GB)**
- **ABM:** Mesa 3.5.1, with mesa-llm or Concordia for LLM agents.
- **MARL:** PettingZoo/MPE2 with SuperSuit and SB3.
- **Evolution:** neat-python, DEAP, pyribs and EvoTorch.
- **Physics:** MuJoCo on CPU.
- **JAX:** the CPU wheel is officially supported on Linux x86_64 ([JAX docs](https://docs.jax.dev/en/latest/installation.html)). It is fine for prototyping JaxMARL, Craftax and evosax at small batch sizes. The headline speed-ups are GPU results: "around 14 times faster" and "up to 12500x when multiple training runs are vectorized" ([JaxMARL abstract](https://arxiv.org/abs/2311.10090)).
- **LLMs:** Ollama with `qwen3.5:0.8b`/`:2b`, `ministral-3:3b` or `gemma4:e2b`.
- **Avoid on this machine:**
  - gpt-oss-20b: 14 GB in 16 GB of RAM.
  - vLLM-CPU: AVX2 only.
  - Isaac Lab.

**(b) Single consumer GPU**
- **JAX stack:** `jax[cuda13]` with JaxMARL, Craftax, Kinetix and XLand-MiniGrid, plus evosax or QDax.
- **Physics/RL:** MuJoCo Playground with Brax's training code, TorchRL/BenchMARL or RLlib, and Genesis.
- **LLMs:** vLLM or llama.cpp serving Qwen3.5-9B or Gemma 4 12B. Move to Qwen3.8-27B or Qwen3.6-35B-A3B on 24-32 GB cards.
- **Isaac Sim minimum:** GeForce RTX 4080, 16 GB VRAM and 32 GB RAM ([requirements](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html)).

**(c) Rented cloud GPU**
- An RTX 4090 or 5090 at $0.14-0.69/h covers JAX RL and small-model LLM societies.
- Use an A100 or H100 for large batched vLLM serving.
- For Isaac Lab, rent an RTX-class card (L40S, 4090, 5090). "GPUs without RT Cores (A100, H100) are not supported."
- For `jax[cuda13]` the host driver must be 580 or newer (525 or newer for cuda12).

**(d) Local LLM-agent societies**
- **Serving:** Ollama or llama-server.
- **Simulation:** mesa-llm (supports Ollama) or Concordia (`[ollama]` extra).
- **Orchestration:** LangGraph 1.x, Microsoft Agent Framework or the OpenAI Agents SDK.
- **Interoperability:** MCP for tools, A2A between agents.
- **Concurrency:** `OLLAMA_NUM_PARALLEL` defaults to 1, and "Required RAM will scale by `OLLAMA_NUM_PARALLEL` * `OLLAMA_CONTEXT_LENGTH`" ([FAQ](https://docs.ollama.com/faq)).
- For OASIS and MetaGPT, use a separate Python 3.11 venv.

## 4. Install commands for Mint 22.3 / Python 3.12 (not executed)

```bash
sudo apt update && sudo apt install -y python3.12-venv python3-dev build-essential cmake git curl libssl-dev
curl -LsSf https://astral.sh/uv/install.sh | sh           # for the 3.10/3.11-only tools

# (a) PyTorch/ABM/evolution venv (CPU)
python3 -m venv ~/venvs/sim && source ~/venvs/sim/bin/activate && pip install -U pip
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install "mesa[rec]" mesa-llm
pip install "gymnasium[classic-control,box2d,mujoco]" "pettingzoo[all]" mpe2 supersuit stable-baselines3 magent2 dm-meltingpot
pip install neat-python deap "ribs[visualize]" evotorch

# JAX venv, kept separate from torch (my advice, to avoid CUDA wheel clashes)
python3 -m venv ~/venvs/jax && source ~/venvs/jax/bin/activate
pip install -U jax                                   # CPU; GPU: pip install -U "jax[cuda13]"  (or "jax[cuda12]")
pip install evosax jaxmarl craftax kinetix-env xminigrid
pip install brax playground mujoco-mjx qdax          # (b)/(c) GPU boxes

# (b)/(c) torch-side GPU tools
pip install "ray[rllib]" torch torchrl benchmarl
pip install genesis-world                            # after torch
pip install vllm

# Tools pinned to older Python
uv venv --python 3.10 ~/venvs/cleanrl && source ~/venvs/cleanrl/bin/activate
git clone https://github.com/vwxyzjn/cleanrl && cd cleanrl && uv pip install -e ".[pettingzoo]"
uv venv --python 3.10.12 ~/venvs/mla && source ~/venvs/mla/bin/activate && uv pip install mlagents==1.1.0
uv venv --python 3.11 ~/venvs/oasis && source ~/venvs/oasis/bin/activate && uv pip install camel-oasis

# (d) local LLM agents
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen3.5:2b && ollama pull gemma4:e2b && ollama pull ministral-3:3b
sudo systemctl edit ollama.service      # [Service] Environment="OLLAMA_NUM_PARALLEL=4"
sudo systemctl daemon-reload && sudo systemctl restart ollama
pip install mesa-llm "gdm-concordia[ollama]" langgraph agent-framework openai-agents
git clone https://github.com/ggml-org/llama.cpp && cd llama.cpp && cmake -B build && cmake --build build --config Release -j 8
```

Pitfalls I checked:
- **`pettingzoo[all]` works on 3.12.** cp312 Linux wheels exist for Box2D 2.3.10, multi-agent-ale-py 0.1.12 and open_spiel ≥1.6.15, so nothing needs compiling.
- **RLlib's docs still show a dropped extra.** They use `gymnasium[atari,accept-rom-license,mujoco]`, but Gymnasium 1.4.0 has no `accept-rom-license` extra, so drop it.
- **Isaac Lab:** 2.3.x needs Python 3.11. 3.0-EA says "Start from a fresh Python 3.12 environment". Follow the official guide; I have not verified its commands.
- **PyTorch on GPU:** check pytorch.org for the right CUDA wheel. The page is script-rendered, so the variants are UNVERIFIED.

## 5. Cost and speed

**Measured GPU throughput** (llama.cpp scoreboard, Llama 2 7B Q4_0, llama-bench; [#15013](https://github.com/ggml-org/llama.cpp/discussions/15013)):

| GPU | Prompt processing, pp512 (tok/s) | Generation, tg128 (tok/s) | With flash attention (pp / tg) |
|---|---|---|---|
| RTX 5090 | 14,073 | 290 | 14,970 / 300 |
| RTX 4090 | 11,993 | 186 | 14,771 / 189 |
| RTX 3090 | 5,175 | 158 | not given |

**i7-8665U throughput (ESTIMATE).** Intel lists the chip as 4 cores / 8 threads, 15 W, dual-channel DDR4-2400, 37.5 GB/s and AVX2 with no AVX-512 ([ARK](https://www.intel.com/content/www/us/en/products/sku/193563/intel-core-i78665u-processor-8m-cache-up-to-4-80-ghz/specifications.html)). On CPU, "the most important factor is memory bandwidth" ([Gaessler](https://johannesgaessler.github.io/llamacpp_performance)). Assuming about 22-28 GB/s is actually achieved:

| Model at 4-bit | Generation speed (ESTIMATE) |
|---|---|
| 1B | about 20-30 tok/s |
| 3-4B | about 7-12 tok/s |
| 7B | about 5-7 tok/s (roughly 25-35 times slower than a 4090) |
| 9B | about 3-5 tok/s |

Two cautions apply. A single-DIMM configuration halves these figures. Sustained loads will throttle at 15 W. Measure with `llama-bench`. A 4B model on a 4090 or 5090 should generate about 300 or 450 tok/s (ESTIMATE, scaled from the 7B results).

**How many LLM agents (ESTIMATE).** Assume each agent turn is about 1,000 prompt tokens plus 150 output tokens.

| Setup | Time per agent turn | Turns per hour |
|---|---|---|
| Laptop, 1B model | about 15 s | about 240 |
| Laptop, 4B model | about 45 s | about 80 |
| RTX 4090, 4B model, one request at a time | about 0.6 s | about 6,000 |

- **Laptop:** realistically 5-25 LLM agents, at minutes per simulated tick. A hybrid design helps: rule-based agents with occasional LLM calls and a shared, cached prompt prefix.
- **GPU:** batched serving with vLLM pushes this into hundreds of agents per tick. The batching multiplier is an ESTIMATE, not measured here.

**Cloud prices** (USD per GPU-hour). Vast.ai figures are a live snapshot of the cheapest rentable single-GPU offers on 10 Oct 2026 ([API](https://console.vast.ai/api/v0/bundles/)).

| GPU | [RunPod](https://www.runpod.io/pricing) Community / Secure (page updated 27 Sep 2026) | [Lambda](https://lambda.ai/pricing) (undated) | Vast.ai (offers sampled) |
|---|---|---|---|
| RTX 3090 | 0.22 / 0.50 | n/a | n/a |
| RTX 4090 | 0.34 / 0.74 (the GPU page says Secure 0.89) | n/a | 0.14-0.43 (30) |
| RTX 5090 | 0.69 / 0.99 (the visible table shows 1.19) | n/a | 0.38-0.54 (30) |
| L40S | 0.79 / 1.09 | n/a | n/a |
| A100 SXM | 1.39 / 1.59 (visible table 1.79) | 1x 40 GB 1.99; 8x 80 GB 2.79 | 0.36-2.00 (25, mostly 40 GB) |
| H100 PCIe / SXM | 1.99 / 2.89; 2.69 / 3.49 (visible table 3.99) | 3.29; SXM 4.29 (1x), 3.99 (8x) | SXM 1.68-6.10 (6) |
| H200 / B200 | 3.59 / 4.59; 5.98 / 6.79 | B200 6.99 | n/a |

The RunPod page contradicts itself, and the Lambda page's tab labels were ambiguous. Check both in their consoles.

**Free tiers**
- **Colab:** GPU types "vary over time". Resources "are not guaranteed", and the limits are unpublished. Notebooks run "at most 12 hours" ([FAQ](https://research.google.com/colaboratory/faq.html)).
- **Kaggle:** UNVERIFIED, because the docs did not render. It was historically about 30 GPU hours a week on a P100 or 2×T4, but that is unconfirmed.

**Consumer hardware**
- **RTX 50 series** ([NVIDIA launch release](https://nvidianews.nvidia.com/news/nvidia-blackwell-geforce-rtx-50-series-opens-new-world-of-ai-computer-graphics), [compare page](https://www.nvidia.com/en-us/geforce/graphics-cards/compare/)):

  | Card | Memory | Launch MSRP |
  |---|---|---|
  | RTX 5090 | 32 GB GDDR7 | $1,999 |
  | RTX 5080 | 16 GB | $999 |
  | RTX 5070 Ti | 16 GB | $749 |
  | RTX 5070 | 12 GB | $549 |

- No 50-series Super cards are listed as of 10 Oct 2026.
- **Apple silicon:**
  - Mac mini: M6 with up to 32 GB, or M5 Pro with up to 64 GB.
  - Mac Studio: M5 Max or M5 Ultra, up to 512 GB. The 512 GB option is "coming late October".

## 6. Still UNVERIFIED

- Street prices for the 50 series and used RTX 4090s (price trackers returned HTTP 429, and NVIDIA's product pages show placeholder prices).
- Apple prices.
- Kaggle quotas.
- Colab's free GPU model.
- Which CUDA wheel variants PyTorch 2.14 ships.
- QDax compatibility with JAX 0.11.
- XLand-MiniGrid, AgentPy and BenchMARL on Python 3.12.
- Ollama tags for Phi-4-mini and Llama 3.2.
- Isaac Lab install commands.
- All throughput and agent-count estimates.