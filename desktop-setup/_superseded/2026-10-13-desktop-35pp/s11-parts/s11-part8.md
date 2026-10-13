### 11.9 What this section does not show

**Everything here is about river world.** Nine conditions on one simulation with one parameter set. The
Baldwin-style result in 11.2 is a fact about these agents in this world, as Section 6 said of its own;
nothing here generalises to learning and evolution in anything else.

**Where you stop decides what you find.** That is the sharpest lesson of 11.2 and 11.7. The
learning-rate ratio peaks at 3.7 near year 300, is 1.7 by year 2,000 and 1.2 by year 10,000. Stopped at
300 it is a large permanent effect; stopped at 10,000 it is a difference in speed. Even 10,000 years is
one horizon: the inheriting world's standing crop and body energy were still rising when it stopped.
A measurement at one horizon is a measurement at one horizon.

**Sixteen seeds and twenty-two columns means some of these *t* values are chance.** Each comparison in
this section tests about twenty-two columns at once. With |*t*| above 2 as the bar, roughly one column
a comparison will clear it by luck alone. Everything claimed here as a result sits above |*t*| = 4, and
most above 6; the numbers quoted near 2, such as the archive in Table 9 or behaviour diversity in
Table 12, are noted but not leaned on.

**The measures are cruder than the numbers look.** `novelty` reaches exactly 0 by year 300 in every arm
and stays there, with the archive saturated around 750 of its 2,048 cells, so it discriminates nothing
after the first few centuries. `q_states` counts a visited flag and, as Table 10 shows, that flag can
outlive the knowledge behind it entirely. `ecology_entropy` and `archive_size` both inherit the same
six-part descriptor, and Section 7.2's warning about it stands: these are the observer, and a better
observer would see a different world.

**Two arms are not quite the same program.** `ford1` and `wall` each differ from the shipped kit by one
line. The terrain was checked, and nothing else in those folders differs, but they are copies and
should be read as such.

**E4 is unanswered rather than answered.** The null in 11.4 is a fact about disturbances that touch a
0.1% of the energy budget. It says nothing about whether disturbance would matter if it
were large enough to notice.

**And the most useful warning of the lot:** check what a treatment does in the code before building an
experiment on its name. `--inherit half` sounds like a halfway point between the other two arms, and
E1 added it on that basis. It is not one. One line of reading would have caught it before 31 minutes of
compute, and the only reason it became a result rather than a wasted arm is that the three arms
disagreed in a pattern strange enough to send us back to the source.
