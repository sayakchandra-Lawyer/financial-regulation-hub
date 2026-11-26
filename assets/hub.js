/* Financial Regulation Hub: shared engine (header, theme, data loading, search, Counsel’s Clerk) */
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
  fema: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.4 2.4 3.5 5.3 3.5 8.5s-1.1 6.1-3.5 8.5M12 3.5C9.6 5.9 8.5 8.8 8.5 12s1.1 6.1 3.5 8.5"/></svg>',
  dpdp: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 3 4.5 6v5.5c0 4.4 3.1 8.3 7.5 9.5 4.4-1.2 7.5-5.1 7.5-9.5V6z"/><rect x="9" y="11" width="6" height="5" rx="1"/><path d="M10.2 11V9.6a1.8 1.8 0 0 1 3.6 0V11"/></svg>',
  ibc: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19.5 12a7.5 7.5 0 1 1-2.2-5.3"/><path d="M19.8 4.5v3.6h-3.6"/><path d="M8.5 12.5h7M8.5 15h4.5"/><path d="M10 9.5h4"/></svg>',
  ifsc: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20.5h16"/><path d="M6 20.5V10l4-2v12.5"/><path d="M10 20.5V5l6 2.5v13"/><path d="M16 20.5v-8l3 1.5v6.5"/><path d="M12.5 10h1M12.5 13h1M12.5 16h1"/></svg>',
  exchanges: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 20.5h17"/><path d="M4 16l4.5-5 3.5 3 4-5.5 4 3.5"/><path d="M16 8.5h4v4"/><path d="M6 20.5v-2M10 20.5v-3.5M14 20.5v-2.5M18 20.5v-4"/></svg>',
  companies: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20.5V8l8-4.5L20 8v12.5"/><path d="M2.5 20.5h19"/><path d="M8 11v6M12 11v6M16 11v6"/><path d="M7 8.5h10"/></svg>',
  misc: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.5"/></svg>',
  search: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
  moon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg>',
  sun: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
  arrow: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  ext: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>',
  map: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="2.5"/><circle cx="4.5" cy="5" r="1.8"/><circle cx="19.5" cy="5" r="1.8"/><circle cx="4.5" cy="19" r="1.8"/><circle cx="19.5" cy="19" r="1.8"/><path d="m6 6.3 4.2 4M18 6.3l-4.2 4M6 17.7l4.2-4M18 17.7l-4.2-4"/></svg>',
  menu: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
  close: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
  logo: '<svg width="28" height="28" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="16" cy="16" r="14" stroke-width="1.6" opacity=".9"/><circle cx="16" cy="16" r="11.6" stroke-width=".9" stroke-dasharray="1.2 2" opacity=".7"/><path transform="translate(5.8 5.4) scale(.85)" stroke-width="2.4" d="M6 4.5h12M6 9h12M8.5 4.5h1.5a4.5 4.5 0 0 1 0 9H6.5l7.5 7"/></svg>',
  grow: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M14 4h6v6M10 20H4v-6M20 4l-7 7M4 20l7-7"/></svg>',
  shrink: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M20 10h-6V4M4 14h6v6M14 10l7-7M10 14l-7 7"/></svg>',
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
  const sys = typeof SYS_DARK !== "undefined" && SYS_DARK && SYS_DARK.matches ? "dark" : "light";
  document.documentElement.dataset.theme = t === "light" || t === "dark" ? t : sys;
  const b = $("#themebtn"); if (!b) return;
  const dark = isDark(); b.innerHTML = dark ? I.sun : I.moon; b.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
}
/* follow the device's light/dark setting until the reader picks one with the toggle */
const SYS_DARK = window.matchMedia ? matchMedia("(prefers-color-scheme: dark)") : null;
function isDark() { const t = document.documentElement.dataset.theme; return t ? t === "dark" : !!(SYS_DARK && SYS_DARK.matches); }
applyTheme(store.get("theme", ""));
if (SYS_DARK && SYS_DARK.addEventListener) SYS_DARK.addEventListener("change", () => applyTheme(store.get("theme", "")));
/* entrance animations only when the page is actually on screen, so content never stays hidden at opacity 0 */
if (document.visibilityState === "visible" && !(window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches)) document.documentElement.classList.add("anim");

