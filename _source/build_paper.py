#!/usr/bin/env python3
"""Build 'Running Persistent AI Worlds' (October 2026 edition): numbered citations, MD + PDF.

Source conventions in paper.src.md:
  [@key] or [@key1; @key2]   citation keys, defined in refs.py (REFS dict)
  <!-- cover -->              everything before this marker is ignored (title block lives in the cover)
  ![Figure N. Caption](figures/name.svg)   figures
  > **Key insight:** ...      callouts (class from the first bold word: insight, verify, note, warning)
"""
import html as htmlmod
import os
import re
import shutil
import subprocess
import sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from refs import REFS  # noqa: E402

CITE_RE = re.compile(r"\[(@[A-Za-z0-9_:\-]+(?:\s*;\s*@[A-Za-z0-9_:\-]+)*)\]")


def number_citations(src):
    order = []
    for m in CITE_RE.finditer(src):
        for key in re.findall(r"@([A-Za-z0-9_:\-]+)", m.group(1)):
            if key not in REFS:
                raise SystemExit(f"unknown citation key: {key}")
            if key not in order:
                order.append(key)
    num = {k: i + 1 for i, k in enumerate(order)}

    def compress(ns):
        ns = sorted(set(ns))
        out, i = [], 0
        while i < len(ns):
            j = i
            while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1:
                j += 1
            out.append(f"{ns[i]}" if j == i else (f"{ns[i]}, {ns[j]}" if j == i + 1 else f"{ns[i]}-{ns[j]}"))
            i = j + 1
        return ", ".join(out)

    def md_sub(m):
        keys = re.findall(r"@([A-Za-z0-9_:\-]+)", m.group(1))
        return "[" + compress([num[k] for k in keys]) + "]"

    md = CITE_RE.sub(md_sub, src)
    unused = [k for k in REFS if k not in num]
    return md, order, num, unused


def references_md(order):
    lines = ["## References", ""]
    for i, k in enumerate(order, 1):
        r = REFS[k]
        url = r.get("url")
        lines.append(f"{i}. {r['text']}" + (f" <{url}>" if url else ""))
    return "\n".join(lines) + "\n"


