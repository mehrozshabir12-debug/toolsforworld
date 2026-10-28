"""Pages folded into their main tool (owner approved, 28 Oct 2026).

Why: AdSense rejected the site twice (18 and 26 Oct) for content quality, and Google sees many
near-identical preset pages. A page is retired only when BOTH are true (data pulled 28 Oct 2026):
  - search demand is tiny (about 10-20 searches a month in the US, India and Pakistan), and
  - Search Console shows it is not close to page one (average position worse than ~25).
Pages with real demand or a top-20 position stay (Urdu OCR: ~540/month in Pakistan; Wi-Fi QR:
2,900/month; 1080x1920 and 1500x500 rank 6-22 for their queries).

What happens to a retired page:
  - it leaves the sitemap and the tool lists;
  - its folder becomes a small redirect page (instant meta refresh + canonical to the main tool),
    so old links and bookmarks still work and Google moves its signals to the main tool;
  - the main tool shows it as a one-click preset button, opened with #p=<old slug>;
  - every internal link to it is rewritten to the main tool with that preset.
"""
import html
import json
import re

RETIRED = [
    # OCR languages: ~10 searches/month, average position 22-44
    "image-to-text-spanish", "image-to-text-turkish", "image-to-text-portuguese",
    "image-to-text-italian", "image-to-text-bengali",
    # Resize sizes: 10-20 searches/month, average position 30-55
    "resize-image-to-400x400", "resize-image-to-1080x1080", "resize-image-to-1280x720",
    "resize-image-to-1000x1500", "resize-image-to-2560x1440", "resize-image-to-1080x1350",
    "resize-image-to-1200x630", "resize-image-to-851x315", "resize-image-to-1584x396",
    # WhatsApp QR: 210/month US, 1,300 India; the plain QR generator does the same job
    "whatsapp-qr-code-generator",
]

GONE = {}   # slug -> retired tool dict (with "parent")


def apply(T):
    """Remove retired pages from T (in place) and remember them."""
    keep = []
    for t in T:
        if t["slug"] in RETIRED:
            if not t.get("parent"):
                raise SystemExit(f"retire.py: {t['slug']} has no parent tool to fold into")
            GONE[t["slug"]] = t
        else:
            keep.append(t)
    missing = set(RETIRED) - set(GONE)
    if missing:
        raise SystemExit(f"retire.py: unknown slugs {sorted(missing)}")
    T[:] = keep
    return GONE


def preset_buttons(parent_slug, label):
    """One-click preset buttons on the main tool for the pages folded into it."""
    items = [t for t in GONE.values() if t["parent"] == parent_slug]
    if not items:
        return ""
    btns = "".join(
        f'<button type="button" class="chipbtn" data-p="{html.escape(t["slug"])}" '
        f'data-preset="{html.escape(json.dumps(t["preset"]))}">{html.escape(t["name"])}</button>' for t in items)
    # Same logic as the preset loader in files.js/calc.js: set each field, then fire input/change.
    js = ('<script>(function(){var B=[].slice.call(document.querySelectorAll(".chipbtn"));'
          'function go(b,scroll){var P=JSON.parse(b.dataset.preset);Object.keys(P).forEach(function(s){var e=document.querySelector(s);'
          'if(!e)return;if(e.type==="checkbox")e.checked=!!P[s];else e.value=P[s];'
          'e.dispatchEvent(new Event("input"));e.dispatchEvent(new Event("change"))});'
          'B.forEach(function(x){x.setAttribute("aria-pressed",x===b)});'
          'if(scroll){var d=document.getElementById("drop")||document.querySelector(".bench");if(d)d.scrollIntoView({block:"center"})}}'
          'B.forEach(function(b){b.addEventListener("click",function(){go(b,false)})});'
          'function fromHash(){var m=/^#p=([a-z0-9-]+)$/.exec(location.hash);if(!m)return;'
          'var b=B.filter(function(x){return x.dataset.p===m[1]})[0];if(b)setTimeout(function(){go(b,true)},0)}'
          'if(document.readyState==="complete")fromHash();else window.addEventListener("load",fromHash);'
          'window.addEventListener("hashchange",fromHash)})();</script>')
    return f'<div class="chips presetbtns"><span class="sect">{label}</span>{btns}</div>{js}'


def rewrite_links(content):
    """Point internal links at retired pages to their main tool with the preset."""
    if not GONE:
        return content
    pat = re.compile(r'href="((?:\.\./)*|/|https://toolsforworld\.com/)(' + "|".join(map(re.escape, GONE)) + r')/(?:index\.html)?"')
    return pat.sub(lambda m: f'href="{m.group(1)}{GONE[m.group(2)]["parent"]}/#p={m.group(2)}"', content)


def stub(base, slug):
    """Redirect page left in the old folder."""
    t = GONE[slug]
    to = base + t["parent"] + "/"
    name = html.escape(t["name"])
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{name} – moved</title>'
            f'<link rel="canonical" href="{to}"><meta name="robots" content="noindex,follow">'
            f'<meta http-equiv="refresh" content="0; url={to}#p={slug}">'
            f'<script>location.replace("{to}#p={slug}")</script></head>'
            f'<body><p>{name} is now part of <a href="{to}#p={slug}">this tool</a>.</p></body></html>\n')
