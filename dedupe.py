"""Remove templated text from preset pages (thin/near-duplicate content audit, 29 Oct 2026).

A site audit measured the share of each page's three-word phrases that appear on no other page.
Preset pages scored 9-35% because each family (compress-pdf-to-*, *-passport-photo, ...) shared
sections and FAQs that were the same sentence with only the number or country swapped.

For every live preset page this drops each body section (split at <h2>) and each FAQ whose text,
with numbers and the page's own label normalised, is mostly the same as a section/FAQ on a sibling
page. What remains is the content written for that page; unique_presets.py then adds more.
The main tool pages keep the full how-to, so nothing useful disappears from the site.
"""
import re

KEEP_SHARE = 0.45   # drop a block when more than this share of its 3-word phrases also occur in one sibling block


def _norm(text, labels):
    t = re.sub(r"<[^>]+>", " ", text).lower()
    for lab in labels:
        if lab:
            t = t.replace(lab.lower(), " LBL ")
    t = re.sub(r"\d+(?:[.,]\d+)?", "#", t)
    t = re.sub(r"\b(kb|mb|px|pixels?|mm|cm|inch(?:es)?)\b", "U", t)
    return re.findall(r"[a-zа-я#ULB×'’-]+", t)


def _grams(words):
    return {tuple(words[i:i + 3]) for i in range(len(words) - 2)}


def _sections(body):
    return [s for s in re.split(r"(?=<h2>)", body) if s.strip()]


def _labels(t):
    """Words that differ between siblings for the same template: the number, country or language."""
    out = set()
    p = t.get("preset") or {}
    out.update(str(v) for v in p.values() if isinstance(v, (str, int)) and not isinstance(v, bool))
    n = t["name"]
    for w in re.findall(r"[A-Za-z]{3,}", n):
        out.add(w)
    return {x for x in out if len(x) >= 2}


def _templated(block_grams, others):
    if len(block_grams) < 4:
        return False
    return any(len(block_grams & o) / len(block_grams) > KEEP_SHARE for o in others)


def apply(T):
    fams = {}
    for t in T:
        if t.get("parent"):
            fams.setdefault(t["parent"], []).append(t)
    # Labels shared by the whole family (e.g. "Compress", "Image") must not be normalised away.
    plan = {}
    for par, kids in fams.items():
        if len(kids) < 2:
            continue
        common = set.intersection(*[_labels(k) for k in kids])
        info = {}
        for k in kids:
            labs = sorted(_labels(k) - common, key=len, reverse=True)
            secs = [(s, _grams(_norm(s, labs))) for s in _sections(k["body"])]
            faqs = [((q, a), _grams(_norm(q + " " + a, labs))) for q, a in k.get("faq", [])]
            info[k["slug"]] = (secs, faqs)
        for k in kids:
            secs, faqs = info[k["slug"]]
            o_secs = [g for s2 in kids if s2 is not k for _, g in info[s2["slug"]][0]]
            o_faqs = [g for s2 in kids if s2 is not k for _, g in info[s2["slug"]][1]]
            body = "".join(s for s, g in secs if not _templated(g, o_secs))
            faq = [qa for qa, g in faqs if not _templated(g, o_faqs)]
            plan[k["slug"]] = (body, faq)
    for t in T:
        if t["slug"] in plan:
            t["body"], t["faq"] = plan[t["slug"]]
            t["deduped"] = True
