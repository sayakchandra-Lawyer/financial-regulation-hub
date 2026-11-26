#!/usr/bin/env python3
"""Static pages for search engines and link previews.

Writes, from the data files the site already uses:
  <section>/i/<ID>/index.html   one page per instrument (RBI, SEBI, IRDAI, FEMA, DPDP, IBC, IFSC ...)
  judgments/j/<ID>/index.html   one page per judgment
  sitemap.xml, robots.txt
and refreshes the Open Graph block in every section's index.html and the home page.

Each page carries the summary as plain HTML (so it can be indexed), a canonical URL and preview tags,
plus a link into the interactive view. Run after any data change:  python3 -I tools/build_pages.py
"""
import html, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_URL = "https://sayakchandra-lawyer.github.io/financial-regulation-hub/"
E = lambda s: html.escape(str(s or ""), quote=True)
OG_START, OG_END = "<!-- og:start -->", "<!-- og:end -->"


def strip_checked(s):
    s = re.sub(r"\s*\((?:re)?checked[^)]*\)", "", str(s or ""), flags=re.I)
    return re.sub(r"\s*\[(?:re)?checked[^\]]*\]", "", s, flags=re.I)


def clean_name(s):
    s = re.sub(r"^Master Directions? [–-] ", "", str(s or ""))
    return re.sub(r"^Reserve Bank of India \(([^)]*)\) ", "", s)


def fmt_date(d):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(d or ""))
    if not m:
        return str(d or "")
    mon = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()[int(m.group(2)) - 1]
    return f"{int(m.group(3))} {mon} {m.group(1)}"


def asset_version():
    m = re.search(r"hub\.css\?v=([\w]+)", open(os.path.join(ROOT, "index.html"), encoding="utf-8").read())
    return m.group(1) if m else "1"


def favicon():
    m = re.search(r'<link rel="icon"[^>]*>', open(os.path.join(ROOT, "index.html"), encoding="utf-8").read())
    return m.group(0) if m else ""


def og_tags(title, desc, url, base, kind="website"):
    return "\n".join([
        OG_START,
        f'<link rel="canonical" href="{E(url)}">',
        f'<meta property="og:type" content="{kind}">',
        '<meta property="og:site_name" content="Financial Regulation Hub">',
        f'<meta property="og:title" content="{E(title)}">',
        f'<meta property="og:description" content="{E(desc)}">',
        f'<meta property="og:url" content="{E(url)}">',
        f'<meta property="og:image" content="{E(base)}assets/og.png">',
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{E(title)}">',
        f'<meta name="twitter:description" content="{E(desc)}">',
        OG_END])


def short(s, n=158):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"


PAGE_CSS = """<style>
.sp{max-width:880px;margin:0 auto;padding:30px max(16px,min(40px,4vw)) 0}
.sp .crumbs{font-size:13px;color:var(--muted)}.sp .crumbs a:hover{color:var(--accent-text)}
.sp h1{font-size:clamp(28px,4vw,38px);line-height:1.15;margin:10px 0 8px}
.sp .full{color:var(--ink-2);margin:0 0 14px}
.sp h2{font-size:21px;margin:30px 0 8px}
.sp ul{padding-left:20px;margin:0}.sp li{margin:6px 0;font-size:15px}
.sp dl{display:grid;grid-template-columns:170px 1fr;gap:6px 16px;margin:0;font-size:15px}.sp dt{color:var(--muted)}.sp dd{margin:0}
@media (max-width:600px){.sp dl{grid-template-columns:1fr}.sp dd{margin-bottom:8px}}
.sp .acts{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0 4px}
.sp .note{font-size:13px;color:var(--muted);margin-top:28px}
</style>"""


