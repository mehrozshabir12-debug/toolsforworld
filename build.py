"""Builds the Tools for World static site: one folder per tool, plus home, about, privacy, terms, sitemap.
Run:  python3 build.py            (BASE = public URL used for canonical links and the sitemap)
"""
import json, os, html, datetime

ROOT = os.environ.get("TK_OUT") or os.path.dirname(os.path.abspath(__file__))
PREVIEW = bool(os.environ.get("TK_PREVIEW"))
import re
BASE = os.environ.get("TK_BASE", "https://toolsforworld.com/")
TODAY = datetime.date.today().isoformat()
PDFLIB = '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js" integrity="sha384-weMABwrltA6jWR8DDe9Jp5blk+tZQh7ugpCsF3JwSA53WZM9/14PjS5LAJNHNjAI" crossorigin="anonymous"></script>'
PDFJS = '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js" integrity="sha384-/1qUCSGwTur9vjf/z9lmu/eCUYbpOTgSjmpbMQZ1/CtX2v/WcAIKqRv+U1DUCG6e" crossorigin="anonymous"></script>'
MAMMOTH = '<script src="https://cdn.jsdelivr.net/npm/mammoth@1.8.0/mammoth.browser.min.js" integrity="sha384-/cXAMbzovUIKbBERjPmR3SnPTh8siWr5lsvFYj1Uq4XP0yaJUZJmsh0YXyGv5P0y" crossorigin="anonymous"></script>'
H2PDF = '<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js" integrity="sha384-Yv5O+t3uE3hunW8uyrbpPW3iw6/5/Y7HitWJBLgqfMoA36NogMmy+8wWZMpn3HWc" crossorigin="anonymous"></script>'

ICON = {
    "text": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h10"/></svg>',
    "qr": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><path d="M14 14h3v3h-3zM20 14v.01M14 20h.01M17 20h4v-3"/></svg>',
    "lock": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
    "music": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>',
    "calc": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 11h2M14 11h2M8 15h2M14 15h2M8 19h2M14 19h2"/></svg>',
    "bolt": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
    "sun": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    "map": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3z"/><path d="M9 3v15M15 6v15"/></svg>',
    "coin": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v6c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/></svg>',
    "grad": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/></svg>',
    "img": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="9" cy="9" r="2"/><path d="m21 15-5-5L5 21"/></svg>',
    "user": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M7 18c1-2.5 3-3.5 5-3.5s4 1 5 3.5"/></svg>',
    "pdf": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg>',
    "word": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13l1.5 5 2.5-4 2.5 4 1.5-5"/></svg>',
}

def F(label, inner, small=""):
    return f'<label class="f"><span>{label}</span>{inner}{f"<small>{small}</small>" if small else ""}</label>'

def N(id_, val="", step="any", minv="0", ph=""):
    return f'<input type="number" id="{id_}" value="{val}" step="{step}" min="{minv}" inputmode="decimal"{f" placeholder={chr(34)}{ph}{chr(34)}" if ph else ""}>'

def SEL(id_, opts, sel=None):
    return f'<select id="{id_}">' + "".join(f'<option value="{v}"{" selected" if v == sel else ""}>{t}</option>' for v, t in opts) + "</select>"

def RESULT(kv=False, table=None, note=True):
    h = '<div class="result" aria-live="polite"><div class="big" id="out-total"></div>'
    if kv: h += '<div class="kv" id="out-kv"></div>'
    if note: h += '<p class="note err" id="out-note" hidden></p>'
    if table: h += f'<div class="scroll"><table class="t"><thead><tr><th>{table[0]}</th><th class="n">{table[1]}</th></tr></thead><tbody id="out-rows"></tbody></table></div>'
    return h + "</div>"

FILE_UI = '''<label class="drop" id="drop" tabindex="0"><input type="file" id="fin"><strong id="d-main">Choose files</strong><span id="d-sub">or drag and drop them here</span><span class="fmt" id="d-fmt"></span><span class="priv">🔒 Processed on your device. Nothing is uploaded.</span></label>
<div class="panel" id="panel" hidden><div class="files" id="list"></div><div id="opts"></div>
<div class="row"><button class="btn" id="go">Start</button><button class="btn ghost" id="clear">Clear</button><span class="note" id="status" role="status" aria-live="polite"></span></div><progress id="prog" max="100" hidden aria-label="Progress"></progress>
<div class="out" id="out"></div>EXTRA</div>'''

