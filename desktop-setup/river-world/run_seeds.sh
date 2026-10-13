#!/usr/bin/env bash
# Run many seeds of river_world.py side by side, one process per physical core.
#
#   ./run_seeds.sh                          16 seeds, 1,000 years each, into runs/main/
#   ./run_seeds.sh 16 1000 darwin --inherit none
#   ./run_seeds.sh 16 1000 main             run again: every seed carries on for another 1,000 years
#
# Arguments: seeds, years, run name, then any river_world.py options (values without spaces).
# JOBS=n overrides the parallelism. Options such as --inherit only apply when a seed's world is created.
set -euo pipefail
cd "$(dirname "$0")"
SEEDS=${1:-16}
YEARS=${2:-1000}
NAME=${3:-main}
shift $(( $# < 3 ? $# : 3 ))
export EXTRA="$*" YEARS NAME
# one process per physical core: the second thread of each core adds little to NumPy work like this
JOBS=${JOBS:-$(( $(nproc) / 2 > 0 ? $(nproc) / 2 : 1 ))}
# keep NumPy single-threaded inside each process, so the processes do not fight over cores
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
mkdir -p "runs/$NAME"
echo "$(date '+%F %T')  $SEEDS seeds x $YEARS years -> runs/$NAME  ($JOBS at a time)  options: ${EXTRA:-none}"
seq 1 "$SEEDS" | xargs -P "$JOBS" -I{} sh -c \
  'nice -n 5 python3 river_world.py --years "$YEARS" --seed {} --dir "runs/$NAME/seed-{}" $EXTRA >> "runs/$NAME/seed-{}.out" 2>&1; tail -n 1 "runs/$NAME/seed-{}.out"' \
  || echo "warning: at least one seed stopped with an error; read its runs/$NAME/seed-N.out" >&2
python3 summarise.py "runs/$NAME"