CSS = r"""
@font-face{font-family:'Plex';font-weight:100 700;src:url(fonts/plexsans-latin.woff2) format('woff2');
  unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}
@font-face{font-family:'Plex';font-weight:100 700;src:url(fonts/plexsans-greek.woff2) format('woff2');unicode-range:U+0370-03FF;}
@font-face{font-family:'Plex';font-style:italic;font-weight:100 700;src:url(fonts/plexsans-italic.woff2) format('woff2');}
@font-face{font-family:'PlexSerif';font-weight:400;src:url(fonts/ibmplexserif-400.woff2) format('woff2');}
@font-face{font-family:'PlexSerif';font-weight:500;src:url(fonts/ibmplexserif-500.woff2) format('woff2');}
@font-face{font-family:'PlexSerif';font-weight:600;src:url(fonts/ibmplexserif-600.woff2) format('woff2');}
@font-face{font-family:'PlexSerif';font-style:italic;font-weight:400;src:url(fonts/ibmplexserif-400i.woff2) format('woff2');}
@font-face{font-family:'PlexSerif';font-style:italic;font-weight:500;src:url(fonts/ibmplexserif-500i.woff2) format('woff2');}
@font-face{font-family:'PlexMono';font-weight:400;src:url(fonts/plexmono-400.woff2) format('woff2');}
@font-face{font-family:'PlexMono';font-weight:500;src:url(fonts/plexmono-500.woff2) format('woff2');}
@font-face{font-family:'PlexMono';font-weight:600;src:url(fonts/plexmono-600.woff2) format('woff2');}

:root{--ink:#1b2430;--ink2:#4b5563;--ink3:#8a94a3;--rule:#d5dbe3;--accent:#14365c;--accent2:#2a78d6;--warn:#b45309;}
@page{size:A4;margin:20mm 19mm 22mm 19mm;
  @top-left{content:"Running Persistent AI Worlds";font-family:'Plex';font-size:7.2pt;color:#8a94a3;letter-spacing:.04em;}
  @top-right{content:"October 2026 edition";font-family:'Plex';font-size:7.2pt;color:#8a94a3;letter-spacing:.04em;}
  @bottom-right{content:counter(page) " / " counter(pages);font-family:'PlexMono';font-size:7.2pt;color:#8a94a3;}}
@page cover{margin:0;@top-left{content:none}@top-right{content:none}@bottom-right{content:none}}
@page wide{size:A4 landscape;margin:16mm 18mm 18mm;}

*{box-sizing:border-box;}
html{font-family:'PlexSerif','IBM Plex Serif',Georgia,serif;font-size:9.9pt;line-height:1.58;color:var(--ink);
  -webkit-print-color-adjust:exact;print-color-adjust:exact;hyphens:auto;}
body{margin:0;}
strong{font-weight:600;}
em{font-style:italic;}
a{color:var(--accent);text-decoration:none;overflow-wrap:anywhere;}
code{font-family:'PlexMono',monospace;font-size:8.3pt;background:#f2f4f8;border:0.5pt solid #e3e8ef;padding:0 2.6pt;border-radius:2.5pt;}
pre{font-family:'PlexMono',monospace;font-size:7.6pt;line-height:1.45;background:#f6f8fb;border:0.6pt solid #e1e6ee;
  border-left:2.4pt solid var(--accent);padding:7pt 9pt;border-radius:0 3pt 3pt 0;white-space:pre-wrap;break-inside:auto;}
pre code{background:none;border:0;padding:0;font-size:inherit;}
p{margin:0 0 7.5pt;text-align:justify;text-justify:inter-word;orphans:3;widows:3;}
ul,ol{margin:0 0 9pt;padding-left:15pt;}
li{margin:2.6pt 0;}
li>ul,li>ol{margin:3pt 0;}
h2,h3,h4,.cap,table,figcaption,.cite{font-family:'Plex','IBM Plex Sans',sans-serif;}
h2{font-size:17pt;font-weight:600;letter-spacing:-.01em;margin:30pt 0 10pt;padding:0 0 6pt;border-bottom:1.1pt solid var(--accent);
  color:var(--ink);break-after:avoid;}
h2[id="about-this-edition"],h2[id="executive-summary"],h2[id="1-the-science-of-never-ending-learning"],
h2[id="appendix-a-corrections-to-the-february-2026-edition"],h2[id="references"]{break-before:page;margin-top:0;}
h2 .num{color:var(--accent2);margin-right:8pt;font-weight:600;}
table.long{break-inside:auto;}
table.long tr{break-inside:avoid;}
td.nw,th.nw{white-space:nowrap;}
h3{font-size:11.4pt;font-weight:600;color:var(--accent);margin:16pt 0 6pt;break-after:avoid;}
h4{font-size:9.6pt;font-weight:600;color:var(--ink);margin:12pt 0 4pt;break-after:avoid;letter-spacing:.01em;}
h2+h3{margin-top:4pt;}
table{width:100%;border-collapse:collapse;margin:4pt 0 12pt;font-size:8.2pt;line-height:1.42;break-inside:avoid;}
thead th{text-align:left;background:#eef2f7;color:var(--ink2);font-weight:600;font-size:7.1pt;letter-spacing:.06em;
  text-transform:uppercase;padding:5pt 6pt;border-bottom:0.9pt solid #c9d1dc;vertical-align:bottom;}
td{padding:4.4pt 6pt;border-bottom:0.6pt solid #e6eaf0;vertical-align:top;}
tbody tr:last-child td{border-bottom:0.9pt solid #c9d1dc;}
p.cap{font-size:8pt;color:var(--ink2);margin:10pt 0 3pt;font-weight:600;letter-spacing:.01em;text-align:left;break-after:avoid;}
p.cap .lab{color:var(--accent);}
p:has(+table),p:has(+ol),p:has(+ul),p:has(+pre){break-after:avoid;}
blockquote{margin:9pt 0 12pt;padding:8pt 12pt;border-left:2.6pt solid var(--accent2);background:#f3f7fc;
  border-radius:0 4pt 4pt 0;break-inside:avoid;font-size:9.3pt;}
blockquote p{text-align:left;}
blockquote p:last-child{margin-bottom:0;}
blockquote.verify,blockquote.warning{border-left-color:var(--warn);background:#fff7ed;}
blockquote.verify strong:first-child,blockquote.warning strong:first-child{color:var(--warn);}
blockquote.insight strong:first-child{color:var(--accent);}
figure{margin:10pt 0 14pt;break-inside:avoid;}
figure img{width:100%;display:block;}
figcaption{font-size:8pt;color:var(--ink2);margin-top:5pt;line-height:1.45;}
figcaption b{color:var(--accent);font-weight:600;}
.cite{font-size:7.6pt;color:var(--accent2);white-space:nowrap;}
.cite a{color:var(--accent2);}
ol.refs{font-family:'Plex',sans-serif;font-size:7.7pt;line-height:1.42;padding-left:22pt;}
ol.refs li{margin:2.6pt 0;break-inside:avoid;}
ol.refs a{font-family:'PlexMono',monospace;font-size:7pt;color:var(--ink3);}
ol.toc{columns:2;column-gap:20pt;padding-left:18pt;font-family:'Plex',sans-serif;font-size:9pt;}
ol.toc li{margin:3pt 0;break-inside:avoid;}
.lead{font-size:11pt;line-height:1.55;color:var(--ink);}
.kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:7pt;margin:6pt 0 14pt;break-inside:avoid;}
.kpi{border:0.7pt solid var(--rule);border-top:2.2pt solid var(--accent2);border-radius:3pt;padding:6pt 8pt;font-family:'Plex',sans-serif;}
.kpi b{display:block;font-size:15pt;font-weight:600;color:var(--ink);letter-spacing:-.01em;}
.kpi span{font-size:7.6pt;color:var(--ink2);line-height:1.35;display:block;margin-top:2pt;}

/* cover */
.cover{page:cover;width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;background:#0f1d30;color:#fff;}
.cover .grid{position:absolute;inset:0;background:
  repeating-linear-gradient(0deg,transparent 0 9.9mm,rgba(255,255,255,.045) 9.9mm 10mm),
  repeating-linear-gradient(90deg,transparent 0 9.9mm,rgba(255,255,255,.045) 9.9mm 10mm);}
.cover .art{position:absolute;left:0;right:0;top:118mm;height:118mm;}
.cover .art img{width:100%;height:100%;display:block;}
.cover .inner{position:absolute;top:24mm;left:19mm;right:19mm;font-family:'Plex',sans-serif;}
.cover .kicker{font-size:7.8pt;letter-spacing:.22em;color:#8fb8ea;font-weight:600;margin-bottom:6mm;}
.cover h1{font-family:'Plex',sans-serif;font-size:34pt;line-height:1.04;margin:0;font-weight:600;letter-spacing:-.02em;}
.cover h1 span{display:block;font-weight:300;color:#c9d6e8;font-size:19pt;letter-spacing:-.005em;margin-top:4mm;line-height:1.2;}
.cover .ed{display:inline-block;margin-top:7mm;font-size:8.4pt;letter-spacing:.14em;font-weight:600;color:#0f1d30;background:#8fb8ea;
  padding:1.6mm 3.2mm;border-radius:1.4mm;}
.cover .foot{position:absolute;left:19mm;right:19mm;bottom:15mm;font-family:'Plex',sans-serif;display:grid;
  grid-template-columns:2.2fr 1fr 1fr 1fr;gap:4mm;border-top:0.8pt solid rgba(255,255,255,.35);padding-top:3.5mm;}
.cover .foot div{font-size:8.2pt;color:#e6edf6;line-height:1.4;}
.cover .foot b{display:block;font-size:6.4pt;letter-spacing:.18em;color:#8fb8ea;font-weight:600;margin-bottom:1mm;}
.cover .covers{font-size:8.6pt;line-height:1.5;color:#c9d6e8;}
"""


