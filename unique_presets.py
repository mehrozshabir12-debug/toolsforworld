"""Hand-written content for each live preset page (thin/near-duplicate content audit, 29 Oct 2026).

dedupe.py first removes the sections and FAQs that were the same template on every sibling page.
This module adds text written for one page only: what that size, country or language is actually
used for, practical problems people hit, and answers to the questions they ask. No sentence here
is reused on a sibling page. Official rules were checked on the government pages linked from each
passport page (29 Oct 2026); where a rule is not certain, the text points to the official page instead.
"""
from unique_presets_data import PAGES
from up_more import MORE
from up_more2 import M as MORE2
from up_leads import LEAD
from up_more3 import M as MORE3


def enrich(T):
    for t in T:
        extra = PAGES.get(t["slug"])
        if not extra:
            continue
        body, faq = extra
        t["body"] = body + t["body"]
        t["faq"] = list(faq) + list(t.get("faq", []))
    for t in T:
        extra = MORE.get(t["slug"])
        for src in (MORE2, MORE3):
            if t["slug"] not in src:
                continue
            b2, f2 = src[t["slug"]]
            extra = ((extra[0] if extra else "") + b2, list(extra[1] if extra else []) + list(f2))
        if extra:
            t["body"] = t["body"] + extra[0]
            t["faq"] = list(t.get("faq", [])) + list(extra[1])
    for t in T:
        if t["slug"] in LEAD:
            t["lead"] = LEAD[t["slug"]]
