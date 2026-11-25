/* Financial Regulation Hub: shared engine (header, theme, data loading, search, Not So Intelligent AI) */
"use strict";
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const trunc = (s, n) => (s = String(s || "")).length > n ? s.slice(0, n - 1).trimEnd() + "…" : s;
const store = {
  get(k, d) { try { const v = localStorage.getItem("hub." + k); return v === null ? d : v; } catch (e) { return d; } },
  set(k, v) { try { localStorage.setItem("hub." + k, v); } catch (e) {} }
};
const MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
function fmtDate(iso, withYear = true) {
  const m = String(iso || "").match(/^(\d{4})-(\d{2})-(\d{2})/); if (!m) return iso || "";
  return `${+m[3]} ${MONTHS[+m[2] - 1]}${withYear ? " " + m[1] : ""}`;
}
async function getJSON(url) { const r = await fetch(url, { cache: "no-cache" }); if (!r.ok) throw new Error(url + " " + r.status); return r.json(); }

/* ---------- icons ---------- */
const I = {
  rbi: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 9.5 12 4l9 5.5"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8"/><path d="M3 20h18"/></svg>',
  sebi: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 19h18"/><path d="m4 15 5-5 4 3 7-7"/><path d="M15 6h5v5"/></svg>',
  irdai: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 3 4.5 6v5.5c0 4.6 3.2 8 7.5 9.5 4.3-1.5 7.5-4.9 7.5-9.5V6z"/><path d="m9 12 2.2 2.2L15.5 10"/></svg>',
  jud: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 4v16M7 20h10"/><path d="M5 7h14"/><path d="m5 7-3 6a3 3 0 0 0 6 0zM19 7l-3 6a3 3 0 0 0 6 0z"/></svg>',
  misc: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.5"/></svg>',
  search: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
  moon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg>',
  sun: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
  arrow: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  ext: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>',
  map: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="2.5"/><circle cx="4.5" cy="5" r="1.8"/><circle cx="19.5" cy="5" r="1.8"/><circle cx="4.5" cy="19" r="1.8"/><circle cx="19.5" cy="19" r="1.8"/><path d="m6 6.3 4.2 4M18 6.3l-4.2 4M6 17.7l4.2-4M18 17.7l-4.2-4"/></svg>',
  logo: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3v18M3 12h18M5.6 5.6l12.8 12.8M18.4 5.6 5.6 18.4"/></svg>',
  gavel: '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><g fill="currentColor"><rect x="9" y="2.5" width="11" height="6" rx="1.5" transform="rotate(45 14.5 5.5)"/><rect x="2" y="13.2" width="11" height="2.8" rx="1.2" transform="rotate(-45 7.5 14.6)"/><rect x="11" y="19" width="11" height="2.6" rx="1.2"/></g></svg>',
};
const JUDGE_SVG = `<svg viewBox="0 0 64 64" aria-hidden="true" class="jsvg">
  <path d="M10 64c2-12 10-18 22-18s20 6 22 18z" fill="#1F1E1D"/>
  <path d="M27 46h10l-2 10h-6z" fill="#FFFFFF"/><path d="M32 47v9" stroke="#C9C4BA" stroke-width="1"/>
  <g fill="#F4F1EA" stroke="#BDB6A8" stroke-width="1.2">
    <circle cx="14" cy="40" r="5"/><circle cx="50" cy="40" r="5"/><circle cx="13" cy="32" r="5.2"/><circle cx="51" cy="32" r="5.2"/>
    <circle cx="15" cy="24" r="5.4"/><circle cx="49" cy="24" r="5.4"/><circle cx="20" cy="16" r="6"/><circle cx="44" cy="16" r="6"/>
    <circle cx="32" cy="12" r="7.5"/><circle cx="26" cy="13" r="6"/><circle cx="38" cy="13" r="6"/>
  </g>
  <ellipse cx="32" cy="31" rx="12" ry="14" fill="#F2C8A0"/>
  <path d="M21 22c4-5 18-5 22 0" fill="#F4F1EA" stroke="#BDB6A8" stroke-width="1.2"/>
  <g fill="none" stroke="#1F1E1D" stroke-width="1.6"><circle cx="27" cy="31" r="3.4"/><circle cx="37" cy="31" r="3.4"/><path d="M30.4 31h3.2"/></g>
  <g class="jeyes" fill="#1F1E1D"><circle cx="27" cy="31" r="1.2"/><circle cx="37" cy="31" r="1.2"/></g>
  <path d="M23.5 25.5l6-1.2M40.5 25.5l-6-1.2" stroke="#7A6A58" stroke-width="1.6" stroke-linecap="round"/>
  <path d="M28 39c2.5 1.6 5.5 1.6 8 0" fill="none" stroke="#9A5B3E" stroke-width="1.6" stroke-linecap="round"/>
</svg>`;

