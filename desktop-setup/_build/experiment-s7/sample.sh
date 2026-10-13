#!/usr/bin/env bash
# Total simulated years across every live run, sampled twice, to measure aggregate throughput.
cd "$(dirname "$0")"
total() { for d in runs/*/seed-*/log.csv ../experiment-s7-ford1/runs/*/seed-*/log.csv ../experiment-s7-wall/runs/*/seed-*/log.csv; do
    [ -f "$d" ] && tail -1 "$d" | cut -d, -f1; done | paste -sd+ | bc; }
a=$(total); t0=$(date +%s); sleep "${1:-120}"; b=$(total); t1=$(date +%s)
echo "procs=$(pgrep -c -f 'python3 river_world.py')  years $a -> $b over $((t1-t0))s  aggregate $(echo "scale=2; ($b-$a)/($t1-$t0)" | bc) simulated years/s"