# ------------------------------------------------------------------ tools
T = []
def tool(**k): T.append(k)
import tools_list
tools_list.define(tool, F, N, SEL, RESULT, PDFLIB, PDFJS, MAMMOTH, H2PDF)
tools_list.landing(tool)
tools_list.enrich(T)
BY = {t['slug']: t for t in T}

# Hand-picked "related tools" for each main tool (what people usually need next)
RELATED = {
    "pdf-to-word": ["word-to-pdf", "image-to-text", "compress-pdf", "pdf-to-jpg"],
    "word-to-pdf": ["pdf-to-word", "compress-pdf", "merge-pdf", "jpg-to-pdf"],
    "compress-pdf": ["compress-pdf-to-200kb", "split-pdf", "merge-pdf", "compress-image"],
    "merge-pdf": ["split-pdf", "compress-pdf", "jpg-to-pdf", "word-to-pdf"],
    "split-pdf": ["merge-pdf", "compress-pdf", "pdf-to-jpg", "pdf-to-word"],
    "jpg-to-pdf": ["compress-image", "merge-pdf", "compress-pdf", "heic-to-jpg"],
    "pdf-to-jpg": ["compress-image", "image-to-text", "split-pdf", "jpg-to-pdf"],
    "image-to-text": ["pdf-to-word", "pdf-to-jpg", "word-counter", "image-to-text-urdu"],
    "compress-image": ["resize-image", "compress-image-to-100kb", "jpg-to-pdf", "heic-to-jpg"],
    "resize-image": ["compress-image", "passport-photo-maker", "remove-background", "resize-image-to-1080x1080"],
    "remove-background": ["passport-photo-maker", "resize-image", "compress-image", "png-to-jpg"],
    "png-to-jpg": ["jpg-to-png", "webp-to-jpg", "compress-image", "heic-to-jpg"],
    "jpg-to-png": ["png-to-jpg", "remove-background", "compress-image", "webp-to-jpg"],
    "webp-to-jpg": ["png-to-jpg", "heic-to-jpg", "compress-image", "resize-image"],
    "heic-to-jpg": ["compress-image", "jpg-to-pdf", "webp-to-jpg", "resize-image"],
    "passport-photo-maker": ["remove-background", "compress-image-to-50kb", "resize-image", "us-passport-photo"],
    "qr-code-generator": ["wifi-qr-code-generator", "whatsapp-qr-code-generator", "password-generator", "word-counter"],
    "word-counter": ["character-counter", "image-to-text", "password-generator", "percentage-calculator"],
    "password-generator": ["qr-code-generator", "word-counter", "character-counter", "age-calculator"],
    "age-calculator": ["percentage-calculator", "discount-calculator", "word-counter", "password-generator"],
    "percentage-calculator": ["discount-calculator", "age-calculator", "word-counter", "character-counter"],
    "mp4-to-mp3": ["compress-image", "heic-to-jpg", "pdf-to-word", "image-to-text"],
}
FMT = {'compress': 'Supported: JPG, PNG, WebP, GIF, BMP · several files at once', 'resize': 'Supported: JPG, PNG, WebP, GIF, BMP · several files at once', 'convert': 'Supported: JPG, PNG, WebP · several files at once', 'passport': 'Supported: JPG, PNG, WebP', 'img2pdf': 'Supported: JPG, PNG, WebP · several files at once', 'merge': 'Supported: PDF · several files at once', 'split': 'Supported: PDF', 'pdf2jpg': 'Supported: PDF', 'word2pdf': 'Supported: Word .docx', 'png2jpg': 'Supported: PNG · several files at once', 'jpg2png': 'Supported: JPG / JPEG · several files at once', 'webp2jpg': 'Supported: WebP · several files at once', 'heic2jpg': 'Supported: HEIC / HEIF (iPhone photos) · several files at once', 'pdfcompress': 'Supported: PDF', 'ocr': 'Supported: JPG, PNG, WebP, BMP', 'bgremove': 'Supported: JPG, PNG, WebP', 'mp4mp3': 'Supported: MP4, MOV, WebM, M4A', 'pdf2word': 'Supported: PDF'}  # what each file tool accepts (shown under the drop zone; kept in sync with TOOLS in files.js)
POPULAR = ["pdf-to-word", "compress-image-to-100kb", "compress-pdf", "remove-background", "image-to-text", "passport-photo-maker", "jpg-to-pdf", "word-to-pdf"]

