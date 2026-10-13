## 1. The desktop

This paper is written for one machine: the Ryzen desktop running Linux Mint 22.3. Its parts decide how the work is split. The simulation itself is NumPy on the CPU, one process per seed, so the sixteen cores are the engine. The graphics card is for the optional GPU stages in Section 9, and the memory and disks are simply never the constraint.

**Table 1.** The desktop and what each part does in this setup.

| Part | Specification | Role here |
|---|---|---|
| CPU | AMD Ryzen 9 5950X, 16 cores / 32 threads, boost to 4.9 GHz | Sixteen seeds at once, one per physical core |
| Memory | 64 GB DDR4-3200 (2 × 32 GB, dual rank) | About 80 MB per seed: sixteen seeds use about 1.3 GB |
| GPU | NVIDIA GeForce RTX 3070 LHR, 8 GB | Optional: JAX environments and a local language model (Section 9) |
| Motherboard | Gigabyte B550M DS3H AC | |
| Operating system | Linux Mint 22.3 (Ubuntu 24.04 base), kernel 7.0.0-38 | Python 3.12 from the distribution |

Three consequences follow.

1. **Seeds, not threads.** One river world is a single-threaded Python loop over NumPy arrays. It cannot use sixteen cores for one world, but sixteen independent worlds use them perfectly. That suits the science too: a result that holds in one seed is an anecdote; one that holds in twelve of sixteen is a finding.
2. **Physical cores, not threads.** The 5950X shows 32 logical CPUs, but its second thread per core adds only 14% to this kind of arithmetic (measured in Section 11.1). The launcher therefore runs `nproc / 2` = 16 processes per condition and pins NumPy to one thread each so they do not compete; to use the second threads, run a second condition alongside, and never more processes than threads.
3. **Heat, not memory, is the limit for week-long runs.** Sixteen busy cores hold the 5950X at its all-core power limit for days. Watch `sensors` for the first hour (Section 5.3); the chip's limit is 90 °C. Measured, it held 49 to 51 °C (Section 11.1).

> **Note:** Every timing in this paper was measured on the laptop the paper was built on (Intel Core i7-8665U, 4 cores, 16 GB). Figures for the desktop are estimates until you run the smoke test in Section 4, which takes a minute and replaces them with your own numbers.
