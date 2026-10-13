#!/usr/bin/env bash
# Block until a milestone, or bail out loudly if the programme stalls (no simulations running, not finished).
#   ./watch_until.sh e3        every base seed at year >= 5,000 (E3 is then complete at 5,000)
#   ./watch_until.sh done      the 10K PROGRAMME FINISHED line
cd "$(dirname "$0")"
idle=0
while true; do
  if [ "$1" = e3 ]; then
    m=$(for s in $(seq 1 16); do tail -1 runs/base/seed-$s/log.csv | cut -d, -f1; done | sort -n | head -1)
    [ "${m:-0}" -ge 5000 ] && { echo "E3 READY: every base seed past year 5,000 at $(date '+%-I:%M %p')"; exit 0; }
  fi
  grep -q "10K PROGRAMME FINISHED" driver.log && { echo "PROGRAMME FINISHED at $(date '+%-I:%M %p')"; exit 0; }
  if [ "$(ps -eo comm= | grep -cx python3)" -eq 0 ]; then idle=$((idle+1)); else idle=0; fi
  [ $idle -ge 5 ] && { echo "STALLED: no simulations for 10 minutes and not finished, at $(date '+%-I:%M %p')"; tail -5 driver.log; exit 2; }
  sleep 120
done