PRINT_CSS = r"""
@page{size:A4;margin:20mm 24mm 22mm 24mm;}
@page :left{margin-left:17mm;margin-right:25mm;
  @top-left{content:"Running Persistent AI Worlds";font-family:'Plex';font-size:7.2pt;color:#5f6b7a;}
  @top-right{content:none;}
  @bottom-left{content:counter(page);font-family:'PlexMono';font-size:7.6pt;color:#3c4654;}
  @bottom-right{content:none;}}
@page :right{margin-left:25mm;margin-right:17mm;
  @top-left{content:none;}
  @top-right{content:"Second edition · 10 October 2026";font-family:'Plex';font-size:7.2pt;color:#5f6b7a;}
  @bottom-right{content:counter(page);font-family:'PlexMono';font-size:7.6pt;color:#3c4654;}
  @bottom-left{content:none;}}
:root{--accent:#1b2f4d;--accent2:#1f4f8a;}
html{color:#111821;}
blockquote{background:none;border:0.6pt solid #c9d1dc;border-left:2.6pt solid var(--accent2);}
blockquote.verify,blockquote.warning{background:none;border:0.6pt solid #e5c9a8;border-left:2.6pt solid #b45309;}
pre{background:none;border:0.6pt solid #c9d1dc;border-left:2.4pt solid var(--accent);}
code{background:none;border:0.5pt solid #d5dbe3;}
thead th{background:#f1f3f6;}
.kpi{border-top:2.2pt solid var(--accent2);}
a{color:inherit;}
.cite,.cite a{color:#1f4f8a;}
.cover.cover-print{background:#ffffff;color:#111821;}
.cover-print .kicker{color:#1f4f8a;}
.cover-print h1{color:#111821;}
.cover-print h1 span{color:#4b5563;}
.cover-print .ed{color:#ffffff;background:#1b2f4d;}
.cover-print .foot{border-top:0.8pt solid #1b2f4d;}
.cover-print .foot div{color:#111821;}
.cover-print .foot b{color:#1f4f8a;}
.cover-print .covers{color:#3c4654;}
.cover-print .art{top:122mm;}
"""


