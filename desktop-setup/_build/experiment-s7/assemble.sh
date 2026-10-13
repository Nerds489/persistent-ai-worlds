#!/usr/bin/env bash
# Fold Section 11 into the paper and rebuild both PDFs. Idempotent: safe to run again.
set -euo pipefail
cd "$(dirname "$0")"
B=..
S=$B/sections

cat s11-part1.md s11-part2.md s11-part3.md s11-part4.md s11-part5.md s11-part6.md s11-part6b.md s11-part7.md s11-part8.md \
  > "$S/11-six-experiments.md"

# the appendices must sort after the new section
[ -f "$S/11-appendices.md" ] && mv "$S/11-appendices.md" "$S/12-appendices.md"

python3 - <<'PY'
import re, io
p = "../sections/00-front.md"
s = io.open(p, encoding="utf-8").read()

# 1. a bullet for the new section
bullet = ("- **The six experiments, run.** All six from Section 7, sixteen seeds each, 2,000 simulated years and 10,000 "
          "for the four still moving, on the desktop. Predictions written first and scored afterwards (Section 11).\n")
if "The six experiments, run.**" not in s:
    anchor = "- **What to do next.**"
    i = s.index(anchor)
    j = s.index("\n", s.index("(Sections 7 and 8)", i)) + 1
    s = s[:j] + bullet + s[j:]

# 2. the laptop/desktop caveat is no longer the whole story
s = s.replace(
 "Measured numbers come from the laptop the paper was built on; numbers for the desktop are labelled as estimates.",
 "Measured numbers in Sections 1 to 10 come from the laptop the paper was built on, and the desktop figures there are "
 "labelled as estimates. Section 11 was run on the desktop itself and replaces those estimates with measurements.")

# 3. the contents
if "#11-the-six-experiments-run" not in s:
    s = s.replace("10. [Before a week-long run](#10-before-a-week-long-run)\n",
                  "10. [Before a week-long run](#10-before-a-week-long-run)\n"
                  "11. [The six experiments, run](#11-the-six-experiments-run)\n")

# 4. the front-page figure that Section 11 revises
s = s.replace(
 "<div class=\"kpi\"><b>0.18 vs 0.05</b><span>learning rate after 300 years with learning inherited, and without: "
 "evolution turns learning down when it is not passed on (Section 6)</span></div>",
 "<div class=\"kpi\"><b>0.18 vs 0.05</b><span>learning rate after 300 years with learning inherited, and without: "
 "evolution turns learning down when it is not passed on (Section 6). By year 2,000 and sixteen seeds the gap is "
 "0.06 against 0.03, and by year 10,000 0.039 against 0.033: the gap was a matter of speed, not destination (Section 11)</span></div>")

io.open(p, "w", encoding="utf-8").write(s)
print("front matter updated")
PY

cd "$B"
python3 build_paper.py out screen 2>&1 | grep -v "^WARNING unused refs:"
python3 build_paper.py out print  2>&1 | grep -v "^WARNING unused refs:"
cp -f figures/*.svg figures/*.png ../figures/ 2>/dev/null || true
cp -f out/paper.md       ../River-World-Desktop-Setup.md
cp -f out/paper.pdf      ../River-World-Desktop-Setup.pdf
cp -f out/paper-print.pdf ../River-World-Desktop-Setup_print.pdf
echo
ls -l ../River-World-Desktop-Setup.md ../River-World-Desktop-Setup.pdf ../River-World-Desktop-Setup_print.pdf