# Google AdSense publisher ID, e.g. "ca-pub-1234567890123456". Empty = no ad code on the site.
ADSENSE_CLIENT = "ca-pub-3864792630233896"

GROUPS = [("pdf", "PDF & document tools"), ("img", "Image tools"), ("util", "Text & everyday tools"), ("media", "Audio & video")]
NAV = {"pdf": "PDF", "img": "Image", "util": "Utilities", "media": "Audio"}

# ------------------------------------------------------------------ layout
BRAND_NAMES = ["ToolsForWorld", "Tools 4 World", "Tools4World", "Tool for World", "Tools for the World", "Tool4World", "toolsforworld.com"]
BRAND_KEYWORDS = "Tools for World, toolsforworld, tools for world, tools 4 world, tools4world, tool for world, tool 4 world, tools world, toolsforworld.com, free online tools, PDF tools, image tools"


FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Figtree:wght@400;500;600&family=JetBrains+Mono:wght@500&display=optional"


def fit_title(t):
    """Keep titles short enough for search results: drop the brand suffix when the title is long."""
    return t.replace(" | Tools for World", "") if len(t) > 62 and t.endswith(" | Tools for World") else t


def fit_desc(d):
    """Search results show about 155-160 characters: end at a full sentence before that."""
    if len(d) <= 160: return d
    cut = d[:160]; end = max(cut.rfind(". "), cut.rfind("! "))
    return cut[:end + 1] if end > 80 else cut[:cut.rfind(" ")].rstrip(",;:") + "…"


