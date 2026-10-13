#!/usr/bin/env bash
# Section 7 experiment driver. Runs conditions one after another, 16 seeds each, 16 processes at a time.
#
#   ./drive.sh base none half          the three E1/E2 arms at their table years
#   ./drive.sh base:3000               carry base on for another 3,000 years (resumes its checkpoints)
#
# Every condition is one change against the stock defaults. The two ford arms live in sibling folders
# holding a one-line edit each, so nothing ever edits code under a running experiment.
set -uo pipefail
cd "$(dirname "$0")"
HERE=$(pwd)
LOG=$HERE/driver.log

spec() {                                  # spec <id>  ->  folder|years|options
  case $1 in
    base)  echo ".|2000|" ;;
    none)  echo ".|2000|--inherit none" ;;
    half)  echo ".|2000|--inherit half" ;;
    calm)  echo ".|2000|--no-events" ;;
    e20k)  echo ".|2000|--energy 20000" ;;
    e45k)  echo ".|2000|--energy 45000 --capacity 3000" ;;
    big)   echo ".|2000|--size 128 --energy 53000 --capacity 3500" ;;
    ford1) echo "../experiment-s7-ford1|2000|" ;;
    wall)  echo "../experiment-s7-wall|2000|" ;;
    *)     echo "" ;;
  esac
}

for arg in "$@"; do
  id=${arg%%:*}
  s=$(spec "$id")
  if [ -z "$s" ]; then echo "$(date '+%F %T')  SKIP unknown condition: $id" >> "$LOG"; continue; fi
  folder=${s%%|*}; rest=${s#*|}; years=${rest%%|*}; opts=${rest#*|}
  case $arg in *:*) years=${arg#*:} ;; esac
  echo "=== $(date '+%F %T')  START $id  (16 seeds x $years years, folder $folder, options: ${opts:-none})" >> "$LOG"
  ( cd "$folder" && JOBS=16 ./run_seeds.sh 16 "$years" "$id" $opts ) >> "$LOG" 2>&1
  rc=$?
  echo "=== $(date '+%F %T')  DONE  $id  rc=$rc" >> "$LOG"
done
echo "=== $(date '+%F %T')  DRIVER FINISHED: $*" >> "$LOG"