/* ---------- theme + chrome ---------- */
function applyTheme(t) {
  if (t === "light" || t === "dark") document.documentElement.dataset.theme = t; else delete document.documentElement.dataset.theme;
  const b = $("#themebtn"); if (!b) return;
  const dark = isDark(); b.innerHTML = dark ? I.sun : I.moon; b.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
}
function isDark() { return document.documentElement.dataset.theme === "dark"; }  /* light by default; dark only when chosen */
applyTheme(store.get("theme", ""));

function renderChrome(hub, opts) {
  const root = opts.root || "";
  const nav = hub.sections.map(s => `<a href="${s.status === "live" ? root + s.href : root + "#" + s.id}" class="${s.id === opts.active ? "on" : ""} ${s.status === "live" ? "" : "soon"}">${esc(s.short)}</a>`).join("");
  const crumb = opts.crumb ? `<span class="crumb">${opts.crumb}</span>` : "";
  $("#top").innerHTML = `<a class="brand" href="${root || "./"}"><span class="logo">${I.logo}</span><span><b>${esc(hub.title)}</b><small>${esc(opts.sub || hub.tagline)}</small></span></a>${crumb}
    <nav class="nav" aria-label="Regulators">${nav}<button class="iconbtn" id="themebtn" type="button"></button></nav>`;
  $("#top").className = "top";
  applyTheme(store.get("theme", ""));
  $("#themebtn").addEventListener("click", () => { const t = isDark() ? "light" : "dark"; store.set("theme", t); applyTheme(t); });
  const f = $("#foot");
  if (f) { f.className = "foot"; f.innerHTML = `<span><b>Not legal advice.</b> An independent, unofficial summary for general information. It may be incomplete or out of date and is not endorsed by any regulator. Verify every point against the official text before relying on it.</span><span id="asof"></span>`; }
  document.addEventListener("keydown", e => {
    if (e.key === "/" && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) { const q = $(".search input"); if (q) { e.preventDefault(); q.focus(); } }
  });
}

