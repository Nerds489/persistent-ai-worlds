Search coverage was partial, so the 2026 coverage comes from fetching arXiv, lab, conference and company pages directly, plus their reference lists. "None found" for 2026 means nothing was found, not that nothing exists. Every item was read at its linked source unless marked UNVERIFIED. The Codex stores were not searched in depth.

## Top findings for the paper

1. **There are two separate failure modes, and the old paper covers only one.** Catastrophic forgetting dates from McCloskey & Cohen (1989). Loss of plasticity is a different problem. Dohare et al. (*Nature* 632:768-774, 21 Aug 2024) show that standard deep learning loses plasticity "until they learn no better than a shallow network". They conclude that "methods based on gradient descent are not enough" ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11338828/)).
2. **Replay is the only family of methods that holds up across settings.** In class-incremental learning, "parameter regularization methods such as EWC and SI fail almost completely, even on Split MNIST". Replay is "the only strategy among the top performers in all three scenarios" ([van de Ven et al., NMI 2022](https://www.nature.com/articles/s42256-022-00568-3)). A persistent simulation with no task labels falls in the hard setting.
3. **Plasticity fixes are cheap, but they don't carry over reliably between environments.**
   - In Dohare's tests, continual backprop, L2 and Shrink-and-Perturb kept plasticity "apparently indefinitely".
   - Lyle et al. found layer norm plus weight decay "highly effective" ([2402.18762](https://arxiv.org/abs/2402.18762)).
   - In AgarCL, Shrink-and-Perturb, ReDo and continual backprop gave little improvement ([2505.18347](https://arxiv.org/abs/2505.18347), revised Aug 2026).
   - In Forager, only L2 Init helped consistently, and state construction was "the most useful intervention" ([2605.01131](https://arxiv.org/abs/2605.01131)).
4. **Continual RL evaluation now runs at much larger scale.** MEAL (ICML 2026) trains on 100-task sequences in a few hours on one GPU. Its authors note most continual RL papers use only 3-10 tasks, and that long sequences reveal failures that short ones hide ([2506.14990](https://arxiv.org/abs/2506.14990)). I found no Craftax-based continual RL benchmark, though Craftax itself lists "continual adaptation to novel situations" as a requirement ([2402.16801](https://arxiv.org/abs/2402.16801)).
5. **LLM-era methods change where and how the model learns.** Some learn at test time (Titans, Hope, TTT-E2E). Others update only sparse memory slots (sparse memory finetuning), have the model write its own training data (SEAL), or stay close to the model's own outputs to limit drift (RL's Razor, SDFT). All the evidence is at research scale: Hope was tested at 760M and 1.3B parameters, SEAL on 1B and 7B models.
6. **Frontier labs have made statements, not releases.**
   - Hassabis, 29 Jan 2026: "that technique has not been cracked yet" ([Big Technology](https://www.bigtechnology.com/p/google-deepmind-ceo-demis-hassabis-946)).
   - Amodei, 13 Feb 2026: "a good chance that in the next year or two, we also solve that", while adding that it "might not be a barrier at all" ([Dwarkesh](https://dwarkesh.com/p/dario-amodei-2)).
   - Patel's 7 Aug 2026 essay still treats continual learning as something in the future ([essay](https://www.dwarkesh.com/p/era-of-continual-learning)).
   - I found no primary source for any frontier model that updates its weights from deployment.
7. **Agent memory without weight updates is the practical route, but its benchmark results are disputed.**
   - Zep disputes Mem0's LoCoMo evaluation, and a Letta agent using only file tools beat both.
   - CL-Bench (June 2026) found that "naive ICL outperforms systems dedicated to memory management".
   - EvoMemBench (May 2026) found long-context baselines "highly competitive".
   - The paper shouldn't rest any argument on LoCoMo leaderboards.
8. **The reference designs for simulations are still Generative Agents and Voyager.** Generative Agents ran 25 agents with memory, reflection and planning ([2304.03442](https://arxiv.org/abs/2304.03442)). Voyager's skill library "alleviates catastrophic forgetting" ([2305.16291](https://arxiv.org/abs/2305.16291)). Newer work adds:
   - memory built into the agent's runtime (Letta);
   - evolving instruction playbooks (ACE);
   - RL over stored episodes (MemRL, JitRL);
   - offline consolidation between sessions (sleep-time compute).

   Silver & Sutton describe the target: "Agents will inhabit streams of experience, rather than short snippets of interaction" ([Era of Experience](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf)).
9. **The "evolution outer loop, learning inner loop" design has strong primary support.**
   - Learning speeds up evolution (Hinton & Nowlan 1987, [Complex Systems](https://www.complex-systems.com/abstracts/v01_i03_a06/)).
   - Evolution can set initial weights for fast learning, the Baldwin effect (Fernando et al. 2018, [1806.07917](https://arxiv.org/abs/1806.07917)).
   - A population of RL agents that each learn an internal reward reached human level at Capture the Flag ([1807.01281](https://arxiv.org/abs/1807.01281)).
   - DERL demonstrated a morphological Baldwin effect ([2102.02202](https://arxiv.org/abs/2102.02202)).
   - DiscoRL learned an RL update rule from a population of agents that beat every existing rule on Atari (*Nature*, 22 Oct 2025, [link](https://www.nature.com/articles/s41586-025-09761-x)).
10. **Evolution does not remove forgetting.** Evolved networks that learn during their lifetime still forget. Ellefsen et al. (2015) needed modular networks (from a cost per connection) plus neuromodulation, and call neuromodulation "a necessary, but not sufficient" ingredient ([PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004128)).

## Method comparison

| Method | Year | Mechanism | Strengths | Failure modes | Persistent-sim use | Source |
|---|---|---|---|---|---|---|
| EWC | 2017 | Quadratic penalty pulling weights back to their old values, weighted by the diagonal of the Fisher matrix; computed at each task switch | No stored data; fixed size | Fails class-incremental; the authors say it under-estimates parameter uncertainty | Guard stable core skills only | [1612.00796](https://arxiv.org/abs/1612.00796) |
| Progressive Nets | 2016 | One new column per task; old columns frozen; lateral connections | No forgetting by construction; forward transfer | Parameters grow with each task; task label needed at inference | Known, discrete eras | [1606.04671](https://arxiv.org/abs/1606.04671) |
| PackNet | 2017 | Prune and retrain to free weights for the next task | No growth; 3 tasks added to one VGG-16 at close to separate-network accuracy | Finite capacity | Small fixed skill sets | [1711.05769](https://arxiv.org/abs/1711.05769) |
| Deep Generative Replay | 2017 | A generator replays synthetic data from past tasks | No raw data kept | Standard version "failed" on split CIFAR-100; needs replay of internal representations instead | Replay internal representations, not pixels | [1705.08690](https://arxiv.org/abs/1705.08690), [NComms 2020](https://www.nature.com/articles/s41467-020-17866-2) |
| GEM / A-GEM | 2017/2019 | Adjust each gradient step so loss on a small store of past examples cannot rise (GEM: one constraint per past task; A-GEM: one averaged constraint) | Can improve old tasks; A-GEM "orders of magnitude faster" | GEM's cost grows with tasks and memory | Small per-agent buffers | [1706.08840](https://arxiv.org/abs/1706.08840), [1812.00420](https://arxiv.org/abs/1812.00420) |
| Experience replay (Rolnick et al.) | 2018 | Replay all past experience, mixing on- and off-policy learning with imitation of past behaviour | Needs no task boundaries; a buffer that discards at random performs nearly as well as an unbounded one | Storage | Default baseline | [1811.11682](https://arxiv.org/abs/1811.11682) |
| Continual backprop | 2024 | Continually re-initialise a small fraction of low-utility units | Kept plasticity on ImageNet, CIFAR-100 and RL tasks | Extra hyperparameters; little gain in AgarCL | Learners that run for a lifetime | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11338828/) |
| L2, Shrink-and-Perturb, L2 Init, resets, ReDo, plasticity injection | 2020-2023 | Keep weights small or near their starting values; reset parts of the network or recycle inactive units | Cheap | Sensitive to settings; mixed results across environments | Scheduled resets of part of the network | [1910.08475](https://arxiv.org/abs/1910.08475), [2308.11958](https://arxiv.org/abs/2308.11958), [2205.07802](https://arxiv.org/abs/2205.07802), [2302.12902](https://arxiv.org/abs/2302.12902), [2305.15555](https://arxiv.org/abs/2305.15555) |
| Titans | Dec 2024 | Small network used as memory, updated at test time from "surprise" (how badly it predicts new input), with momentum and adaptive forgetting | Claims ">2M context" | Evidence only at 760M scale | Long history within one episode | [2501.00663](https://arxiv.org/abs/2501.00663) |
| Nested Learning / Hope | NeurIPS 2025 | Memory blocks updated at different frequencies (fast to slow), with a self-modifying variant of Titans | Beats Transformer++ and Titans at 760M and 1.3B; best against ICL, EWC and InCA on class-incremental text tasks | Continual-learning results shown only as bar charts | Memory tiers matched to simulation clocks | [blog](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/), [NeurIPS](https://neurips.cc/virtual/2025/poster/116123) |
| TTT-E2E | Dec 2025 | Transformer with sliding-window attention that writes its context into its weights by training on it at test time | Scales like full attention at 3B; constant latency | Learning stays within one context | Compress long histories | [2512.23675](https://arxiv.org/abs/2512.23675) |
| SEAL | 2025 | Model writes its own training data and instructions (self-edits), applied by fine-tuning; RL trains it to write better ones | Beats GPT-4.1-generated data (single passage) | Forgetting grows with each edit; 30-45 s to evaluate each edit | Offline consolidation | [2506.10943](https://arxiv.org/abs/2506.10943) |
| Sparse memory finetuning | 2025 | Update only the memory-layer slots most activated by new data | Far less forgetting than full fine-tuning or LoRA | Needs a model with memory layers | Learning new facts | [2510.15103](https://arxiv.org/abs/2510.15103) |
| RL's Razor; SDFT | 2025/2026 | Forgetting tracks how far the model drifts from its starting behaviour; learning from its own outputs (RL or self-distillation) keeps drift small | Forgets less than standard fine-tuning (SFT) | Needs rewards (RL) or demonstrations (SDFT) | Updates between simulation epochs | [2509.04259](https://arxiv.org/abs/2509.04259), [2601.19897](https://arxiv.org/abs/2601.19897) |
| MemGPT / Letta | 2023-2026 | Operating-system-style tiers of context; agent edits its own memory; memory built into the agent runtime | Works with any model; inspectable | No weight learning | Persistent LLM characters | [2310.08560](https://arxiv.org/abs/2310.08560), [Letta](https://www.letta.com/blog/why-memory-isnt-a-plugin/) |
| Mem0 / Zep / A-MEM | 2025 | Extract, consolidate and retrieve; time-aware knowledge graph; linked notes | Lower latency and token use | Evaluations disputed | Timestamped facts and relationships | [2504.19413](https://arxiv.org/abs/2504.19413), [2501.13956](https://arxiv.org/abs/2501.13956), [2502.12110](https://arxiv.org/abs/2502.12110) |
| Sleep-time compute | 2025 | Pre-compute over the context offline, before questions arrive | About 5x less compute at answer time | Depends on how predictable the questions are | Night-cycle consolidation | [2504.13171](https://arxiv.org/abs/2504.13171) |
| Evolution outer, RL inner | 1987-2025 | Population selects rewards, hyperparameters, initial weights, body shape or update rule; individuals learn within their lifetime | Human-level Capture the Flag; Atari-leading discovered rule | Compute-heavy; the individual learners still forget | The old paper's design: supported | [1807.01281](https://arxiv.org/abs/1807.01281), [2102.02202](https://arxiv.org/abs/2102.02202), [Nature 2025](https://www.nature.com/articles/s41586-025-09761-x) |

## Key numbers

- **Plasticity** ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11338828/)):
  - Continual ImageNet: up to 88% on early tasks; by task 2,000, some settings were "only slightly better than the linear network". The 2023 preprint gives 89% falling to 77% ([2306.13812](https://arxiv.org/abs/2306.13812)).
  - Permuted MNIST: up to 25% of units dead after 800 tasks; around 60% with Adam.
  - Continual backprop: 76.13% on all 100 CIFAR classes.
  - Ant with fixed friction: PPO failed every episode after 20M steps.
- **EWC on Atari:** 10 games; it learned several but scored below ten separately trained DQNs ([1612.00796](https://arxiv.org/abs/1612.00796)).
- **SEAL:** SQuAD without the passage in context rose from 33.5% to 47.0% (GPT-4.1-generated data: 46.3%). ARC subset: 72.5%, against 20% without RL and 0% with in-context learning alone.
- **Sparse memory finetuning:** drop in NaturalQuestions F1 of 89% (full fine-tuning), 71% (LoRA) and 11% (sparse).
- **Hope** (Nested Learning PDF, Table 2):
  - 760M parameters, 30B tokens: Wiki perplexity 18.68, against 24.18 (Transformer++) and 20.08 (Titans); average accuracy 52.28, against 50.11 and 51.68.
  - 1.3B parameters, 100B tokens: perplexity 14.39, against 17.92 and 15.60; average accuracy 58.04, against 53.38 and 56.82.
- **Test-time training:**
  - TTT-E2E: 3B model, 164B tokens, 2.7x faster than full attention at 128K context.
  - TTT on ARC: 53.0% with an 8B model; 61.9% when combined with program synthesis ([2411.07279](https://arxiv.org/abs/2411.07279)).
- **Memory systems:**
  - Mem0: 26% relative improvement over OpenAI's memory (LLM-as-judge score); 91% lower p95 latency; more than 90% fewer tokens.
  - Zep: 94.8% on DMR against 93.4% for MemGPT; up to 18.5% higher accuracy on LongMemEval; 90% lower latency.
  - Zep's rebuttal of Mem0's evaluation: Zep 75.14%, Mem0 graph 68.44%, Mem0 66.88%, full context 72.90% ([Zep](https://www.getzep.com/blog/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/)).
  - Letta agent using only file tools (GPT-4o mini): 74.0% ([Letta](https://www.letta.com/blog/benchmarking-ai-agent-memory)).
- **Memory benchmarks:** LoCoMo conversations average about 300 turns and 9K tokens, up to 35 sessions ([2402.17753](https://arxiv.org/abs/2402.17753)). LongMemEval has 500 questions testing 5 abilities; commercial assistants show a 30% accuracy drop ([2410.10813](https://arxiv.org/abs/2410.10813)).
- **Sleep-time compute:** about 5x less test-time compute; up to 13% (GSM-Symbolic) and 18% (AIME) higher accuracy; 2.5x lower cost per query.
- **CL-Bench** (normalised reward / gain from experience) ([2606.05661](https://arxiv.org/abs/2606.05661)):
  - In-context learning with Sonnet 4.6: 22.3% / 25.4%, the best.
  - Claude Code: 19.0% / 23.9%.
  - Mem0 with GPT-5.4: 15.1% / 20.2%.
  - ACE: gain of 8.6% at a cost of $62.8.
  - Codex: 6.6% / 14.6%.
- **Voyager:** 3.3x more unique items, 2.3x longer distances, tech-tree milestones up to 15.3x faster.
- **RL environments:**
  - Craftax: 250x faster than Crafter; 1B interactions in under an hour on one GPU.
  - Continual World CW20: 20 tasks of 1M steps each, using SAC ([2105.10919](https://arxiv.org/abs/2105.10919)).
  - Forager: about 328x faster than Jelly Bean World, using 0.1 GB of memory against 13.2 GB.
- **DiscoRL:** its Disco57 rule scored an Atari IQM of 13.86 (*Nature* 648:312-319).
- **Others:** ACE +10.6% on agent tasks and +8.6% on finance; JitRL more than 30x cheaper than the WebRL fine-tuning baseline.

## 2026 developments (Jan-Oct)

- **Background from late 2025:**
  - Karpathy (17 Oct 2025): "They don't have continual learning" ([link](https://www.dwarkesh.com/p/andrej-karpathy)).
  - Sutskever (25 Nov 2025): "we rely on continual learning" ([link](https://www.dwarkesh.com/p/ilya-sutskever-2)).
  - Patel (2 Dec 2025) predicted labs would "release something next year which they call continual learning" ([link](https://www.dwarkesh.com/p/thoughts-on-ai-progress-dec-2025)). I found no such release.
- **Lab statements:** Hassabis and Amodei, as in finding 6. FutureSearch (14 Aug 2026) puts 60% on "continual learning" in mid-2027 meaning context and memory only, with no weight change. That is a forecast, not a finding ([link](https://futuresearch.ai/dwarkesh-continual-learning-forecast/)).
- **UNVERIFIED (secondary sources only):**
  - Amodei saying in a March 2026 interview that continual learning "will be solved in 2026".
  - Sholto Douglas predicting a 2026 solution.
  - Google DeepMind calling 2026 the "year of continual learning" ([dev.to](https://dev.to/max_quimby/scaling-hit-a-wall-three-labs-found-whats-next-3mdd), [eastondev](https://eastondev.com/blog/en/posts/ai/self-evolving-ai-continual-learning/)).
  - Hassabis's remarks at the India AI Impact Summit on 18 Feb 2026 ([storyboard18](https://storyboard18.com/brand-makers/google-deepmind-ceo-says-agi-not-here-yet-calls-current-ai-jagged-intelligence-90028.htm)).
- **LLM continual learning:**
  - SDFT (27 Jan 2026).
  - TMEM, which updates fast LoRA weights during an episode (3 Jun 2026, [2606.04536](https://arxiv.org/abs/2606.04536)).
  - "When Does Continual Learning Require Learning" (8 Jul 2026, [2607.07847](https://arxiv.org/abs/2607.07847)): prompt-based methods adapt fast but degrade later; distillation retains knowledge but struggles to update facts; online RL adapts best but is sensitive to noisy rewards.
  - Thomson (27 Aug 2026, [2608.27147](https://arxiv.org/abs/2608.27147)) claims forgetting is eliminated "almost completely", with no numbers in the abstract.
  - A survey (6 Aug 2026, [2608.06216](https://arxiv.org/abs/2608.06216)) describes a shift "from parameter-centric learning toward system-level adaptation".
  - I found no 2026 Google follow-up to Titans or Hope.
- **Plasticity and continual RL:** Forager (1 May 2026); AgarCL revisions (Mar and Aug 2026); MEAL at ICML 2026; an ICML 2026 position paper, "Deployed Reinforcement Learning should be Continual" ([2606.04029](https://arxiv.org/abs/2606.04029)); Stream-X revised 21 Sep 2026, tested on 58 Atari games and 50 control tasks ([2410.14606](https://arxiv.org/abs/2410.14606)). I found no 2026 plasticity result with the impact of Dohare et al.
- **Agent memory:**
  - CL-Bench (4 Jun 2026).
  - EvoMemBench (18 May 2026, 15 methods, "far from a general solution", [2605.18421](https://arxiv.org/abs/2605.18421)).
  - MemRL (6 Jan 2026, [2601.03192](https://arxiv.org/abs/2601.03192)).
  - JitRL, an oral at the ICLR 2026 workshop on memory for agents (27 Apr 2026, [link](https://iclr.cc/virtual/2026/10021226)).
  - ACE at ICLR 2026 ([2510.04618](https://arxiv.org/abs/2510.04618)).
  - Letta's "Why Memory Isn't a Plugin" (3 Apr 2026) and Mods, which let agents modify their own runtime (24 Jun 2026, [link](https://www.letta.com/blog/introducing-mods/)).
- **Evolution and learning:** none found for 2026. DiscoRL (Oct 2025) is the latest I could confirm.

## Corrections to the old paper's summary

- **EWC "penalises changes to important parameters":** correct but incomplete. The penalty uses the diagonal of the Fisher matrix and is computed at task switches, so it needs task boundaries. It fails in class-incremental learning, and its authors say it "under-estimates parameter uncertainty". Their Atari agent also needed a task-recognition model, per-game biases and gains, and short-term replay buffers per task. Even then it scored below ten separate DQNs.
- **Progressive Nets "immune to forgetting":** true by construction, because old columns are frozen. The authors list two limitations: "growth in number of parameters with the number of tasks", and that choosing the column at inference "requires knowledge of the task label". Frozen columns also can't benefit from later learning; that follows from the freezing rather than being stated in the paper.
- **Generative Replay:** the mechanism is described correctly, but the standard version "failed" on natural images. Scaling it needed replay of internal representations (van de Ven et al. 2020).
- **"Population-based evolution sidesteps the problem":** wrong as stated. Individuals that don't learn during their lifetime avoid forgetting only because they don't learn (this is my reasoning, not a cited result). Evolved learners still forget (Ellefsen et al. 2015). The primary evidence supports evolution as an outer loop that shapes the learner, not as a replacement for replay or plasticity maintenance.
- **Missing topics:** loss of plasticity, test-time learning, and agent memory without weight updates.

**UNVERIFIED citation details:**
- McCloskey & Cohen: volume 24, pp. 109-165 and DOI 10.1016/S0079-7421(08)60536-8. The publisher page returned 403; that they coined the term in 1989 comes from [Wikipedia](https://en.wikipedia.org/wiki/Catastrophic_interference).
- PackNet at CVPR 2018.
- Generative Agents at UIST 2023.

## Local files

- Primary PDFs read: the full 52-page Nested Learning paper (the Hope tables are on pp. 33-37) and the Era of Experience chapter.
- `/home/minty/CORTEX/matrix/lanes/02-artificial-intelligence/neural-evolution.md` indexes related papers in the store. Those papers were not read.