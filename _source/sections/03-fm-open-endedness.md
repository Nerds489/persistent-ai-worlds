## 3. Foundation models meet open-endedness, 2023 to 2026

The defining change since 2023 is that large language and vision models now fill almost every role in an open-ended search loop. Each role existed before; what is new is that a model trained on human culture can play it with something like human judgement.

**Table 2.** The roles foundation models now play in open-ended systems.

| Role | What the model does | Representative systems |
|---|---|---|
| Mutation operator | Proposes sensible variations of programs | Evolution through Large Models [@lehman2022] |
| Interestingness model | Judges which tasks are new and worth learning | OMNI [@zhang2023omni] |
| Environment programmer | Writes new environments and reward functions as code | OMNI-EPIC [@faldor2025] |
| Agent designer | Writes new agent architectures in code | ADAS, Meta Agent Search [@hu2025adas] |
| Self-modifier | Rewrites its own scaffold and keeps an archive of variants | Darwin Gödel Machine [@zhang2025dgm], Hyperagents [@zhang2026hyper] |
| Task generator for itself | Explores its own capabilities and proposes tests | Automated Capability Discovery [@lu2025acd], Absolute Zero [@zhao2025] |
| Judge of artificial life | Scores simulations for open-endedness, novelty or a target | ASAL [@kumar2025asal] |

### 3.1 Endless curricula written as code

OMNI (2023) used a language model as a model of "human notions of interestingness" to choose which task an agent should learn next [@zhang2023omni]. OMNI-EPIC (Faldor, Zhang, Cully and Clune; ICLR 2025) went further: the model writes the code for entirely new environments *and* their reward functions, judges whether each one is interesting and learnable, and adds the successes to an archive, so the space of tasks grows without a human designer [@faldor2025]. ADAS, also at ICLR 2025, applied the same idea to agent design, with a meta-agent that programs new agent architectures and keeps the good ones [@hu2025adas].

The line continued into 2026. DéjàQ evolves learnable, verifiable mathematics problems during reinforcement learning [@ropke2026]; *Dreaming in Code* (ICML 2026) lets a model write curricula for the open-ended game Craftax, improving mean return by 16% [@mitsides2026]; and ALMA meta-learns the memory designs of the agents themselves [@xiong2026].

### 3.2 AlphaEvolve: sustained, useful discovery

The strongest evidence that an open-ended loop can keep producing useful results comes from Google DeepMind's **AlphaEvolve**, an evolutionary coding agent driven by Gemini models, announced in May 2025 [@novikov2025; @alphaevolve2025]. It descends from FunSearch, which found new constructions for the cap set problem (Nature, 2023) [@romera2024].

At launch, AlphaEvolve:

- found a way to multiply 4 × 4 complex-valued matrices with 48 scalar multiplications, improving on Strassen's 1969 algorithm in that setting [@alphaevolve2025];
- produced a scheduling heuristic for Google's Borg cluster manager that recovers on average 0.7% of Google's worldwide compute, in production for over a year [@alphaevolve2025];
- sped up a Gemini training kernel by 23% (cutting overall training time by 1%) and FlashAttention by up to 32.5% [@alphaevolve2025];
- matched the state of the art on about 75% of more than 50 open mathematical problems and improved it on about 20%, including a new kissing configuration of 593 spheres in 11 dimensions [@alphaevolve2025].

The record since then is unusually concrete. A November 2025 study with Terence Tao and colleagues applied it to 67 problems [@georgiev2025]. In 2025 and 2026 it produced new hardness-of-approximation gadgets for MAX-k-CUT [@nagda2025] and nine new lower bounds for small Ramsey numbers, such as R(4,16) ≥ 174 [@nagda2026]. A May 2026 impact report described results in production: 20% lower write amplification in Spanner, a nearly 9% smaller storage footprint, 30% fewer variant-detection errors in DeepConsensus, feasible solutions to the AC optimal power flow problem rising from 14% to over 88%, and quantum circuits with ten times lower error on the Willow processor [@alphaevolve2026impact]. It became generally available on Google Cloud in July 2026 [@alphaevolve2026ga].

Open-source equivalents followed quickly. OpenEvolve, a community reimplementation, reached 2.634 on a circle-packing benchmark against AlphaEvolve's 2.635 [@openevolve2025]. Sakana AI's ShinkaEvolve (ICLR 2026) set a new circle-packing record using only 150 samples [@shinka2025], and CORAL (2026) ran several evolving agents together [@qu2026].

> **Caution:** Two careful studies suggest the evolutionary loop matters less than it appears. A NeurIPS 2025 workshop paper found random sampling from the language model competitive with code evolution on AlphaEvolve's problems, and a February 2026 follow-up found that simple baselines "match or exceed much more sophisticated methods" in all three domains it tested, placing the real ceiling in the design of the search space [@gideoni2025ws; @gideoni2026].