def to_html(md_numbered, num):
    body = md_numbered.split("<!-- cover -->", 1)[1] if "<!-- cover -->" in md_numbered else md_numbered
    h = markdown.markdown(body, extensions=["tables", "toc", "sane_lists", "attr_list", "fenced_code", "md_in_html"])
    # citations -> linked superscript-free brackets
    def cite_html(m):
        inner = m.group(1)
        parts = []
        for tok in [t.strip() for t in inner.split(",")]:
            if "-" in tok:
                a, b = tok.split("-")
                parts.append(f'<a href="#ref-{a}">{a}</a>-<a href="#ref-{b}">{b}</a>')
            else:
                parts.append(f'<a href="#ref-{tok}">{tok}</a>')
        return '<span class="cite">[' + ", ".join(parts) + "]</span>"
    h = re.sub(r"\[((?:\d+(?:-\d+)?)(?:, \d+(?:-\d+)?)*)\]", cite_html, h)
    # numbered h2 sections
    h = re.sub(r'<h2 id="([^"]+)">(\d+)\. ', r'<h2 id="\1"><span class="num">\2</span>', h)
    h = re.sub(r'<h2 id="([^"]+)">(?!<span)', r'<h2 class="unnum" id="\1">', h)
    # contents list
    h = re.sub(r'(<h2 class="unnum" id="contents">Contents</h2>\s*)<ol>', r'\1<ol class="toc">', h, count=1)
    # references list
    h = re.sub(r'(<h2 class="unnum" id="references">References</h2>\s*)<ol>', r'\1<ol class="refs">', h, count=1)
    def refs_ids(m):
        block = m.group(0)
        i = [0]
        def li(mm):
            i[0] += 1
            return f'<li id="ref-{i[0]}">'
        return re.sub(r"<li>", li, block)
    h = re.sub(r'<ol class="refs">.*?</ol>', refs_ids, h, flags=re.S)
    # table / figure captions
    h = re.sub(r"<p><strong>(Table \d+\.)</strong>", r'<p class="cap"><span class="lab">\1</span>', h)
    h = re.sub(r'<p><img alt="(Figure \d+\.)\s*([^"]*)" src="([^"]+)" ?/?></p>',
               lambda m: f'<figure><img src="{m.group(3)}" alt="{m.group(1)} {m.group(2)}">'
                         f'<figcaption><b>{m.group(1)}</b> {m.group(2)}</figcaption></figure>', h)
    # long tables may break across pages; keep dates on one line
    def mark_long(m):
        t = m.group(0)
        if t.count("<tr") > 11:
            t = t.replace("<table>", '<table class="long">', 1)
        return t
    h = re.sub(r"<table>.*?</table>", mark_long, h, flags=re.S)
    h = re.sub(r"(<td>[^<]*?)\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{4})",
               lambda m: f"{m.group(1)}{m.group(2)}\u00a0{m.group(3)}", h)
    # callouts
    def bq(m):
        first = re.search(r"<strong>([A-Za-z]+)", m.group(0))
        cls = (first.group(1).lower() if first else "note")
        cls = {"key": "insight", "verify": "verify", "warning": "warning", "caution": "warning"}.get(cls, "note")
        return m.group(0).replace("<blockquote>", f'<blockquote class="{cls}">', 1)
    h = re.sub(r"<blockquote>.*?</blockquote>", bq, h, flags=re.S)
    return h


