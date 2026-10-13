#!/usr/bin/env python3
"""Fetch arXiv metadata (title, authors, dates, journal reference) for every arXiv paper cited.

IDs come from the research notes and from the ax() entries in refs.py. Entries already in
research/arxiv_meta.json are updated in place, never dropped, so a failed fetch cannot break refs.py.

    python3 arxiv_meta.py            # run from this folder
    python3 arxiv_meta.py <folder>   # or name the folder that holds refs.py and research/
"""
import glob
import json
import os
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

A = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(A, "research", "arxiv_meta.json")
NS = {"a": "http://www.w3.org/2005/Atom"}

ids = set()
for f in glob.glob(os.path.join(A, "research", "*.md")):
    ids |= set(re.findall(r"arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})", open(f, encoding="utf-8").read()))
ids |= set(re.findall(r'\bax\("([^"]+)"', open(os.path.join(A, "refs.py"), encoding="utf-8").read()))
ids = sorted(ids)
meta = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}

for i in range(0, len(ids), 40):
    batch = ids[i:i + 40]
    url = "https://export.arxiv.org/api/query?id_list=" + ",".join(batch) + "&max_results=50"
    root = ET.fromstring(urllib.request.urlopen(url, timeout=60).read())
    for e in root.findall("a:entry", NS):
        link = e.find("a:id", NS).text
        if "/abs/" not in link:  # the API reports a bad ID as an entry of its own
            continue
        base = re.sub(r"v\d+$", "", link.split("/abs/", 1)[1])  # keeps old-style IDs such as cs/0309048
        jr = e.find("{http://arxiv.org/schemas/atom}journal_ref")
        meta[base] = {"title": " ".join(e.find("a:title", NS).text.split()),
                      "authors": [a.find("a:name", NS).text for a in e.findall("a:author", NS)],
                      "published": e.find("a:published", NS).text[:10],
                      "updated": e.find("a:updated", NS).text[:10],
                      "journal_ref": jr.text if jr is not None else None}
    time.sleep(3)

json.dump(meta, open(OUT, "w", encoding="utf-8"), indent=1)
missing = [i for i in ids if i not in meta]
print(f"{len(ids)} IDs cited; {len(meta)} entries in {os.path.relpath(OUT)}; missing: {missing or 'none'}")
