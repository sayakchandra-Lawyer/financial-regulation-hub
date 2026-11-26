#!/usr/bin/env python3
"""Collect official regulator headlines for the landing-page band into news.json.

Sources: RBI notifications and press releases RSS, SEBI RSS. Headlines are kept
verbatim with a link to the regulator's own page. Only items relevant to the
hub's readers are kept; market-operations notices, entity variants for banks,
and enforcement items that name a company are dropped.

Usage: python3 -I tools/fetch_news.py            (writes news.json at repo root)
       python3 -I tools/fetch_news.py --file rbi_notif=a.xml --file rbi_pr=b.xml   (offline test)
"""
import json, os, re, sys, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

IST = timezone(timedelta(hours=5, minutes=30))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "news.json")
KEEP_DAYS = 10

FEEDS = {
    "rbi_notif": ("rbi", "Notification", "https://www.rbi.org.in/notifications_rss.xml"),
    "rbi_pr": ("rbi", "Press release", "https://www.rbi.org.in/pressreleases_rss.xml"),
    "sebi": ("sebi", "Update", "https://www.sebi.gov.in/sebirss.xml"),
}

# Notifications meant only for other kinds of regulated entity.
OTHER_ENTITY = re.compile(r"\((?:Commercial|Small Finance|Payments|Regional Rural|Local Area|Urban Co-?operative|Rural Co-?operative|State Co-?operative|Central Co-?operative|Co-?operative)\s+Banks?\b|All India Financial Institutions", re.I)
# Press releases are mostly market operations; keep only regulatory ones.
PR_KEEP = re.compile(r"\b(NBFCs?|non-banking|housing finance|HFCs?|directions?|circulars?|framework|master|regulations?|guidelines?|draft|consultation|discussion paper|comments|FEMA|foreign exchange management|external commercial|ECB|KYC|digital lending|fair practices|monetary policy|statement on developmental|policy rates?|amendment|notification|scheme)\b", re.I)
PR_DROP = re.compile(r"\b(auction|money market operations|treasury bills?|T-bills?|repo|reverse repo|reserve money|money supply|weekly statistical|bulletin|survey|forex reserves|foreign exchange reserves|government stock|state government securities|SDL|underwriting|sovereign gold|result of|data on|lending and deposit rates|penalty|penalt|cancel|cancellation|certificate of registration|section 35A|all inclusive directions|imposes|withdraws|lifts)\b", re.I)
SEBI_DROP = re.compile(r"\b(order in the matter|adjudication|settlement order|recovery|attachment|penalty|show cause|in respect of m/s|in the matter of)\b", re.I)

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (regulation-hub news band)", "Accept": "application/rss+xml, application/xml, text/xml"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read()

def parse_date(s):
    s = (s or "").strip()
    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S", "%d %b %Y %H:%M:%S %z", "%d %b %Y %H:%M:%S", "%a, %d %b %Y"):
        try:
            d = datetime.strptime(s, fmt)
            return (d.replace(tzinfo=IST) if d.tzinfo is None else d).astimezone(IST)
        except ValueError:
            pass
    return None

def clean(t):
    t = re.sub(r"<[^>]+>", " ", t or "")
    t = t.replace("&amp;", "&").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", t).strip()

def items(key, raw):
    reg, kind, _ = FEEDS[key]
    root = ET.fromstring(raw)
    for it in root.iter("item"):
        title = clean(it.findtext("title"))
        link = (it.findtext("link") or "").strip().replace("&amp;", "&")
        d = parse_date(it.findtext("pubDate"))
        if not title or not link.startswith("https://") or not d:
            continue
        if key == "rbi_notif" and OTHER_ENTITY.search(title):
            continue
        if key == "rbi_pr" and (PR_DROP.search(title) or not PR_KEEP.search(title)):
            continue
        if key == "sebi" and SEBI_DROP.search(title):
            continue
        k = kind
        if key == "rbi_notif" and re.search(r"\bdraft\b", title, re.I): k = "Draft"
        elif key == "rbi_notif" and re.search(r"\bdirections?\b", title, re.I): k = "Directions"
        yield {"reg": reg, "kind": k, "title": title[:300], "url": link, "date": d.strftime("%Y-%m-%d"), "time": d.strftime("%H:%M")}

def main(argv):
    files = dict(a.split("=", 1) for a in argv[argv.index("--file") + 1:] if "=" in a) if "--file" in argv else {}
    old = []
    if os.path.exists(OUT):
        try: old = json.load(open(OUT, encoding="utf-8")).get("items", [])
        except Exception: old = []
    got, ok = [], []
    for key, (_, _, url) in FEEDS.items():
        if files and key not in files: continue
        try:
            raw = open(files[key], "rb").read() if files else fetch(url)
            got += list(items(key, raw)); ok.append(key)
        except Exception as e:
            print(f"warn: {key}: {e}", file=sys.stderr)
    today = datetime.now(IST).date()
    cutoff = (today - timedelta(days=KEEP_DAYS)).isoformat()
    by = {}
    for x in old + got:                       # keep earlier items if a feed fails today
        if x.get("date", "") >= cutoff: by[x["url"]] = x
    out = sorted(by.values(), key=lambda x: (x["date"], x.get("time", "")), reverse=True)[:60]
    data = {"updated": datetime.now(IST).strftime("%Y-%m-%dT%H:%M+05:30"), "items": out}
    if old == out and os.path.exists(OUT):
        print(f"no change ({len(out)} items; feeds read: {', '.join(ok) or 'none'})"); return 0
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1); f.write("\n")
    print(f"wrote {len(out)} items; feeds read: {', '.join(ok) or 'none'}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
