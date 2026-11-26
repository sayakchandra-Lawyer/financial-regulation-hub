#!/usr/bin/env python3
"""Build the files behind "Follow", the watchlist and version history.

Writes, from the data the site already has:
  feed.xml, <section>/feed.xml      RSS 2.0 feeds of each section's updates.json (newest first)
  changes.json                       last change date per instrument, for "changed since you last looked" badges
  versions/state.json                fingerprint of each instrument's current full text
  versions/index.json                earlier versions held for each instrument (newest first)
  versions/<section>/<ID>/<date>.json  the text of an earlier version

When an instrument's full text changes, the previous text is read back from git history
(the last commit that changed that fulltext.json) and kept as an earlier version, so the
page can show a redline. Run from the repo root after any data change:
  python3 -I tools/build_extras.py
Add an earlier version by hand (e.g. from a regulator's previous-versions page):
  python3 -I tools/build_extras.py --add-version <section> <ID> <YYYY-MM-DD> <text file> [source url]
  (the text file is split into paragraphs on lines that start with a paragraph number)
"""
import json, os, re, sys, hashlib, subprocess, datetime, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://sayakchandra-lawyer.github.io/financial-regulation-hub/"
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
TODAY = datetime.datetime.now(IST).date().isoformat()


def load(p, default=None):
    p = os.path.join(ROOT, p)
    if not os.path.exists(p): return default
    with open(p, encoding="utf-8") as f: return json.load(f)


def dump(p, obj, pretty=False):
    p = os.path.join(ROOT, p)
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        if pretty: json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=True)
        else: json.dump(obj, f, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        f.write("\n")


def write_if_changed(p, text):
    full = os.path.join(ROOT, p)
    if os.path.exists(full) and open(full, encoding="utf-8").read() == text: return False
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    open(full, "w", encoding="utf-8").write(text)
    return True


def sections():
    hub = load("hub.json")
    out = []
    for s in hub["sections"]:
        d = s.get("data") or {}
        if s.get("status") == "live" and d.get("register"): out.append(s)
    return hub, out


def clean_name(s):
    s = re.sub(r"^Master Directions? [–-] ", "", str(s or ""))
    return s


# ---------------- RSS ----------------
def rfc822(d):
    try: dt = datetime.datetime.strptime(d[:10], "%Y-%m-%d").replace(hour=9, tzinfo=IST)
    except Exception: dt = datetime.datetime.now(IST)
    return dt.strftime("%a, %d %b %Y %H:%M:%S +0530")


def item_xml(sec, u):
    link = f"{BASE}{sec['href']}#changes/{u['id']}"
    parts = []
    meta = " · ".join(x for x in [sec["short"], u.get("kind"), u.get("ref")] if x)
    if meta: parts.append(f"<p><b>{html.escape(meta)}</b></p>")
    if u.get("effective"): parts.append(f"<p>Effective {html.escape(u['effective'])}.</p>")
    if u.get("applies"): parts.append(f"<p>Who it covers: {html.escape(u['applies'])}</p>")
    ch = [c for c in (u.get("changes") or []) if c]
    if ch: parts.append("<ul>" + "".join(f"<li>{html.escape(c)}</li>" for c in ch) + "</ul>")
    if u.get("url"): parts.append(f'<p><a href="{html.escape(u["url"])}">Official source</a></p>')
    desc = "".join(parts).replace("]]>", "]]&gt;")
    return (f"<item><title>{html.escape(sec['short'] + ': ' + u.get('title', ''))}</title>"
            f"<link>{html.escape(link)}</link>"
            f"<guid isPermaLink=\"false\">frh-{html.escape(sec['id'])}-{html.escape(u['id'])}</guid>"
            f"<pubDate>{rfc822(u.get('date') or '')}</pubDate>"
            f"<category>{html.escape(sec['short'])}</category>"
            f"<description><![CDATA[{desc}]]></description></item>")


def feed_xml(title, desc, link, self_url, items):
    last = items[0][1].get("date") if items else TODAY
    body = "".join(item_xml(s, u) for s, u in items)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
            f"<title>{html.escape(title)}</title><link>{html.escape(link)}</link>"
            f"<description>{html.escape(desc)}</description><language>en-in</language>"
            f'<atom:link href="{html.escape(self_url)}" rel="self" type="application/rss+xml"/>'
            f"<lastBuildDate>{rfc822(last or TODAY)}</lastBuildDate>"
            f"{body}</channel></rss>\n")


def build_feeds(hub, secs):
    allitems, changed = [], 0
    for s in secs:
        up = load(s["data"].get("updates") or "", {}) or {}
        items = sorted(up.get("updates") or [], key=lambda u: (u.get("date") or "", u.get("id")), reverse=True)
        pairs = [(s, u) for u in items if u.get("id") and u.get("title")]
        allitems += pairs
        path = s["href"].rstrip("/") + "/feed.xml"
        changed += write_if_changed(path, feed_xml(f"{hub['title']} · {s['short']}", f"New and amended rules from {s.get('full') or s['name']}, as covered by the {hub['title']}.",
                                                   BASE + s["href"], BASE + path, pairs))
    allitems.sort(key=lambda p: (p[1].get("date") or "", p[0]["id"], p[1]["id"]), reverse=True)
    changed += write_if_changed("feed.xml", feed_xml(hub["title"], "New and amended financial regulation for NBFCs, HFCs and other regulated entities, across all sections.",
                                                     BASE, BASE + "feed.xml", allitems[:60]))
    return changed


# ---------------- versions ----------------
def norm(t): return re.sub(r"\s+", " ", str(t or "")).strip()


def fingerprint(chunks): return hashlib.sha1("\n".join(norm(c[2]) for c in chunks).encode("utf-8")).hexdigest()[:16]


