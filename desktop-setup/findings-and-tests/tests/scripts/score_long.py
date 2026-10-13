#!/usr/bin/env python3
"""Numbers for the third pre-registration (L1-L8) at a given year, default 10,000."""
import csv, glob, math, statistics as st, sys
Y = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
ARMS = {'base': 'runs/base', 'none': 'runs/none',
        'ford1': 'runs/ford1', 'wall': 'runs/wall'}
data = {a: [list(csv.DictReader(open(f))) for f in sorted(glob.glob(d + '/seed-*/log.csv'))] for a, d in ARMS.items()}
def win(rows, col, y=Y, n=100):
    v = [float(r[col]) for r in rows if y - n < int(r['year']) <= y and r[col] != '']
    return st.mean(v) if v else float('nan')
def arm(a, col, y=Y): return [win(r, col, y) for r in data[a]]
def welch(x, z):
    return (st.mean(x) - st.mean(z)) / math.sqrt(st.variance(x) / len(x) + st.variance(z) / len(z))
def ms(x): return f'{st.mean(x):.4f} +/- {st.stdev(x)/math.sqrt(len(x)):.4f}'
print('reached year:', {a: min(int(r[-1]['year']) for r in data[a]) for a in data})
print('\nBaldwin ratio copy/none gene_alpha by checkpoint')
for y in (300, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000):
    c, n = arm('base', 'gene_alpha', y), arm('none', 'gene_alpha', y)
    if any(math.isnan(v) for v in c + n): continue
    print(f'  {y:5d}  copy {st.mean(c):.4f}  none {st.mean(n):.4f}  ratio {st.mean(c)/st.mean(n):.2f}  t {welch(c, n):.2f}')
for col in ('gene_eps', 'q_states', 'policy_complexity', 'signal_entropy', 'population', 'max_generation'):
    c, n = arm('base', col), arm('none', col)
    print(f'  {col:18s} copy {ms(c)}  none {ms(n)}  t {welch(c, n):.2f}')
print('\nL2 none gene_alpha', ms(arm('none', 'gene_alpha')), ' none signal_entropy', ms(arm('none', 'signal_entropy')))
print('L3 base signal_entropy', ms(arm('base', 'signal_entropy')))
gap = lambda a: [abs(win(r, 'pop_west') - win(r, 'pop_east')) / win(r, 'population') for r in data[a]]
print('L4 base bank_gap', ms(gap('base')))
print('L5 base population', ms(arm('base', 'population')), ' max_generation', ms(arm('base', 'max_generation')))
print('\nL6/L7 dialect_jsd by checkpoint')
for y in range(2000, Y + 1, 1000):
    print(f'  {y:5d}', '  '.join(f'{a} {st.mean(arm(a, "dialect_jsd", y)):.4f}' for a in ('base', 'ford1', 'wall')))
w, b = arm('wall', 'dialect_jsd'), arm('base', 'dialect_jsd')
print('  wall vs base t', round(welch(w, b), 2), ' wall seeds above 0.10:', sum(v > 0.10 for v in w))
print('\nL8 survival')
for a in data:
    rr = [[r for r in rows if int(r['year']) <= Y] for rows in data[a]]
    print(f'  {a:5s} min pop {min(min(int(r["population"] or 0) for r in s) for s in rr)}'
          f'  min bank {min(min(min(int(r["pop_west"] or 0), int(r["pop_east"] or 0)) for r in s) for s in rr)}')
