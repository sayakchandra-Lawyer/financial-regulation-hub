"""Build the monthly newsletter pages from newsletter/data/<YYYY-MM>.json.

Run from the repo root:  python3 -I tools/make_newsletter.py
Writes newsletter/index.html (archive) and newsletter/<YYYY-MM>/index.html (one page per issue).
To publish a new month, add newsletter/data/<YYYY-MM>.json in the same shape and run this again.
"""
import html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
NL = ROOT / "newsletter"
idx = (ROOT / "index.html").read_text(encoding="utf-8")
VER = re.search(r"hub\.css\?v=([\w]+)", idx).group(1)
ICON = re.search(r'<link rel="icon"[^>]+>', idx).group(0)
NLV = "20261128b"  # newsletter.css cache key
e = lambda s: html.escape(str(s or ""), quote=True)
EXT = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'
REGC = {"RBI": "rbi", "SEBI": "sebi", "IRDAI": "irdai", "IFSCA": "ifsc", "NSE / BSE": "exchanges", "NHB": "nhb", "MCA": "companies",
        "IBBI": "ibc", "FEMA": "fema", "DPDP": "dpdp", "Supreme Court": "jud", "NCLAT": "jud", "RBI / NHB": "nhb", "RBI (UAPA)": "rbi",
        "RBI (FEMA)": "fema", "CERT-In": "misc", "Others": "misc"}
IMP = {"High": 3, "Medium": 2, "Low": 1}
SITE = "https://sayakchandra-lawyer.github.io/financial-regulation-hub/"


def head(title, desc, root, canon):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)} · Financial Regulation Hub</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{canon}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:image" content="{SITE}assets/og.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400&display=swap">
<link rel="stylesheet" href="{root}assets/hub.css?v={VER}">
<link rel="stylesheet" href="{root}assets/newsletter.css?v={NLV}">
{ICON}
</head>
<body>
<header id="top"></header>
'''


def tail(root, crumb, extra=""):
    return f'''<footer id="foot"></footer>