def check_numbering(src):
    """Figures and numbered tables must run 1, 2, 3 ... in order of appearance."""
    for label, found in (("Figure", re.findall(r"!\[Figure (\d+)\.", src)),
                         ("Table", re.findall(r"^\*\*Table (\d+)\.\*\*", src, re.M))):
        got = [int(n) for n in found]
        if got != list(range(1, len(got) + 1)):
            sys.exit(f"{label} numbers out of sequence: {got}")


def main(out_dir, mode="screen"):
    secdir = os.path.join(HERE, "sections")
    src = "\n\n".join(open(os.path.join(secdir, f), encoding="utf-8").read().rstrip()
                       for f in sorted(os.listdir(secdir)) if f.endswith(".md")) + "\n"
    open(os.path.join(HERE, "paper.src.md"), "w", encoding="utf-8").write(src)
    check_numbering(src)
    md, order, num, unused = number_citations(src)
    md_full = md.rstrip() + "\n\n" + references_md(order)
    if unused:
        print("WARNING unused refs:", ", ".join(unused))
    print(f"{len(order)} references cited")
    os.makedirs(out_dir, exist_ok=True)
    # deliverable markdown: drop the cover marker block header comment only
    open(os.path.join(out_dir, "paper.md"), "w", encoding="utf-8").write(md_full.replace("<!-- cover -->\n", ""))
    build = os.path.join(HERE, "build")
    if os.path.isdir(build):
        shutil.rmtree(build)
    os.makedirs(build)
    shutil.copytree(os.path.join(HERE, "fonts"), os.path.join(build, "fonts"))
    shutil.copytree(os.path.join(HERE, "figures"), os.path.join(build, "figures"))
    cover_file = "cover_print.html" if mode == "print" else "cover.html"
    cover = open(os.path.join(HERE, cover_file), encoding="utf-8").read().replace("{NREFS}", str(len(order)))
    css = CSS + (PRINT_CSS if mode == "print" else "")
    body = to_html(md_full, num)
    doc = (f'<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>Running Persistent AI Worlds</title>'
           f"<style>{css}</style></head><body>{cover}<main>{body}</main></body></html>")
    hp = os.path.join(build, "paper.html")
    open(hp, "w", encoding="utf-8").write(doc)
    pdf = os.path.join(out_dir, "paper-print.pdf" if mode == "print" else "paper.pdf")
    subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=15000", f"--print-to-pdf={pdf}", "file://" + hp],
                   check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    print(pdf)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "screen")
