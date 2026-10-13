#!/usr/bin/env bash
# Does the 5950X's second thread per core buy anything on this workload?
# A: ford1 + wall together, 32 processes.  B: ford1 alone, 16 processes, wall frozen.
cd "$(dirname "$0")"
yrs() { for f in ../experiment-s7-$1/runs/$1/seed-*/log.csv; do tail -1 "$f" | cut -d, -f1; done | paste -sd+ | bc; }
wallpids() { for p in $(pgrep -f 'runs/wall/seed'); do [ "$(cat /proc/$p/comm 2>/dev/null)" = python3 ] && echo "$p"; done; }
W=180

f0=$(yrs ford1); w0=$(yrs wall); t0=$(date +%s)
sleep $W
f1=$(yrs ford1); w1=$(yrs wall); t1=$(date +%s); d=$((t1-t0))
A_f=$(echo "scale=3; ($f1-$f0)/$d" | bc); A_w=$(echo "scale=3; ($w1-$w0)/$d" | bc)
echo "A  32 processes (ford1 + wall), ${d}s:  ford1 $A_f + wall $A_w = $(echo "$A_f+$A_w"|bc) simulated years/s"

for p in $(wallpids); do kill -STOP "$p"; done
echo "   wall frozen: $(wallpids | wc -l) processes stopped at $(date '+%T')"
sleep 5
f0=$(yrs ford1); t0=$(date +%s)
sleep $W
f1=$(yrs ford1); t1=$(date +%s); d=$((t1-t0))
B_f=$(echo "scale=3; ($f1-$f0)/$d" | bc)
for p in $(wallpids); do kill -CONT "$p"; done
echo "   wall resumed at $(date '+%T')"
echo "B  16 processes (ford1 alone), ${d}s:  $B_f simulated years/s"
echo
echo "second-thread gain: $(echo "scale=3; ($A_f+$A_w)/$B_f" | bc)x aggregate throughput for 2x the processes"
