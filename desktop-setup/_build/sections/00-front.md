# River World on the Desktop

**A setup paper: Scenarios A and B in one sealed world, with a river down the middle.** 11 October 2026.

Lachlan Bremner (Nerds489). DOI: [10.5281/zenodo.23337944](https://doi.org/10.5281/zenodo.23337944). The text and figures are licensed under CC BY 4.0, the code under the MIT License.

<!-- cover -->

## About this paper

The research paper *Running Persistent AI Worlds* (second edition, 10 October 2026) ran two scenarios on a laptop: two learning agents in a forest that never ends (Scenario A), and an evolving population sealed in a box with a fixed amount of energy (Scenario B). This paper joins them into one world, adds a river, and sets it up to run for days on the Ryzen 9 5950X desktop.

- **A new simulation, tested.** `river_world.py` puts Scenario A's learning agents inside Scenario B's sealed, evolving population, on a cylinder of land split by a river that carries nutrients and can be crossed only at three fords. Energy is conserved and checked every tick; a stopped run resumes exactly where it left off (Appendix B).
- **A setup for sixteen cores.** One process per core, one seed per process, a launcher, a summariser and a map tool (Sections 3 to 5).
- **A first experiment, measured.** Does it matter whether a child inherits what its parent learned? Four seeds of each, 300 simulated years, run on the laptop (Section 6).
- **What to do next.** Six experiments, one change each, and how to read the log (Sections 7 and 8); the RTX 3070's place in all this (Section 9); and a checklist for a week-long run (Section 10).
- **The six experiments, run.** All six from Section 7, sixteen seeds each, 2,000 simulated years and 10,000 for the four still moving, on the desktop. Predictions written first and scored afterwards (Section 11).

Measured numbers in Sections 1 to 10 come from the laptop the paper was built on, and the desktop figures there are labelled as estimates. Section 11 was run on the desktop itself and replaces those estimates with measurements.

## Contents

1. [The desktop](#1-the-desktop)
2. [River world: Scenarios A and B in one world](#2-river-world-scenarios-a-and-b-in-one-world)
3. [Install](#3-install)
4. [First run: four checks](#4-first-run-four-checks)
5. [Running sixteen seeds](#5-running-sixteen-seeds)
6. [The first experiment: should learning be inherited?](#6-the-first-experiment-should-learning-be-inherited)
7. [Experiments to run next](#7-experiments-to-run-next)
8. [Reading the log](#8-reading-the-log)
9. [Using the RTX 3070](#9-using-the-rtx-3070)
10. [Before a week-long run](#10-before-a-week-long-run)
11. [The six experiments, run](#11-the-six-experiments-run)
- [Appendix A: Parameters](#appendix-a-parameters)
- [Appendix B: How the kit was tested](#appendix-b-how-the-kit-was-tested)
- [References](#references)

<div class="kpis">
<div class="kpi"><b>30,000</b><span>energy units in the world, never created or destroyed, checked 400 times a simulated year</span></div>
<div class="kpi"><b>3 fords</b><span>the only way across the river; the world wraps north to south and is walled east to west</span></div>
<div class="kpi"><b>16 seeds</b><span>at once on the 5950X: one process per physical core, about 80 MB each</span></div>
<div class="kpi"><b>0.18 vs 0.05</b><span>learning rate after 300 years with learning inherited, and without: evolution turns learning down when it is not passed on (Section 6). By year 2,000 and sixteen seeds the gap is 0.06 against 0.03, and by year 10,000 0.039 against 0.033: the gap was a matter of speed, not destination (Section 11)</span></div>
<div class="kpi"><b>70 → 21</b><span>energy needed to reproduce, at the start and after 300 years: evolution chose many small, hungry agents (Section 6)</span></div>
<div class="kpi"><b>identical</b><span>a stopped and resumed run matches an uninterrupted one, byte for byte (Appendix B)</span></div>
</div>