def page(rel_root, title, desc, canon, body, scripts="", body_attr="", jsonld=None, active="", keywords=""):
    title, desc = fit_title(title), fit_desc(desc)
    nav = "".join(f'<a href="{rel_root}#{g}"{" aria-current=true" if active == g else ""}>{NAV[g]}</a>' for g, l in GROUPS)
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta http-equiv="Content-Security-Policy" content="object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">{f'<meta name="keywords" content="{html.escape(keywords)}">' if keywords else ""}
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{canon}"><meta property="og:type" content="website"><meta property="og:site_name" content="Tools for World"><meta property="og:image" content="{BASE}og-image.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="https://toolsforworld.com/favicon.ico" sizes="48x48"><link rel="icon" href="https://toolsforworld.com/favicon-96.png" type="image/png" sizes="96x96"><link rel="icon" href="https://toolsforworld.com/favicon-192.png" type="image/png" sizes="192x192"><link rel="icon" href="https://toolsforworld.com/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="https://toolsforworld.com/apple-touch-icon.png"><link rel="manifest" href="https://toolsforworld.com/site.webmanifest"><meta name="theme-color" content="#0d7a55">
{(f'<meta name="google-adsense-account" content="{ADSENSE_CLIENT}"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>') if ADSENSE_CLIENT else ""}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{FONTS}"><link rel="stylesheet" href="{FONTS}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="{FONTS}"></noscript>
<link rel="stylesheet" href="{rel_root}assets/style.css">
{ld}
</head>
<body{body_attr}>
<header><div class="wrap"><a class="logo" href="{rel_root}" aria-label="Tools for World home"><svg viewBox="0 0 32 32" width="40" height="40" aria-hidden="true"><circle cx="16" cy="16" r="15" fill="var(--accent)"/><g fill="none" stroke="var(--accent-ink)" stroke-width="1.8"><circle cx="16" cy="16" r="9.5"/><ellipse cx="16" cy="16" rx="4.2" ry="9.5"/><path d="M6.8 13h18.4M6.8 19h18.4"/></g></svg><span>Tools <i>for</i> World</span></a><nav aria-label="Main">{nav}<a href="{rel_root}#all" class="navall">All tools</a></nav><form class="hsearch" role="search" action="{rel_root}" method="get"><input type="search" name="q" placeholder="Search tools…" aria-label="Search tools" autocomplete="off"></form></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap"><span>© <span id="yr">{datetime.date.today().year}</span> Tools for World · Free tools that run in your browser.</span>
<span><a href="{rel_root}about/">About</a> · <a href="{rel_root}privacy/">Privacy Policy</a> · <a href="{rel_root}terms/">Terms</a> · <a href="{rel_root}contact/">Contact</a> · <a href="{rel_root}credits/">Open-source credits</a></span></div></footer>
{scripts}
<script src="{rel_root}assets/site.js" defer></script>
<!-- Cloudflare Web Analytics --><script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "58c7e905638641ae816794606d09687a"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
'''

KW = {  # extra search words (synonyms people type)
    "pdf-to-word": "docx doc editable convert", "word-to-pdf": "docx doc cv resume", "compress-pdf": "reduce shrink size kb mb smaller",
    "merge-pdf": "combine join", "split-pdf": "extract pages separate cut", "jpg-to-pdf": "image photo png pictures scan",
    "pdf-to-jpg": "image png pictures pages", "image-to-text": "ocr scan read copy extract text photo screenshot",
    "compress-image": "reduce shrink kb size photo jpg png smaller", "resize-image": "dimensions pixels width height scale crop",
    "remove-background": "transparent cutout bg erase png", "heic-to-jpg": "iphone apple heif photo", "passport-photo-maker": "visa id photo 2x2 35x45",
    "qr-code-generator": "qrcode barcode link", "word-counter": "count words characters essay", "password-generator": "secure random strong",
    "age-calculator": "birthday date of birth years", "percentage-calculator": "percent discount increase decrease", "mp4-to-mp3": "audio video extract sound music",
    "png-to-jpg": "convert image", "jpg-to-png": "convert image transparent", "webp-to-jpg": "convert image",
}


def cards(rel_root, items):
    return '<div class="grid">' + "".join(
        f'<a class="tool" href="{rel_root}{t["slug"]}/" data-k="{KW.get(t["slug"], "")}"><span class="ic">{ICON[t["icon"]]}</span><span><h2>{t["name"]}</h2><p>{t["card"]}</p></span></a>' for t in items) + "</div>"

def chips(rel_root, items, label):
    """Preset links. The words every chip shares (e.g. "Compress Image to ") are hidden on small screens."""
    names = [t["name"] for t in items]
    pre = os.path.commonprefix(names) if len(names) > 1 else ""
    pre = pre[:pre.rfind(" ") + 1] if " " in pre else ""
    def lab(n):
        return f'<span class="pre">{n[:len(pre)]}</span>{n[len(pre):]}' if pre else n
    return f'<div class="chips"><span class="sect">{label}</span>' + "".join(
        f'<a href="{rel_root}{t["slug"]}/">{lab(t["name"])}</a>' for t in items) + "</div>"

def write(rel_path, content):
    if PREVIEW and rel_path.endswith(".html"):
        content = re.sub(r'href="((?:\.\./)*(?:[a-z0-9-]+/)?)(#[a-z]*)?"', lambda m: f'href="{m.group(1)}index.html{m.group(2) or ""}"', content)
    p = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

def build():
    urls = [BASE]
    for t in T:
        r = "../"
        faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t.get("faq", []))
        par = BY.get(t.get("parent"))
        kids = [x for x in T if x.get("parent") == t["slug"]]
        if par:
            sibs = [x for x in T if x.get("parent") == par["slug"] and x["slug"] != t["slug"]]
            start = next((i for i, x in enumerate(sibs) if x["slug"] > t["slug"]), 0)
            related = [par] + (sibs[start:] + sibs[:start])[:3] + [BY[x] for x in RELATED.get(par["slug"], [])[:2] if x in BY]
        else:
            related = [BY[x] for x in RELATED.get(t["slug"], []) if x in BY] or \
                      [x for x in T if x["group"] == t["group"] and x["slug"] != t["slug"] and not x.get("parent")][:4]
        preset = f'<script>window.PRESET={json.dumps(t["preset"])}</script>' if t.get("preset") else ""
        if "ftool" in t:
            ui = FILE_UI.replace("EXTRA", t.get("extra", "")).replace('<span class="fmt" id="d-fmt"></span>', f'<span class="fmt" id="d-fmt">{FMT.get(t["ftool"], "")}</span>')
            scripts = preset + f'<script src="{r}assets/files.js"></script>'
            attr = f' data-tool="{t["ftool"]}"'
        else:
            ui = t.get("ui") or par["ui"]; scripts = preset + t.get("libs", "") + f'<script src="{r}assets/calc.js"></script>'; attr = f' data-calc="{t["calc"]}"'
        group_name = dict(GROUPS)[t["group"]]
        body = f'''<p class="crumbs"><a href="{r}">Home</a> › <a href="{r}#{t["group"]}">{group_name}</a>{f' › <a href="{r}{par["slug"]}/">{par["name"]}</a>' if par else ""}</p>
