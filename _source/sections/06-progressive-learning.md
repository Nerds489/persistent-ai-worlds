## 6. Progressive learning: forgetting, plasticity and memory

An agent that lives in a persistent world must keep learning for its whole life. Two different things go wrong.

### 6.1 Two failure modes, not one

**Catastrophic forgetting** is the old problem, named by McCloskey and Cohen in 1989: training a network on new data overwrites what it learned from old data [@mccloskey1989]. **Loss of plasticity** is the newer one, and the first edition did not mention it. Dohare and colleagues showed in *Nature* (August 2024) that standard deep-learning methods gradually lose the ability to learn at all when trained continually, "until they learn no better than a shallow network" [@dohare2024]. On a continual version of ImageNet, accuracy on new tasks reached about 88% early on and fell, by the 2,000th task, to "only slightly better than the linear network"; on permuted MNIST up to 25% of the units in a network were dead after 800 tasks, and around 60% with the Adam optimiser [@dohare2024]. Their conclusion: "methods based on gradient descent are not enough".

A persistent simulation is the hard case for both problems. Nobody tells the agent when one "task" ends and another begins, the world changes continuously, and the agent must learn for far longer than any benchmark.

### 6.2 What works, and what the first edition got wrong

**Table 5.** Continual-learning methods and how they fare in a persistent world.

| Method | Year | Mechanism | Use in a persistent simulation | Caveat |
|---|---|---|---|---|
| Experience replay | 2018 | Mix stored past experience into every update | The default baseline; a buffer that discards at random works almost as well as an unbounded one [@rolnick2019] | Storage |
| Elastic weight consolidation (EWC) | 2017 | Penalise changes to weights important to earlier tasks, using the Fisher information [@kirkpatrick2017] | Protect a small set of core skills | Needs task boundaries; fails almost completely in class-incremental settings [@vandeven2022] |
| Progressive networks | 2016 | Add a new network column per task; freeze old ones [@rusu2016] | Discrete, known eras | Grows with every task; needs the task label at inference |
| Generative replay | 2017 | A generator replays synthetic past data [@shin2017] | Replay internal representations, not raw inputs [@vandeven2020] | The basic version fails on natural images |
| GEM / A-GEM | 2017 / 2019 | Constrain each update so loss on stored examples cannot rise [@lopezpaz2017; @chaudhry2019] | Small per-agent memories | GEM's cost grows with tasks |
| Continual backpropagation | 2024 | Re-initialise a small fraction of low-utility units continually [@dohare2024] | Learners that run for a lifetime | Extra hyperparameters; little gain in some environments |
| L2, shrink-and-perturb, resets, ReDo | 2020-2023 | Keep weights small or near initialisation; recycle dead units [@ash2020; @nikishin2022; @sokar2023] | Cheap scheduled maintenance | Results vary by environment |

The evidence favours **replay** above everything else. In a large comparison, "parameter regularization methods such as EWC and SI fail almost completely, even on Split MNIST" in the class-incremental setting, and replay was "the only strategy among the top performers in all three scenarios" [@vandeven2022]. Plasticity fixes are cheap but transfer unreliably: continual backpropagation, L2 regularisation and shrink-and-perturb preserved plasticity "apparently indefinitely" in Dohare's experiments [@dohare2024], and layer normalisation plus weight decay is "highly effective" [@lyle2024], yet in the open-ended AgarCL environment the same fixes gave little improvement [@mohamed2025agarcl], and in the 2026 Forager benchmark only L2-to-initialisation helped consistently, with better *state construction* the most useful intervention of all [@forager2026]. Evaluation is also scaling up: the MEAL benchmark (ICML 2026) runs sequences of 100 tasks on one GPU and shows failures that the usual 3 to 10-task sequences hide [@meal2026].

The first edition said that population-based evolution "sidesteps the problem entirely". It does not. Individuals that never learn during their lives avoid forgetting only because they never learn; evolved networks that *do* learn still forget, and Ellefsen and colleagues needed both modular networks and neuromodulation to reduce it, calling neuromodulation "a necessary, but not sufficient" ingredient [@ellefsen2015].

