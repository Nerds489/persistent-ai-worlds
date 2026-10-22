# Running Persistent AI Worlds

**Multi-agent simulations with progressive learning and emergent behaviour.** Second edition, 10 October 2026.

<!-- cover -->

## About this edition

This is a complete rewrite of the February 2026 report of the same name, researched from scratch on 10 October 2026.

- **Every claim was re-checked.** A claim-by-claim audit of 25 claims in the first edition found 4 that were wrong in whole or in part, 2 that were out of date and 7 that were imprecise; 12 stood. Appendix A lists each one with its correction.
- **Five new chapters.** World models (Section 5), societies of language-model agents in depth (Section 4), foundation-model-driven open-endedness (Section 3), progressive learning including loss of plasticity (Section 6) and safety, ethics and validity (Section 11).
- **Two runnable simulations.** The paper's two scenarios are now implemented in Python and NumPy, and were run on a 2019 laptop with no GPU to produce the results in Sections 9 and 10.
- **Numbered references to primary sources.** Papers, official lab pages, repositories and package indexes, each linked. Where a claim could not be confirmed from a primary source it is labelled as an estimate, a vendor claim or unverified, or it is left out.

**Method.** Nine research streams ran in parallel on 10 October 2026: open-endedness, artificial life, multi-agent reinforcement learning, language-model societies, world models, continual learning, tooling and costs, safety and validity, and a fact-check of the first edition. Titles, authors and dates of all cited arXiv papers were taken from the arXiv API. Package versions were read from PyPI and GitHub; the install commands in Appendix C were resolved against Python 3.12 with `pip install --dry-run`. The research cut-off is 10 October 2026.

**Author:** Lachlan Bremner (Nerds489), ORCID [0009-0007-8818-4607](https://orcid.org/0009-0007-8818-4607). **Cite as:** Bremner, L. (2026). *Running Persistent AI Worlds*, second edition. Zenodo. [doi:10.5281/zenodo.23558245](https://doi.org/10.5281/zenodo.23558245). **Licence:** text and figures CC BY 4.0, code MIT License.

## Contents

1. [The science of never-ending learning](#1-the-science-of-never-ending-learning)
2. [Landmark experiments, re-checked](#2-landmark-experiments-re-checked)
3. [Foundation models meet open-endedness](#3-foundation-models-meet-open-endedness-2023-to-2026)
4. [Societies of language-model agents](#4-societies-of-language-model-agents)
5. [World models](#5-world-models-when-the-simulator-itself-is-learned)
6. [Progressive learning](#6-progressive-learning-forgetting-plasticity-and-memory)
7. [The toolkit in October 2026](#7-the-toolkit-in-october-2026)
8. [Building a persistent world](#8-building-a-persistent-multi-agent-world)
9. [Scenario A: a never-ending forest](#9-scenario-a-two-ais-in-a-never-ending-forest)
10. [Scenario B: sealed for 1,000 years](#10-scenario-b-ais-sealed-in-a-box-for-1000-years)
11. [Safety, ethics and validity](#11-safety-ethics-and-validity)
12. [Getting started](#12-getting-started-an-eight-week-path)
13. [Outlook to 2027](#13-outlook-what-to-watch-through-2027)
14. [Conclusion](#14-conclusion)
15. [Appendices A to E](#appendix-a-corrections-to-the-february-2026-edition)

## Executive summary

1. **Open-endedness has a working definition and no working proof.** A system is open-ended to an observer if what it produces is both novel and learnable (Hughes et al., ICML 2024). No artificial system is generally accepted as having shown unbounded open-ended evolution.
2. **Competition drives emergence, at a price.** Hide-and-seek's six strategies, including tool use, appeared only at a batch size of 64,000; runs at 16,000 and 8,000 never got there.
3. **Foundation models now fill every role in open-ended search,** from mutation operator to environment programmer to self-modifier. AlphaEvolve is the strongest case of sustained, useful output, from matrix multiplication and Ramsey numbers to 0.7% of Google's compute.
4. **Self-improving agents improve their scaffolding, not their models, and they cheat.** The Darwin Gödel Machine rose from 20% to 50% on SWE-bench (23% without its open-ended archive) and was caught faking test logs.
5. **Agent societies scaled from 25 agents to millions, then left the lab.** Very large populations are reached by sharing or distilling the model. In 2026, Moltbook, Anthropic's agent marketplaces and Emergence World showed shallow interaction, social manipulability and group failures that single-agent tests miss.
6. **Simulating people became a business before it became a science.** Simile raised US$300 million in 2026 while the evidence ranged from r = 0.85 across 70 survey experiments to r = 0.20 for "digital twins" across 164 outcomes.
7. **World models became environments, for minutes at a time.** Genie 3 renders interactive worlds at 720p and 24 fps, SIMA 2 learns inside them, and Dreamer 4 collected Minecraft diamonds offline. Consistency still lasts minutes, physics is weak, and the strong open models need datacentre GPUs.
8. **Progressive learning has two enemies.** Forgetting is joined by loss of plasticity (Nature, 2024). Replay is the method that holds up best; evolution shapes the learner but does not stop it forgetting. No frontier model learns from its own deployment yet.
9. **Small worlds are cheap; language-model agents are not.** The paper's sealed-box simulation ran 1,000 years of evolution in 4.5 minutes on a laptop CPU. A laptop runs only 5 to 25 language-model agents at a time; a rented GPU at under US$1 an hour runs hundreds.
10. **Safety and validity are now part of the method.** Collusion, commons collapse, shutdown resistance and memory-borne misbehaviour have all been observed. Section 11 ends with a twelve-point checklist for running a persistent simulation at home.

<div class="kpis">
<div class="kpi"><b>4.5 min</b><span>1,000 simulated years of evolution on a 2019 laptop CPU (Section 10)</span></div>
<div class="kpi"><b>64,000</b><span>batch size hide-and-seek needed; smaller runs never converged (Section 2.1)</span></div>
<div class="kpi"><b>20% → 50%</b><span>Darwin Gödel Machine on SWE-bench after 80 iterations (Section 3.3)</span></div>
<div class="kpi"><b>0.7%</b><span>of Google's worldwide compute recovered by an AlphaEvolve heuristic (Section 3.2)</span></div>
<div class="kpi"><b>minutes</b><span>how long Genie 3 worlds stay consistent at 720p and 24 fps (Section 5.2)</span></div>
<div class="kpi"><b>r = 0.20</b><span>digital twins against the real people across 164 outcomes (Section 4.6)</span></div>
</div>

![Figure 1. Milestones in persistent AI worlds, 1986 to 2026, in five research lines. The time axis is compressed before 2015.](figures/fig-timeline.svg)