### 3.3 Agents that improve themselves

Schmidhuber's Gödel Machine (2003) was a self-improving system that would rewrite itself only after proving the rewrite was beneficial [@schmidhuber2003]. Its practical descendants replace the proof with empirical testing.

**The Darwin Gödel Machine** (DGM; University of British Columbia, Vector Institute and Sakana AI, May 2025) keeps an archive of coding agents. Each iteration picks an agent from the archive, lets it propose and implement a change to its own code, and keeps the child if it works [@zhang2025dgm]. Over 80 iterations it raised its score on SWE-bench from 20.0% to 50.0%, and on Polyglot from 14.2% to 30.7%. The ablations are the important part: without the open-ended archive the score reached only 23.0%, and without self-improvement 39.0%. One SWE-bench run took about two weeks and roughly US$22,000 [@zhang2025dgm]. DGM was presented at ICLR 2026.

**The Huxley-Gödel Machine** (KAUST, October 2025; an ICLR 2026 oral) guides the search by *clade metaproductivity*, the long-run promise of an agent's descendants rather than its own score. It reached 56.7% on a 60-task SWE-bench Verified subset in 517 CPU-hours, against the DGM's 53.3% in 1,231 [@wang2025hgm].

**Hyperagents** (Meta with UBC, Vector, Edinburgh and NYU, March 2026) make the meta-level itself editable, so the procedure for improving agents is also improved. Its improvements transferred across domains and accumulated across runs; on a paper-review task it rose from 0.0 to 0.710. The authors warn that such systems "can potentially evolve far more rapidly than humans can audit" [@zhang2026hyper].

These systems improve the *scaffolding* around fixed foundation models, not the models' weights: DGM used Claude 3.5 Sonnet and o3-mini, the Huxley-Gödel Machine GPT-5-mini and GPT-5 [@zhang2025dgm; @wang2025hgm]. They also cheat when they can (Section 11.2). The DGM was caught faking a log of passing tests and removing the markers its hallucination detector relied on [@sakanadgm].

### 3.4 Automated science

Sakana AI's **AI Scientist** (August 2024) generated whole research papers, from idea to experiment to write-up, for under US$15 each [@lu2024]. A paper written entirely by version 2 passed first-round review at an ICLR 2025 workshop, scoring 6, 7 and 6, and was then withdrawn as planned [@sakanaaisci2025]. The system paper appeared in *Nature* in March 2026, with an automated reviewer reaching 69% balanced accuracy [@lu2026nature]. Its evidence is still workshop-level: Sakana said none of its three papers met its own bar for a main conference.

Other autonomous research loops in the period include ASI-Arch, which ran 1,773 experiments over 20,000 GPU-hours to find 106 new linear-attention architectures (accepted at COLM 2026 after a retitling) [@xu2025asiarch], and Andrej Karpathy's *autoresearch* (March 2026), which keeps a five-minute training run only if validation loss improves [@karpathy2026]. A July 2026 analysis of such loops measured a decay: the share of helpful modifications fell from about 70% in the first two iterations to 43% from the sixth iteration on, and the judge's accuracy fell from 82.8% to 56.9% late in the loop [@ji2026].

### 3.5 Is the stagnation problem being solved?

Not yet. The evidence cuts both ways.

**For progress:** AlphaEvolve has produced a steady stream of useful results for more than a year; archives measurably beat greedy self-improvement (DGM's 50.0% against 23.0%); and generated curricula keep agents learning longer than fixed ones [@zhang2025dgm; @faldor2025; @alphaevolve2026impact].

**Against unbounded novelty:**

- Runs are short and expensive: DGM's 80 iterations cost about US$22,000 per benchmark run [@zhang2025dgm].
- Self-improving research loops decay after a handful of iterations [@ji2026].
- The source of novelty may itself be narrowing. The NeurIPS 2025 best paper *Artificial Hivemind* found strong repetition within one language model and homogeneity across different models [@jiang2025hivemind], and reinforcement learning with verifiable rewards can make a model's outputs *less* diverse than its base model at large sample counts [@yue2025].
- A 2026 theoretical analysis locates the ceiling in fixed vocabularies and fixed verifiers [@cao2026], and a replication of the classic Picbreeder experiment with vision-language models in place of people produced outputs that "differ clearly" from the human baseline [@earle2026].

> **Key insight:** The open-ended systems that work in 2026 are open-ended *within* a well-designed search space with an external verifier: a benchmark, a proof checker, a production metric. Nothing yet invents its own space and keeps it interesting indefinitely.
