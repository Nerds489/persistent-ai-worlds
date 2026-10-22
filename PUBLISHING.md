# Publishing this work: step by step

Where the two papers in this repository can go, in the order to do it, and exactly how. Checked against each
venue's own pages on 13 October 2026; the links at the end of each part are the places to re-check, because
rules and dates change.

| Paper | What it is | Where it fits |
|---|---|---|
| *River World on the Desktop* (`desktop-setup/`) | Original research: six experiments, 144 runs, pre-registered predictions scored afterwards | Zenodo, arXiv, ALIFE conference, *Artificial Life* journal |
| *Running Persistent AI Worlds* (top level) | A review of the field, with two small reference simulations | Zenodo only for now (see Part 3, the arXiv rule on review articles) |
| The simulation kit (`desktop-setup/river-world/`) | 664 lines of Python | Zenodo with the paper; JOSS is a long shot (Part 6) |

## Where it stands (13 October 2026)

| Step | Status |
|---|---|
| ORCID | Done: [0009-0007-8818-4607](https://orcid.org/0009-0007-8818-4607) |
| Licences | Done for *River World on the Desktop*: text and figures CC BY 4.0, code MIT. *Running Persistent AI Worlds* still undecided |
| Zenodo record A, paper and kit | Published: [10.5281/zenodo.23338390](https://doi.org/10.5281/zenodo.23338390) ([record](https://zenodo.org/records/23338390)) |
| Zenodo record B, data | Published. Version 1 (logs and tests) [10.5281/zenodo.23338578](https://doi.org/10.5281/zenodo.23338578); version 2 adds every checkpoint, [10.5281/zenodo.23341715](https://doi.org/10.5281/zenodo.23341715) ([record](https://zenodo.org/records/23341715)). All versions: [10.5281/zenodo.23338577](https://doi.org/10.5281/zenodo.23338577) |
| Checkpoints | Done, in record B version 2 (22 October 2026): 152 checkpoints in 49 archives. Zenodo cut long uploads off with 502 errors, so large archives were split by seed until each uploaded in minutes |
| Repository public | Not yet |
| arXiv, ALIFE 2027, journal, JOSS | Not started |

The order:

1. **Before anything:** an ORCID iD, the licence, and the repository made public (Part 0).
2. **Zenodo**, for a DOI and a home for the data, the same day (Part 1).
3. **OSF**, only for the next experiment, before it runs (Part 2).
4. **arXiv**, once an endorser says yes (Part 3).
5. **ALIFE 2027** as an 8-page paper (Part 4), or the ***Artificial Life* journal** in full (Part 5).
6. **JOSS**, at the earliest six months after the code goes public (Part 6).

---

## Part 0: the groundwork (about an hour, once)

### 0.1 Get an ORCID iD

ORCID is a free, permanent ID for a researcher. Zenodo, arXiv, MIT Press and JOSS all use it, and it ties your
papers to you even when your name is written differently in each place.

1. Go to <https://orcid.org/register>.
2. Register with the name you want on the papers and a personal email (an ORCID survives job changes).
3. Set the visibility of your record to "Everyone".
4. Note the 16-digit iD (`0000-0000-0000-0000`). It goes on every paper's title page from now on.

### 0.2 Decide the byline

Each venue asks for an author name and an affiliation. With no institution, the usual form is
"Independent researcher" plus your city and country. Use the same name everywhere so the ORCID matches.

### 0.3 Choose the licences

Nothing in this repository has a licence yet, which means nobody else may legally reuse any of it. Run `/license`
first: it decides from the law store, never from memory. What it will be weighing:

- **The papers and figures:** a Creative Commons licence. CC BY 4.0 is the most widely accepted (every venue
  below takes it). CC BY-NC-SA 4.0, the Codex's licence, is also allowed on Zenodo and arXiv, but it blocks
  commercial reuse and some journals will not take it.
- **The code:** an open-source licence approved by the Open Source Initiative, such as MIT or Apache-2.0.
  Creative Commons licences are not meant for code, and JOSS requires an OSI licence.
- **The data** (logs, checkpoints): CC BY 4.0 or CC0.

The licence chosen on Zenodo and arXiv is permanent for that version, so settle it here, once.

### 0.4 Make this repository public (when ready)

It is private now. Zenodo's GitHub link, JOSS and readers all need it public. Going public runs through the
licence gate (`/workflow public-release`), which also scans the whole history for anything that should not go
out. The run logs contain local paths such as `/home/minty/...`; harmless, but the scan will show them.

---

## Part 1: Zenodo (do this first, same day)

Zenodo is run by CERN. It is free, has no gatekeeping or review, and gives every upload a DOI: a permanent,
citable identifier like `10.5281/zenodo.1234567` that works in any reference list. It also keeps the data.

**Limits:** 50 GB and 100 files per record. The river world's 152 checkpoints (144 from Section 11, 8 from Section 6) are 6.4 GB, so they fit by size but not by
count: pack them into archives first (step 1.4).

**Know this before pressing Publish:** a published record cannot be deleted by you, and its files cannot be
changed. Corrections are made by publishing a new version. Everything up to Publish can be edited freely.

### 1.1 Make an account

1. Go to <https://zenodo.org> and choose **Sign up**.
2. Sign up with **ORCID** (it links your iD automatically) or with GitHub.
3. Confirm the email.

### 1.2 Plan two records

Make two linked records rather than one, so the paper can be cited on its own and the data can grow:

| Record | Resource type | Files |
|---|---|---|
| A, the paper and code | Publication, then Preprint | Both PDFs, the Markdown, the kit (as a zip) |
| B, the data | Dataset | The run logs and test outputs archive, the checkpoint archives |

### 1.3 Reserve the DOIs first

Reserving lets you print the DOI inside the paper before it is published.

1. **New upload**, top right.
2. Under **Digital Object Identifier**, answer "No" to "Do you already have a DOI?", then **Get a DOI now!**
3. Copy the reserved DOI. Save the draft.
4. Repeat for record B.
5. Add both DOIs to the paper's title page and the "Data and code" note, rebuild the PDFs
   (`desktop-setup/_build/experiment-s7/assemble.sh`), and check the page counts are still 35 and 36.

### 1.4 Pack the files

From the repository's root folder:

```bash
mkdir -p ~/zenodo-upload
# Record A: the kit
cd desktop-setup && zip -r ~/zenodo-upload/river-world-kit.zip river-world && cd ..
# Record B: logs, scripts and tests (no checkpoints): the same archive filed in the Codex
tar -czf ~/zenodo-upload/river-world-logs-and-tests.tar.gz --exclude='*.pkl' desktop-setup/findings-and-tests
# Record B: checkpoints, one archive per experiment folder (well under 100 files in all)
for d in desktop-setup/_build/experiment*/runs/*/; do
  name=$(basename "$(dirname "$(dirname "$d")")")-$(basename "$d")
  tar -cf ~/zenodo-upload/checkpoints-$name.tar -C "$d" $(cd "$d" && find . -name checkpoint.pkl)
done
ls ~/zenodo-upload | wc -l      # must be at most 100
cd ~/zenodo-upload && sha256sum * > SHA256SUMS.txt
```

Checkpoints are Python pickles, and loading a pickle can run code. Say on the record's page that people should
load only files they have checked against `SHA256SUMS.txt`.

### 1.5 Fill in record A

1. Open the draft. Drag in the files.
2. **Resource type:** Publication, then Preprint.
3. **Title:** *River World on the Desktop: a persistent multi-agent world with a river, and six experiments on it*,
   or the paper's own title.
4. **Creators:** your name, with the ORCID iD and affiliation from Part 0.
5. **Description:** the abstract (copy the paper's opening summary).
6. **Licence:** the one chosen in 0.3.
7. **Keywords:** artificial life, multi-agent reinforcement learning, Q-learning, neuroevolution, open-endedness,
   pre-registration, Baldwin effect.
8. **Related works:** add record B's DOI with the relation "Is supplemented by". Once the repository is public,
   add its URL with the relation "Is supplemented by" too.
9. **Version:** `1.0`. **Language:** English.
10. **Preview**, read it as a stranger would, then **Publish**.

### 1.6 Fill in record B

The same as 1.5, except: resource type **Dataset**; the description says what each archive holds and how big it
unpacks; related works points back to record A with "Is supplement to".

### 1.7 Later: link GitHub for automatic DOIs

This works only once the repository is public (Zenodo cannot see private ones).

1. Zenodo, the profile menu, **GitHub**, **Sync now**.
2. Switch on `Nerds489/persistent-ai-worlds`.
3. Each GitHub release from then on is archived with its own DOI. Cutting a release goes through the licence gate.

### 1.8 Do the same for *Running Persistent AI Worlds*

One record, Publication then Preprint, with both PDFs, the Markdown and `sim/`. This is the right place for the
review paper while arXiv will not take it (Part 3).

Re-check: <https://help.zenodo.org>, <https://support.zenodo.org>.

---

## Part 2: OSF pre-registration (for the next experiment)

The strongest thing about the river world paper is that its predictions were written down before the runs. The
weak point is that the only proof of when is your own files. A registration on the Open Science Framework is a
frozen, timestamped copy held by someone else, which reviewers trust.

This cannot be done after the fact for the six experiments already run. Use it for the next batch:

1. Make an account at <https://osf.io> (ORCID sign-in works).
2. **Create project**, named for the experiment.
3. Upload the prediction file, written as `predictions.md` was: each prediction numbered, with the number that
   would prove it wrong.
4. **Registrations**, **New registration**, and pick the **OSF Preregistration** template. Answer its questions
   from the prediction file.
5. Choose an embargo if you do not want it public yet (up to four years; it opens itself at the end).
6. Submit. The registration is frozen and timestamped; you cannot edit it.
7. Only now start the runs. Cite the registration's DOI in the paper.

---

## Part 3: arXiv

arXiv is where most researchers in the field read new work first. It is a preprint server: moderated (a person
checks each paper is on topic and is research), not peer reviewed.

### What goes and what does not

- ***River World on the Desktop*: yes.** It is original research with new results.
- ***Running Persistent AI Worlds*: not yet.** Since 31 October 2025, arXiv's Computer Science section only takes
  review articles and position papers after a journal or conference has accepted them through peer review, with
  proof attached. It goes to Zenodo (Part 1.8) until a venue accepts it.

### 3.1 Get endorsed (the slow step: start now)

First-time submitters to a category need one endorsement from someone who has published enough in it recently.

1. Register at <https://arxiv.org/user/register>, and link your ORCID in the profile.
2. Start a new submission and choose the category **cs.NE** (Neural and Evolutionary Computing). arXiv then emails
   you an endorsement code and a link to send to an endorser.
3. Find an endorser. On the arXiv page of a recent paper the river world paper cites, or of a recent cs.NE
   paper on artificial life or open-endedness, click **"Which authors of this paper are endorsers?"**. Contact
   addresses are under **Submission history**.
4. Write to **one** person at a time, briefly: who you are, the paper's title and two-sentence result, the PDF or
   the Zenodo DOI, and the endorsement code. Do not send the same request to many people at once; arXiv treats
   that as spam.
5. If there is no answer after a week or two, try the next person.

### 3.2 Prepare the files

- arXiv prefers LaTeX source, but takes a **PDF made from something other than LaTeX**, which this one is (it is
  built from Markdown through Chrome). Upload `River-World-Desktop-Setup.pdf`, the screen edition.
- All fonts must be embedded: `pdffonts River-World-Desktop-Setup.pdf` must show `yes` in the `emb` column on
  every line.
- File names may contain only letters, digits and `_ + - . , =`.
- Figures must be inside the PDF; external links to figures are not accepted.

### 3.3 Submit

1. **Primary category:** cs.NE. **Cross-lists:** cs.MA (Multiagent Systems); cs.LG (Machine Learning) is
   optional.
2. **Licence:** the one chosen in 0.3. This is permanent for that version.
3. **Title and abstract:** plain text. Mathematics in the abstract is written as TeX (`$\alpha$`).
4. **Comments field:** `35 pages, 7 figures. Code and data: https://doi.org/10.5281/zenodo.XXXXXXX`
5. Check the preview arXiv builds, then submit.
6. **Timing:** submitted before 14:00 US Eastern, Monday to Friday, it is normally announced at 20:00 Eastern
   that day. In Western Australian time (AWST) that is a 02:00 cut-off and a 08:00 announcement the next
   morning while the US is on daylight saving, and an hour later otherwise.

### 3.4 After it is announced

- It can never be removed. A correction is uploaded as a replacement (version 2); version 1 stays visible.
- Before announcement, **Unsubmit** returns it to a draft for changes.
- Add the arXiv ID to the Zenodo record's related works (relation "Is identical to") and to the README.

Re-check: <https://info.arxiv.org/help/endorsement.html>, <https://info.arxiv.org/help/submit/index.html>,
<https://blog.arxiv.org/?p=1740> (the review-article rule).

---

## Part 4: the ALIFE 2027 conference

The yearly conference of the International Society for Artificial Life, and the natural audience for this work.
Accepted full papers are published open access by MIT Press with a DOI.

**ALIFE 2027:** Prague, Czech Republic, 19 to 23 July 2027. The call for papers and deadline are not out yet. Past
deadlines: 10 April 2024, 4 May 2025, 30 March to 12 April 2026. Plan for **late March 2027** and watch
<https://2027.alife.org>.

### The rules (from the 2026 call; check 2027's)

- **Full paper:** 3 to 8 pages, not counting references and acknowledgements. Must be new, unpublished work.
  A preprint on arXiv or Zenodo does **not** count as published, so Parts 1 and 3 are safe.
- **Not anonymous:** names and affiliations go on the paper (single-blind review).
- **Templates:** LaTeX (on Overleaf) or Word, linked from the call.
- Two other formats, neither in the proceedings: a **summary** (2 pages, only for work already peer reviewed
  elsewhere) and a **late-breaking abstract** (2 pages, work in progress, a poster).

### 4.1 Cut 35 pages to 8

The setup guide (Sections 1 to 10) is not what reviewers want; the experiments are. A shape that fits:

| Part | Pages | From |
|---|---|---|
| Introduction: question, why it matters, what is new (pre-registered predictions in ALife) | 1 | Section 11 opening |
| The world: river, energy pools, agents, inheritance rules | 1.5 | Sections 2 and 11.1, Figure 2 |
| Method: 9 conditions, 16 seeds, the pre-registration and how it was scored | 1 | 11.1, 11.8, `predictions.md` |
| Results: the three strongest experiments, with their figures | 3 | 11.2, 11.3, 11.7; Figures 4, 5, 7 |
| The scorecard: 17 right, 5 partly, 17 wrong, and what the wrong ones teach | 1 | 11.8, Table 15 |
| Discussion and limits | 0.5 | Section 11 close |

Everything cut goes in the Zenodo record, which the paper cites.

### 4.2 Write it

1. Open the ALIFE template on Overleaf (<https://www.overleaf.com>, free account).
2. Write to the table above. Keep every number exactly as in the 35-page paper; cite the Zenodo DOI for the full
   version, code and data.
3. Redraw the figures at the column width; the SVGs in `desktop-setup/figures/` convert directly.
4. Ask one person who has not seen the work to read it cold before submitting.

### 4.3 Submit

1. Through the submission link in the 2027 call, before the deadline (Anywhere on Earth time: 23:59 AoE is about
   20:00 AWST the next day, so you get most of an extra day).
2. Notification comes about two months later. If accepted: revise, upload the camera-ready version (about two
   weeks later), sign the MIT Press agreement (non-exclusive, so the preprints stay up), register, and present
   in Prague, in person or as the call allows.

Re-check: <https://alife.org/conference/>, <https://2027.alife.org>, last year's call
<https://2026.alife.org/call-for-papers/>.

---

## Part 5: the *Artificial Life* journal (MIT Press)

The field's main journal. It takes longer, fuller papers than the conference, so most of Section 11 fits. The bar
is higher and review takes months. A bonus: papers recently published in the journal are automatically given an
oral slot at the ALIFE conference.

Choose this **or** the conference for the same results, not both at once: a full paper must be unpublished.
Sending the conference version first and a longer journal version later is normal, provided the journal version
adds substantially and says so in its cover letter.

1. Read the current guidelines at <https://direct.mit.edu/artl/pages/submission-guidelines> (length limits and
   the submission system are listed there).
2. Use the journal's Overleaf template ("Artificial Life Journal Submission Template"). The manuscript is single
   column and double spaced throughout, with a cover page carrying the title, authors, abstract and five or six
   keywords.
3. Restructure as a research article: introduction, related work, model, experiments, results, discussion. The
   install and launch instructions (Sections 3 to 5) become a short "Reproducibility" paragraph pointing at the
   Zenodo record.
4. Data: MIT Press has a research data policy; the Zenodo records meet it. Cite them.
5. Write a one-page cover letter: what is new, why it fits the journal, and that a preprint is on arXiv.
6. Submit through the system the guidelines name. Questions go to `editor@alife.org`.
7. Expect reviews in months, then a revision round. Answer every reviewer point in a separate response letter.

---

## Part 6: JOSS, the Journal of Open Source Software

JOSS reviews software, not results: it publishes a short paper about the code so the code itself becomes
citable. It is free.

### Honest fit: not yet, and maybe not this kit

- **Six months public:** the repository must have been public, with active development, for **more than six
  months** before submission. Made public in October 2026, the earliest is **April 2027**.
- **Substantial effort:** JOSS wants software that reflects "substantial scholarly effort" and is useful to other
  researchers. A 664-line single-purpose simulation is likely to be judged too small. It would fit if the kit
  grew into a reusable library: configurable worlds, documented API, installable package, tests.
- **The paper must not be about the research results**; it describes the software.

### If it grows into that

1. Choose an OSI licence (Part 0.3) and put the `LICENSE` file in the repository.
2. Make it installable (`pyproject.toml`), with automated tests and documentation of every option.
3. Develop it in the open for six months: issues, commits, releases.
4. Write `paper.md` (title, summary, statement of need, author with ORCID and affiliation, key references) beside
   the code, following JOSS's example paper.
5. JOSS's submission requirements include an AI-usage disclosure statement and a conflict-of-interest
   declaration; what goes in them is the author's decision.
6. Submit the short form at <https://joss.theoj.org/papers/new>. An editor opens a public review issue; respond
   to reviewers within two weeks and finish changes within four to six.

Re-check: <https://joss.readthedocs.io/en/latest/submitting.html>.

---

## Before any submission

Every venue has its own author policies, covering licence, data, competing interests and the use of generative
AI tools. Read each one's current page before submitting; several now ask authors for a statement.
