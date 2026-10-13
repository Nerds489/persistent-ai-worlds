#!/usr/bin/env bash
# Carry conditions on to an exact target year, however far each seed happens to have got.
#
#   ./resume.sh 5000 ford1 wall base        take all three to year 5,000
#   ./resume.sh 5000 ford1                  just one
#
# river_world.py's --years is "years to run THIS TIME", not a target, and an interrupted programme
# leaves seeds at different years, so each seed gets its own top-up. Conditions given together run
# side by side, which the Section 11.1 measurement shows is 14% faster than running them in turn.
set -uo pipefail
cd "$(dirname "$0")"
TARGET=${1:?usage: ./resume.sh TARGET_YEAR condition [condition ...]}; shift
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LOG=$(pwd)/driver.log

folder() { case $1 in ford1|wall) echo "../experiment-s7-$1" ;; *) echo "." ;; esac; }

pids=()
for name in "$@"; do
  d=$(folder "$name")
  ( cd "$d" || exit 1
    todo=""
    for s in $(seq 1 16); do
      cur=$(tail -1 "runs/$name/seed-$s/log.csv" 2>/dev/null | cut -d, -f1)
      cur=${cur:-0}; [ "$cur" -eq "$cur" ] 2>/dev/null || cur=0
      left=$((TARGET - cur))
      [ "$left" -gt 0 ] && todo="$todo $s:$left"
    done
    if [ -z "$todo" ]; then echo "=== $(date '+%F %T')  $name already at or past year $TARGET" >> "$LOG"; exit 0; fi
    echo "=== $(date '+%F %T')  RESUME $name to year $TARGET:$todo" >> "$LOG"
    echo $todo | tr ' ' '\n' | xargs -P 16 -I{} sh -c '
      s=${0%%:*}; y=${0##*:}
      nice -n 5 python3 river_world.py --years "$y" --seed "$s" --dir "runs/'"$name"'/seed-$s" >> "runs/'"$name"'/seed-$s.out" 2>&1
      tail -n 1 "runs/'"$name"'/seed-$s.out"' {}
    echo "=== $(date '+%F %T')  DONE  $name at year $TARGET" >> "$LOG"
    python3 summarise.py "runs/$name" > /dev/null 2>&1 || true
  ) &
  pids+=($!)
done
for p in "${pids[@]}"; do wait "$p"; done
echo "=== $(date '+%F %T')  RESUME FINISHED: $* to year $TARGET" >> "$LOG"
