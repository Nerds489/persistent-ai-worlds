Verified from primary sources, with one limit: search coverage was partial, and later checks fetched known URLs only. Where the 2026 section says "none found", that is weaker evidence than a full search would give.

## Top findings for the paper

1. **Hide-and-seek: the old phase names are wrong and the headline number is misattributed.** The paper names the six phases "(1) Running and Chasing, (2) Fort Building, (3) Ramp Use, (4) Ramp Defense, (5) Box Surfing, (6) Surf Defense" (Fig. 3 caption, p. 6). The 132.3M-episode figure is what the default model needed to reach stage 4 only (p. 7). [arXiv 1909.07528](https://arxiv.org/abs/1909.07528)
2. **The autocurriculum only appeared at scale.** The default run used a batch of 64,000 with 1.6M parameters. Batch sizes of 16,000 and 8,000 "never converged" (p. 7).
3. **Capture the Flag (FTW, "For The Win"):** "We train a population of 30 different agents together" using population-based training, and the agents evolve their own internal rewards (pp. 3-5).
4. **AlphaStar and OpenAI Five: the claims hold, with caveats.** AlphaStar's 99.8% claim is confirmed. OpenAI Five's 99.4% public win rate counts 3,140 games that human players abandoned among its 7,215 wins (p. 8, fn. 9).
5. **XLand's 3.4M figure is tasks each agent experienced, not the size of the task space.** AdA's XLand 2.0 has "over 10^40 possible tasks".
6. **The environment-design line runs:** PAIRED, PLR, ACCEL, MAESTRO (the first multi-agent version), SFL, OMNI-EPIC and Kinetix. SFL (NeurIPS 2024) shows that practical "regret" estimates mostly just track success rate.
7. **Neural MMO grew from 128 to 1,024+ agents** and now lives inside PufferLib (version 3.0, rewritten in C).
8. **JAX speedups need their conditions stated.** JaxMARL is about 14x for a single training run, and reaches "up to 12500x" only when many runs are vectorised.
9. **Emergent social structure is now studied in three ways:** in animal-behaviour terms (dominance hierarchies, tolerated theft), at very large scale (Lux, up to 1,000 agents per team), and in LLM populations (Science Advances 2025).
10. **Self-play has moved into LLM reasoning (SPIRAL, ICLR 2026; Absolute Zero) and driving (GIGAFLOW, ICML 2025: 1.6 billion km, no human data).**

## Timeline

| Date | System | Org / lead | Result | Venue | Source |
|---|---|---|---|---|---|
| Jul 2018 / May 2019 | FTW (Quake III CTF) | DeepMind | Population of 30; human-level | Science 364(6443):859 | https://arxiv.org/abs/1807.01281 |
| Jan 2019 | POET | Wang, Lehman, Clune, Stanley | Co-evolves environments and solutions | arXiv; GECCO 2019 | https://arxiv.org/abs/1901.01753 |
| 2 Mar 2019 | Neural MMO 1.0 | Suarez et al. (OpenAI) | 16-128 agents per world, 100 worlds | arXiv | https://arxiv.org/abs/1903.00784 |
| 13 Apr 2019 | OpenAI Five | OpenAI | Beat OG 2-0; 99.4% of 7,257 public games | arXiv 1912.06680 | https://arxiv.org/abs/1912.06680 |
| 17 Sep 2019 | Hide-and-seek | OpenAI | Six emergent phases, tool use | ICLR 2020 | https://arxiv.org/abs/1909.07528 |
| 30 Oct 2019 | AlphaStar | DeepMind | Grandmaster, all 3 races, >99.8% | Nature 575:350-354 | https://www.nature.com/articles/s41586-019-1724-z |
| Mar 2020 | Enhanced POET | Wang et al. | Open-ended challenge invention | ICML 2020, PMLR 119:9940-9951 | https://proceedings.mlr.press/v119/wang20l.html |
| Dec 2020 | PAIRED | Dennis et al. | Regret-based environment design | NeurIPS 2020 | https://proceedings.neurips.cc/paper/2020/hash/985e9a46e10005356bbaf194249f6856-Abstract.html |
| 2021 | PLR | Jiang et al. | Replays levels by learning potential | ICML 2021 | https://proceedings.mlr.press/v139/jiang21b.html |
| 27 Jul 2021 | XLand | DeepMind | 3.4M tasks per final-generation agent | arXiv 2107.12808 | https://deepmind.google/discover/blog/generally-capable-agents-emerge-from-open-ended-play/ |
| 2022 | ACCEL | Parker-Holder et al. | Regret plus level editing | ICML 2022 | https://proceedings.mlr.press/v162/parker-holder22a.html |
| Nov 2022 | Melting Pot 2.0 | DeepMind | >50 substrates, >256 scenarios | Tech report | https://arxiv.org/abs/2211.13746 |
| Jan 2023 | Lux | Chen et al. | Up to 1,000 agents per team | NeurIPS 2022 DRL workshop | https://arxiv.org/abs/2301.01609 |
| Jan 2023 | AdA / XLand 2.0 | DeepMind | Human-timescale adaptation | ICML 2023 | https://proceedings.mlr.press/v202/bauer23a.html |
| Mar 2023 | MAESTRO | Samvelyan et al. | First multi-agent environment design | ICLR 2023 | https://arxiv.org/abs/2303.03376 |
| Jul 2023 | Resource exchange / tolerated theft | Garbus, Pollack | Emergent exchange protocol | arXiv | https://arxiv.org/abs/2307.01862 |
| Nov 2023 | Neural MMO 2.0 | Suarez et al. | 128 agents standard, 1-1024 supported | NeurIPS 2023 D&B | https://proceedings.neurips.cc/paper_files/paper/2023/hash/9ca22870ae0ba55ee50ce3e2d269e5de-Abstract-Datasets_and_Benchmarks.html |
| Nov 2023 | JaxMARL | Rutherford et al. | ~14x; up to 12,500x vectorised | NeurIPS 2024 D&B | https://arxiv.org/abs/2311.10090 |
| Jan 2024 | Dominance hierarchies | Rachum et al. | Hierarchies passed to new populations | arXiv | https://arxiv.org/abs/2401.12258 |
| Feb 2024 | Craftax | Matthews et al. | 1B steps in under 1 h on one GPU | ICML 2024 | https://proceedings.mlr.press/v235/matthews24a.html |
| Aug 2024 | SFL | Rutherford et al. | Sampling by learnability beats regret estimates | NeurIPS 2024 | https://arxiv.org/abs/2408.15099 |
| Oct 2024 | Kinetix | Matthews, Beukman et al. | Tens of millions of physics tasks | ICLR 2025 oral | https://arxiv.org/abs/2410.23208 |
| 2024 | Melting Pot Contest report | Trivedi et al. | 600+ participants, 100+ teams | NeurIPS 2024 D&B | https://neurips.cc/virtual/2024/poster/97476 |
| Feb 2025 | GIGAFLOW | Cusumano-Towner et al. | 1.6B km of self-play driving | ICML 2025 | https://proceedings.mlr.press/v267/cusumano-towner25a.html |
| Mar 2025 | OvercookedV2 | Gessler et al. | Redesigned zero-shot coordination benchmark | ICLR 2025 | https://iclr.cc/virtual/2025/poster/28745 |
| May 2025 | Absolute Zero | Zhao et al. | Self-proposed tasks, no external data | arXiv (venue UNVERIFIED) | https://arxiv.org/abs/2505.03335 |
| Jun 2025 | SPIRAL | Liu et al. | Zero-sum self-play improves LLM reasoning | ICLR 2026 | https://arxiv.org/abs/2506.24119 |
| 13 Nov 2025 | SIMA 2 | DeepMind | Learns through self-directed play; acts in Genie 3 worlds | Blog | https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/ |
| 21 Aug 2026 | EVE Online partnership | Google DeepMind + Fenris Creations | Multi-agent MMO research announced | Blog | https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/ |

## Key numbers

**Hide-and-seek** (Baker et al., ICLR 2020, PDF pp. 2-7)

| # | Paper's name | What happens | Episode count in the paper |
|---|---|---|---|
| 1 | Running and Chasing | Seekers chase, hiders "crudely run away" | From the start |
| 2 | Fort Building | Hiders move and lock boxes into shelters | "approximately 25 million" |
| 3 | Ramp Use | Seekers use ramps to get over walls | "another 75 million" later (about 100M cumulative; my arithmetic) |
| 4 | Ramp Defense | Hiders push ramps to the edge and lock them | "10 million episodes later" (about 110M; my arithmetic) |
| 5 | Box Surfing | Seekers ride a box from a locked ramp | "After 380 million total episodes" |
| 6 | Surf Defense | Hiders "lock all of the boxes in place before building their shelter" | Not stated; the Fig. 1 axis ends at 500M |

- **The 132.3M figure:** the default model "requires 132.3 million episodes (31.7 billion frames) over 34 hours of training to reach stage 4", i.e. ramp defence. As a check, 132.3M × 240-step episodes ≈ 31.75B, so "frames" means timesteps.
- **Why it differs from the phase table:** the paper's prose gives an approximate ~110M to ramp defence for the Fig. 1 runs (mean of 3 seeds). The 132.3M comes from a separate batch-size experiment (Fig. 4).
- **Setup:** 1-3 hiders, 1-3 seekers, 3-9 boxes, 2 ramps. Episodes are 240 steps, the first 40% a preparation phase. Teams of 2 and 3 hiders lock 25% and 36% more boxes than a single hider.

**Other systems**

- **FTW (Capture the Flag):**
  - Up to about 450K training games (Fig. 2b axis).
  - Tagging accuracy was 80% against humans' 48%, and reaction time 258 ms against 559 ms.
  - DeepMind's blog reports a separate study: strong humans won 21% against agents slowed to human reaction times. Keep that apart from the 25% result.
- **OpenAI Five:**
  - One training run, 30 Jun 2018 to 22 Apr 2019, using 770±50 PFlops/s·days.
  - About 159M parameters.
  - Batch up to 2,949,120 timesteps on up to 1,536 GPUs.
  - Public "Arena", 18-21 Apr 2019: 3,193 teams, 7,257 games, 42 losses.
- **AdA:** largest model 265M Transformer-XL / 533M total parameters, evaluated on 1,000 held-out test tasks ([ar5iv](https://ar5iv.labs.arxiv.org/html/2301.07608)).
- **Enhanced POET:** Appendix A.6, Fig. 6 shows "the phylogenetic tree of the first 100 environments of a POET run". The authors say it resembles natural trees but "is much smaller" ([PDF](https://arxiv.org/pdf/2003.08536) pp. 18-19).
- **Neural MMO:**
  - **1.0:** "up to 100 million agent trajectories (lifetimes) on 100 cores in 1 week".
  - **2.0:** "three-fold improved performance".
  - **NeurIPS 2023 competition:** 200+ participants and submissions. The winner scored 4x the baseline "within 8 hours of training on a single 4090 GPU", and everything was released under MIT ([arXiv 2508.12524](https://arxiv.org/abs/2508.12524), Aug 2025).
  - **3.0 ([PufferAI](https://puffer.ai/blog/nmmo3/)):** written in C. The demo map has 1,024 agents and 2,048 enemies. It claims "millions of steps per second per cpu core", and a baseline of about 107B steps in under 3 days on one RTX 4090 (self-reported).
  - **3.0 release date:** the post is undated. The code has been in PufferLib since at least 7 Dec 2024.
  - **Earlier challenges:** participation figures for the 2022 IJCAI and NeurIPS challenges are UNVERIFIED.
- **Overcooked:**
  - Carroll et al. (NeurIPS 2019) found that agents trained by self-play coordinate poorly with humans.
  - OvercookedV2 attributes the original benchmark's zero-shot coordination failures to poor state coverage. It is now part of JaxMARL.
  - The [Overcooked Generalisation Challenge](https://arxiv.org/abs/2406.17949v3) finds that current curriculum-generation methods "struggle". Its TMLR 2025 venue is UNVERIFIED.
- **JAX ecosystem:**
  - **JaxMARL:** now 11 environments, including SMAX, JaxNav and JaxRobotarium.
  - **PureJaxRL:** the blog headline says "over 4000x". The README's measured claims are smaller: ">1000x" faster with many agents in parallel, and 2,048 PPO agents trained in half the time of one PyTorch agent.
  - **Craftax-Classic:** "up to 250x faster" than the Python original.
  - **XLand-MiniGrid (NeurIPS 2024 D&B):** 2^16 parallel environments on one GPU, "1 trillion environment steps under two days" on multiple GPUs, and up to 3M unique tasks.
  - **NAVIX:** "over 200 000x" faster than MiniGrid in batch mode, with 2,048 agents on one A100. Its venue is not stated.
  - **Jumanji:** published at ICLR 2024.
  - **Sable (ICML 2025):** handles more than 1,000 agents with linear memory growth, and wins on 34 of 45 tasks.
  - **Multi-agent Craftax:** not mentioned in the Craftax or JaxMARL READMEs. Whether one exists is UNVERIFIED.
- **Emergent behaviour:**
  - **Lux:** "up to 2000 [agents] in a single timestep", with three stages: "Atomic skills", "Regional Coordination", "Global Strategies".
  - **Garbus and Pollack:** a campfire gives agents downtime together. They develop a drop-and-pick-up exchange protocol and tolerated theft, without any punishment, combat or theft mechanics.
  - **Rachum et al.:** agents "invent, learn, enforce, and transmit a dominance hierarchy to new populations".
  - **Emergent communication:** the review by Boldt and Mortensen ([TMLR 2024](https://arxiv.org/abs/2407.03302)).
  - **LLM populations:** they converge on shared conventions, show collective bias, and can be tipped by committed minorities ([Science Advances 11, eadu9368](https://arxiv.org/abs/2410.08948)).
- **Self-play:**
  - **SPIRAL:** trained on TicTacToe, Kuhn Poker and Simple Negotiation. It gains up to 10% across 8 reasoning benchmarks and beats supervised fine-tuning on 25,000 expert trajectories.
  - **GIGAFLOW:** simulates "42 years of subjective driving experience per hour" on one 8-GPU node, with 17.5 years between incidents in simulation.

## 2026 developments (Jan to Oct 2026)

- **Large-scale multi-agent research:** Google DeepMind and Fenris Creations (the EVE Online studio) announced a research partnership on 21 Aug 2026. It targets "cooperation, competition, negotiation, economics, and emergent social behavior at scale", plus memory and continual learning. No results or agent counts have been published.
- **Self-play for LLMs:** SPIRAL was accepted at ICLR 2026 (arXiv v3, 2 Mar 2026).
- **Training throughput:** PufferLib 4.0 claims "15M steps per second" on one RTX 5090, up from 4M in 3.0. Its experiments release is dated 2026-04-05, and the 5.0 experiments 2026-09-13 ([GitHub API](https://api.github.com/repos/PufferAI/PufferLib/releases)). This is PyTorch/C, not JAX.
- **JaxMARL:** arXiv v6 posted 4 Jul 2026. I couldn't identify what changed.
- **Melting Pot:** v2.4.1 (30 Sep 2026) is maintenance only. The Neural MMO 3.0 code in PufferLib was last changed 23 Mar 2026, and no new version was found.
- **None found:** environment-design or POET successors, XLand/AdA successors, multi-agent Craftax, or 2026 papers on emergent communication or social structure.

## Corrections to the old paper

1. **"132.3 million episodes (31.7 billion frames)"** is the cost to reach stage 4 (ramp defence), not the total. Box surfing comes after 380M episodes, and the plotted training runs to about 500M.
2. **Phase names:** "random" should be "Running and Chasing", and "lock everything" should be "Surf Defense" (ramp locking belongs to Ramp Defense). The order of the middle four was correct.
3. **CTF:** "30 agents" and "25% after 12 hours" are both correct. Add the specifics: two professional testers with full communication, against a fixed pair of FTW agents, with 6.3% draws.
4. **AlphaStar:** correct. Say "officially ranked", across all three races.
5. **XLand "3.4 million unique tasks":** correct, but it is per final-generation agent (with 200B steps), not the size of the task space.
6. **"Phylogenetic trees":** supported, but it is one tree of 100 environments from a single run, in the appendix of the Enhanced POET arXiv version.
7. **Neural MMO "up to 128":** correct for 1.0 as a per-world cap. Version 2.0 supports 1-1024 agents.
8. **JaxMARL "12,500x":** add "when multiple training runs are vectorised (wall-clock)". A single run is about 14x.

## CORTEX store notes (codex-division-2)

Three related papers (dominance hierarchies, resource exchange and Lux) were expected in the agents lane. It lists two, and two of the three are filed in odd places:
- **2401.12258 (dominance hierarchies):** listed in `/home/minty/CORTEX/matrix/lanes/02-artificial-intelligence/agents.md` (line 133).
- **2307.01862 (resource exchange):** listed in the same file (line 347), but filed under `relocated-from-division-15/part-a/medicine_infectious-disease_hiv-aids__2307.01862.pdf`.
- **2301.01609 (Lux):** not in the agents lane. It is in `/home/minty/CORTEX/matrix/lanes/02-artificial-intelligence/hardware-integration.md` (line 61), under `hardware-integration/distributed-training/inference-engines-a/`.


Sources (in addition to every URL in the timeline table):
- [DeepMind CTF blog](https://deepmind.google/discover/blog/capture-the-flag-the-emergence-of-complex-cooperative-agents/)
- [Europe PMC AlphaStar record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:31666705%20AND%20SRC:MED&resultType=core&format=json)
- [arXiv 2107.12808](https://arxiv.org/abs/2107.12808), [ar5iv 1903.00784](https://ar5iv.labs.arxiv.org/html/1903.00784), [ar5iv 2301.01609](https://ar5iv.labs.arxiv.org/html/2301.01609), [OpenAI Neural MMO](https://openai.com/index/neural-mmo)
- [PufferLib 3.0](https://puffer.ai/blog/3.0/), [PufferLib 4.0](https://puffer.ai/blog/4.0/), [PufferLib ocean directory](https://github.com/PufferAI/PufferLib/tree/3.0/pufferlib/ocean), [nmmo3 commit history](https://api.github.com/repos/PufferAI/PufferLib/commits?path=pufferlib/ocean/nmmo3&per_page=100)
- [Melting Pot README](https://github.com/google-deepmind/meltingpot), [Melting Pot releases](https://api.github.com/repos/google-deepmind/meltingpot/releases)
- [JaxMARL proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5aee125f052c90e326dcf6f380df94f6-Abstract.html), [JaxMARL README](https://github.com/FLAIROx/JaxMARL)
- [PureJaxRL README](https://github.com/luchris429/purejaxrl), [PureJaxRL blog](https://chrislu.page/blog/meta-disco/), [Craftax README](https://github.com/MichaelTMatthews/Craftax), [XLand-MiniGrid](https://arxiv.org/abs/2312.12044), [XLand-MiniGrid README](https://github.com/dunnolab/xland-minigrid), [NAVIX](https://arxiv.org/abs/2407.19396), [Jumanji](https://arxiv.org/abs/2306.09884)
- [Sable](https://proceedings.mlr.press/v267/mahjoub25a.html), [SFL README](https://github.com/amacrutherford/sampling-for-learnability), [PAIRED arXiv](https://arxiv.org/abs/2012.02096), [PLR arXiv](https://arxiv.org/abs/2010.03934), [ACCEL arXiv](https://arxiv.org/abs/2203.01302)
- [OMNI-EPIC](https://arxiv.org/abs/2405.15568), [OMNI-EPIC project page](https://omni-epic.vercel.app/), [OvercookedV2 arXiv](https://arxiv.org/pdf/2503.17821), [Overcooked-AI](https://arxiv.org/abs/1910.05789)
- [Absolute Zero repo](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner), [GIGAFLOW arXiv](https://arxiv.org/abs/2502.03349), [DeepMind blog index](https://deepmind.google/discover/blog/)