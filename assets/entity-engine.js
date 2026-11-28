/* Entity applicability engine, shared by the entity builder (entity/) and the dashboard (dashboard/).
   entityEngine(D) with D = entity/data/entity.json returns compute(sel): sel = Set of attribute ids
   -> { items, combos, rulings, rbiReg, t, L }. Each item carries why, scope, cond and tier. */
function entityEngine(D) {
  const A = new Map(D.attrs.map(a => [a.id, a]));
  const SEC = new Map(D.sections.map(s => [s.id, s]));
  const LIDX = Object.fromEntries(D.layers.map((l, i) => [l.cat, i]));
  const LBYID = Object.fromEntries(D.layers.map((l, i) => [l.id, i]));
  /* laws that bite on a transaction or an event (security, enforcement, insolvency), not on the licence itself */
  const TIER_EVENT = new Set(["ibc", ...["Enforcement and recovery", "Mortgages, property and goods as security", "Cheques and negotiable instruments", "Contracts, guarantees and pledges", "Electronic contracts and evidence", "Stamp duty and registration"].map(t => "laws:" + t)]);
  return function compute(sel){
    const typeOf = () => [...sel].map(x => A.get(x)).find(a => a.group === "type");
    const t = typeOf(), rbiReg = !!(t && t.rbi), items = new Map(), lab = a => a.short || a.label;
    const layerId = [...sel].find(x => A.get(x).group === "layer"), L = layerId != null ? LBYID[layerId] : -1;
    const add = (sec, id, why, o = {}) => {
      const k = (o.via ? "via:" + o.via + ":" : "") + sec + "/" + id;
      let it = items.get(k);
      if (!it) { const r = D.inst[sec] && D.inst[sec][id]; if (!r) return null; it = { k, sec: o.via ? "lender" : sec, home: sec, id, name: r[0], type: r[1], theme: r[2], tl: r[4], why: new Set(), scope: [], focus: [], notes: [], via: o.via || "", combos: [], also: [] }; items.set(k, it); }
      if (why) it.why.add(why);
      if (o.scope && !it.scope.includes(o.scope)) it.scope.push(o.scope);
      if (o.focus && !it.focus.includes(o.focus)) it.focus.push(o.focus);
      if (o.note) it.notes.push(o.note);
      if (o.combo) it.combos.push(o.combo);
      return it;
    };
    if (rbiReg) {
      const cats = [t.rbi_cat].concat(sel.has("dep") ? ["CAT-D"] : []);
      const why = `${t.label}${L >= 0 ? " · " + D.layers[L].label + " Layer" : ""}`;
      for (const [id, r] of Object.entries(D.inst.rbi)) {
        const tags = r[3]; if (!tags.length) continue;
        const c = tags.filter(x => !(x in LIDX)), ls = tags.filter(x => x in LIDX).map(x => LIDX[x]);
        if (c.length && !cats.some(x => c.includes(x))) continue;
        if (ls.length && Math.min(...ls) > Math.max(L, 0)) continue;
        add("rbi", id, c.includes(t.rbi_cat) || !c.length ? why : "Takes public deposits");
      }
    }
    const lens = {};
    const feed = (f, why) => { if (f.layers && !f.layers.includes(layerId)) return; (lens[f.sec] = lens[f.sec] || {})[f.lens] = (lens[f.sec][f.lens] || new Set()).add(why); };
    for (const x of sel) {
      const a = A.get(x), w = a.group === "type" ? a.label : lab(a);
      if (a.rbi_only && !rbiReg) continue;
      (a.feeds || []).forEach(f => feed(f, w));
      (rbiReg ? a.feeds_rbi || [] : a.feeds_other || []).forEach(f => feed(f, w));
      (a.adds || []).forEach(d => { if (d.rbi_only && !rbiReg) return; add(d.sec, d.id, w, a.group === "act" ? { focus: d.scope } : { scope: d.scope }); });
      (a.via || []).forEach(d => add(d.sec, d.id, w, { via: a.id, scope: d.scope, note: d.note }));
    }
    for (const [sec, m] of Object.entries(lens)) {
      for (const [id, r] of Object.entries(D.inst[sec] || {})) {
        const hit = r[3].filter(x => m[x]); if (!hit.length) continue;
        const it = add(sec, id); hit.forEach(h => m[h].forEach(w => it.why.add(w)));
      }
    }
    const combos = D.combos.filter(c => (c.all || []).every(x => sel.has(x)) && (!c.any || c.any.some(x => sel.has(x))) && (!c.any2 || c.any2.some(x => sel.has(x))) && !(c.none || []).some(x => sel.has(x)));
    for (const c of combos) {
      const w = [...(c.all || []), ...(c.any || []).filter(x => sel.has(x)), ...(c.any2 || []).filter(x => sel.has(x))].map(x => lab(A.get(x)));
      c._why = c.because ? [c.because] : [...new Set(w)];
      c.adds.forEach(d => add(d.sec, d.id, c._why.join(" + "), { scope: d.scope, combo: c.id }));
    }
    for (const [[ps, pi], [ss, si]] of D.same_as) {
      const p = items.get(ps + "/" + pi), s = items.get(ss + "/" + si);
      if (p && s) { s.why.forEach(w => p.why.add(w)); p.also.push(SEC.get(ss).short); items.delete(s.k); }
    }
    /* how each instrument reaches you: directly, only if you take up an activity or licence you have not picked,
       in part, or as a general / event-triggered law (insolvency, contract, enforcement). A guide to reading the list, not a legal conclusion. */
    const onAdds = new Set(), cond = new Map();
    for (const x of sel) (A.get(x).adds || []).forEach(d => { if (!d.scope) onAdds.add(d.sec + "/" + d.id); });
    D.attrs.filter(a => (a.group === "act" || a.group === "lic") && !sel.has(a.id)).forEach(a => (a.adds || []).forEach(d => {
      const k = d.sec + "/" + d.id; if (d.scope || onAdds.has(k)) return; if (!cond.has(k)) cond.set(k, []); cond.get(k).push(a.short || a.label); }));
    for (const it of items.values()) {
      it.cond = cond.get(it.home + "/" + it.id) || [];
      it.tier = it.via ? "via" : /^proposed/i.test(it.theme || "") ? "prop" : TIER_EVENT.has(it.home) || TIER_EVENT.has(it.home + ":" + it.theme) ? "event" : it.cond.length ? "cond" : it.scope.length ? "part" : "direct";
    }
    const sectors = new Set([...sel].flatMap(x => A.get(x).sectors || []));
    const rulings = D.rulings.filter(j => j.sectors.some(s => sectors.has(s)));
    return { items: [...items.values()], combos, rulings, rbiReg, t, L };
  };
}