function renderChrome(hub, opts) {
  const root = opts.root || "";
  const nav = hub.sections.filter(s => s.status === "live").map(s => `<a href="${s.status === "live" ? root + s.href : root + "#" + s.id}" class="${s.id === opts.active ? "on" : ""} ${s.status === "live" ? "" : "soon"}">${esc(s.short)}</a>`).join("") + (hub.tools || []).map(t => `<a href="${root + t.href}" class="${t.id === opts.active ? "on" : ""}" title="${esc(t.name || t.short)}">${esc(t.short)}</a>`).join("");
  const crumb = opts.crumb ? `<span class="crumb">${opts.crumb}</span>` : "";
  $("#top").innerHTML = `<a class="brand" href="${root || "./"}"><span class="logo">${I.logo}</span><span><b>${esc(hub.title)}</b><small>${esc(opts.sub || hub.tagline)}</small></span></a>${crumb}
    <nav class="nav" aria-label="Regulators"><div class="navl" id="navl">${nav}</div><button class="iconbtn" id="themebtn" type="button"></button><button class="iconbtn" id="menubtn" type="button" aria-label="Menu" aria-expanded="false" aria-controls="navl">${I.menu}</button></nav>`;
  $("#top").className = "top";
  const mb = $("#menubtn"), nl = $("#navl");
  const setMenu = on => { nl.classList.toggle("open", on); mb.setAttribute("aria-expanded", on ? "true" : "false"); mb.innerHTML = on ? I.close : I.menu; };
  mb.addEventListener("click", e => { e.stopPropagation(); setMenu(!nl.classList.contains("open")); });
  document.addEventListener("click", e => { if (!e.target.closest("#navl")) setMenu(false); });
  document.addEventListener("keydown", e => { if (e.key === "Escape") setMenu(false); });
  nl.addEventListener("click", e => { if (e.target.closest("a")) setMenu(false); });
  applyTheme(store.get("theme", ""));
  $("#themebtn").addEventListener("click", () => { const t = isDark() ? "light" : "dark"; store.set("theme", t); applyTheme(t); });
  const f = $("#foot");
  if (f) {
    f.className = "foot";
    const fl = [["about/", "About"], ["feedback/", "Feedback"], ["contact/", "Contact"], ["disclaimer/", "Disclaimer & privacy"]];
    f.innerHTML = `<nav class="flinks" aria-label="Site">${fl.map(([h, t]) => `<a href="${root}${h}"${opts.active === h.slice(0, -1) ? ' aria-current="page"' : ""}>${t}</a>`).join("")}</nav><span><b>Not legal advice.</b> An independent, unofficial summary for general information. It may be incomplete or out of date and is not endorsed by any regulator. Verify every point against the official text before relying on it.</span><span id="asof"></span>`;
    /* the Feedback link carries the page the reader was on, so the form can prefill it */
    const fb = f.querySelector(`a[href="${root}feedback/"]`);
    if (fb && opts.active !== "feedback") fb.addEventListener("click", () => { fb.href = `${root}feedback/?from=${encodeURIComponent(location.pathname + location.hash)}`; });
  }
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
  const pw = tok(P.raw).flatMap(w => w.split(/[.'-]/)).filter(Boolean), phrase = pw.length > 1 ? new RegExp("(^|[^a-z0-9])" + pw.map(w => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("[\\s\\-–/,]+") + "($|[^a-z0-9])", "i") : null;
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
    // the words typed together, in that order, rank first
    let exact = false;
    if (phrase) { const ph = d.lines.filter(l => phrase.test(l.txt)); if (ph.length) { exact = true; sc *= 3; ph.forEach(l => { const k = hits.indexOf(l); if (k >= 0) hits.splice(k, 1); }); hits.unshift(...ph.sort((a, b) => b.w - a.w)); } }
    out.push({ it: d.it, sc, hits, full: exact || cov >= G, exact });
  });
  // when some instruments hold every word, leave out those that hold only some
  if (P.groups.length > 1 && out.some(o => o.full)) { const keep = out.filter(o => o.full); out.length = 0; out.push(...keep); }
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
  const ws = [...new Set([...(tok(P.raw).length > 1 ? [tok(P.raw).join(" ")] : []), ...P.groups.flatMap(g => g.alts)].filter(a => a.length > 2))].sort((a, b) => b.length - a.length).slice(0, 12);
  ws.forEach(w => { s = s.replace(new RegExp(`(^|[^\\w>])(${w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\w*)`, "gi"), "$1<mark>$2</mark>"); });
  return s;
}

/* ---------- whole-site search: prebuilt index over every full text and judgment (search/, built by tools/build_search.py) ---------- */
const SX = { root: "", meta: null, mp: null, vocab: null, common: null, bigCommon: null, shards: new Map(), texts: new Map(), cache: new Map() };
const SX_NAME = { rbi: "RBI", sebi: "SEBI", irdai: "IRDAI", fema: "FEMA", dpdp: "DPDP", ibc: "IBC", ifsc: "IFSC", exchanges: "Stock exchanges", companies: "Companies Act", judgments: "Judgments" };
const sxTok = s => (String(s).toLowerCase().match(/[a-z0-9₹%]+/g) || []);
const CRC = (() => { const t = new Uint32Array(256); for (let n = 0; n < 256; n++) { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; t[n] = c >>> 0; } return t; })();
function crc32(str) { const b = new TextEncoder().encode(str); let c = 0xFFFFFFFF; for (const x of b) c = CRC[(c ^ x) & 255] ^ (c >>> 8); return (c ^ 0xFFFFFFFF) >>> 0; }
function sxLoad() {
  if (!SX.mp) SX.mp = fetch(SX.root + "search/meta.json").then(r => { if (!r.ok) throw 0; return r.json(); }).then(m => {
    SX.meta = m; SX.vocab = m.vocab.split(" "); SX.dfOf = new Map(SX.vocab.map((w, i) => [w, m.df[i]]));
    SX.common = new Set(m.common); SX.bigCommon = new Set(m.bigCommon); SX.avg = m.plen.reduce((a, b) => a + b, 0) / m.n; return m;
  }).catch(() => (SX.mp = null, null));
  return SX.mp;
}
function sxGet(map, url) { if (!map.has(url)) map.set(url, fetch(url).then(r => r.ok ? r.json() : null).catch(() => (map.delete(url), null))); return map.get(url); }
async function sxPost(term) {
  const sh = await sxGet(SX.shards, `${SX.root}search/p/${crc32(term) % SX.meta.shards}.json`);
  const s = sh && sh[term]; if (!s) return null;
  const out = new Map(); let id = 0;
  s.split(",").forEach(e => { const [d, n] = e.split(":"); id += parseInt(d, 36); out.set(id, n ? parseInt(n, 36) : 1); });
  return out;
}
async function sxPassage(i) { const per = SX.meta.textPer, t = await sxGet(SX.texts, `${SX.root}search/t/${Math.floor(i / per)}.json`); return t ? t[i % per] : null; }
function sxExpand(w) {
  // the word itself, simple plural/singular forms, and longer words that start with it (5+ letters)
  const V = SX.vocab, set = new Set();
  [w, w + "s", w + "es", w.replace(/s$/, ""), w.replace(/es$/, "")].forEach(x => { if (x && SX.dfOf.has(x)) set.add(x); });
  const pre = p => { let lo = 0, hi = V.length; while (lo < hi) { const m = (lo + hi) >> 1; if (V[m] < p) lo = m + 1; else hi = m; }
    for (let i = lo; i < V.length && V[i].startsWith(p) && set.size < 25; i++) set.add(V[i]); };
  if (w.length >= 5) pre(w);
  // a light stem, so "securitisation" also finds "securitised" and "retention" finds "retained"
  const sf = ["isation", "ization", "ations", "ation", "ised", "ized", "ising", "izing", "ions", "ion", "ings", "ing", "ers", "er", "ed", "es", "s"].find(x => w.endsWith(x) && w.length - x.length >= 5);
  if (sf) pre(w.slice(0, w.length - sf.length));
  return [...set];
}
function sxParse(raw) {
  const q = String(raw || "").trim();
  const quoted = [...q.matchAll(/["“”]([^"“”]+)["“”]/g)].map(m => sxTok(m[1])).filter(a => a.length > 1);
  const all = sxTok(q), words = all.filter(w => !STOP.has(w));
  const terms = [...new Set(words.length ? words : all)];
  return { raw: q, all, terms, quoted, phrase: all.length > 1 ? all : null };
}
async function sxSearch(raw) {
  if (SX.cache.has(raw)) return SX.cache.get(raw);
  const m = await sxLoad(); if (!m) return null;
  const Q = sxParse(raw); if (!Q.terms.length) return null;
  const N = m.n, k1 = 1.2, b = .75, score = new Map(), cov = new Map();
  const groups = Q.terms.filter(t => !SX.common.has(t));
  const lists = await Promise.all(groups.map(async t => { const ws = sxExpand(t); const ps = await Promise.all(ws.map(w => sxPost(w).then(p => [w, p]))); return ps; }));
  lists.forEach(ps => {
    const tf = new Map(); ps.forEach(([w, p]) => { if (p) p.forEach((n, i) => tf.set(i, (tf.get(i) || 0) + (w === ps[0][0] ? n : n * .8))); });
    if (!tf.size) return;
    const idf = Math.log(1 + (N - tf.size + .5) / (tf.size + .5));
    tf.forEach((n, i) => { score.set(i, (score.get(i) || 0) + idf * n * (k1 + 1) / (n + k1 * (1 - b + b * m.plen[i] / SX.avg))); cov.set(i, (cov.get(i) || 0) + 1); });
  });
  // phrases: a passage holds the phrase when it holds every adjacent word pair of it
  const bigSets = async seq => { const pairs = []; for (let i = 0; i + 1 < seq.length; i++) { const k = seq[i] + " " + seq[i + 1]; if (!SX.bigCommon.has(k)) pairs.push(k); }
    if (!pairs.length) return null;
    const ps = await Promise.all(pairs.map(async (k, n) => { const a = await sxPost(k); if (n < pairs.length - 1 || /s$/.test(k)) return a;
      const b2 = await sxPost(k + "s"); if (!a) return b2; if (b2) b2.forEach((v, i) => a.set(i, v)); return a; }));  // last word may be plural
    if (ps.some(p => !p)) return new Set();
    ps.sort((x, y) => x.size - y.size); return new Set([...ps[0].keys()].filter(i => ps.every(p => p.has(i)))); };
  const req = await Promise.all(Q.quoted.map(bigSets));
  const phr = Q.phrase ? await bigSets(Q.phrase) : null;
  const G = Math.max(1, groups.length);
  let ids = [...score.keys()];
  req.forEach(s => { if (s) ids = ids.filter(i => s.has(i)); });
  if (phr) phr.forEach(i => { if (!score.has(i)) { score.set(i, 1); cov.set(i, G); ids.push(i); } });
  let full = ids.filter(i => cov.get(i) >= G || (phr && phr.has(i)));
  const partial = !full.length;
  if (!partial) ids = full;
  const pas = ids.map(i => { const exact = !!(phr && phr.has(i)); let sc = score.get(i) * Math.pow((cov.get(i) || 0) / G, 2) * (exact ? 3 : 1);
    const d = m.docs[m.pdoc[i]]; if (d[3]) sc *= .6; return { i, sc, exact, d: m.pdoc[i] }; }).sort((x, y) => y.sc - x.sc);
  const byDoc = new Map();
  pas.forEach(p => { let g = byDoc.get(p.d); if (!g) byDoc.set(p.d, g = { d: p.d, doc: m.docs[p.d], ps: [], sc: 0, exact: 0 }); g.ps.push(p); if (p.exact) g.exact++; });
  const docs = [...byDoc.values()].map(g => { g.sc = g.ps[0].sc + .15 * g.ps.slice(1, 6).reduce((a, p) => a + p.sc, 0); return g; }).sort((x, y) => y.sc - x.sc);
  const res = { Q, docs, n: pas.length, exactN: pas.filter(p => p.exact).length, partial };
  SX.cache.set(raw, res); return res;
}
function sxHl(txt, Q) {
  let s = esc(txt); const pats = [];
  if (Q.phrase) pats.push(Q.phrase.map(w => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("[\\s\\-–/,]+") + "\\w*");
  Q.quoted.forEach(a => pats.push(a.join("[\\s\\-–/,]+") + "\\w*"));
  Q.terms.filter(w => w.length > 1).sort((a, b) => b.length - a.length).forEach(w => pats.push(w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\w*"));
  if (!pats.length) return s;
  return s.replace(new RegExp(`(^|[^\\w])(${pats.join("|")})`, "gi"), "$1<mark>$2</mark>");
}
/* table text from PDFs: drop empty cells and runs of pipes so snippets read as prose */
const sxClean = t => String(t || "").replace(/\|(?:[ \t]*\|)+/g, "|").replace(/[ \t]*\|[ \t]*(?=\n|$)/g, "").replace(/(^|\n)[ \t]*\|[ \t]*/g, "$1").replace(/[ \t]*\|[ \t]*/g, " · ");
function sxSnippet(txt, Q, n = 300) {
  const low = txt.toLowerCase(); let at = -1;
  if (Q.phrase) { const re = new RegExp(Q.phrase.join("[\\s\\-–/,]+"), "i"); const mm = re.exec(txt); if (mm) at = mm.index; }
  if (at < 0) for (const w of Q.terms) { const j = low.search(new RegExp("\\b" + w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"))); if (j >= 0 && (at < 0 || j < at)) at = j; }
  let a = Math.max(0, at - Math.round(n * .35)); if (a > 0) { const sp = txt.indexOf(" ", a); if (sp > 0 && sp - a < 30) a = sp + 1; }
  const s = sxClean(txt.slice(a, a + n)).replace(/\s+/g, " ").trim();
  return (a > 0 ? "…" : "") + s + (a + n < txt.length ? "…" : "");
}
function sxWhere(doc, chap, para) {
  if (doc[0] === "judgments") return [chap, para ? fmtDate(para) : ""].filter(Boolean).join(" · ");
  const id = doc[1], unit = /^ACT-/.test(id) ? "Section" : /^REG-/.test(id) ? "Regulation" : /^RULES-/.test(id) ? "Rule" : "Para";
  const p = String(para || "").replace(/\s*\(contd\.\)/, "");
  return [chap, p === "footnotes" ? "Footnotes" : p ? `${unit} ${p}` : ""].filter(Boolean).join(" · ");
}
function sxHref(root, doc) { return doc[0] === "judgments" ? `${root}judgments/#j/${encodeURIComponent(doc[1])}` : `${root}${doc[0]}/#d/${encodeURIComponent(doc[1])}`; }
/* For a phrase of 2+ words that no instrument summary holds, the full-text passages are the better answer: show them first */
function sxFirst(raw, docs) {
  const el = $("#sxres"); if (!el || tok(raw).length < 2 || (docs || []).some(d => d.exact)) return false;
  const pg = el.parentNode, tgt = pg && pg.querySelector("h3"); if (tgt) { tgt.before(el); el.style.margin = "18px 0 6px"; }
  return true;
}
/* Render whole-site full-text results into el.  opts: { root: "" | "../", here: section id or "", compact: bool } */
async function sxMount(el, raw, opts = {}) {
  if (!el) return;
  SX.root = opts.root || ""; const tokn = (el._sx = (el._sx || 0) + 1);
  el.innerHTML = `<div class="rhead"><b>Found in the full text</b><span>Searching every Act, rule, direction and judgment…</span></div>`;
  const R = await sxSearch(raw); if (el._sx !== tokn) return;
  if (!R) { el.innerHTML = ""; return; }
  const Q = R.Q, here = opts.here || "", seen = new Set(R.docs.filter(g => g.doc[0] === here).map(g => g.doc[1]));
  const docs = R.docs.filter(g => g.doc[0] === here || (!seen.has(g.doc[1]) && seen.add(g.doc[1])));
  const mine = docs.filter(g => g.doc[0] === here), rest = docs.filter(g => g.doc[0] !== here);
  const lim = opts.compact ? 6 : 12, show = opts.compact ? docs.slice(0, lim) : [...mine.slice(0, lim), ...rest.slice(0, here ? 6 : lim)];
  if (opts.skipHere && !rest.length) { el.innerHTML = ""; return; }
  if (!R.docs.length) { el.innerHTML = `<div class="rhead"><b>Found in the full text</b><span>No passage contains these words.</span></div>`; return; }
  const secCount = {}; R.docs.forEach(g => secCount[g.doc[0]] = (secCount[g.doc[0]] || 0) + g.ps.length);
  await Promise.all(show.map(g => sxPassage(g.ps[0].i))); if (el._sx !== tokn) return;
  { // the same text kept under two sections (e.g. the FDI direction under RBI and FEMA) shows once
    const seenT = new Set();
    const keep = []; for (const g of [...show].sort((a, b) => (b.doc[0] === here) - (a.doc[0] === here))) { const p = await sxPassage(g.ps[0].i), t = p ? p[3].slice(0, 400) : g.d; if (!seenT.has(t)) { seenT.add(t); keep.push(g); } }
    for (let k = show.length - 1; k >= 0; k--) if (!keep.includes(show[k])) show.splice(k, 1);
  }
  const item = async (g) => {
    const [, chap, para, txt] = await sxPassage(g.ps[0].i) || [0, "", "", ""];
    const more = g.ps.length - 1, d = g.doc;
    return `<div class="res sx" data-d="${g.d}"><a class="t" href="${sxHref(SX.root, d)}">${esc(d[2])}</a> ${d[3] ? '<span class="pill p-old">Superseded</span>' : ""}
      <div class="m">${SX_NAME[d[0]] || d[0]}<span class="sep"></span>${esc(sxWhere(d, chap, para))}${g.ps[0].exact ? '<span class="sep"></span>Exact phrase' : ""}</div>
      <div class="s">${sxHl(sxSnippet(txt, Q), Q)}</div>
      <div class="sxa"><button class="lnk" type="button" data-read="${g.ps[0].i}">Read passage</button>${more ? `<button class="lnk" type="button" data-more="${g.d}">${more} more passage${more > 1 ? "s" : ""} in this document</button>` : ""}</div></div>`;
  };
  const head = (t, extra) => opts.compact ? `<div class="rhead"><b>${t}</b><span>${extra}</span></div>` : `<h3 style="font-size:19px">${t}</h3><p class="tag" style="margin:4px 0 8px">${extra}</p>`;
  const summary = `${R.n} passage${R.n === 1 ? "" : "s"} in ${R.docs.length} document${R.docs.length === 1 ? "" : "s"}${R.exactN && Q.phrase ? ` · ${R.exactN} with the exact phrase` : ""}${R.partial ? " · no passage has every word, closest matches shown" : ""}`;
  let h = "";
  if (opts.compact) h = head(R.exactN && Q.phrase ? "The exact words, in the full text" : "Found in the full text", summary) + (await Promise.all(show.map(item))).join("");
  else {
    h = head("Found in the full text", summary);
    if (here) {
      const m1 = show.filter(g => g.doc[0] === here), r1 = show.filter(g => g.doc[0] !== here);
      if (opts.skipHere) h = head("Also in the regulations", `${rest.reduce((a, g) => a + g.ps.length, 0)} passages in ${rest.length} documents`);
      else h += m1.length ? `<div class="card sxc">${(await Promise.all(m1.map(item))).join("")}</div>` : `<p class="empty" style="padding:6px 0">Nothing in ${SX_NAME[here] || "this section"}'s full texts.</p>`;
      if (r1.length) {
        const others = Object.keys(secCount).filter(k => k !== here).map(k => `<a class="chip" href="${k === "judgments" ? SX.root + "judgments/" : SX.root + k + "/"}#search/${encodeURIComponent(raw)}">${SX_NAME[k] || k} · ${secCount[k]}</a>`).join("");
        h += `${opts.skipHere ? "" : '<h3 style="font-size:17px;margin-top:20px">In other sections</h3>'}<div class="filter" style="margin:8px 0">${others}</div><div class="card sxc">${(await Promise.all(r1.map(item))).join("")}</div>`;
      }
    } else h += `<div class="card sxc">${(await Promise.all(show.map(item))).join("")}</div>`;
  }
  if (el._sx !== tokn) return;
  el.innerHTML = h;
  el.onclick = async e => {
    const rb = e.target.closest("[data-read]"), mb = e.target.closest("[data-more]");
    if (rb) {
      e.preventDefault(); e.stopPropagation();
      const box = rb.closest(".res"), open = box.querySelector(".sxp");
      if (open) { open.remove(); rb.textContent = "Read passage"; return; }
      const i = +rb.dataset.read, p = await sxPassage(i); if (!p) return; const d = SX.meta.docs[p[0]];
      const div = document.createElement("div"); div.className = "sxp";
      div.innerHTML = `<div class="m" style="margin-bottom:6px">${esc(sxWhere(d, p[1], p[2]))}</div><div class="sxt">${sxHl(sxClean(p[3]), Q)}</div><div class="sxa"><a class="lnk" href="${sxHref(SX.root, d)}">Open ${d[0] === "judgments" ? "the judgment summary" : "the instrument page"} →</a>${d[4] ? `<a class="lnk" href="${esc(d[4])}" target="_blank" rel="noopener">Official source ↗</a>` : ""}</div>`;
      rb.closest(".sxa").after(div); rb.textContent = "Close passage";
    } else if (mb) {
      e.preventDefault(); e.stopPropagation();
      const g = R.docs.find(x => x.d === +mb.dataset.more); if (!g) return;
      const extra = g.ps.slice(1, 13), ps = await Promise.all(extra.map(p => sxPassage(p.i)));
      const box = document.createElement("div"); box.className = "sxmore";
      box.innerHTML = ps.map((p, k) => p ? `<div class="sxm"><div class="m">${esc(sxWhere(g.doc, p[1], p[2]))}${extra[k].exact ? '<span class="sep"></span>Exact phrase' : ""}</div><div class="s">${sxHl(sxSnippet(p[3], Q, 240), Q)}</div><div class="sxa"><button class="lnk" type="button" data-read="${extra[k].i}">Read passage</button></div></div>` : "").join("") + (g.ps.length > 13 ? `<div class="m" style="padding:6px 0">and ${g.ps.length - 13} more</div>` : "");
      mb.closest(".sxa").after(box); mb.remove();
    }
  };
}

/* ---------- Counsel’s Clerk ---------- */
let FT = { state: "idle", p: null, chunks: [], idx: null, len: [], avg: 1 };
const FTS = {};
function loadFull(url) {
  url = url || "";
  FT = FTS[url] || (FTS[url] = { state: "idle", p: null, chunks: [], idx: null, len: [], avg: 1 });
  if (FT.p) return FT.p;
  if (!url) { FT.state = "none"; return (FT.p = Promise.resolve(false)); }
  const ft = FT;
  ft.state = "loading";
  ft.p = getJSON(url).then(j => {
    const FT = ft;
    FT.chunks = j.chunks || []; const idx = new Map(); let tot = 0;
    FT.chunks.forEach((c, i) => {
      const toks = tok(c[3]); FT.len[i] = toks.length; tot += toks.length;
      const tf = new Map(); toks.forEach(w => tf.set(w, (tf.get(w) || 0) + 1));
      tf.forEach((n, w) => { let a = idx.get(w); if (!a) idx.set(w, a = []); a.push(i, n); });
    });
    FT.idx = idx; FT.vocab = [...idx.keys()]; FT.avg = tot / Math.max(1, FT.chunks.length); FT.state = "ready"; return true;
  }).catch(() => { ft.state = "failed"; return false; });
  return ft.p;
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
const Judge = { M: null, endpoint: "", fulltext: "", link: id => "#d/" + id, scope: "", section: "rbi", docs: "the Directions", judUrl: "", judLink: null, pick: null,
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
  return esc(t).split(/\n{2,}/).map(par => `<p>${par.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>").replace(/\n/g, "<br>").replace(/\[([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)\]/g, (m, id) => M && M.byId.has(id) ? `<a class="lnk" href="${Judge.link(id)}" title="${id}">${esc(trunc(M.byId.get(id).label, 48))}</a>` : /^JUD-/.test(id) && Judge.judLink && JUD.byId && JUD.byId.has(id.slice(4)) ? `<a class="lnk" href="${Judge.judLink(id.slice(4))}">${esc(JUD.byId.get(id.slice(4)).short)}</a>` : m)}</p>`).join("");
}
/* key judgments: the rulings that best match a question go to the assistant with any regulator's texts */
const JUD = { p: null, list: [], byId: null, df: new Map() };
const COURT_Q = /\b(judg[e]?ments?|court|courts|ruling|rulings|held|holds|case law|precedent|tribunal|nclat|sat)\b/i;
const jstem = w => w.length > 4 ? w.replace(/(ies|es|s)$/, "") : w;
function loadJud(url) {
  if (JUD.p || !url) return JUD.p || Promise.resolve(false);
  return (JUD.p = getJSON(url).then(d => {
    JUD.list = (d.judgments || []).map(j => {
      const txt = [j.title, j.topic, j.issue, ...(j.holding || []), ...(j.impact || []), ...(j.statutes || [])].join(" ");
      const set = new Set(tok(txt).map(jstem));
      return { j, set, title: new Set(tok(j.title + " " + j.topic).map(jstem)) };
    });
    JUD.list.forEach(x => x.set.forEach(w => JUD.df.set(w, (JUD.df.get(w) || 0) + 1)));
    JUD.byId = new Map(JUD.list.map(x => [x.j.id, Object.assign({ short: x.j.title.split(/ v\.? /)[0].slice(0, 40) }, x.j)]));
    return true;
  }).catch(() => false));
}
function judExtracts(raw, all) {
  if (!JUD.list.length) return [];
  const qs = [...new Set(tok(raw).filter(w => w.length > 2 && !STOP.has(w) && !/^(judg[e]?ments?|court|courts|ruling|rulings|held|case|law|supreme|high|india|indian)$/.test(w)).map(jstem))];
  if (!qs.length) return [];
  const N = JUD.list.length, asked = all || COURT_Q.test(raw);
  const out = [];
  JUD.list.forEach(x => {
    let sc = 0, cov = 0;
    qs.forEach(w => { if (x.set.has(w)) { cov++; sc += Math.log(1 + N / (JUD.df.get(w) || 1)) * (x.title.has(w) ? 1.6 : 1); } });
    const need = asked ? 0.5 : 0.75;
    if (cov >= Math.min(2, qs.length) && cov / qs.length >= need) out.push([sc * cov / qs.length, x.j]);
  });
  out.sort((a, b) => b[0] - a[0]);
  return out.slice(0, asked ? 4 : 2).map(([, j]) => `[JUD-${j.id}] JUDGMENT of the ${j.court}, ${j.title}, ${j.date}${j.neutral_citation ? `, ${j.neutral_citation}` : ""}${j.report_citation ? `, ${j.report_citation}` : ""}${j.status_note ? ` (status: ${j.status_note})` : ""}
Question: ${j.issue}
Held: ${(j.holding || []).join(" ")}
What it means: ${(j.impact || []).join(" ")}`.slice(0, 3200));
}
async function askJudge() {
  const t = $("#jq"), raw = t.value.trim(), btn = $("#jsend");
  if (raw.length < 3 || btn.disabled) return;
  if (Judge.pick) Object.assign(Judge, Judge.pick(raw));
  const M = Judge.M;
  t.value = ""; const asked = judgeMsg("me", esc(raw));
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
    if (Judge.judUrl) { await loadJud(Judge.judUrl); const js = judExtracts(raw, Judge.section === "jud"); if (js.length) ext = Judge.section === "jud" ? [...js, ...ext] : [...ext.slice(0, 12), ...js, ...ext.slice(12, 40)]; }
    const post = x => fetch(Judge.endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ question: raw.slice(0, 500), extracts: x, section: Judge.section }) });
    let r = await post(ext);
    if (r.status === 413) { const small = []; let room = 14000; for (const x of ext) { const y = x.slice(0, 1800); if (y.length > room) break; small.push(y); room -= y.length; } r = await post(small.slice(0, 8)); }
    const j = await r.json().catch(() => ({}));
    wait.classList.remove("thinking");
    const more = docs.slice(0, 3).map(d => `<a class="lnk" href="${Judge.link(d.it.id)}">${esc(trunc(d.it.label, 40))}</a>`).join(" · ");
    wait.innerHTML = j.answer ? aiFormat(j.answer) + (more ? `<p class="jsrc">Read further: ${more}</p>` : "") : `<p>${esc(j.error || "Counsel’s Clerk is not available right now. Please try again later, or use the search box.")}</p>`;
  } catch (e) {
    wait.classList.remove("thinking");
    wait.innerHTML = `<p>Counsel’s Clerk could not be reached. Please check your connection, or use the search box.</p>`;
  }
  btn.disabled = false; judgeShowStart(asked);
}
/* bring the question to the top of the panel so a long answer is read from its start */
function judgeShowStart(el) { const log = $("#jlog"); if (!log || !el) return; log.scrollTop += el.getBoundingClientRect().top - log.getBoundingClientRect().top - 8; }
function initJudge(opts) {
  Object.assign(Judge, opts);
  if (!Judge.endpoint || $("#jfab")) return;
  const fab = document.createElement("button");
  fab.id = "jfab"; fab.type = "button"; fab.setAttribute("aria-controls", "judge"); fab.setAttribute("aria-expanded", "false");
  fab.setAttribute("aria-label", "Ask Counsel’s Clerk, the AI assistant"); fab.title = "Ask Counsel’s Clerk";
  fab.innerHTML = `${JUDGE_SVG}<span class="jtag">Ask Counsel’s Clerk</span>`;
  if (opts.wide) { fab.classList.add("wide"); const narrow = () => { if (scrollY > 120) { fab.classList.remove("wide"); removeEventListener("scroll", narrow); } }; addEventListener("scroll", narrow, { passive: true }); }
  const w = document.createElement("section");
  w.id = "judge"; w.hidden = true; w.setAttribute("role", "dialog"); w.setAttribute("aria-label", "Counsel’s Clerk");
  w.innerHTML = `<header>${JUDGE_SVG}<div><b>Counsel’s Clerk</b><span id="jscope">${esc(Judge.scope || "Answers from the RBI texts on this site")}</span></div><button class="iconbtn" id="jmax" type="button" aria-label="Enlarge chat window" title="Enlarge">${I.grow}</button><button class="iconbtn" id="jclose" type="button" aria-label="Close">✕</button></header>
  <div id="jlog" aria-live="polite"><div class="jmsg bot"><p><b>Order, order!</b> I am Counsel’s Clerk. ${esc(Judge.intro)}</p><p class="jtry">Try: ${Judge.tries.map(([q, t]) => `<button class="lnk" data-try="${esc(q)}">${esc(t)}</button>`).join(" · ")}</p></div></div>
  <form id="jform"><label class="sr" for="jq">Your question</label><textarea id="jq" rows="2" maxlength="500" placeholder="${esc(Judge.placeholder)}"></textarea><button id="jsend" type="submit" aria-label="Ask">${I.gavel}</button></form>
  <p class="jdisc">AI-generated answers can be wrong. Not legal advice: read the official text. Each question is answered on its own.</p>`;
  document.body.appendChild(w); document.body.appendChild(fab);
  fab.addEventListener("click", () => w.hidden ? openJudge() : closeJudge());
  $("#jclose").addEventListener("click", closeJudge);
  const setMax = on => { w.classList.toggle("max", on); const b = $("#jmax"); b.innerHTML = on ? I.shrink : I.grow; b.title = on ? "Shrink" : "Enlarge"; b.setAttribute("aria-label", on ? "Shrink chat window" : "Enlarge chat window"); try { localStorage.setItem("hub.jmax", on ? "1" : ""); } catch (e) {} };
  try { if (localStorage.getItem("hub.jmax")) setMax(true); } catch (e) {}
  $("#jmax").addEventListener("click", () => setMax(!w.classList.contains("max")));
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

/* section pages: compact header on inner tabs; fade + scroll for tab strips that do not fit */
function hubTabState() {
  const seg = decodeURIComponent((location.hash || "").replace(/^#/, "").split("/")[0]);
  document.body.classList.toggle("inner", !!seg);
  /* instrument pages: name the browser tab after the instrument */
  if (!hubTabState.base) hubTabState.base = document.title;
  if (seg === "d" && document.querySelector(".tabs")) { const h = document.querySelector("#view h1"); document.title = h ? h.textContent.trim() + " · " + hubTabState.base : hubTabState.base; }
  else if (document.querySelector(".tabs") && !/^#j\//.test(location.hash)) document.title = hubTabState.base;
  document.querySelectorAll(".tabs").forEach(t => {
    const on = t.querySelector("a.on"); if (on) { const l = on.offsetLeft - t.offsetLeft, r = l + on.offsetWidth; if (l < t.scrollLeft || r > t.scrollLeft + t.clientWidth) t.scrollLeft = Math.max(0, l - 24); }
    const fit = () => { t.classList.toggle("fl", t.scrollLeft > 4); t.classList.toggle("fr", t.scrollLeft + t.clientWidth < t.scrollWidth - 4); };
    if (!t.dataset.fade) { t.dataset.fade = 1; t.addEventListener("scroll", fit, { passive: true }); }
    fit();
  });
}
addEventListener("hashchange", () => setTimeout(hubTabState, 60));
addEventListener("resize", () => hubTabState());
addEventListener("load", () => setTimeout(hubTabState, 300));
new MutationObserver((m, o) => { if (document.querySelector(".tabs")) { o.disconnect(); setTimeout(hubTabState, 60); } }).observe(document.documentElement, { childList: true, subtree: true });