<section class="bench"><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p>
{chips(r, kids, "Popular presets") if kids else ""}
{ui}
<div class="how">{t["body"]}{f'<h2>Questions</h2><div class="faq">{faq}</div>' if faq else ""}</div>
<div class="related"><div class="sect">{"Related tools" if par else "More " + group_name.lower()}</div>{cards(r, related)}</div></section>'''
        canon = BASE + t["slug"] + "/"
        ld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": t["name"], "url": canon, "applicationCategory": "UtilitiesApplication",
               "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": t["desc"]}]
        if t.get("faq"):
            ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]})
        write(f'{t["slug"]}/index.html', page(r, t["title"], t["desc"], canon, body, scripts, attr, ld, t["group"]))
        urls.append(canon)

    home = '''<div class="hero"><p class="brand-big" aria-hidden="true">Tools <i>for</i> World</p><h1>Free online tools that keep your files private</h1>
<p>Convert PDF and Word files, compress and edit images, remove backgrounds, make QR codes and more. No sign-up, no watermark, no limits. Every tool runs in your browser, so your files never leave your device.</p>
<div class="bigsearch" role="search"><input type="search" id="q" placeholder="Search tools: compress pdf, passport, heic…" aria-label="Search tools" autocomplete="off"></div>
<p class="aka">Tools for World (also written ToolsForWorld or Tools 4 World) is at toolsforworld.com.</p></div>
<div id="results" hidden><div class="sect">Search results</div><div class="grid" id="rgrid"></div><p class="note" id="rnone" hidden>No tool matches that yet. <a href="contact/">Ask us for it</a>.</p></div>
<div id="browse"><div id="recent" hidden><div class="sect">Recently used</div><div class="chips" id="rchips"></div></div>'''
    home += '<div class="sect">Popular tools</div>' + cards("", [BY[x] for x in POPULAR if x in BY])
    home += '<div id="all"></div>'
    for g, label in GROUPS:
        home += f'<div class="sect" id="{g}">{label}</div>' + cards("", [t for t in T if t["group"] == g and not t.get("parent")])
    home += '<div class="sect" id="presets">Popular sizes &amp; presets</div>'
    for par in [p for p in T if any(x.get("parent") == p["slug"] for x in T)]:
        home += chips("", [t for t in T if t.get("parent") == par["slug"]], par["name"])
    home += "</div>"
    write("index.html", page("", "Tools for World – Free PDF, Image & Everyday Tools Online",
                             "Free online tools: PDF to Word, Word to PDF, compress PDF and images, background remover, HEIC to JPG, OCR, QR code generator, MP4 to MP3 and more. Private: files never leave your device.",
                             BASE, home, f'<script src="assets/calc.js"></script>',
                             jsonld=[{"@context": "https://schema.org", "@type": "WebSite", "name": "Tools for World", "alternateName": BRAND_NAMES, "url": BASE},
                                     {"@context": "https://schema.org", "@type": "Organization", "name": "Tools for World", "alternateName": BRAND_NAMES, "url": BASE, "logo": BASE + "logo.png",
                                      "email": "hello@toolsforworld.com"}], keywords=BRAND_KEYWORDS))

    info = {
        "about": ("About Tools for World", "Tools for World makes free, simple and private online tools for everyday tasks.",
                  '''<h1>About Tools for World</h1><p>Tools for World is a free collection of everyday online tools: PDF and Word converters, image compressors and converters, a background remover, OCR, a QR code generator, a password generator and more.</p>
