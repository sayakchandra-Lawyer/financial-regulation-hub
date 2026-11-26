#!/usr/bin/env python3
"""Fail if any update, judgment or news item has no link to its official source.
Run from anywhere:  python3 -I tools/check_sources.py   (exit code 1 lists what is missing)
"""
import json, glob, os, sys
from urllib.parse import urlparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Official hosts accepted for section updates (regulators, ministries, gazette, statute and court sites).
OFFICIAL = ("rbi.org.in", "sebi.gov.in", "irdai.gov.in", "meity.gov.in", "ibbi.gov.in", "ifsca.gov.in",
            "nhb.org.in", "fiuindia.gov.in", "mca.gov.in", "egazette.gov.in", "egazette.nic.in", "indiacode.nic.in",
            "indiacode.gov.in", "pib.gov.in", "cert-in.org.in", "finmin.gov.in", "dea.gov.in", "incometaxindia.gov.in",
            "main.sci.gov.in", "sci.gov.in", "nclat.nic.in", "nclt.gov.in")
def official(u):
    h = urlparse(u).netloc.lower()
    return any(h == d or h.endswith("." + d) for d in OFFICIAL)
def bad_url(u):
    return not isinstance(u, str) or not u.startswith("https://") or " " in u
problems = []
for f in sorted(glob.glob(os.path.join(ROOT, "*", "data", "updates.json"))):
    sec = os.path.relpath(f, ROOT).split(os.sep)[0]
    for u in json.load(open(f, encoding="utf-8")).get("updates", []):
        url = u.get("url")
        if not url: problems.append(f"{sec}: {u.get('id')} has no source link")
        elif bad_url(url): problems.append(f"{sec}: {u.get('id')} source link is not a plain https URL: {url}")
        elif not official(url): problems.append(f"{sec}: {u.get('id')} source link is not an official site: {url}")
jf = os.path.join(ROOT, "judgments", "data", "judgments.json")
if os.path.exists(jf):
    for j in json.load(open(jf, encoding="utf-8")).get("judgments", []):
        if not j.get("url") or bad_url(j["url"]): problems.append(f"judgments: {j.get('id')} has no source link")
nf = os.path.join(ROOT, "news.json")
if os.path.exists(nf):
    for n in json.load(open(nf, encoding="utf-8")).get("items", []):
        if not n.get("url") or bad_url(n["url"]): problems.append(f"news.json: '{n.get('title','')[:60]}' has no source link")
if problems:
    print("Missing or unofficial source links:\n  " + "\n  ".join(problems)); sys.exit(1)
print("Source links: every update, judgment and news item links to its source.")
