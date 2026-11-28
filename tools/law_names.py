"""Full law names for short forms ("RBI Act 1934", "Act ss. 11 to 15", "LODR").

Reads assets/laws.json, the same table assets/hub.js uses on the live pages, so the
static pages and the interactive pages show the same full titles and links.
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_T = json.load(open(os.path.join(ROOT, "assets", "laws.json"), encoding="utf-8"))
LAWS, RULES = _T["laws"], _T["rules"]
UNIT = re.compile(r"^\s+(?=(?:ss?\.|rr?\.|rules?\b|regs?\b|regulations?\b|chapters?\b|paras?\b|sections?\b|part\b|schedule\b))", re.I)
_RX = {}


def _rx(sec, ref):
    key = (sec if ref else "", bool(ref))
    if key not in _RX:
        rs = [r for r in RULES if not r.get("sec") or (ref and r["sec"] == sec)]
        _RX[key] = (rs, re.compile("|".join("(" + r["re"] + ")" for r in rs)))
    return _RX[key]


def segs(text, sec, ref=False):
    text = str(text or "")
    rs, rx = _rx(sec, ref)
    out, last = [], 0
    for m in rx.finditer(text):
        if not m.group(0):
            continue
        r = rs[next(i for i, g in enumerate(m.groups()) if g is not None)]
        if m.start() > last:
            out.append(text[last:m.start()])
        out.append({"ids": [i for i in r["laws"] if i in LAWS], "src": m.group(0), "tail": r.get("tail", "")})
        last = m.end()
    if last < len(text):
        out.append(text[last:])
    return out


def render(text, sec, ref=False, as_html=False, first=False, seen=None):
    seen = set() if seen is None else seen
    E = (lambda s: html.escape(s, quote=True)) if as_html else (lambda s: s)
    out, prev = [], False
    for s in segs(text, sec, ref):
        if isinstance(s, str):
            t = UNIT.sub(", ", s) if prev else s
            if ref:
                t = re.sub(r"\b(ss?|rr?)\.(?=\d)", r"\1. ", t)
            out.append(E(t)); prev = False
            continue
        if not s["ids"] or (first and all(i in seen for i in s["ids"])):
            out.append(E(s["src"])); prev = False
            continue
        names = []
        for i in s["ids"]:
            seen.add(i)
            L = LAWS[i]
            names.append(f'<a href="{E(L["url"])}" target="_blank" rel="noopener">{E(L["name"])}</a>' if as_html and L.get("url") else E(L["name"]))
        out.append(" and ".join(names) + (", " + s["tail"] if s["tail"] else ""))
        prev = not s["tail"]
    return "".join(out)


def clean_powers(arr):
    return [x for x in (arr or []) if not re.match(r"\s*UNVERIFIED\b", x, re.I)]


def cited(it, sec):
    """Laws an instrument (a register row) cites, in order, leaving out the instrument's own Act."""
    ids = []

    def add(t, ref=False):
        for s in segs(t, sec, ref):
            if not isinstance(s, str):
                ids.extend(i for i in s["ids"] if i not in ids)
    add(it.get("reference_no"), True)
    for x in clean_powers(it.get("statutory_powers")) + list(it.get("cross_references") or []):
        add(x)
    add(it.get("consequences_general"))
    add(it.get("title"))
    for k in ("core_obligations", "timelines", "consequences_stated", "applies_to", "excluded", "key_concepts"):
        for x in it.get(k) or []:
            add(x)
    own = re.sub(r"^The ", "", str(it.get("title") or ""))
    keep = []
    for i in ids:
        n = LAWS[i]["name"]
        if own.startswith(n) and not own[len(n):].startswith(","):
            continue
        keep.append(LAWS[i])
    return keep