/* ---------- section data model (RBI-style register) ---------- */
const LAYERS = [["CAT-BL", "Base Layer", "bl"], ["CAT-ML", "Middle Layer", "ml"], ["CAT-UL", "Upper Layer", "ul"], ["CAT-TL", "Top Layer", "tl"]];
const cleanName = s => String(s || "").replace(/^Master Directions? [–-] /, "").replace(/^Reserve Bank of India \(([^)]*)\) /, "");
const stripChecked = s => String(s || "").replace(/\s*\((?:re)?checked[^)]*\)/gi, "").replace(/\s*\[(?:re)?checked[^\]]*\]/gi, "");
function statusClass(st) { st = String(st || "").toLowerCase(); return /supersed|repeal|withdrawn/.test(st) ? "old" : /draft/.test(st) ? "draft" : "live"; }
function splitPara(line) {
  const m = String(line).match(/^((?:paras?|sections?|ss?\.|chapter|annex|rule|regulation|reg\.)\s*[^:]{1,40}):\s*(.+)$/i);
  return m ? [m[1].replace(/^paras?\s*/i, "para ").replace(/^sections?\s*/i, "s. "), m[2]] : ["", String(line)];
}
async function loadSection(sec, base) {
  const p = x => base + x;
  const [reg, graph, defs, gloss, upd] = await Promise.all([
    getJSON(p(sec.data.register)), getJSON(p(sec.data.graph)).catch(() => null),
    sec.data.definitions ? getJSON(p(sec.data.definitions)).catch(() => null) : null,
    sec.data.glossary ? getJSON(p(sec.data.glossary)).catch(() => null) : null,
    sec.data.updates ? getJSON(p(sec.data.updates)).catch(() => null) : null]);
  const M = { sec, base, meta: reg.meta || {}, items: [], byId: new Map(), themes: [], defs: [], gloss: [], updates: [], updMeta: {}, layerMin: new Map(), lensOf: new Map(), links: new Map(), applyBasis: new Map() };
  /* lenses: RBI uses the cumulative SBR layers; other sections name their own entity lenses in hub.json */
  M.lenses = sec.lenses ? sec.lenses.map(l => [l.id, l.name, l.key || l.id.toLowerCase(), l.desc || ""]) : LAYERS;
  M.cumulative = sec.lenses ? !!sec.cumulative : true;
  reg.instruments.forEach(r => {
    const it = {
      id: r.id, label: cleanName(r.short_name || r.title), title: r.title, type: r.type, theme: r.theme, status: r.status || "",
      sc: statusClass(r.status), url: r.official_url, pdf: r.official_pdf, ref: r.reference_no, issue: r.issue_date, updated: r.updated_as_on,
      effective: r.effective_date, dept: r.issuing_department, powers: r.statutory_powers || [], applies: r.applies_to || [], excluded: r.excluded || [],
      concepts: r.key_concepts || [], obl: r.core_obligations || [], time: r.timelines || [], cons: r.consequences_stated || [],
      consGen: r.consequences_general || "", xrefs: r.cross_references || [], repeals: r.repeals || "", raw: r
    };
    if (it.type === "Superseded instrument") it.sc = "old";
    M.items.push(it); M.byId.set(it.id, it);
  });
  // subjects in the order given by the section config
  const order = sec.subjects || [];
  const byTheme = new Map();
  M.items.forEach(it => { if (!byTheme.has(it.theme)) byTheme.set(it.theme, []); byTheme.get(it.theme).push(it); });
  const names = [...order.map(o => o.theme).filter(t => byTheme.has(t)), ...[...byTheme.keys()].filter(t => !order.some(o => o.theme === t))];
  names.forEach((t, i) => {
    const o = order.find(x => x.theme === t) || {};
    M.themes.push({ name: t, nice: o.nice || t, slug: (o.slug || t.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "")), idx: (i % 6) + 1, history: !!o.history, items: byTheme.get(t).sort((a, b) => (a.sc === "old") - (b.sc === "old")) });
  });
  M.themeOf = new Map(); M.themes.forEach(t => t.items.forEach(it => M.themeOf.set(it.id, t)));
  if (graph) {
    const li = new Map(M.lenses.map((l, i) => [l[0], i]));
    graph.edges.forEach(e => {
      if (e.relation === "applies_to" && li.has(e.target) && !M.cumulative) {
        if (!M.lensOf.has(e.source)) M.lensOf.set(e.source, new Set());
        M.lensOf.get(e.source).add(li.get(e.target));
        if (e.basis && !M.applyBasis.has(e.source)) M.applyBasis.set(e.source, stripChecked(e.basis));
      } else if (e.relation === "applies_to" && li.has(e.target)) {
        const cur = M.layerMin.get(e.source); const v = li.get(e.target);
        if (cur === undefined || v < cur) { M.layerMin.set(e.source, v); M.applyBasis.set(e.source, stripChecked(e.basis)); }
      } else if (e.relation !== "applies_to" && e.relation !== "issued_under" && M.byId.has(e.source) && M.byId.has(e.target)) {
        const add = (a, b, rel) => { if (!M.links.has(a)) M.links.set(a, []); if (!M.links.get(a).some(x => x.id === b)) M.links.get(a).push({ id: b, rel }); };
        add(e.source, e.target, e.relation); add(e.target, e.source, e.relation === "supersedes" ? "superseded_by" : e.relation === "migrated_from" ? "migrated_to" : e.relation);
      } else if (e.relation === "issued_under" && M.byId.has(e.source) && M.byId.has(e.target)) {
        const add = (a, b, rel) => { if (!M.links.has(a)) M.links.set(a, []); if (!M.links.get(a).some(x => x.id === b)) M.links.get(a).push({ id: b, rel }); };
        add(e.source, e.target, "issued_under");
      }
    });
  }
  if (defs) Object.entries(defs.instruments || {}).forEach(([id, arr]) => arr.forEach(d => M.defs.push({ id, ...d })));
  if (gloss) M.gloss = gloss.terms || [];
  if (upd) { M.updates = (upd.updates || []).slice().sort((a, b) => String(b.date).localeCompare(String(a.date))); M.updMeta = upd.meta || {}; }
  buildIndex(M);
  return M;
}
/* applies to a layer: tagged to that layer or a lower one (SBR layers are cumulative), or not layer-specific */
function appliesAt(M, it, L) {
  if (it.sc === "old") return false;
  if (L < 0) return true;
  if (M.cumulative === false) { const s = M.lensOf.get(it.id); return !s || s.has(L); }
  const m = M.layerMin.get(it.id); return m === undefined || m <= L;
}
function layerNote(M, it) {
  if (M.cumulative === false) {
    const s = M.lensOf.get(it.id);
    return !s ? (M.sec.lensAll || "Applies generally") : s.size === M.lenses.length ? "All entity types" : [...s].sort().map(i => M.lenses[i][1]).join(", ");
  }
  const m = M.layerMin.get(it.id);
  return m === undefined ? "Not tied to a layer" : m === 0 ? "All layers" : `${LAYERS[m][1]} and above`;
}