def by_inst(ft):
    out = {}
    for did, chap, para, txt in (ft or {}).get("chunks", []): out.setdefault(did, []).append([chap or "", para or "", txt or ""])
    return out


def git_previous(path):
    """Text of `path` as of the commit before its latest change, or None."""
    try:
        dirty = subprocess.run(["git", "diff", "--quiet", "HEAD", "--", path], cwd=ROOT, timeout=60).returncode == 1
        if dirty: rev = "HEAD"   # run by hand before committing: the committed file is the previous one
        else:
            hs = subprocess.run(["git", "log", "-2", "--format=%H", "--", path], cwd=ROOT, capture_output=True, text=True, timeout=60).stdout.split()
            if len(hs) < 2: return None
            rev = hs[1]
        out = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True, timeout=120)
        return json.loads(out.stdout.decode("utf-8")) if out.returncode == 0 else None
    except Exception:
        return None


def add_index(index, key, date, path):
    lst = [v for v in index.get(key, []) if v["file"] != path]
    lst.append({"date": date, "file": path})
    index[key] = sorted(lst, key=lambda v: v["date"], reverse=True)


def archive(index, sec_id, did, date, chunks, source=""):
    key = f"{sec_id}/{did}"
    taken = {v["file"] for v in index.get(key, [])}
    n, path = 1, f"versions/{sec_id}/{did}/{date}.json"
    while path in taken and os.path.exists(os.path.join(ROOT, path)):
        n += 1; path = f"versions/{sec_id}/{did}/{date}-{n}.json"
    dump(path, {"id": did, "section": sec_id, "date": date, "source": source, "chunks": chunks})
    add_index(index, key, date, path)
    return path


def inst_dates(s):
    """Latest dated event per instrument: register 'updated as on' / issue date and update dates."""
    reg = load(s["data"]["register"], {}) or {}
    dates = {}
    for r in reg.get("instruments", []):
        d = r.get("updated_as_on") or r.get("issue_date") or ""
        if re.match(r"\d{4}-\d{2}-\d{2}", str(d)): dates[r["id"]] = str(d)[:10]
    up = load(s["data"].get("updates") or "", {}) or {}
    for u in up.get("updates") or []:
        i, d = u.get("instrument"), str(u.get("date") or "")[:10]
        if i and re.match(r"\d{4}-\d{2}-\d{2}", d) and d > dates.get(i, ""): dates[i] = d
    return dates


def build_versions(secs):
    state = load("versions/state.json", {}) or {}
    index = load("versions/index.json", {}) or {}
    archived = 0
    for s in secs:
        fp = s["data"].get("fulltext")
        if not fp: continue
        cur = by_inst(load(fp))
        dates = inst_dates(s)
        prev_ft = None
        for did, chunks in cur.items():
            key = f"{s['id']}/{did}"
            h = fingerprint(chunks)
            st = state.get(key)
            new_date = dates.get(did) or TODAY
            if st and st.get("h") != h:
                if prev_ft is None: prev_ft = by_inst(git_previous(fp)) or {}
                old = prev_ft.get(did)
                if old and fingerprint(old) != h:
                    od = st.get("date") or TODAY
                    archive(index, s["id"], did, od, old); archived += 1
                    if new_date <= od: new_date = TODAY
            if not st or st.get("h") != h: state[key] = {"h": h, "date": new_date if not st else max(new_date, st.get("date") or "")}
    dump("versions/state.json", state, pretty=True)
    dump("versions/index.json", index, pretty=True)
    return archived, state, index


# ---------------- watchlist manifest ----------------
def build_changes(secs, state, index):
    items = {}
    for s in secs:
        for did, d in inst_dates(s).items(): items[f"{s['id']}/{did}"] = d
    for key, st in state.items():
        if st.get("date") and st["date"] > items.get(key, ""): items[key] = st["date"]
    jd = load("judgments/data/judgments.json", {}) or {}
    for j in jd.get("judgments", []):
        d = str(j.get("updated") or "")[:10]
        if re.match(r"\d{4}-\d{2}-\d{2}", d): items[f"jud/{j['id']}"] = d
    dump("changes.json", {"v": 1, "items": items})
    return len(items)


# ---------------- manual earlier version ----------------
PARA = re.compile(r"^\s*(\d+[A-Z]?(?:\.\d+)*)[.)]?\s+\S")


def split_text(txt):
    chunks, cur, lab = [], [], ""
    for line in txt.splitlines():
        m = PARA.match(line)
        if m and cur:
            chunks.append(["", lab, "\n".join(cur).strip()]); cur = []
        if m: lab = m.group(1)
        cur.append(line)
    if cur: chunks.append(["", lab, "\n".join(cur).strip()])
    return [c for c in chunks if c[2]]


def add_version(sec_id, did, date, path, source=""):
    index = load("versions/index.json", {}) or {}
    chunks = split_text(open(path, encoding="utf-8").read())
    p = archive(index, sec_id, did, date, chunks, source)
    dump("versions/index.json", index, pretty=True)
    print(f"added {p}: {len(chunks)} paragraphs")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--add-version":
        a = sys.argv[2:]
        if len(a) < 4: sys.exit(__doc__)
        return add_version(a[0], a[1], a[2], a[3], a[4] if len(a) > 4 else "")
    hub, secs = sections()
    n_feeds = build_feeds(hub, secs)
    archived, state, index = build_versions(secs)
    n = build_changes(secs, state, index)
    print(f"feeds: {n_feeds} changed · versions: {len(state)} tracked, {archived} new earlier versions, {sum(len(v) for v in index.values())} held · changes.json: {n} items")


if __name__ == "__main__":
    main()