def page(title, desc, url, base, depth, active, crumb_html, body, sub):
    up = "../" * depth
    v = asset_version()
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(title)} · Financial Regulation Hub</title>
<meta name="description" content="{E(desc)}">
{og_tags(title, desc, url, base, "article")}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400&display=swap">
<link rel="stylesheet" href="{up}assets/hub.css?v={v}">
{favicon()}
{PAGE_CSS}
</head>
<body>
<header id="top" class="top"></header>
<main class="sp">
{body}
</main>
<footer id="foot"></footer>
<script src="{up}assets/hub.js?v={v}"></script>
<script>
(async function(){{ const hub = await getJSON("{up}hub.json"); renderChrome(hub, {{ root: "{up}", active: "{active}", sub: {json.dumps(sub)}, crumb: {json.dumps(crumb_html)} }}); }})();
</script>
</body>
</html>
"""


def ul(items):
    items = [strip_checked(x) for x in items if str(x or "").strip()]
    return "<ul>" + "".join(f"<li>{E(x)}</li>" for x in items) + "</ul>" if items else ""


def section_title(sec_dir):
    t = re.search(r"<title>(.*?)</title>", open(os.path.join(ROOT, sec_dir, "index.html"), encoding="utf-8").read(), re.S)
    return html.unescape(t.group(1).split(" · ")[0].strip()) if t else sec_dir.upper()


def instrument_body(sec, it, sec_title):
    sid, href = sec["id"], sec["href"]
    name = clean_name(it.get("short_name") or it.get("title"))
    rows = [("Type", it.get("type")), ("Status", strip_checked(it.get("status"))), ("Reference", it.get("reference_no")),
            ("Issued", fmt_date(it.get("issue_date"))), ("Effective", fmt_date(it.get("effective_date"))),
            ("Updated as on", fmt_date(it.get("updated_as_on"))), ("Issued by", it.get("issuing_department")),
            ("Issued under", "; ".join(it.get("statutory_powers") or [])),
            ("Applies to", "; ".join(strip_checked(x) for x in it.get("applies_to") or [])),
            ("Does not apply to", "; ".join(strip_checked(x) for x in it.get("excluded") or []))]
    dl = "".join(f"<dt>{E(k)}</dt><dd>{E(v)}</dd>" for k, v in rows if str(v or "").strip())
    src = []
    if it.get("official_url"):
        src.append(f'<a class="btn g" href="{E(it["official_url"])}" target="_blank" rel="noopener">Official text ↗</a>')
    if it.get("official_pdf"):
        src.append(f'<a class="btn g" href="{E(it["official_pdf"])}" target="_blank" rel="noopener">Official PDF ↗</a>')
    parts = [f'<div class="crumbs"><a href="../../../">Home</a> / <a href="../../">{E(sec.get("short") or sec_title)}</a> / {E(it.get("theme") or "")}</div>',
             f"<h1>{E(name)}</h1>"]
    if it.get("title") and clean_name(it["title"]) != name:
        parts.append(f'<p class="full">{E(it["title"])}</p>')
    parts.append(f'<div class="acts"><a class="btn p" href="../../#d/{E(it["id"])}">Open the full interactive summary</a>{"".join(src)}</div>')
    parts.append(f"<h2>At a glance</h2><dl>{dl}</dl>")
    for head, key in [("Key concepts", "key_concepts"), ("Key obligations", "core_obligations"),
                      ("Deadlines and cycles", "timelines"), ("If you breach it", "consequences_stated")]:
        block = ul(it.get(key) or [])
        if block:
            parts.append(f"<h2>{head}</h2>{block}")
    if it.get("consequences_general"):
        parts.append(f'<p class="note"><b>General consequences under the statute.</b> {E(strip_checked(it["consequences_general"]))}</p>')
    parts.append('<p class="note"><b>Not legal advice.</b> An independent, unofficial summary. Verify every point against the official text before relying on it.</p>')
    return "\n".join(parts)


def judgment_body(j):
    rows = [("Court", j.get("court")), ("Date", fmt_date(j.get("date"))), ("Neutral citation", j.get("neutral_citation")),
            ("Report citation", j.get("report_citation")), ("Case no.", j.get("case_no")), ("Bench", j.get("bench")),
            ("Statutes", "; ".join(j.get("statutes") or [])), ("Status", j.get("status_note") or "")]
    dl = "".join(f"<dt>{E(k)}</dt><dd>{E(v)}</dd>" for k, v in rows if str(v or "").strip())
    src = f'<a class="btn g" href="{E(j["url"])}" target="_blank" rel="noopener">Judgment text ↗</a>' if j.get("url") else ""
    parts = ['<div class="crumbs"><a href="../../../">Home</a> / <a href="../../">Key judgments</a></div>',
             f"<h1>{E(j.get('title'))}</h1>", f'<p class="full">{E(j.get("topic"))}</p>',
             f'<div class="acts"><a class="btn p" href="../../#j/{E(j["id"])}">Open in Key judgments</a>{src}</div>',
             f"<h2>Case details</h2><dl>{dl}</dl>"]
    if j.get("issue"):
        parts.append(f"<h2>The question</h2><p>{E(j['issue'])}</p>")
    for head, key in [("What the court held", "holding"), ("What it means in practice", "impact")]:
        block = ul(j.get(key) or [])
        if block:
            parts.append(f"<h2>{head}</h2>{block}")
    parts.append('<p class="note"><b>Not legal advice.</b> An independent, unofficial summary. Read the judgment itself before relying on it.</p>')
    return "\n".join(parts)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def set_og(path, title, desc, url, base):
    s = open(path, encoding="utf-8").read()
    block = og_tags(title, desc, url, base)
    if OG_START in s:
        s = re.sub(re.escape(OG_START) + r".*?" + re.escape(OG_END), lambda m: block, s, flags=re.S)
    else:
        s = re.sub(r'(<meta name="description"[^>]*>)', lambda m: m.group(1) + "\n" + block, s, count=1)
    open(path, "w", encoding="utf-8").write(s)


def main():
    hub = json.load(open(os.path.join(ROOT, "hub.json"), encoding="utf-8"))
    base = hub.get("site_url") or DEFAULT_URL
    if not base.endswith("/"):
        base += "/"
    urls = [(base, None)]
    home_desc = re.search(r'<meta name="description" content="([^"]*)"', open(os.path.join(ROOT, "index.html"), encoding="utf-8").read())
    set_og(os.path.join(ROOT, "index.html"), hub.get("title", "Financial Regulation Hub"), html.unescape(home_desc.group(1)) if home_desc else hub.get("tagline", ""), base, base)
    n = 0
    for sec in hub["sections"]:
        d = sec.get("data") or {}
        if sec.get("status") != "live" or not sec.get("href"):
            continue
        sdir = sec["href"].strip("/")
        stitle = section_title(sdir)
        sdesc = re.search(r'<meta name="description" content="([^"]*)"', open(os.path.join(ROOT, sdir, "index.html"), encoding="utf-8").read())
        set_og(os.path.join(ROOT, sdir, "index.html"), stitle, html.unescape(sdesc.group(1)) if sdesc else stitle, base + sdir + "/", base)
        urls.append((base + sdir + "/", None))
        if "register" in d:
            reg = json.load(open(os.path.join(ROOT, d["register"]), encoding="utf-8"))
            out = os.path.join(ROOT, sdir, "i")
            shutil.rmtree(out, ignore_errors=True)
            for it in reg.get("instruments", []):
                iid = it["id"]
                name = clean_name(it.get("short_name") or it.get("title"))
                desc = short(f"{sec.get('short')}: {name}. " + "; ".join(strip_checked(x) for x in (it.get("core_obligations") or [])[:2]))
                url = f"{base}{sdir}/i/{iid}/"
                write(os.path.join(out, iid, "index.html"), page(f"{name} ({sec.get('short')})", desc, url, base, 3, sec["id"],
                      f'<a href="../../../">Home</a> / <a href="../../">{E(sec.get("short"))}</a>', instrument_body(sec, it, stitle), stitle))
                urls.append((url, it.get("updated_as_on") or it.get("issue_date"))); n += 1
        if "judgments" in d:
            data = json.load(open(os.path.join(ROOT, d["judgments"]), encoding="utf-8"))
            out = os.path.join(ROOT, sdir, "j")
            shutil.rmtree(out, ignore_errors=True)
            for j in data.get("judgments", []):
                url = f"{base}{sdir}/j/{j['id']}/"
                desc = short(f"{j.get('court')}, {fmt_date(j.get('date'))}: {j.get('topic')}. {j.get('issue') or ''}")
                write(os.path.join(out, j["id"], "index.html"), page(j.get("title"), desc, url, base, 3, sec["id"],
                      '<a href="../../../">Home</a> / <a href="../../">Key judgments</a>', judgment_body(j), "Key judgments"))
                urls.append((url, j.get("date"))); n += 1
    for t in hub.get("tools", []):
        urls.append((base + t["href"], None))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, lm in urls:
        lm = lm if re.match(r"\d{4}-\d{2}-\d{2}$", str(lm or "")) else None
        sm.append(f"  <url><loc>{E(u)}</loc>{f'<lastmod>{lm}</lastmod>' if lm else ''}</url>")
    sm.append("</urlset>")
    write(os.path.join(ROOT, "sitemap.xml"), "\n".join(sm) + "\n")
    write(os.path.join(ROOT, "robots.txt"), f"User-agent: *\nAllow: /\nDisallow: /search/\n\nSitemap: {base}sitemap.xml\n")
    print(f"{n} static pages, {len(urls)} sitemap URLs")


if __name__ == "__main__":
    main()
