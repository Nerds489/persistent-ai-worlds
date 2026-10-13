## 10. Before a week-long run

1. **Prediction written down** in `runs/<name>/PREDICTION.md`, with numbers.
2. **Smoke test passed** on this machine today (Section 4), including the resume check.
3. **One change per condition**, each condition in its own folder, 16 seeds each.
4. **Launcher inside `tmux`** (Section 5.4), so a closed terminal does not stop it.
5. **Temperatures watched for the first hour** (Section 5.3); `JOBS=12` if the CPU runs hot.
6. **Disk checked:** `df -h ~` shows at least 2 GB free for 16 seeds.
7. **The code frozen:** no edits to `river_world.py` while its worlds are running (Section 7).
8. **Summarise daily:** `python3 summarise.py runs/A runs/B` takes a second and changes nothing.
9. **Snapshot weekly,** or whenever a column does something odd: `python3 snapshot.py runs/A/seed-3`.
10. **Copy any checkpoint worth keeping** before the run overwrites it.
11. **After a reboot,** run the same `./run_seeds.sh` line again: every seed resumes.
12. **At the end,** keep the logs, the summaries and the prediction together, and write one paragraph on what was right and what was wrong.
