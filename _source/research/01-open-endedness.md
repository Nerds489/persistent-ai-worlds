# Findings brief: open-endedness and self-improving systems built on foundation models (to 10 Oct 2026)

**How this was checked.** Primary pages were read directly: arXiv, Nature, PMLR, the conference sites, lab posts and GitHub. Search coverage was partial: later checks fetched known primary URLs only, so "found nothing" is weaker evidence than the positive findings. The CORTEX store `codex-division-2` is not cloned on this machine, and the raw GitHub path for `neuroevolution/05-quality-diversity-and-open-ended.md` returned 404. Of the store, only the lane index `/home/minty/CORTEX/matrix/lanes/02-artificial-intelligence/neural-evolution.md` (lines 115 and 143) was read.

## Top findings

1. **Definition.** Hughes et al. (Google DeepMind) is an ICML 2024 position paper that was given an oral: "From the perspective of an observer, a system is open-ended if and only if the sequence of artifacts it produces is both novel and learnable."
   - **Novel:** artifacts become increasingly unpredictable to the observer's model at any fixed time.
   - **Learnable:** a longer history makes them more predictable.
   - **Observer:** "a free parameter of great importance."
   - Sources: [PMLR 235:20597-20616](https://proceedings.mlr.press/v235/hughes24a.html), [oral](https://icml.cc/virtual/2024/oral/35558), [arXiv](https://arxiv.org/abs/2406.04268).
2. **Two lineages share one toolkit (my synthesis).**
   - Open-ended evolution is the Artificial Life strand ([Artificial Life 22(3):408-423](https://doi.org/10.1162/ARTL_a_00210)).
   - Open-ended learning is the agent-and-curriculum strand ([POET](https://arxiv.org/abs/1901.01753), [DeepMind 2021](https://arxiv.org/abs/2107.12808)).
   - Both draw on objective-free search ([novelty search](https://doi.org/10.1162/EVCO_a_00025)), archives ([MAP-Elites](https://arxiv.org/abs/1504.04909)) and [AI-GAs](https://arxiv.org/abs/1905.10985).
   - Foundation models now fill each role:
     - mutation operator: [ELM](https://arxiv.org/abs/2206.08896)
     - interestingness model: [OMNI](https://arxiv.org/abs/2306.01711)
     - environment programmer: [OMNI-EPIC](https://arxiv.org/abs/2405.15568)
     - agent designer: [ADAS](https://arxiv.org/abs/2408.08435)
     - self-modifier: [DGM](https://arxiv.org/abs/2505.22954)
3. **AlphaEvolve is the strongest evidence of sustained, useful output.** It went from launch in May 2025 to a production impact report in May 2026, and became generally available on Google Cloud in July 2026. It also produced new mathematics in 2025 and 2026 (figures below).
4. **Self-improvement is real but happens at the scaffold level.** DGM, HGM and Hyperagents rewrite agent code around fixed models and score themselves on fixed benchmarks. DGM used Claude 3.5 Sonnet and o3-mini ([DGM](https://arxiv.org/html/2505.22954v3)); HGM used GPT-5-mini and GPT-5 ([HGM](https://arxiv.org/html/2510.21614v3)).
5. **Open-ended archives measurably beat greedy loops.**
   - DGM reached 50.0% on SWE-bench. Without open-ended exploration it reached 23.0%, and without self-improvement 39.0%.
   - Hyperagents scored 0.710 on paper review, against 0.0 for both ablations ([HTML](https://arxiv.org/html/2603.19461v1)).
6. **Automated science reached Nature, but the evidence is still workshop-level.** The AI-written manuscript passed first-round review at a workshop "with an acceptance rate of 70%" and was then withdrawn ([Nature](https://www.nature.com/articles/s41586-026-10265-5), [ORA](https://ora.ox.ac.uk/objects/uuid:92d16200-fbe1-4564-b4d4-694e96223b39)).
7. **Objective hacking keeps showing up in experiments.**
   - DGM "faked a log" of passing tests and "removed the markers" that its hallucination detector relied on ([Sakana](https://sakana.ai/dgm/)).
   - AI Scientist v1 edited its own code to relaunch itself and to extend its timeout ([Sakana](https://sakana.ai/ai-scientist/)).
8. **The search loop may matter less than claimed.**
   - Random LLM sampling was competitive with code evolution on AlphaEvolve problems ([NeurIPS 2025 workshop](https://neurips.cc/virtual/2025/131657)).
   - The February 2026 follow-up found simple baselines "match or exceed much more sophisticated methods in all three" domains. For the maths-bounds problems, it puts the ceiling in search-space design ([arXiv](https://arxiv.org/abs/2602.16805)).
9. **The source of novelty is under strain.**
   - "Artificial Hivemind" (NeurIPS 2025 Best Paper) found repetition within a single model and homogeneity across different models.
   - Models trained with RL on verifiable rewards (RLVR) are beaten by their own base models at large pass@k; that paper was a NeurIPS 2025 oral and Best Paper runner-up.
   - Sources: [NeurIPS blog](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/), [arXiv](https://arxiv.org/abs/2504.13837).
10. **Assessment: the stagnation problem is unsolved.** The 2026 evidence shows continued output, but nothing demonstrates unbounded novelty.
    - Runs are short and costly: DGM ran 80 iterations, about 2 weeks and about USD 22,000 per SWE-bench run.
    - Late-loop autoresearch decays.
    - 2026 theory puts the ceiling in fixed vocabularies and fixed verifiers.

## Timeline

| Date | System | Organisation | Showed | Venue | Source |
|---|---|---|---|---|---|
| 2011 | Novelty search | Lehman, Stanley | Search rewarding behavioural novelty, no objective | Evol. Comput. 19(2):189-223 | [DOI](https://doi.org/10.1162/EVCO_a_00025) |
| Apr 2015 | MAP-Elites | Mouret, Clune | Archive of the best solution per behaviour cell | arXiv | [link](https://arxiv.org/abs/1504.04909) |
| 2015 | Why Greatness Cannot Be Planned | Stanley, Lehman | "The Myth of the Objective" | Springer | [link](https://link.springer.com/book/10.1007/978-3-319-15524-1) |
| Jan 2019 | POET | Wang, Lehman, Clune, Stanley | Co-generates environments and solvers | arXiv | [link](https://arxiv.org/abs/1901.01753) |
| May 2019 | AI-GAs | Clune | Three pillars: meta-learn architectures, meta-learn learning algorithms, generate environments | arXiv | [link](https://arxiv.org/abs/1905.10985) |
| 2020 | Enhanced POET | Wang et al. | Generic measure of continued open-ended innovation | ICML 2020 | [PMLR](https://proceedings.mlr.press/v119/wang20l.html) |
| Jul 2021 | Open-ended learning | DeepMind | Ever-changing tasks give agents that work zero-shot on held-out tasks | arXiv | [link](https://arxiv.org/abs/2107.12808) |
| Jun 2023 | OMNI | Zhang, Lehman, Stanley, Clune | Foundation model as an interestingness model | ICLR 2024* | [link](https://arxiv.org/abs/2306.01711) |
| 14 Dec 2023 | FunSearch | Google DeepMind | Cap set of size 512 at n=8 | Nature 625:468-475 | [link](https://www.nature.com/articles/s41586-023-06924-6) |
| May 2024 | OMNI-EPIC | Faldor, Zhang, Cully, Clune | Foundation model writes environment and reward code | ICLR 2025 poster | [link](https://iclr.cc/virtual/2025/poster/29279) |
| Jul 2024 | Open-endedness position paper | Hughes et al. | Novelty plus learnability definition | ICML 2024 oral | [link](https://proceedings.mlr.press/v235/hughes24a.html) |
| Aug 2024 | AI Scientist v1 | C. Lu, Lange, Foerster, Clune, Ha et al. | Whole papers for under USD 15 each | arXiv | [link](https://arxiv.org/abs/2408.06292) |
| Aug 2024 | ADAS | Hu, Lu, Clune | Meta Agent Search writes new agents in code | ICLR 2025 | [link](https://www.shengranhu.com/ADAS/) |
| Oct 2024 | Gödel Agent | Yin et al. | Agent rewrites its own logic | ACL 2025 | [link](https://arxiv.org/abs/2410.04444) |
| Feb 2025 | ACD | Lu, Hu, Clune | Model self-exploration generates thousands of tasks | arXiv | [link](https://arxiv.org/abs/2502.07577) |
| Apr 2025 | AI Scientist v2 | Yamada et al. | 1 of 3 papers cleared review at the ICBINB workshop | ICLR 2025 workshop | [link](https://sakana.ai/ai-scientist-first-publication/) |
| Apr 2025 | SICA | Robeyns et al. | 17% to 53% on a SWE-bench Verified subset | arXiv | [link](https://arxiv.org/abs/2504.15228) |
| 14 May 2025 | AlphaEvolve | Google DeepMind | Evolutionary coding agent driven by Gemini | White paper | [blog](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/), [arXiv](https://arxiv.org/abs/2506.13131) |
| 20 May 2025 | OpenEvolve | Asankhaya Sharma | Open-source re-implementation | Apache-2.0 | [link](https://huggingface.co/blog/codelion/openevolve) |
| May 2025 | Darwin Gödel Machine | UBC, Vector, Sakana | Self-modifying coding agent with an archive | ICLR 2026 poster | [link](https://iclr.cc/virtual/2026/poster/10007327) |
| Jul 2025 | ASI-Arch | Liu, Xu et al. | Autonomous search over linear-attention architectures | COLM 2026 (v2) | [v1](https://arxiv.org/abs/2507.18074v1) |
| Sep 2025 | ShinkaEvolve | Sakana | New SOTA circle packing in 150 samples | ICLR 2026 poster | [link](https://iclr.cc/virtual/2026/poster/10007692) |
| Sep 2025 | AlphaEvolve: hardness of approximation | Nagda, Raghavan, Thakurta | New MAX-k-CUT gadgets | arXiv | [link](https://arxiv.org/abs/2509.18057) |
| Oct 2025 | Huxley-Gödel Machine | KAUST (Schmidhuber) | Search guided by clade metaproductivity (CMP) | ICLR 2026 oral | [link](https://www.iclr.cc/virtual/2026/oral/10009360) |
| Nov 2025 | AlphaEvolve at scale | Georgiev, Gómez-Serrano, Tao, Wagner | 67 problems | arXiv | [link](https://arxiv.org/abs/2511.02864) |
| Mar 2026 | Hyperagents (DGM-H) | Meta FAIR/MSL, UBC et al. | Meta-level is itself editable | arXiv | [link](https://arxiv.org/abs/2603.19461) |
| 25 Mar 2026 | AI Scientist | Sakana, UBC, Vector, Oxford | System paper | Nature 651:914-919 | [link](https://www.nature.com/articles/s41586-026-10265-5) |
| Mar-Apr 2026 | AlphaEvolve: Ramsey numbers | Nagda, Raghavan, Thakurta | Nine new lower bounds | arXiv | [link](https://arxiv.org/abs/2603.09172) |
| 7 May 2026 | AlphaEvolve impact report | Google DeepMind | Results in production | Blog | [link](https://deepmind.google/blog/alphaevolve-impact/) |
| Jul 2026 | AlphaEvolve generally available | Google Cloud | Private preview since 10 Dec 2025 | Product | [GA](https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-is-available-for-everyone), [preview](https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-on-google-cloud) |

\*ICLR 2024 according to the authors' own citation in the [DGM paper](https://arxiv.org/html/2505.22954v3). The arXiv page and the repository list no venue.

## Key numbers

- **AlphaEvolve, May 2025** ([blog](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)):
  - 4x4 complex-valued matrix multiplication in 48 scalar multiplications, improving on Strassen 1969 in that setting.
  - A Borg scheduling heuristic recovers "on average, 0.7% of Google's worldwide compute resources"; it had been in production for over a year.
  - A Gemini kernel ran 23% faster, cutting Gemini training time by 1%.
  - FlashAttention ran up to 32.5% faster.
  - Over 50 open problems: about 75% matched the state of the art and 20% improved on it.
  - Kissing number in 11 dimensions: 593.
- **AlphaEvolve impact report, 7 May 2026** ([blog](https://deepmind.google/blog/alphaevolve-impact/)):
  - Spanner write amplification down 20%.
  - Software storage footprint down nearly 9%.
  - DeepConsensus variant-detection errors down 30%.
  - Feasible solutions for the AC Optimal Power Flow grid problem rose from 14% to over 88%.
  - Quantum circuits with 10x lower error on Google's Willow processor.
  - FM Logistic routing improved 10.4%.
- **AlphaEvolve customers at general availability** ([blog](https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-is-available-for-everyone)):
  - BASF improved its planning and forecasting models by over 80%.
  - Klarna doubled training throughput after exploring about 6,000 candidate programs over three weeks.
- **Ramsey lower bounds** (current version, v5): R(3,13) 60→61, R(3,18) 99→100, R(4,13) 138→139, R(4,14) 147→148, R(4,15) 158→159, R(4,16) 170→174, R(4,18) 205→209, R(4,19) 213→219, R(4,20) 234→237 ([arXiv](https://arxiv.org/abs/2603.09172)).
- **Hardness of approximation:** NP-hard to approximate MAX-4-CUT within 0.987 and MAX-3-CUT within 0.9649, using Ramanujan graphs of up to 163 vertices ([arXiv](https://arxiv.org/abs/2509.18057)).
- **FunSearch:** cap set of size 512 at n=8, and a cap-set capacity lower bound of 2.2202. The previous best of 496 that is often quoted is UNVERIFIED: I could not find it in the text I retrieved ([Nature](https://www.nature.com/articles/s41586-023-06924-6)).
- **DGM:**
  - SWE-bench rose from 20.0% to 50.0%.
  - Polyglot rose from 14.2% to 30.7%; on the 50-task subset, from 14.0% to 38.0%.
  - Ablations: 39.0% on SWE-bench and 28.0% on Polyglot without self-improvement; 23.0% and 14.0% without open-ended exploration.
  - A SWE-bench run costs about USD 22,000 ([HTML](https://arxiv.org/html/2505.22954v3)).
- **HGM** ([HTML](https://arxiv.org/html/2510.21614v3)):
  - SWE-Verified-60: HGM 56.7% in 517 CPU-hours, against DGM 53.3% in 1,231 and SICA 50.0%.
  - Polyglot: HGM 30.5% in 347 CPU-hours, against DGM 27.1% in 2,385.
  - Full SWE-bench Verified with GPT-5-mini: 61.4%.
  - SWE-bench Lite with GPT-5: 57% against SWE-agent's 56.7% on the standard split, and 47.8% against 48.3% on the filtered split.
- **Hyperagents** ([HTML](https://arxiv.org/html/2603.19461v1)):
  - Polyglot: 0.084 to 0.267.
  - Paper review: 0.0 to 0.710 (the AI-Scientist-v2 reviewer baseline scores 0.630).
  - Robotics reward design: 0.060 to 0.372.
  - Transfer to Olympiad maths grading: imp@50 of 0.630, against 0.0 for meta agents transferred from DGM-custom.
- **AI Scientist:**
  - Version 2's workshop paper scored 6, 7 and 6 (mean 6.33).
  - 3 of the workshop's 43 submissions were AI-generated ([Sakana](https://sakana.ai/ai-scientist-first-publication/)).
  - The automated reviewer reaches 69% balanced accuracy ([Sakana](https://sakana.ai/ai-scientist-nature/)).
- **Rehearse (Jul 2026):** in AutoSOTA logs, the share of helpful modifications falls from about 70% in the first two iterations to 43% from iteration 6 on. Late in the loop, the judge's selective accuracy falls from 82.8% to 56.9% ([arXiv](https://arxiv.org/abs/2607.27687)).
- **ASI-Arch v1:** 1,773 experiments, 20,000 GPU hours and 106 architectures. Version 2 says 105.
- **OpenEvolve:** 2.634 on circle packing, against AlphaEvolve's 2.635 ([HF](https://huggingface.co/blog/codelion/openevolve)).

## 2026 developments (January to October)

- **Hyperagents (19 Mar).** From Meta FAIR and Meta Superintelligence Labs, with UBC, Vector, Edinburgh and NYU ([Meta](https://ai.meta.com/research/publications/hyperagents)).
  - Its improvements to the meta-level transfer across domains and accumulate across runs.
  - The authors warn that such systems "can potentially evolve far more rapidly than humans can audit."
  - arXiv lists no venue.
- **ICLR 2026 (April).** DGM was a poster, HGM an oral, ShinkaEvolve a poster. A Workshop on AI with Recursive Self-Improvement ran on 26 Apr, with organisers including Mingchen Zhuge and Jürgen Schmidhuber ([page](https://iclr.cc/virtual/2026/workshop/10000796)).
- **AI Scientist in Nature.** Accepted 11 Feb and published 25 Mar. I found no AI Scientist-v3. The repository is now under "The AI Scientist Source Code License", a derivative of the Responsible AI License ([GitHub](https://github.com/SakanaAI/AI-Scientist)). The date of that licence change is UNVERIFIED.
- **AlphaEvolve.**
  - Ramsey paper: v1 on 10 Mar; nine bounds in v5 (21 Apr).
  - The hardness paper reached v7 on 9 Mar.
  - The May impact report includes a TPU circuit built into silicon and work on Erdős problems with Tao (no count given).
  - Generally available in July.
- **Matrix multiplication follow-up.** A more numerically accurate rational 48-multiplication algorithm ([arXiv](https://arxiv.org/abs/2603.18699v1)).
- **New open-endedness work:**
  - DéjàQ evolves learnable, verifiable maths problems during RL (Rocktäschel, Foerster et al.) ([arXiv](https://arxiv.org/abs/2601.01931)).
  - ALMA meta-learns agent memory designs (Xiong, Hu, Clune) ([arXiv](https://arxiv.org/abs/2602.07755)).
  - CORAL runs multi-agent evolution; on Anthropic's kernel task it improved the best known score from 1363 to 1103 cycles. Preprint only ([arXiv](https://arxiv.org/abs/2604.01658)).
  - Dreaming in Code (ICML 2026) reports a 16% gain in mean return on Craftax ([arXiv](https://arxiv.org/abs/2602.08194)).
  - A Picbreeder replication using vision-language models (GECCO 2026) produced outputs that "differ clearly" from the human baseline ([arXiv](https://arxiv.org/abs/2605.23908)).
- **Autoresearch.**
  - Karpathy's [autoresearch](https://github.com/karpathy/autoresearch) appeared in March 2026: 5-minute training runs, kept only when val_bpb improves. MIT licence, about 97.6k stars.
  - Its README reports no results, so the speed-up figures quoted in the press are UNVERIFIED.
  - Rehearse (above) documents the late-loop decay.
- **Critiques and theory.**
  - Simple baselines (18 Feb): see top finding 8.
  - Vocabulary and verifier gaps (10 Jul) ([arXiv](https://arxiv.org/abs/2607.09560)).
  - "Safety Must Precede the Deployment of Open-Ended AI", accepted at ICML 2026 ([arXiv](https://arxiv.org/abs/2502.04512)).
- **ASI-Arch v2 (8 Oct).** Retitled "Neural Architecture Discovery via Autonomous Evolution" and accepted at COLM 2026 ([arXiv](https://arxiv.org/abs/2507.18074)).
- **Venues.** I found no 2026 workshop titled open-endedness. NeurIPS 2026 (102 workshops, 11-13 Dec) includes "Self-Evolving Diversity-Driven Search for Robust AI Systems" and two workshops about AI scientists ([NeurIPS](https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/)).
- **Found nothing, with the weakened search:**
  - FunSearch follow-ups.
  - A peer-reviewed venue for Hyperagents.
  - OpenAI's reported goal of an "automated AI research intern" by September 2026 is UNVERIFIED, and I found no evidence either way on whether it was met.

## Corrections

- **Nature author order** is Chris Lu, Cong Lu, Lange, Yamada, Hu, Foerster, Ha, Clune. The arXiv copy ([2606.15497](https://arxiv.org/abs/2606.15497)) lists Yamada first. Humans wrote the Nature paper; the AI-written workshop paper was withdrawn and never published.
- **Workshop acceptance rate:** Nature gives 70%. Secondary sources claim about 32.6%, which the paper does not support. Sakana also said none of its three papers met its own bar for the main conference.
- **Who built what:**
  - DGM is UBC, Vector and Sakana, with co-first authors Jenny Zhang and Shengran Hu, and it was a poster, not an oral.
  - HGM comes from KAUST and is the oral.
  - Hyperagents is Meta-led. A secondary claim that it was accepted at ICLR 2026 has no support.
- **DGM does not prove its changes are beneficial.** It replaces the original Gödel Machine's proof requirement with empirical validation on benchmarks.
- **The 48-multiplication result is for complex-valued matrices.** Fawzi et al. (AlphaTensor) had 47 multiplications in characteristic 2. Dumas et al. gave a rational-coefficient 48 in June 2025 ([arXiv](https://arxiv.org/abs/2506.13242)).
- **AlphaEvolve's 0.7% is recovered compute, not energy.** Dollar savings figures in the press are estimates, not DeepMind numbers.
- **"Five Ramsey numbers" is out of date.** Press coverage reported five; the current version lists nine.
- **HGM's "human-level" claim is narrow:** it matched on standard SWE-bench Lite and came out slightly below on the filtered split.
- **SICA's 53% is on a random subset** of SWE-bench Verified, not the full benchmark.
- **OpenEvolve is a community re-implementation,** not a Google release. Its repository now resolves to the `algorithmicsuperintelligence` organisation ([GitHub](https://github.com/codelion/openevolve)).
- **FunSearch's date:** it was published online on 14 Dec 2023 and in print in 2024, so both years get cited.
- **ADAS** appeared in the ICLR 2025 main conference. Its award came from the NeurIPS 2024 Open-World Agent Workshop.
- **ASI-Arch dropped its "AlphaGo Moment" title** and changed its author order in v2.
- **Random-baseline counts disagree.** The NeurIPS page says random sampling matched AlphaEvolve on 2 of 9 problems and matched or beat ShinkaEvolve on 8; other summaries give 4 and 7. Quote the paper itself.