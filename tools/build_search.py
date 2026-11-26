#!/usr/bin/env python3
"""Build the site-wide search index (search/) from each section's fulltext.json and judgments.json.
Run from the repo root after any data change:  python3 -I tools/build_search.py
"""
import json, re, os, sys, zlib, shutil
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "search")
SHARDS = 256          # postings shards, picked by crc32(term) % SHARDS
TEXT_PER = 120        # passages per text file
COMMON = 0.25         # stop words in more than this share of passages are not indexed (phrase bigrams still are)
BIG_MAX = 1500        # bigrams in more passages than this are not indexed

TOK = re.compile(r"[a-z0-9₹%]+")
def toks(s): return TOK.findall(str(s).lower())

STOP = set("a an and are as at be by can do does for from has have how i if in is it its may me must my no not of on or our shall should that the their there this to under us was we what when where which who whom why will with would you your about any into than then them they such other all".split())

def shard_of(term): return zlib.crc32(term.encode()) % SHARDS

def b36(n):
    s = ""; d = "0123456789abcdefghijklmnopqrstuvwxyz"
    while True:
        n, r = divmod(n, 36); s = d[r] + s
        if not n: return s

def main():
    hub = json.load(open(os.path.join(ROOT, "hub.json")))
    docs, dindex, passages = [], {}, []   # passages: (doc, chap, para, text)
    def doc(sec, did, label, old, url):
        k = (sec, did)
        if k not in dindex: dindex[k] = len(docs); docs.append([sec, did, label, old, url or ""])
        return dindex[k]
    for s in hub["sections"]:
        d = s.get("data") or {}
        if s.get("status") != "live" or not d.get("fulltext"): continue
        reg = json.load(open(os.path.join(ROOT, d["register"])))
        byid = {r["id"]: r for r in reg.get("instruments", [])}
        ft = json.load(open(os.path.join(ROOT, d["fulltext"])))
        for did, chap, para, txt in ft["chunks"]:
            r = byid.get(did, {})
            lab = re.sub(r"^Master Directions? [–-] ", "", r.get("short_name") or r.get("title") or did)
            st = (r.get("status") or "").lower()
            old = 1 if re.search(r"supersed|repeal|withdrawn", st) or r.get("type") == "Superseded instrument" else 0
            passages.append((doc(s["id"], did, lab, old, r.get("official_url")), chap or "", para or "", txt))
    jp = os.path.join(ROOT, "judgments/data/judgments.json")
    if os.path.exists(jp):
        for j in json.load(open(jp))["judgments"]:
            label = j["title"]
            meta = " · ".join(x for x in [j.get("court"), j.get("neutral_citation") or j.get("report_citation")] if x)
            parts = [j.get("issue"), j.get("holding"), j.get("impact")]
            st = j.get("statutes") or []
            if st: parts.append("Statutes: " + "; ".join(map(str, st)))
            topic = j.get("topic") or ""
            txt = "\n\n".join(str(p) for p in parts if p)
            passages.append((doc("judgments", j["id"], label, 0, j.get("url")), meta, str(j.get("date") or ""), (topic + "\n\n" if topic else "") + txt))
    N = len(passages)
    post, lens = {}, []
    for i, (_, chap, para, txt) in enumerate(passages):
        w = toks(txt); lens.append(len(w))
        tf = {}
        for t in w: tf[t] = tf.get(t, 0) + 1
        for a, b in zip(w, w[1:]):
            k = a + " " + b; tf.setdefault(k, 0)
            if tf[k] == 0: tf[k] = -1      # mark bigram present (tf not needed)
        for t, n in tf.items(): post.setdefault(t, []).append((i, n))
    uni_df, common, big_common = {}, [], []
    shards = [dict() for _ in range(SHARDS)]
    for t, lst in post.items():
        big = " " in t
        if big and len(lst) > BIG_MAX: big_common.append(t); continue
        if not big:
            uni_df[t] = len(lst)
            if t in STOP and len(lst) > COMMON * N: common.append(t); continue
        prev, parts = 0, []
        for i, n in lst:
            parts.append(b36(i - prev) + (":" + b36(n) if (not big and n > 1) else "")); prev = i
        shards[shard_of(t)][t] = ",".join(parts)
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "p")); os.makedirs(os.path.join(OUT, "t"))
    for k, sh in enumerate(shards):
        json.dump(sh, open(os.path.join(OUT, "p", f"{k}.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    for k in range(0, N, TEXT_PER):
        json.dump([[p[0], p[1], p[2], p[3]] for p in passages[k:k + TEXT_PER]], open(os.path.join(OUT, "t", f"{k // TEXT_PER}.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    vocab = sorted(uni_df)
    meta = {"v": 1, "n": N, "shards": SHARDS, "textPer": TEXT_PER, "bigMax": BIG_MAX, "docs": docs,
            "pdoc": [p[0] for p in passages], "plen": lens,
            "vocab": " ".join(vocab), "df": [uni_df[t] for t in vocab], "common": sorted(common), "bigCommon": sorted(big_common)}
    json.dump(meta, open(os.path.join(OUT, "meta.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"search index: {N} passages, {len(docs)} documents, {len(vocab)} words, {len(common)} common words skipped")

if __name__ == "__main__":
    main()
