## Appendix A: Parameters

All of these are constants or options in `river_world.py`. Options can be set on the command line; constants need an edit (in a copy, Section 7).

**Table A1.** River world's parameters and their defaults.

| Parameter | Default | Where |
|---|---|---|
| World size | 96 × 96 cells, wrapping north to south, walled east and west | `--size` |
| Total energy | 30,000 units, conserved | `--energy` |
| Agent capacity | 2,000 at once | `--capacity` |
| Starting population | 300 agents, 40 energy each, on random land cells | `World.__init__` |
| Terrain | rock 5% of cells, clearings 22%, forest the rest; the river is carved through them | `World.__init__` |
| River | 3 cells wide; centre swings up to about 11 cells either side; fords at rows 16, 48 and 80, three rows deep | `World.__init__` |
| Time | day 20 ticks (night is the last 8); season 100 ticks; year 400 ticks | `DAY`, `SEASON`, `YEAR` |
| Costs | rest 0.5, move 0.9, ×1.25 at night, +0.05 to send a signal | `World.step` |
| Eating | up to 4 a tick; at most 150 held | `FEED`, `MAX_E` |
| Decomposition | 5% (forest), 3.5% (clearing), 2% (ford) of detritus a tick; ×1.2 spring, ×1.0 summer, ×0.8 autumn, ×0.4 winter | `World.step_environment` |
| Diffusion | 2% of a cell's nutrients a tick to each land neighbour | `World.step_environment` |
| River | erosion 0.2% of bank nutrients a tick; 20% of each row's load moves one row south a tick; 1% of the load settles as silt a tick, ×2.5 in spring | `World.step_environment` |
| Flood | 25% chance each spring; 40 ticks of 6× silt and 3× erosion | `World.maybe_event` |
| Drought | 15% chance each summer; 100 ticks of the river at a quarter of its flow and silt | `World.maybe_event` |
| Fire | 12% chance at the start of summer and of autumn; radius 6; nutrients become detritus; agents in it lose half their energy | `World.maybe_event` |
| Learning | tabular Q-learning, 240 states × 20 actions, discount 0.95, reward = change in energy, random tie-breaks | `World.step` |
| Starting genes | lifespan 1,200 ticks, reproduce above 70 energy, mutation scale 0.05, learning rate 0.2, exploration 0.1 | `World.__init__` |
| Mutation | each gene moves by a normal step × (mutation scale ÷ 0.05) × 80 ticks, 8 energy, 0.01, 0.05 and 0.03 respectively, within fixed limits | `G_SCALE`, `G_MIN`, `G_MAX` |
| Inheritance | the parent's Q-table is copied to the child | `--inherit copy`, `half` or `none` |
| Checkpoint | every 10 years, and on exit | `--save-every` |

## Appendix B: How the kit was tested

Everything below was run on the laptop before this paper was written, and every test passed in its final form.

- **Energy.** Conservation is asserted after every tick in every run. In the eight 300-year runs of Section 6 the largest end-of-year drift was 3.1 × 10⁻⁸ energy units, about one part in 10¹² of the total.
- **Resume.** A run stopped and resumed produced a log byte-identical to an uninterrupted run in four cases: stopped at a year boundary; stopped part-way through a year; stopped with Ctrl-C at year 8 of 20; and killed outright with `kill -9` after its last checkpoint, where the resumed run trimmed the one log row written after the checkpoint and carried on.
- **Symmetry.** A world and its exact mirror image, left for right, were run side by side. The first version of the code favoured the east bank, by between three and seven to one, because untried actions were chosen in index order and east comes before west. Random tie-breaking removed the bias: which bank leads now varies with the seed and the mirror, as it should.
- **Review.** A line-by-line review found seven defects in the first version, all fixed and re-tested: an interrupted run skipped the seasonal event roll and could not resume exactly; the signal colouring of maps was always blank; maps of extinct worlds crashed; one failed seed stopped the summary; extinct seeds were hidden in the summary; a log row still being written crashed it; and a hard kill could leave duplicate rows in the log.
- **Tools.** `run_seeds.sh`, `summarise.py` and `snapshot.py` were run on real and on deliberately extinct worlds.
