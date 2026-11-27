#!/usr/bin/env python3
"""Build the Follow updates, Watchlist and Common questions pages (follow/, watchlist/, faq/).

Run from the repo root:  python3 -I tools/make_tool_pages.py
The pages read their content at run time: follow/ from hub.json, watchlist/ from the reader's own browser
plus changes.json, faq/ from faq/faq.json (only items with "status": "approved" are shown).
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
idx = (ROOT / "index.html").read_text(encoding="utf-8")
VER = re.search(r"hub\.css\?v=([\w]+)", idx).group(1)
ICON = re.search(r'<link rel="icon"[^>]+>', idx).group(0)


def page(key, title, desc, crumb, body, script, extra_head=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} · Financial Regulation Hub</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://sayakchandra-lawyer.github.io/financial-regulation-hub/{key}/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400&display=swap">
<link rel="stylesheet" href="../assets/hub.css?v={VER}">
{ICON}{extra_head}
</head>
<body>
<header id="top"></header>
<main class="wrap">
  <div class="pg" style="max-width:920px;margin:0 auto;padding:34px 0 60px">
{body}
  </div>
</main>
<footer id="foot"></footer>
<script src="../assets/hub.js?v={VER}"></script>
<script>
(async function(){{
  const hub = await getJSON("../hub.json");
  renderChrome(hub, {{ root: "../", active: "{key}", sub: "{title}", crumb: `<a href="../">Home</a> / <b>{title}</b>` }});
{script}
}})();
</script>
</body>
</html>
'''


FOLLOW_BODY = '''    <div class="eyebrow">Follow updates</div>
    <h1 style="font-size:clamp(28px,4vw,40px);margin-top:8px">New rules, in your own feed</h1>
    <p style="color:var(--ink-2);max-width:720px">Every new or amended rule added to this site is published as an RSS feed, one for the whole site and one for each section. Add a feed to your reader, Outlook or Slack and new items arrive by themselves, each with a link to the official source.</p>
    <div class="card panel" style="margin-top:22px;padding:6px 20px 10px" id="feeds"><p class="tag" style="padding:14px 0">Loading the feeds…</p></div>
    <h2 style="font-size:22px;margin-top:34px">How to add a feed</h2>
    <div class="grid g3" style="margin-top:12px">
      <div class="card panel"><h3 style="font-size:17px">Outlook (Windows)</h3><p class="tag" style="margin:6px 0 0">In the folder list, right-click <b>RSS Subscriptions</b> (or <b>RSS Feeds</b>), choose <b>Add a New RSS Feed</b> and paste the feed address.</p></div>
      <div class="card panel"><h3 style="font-size:17px">Slack</h3><p class="tag" style="margin:6px 0 0">Add Slack's <b>RSS</b> app to your workspace, then in a channel type <code>/feed subscribe</code> followed by the feed address.</p></div>
      <div class="card panel"><h3 style="font-size:17px">A feed reader</h3><p class="tag" style="margin:6px 0 0">In Feedly, Inoreader, NetNewsWire or any reader, choose <b>Add</b> or <b>Follow</b> and paste the feed address.</p></div>
    </div>
    <p class="tag" style="margin-top:22px">Want to keep an eye on particular rules instead? Use the <b>Watch</b> button on any instrument or judgment and see what changed on <a class="lnk" href="../watchlist/">your watchlist</a>.</p>'''

FOLLOW_JS = '''  const base = new URL("../", location.href).href;
  const rows = [["", "Everything on the site", "All sections, newest 60 items"], ...hub.sections.filter(s => s.status === "live" && s.data && s.data.updates).map(s => [s.href, s.name === s.short ? (s.full || s.name) : s.name, s.full && s.full !== s.name ? s.full : ""])];
  $("#feeds").innerHTML = `<div class="flist">${rows.map(([h, t, m], i) => { const u = base + h + "feed.xml"; return `<div class="frow" style="${i ? "" : "border-top:0"}"><div style="flex:1;min-width:220px"><div class="t">${I.rss} ${esc(t)}</div>${m ? `<div class="m">${esc(m)}</div>` : ""}<code>${esc(u)}</code></div><button type="button" class="btn g sm" data-copy="${esc(u)}">${I.link} Copy address</button><a class="btn g sm" href="${esc(u)}" target="_blank" rel="noopener">Open</a></div>`; }).join("")}</div>`;
  $("#feeds").addEventListener("click", e => { const b = e.target.closest("[data-copy]"); if (b) hubCopy(b.dataset.copy, "Feed address copied"); });'''

WATCH_BODY = '''    <div class="eyebrow">Your watchlist</div>
    <h1 style="font-size:clamp(28px,4vw,40px);margin-top:8px">Rules you are watching</h1>
    <p style="color:var(--ink-2);max-width:720px">Press <b>Watch</b> on any instrument or judgment to add it here. Anything that has changed since you last opened it is marked <span class="pill p-chg">Changed</span>.</p>
    <p class="tag" style="max-width:720px">Your watchlist is kept only in this browser, on this device. Nothing is sent to us. Clearing your browser data removes it, so use <b>Save a copy</b> to keep it or move it to another device.</p>
    <div class="filter" id="wtools" style="margin:16px 0 4px"></div>
    <div id="wlist"><p class="tag" style="padding:14px 0">Loading…</p></div>'''

WATCH_JS = '''  const secName = Object.fromEntries(hub.sections.map(s => [s.id, s.short]));
  const draw = async () => {
    const w = Watch.all(), keys = Object.keys(w), ch = await hubChanges();
    const changed = k => ch[k] && ch[k] > (w[k].seen || w[k].added || "");
    $("#wtools").innerHTML = keys.length ? `<button type="button" class="btn g sm" data-w="seen">Mark all as seen</button><button type="button" class="btn g sm" data-w="export">Save a copy</button><label class="btn g sm" style="cursor:pointer">Load a saved copy<input type="file" accept="application/json,.json" id="wimp" hidden></label>`
      : `<label class="btn g sm" style="cursor:pointer">Load a saved copy<input type="file" accept="application/json,.json" id="wimp" hidden></label>`;
    if (!keys.length) { $("#wlist").innerHTML = `<div class="card panel" style="margin-top:12px"><h2 style="font-size:19px">Nothing here yet</h2><p class="tag" style="margin:6px 0 0">Open any instrument (for example in <a class="lnk" href="../rbi/#az">RBI rules A–Z</a>) or <a class="lnk" href="../judgments/#all">a judgment</a> and press <b>Watch</b>.</p></div>`; return; }
    const groups = {};
    keys.forEach(k => { const g = k.split("/")[0]; (groups[g] = groups[g] || []).push(k); });
    const nC = keys.filter(changed).length;
    $("#wlist").innerHTML = `<p class="tag" style="margin:10px 0">${keys.length} watched${nC ? ` · <b style="color:var(--accent-text)">${nC} changed since you last looked</b>` : " · nothing has changed since you last looked"}</p>` + Object.entries(groups).map(([g, ks]) => `<section style="margin-top:18px"><h2 style="font-size:19px">${esc(secName[g] || w[ks[0]].s || g)}</h2>
      ${ks.sort((a, b) => changed(b) - changed(a) || (w[a].t || "").localeCompare(w[b].t || "")).map(k => `<div class="frow"><div style="flex:1;min-width:220px"><a class="t lnk" href="../${esc(w[k].h || "")}">${esc(w[k].t || k)}</a>
        <div class="m">${changed(k) ? `<span class="pill p-chg">Changed</span> ${fmtDate(ch[k])} · ` : ch[k] ? `Last change ${fmtDate(ch[k])} · ` : ""}watching since ${fmtDate(w[k].added)}</div></div>
        <button type="button" class="btn g sm" data-rm="${esc(k)}" aria-label="Stop watching ${esc(w[k].t || k)}">Remove</button></div>`).join("")}</section>`).join("");
  };
  document.addEventListener("click", async e => {
    const rm = e.target.closest("[data-rm]"); if (rm) { const w = Watch.all(); delete w[rm.dataset.rm]; Watch.save(w); draw(); return; }
    const b = e.target.closest("[data-w]"); if (!b) return;
    if (b.dataset.w === "seen") { const w = Watch.all(), ch = await hubChanges(); Object.keys(w).forEach(k => { if (ch[k]) w[k].seen = ch[k]; }); Watch.save(w); draw(); }
    if (b.dataset.w === "export") { const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([JSON.stringify({ watchlist: Watch.all() }, null, 1)], { type: "application/json" })); a.download = "regulation-hub-watchlist.json"; a.click(); }
  });
  document.addEventListener("change", e => {
    if (e.target.id !== "wimp" || !e.target.files[0]) return;
    const r = new FileReader(); r.onload = () => { try { const d = JSON.parse(r.result).watchlist || {}; const w = Watch.all(); Object.entries(d).forEach(([k, v]) => { if (/^[a-z-]+\\/[\\w.-]+$/.test(k) && v && typeof v === "object") w[k] = { t: String(v.t || ""), s: String(v.s || ""), h: String(v.h || "").replace(/^[\\/]+|^\\w+:/g, ""), added: String(v.added || "").slice(0, 10), seen: String(v.seen || "").slice(0, 10) }; }); Watch.save(w); hubToast("Watchlist loaded"); draw(); } catch (x) { hubToast("That file is not a saved watchlist"); } };
    r.readAsText(e.target.files[0]);
  });
  draw();'''

FAQ_BODY = '''    <div class="eyebrow">Common questions</div>
    <h1 style="font-size:clamp(28px,4vw,40px);margin-top:8px">Common questions, answered</h1>
    <p style="color:var(--ink-2);max-width:720px">Short answers to the questions people ask most about the rules on this site, each linked to the paragraph it comes from. They explain the law in general; they are not advice on any particular case.</p>
    <form class="search" id="fform" role="search" style="margin-top:18px" onsubmit="return false"><label class="sr" for="fq">Search common questions</label><input id="fq" type="search" autocomplete="off" placeholder="Search the questions, e.g. “co-lending”, “KYC”"></form>
    <div class="filter" id="fsec" style="margin:14px 0 4px"></div>
    <div id="flist" class="faq"><p class="tag" style="padding:14px 0">Loading…</p></div>'''

FAQ_JS = '''  $("#fform").insertAdjacentHTML("afterbegin", I.search);
  const d = await getJSON("../faq/faq.json").catch(() => ({ items: [], topics: [] }));
  const items = (d.items || []).filter(x => x.status === "approved");
  const topics = Object.fromEntries((d.topics || []).map(t => [t.id, t.name]));
  const secName = Object.fromEntries(hub.sections.map(s => [s.id, s.short]));
  let S = "", Q = "";
  const draw = () => {
    const ws = Q.toLowerCase().split(/\\s+/).filter(Boolean);
    const list = items.filter(x => (!S || (x.sections || []).includes(S)) && ws.every(w => (x.q + " " + x.a + " " + (x.keywords || []).join(" ")).toLowerCase().includes(w)));
    const secs = [...new Set(items.flatMap(x => x.sections || []))];
    $("#fsec").innerHTML = secs.length > 1 ? [["", "All"], ...secs.map(s => [s, secName[s] || s])].map(([k, t]) => `<button type="button" class="chip ${S === k ? "on" : ""}" data-s="${k}">${esc(t)}</button>`).join("") : "";
    if (!items.length) { $("#flist").innerHTML = `<div class="card panel"><p style="margin:0">The first answers are being written. Meanwhile, ask <b>Counsel’s Clerk</b> (bottom right on any section page) or <a class="lnk" href="../">search the site</a>.</p></div>`; return; }
    const by = {}; list.forEach(x => (by[x.topic] = by[x.topic] || []).push(x));
    $("#flist").innerHTML = list.length ? Object.entries(by).map(([t, xs]) => `<section style="margin-top:22px"><h2 style="font-size:20px;margin-bottom:6px">${esc(topics[t] || t)}</h2>${xs.map(x => `<details id="q-${esc(x.id)}"${location.hash === "#q-" + x.id ? " open" : ""}><summary>${esc(x.q)}</summary><div class="ans">${faqAnswerHTML(x)}<p class="tag">${(x.sections || []).map(s => esc(secName[s] || s)).join(" · ")}${x.updated ? ` · answer as on ${fmtDate(x.updated)}` : ""} · <button type="button" class="lnk" data-ql="${esc(x.id)}">Copy link</button></p></div></details>`).join("")}</section>`).join("")
      : `<p class="empty">No question matches. Try fewer words, or ask Counsel’s Clerk on any section page.</p>`;
  };
  $("#fq").addEventListener("input", () => { Q = $("#fq").value.trim(); draw(); });
  document.addEventListener("click", e => {
    const c = e.target.closest("[data-s]"); if (c) { S = c.dataset.s; draw(); return; }
    const l = e.target.closest("[data-ql]"); if (l) { history.replaceState(null, "", "#q-" + l.dataset.ql); hubCopy(location.href, "Link copied"); }
  });
  draw();
  if (location.hash) { const el = document.getElementById(location.hash.slice(1)); if (el) { el.open = true; el.scrollIntoView(); } }'''


def main():
    out = {
        "follow": page("follow", "Follow updates", "RSS feeds of every new and amended rule on the Financial Regulation Hub, for the whole site and for each section.", "", FOLLOW_BODY, FOLLOW_JS,
                       '\n<link rel="alternate" type="application/rss+xml" title="All updates · Financial Regulation Hub" href="../feed.xml">'),
        "watchlist": page("watchlist", "Watchlist", "The rules and judgments you are watching on the Financial Regulation Hub, with what changed since you last looked.", "", WATCH_BODY, WATCH_JS,
                          '\n<meta name="robots" content="noindex">'),
        "faq": page("faq", "Common questions", "Short answers to common questions on financial regulation for NBFCs, HFCs and other regulated entities, each linked to its source paragraph.", "", FAQ_BODY, FAQ_JS),
    }
    for k, html in out.items():
        p = ROOT / k / "index.html"; p.parent.mkdir(exist_ok=True); p.write_text(html, encoding="utf-8")
        print("wrote", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