<script src="{root}assets/hub.js?v={VER}"></script>
<script>
(async function(){{
  const hub = await getJSON("{root}hub.json");
  renderChrome(hub, {{ root: "{root}", active: "newsletter", crumb: `{crumb}` }});
{extra}
}})();
</script>
</body>
</html>
'''


def rpill(reg):
    return f'<span class="pill nl-reg" style="--c:var(--{REGC.get(reg, "misc")})">{e(reg)}</span>'


def ipill(imp):
    return f'<span class="pill nl-imp i{IMP.get(imp, 1)}">{e(imp)} impact</span>'


def src(url, label="Source"):
    return f'<a class="lnk nl-src" href="{e(url)}" target="_blank" rel="noopener">{label} {EXT}</a>'


def heat(d):
    """sector x theme grid: each cell is the highest impact among that sector's items on that theme."""
    g = {s["id"]: [0] * len(d["themes"]) for s in d["sectors"]}
    for it in d["items"]:
        t = d["themes"].index(it["theme"])
        for s in it["sectors"]:
            g[s][t] = max(g[s][t], IMP[it["impact"]])
    return g


def issue_page(d, all_issues):
    root = "../../"
    items = {i["id"]: i for i in d["items"]}
    sec = {s["id"]: s for s in d["sectors"]}
    high = sum(1 for i in d["items"] if i["impact"] == "High")
    dl = len(d["timeline"])
    kpis = [(d["tracked"], "Regulatory changes tracked"), (len(d["items"]), "Covered in this issue"),
            (high, "High-impact changes"), (len(d["judgments"]), "Court rulings that matter")]
    # issue switcher
    opts = "".join(f'<option value="{root}newsletter/{x["id"]}/"{" selected" if x["id"] == d["id"] else ""}>{e(x["issue"])}</option>' for x in all_issues)
    mast = f'''<section class="nl-mast rise">
    <div class="nl-mast-l">
      <div class="eyebrow">Monthly newsletter <span class="sep"></span>Issue {d["number"]:02d}</div>
      <h1>{e(d["issue"])}</h1>
      <p class="nl-period">Covering {e(d["period"])}</p>
      <p class="nl-head">{e(d["headline"])}</p>
    </div>
    <div class="nl-mast-r">
      <label class="sr" for="nlpick">Choose an issue</label>
      <select class="chip" id="nlpick">{opts}</select>
      <button class="btn g" type="button" id="nlprint">Print or save as PDF</button>
      <a class="lnk" href="{root}newsletter/">All issues</a>
    </div>
  </section>'''
    toc = '<nav class="nl-toc" aria-label="In this issue">' + "".join(
        f'<a class="chip" href="#{a}">{t}</a>' for a, t in
        [("six", "Top six"), ("impact", "Where the impact falls"), ("dates", "Dates ahead"), ("sectors", "By sector"), ("rulings", "Court rulings that matter")]) + "</nav>"
    k = '<div class="nl-kpis">' + "".join(f'<div class="card"><b>{n}</b><span>{e(l)}</span></div>' for n, l in kpis) + "</div>"
    # top six
    tops = []
    for n, t in enumerate(d["top"], 1):
        it = items[t["id"]]
        chips = "".join(f'<span class="nl-sec" style="--c:var(--{sec[s]["c"]})">{e(sec[s]["name"])}</span>' for s in it["sectors"])
        tops.append(f'''<article class="card nl-topc">
      <div class="nl-n">{n:02d}</div>
      <div class="nl-meta">{rpill(it["reg"])}{ipill(it["impact"])}</div>
      <h3><a href="#{it["id"]}">{e(it["title"])}</a></h3>
      <p>{e(t["so_what"])}</p>
      <div class="nl-secs">{chips}</div>
      <div class="nl-foot"><span class="nl-date">{"Key date: <b>" + e(it["date"]) + "</b>" if it["date"] else ""}</span>{src(it["url"])}</div>
    </article>''')
    top = f'<section id="six" class="nl-block"><h2>The month in six</h2><p class="nl-sub">The changes most likely to need attention across the sector.</p><div class="nl-tops">{"".join(tops)}</div></section>'
    # heatmap
    g = heat(d)
    lv = {0: ("", "None"), 1: ("Low", "Low"), 2: ("Med", "Medium"), 3: ("High", "High")}
    rows = "".join(
        f'<tr><th scope="row"><span class="nl-dot" style="--c:var(--{s["c"]})"></span>{e(s["name"])}</th>' +
        "".join(f'<td class="h{v}" title="{e(s["name"])} · {e(d["themes"][j])}: {lv[v][1]}">{lv[v][0] or "<span aria-label=\"None\">·</span>"}</td>' for j, v in enumerate(g[s["id"]])) + "</tr>"
        for s in d["sectors"])
    hm = f'''<div class="card nl-heat"><h3>Impact by sector and theme</h3>
      <div class="nl-scroll"><table><thead><tr><th></th>{"".join(f'<th scope="col">{e(t)}</th>' for t in d["themes"])}</tr></thead><tbody>{rows}</tbody></table></div>
      <div class="nl-legend"><span><i class="h1"></i>Low</span><span><i class="h2"></i>Medium</span><span><i class="h3"></i>High</span><span class="tag">Each cell shows the highest impact among this month's changes for that sector and theme.</span></div></div>'''
    mx = max(n for _, n in d["regulators"])
    bars = "".join(f'<li><span>{e(r)}</span><i style="--w:{n / mx * 100:.1f}%;--c:var(--{REGC.get(r, "misc")})"></i><b>{n}</b></li>' for r, n in d["regulators"])
    rb = f'<div class="card nl-bars"><h3>Changes by regulator</h3><ul>{bars}</ul><p class="tag">{d["tracked"]} changes tracked in {e(d["period"])}.</p></div>'
    impact = f'<section id="impact" class="nl-block"><h2>Where the impact falls</h2><div class="nl-two">{hm}{rb}</div></section>'
    # timeline grouped by month
    months = {}
    for t in d["timeline"]:
        y, m, _ = t["iso"].split("-")
        months.setdefault((y, m), []).append(t)
    MN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    tl = "".join(f'<div class="nl-month"><h3>{MN[int(m) - 1]} {y}</h3><ol>' + "".join(
        f'<li style="--c:var(--{sec[t["sector"]]["c"]})"><time datetime="{t["iso"]}">{e(t["date"].replace(" " + y, ""))}</time><a href="#{t["item"]}">{e(t["text"])}</a><span class="nl-sec" style="--c:var(--{sec[t["sector"]]["c"]})">{e(sec[t["sector"]]["name"])}</span></li>'
        for t in ts) + "</ol></div>" for (y, m), ts in months.items())
    dates = f'<section id="dates" class="nl-block"><h2>Dates ahead</h2><p class="nl-sub">Deadlines and start dates set by this month\'s changes.</p><div class="nl-tl">{tl}</div></section>'
    # sectors
    chips = '<div class="nl-filter" role="toolbar" aria-label="Filter by sector"><button class="chip on" type="button" data-s="">All sectors</button>' + "".join(
        f'<button class="chip" type="button" data-s="{s["id"]}"><span class="nl-dot" style="--c:var(--{s["c"]})"></span>{e(s["name"])}</button>' for s in d["sectors"]) + "</div>"
    blocks = []
    shown = set()
    for s in d["sectors"]:
        mine = [i for i in d["items"] if s["id"] in i["sectors"]]
        mine.sort(key=lambda i: -IMP[i["impact"]])
        full, brief, also = [], [], []
        for it in mine:
            if it["id"] in shown:
                first = sec[it["sectors"][0]]["name"] if it["sectors"][0] != s["id"] else sec[it["sectors"][1]]["name"]
                also.append(f'<li><a href="#{it["id"]}">{e(it["title"])}</a> <span class="tag">under {e(first)}</span></li>')
                continue
            shown.add(it["id"])
            if it["impact"] == "Low":
                brief.append(f'<li id="{it["id"]}"><div class="nl-meta">{rpill(it["reg"])}<span class="tag">{e(it["issued"])}</span></div><b>{e(it["title"])}</b><p>{e(it["what"])} {e(it["why"])}</p>{src(it["url"])}</li>')
                continue
            pts = "".join(f"<li>{e(p)}</li>" for p in it["points"])
            more = (f'<details><summary>Who it applies to and key points</summary><p><b>Applies to:</b> {e(it["applies"])}</p>'
                    + (f"<ul>{pts}</ul>" if pts else "") + "</details>")
            full.append(f'''<article class="card nl-item" id="{it["id"]}">
        <div class="nl-meta">{rpill(it["reg"])}{ipill(it["impact"])}<span class="pill p-grey">{e(it["theme"])}</span><span class="tag">Issued {e(it["issued"])}</span></div>
        <h3>{e(it["title"])}</h3>
        <div class="nl-cols"><div><h4>What changed</h4><p>{e(it["what"])}</p></div><div><h4>Why it matters</h4><p>{e(it["why"])}</p></div></div>
        {f'<p class="nl-step"><b>Practical step:</b> {e(it["step"])}</p>' if it["step"] else ""}
        {more}
        <div class="nl-foot"><span class="nl-date">{"Key date: <b>" + e(it["date"]) + "</b>" if it["date"] else ""}</span>{src(it["url"])}</div>
      </article>''')
        body = "".join(full)
        if brief: body += f'<div class="card nl-brief"><h4>Also this month</h4><ul>{"".join(brief)}</ul></div>'
        if also: body += f'<div class="nl-also"><h4>Also relevant</h4><ul>{"".join(also)}</ul></div>'
        blocks.append(f'<section class="nl-sector" data-s="{s["id"]}" style="--c:var(--{s["c"]})"><h3 class="nl-sh"><span class="nl-dot"></span>{e(s["name"])} <span class="tag">{len(mine)} change{"s" if len(mine) != 1 else ""}</span></h3>{body}</section>')
    sectors = f'<section id="sectors" class="nl-block"><h2>By sector</h2><p class="nl-sub">Each change appears in full once. Where it also touches another sector, that sector links back to it.</p>{chips}{"".join(blocks)}</section>'
    # judgments
    jc = "".join(f'''<article class="card nl-jud">
      <div class="nl-meta"><span class="pill nl-reg" style="--c:var(--jud)">{e(j["court"])}</span><span class="tag">{e(j["kind"])} · {e(j["date"])}</span></div>
      <h3>{e(j["headline"])}</h3>
      <p>{e(j["takeaway"])}</p>
      <p class="nl-case">{e(j["title"])}</p>
      <div class="nl-foot">{f'<a class="lnk" href="{root}judgments/j/{e(j["hub"])}/">Case note</a>' if j["hub"] else "<span></span>"}{src(j["url"], "Official text")}</div>
    </article>''' for j in d["judgments"])
    rulings = f'<section id="rulings" class="nl-block"><h2>Court rulings that matter</h2><p class="nl-sub">Supreme Court and NCLAT rulings this month that matter to lenders, insurers and intermediaries.</p><div class="nl-juds">{jc}</div></section>'
    disc = f'''<section class="nl-block"><div class="nl-disc"><h2>Please read</h2>
      <p>This newsletter is an independent, unofficial summary of public documents for general information. It is not legal advice, it is not endorsed by any regulator or court, and it may be incomplete or out of date. Practical steps are general pointers, not recommendations for any particular entity. Always read the official text linked from each item and take professional advice before acting. See the <a class="lnk" href="{root}disclaimer/">disclaimer</a>.</p></div></section>'''
    script = '''  const pick = document.getElementById("nlpick"); pick.addEventListener("change", () => { location.href = pick.value; });
  document.getElementById("nlprint").addEventListener("click", () => { document.querySelectorAll(".nl-item details").forEach(x => x.open = true); window.print(); });
  const bs = [...document.querySelectorAll(".nl-filter .chip")], ss = [...document.querySelectorAll(".nl-sector")];
  bs.forEach(b => b.addEventListener("click", () => { bs.forEach(x => x.classList.toggle("on", x === b)); ss.forEach(s => s.hidden = !!b.dataset.s && s.dataset.s !== b.dataset.s); }));
  document.body.classList.add("anim");'''
    desc = f'{d["issue"]} newsletter: {d["headline"]}.'
    page = head(f'Newsletter · {d["issue"]}', desc, root, f'newsletter/{d["id"]}/') + f'''<main class="wrap nl">
  {mast}
  {toc}
  {k}
  {top}
  {impact}
  {dates}
  {sectors}
  {rulings}
  {disc}
</main>
''' + tail(root, f'<a href="{root}">Home</a> / <a href="{root}newsletter/">Newsletter</a> / <b>{e(d["issue"])}</b>', script)
    out = NL / d["id"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")


def archive(all_issues):
    root = "../"
    latest = all_issues[0]
    high = sum(1 for i in latest["items"] if i["impact"] == "High")
    feat = f'''<a class="card nl-feat rise" href="{latest["id"]}/">
      <div class="eyebrow">Latest issue <span class="sep"></span>Issue {latest["number"]:02d}</div>
      <h2>{e(latest["issue"])}</h2>
      <p class="nl-head">{e(latest["headline"])}</p>
      <div class="nl-fk"><span><b>{latest["tracked"]}</b> changes tracked</span><span><b>{high}</b> high impact</span><span><b>{len(latest["judgments"])}</b> court rulings</span></div>
      <span class="btn p">Read the {e(latest["issue"])} issue</span>
    </a>'''
    years = {}
    for x in all_issues: years.setdefault(x["id"][:4], []).append(x)
    lst = "".join(f'<h2 class="nl-year">{y}</h2><ul class="nl-arch">' + "".join(
        f'<li><a href="{x["id"]}/"><b>{e(x["issue"])}</b><span>{e(x["headline"])}</span></a></li>' for x in xs) + "</ul>" for y, xs in years.items())
    page = head("Monthly newsletter", "A monthly round-up of changes in Indian financial regulation: what changed, why it matters by sector, dates ahead and court rulings.", root, "newsletter/") + f'''<main class="wrap nl">
  <div class="ipage">
    <section>
      <div class="eyebrow">Newsletter</div>
      <h1>Monthly newsletter</h1>
      <p class="lede">One page a month on what changed in Indian financial regulation: the changes that matter most, how they affect NBFCs, housing finance companies, insurers, mutual funds, brokers and digital lenders, the dates ahead and the court rulings worth knowing. Every item links to the official text.</p>
      {feat}
      {lst}
    </section>
    <aside>
      <div class="card"><h3>Every week, not just monthly</h3><p class="tag" style="margin:0 0 12px">The home page lists every change as it happens. Follow updates by RSS or keep a watchlist of the rules you track.</p><a class="btn g" href="{root}follow/">Follow updates</a></div>
      <div class="card"><h3>Not legal advice</h3><p class="tag" style="margin:0">An independent, unofficial summary of public documents. Check the official text before relying on any point. <a class="lnk" href="{root}disclaimer/">Disclaimer</a></p></div>
    </aside>
  </div>
</main>
''' + tail(root, f'<a href="{root}">Home</a> / <b>Newsletter</b>', '  document.body.classList.add("anim");')
    (NL / "index.html").write_text(page, encoding="utf-8")


# public pages stay generic: no group or company branding, no internal process notes
BLOCK = re.compile(r"Aditya|Birla|\bABC[DL]?\b|\bABSL\b|\bABHFC\b|ChatGPT|Gemini|verif|reviewed here|not yet reviewed|assessment pending|\b(?:our|we|us)\b", re.I)
for p in (NL / "data").glob("*.json"):
    m = BLOCK.search(p.read_text(encoding="utf-8"))
    if m: raise SystemExit(f"{p.name}: remove '{m.group(0)}' before publishing")
issues = sorted((json.loads(p.read_text(encoding="utf-8")) for p in (NL / "data").glob("[0-9][0-9][0-9][0-9]-[0-9][0-9].json")), key=lambda x: x["id"], reverse=True)
for d in issues:
    issue_page(d, issues)
archive(issues)
# home page "headline changes": the latest issue's top six, resolved to plain fields
L = issues[0]; byid = {i["id"]: i for i in L["items"]}; sn = {x["id"]: x for x in L["sectors"]}
latest = {"id": L["id"], "issue": L["issue"], "period_end": L.get("period_end", ""), "href": f"newsletter/{L['id']}/", "top": [
    {"title": byid[t["id"]]["title"], "so_what": t["so_what"], "reg": byid[t["id"]]["reg"], "regc": REGC.get(byid[t["id"]]["reg"], "misc"),
     "impact": byid[t["id"]]["impact"], "date": byid[t["id"]]["date"], "url": byid[t["id"]]["url"],
     "more": f"newsletter/{L['id']}/#{t['id']}", "sectors": [[sn[x]["name"], sn[x]["c"]] for x in byid[t["id"]]["sectors"]]} for t in L["top"]]}
(NL / "latest.json").write_text(json.dumps(latest, ensure_ascii=False, indent=1), encoding="utf-8")
print("newsletter:", ", ".join(x["id"] for x in issues))
