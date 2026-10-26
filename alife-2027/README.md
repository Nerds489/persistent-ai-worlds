# ALIFE 2027 full paper: draft

*What a Lineage Learns: Thirty-Nine Pre-registered Predictions in a Sealed Artificial World with a River*,
the 8-page conference cut of *River World on the Desktop* (Section 11 of that paper, with the setup guide
left out and cited through Zenodo).

| | |
|---|---|
| Venue | ALIFE 2027, Prague, 19 to 23 July 2027 |
| Call for papers | Not out as of 26 October 2026; past deadlines fell between late March and early May. Watch <https://2027.alife.org> |
| Format used | The 2026 rules: full paper 3 to 8 pages excluding references and acknowledgements, not anonymous, `alifeconf.sty` two-column template |
| Length now | 7 pages of body, references on page 8. One page of headroom |

## Files

| File | What it is |
|---|---|
| `main.tex` | The paper |
| `refs.bib` | References (apalike style, as the template uses) |
| `figures/*.pdf` | Vector PDFs made from `../desktop-setup/figures/*.svg` by `svg2pdf.sh` |
| `svg2pdf.sh` | Regenerates the figure PDFs through headless Chrome; rerun after any figure changes |
| `main.pdf` | The current build |

`alifeconf.sty` is not in the repository. It belongs to the conference template: download it from the
2027 call (Overleaf, LaTeX or Word links on the call page) so the paper is built against that year's
version, not last year's.

## Building

**Overleaf:** open the 2027 ALIFE template, then upload `main.tex`, `refs.bib` and the `figures/` folder
over it.

**Locally:** with `alifeconf.sty` beside `main.tex`, `tectonic -X compile main.tex`.

## Before submitting

1. **Check the 2027 call** against the 2026 rules above: page limit, template version, and any change to
   the submission formats.
2. **Read the author policies:** licence, data and competing interests, and the use of generative AI tools.
   What goes in any statement those policies ask for is the author's decision.
3. **Fill in the author block** if the 2027 template asks for an email address. The draft gives name,
   affiliation and ORCID only.
4. **Figures use Type 3 fonts** (IBM Plex, embedded through Chrome's print). Every font is embedded, but
   some proceedings checkers reject Type 3. If MIT Press's checker complains, redraw the figures as
   PDF with Type 1 or TrueType fonts.
5. **Have one person read it cold** before sending.
6. **Submit by the deadline in Anywhere on Earth time:** 23:59 AoE is about 20:00 AWST the next day.

Choose this conference **or** the *Artificial Life* journal for the same results, not both at once
(`../PUBLISHING.md`, Parts 4 and 5). The arXiv preprint of the full paper does not count as publication.
