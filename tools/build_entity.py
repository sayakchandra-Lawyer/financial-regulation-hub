#!/usr/bin/env python3
"""Build entity/data/entity.json for the 'What applies to my entity' page.

Reads hub.json, each section's register and graph, the RBI full text (to check paragraph references),
the judgments list and tools/entity_rules.py. Stops with an error if a rule names an instrument, lens or
paragraph that does not exist, so a broken rule never reaches the site.

Run from the repo root:  python3 -I tools/build_entity.py
"""
import json, os, re, sys
sys.dont_write_bytecode = True

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import entity_rules as R  # noqa: E402

OLD = re.compile(r"supersed|repeal|withdrawn|pending", re.I)  # pending = Bills not yet law
errors = []


def load(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return json.load(f)


def para_numbers(rbi_full):
    out = {}
    for c in rbi_full["chunks"]:
        for n in re.findall(r"\d+", c[2] or ""):
            out.setdefault(c[0], set()).add(int(n))
    return out


def main():
    hub = load("hub.json")
    secs, inst, lenses, as_of = [], {}, {}, []
    for s in hub["sections"]:
        d = s.get("data") or {}
        if s.get("status") != "live" or "register" not in d:
            continue
        reg, g = load(d["register"]), load(d["graph"])
        as_of.append(str(reg.get("meta", {}).get("as_of", "")))
        tags = {}
        for e in g["edges"]:
            if e.get("relation") == "applies_to":
                tags.setdefault(e["source"], []).append(e["target"])
        lenses[s["id"]] = {n["id"] for n in g["nodes"] if n["id"].startswith(("ENT-", "CAT-"))}
        rows = {}
        for it in reg["instruments"]:
            if OLD.search(str(it.get("status", ""))) or str(it.get("type", "")).lower().startswith("superseded"):
                continue
            tl = [t for t in (it.get("timelines") or []) if isinstance(t, str)][:12]
            rows[it["id"]] = [it.get("short_name") or it["id"], it.get("type", ""), it.get("theme", ""),
                              sorted(set(tags.get(it["id"], []))), tl]
        inst[s["id"]] = rows
        secs.append({"id": s["id"], "short": s["short"], "full": s.get("full", s["short"]), "href": s["href"]})

    paras = para_numbers(load("rbi/data/fulltext.json"))

    def check_add(a, where):
        sec, iid = a["sec"], a["id"]
        if sec not in inst or iid not in inst[sec]:
            errors.append(f"{where}: no in-force instrument {sec}/{iid}")
            return
        if "paras" in a:
            if sec != "rbi":
                errors.append(f"{where}: paragraph checks only run on RBI texts ({sec}/{iid})")
            have = paras.get(iid, set())
            for p in a["paras"]:
                if p not in have:
                    errors.append(f"{where}: {iid} has no paragraph {p} in the full text")

    def check_feed(f, where):
        if f["lens"] not in lenses.get(f["sec"], set()):
            errors.append(f"{where}: no lens {f['sec']}/{f['lens']}")

    for a in R.ATTRS:
        w = f"attr {a['id']}"
        for f in a.get("feeds", []) + a.get("feeds_rbi", []) + a.get("feeds_other", []):
            check_feed(f, w)
        for x in a.get("adds", []) + a.get("via", []):
            check_add(x, w)
        for k in ("rbi_cat", "rbi_cat_add"):
            if a.get(k) and a[k] not in lenses["rbi"]:
                errors.append(f"{w}: no RBI category {a[k]}")
    ids = {a["id"] for a in R.ATTRS}
    for c in R.COMBOS:
        for k in ("all", "any", "any2", "none"):
            for x in c.get(k, []):
                if x not in ids:
                    errors.append(f"combo {c['id']}: unknown choice {x}")
        for x in c["adds"]:
            check_add(x, f"combo {c['id']}")
    for a, b in R.SAME_AS:
        for sec, iid in (a, b):
            if iid not in inst.get(sec, {}):
                errors.append(f"same-as: no in-force instrument {sec}/{iid}")
    for p in R.PRESETS:
        for x in p["sel"]:
            if x not in ids:
                errors.append(f"preset {p['label']}: unknown choice {x}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)

    jud = load("judgments/data/judgments.json")["judgments"]
    rulings = [{"id": j["id"], "title": j["title"], "court": j["court"], "date": j["date"], "topic": j["topic"],
                "sectors": j.get("sectors", [])} for j in jud]
    out = {"meta": {"as_of": max(a for a in as_of if a) if any(as_of) else ""},
           "sections": secs, "layers": [{"id": i, "label": l, "cat": c} for i, l, c in R.LAYERS],
           "groups": R.GROUPS, "attrs": R.ATTRS, "combos": R.COMBOS,
           "same_as": [[list(a), list(b)] for a, b in R.SAME_AS], "presets": R.PRESETS,
           "inst": inst, "rulings": rulings}
    os.makedirs(os.path.join(ROOT, "entity", "data"), exist_ok=True)
    with open(os.path.join(ROOT, "entity", "data", "entity.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    n = sum(len(v) for v in inst.values())
    print(f"entity.json: {len(secs)} sections, {n} instruments, {len(R.ATTRS)} choices, {len(R.COMBOS)} combinations")


if __name__ == "__main__":
    main()
