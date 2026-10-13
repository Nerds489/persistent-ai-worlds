#!/usr/bin/env bash
# The 10,000-year programme, two conditions at a time (32 processes: the measured optimum;
# 64 processes ran at 15.56 years/s against 20.15). Ordered so E3 is complete at year 5,000 first.
cd "$(dirname "$0")"
./resume.sh 5000  ford1 wall &&
./resume.sh 10000 base none  &&
./resume.sh 10000 ford1 wall
echo "=== $(date '+%F %T')  10K PROGRAMME FINISHED" >> driver.log