### 6.3 Evolution outside, learning inside

The first edition's central design recommendation, evolution as an outer loop and learning as an inner loop, has strong support:

- Learning makes evolution faster: Hinton and Nowlan's 1987 demonstration of the Baldwin effect [@hinton1987].
- Evolution can choose starting weights that make lifetime learning fast [@fernando2018].
- A population that evolves each agent's internal reward produced human-level Capture the Flag players (Section 2.2) [@jaderberg2019].
- Deep evolutionary reinforcement learning (DERL) evolved body shapes that learn faster, a morphological Baldwin effect [@gupta2021].
- DiscoRL (*Nature*, October 2025) used a population of agents to *discover* a reinforcement-learning update rule that outperformed every hand-designed rule on Atari [@oh2025disco].

The right reading is that evolution *shapes the learner*: its rewards, its hyperparameters, its starting point, its body and even its learning rule. It does not replace replay or plasticity maintenance inside each lifetime.

### 6.4 Language models that keep learning

The 2025 to 2026 research on continual learning in language models changes *where* learning happens:

- **At test time.** *Titans* (Google, December 2024) adds a neural memory updated during use, driven by how surprising each input is [@behrouz2025titans]. *Nested Learning* and its *Hope* architecture (NeurIPS 2025) stack memories that update at different speeds, from fast to slow [@behrouz2025nested]. TTT-E2E (December 2025) writes its context into its own weights by training on it as it reads [@tttE2E].
- **In sparse slots.** *Sparse memory finetuning* (2025) updates only the memory-layer entries most activated by new data, cutting the drop in prior knowledge from 89% (full fine-tuning) and 71% (LoRA) to 11% [@lin2025sparse].
- **From its own outputs.** *SEAL* (MIT, 2025) has the model write its own training data and learn from it [@zweiger2025seal]; *RL's Razor* (2025) found that forgetting tracks how far a model's behaviour drifts from where it started, and that learning from the model's own outputs keeps the drift small [@shenfeld2025].

All of this is research-scale: Hope was tested at 760 million and 1.3 billion parameters, SEAL on 1 and 7 billion. Frontier labs talked about continual learning throughout 2026 without shipping it. In January Demis Hassabis said "that technique has not been cracked yet" [@hassabis2026]; in February Dario Amodei put "a good chance that in the next year or two, we also solve that" [@amodei2026]. No primary source shows a frontier model that updates its weights from its own deployment as of October 2026.

### 6.5 Memory without weight updates

For agents built on language models, the practical answer in 2026 is still *external memory*: the model's weights stay fixed, and the agent reads and writes a store. The reference designs remain Generative Agents' memory stream with reflection (Section 4.1) [@park2023] and Voyager's library of code skills, which "alleviates catastrophic forgetting" [@wang2023voyager]. Newer systems manage memory like an operating system (MemGPT, now Letta) [@packer2023], extract and consolidate facts (Mem0) [@chhikara2025], keep a time-aware knowledge graph (Zep) [@rasmussen2025], or consolidate offline between sessions, which Letta calls *sleep-time compute* and which cut the compute needed at answer time by about five times [@lin2025sleep].

> **Caution:** Memory benchmarks are disputed. Zep contests Mem0's LoCoMo evaluation (75.1% against 66.9% by Zep's count) [@zepvsmem0]; an agent with nothing but file-system tools scored 74.0% on the same test [@lettabench]; and two 2026 benchmarks found plain in-context learning and long-context baselines "highly competitive" with dedicated memory systems [@clbench2026; @evomembench2026]. Do not choose a memory system from a leaderboard.

Silver and Sutton describe the destination: "Agents will inhabit streams of experience, rather than short snippets of interaction" [@silver2025era]. A persistent simulation is exactly such a stream, which is why it is a good place to test any of these methods.