/* ---------- search ---------- */
const STOP = new Set("a an and are as at be by can do does for from has have how i if in is it its may me must my no not of on or our shall should that the their there this to under us was we what when where which who whom why will with would you your about any into than then them they".split(" "));
const tok = s => (String(s).toLowerCase().match(/[a-z0-9₹%]+(?:[.'-][a-z0-9]+)*/g) || []);
const FIELDS = [["label", "Name", 6], ["title", "Full title", 3], ["concepts", "Key concepts", 4], ["obl", "Obligation", 3], ["time", "Timeline", 2.5], ["cons", "If breached", 2.5], ["applies", "Applies to", 2], ["excluded", "Excluded", 1.5], ["xrefs", "Related", 1], ["powers", "Powers", 1], ["consGen", "General consequences", .3], ["status", "Status", .8], ["repeals", "Repeals", .8], ["dept", "Department", .5]];
function buildIndex(M) {
  M.docs = M.items.map(it => {
    const lines = [];
    FIELDS.forEach(([f, lab, w]) => { const v = it[f]; (Array.isArray(v) ? v : v ? [v] : []).forEach(x => lines.push({ f, lab, w, txt: String(x), toks: tok(x) })); });
    return { it, lines };
  });
  const df = new Map();
  M.docs.forEach(d => { const s = new Set(); d.lines.forEach(l => l.toks.forEach(t => s.add(t))); s.forEach(t => df.set(t, (df.get(t) || 0) + 1)); });
  M.df = df; M.vocab = [...df.keys()];
}
function parseQuery(M, raw) {
  const q = String(raw || "").trim();
  const P = { raw: q, groups: [], para: null, gl: [] };
  const pm = q.match(/\b(?:para(?:graph)?|section|s\.)\s*([0-9]+[A-Z]?(?:\([0-9a-z]+\))*)/i);
  if (pm) P.para = pm[1].toLowerCase();
  const lq = " " + q.toLowerCase().replace(/[^a-z0-9₹% ]+/g, " ") + " ";
  const used = new Set();
  M.gloss.forEach(t => {
    const names = [t.term, t.full, ...(t.aka || [])].filter(Boolean);
    const hit = names.find(n => { const x = n.toLowerCase().replace(/[^a-z0-9₹% ]+/g, " ").trim(); return x.length > 1 && lq.includes(" " + x + " "); });
    if (hit && !["NBFC", "NBFI"].includes(t.term)) { P.gl.push(t); P.groups.push({ label: hit, alts: names.map(n => n.toLowerCase()) }); tok(hit).forEach(w => used.add(w)); }
  });
  tok(q).forEach(w => { if (!STOP.has(w) && !used.has(w) && !(P.para && (w === P.para || /^(para|paragraph|section|s)$/.test(w)))) P.groups.push({ label: w, alts: [w] }); });
  return P;
}
function wordsFor(M, alt) {
  // a phrase alt is matched as a phrase; single words also match by prefix (len>=4) and simple plural
  const ws = tok(alt); if (ws.length !== 1) return { phrase: alt.toLowerCase() };
  const w = ws[0], set = new Set([w, w + "s", w.replace(/s$/, "")]);
  if (w.length >= 4) M.vocab.forEach(v => { if (v.startsWith(w)) set.add(v); });
  return { words: set };
}
function rankDocs(M, P, opts = {}) {
  if (!P.groups.length && !P.para) return [];
  const N = M.docs.length, matchers = P.groups.map(g => g.alts.map(a => wordsFor(M, a)));
  const idfs = P.groups.map((g, gi) => { let n = 0; M.docs.forEach(d => { if (d.lines.some(l => hitLine(l, matchers[gi]))) n++; }); return Math.log(1 + N / (1 + n)); });
  const out = [];
  M.docs.forEach(d => {
    if (opts.layer !== undefined && !appliesAt(M, d.it, opts.layer) && d.it.sc !== "old") return;
    let sc = 0, cov = 0; const hits = [];
    matchers.forEach((m, gi) => {
      let best = 0;
      d.lines.forEach(l => { if (hitLine(l, m)) { best += l.w; if (!hits.includes(l)) hits.push(l); } });
      if (best) { cov++; sc += idfs[gi] * Math.min(best, 12); }
    });
    if (P.para) d.lines.forEach(l => { if (new RegExp(`\\b(?:para|paras|s\\.|section)\\s*[^:]*\\b${P.para.replace(/[()]/g, "\\$&")}\\b`, "i").test(l.txt)) { sc += 6; if (!hits.includes(l)) hits.push(l); if (!P.groups.length) cov = 1; } });
    if (!sc) return;
    const G = Math.max(1, P.groups.length);
    sc *= Math.pow(Math.max(cov, P.para ? 1 : 0) / G, 1.5);
    if (d.it.sc === "old") sc *= 0.6;
    hits.sort((a, b) => b.w - a.w);
    out.push({ it: d.it, sc, hits });
  });
  out.sort((a, b) => b.sc - a.sc);
  const top = out[0] ? out[0].sc : 1; out.forEach(o => o.rel = o.sc / top);
  return out;
}
function hitLine(l, ms) {
  const low = l.txt.toLowerCase();
  return ms.some(m => m.phrase ? low.includes(m.phrase) : l.toks.some(t => m.words.has(t)));
}
function matchDefs(M, P) {
  if (!P.groups.length) return [];
  const words = P.groups.map(g => g.alts);
  const out = [];
  M.defs.forEach(d => {
    const term = d.term.toLowerCase();
    const ok = words.every(alts => alts.some(a => term.includes(a) || tok(a).every(w => tok(term).some(t => t.startsWith(w.slice(0, Math.max(4, w.length - 1)))))));
    if (!ok) return;
    let sc = 10 - Math.min(8, Math.abs(tok(term).length - P.groups.length) * 2);
    if (/^same meaning|^as defined|has the meaning/i.test(d.def)) sc -= 4;
    const it = M.byId.get(d.id); if (it && it.sc === "old") sc -= 3;
    out.push({ d, it, sc });
  });
  return out.sort((a, b) => b.sc - a.sc);
}
function hl(txt, P) {
  let s = esc(txt);
  const ws = [...new Set(P.groups.flatMap(g => g.alts).filter(a => a.length > 2))].sort((a, b) => b.length - a.length).slice(0, 12);
  ws.forEach(w => { s = s.replace(new RegExp(`(^|[^\\w>])(${w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\w*)`, "gi"), "$1<mark>$2</mark>"); });
  return s;
}

/* ---------- Not So Intelligent AI ---------- */
const FT = { state: "idle", p: null, chunks: [], idx: null, len: [], avg: 1 };
function loadFull(url) {
  if (FT.p) return FT.p;
  if (!url) { FT.state = "none"; return (FT.p = Promise.resolve(false)); }
  FT.state = "loading";
  FT.p = getJSON(url).then(j => {
    FT.chunks = j.chunks || []; const idx = new Map(); let tot = 0;
    FT.chunks.forEach((c, i) => {
      const toks = tok(c[3]); FT.len[i] = toks.length; tot += toks.length;
      const tf = new Map(); toks.forEach(w => tf.set(w, (tf.get(w) || 0) + 1));
      tf.forEach((n, w) => { let a = idx.get(w); if (!a) idx.set(w, a = []); a.push(i, n); });
    });
    FT.idx = idx; FT.vocab = [...idx.keys()]; FT.avg = tot / Math.max(1, FT.chunks.length); FT.state = "ready"; return true;
  }).catch(() => { FT.state = "failed"; return false; });
  return FT.p;
}
function ftExtracts(M, P, boost) {
  if (FT.state !== "ready" || !P.groups.length) return [];
  const N = FT.chunks.length, k1 = 1.2, b = 0.75, score = new Float64Array(N), cov = new Uint8Array(N);
  P.groups.forEach(g => {
    const words = new Set();
    g.alts.forEach(a => tok(a).forEach(w => { if (w.length >= 5) FT.vocab.forEach(v => { if (v.startsWith(w)) words.add(v); }); else { words.add(w); words.add(w + "s"); } }));
    const tf = new Map();
    words.forEach(w => { const a = FT.idx.get(w); if (a) for (let i = 0; i < a.length; i += 2) tf.set(a[i], (tf.get(a[i]) || 0) + a[i + 1]); });
    if (!tf.size) return;
    const idf = Math.log(1 + (N - tf.size + .5) / (tf.size + .5));
    tf.forEach((n, i) => { score[i] += idf * n * (k1 + 1) / (n + k1 * (1 - b + b * FT.len[i] / FT.avg)); cov[i]++; });
  });
  const G = P.groups.length, hits = [];
  for (let i = 0; i < N; i++) if (score[i]) { let sc = score[i] * Math.pow(cov[i] / G, 2); if (boost.has(FT.chunks[i][0])) sc *= 1.25; if (FT.chunks[i][2] === "footnotes") sc *= .5; hits.push([sc, i]); }
  hits.sort((x, y) => y[0] - x[0]);
  let budget = 60000; const out = [];
  for (const [, i] of hits.slice(0, 30)) {
    const [id, chap, para, txt] = FT.chunks[i], lab = M.byId.has(id) ? M.byId.get(id).label : id;
    const e = `[${id}] FULL TEXT of ${lab}${chap ? `, ${chap}` : ""}${para && para !== "footnotes" ? `, ${/^ACT-/.test(id) ? "section" : /^REG-/.test(id) ? "regulation" : /^RULES-/.test(id) ? "rule" : "para"} ${para}` : ""}:\n${txt}`;
    if (e.length > budget) break; budget -= e.length; out.push(e);
  }
  return out;
}
function aiExtracts(M, P, docs) {
  const out = [];
  matchDefs(M, P).slice(0, 6).forEach(x => out.push(`[${x.d.id}] DEFINITION in ${x.it ? x.it.label : x.d.id}${x.it && x.it.sc === "old" ? " [SUPERSEDED]" : ""}, ${x.d.para}${x.d.scope ? ` (applies: ${x.d.scope})` : ""}: "${x.d.term}" — ${x.d.def}`));
  P.gl.slice(0, 2).forEach(t => out.push(`[GLOSSARY ${t.term}] ${t.full || ""}: ${t.def}`));
  docs.slice(0, 5).forEach(d => {
    const lines = d.hits.filter(x => x.lab !== "Name").slice(0, docs.length <= 2 ? 12 : 6).map(x => `- ${x.lab}: ${x.txt.slice(0, 300)}`);
    out.push(`[${d.it.id}] ${d.it.label}${d.it.title && d.it.title !== d.it.label ? ` (${d.it.title})` : ""}${d.it.sc === "old" ? " [SUPERSEDED]" : ""}\n${lines.join("\n")}`);
  });
  return out;
}
const Judge = { M: null, endpoint: "", fulltext: "", link: id => "#d/" + id, scope: "", section: "rbi", docs: "the Directions",
  intro: "Put your question on RBI regulation of NBFCs and I shall answer from the Directions on this site, citing the paragraph. Check what I say.",
  tries: [["Is the term project finance defined?", "Is project finance defined?"], ["What is the LTV limit for gold loans?", "LTV for gold loans"], ["Who is a wilful defaulter?", "Who is a wilful defaulter?"]],
  placeholder: "Ask a question, e.g. When must an NBFC report fraud?" };
function judgeMsg(role, html) { const log = $("#jlog"), el = document.createElement("div"); el.className = "jmsg " + role; el.innerHTML = html; log.appendChild(el); log.scrollTop = log.scrollHeight; return el; }
function openJudge(prefill) {
  const w = $("#judge"); if (!w) return; loadFull(Judge.fulltext);
  w.hidden = false; $("#jfab").setAttribute("aria-expanded", "true"); $("#jfab").classList.add("open");
  const t = $("#jq"); if (prefill) t.value = prefill; setTimeout(() => t.focus(), 30);
}
function closeJudge() { const w = $("#judge"); if (!w) return; w.hidden = true; $("#jfab").setAttribute("aria-expanded", "false"); $("#jfab").classList.remove("open"); }
function aiFormat(t) {
  const M = Judge.M;
  return esc(t).split(/\n{2,}/).map(par => `<p>${par.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>").replace(/\n/g, "<br>").replace(/\[([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)\]/g, (m, id) => M && M.byId.has(id) ? `<a class="lnk" href="${Judge.link(id)}">${id}</a>` : m)}</p>`).join("");
}
async function askJudge() {
  const t = $("#jq"), raw = t.value.trim(), btn = $("#jsend"), M = Judge.M;
  if (raw.length < 3 || btn.disabled) return;
  t.value = ""; judgeMsg("me", esc(raw));
  const wait = judgeMsg("bot thinking", `<span class="dots"><i></i><i></i><i></i></span> ${FT.state === "ready" ? `Reading ${Judge.docs}…` : `Opening the full text of ${Judge.docs} (first question only)…`}`);
  btn.disabled = true;
  try {
    let ext = [], docs = [];
    if (M) {
      const P = parseQuery(M, raw); docs = rankDocs(M, P);
      await loadFull(Judge.fulltext);
      const boost = new Set(docs.slice(0, 5).map(d => d.it.id)); matchDefs(M, P).forEach(x => boost.add(x.d.id));
      ext = [...ftExtracts(M, P, boost), ...aiExtracts(M, P, docs)];
    }
    const post = x => fetch(Judge.endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ question: raw.slice(0, 500), extracts: x, section: Judge.section }) });
    let r = await post(ext);
    if (r.status === 413) { const small = []; let room = 14000; for (const x of ext) { const y = x.slice(0, 1800); if (y.length > room) break; small.push(y); room -= y.length; } r = await post(small.slice(0, 8)); }
    const j = await r.json().catch(() => ({}));
    wait.classList.remove("thinking");
    const more = docs.slice(0, 3).map(d => `<a class="lnk" href="${Judge.link(d.it.id)}">${esc(trunc(d.it.label, 40))}</a>`).join(" · ");
    wait.innerHTML = j.answer ? aiFormat(j.answer) + (more ? `<p class="jsrc">Read further: ${more}</p>` : "") : `<p>${esc(j.error || "Not So Intelligent AI is not available right now. Please try again later, or use the search box.")}</p>`;
  } catch (e) {
    wait.classList.remove("thinking");
    wait.innerHTML = `<p>Not So Intelligent AI could not be reached. Please check your connection, or use the search box.</p>`;
  }
  btn.disabled = false; $("#jlog").scrollTop = $("#jlog").scrollHeight;
}
function initJudge(opts) {
  Object.assign(Judge, opts);
  if (!Judge.endpoint || $("#jfab")) return;
  const fab = document.createElement("button");
  fab.id = "jfab"; fab.type = "button"; fab.setAttribute("aria-controls", "judge"); fab.setAttribute("aria-expanded", "false");
  fab.setAttribute("aria-label", "Ask Not So Intelligent AI, the AI assistant"); fab.title = "Ask Not So Intelligent AI";
  fab.innerHTML = `${JUDGE_SVG}<span class="jtag">Ask Not So Intelligent AI</span>`;
  if (opts.wide) fab.classList.add("wide");
  const w = document.createElement("section");
  w.id = "judge"; w.hidden = true; w.setAttribute("role", "dialog"); w.setAttribute("aria-label", "Not So Intelligent AI");
  w.innerHTML = `<header>${JUDGE_SVG}<div><b>Not So Intelligent AI</b><span>${esc(Judge.scope || "Answers from the RBI texts on this site")}</span></div><button class="iconbtn" id="jclose" type="button" aria-label="Close">✕</button></header>
  <div id="jlog" aria-live="polite"><div class="jmsg bot"><p><b>Order, order!</b> I am Not So Intelligent AI. ${esc(Judge.intro)}</p><p class="jtry">Try: ${Judge.tries.map(([q, t]) => `<button class="lnk" data-try="${esc(q)}">${esc(t)}</button>`).join(" · ")}</p></div></div>
  <form id="jform"><label class="sr" for="jq">Your question</label><textarea id="jq" rows="2" maxlength="500" placeholder="${esc(Judge.placeholder)}"></textarea><button id="jsend" type="submit" aria-label="Ask">${I.gavel}</button></form>
  <p class="jdisc">AI-generated answers can be wrong. Not legal advice: read the official text. Each question is answered on its own.</p>`;
  document.body.appendChild(w); document.body.appendChild(fab);
  fab.addEventListener("click", () => w.hidden ? openJudge() : closeJudge());
  $("#jclose").addEventListener("click", closeJudge);
  $("#jform").addEventListener("submit", e => { e.preventDefault(); askJudge(); });
  $("#jq").addEventListener("keydown", e => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); askJudge(); } });
  w.addEventListener("keydown", e => { if (e.key === "Escape") closeJudge(); });
  w.addEventListener("click", e => {
    const tr = e.target.closest("[data-try]"); if (tr) { $("#jq").value = tr.dataset.try; askJudge(); return; }
    if (e.target.closest("a.lnk") && innerWidth < 700) closeJudge();
  });
}

/* count-up animation for stat numbers */
function countUp(el, to, ms = 900) {
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) { el.textContent = to.toLocaleString("en-IN"); return; }
  const t0 = performance.now();
  const step = t => { const k = Math.min(1, (t - t0) / ms), v = Math.round(to * (1 - Math.pow(1 - k, 3))); el.textContent = v.toLocaleString("en-IN"); if (k < 1) requestAnimationFrame(step); };
  requestAnimationFrame(step);
}
