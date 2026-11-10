"""Focus the site on 15 main tools (owner's decision, 10 Nov 2026).

Why: between 6 and 10 Nov Google dropped most of the site from its index ("Crawled - currently not
indexed"; no manual action, no technical fault). The site had grown to ~90 pages in four weeks, many of
them size/country/language variants of the same tool. For a new site with almost no backlinks that
looked thin to Google. The owner's plan: get 10-15 strong tools indexed and AdSense-approved first,
then launch one more tool every week or month.

What this does:
  - KEEP: the only tools Google sees (in the sitemap, on the home page, indexable, with ad code).
  - Every variant page of a kept tool (compress-image-to-50kb, resize-image-to-500x500, image-to-text-urdu,
    us-passport-photo, compress-pdf-to-200kb, jpg-to-pdf-under-100kb, wifi-qr-code-generator,
    discount-calculator ...) is folded into its main tool through retire.py: the old URL becomes a redirect
    page to the main tool, and the variant stays available there as a one-click preset button.
  - Every other tool stays online for anyone with the link, but is hidden: noindex, out of the sitemap,
    the home page, menus and "related tools", and carries no ad code. To relaunch one, add it to KEEP.
"""
import retire

KEEP = [
    "compress-image", "resize-image", "compress-pdf", "merge-pdf", "jpg-to-pdf", "pdf-to-jpg",
    "pdf-to-word", "word-to-pdf", "image-to-text", "passport-photo-maker", "heic-to-jpg", "png-to-jpg",
    "qr-code-generator", "age-calculator", "percentage-calculator",
]

PRESET_LABEL = {
    "compress-image": "Exact sizes (one click)", "compress-pdf": "Exact sizes (one click)",
    "passport-photo-maker": "Countries (one click)", "jpg-to-pdf": "PDF size limits (one click)",
    "percentage-calculator": "More (one click)",
}


def prepare(T):
    """Before retire.apply: fold every variant of a kept tool into it."""
    for t in T:
        if t.get("parent") in KEEP and t["slug"] not in retire.RETIRED:
            retire.RETIRED.append(t["slug"])


def apply(T):
    """After all content modules: mark everything outside KEEP as hidden."""
    have = {t["slug"] for t in T}
    missing = set(KEEP) - have
    if missing:
        raise SystemExit(f"focus.py: unknown tools {sorted(missing)}")
    for t in T:
        t["hidden"] = t["slug"] not in KEEP
