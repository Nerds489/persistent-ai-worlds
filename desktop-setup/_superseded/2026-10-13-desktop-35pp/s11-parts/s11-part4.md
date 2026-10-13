### 11.4 E4: does disturbance keep the world interesting?

![Figure 6. Disturbance, energy and size, sixteen seeds an arm over 2,000 simulated years. Top left: switching fires, floods and droughts off changes nothing measurable (11.4). Top right and bottom left: population tracks total energy more than proportionally while the nutrients standing on the land do not move at all (11.5). Bottom right: a world nearly twice the size explores barely more behaviours (11.6).](figures/fig-s7-world.svg)

No. Not as the three disturbances are currently sized.

`calm` is the defaults with `--no-events`. Against `base` at year 2,000, sixteen seeds a side, every
measure in the log falls inside seed noise. The largest |*t*| among the twenty-two columns is 1.9, and
the two that come closest both point the wrong way for the hypothesis: the calm world has slightly
*more* behaviour diversity (5.00 against 4.81 bits, *t* = −1.6) and slightly *more* structured
signalling (1.859 against 1.828 bits, *t* = −1.9). Population, lineage depth, the five genes, the
archive and `change` are all flat. The only column that separates is the treatment itself: 1,037 events
in 2,000 years against 0.

That is a negative result, so it is worth showing that the instrument was not asleep. Two checks inside
`base` itself:

- **Years with an event look like years without.** Over years 500 to 2,000 and sixteen seeds, the annual
  change in population averages +0.060% in the 12,485 year-slots carrying an event and −0.029% in the
  11,515 that do not, with standard deviations of 1.540 and 1.536.
- **Events add no volatility.** The standard deviation of the annual change, `base` against `calm`:
  population 1.537 against 1.521, nutrients 2.287 against 2.252, detritus 0.417 against 0.406, mean
  energy 6.407 against 6.291. Ratios of 1.01 to 1.03. The two columns that move at all, `q_states` at
  1.19 and signal entropy at 1.11, are the smallest numbers on the list in absolute terms.

The reason is arithmetic, and it is in the pools the events touch. A fire burns a disc of radius 6, so
about 113 of the world's 8,494 land cells. It moves the nutrients under that disc into detritus, about
60 of the 4,544 units on land, which decay back at 5% a tick; and it takes half the body energy of the
agents standing in it, about fifteen agents holding about 0.45 each, so roughly 3 units. Floods and
droughts change erosion, flow and deposition for 40 and 100 ticks, and all three of those act on the
river's load, which holds **24 units of the world's 30,000**. Every disturbance in the model is working
on 0.1% of the world's energy, in a world where 25,000 of the 30,000 units sit in
detritus and are rained back onto the land continuously.

So E4's question is not answered by this run; it is deferred until the disturbances are large enough to
answer it. A rerun worth doing on the desktop: scale fire's radius with the world (radius 20 burns 12%
of the land rather than 1.3%), make drought suppress decomposition rather than river flow, since
decomposition is the pipe the whole world feeds through, and only then compare against `calm`. The
prediction to write first is the one this run can already falsify: that a disturbance confined to 0.1%
of the energy budget cannot move a population of 1,100.