<p>All tools run inside your browser. Files you open are processed on your own device and are never uploaded to our servers.</p>
<p>We keep the tools simple, fast and free, with no sign-up and no watermarks.</p>
<p>You may also see us written as ToolsForWorld, Tools4World or Tools 4 World. It's the same site: <a href="https://toolsforworld.com/">toolsforworld.com</a>.</p>'''),
        "privacy": ("Privacy Policy – Tools for World", "How Tools for World handles your data: files are processed on your device, plus how ads, cookies and analytics work.",
                    f'''<h1>Privacy Policy</h1><p>Last updated: {TODAY}</p>
<h2>Your files and numbers</h2><p>Tools for World tools work entirely in your browser. Images, PDFs, Word documents and the numbers you type are processed on your device and are not sent to or stored on our servers.</p>
<h2>Cookies and advertising</h2><p>We may show ads from Google AdSense. Google and its partners use cookies to show ads based on your visits to this and other websites. You can turn off personalised ads in <a href="https://adssettings.google.com">Google Ads Settings</a>. Learn more at <a href="https://policies.google.com/technologies/ads">How Google uses information from sites that use its services</a>.</p>
<h2>Your consent choices</h2><p>Visitors in the European Economic Area, the UK and Switzerland are asked for consent before personalised ads, using Google's certified consent message. You can choose not to consent, and you can change your choice later from the same message or by clearing this site's cookies.</p>
<h2>Analytics</h2><p>We use Cloudflare Web Analytics to count page visits and measure page speed. It does not use cookies and never sees the content of your files.</p>
<h2>Stored in your browser</h2><p>The home page shows the tools you opened recently. That list is kept only in your browser's local storage, is never sent to us, and disappears when you clear this site's data.</p>
<h2>Third-party code</h2><p>Some tools load open-source libraries (pdf-lib, PDF.js, Mammoth, html2pdf.js, Tesseract.js, heic2any, lamejs, JSZip, qrcode-generator, IMG.LY background removal) and fonts. See <a href="../credits/">open-source credits</a> for their licences. These libraries and fonts load from public CDNs such as cdnjs, jsDelivr and Google Fonts, and the OCR language data and background-removal AI model are downloaded from their publishers' servers. These services may see your IP address when your browser downloads them, but they never receive your files: the files are processed on your device after the code has been downloaded.</p>
<h2>Children</h2><p>Tools for World is a general-audience site and does not knowingly collect personal information from children.</p>
<h2>Contact</h2><p>Questions about this policy: see our <a href="../contact/">contact page</a>.</p>'''),
        "terms": ("Terms of Use – Tools for World", "The terms for using Tools for World's free online PDF, image and text tools, including limits of liability.",
                  f'''<h1>Terms of Use</h1><p>Last updated: {TODAY}</p><p>Tools for World tools are free to use for personal and business purposes. They are provided “as is”, without any warranty, and we are not liable for any loss arising from their use.</p>
<p>Results such as conversions and calculations are provided for convenience. Check important documents and figures before you rely on them.</p>
<p>You are responsible for the files you process. Only convert files you own or have permission to use, and do not use the tools for anything illegal.</p>
<p>Official photo sizes and other rules shown on this site are a guide. Always check the latest requirements with the official authority before you submit an application.</p>
<p>We may change or remove tools and these terms at any time. Questions: see our <a href="../contact/">contact page</a>.</p>'''),
        "credits": ("Open-Source Credits – Tools for World", "The open-source libraries and fonts that power Tools for World, with their licences.",
                    '''<h1>Open-source credits</h1><p>Tools for World is built on excellent open-source software. Thank you to everyone who makes these projects. Each library is used unmodified and is loaded from a public CDN; follow the links for the source code and full licence text.</p>
<div class="scroll"><table class="t"><thead><tr><th>Project</th><th>Used for</th><th>Licence</th></tr></thead><tbody>
<tr><td><a href="https://github.com/mozilla/pdf.js">PDF.js</a> (Mozilla)</td><td>Reading PDFs: PDF to Word, PDF to JPG, compress PDF</td><td><a href="https://github.com/mozilla/pdf.js/blob/master/LICENSE">Apache-2.0</a></td></tr>
<tr><td><a href="https://github.com/Hopding/pdf-lib">pdf-lib</a></td><td>Creating PDFs: merge, split, JPG to PDF, compress PDF</td><td><a href="https://github.com/Hopding/pdf-lib/blob/master/LICENSE.md">MIT</a></td></tr>
<tr><td><a href="https://github.com/mwilliamson/mammoth.js">Mammoth.js</a></td><td>Reading Word (.docx) files</td><td><a href="https://github.com/mwilliamson/mammoth.js/blob/master/LICENSE">BSD-2-Clause</a></td></tr>
<tr><td><a href="https://github.com/eKoopmans/html2pdf.js">html2pdf.js</a> (with jsPDF and html2canvas)</td><td>Word to PDF</td><td><a href="https://github.com/eKoopmans/html2pdf.js/blob/main/LICENSE">MIT</a></td></tr>
<tr><td><a href="https://github.com/naptha/tesseract.js">Tesseract.js</a> and <a href="https://github.com/tesseract-ocr/tesseract">Tesseract OCR</a></td><td>Image to text (OCR) and language data</td><td><a href="https://github.com/naptha/tesseract.js/blob/master/LICENSE.md">Apache-2.0</a></td></tr>
<tr><td><a href="https://github.com/imgly/background-removal-js">IMG.LY Background Removal</a></td><td>Background remover (AI model runs in your browser)</td><td><a href="https://github.com/imgly/background-removal-js/blob/main/LICENSE.md">AGPL-3.0</a> – used unmodified; source code at the link</td></tr>
<tr><td><a href="https://github.com/microsoft/onnxruntime">ONNX Runtime Web</a></td><td>Runs the background-removal model</td><td><a href="https://github.com/microsoft/onnxruntime/blob/main/LICENSE">MIT</a></td></tr>
<tr><td><a href="https://github.com/alexcorvi/heic2any">heic2any</a> (includes <a href="https://github.com/strukturag/libheif">libheif</a>)</td><td>HEIC to JPG</td><td><a href="https://github.com/alexcorvi/heic2any/blob/master/LICENSE">MIT</a>; libheif <a href="https://github.com/strukturag/libheif/blob/master/COPYING">LGPL-3.0</a></td></tr>
<tr><td><a href="https://github.com/zhuker/lamejs">lamejs</a></td><td>MP4 to MP3 (MP3 encoding)</td><td><a href="https://github.com/zhuker/lamejs/blob/master/LICENSE">LGPL-3.0</a> – used unmodified; source code at the link</td></tr>
<tr><td><a href="https://github.com/Stuk/jszip">JSZip</a></td><td>Building .docx files for PDF to Word</td><td><a href="https://github.com/Stuk/jszip/blob/main/LICENSE.markdown">MIT or GPL-3.0</a> (used under MIT)</td></tr>
<tr><td><a href="https://github.com/kazuhikoarase/qrcode-generator">qrcode-generator</a></td><td>QR code generator</td><td><a href="https://github.com/kazuhikoarase/qrcode-generator/blob/master/LICENSE">MIT</a></td></tr>
<tr><td><a href="https://fonts.google.com/specimen/Bricolage+Grotesque">Bricolage Grotesque</a>, <a href="https://fonts.google.com/specimen/Figtree">Figtree</a>, <a href="https://fonts.google.com/specimen/JetBrains+Mono">JetBrains Mono</a></td><td>Fonts</td><td><a href="https://openfontlicense.org/">SIL Open Font License 1.1</a></td></tr>
</tbody></table></div>
<p>Trademarks and product names mentioned on this site belong to their owners. Tools for World is an independent project and is not affiliated with any government office or with the projects above.</p>
<p>Spotted a missing credit? Please tell us via the <a href="../contact/">contact page</a>.</p>'''),
        "contact": ("Contact – Tools for World", "Contact Tools for World to report a bug, suggest a new free tool or ask a question about privacy.",
                    '''<h1>Contact</h1><p>Found a bug, or want a new tool? We would love to hear from you.</p><p>Email: <b>hello@toolsforworld.com</b>.</p>
<p>When reporting a problem, tell us which tool you used, your device and browser (for example “iPhone, Safari” or “Windows, Chrome”), and what happened. Please don't send us private documents: our tools never need your files, because everything runs in your browser.</p>'''),
    }
    for slug, (title, desc, content) in info.items():
        write(f"{slug}/index.html", page("../", title, desc, BASE + slug + "/", f'<section class="bench how" style="max-width:70ch">{content}</section>'))
        urls.append(BASE + slug + "/")

    write("404.html", page(BASE, "Page not found – Tools for World", "Page not found.", BASE, f'<section class="bench"><h1>Page not found</h1><p class="lead">This page does not exist. <a href="{BASE}">See all tools</a>.</p></section>'))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    write("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="31" fill="#0d7a55"/><g fill="none" stroke="#fff" stroke-width="3.6"><circle cx="32" cy="32" r="19"/><ellipse cx="32" cy="32" rx="8.5" ry="19"/><path d="M13.6 26h36.8M13.6 38h36.8"/></g></svg>')
    if ADSENSE_CLIENT:
        write("ads.txt", f"google.com, {ADSENSE_CLIENT.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    write(".nojekyll", "")
    print(f"built {len(urls)} pages")

if __name__ == "__main__":
    build()
