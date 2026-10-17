"""Builds the Tools for World static site: one folder per tool, plus home, about, privacy, terms, sitemap.
Run:  python3 build.py            (BASE = public URL used for canonical links and the sitemap)
"""
import json, os, html, datetime

ROOT = os.environ.get("TK_OUT") or os.path.dirname(os.path.abspath(__file__))
PREVIEW = bool(os.environ.get("TK_PREVIEW"))
import re
BASE = os.environ.get("TK_BASE", "https://toolsforworld.com/")
TODAY = os.environ.get("TK_TODAY") or datetime.date.today().isoformat()
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
import landing_notes
landing_notes.enrich(T)
import query_boost
query_boost.enrich(T)
BY = {t['slug']: t for t in T}

# Hand-picked "related tools" for each main tool (what people usually need next)
RELATED = {
    "pdf-to-word": ["word-to-pdf", "image-to-text", "compress-pdf", "pdf-to-jpg"],
    "word-to-pdf": ["pdf-to-word", "compress-pdf", "merge-pdf", "jpg-to-pdf"],
    "compress-pdf": ["compress-pdf-to-200kb", "split-pdf", "merge-pdf", "compress-image", "word-to-pdf"],
    "merge-pdf": ["split-pdf", "compress-pdf", "jpg-to-pdf", "word-to-pdf"],
    "split-pdf": ["merge-pdf", "compress-pdf", "pdf-to-jpg", "pdf-to-word"],
    "jpg-to-pdf": ["compress-image", "merge-pdf", "compress-pdf", "heic-to-jpg", "word-to-pdf"],
    "pdf-to-jpg": ["compress-image", "image-to-text", "split-pdf", "jpg-to-pdf"],
    "image-to-text": ["pdf-to-word", "pdf-to-jpg", "word-counter", "image-to-text-urdu"],
    "compress-image": ["resize-image", "compress-image-to-100kb", "jpg-to-pdf", "heic-to-jpg"],
    "resize-image": ["compress-image", "passport-photo-maker", "remove-background", "resize-image-to-1080x1080"],
    "remove-background": ["passport-photo-maker", "resize-image", "compress-image", "png-to-jpg", "jpg-to-png"],
    "png-to-jpg": ["jpg-to-png", "webp-to-jpg", "compress-image", "heic-to-jpg"],
    "jpg-to-png": ["png-to-jpg", "remove-background", "compress-image", "webp-to-jpg"],
    "webp-to-jpg": ["png-to-jpg", "heic-to-jpg", "compress-image", "resize-image", "mp4-to-mp3"],
    "heic-to-jpg": ["compress-image", "jpg-to-pdf", "webp-to-jpg", "resize-image", "mp4-to-mp3"],
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
GA_ID = "G-VCVTPZQZKP"  # Google Analytics 4

GROUPS = [("pdf", "PDF & document tools"), ("img", "Image tools"), ("util", "Text & everyday tools"), ("media", "Audio & video")]
NAV = {"pdf": "PDF", "img": "Image", "util": "Utilities", "media": "Audio"}

# ------------------------------------------------------------------ layout
BRAND_NAMES = ["ToolsForWorld", "Tools 4 World", "Tools4World", "Tool for World", "Tools for the World", "Tool4World", "toolsforworld.com"]
BRAND_KEYWORDS = "Tools for World, toolsforworld, tools for world, tools 4 world, tools4world, tool for world, tool 4 world, tools world, toolsforworld.com, free online tools, PDF tools, image tools"


def _v(name):
    """Short content hash for cache-busting: a changed file gets a new URL, so browsers never mix old CSS with new HTML."""
    import hashlib
    try:
        return hashlib.sha256(open(os.path.join(ROOT, "assets", name), "rb").read()).hexdigest()[:8]
    except OSError:
        return "0"


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
<!-- Google tag (gtag.js): only real visitors on the live site, never test browsers or local copies --><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}if(location.hostname==='toolsforworld.com'&&!navigator.webdriver){{var g=document.createElement('script');g.async=true;g.src='https://www.googletagmanager.com/gtag/js?id={GA_ID}';document.head.appendChild(g);gtag('js',new Date());gtag('config','{GA_ID}');}}</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta http-equiv="Content-Security-Policy" content="object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">{f'<meta name="keywords" content="{html.escape(keywords)}">' if keywords else ""}
{f'<link rel="canonical" href="{canon}">' if canon else '<meta name="robots" content="noindex">'}
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">{f'<meta property="og:url" content="{canon}">' if canon else ""}<meta property="og:type" content="website"><meta property="og:site_name" content="Tools for World"><meta property="og:image" content="{BASE}og-image.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="https://toolsforworld.com/favicon.ico" sizes="48x48"><link rel="icon" href="https://toolsforworld.com/favicon-96.png" type="image/png" sizes="96x96"><link rel="icon" href="https://toolsforworld.com/favicon-192.png" type="image/png" sizes="192x192"><link rel="icon" href="https://toolsforworld.com/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="https://toolsforworld.com/apple-touch-icon.png"><link rel="manifest" href="https://toolsforworld.com/site.webmanifest"><meta name="theme-color" content="#0d7a55">
{(f'<meta name="google-adsense-account" content="{ADSENSE_CLIENT}"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>') if ADSENSE_CLIENT else ""}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{FONTS}"><link rel="stylesheet" href="{FONTS}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="{FONTS}"></noscript>
<link rel="stylesheet" href="{rel_root}assets/style.css?v={_v("style.css")}">
{ld}
</head>
<body{body_attr}>
<header><div class="wrap"><a class="logo" href="{rel_root}" aria-label="Tools for World home"><svg viewBox="0 0 32 32" width="40" height="40" aria-hidden="true"><circle cx="16" cy="16" r="15" fill="var(--accent)"/><g fill="none" stroke="var(--accent-ink)" stroke-width="1.8"><circle cx="16" cy="16" r="9.5"/><ellipse cx="16" cy="16" rx="4.2" ry="9.5"/><path d="M6.8 13h18.4M6.8 19h18.4"/></g></svg><span>Tools <i>for</i> World</span></a><nav aria-label="Main">{nav}<a href="{rel_root}#all" class="navall">All tools</a></nav><form class="hsearch" role="search" action="{rel_root}" method="get"><input type="search" name="q" placeholder="Search tools…" aria-label="Search tools" autocomplete="off"></form></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap"><span>© <span id="yr">{datetime.date.today().year}</span> Tools for World · Free tools that run in your browser.</span>
<span><a href="{rel_root}guides/">Guides</a> · <a href="{rel_root}about/">About</a> · <a href="{rel_root}privacy/">Privacy Policy</a> · <a href="{rel_root}terms/">Terms</a> · <a href="{rel_root}contact/">Contact</a> · <a href="{rel_root}credits/">Open-source credits</a></span></div></footer>
{scripts}
<script src="{rel_root}assets/site.js?v={_v("site.js")}" defer></script>
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

# Real "last changed" dates: a page's date moves only when its content changes (kept in lastmod.json).
LASTMOD_FILE = os.path.join(ROOT, "lastmod.json")
try:
    LASTMOD = json.load(open(LASTMOD_FILE))
except Exception:
    LASTMOD = {}
PAGE_DATE = {}


def page_url(rel_path):
    return BASE + ("" if rel_path == "index.html" else rel_path[: -len("index.html")])


def write(rel_path, content):
    if rel_path.endswith("index.html") and not PREVIEW:
        import hashlib
        url = page_url(rel_path)
        h = hashlib.sha256(re.sub(r"\?v=[0-9a-f]{8}", "", content).encode()).hexdigest()[:16]  # asset versions don't count as a content change
        old = LASTMOD.get(url)
        date = old[1] if old and old[0] == h else TODAY
        LASTMOD[url] = [h, date]; PAGE_DATE[url] = date
        content = content.replace("__LASTMOD__", date)
    if PREVIEW and rel_path.endswith(".html"):
        content = re.sub(r'href="((?:\.\./)*(?:[a-z0-9-]+/)?)(#[a-z]*)?"', lambda m: f'href="{m.group(1)}index.html{m.group(2) or ""}"', content)
    p = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

GUIDE_FOR = {  # tool family (main slug) -> guides that explain it
    "passport-photo-maker": ["passport-photo-size-by-country"],
    "compress-image": ["how-to-compress-photo-to-50kb"],
    "compress-pdf": ["reduce-scanned-pdf-size"],
    "jpg-to-pdf": ["reduce-scanned-pdf-size"],
    "resize-image": ["social-media-image-sizes", "image-resolution-sizes-explained"],
}
EXTRA_GUIDE = {"resize-image-to-600x600": "passport-photo-size-by-country", "us-passport-photo": "passport-photo-size-by-country"}


def guide_links(r, t, par):
    import guides as G
    by = {g["slug"]: g for g in G.GUIDES}
    fam = par["slug"] if par else t["slug"]
    slugs = list(GUIDE_FOR.get(fam, []))
    if t["slug"] in EXTRA_GUIDE and EXTRA_GUIDE[t["slug"]] not in slugs:
        slugs.append(EXTRA_GUIDE[t["slug"]])
    if "ftool" in t:
        slugs.append("check-files-never-uploaded")
    items = "".join(f'<li><a href="{r}guides/{g}/">{html.escape(by[g]["h1"])}</a></li>' for g in slugs if g in by)
    return f'<h2>Helpful guides</h2><ul class="guidelinks">{items}</ul>' if items else ""


def build():
    urls = [BASE]
    for t in T:
        r = "../"
        faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t.get("faq", []))
        par = BY.get(t.get("parent"))
        kids = [x for x in T if x.get("parent") == t["slug"]]
        if par:
            fam = [x for x in T if x.get("parent") == par["slug"]]
            i = fam.index(t)
            sibs = fam[i + 1:] + fam[:i]   # the next pages in the family, wrapping round, so every page gets links
            related = [par] + sibs[:5] + [BY[x] for x in RELATED.get(par["slug"], [])[:2] if x in BY]
        else:
            related = [BY[x] for x in RELATED.get(t["slug"], []) if x in BY] or \
                      [x for x in T if x["group"] == t["group"] and x["slug"] != t["slug"] and not x.get("parent")][:4]
        preset = f'<script>window.PRESET={json.dumps(t["preset"])}</script>' if t.get("preset") else ""
        if "ftool" in t:
            ui = FILE_UI.replace("EXTRA", t.get("extra", "")).replace('<span class="fmt" id="d-fmt"></span>', f'<span class="fmt" id="d-fmt">{FMT.get(t["ftool"], "")}</span>')
            scripts = preset + f'<script src="{r}assets/files.js?v={_v("files.js")}"></script>'
            attr = f' data-tool="{t["ftool"]}"'
        else:
            ui = t.get("ui") or par["ui"]; scripts = preset + t.get("libs", "") + f'<script src="{r}assets/calc.js?v={_v("calc.js")}"></script>'; attr = f' data-calc="{t["calc"]}"'
        group_name = dict(GROUPS)[t["group"]]
        body = f'''<p class="crumbs"><a href="{r}">Home</a> › <a href="{r}#{t["group"]}">{group_name}</a>{f' › <a href="{r}{par["slug"]}/">{par["name"]}</a>' if par else ""}</p>
<section class="bench"><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p>
{chips(r, kids, "Popular presets") if kids else ""}
{ui}
<div class="how">{t["body"]}{guide_links(r, t, par)}{f'<h2>Questions</h2><div class="faq">{faq}</div>' if faq else ""}</div>
<div class="related"><div class="sect">{"Related tools" if par else "More " + group_name.lower()}</div>{cards(r, related)}</div></section>'''
        canon = BASE + t["slug"] + "/"
        ld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": t["name"], "url": canon, "applicationCategory": "UtilitiesApplication",
               "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": t["desc"]}]
        if t.get("faq"):
            ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]})
        write(f'{t["slug"]}/index.html', page(r, t["title"], t["desc"], canon, body, scripts, attr, ld, t["group"]))
        urls.append(canon)

    # ---- home: tool grid with category filter (each tool has its own colour and icon) ----
    def short_names(kids):
        names = [k["name"] for k in kids]
        if len(names) < 2:
            return names
        pre = os.path.commonprefix(names); pre = pre[:pre.rfind(" ") + 1] if " " in pre else ""
        rev = os.path.commonprefix([n[::-1] for n in names])[::-1]; suf = rev[rev.find(" "):] if " " in rev else ""
        out = [n[len(pre):len(n) - len(suf)] if suf else n[len(pre):] for n in names]
        return [o.strip() or n for o, n in zip(out, names)]

    def sv(d):
        return ('<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + d + '</svg>')
    DOC = '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>'
    TILE = {  # slug: (colour, icon)
        "pdf-to-word": ("#2563eb", sv(DOC + '<path d="M8.5 12.5l1.2 4 1.3-3 1.3 3 1.2-4"/>')),
        "word-to-pdf": ("#0e7490", sv(DOC + '<path d="M9 17v-4h1.5a1.25 1.25 0 0 1 0 2.5H9"/>')),
        "compress-pdf": ("#dc2626", sv(DOC + '<path d="M12 10v3m0 0l-2-2m2 2l2-2M12 18v-3m0 0l-2 2m2-2l2 2"/>')),
        "merge-pdf": ("#ea580c", sv('<rect x="3" y="4" width="8" height="11" rx="1.5"/><rect x="13" y="9" width="8" height="11" rx="1.5"/><path d="M9 18h3"/>')),
        "split-pdf": ("#b45309", sv('<circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><path d="M8 7.5L20 18M8 16.5L20 6"/>')),
        "jpg-to-pdf": ("#e11d48", sv('<rect x="3" y="5" width="11" height="9" rx="1.5"/><circle cx="7" cy="8.5" r="1.2"/><path d="M3 12l3-2 4 3"/><path d="M15 10h4a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-8a2 2 0 0 1-2-2v-2"/>')),
        "pdf-to-jpg": ("#d97706", sv(DOC + '<circle cx="10" cy="13" r="1.3"/><path d="M7 18l3-3 2 2 2-2 3 3"/>')),
        "image-to-text": ("#7c3aed", sv('<path d="M4 8V5a1 1 0 0 1 1-1h3M16 4h3a1 1 0 0 1 1 1v3M20 16v3a1 1 0 0 1-1 1h-3M8 20H5a1 1 0 0 1-1-1v-3"/><path d="M8 9h8M8 12h8M8 15h5"/>')),
        "compress-image": ("#16a34a", sv('<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M9 9L6 6M9 9H6.5M9 9V6.5M15 15l3 3M15 15h2.5M15 15v2.5"/>')),
        "resize-image": ("#0d9488", sv('<rect x="3" y="9" width="12" height="12" rx="2"/><path d="M13 3h8v8M21 3l-8 8"/>')),
        "remove-background": ("#c026d3", sv('<path d="M5 19L15 9"/><path d="M14 4l1 2 2 1-2 1-1 2-1-2-2-1 2-1zM19 11l.7 1.3L21 13l-1.3.7L19 15l-.7-1.3L17 13l1.3-.7z"/>')),
        "png-to-jpg": ("#0284c7", sv('<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.5"/><path d="M21 16l-5-5-9 9"/>')),
        "jpg-to-png": ("#4f46e5", sv('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M9 4v16"/>')),
        "webp-to-jpg": ("#0891b2", sv('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>')),
        "heic-to-jpg": ("#475569", sv('<rect x="6" y="2.5" width="12" height="19" rx="2.5"/><path d="M11 18.5h2"/><circle cx="12" cy="9" r="2.5"/>')),
        "passport-photo-maker": ("#059669", sv('<rect x="5" y="3" width="14" height="18" rx="2"/><circle cx="12" cy="10" r="2.6"/><path d="M8.5 17c.8-1.8 2-2.6 3.5-2.6s2.7.8 3.5 2.6"/>')),
        "qr-code-generator": ("#1f2937", sv('<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><path d="M14 14h3v3h-3zM20 14v.01M14 20h.01M17 20h4v-3"/>')),
        "word-counter": ("#9333ea", sv('<path d="M4 6h16M4 12h16M4 18h9"/><path d="M17 16v4M15 18h4"/>')),
        "password-generator": ("#b91c1c", sv('<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/><path d="M12 15v2"/>')),
        "age-calculator": ("#db2777", sv('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/><path d="M8 14h2M14 14h2M8 17h2"/>')),
        "percentage-calculator": ("#65a30d", sv('<path d="M19 5L5 19"/><circle cx="7" cy="7" r="2.5"/><circle cx="17" cy="17" r="2.5"/>')),
        "mp4-to-mp3": ("#f97316", sv('<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>')),
    }
    FILTERS = [("all", "All tools"), ("pdf", "PDF & Word"), ("img", "Images"), ("util", "Text & everyday"), ("media", "Audio")]
    order = ["pdf-to-word", "compress-pdf", "compress-image", "remove-background", "word-to-pdf", "jpg-to-pdf", "image-to-text", "passport-photo-maker",
             "merge-pdf", "split-pdf", "pdf-to-jpg", "resize-image", "heic-to-jpg", "png-to-jpg", "jpg-to-png", "webp-to-jpg",
             "qr-code-generator", "word-counter", "password-generator", "age-calculator", "percentage-calculator", "mp4-to-mp3"]
    mains = sorted([t for t in T if not t.get("parent")], key=lambda t: order.index(t["slug"]) if t["slug"] in order else 99)
    TICK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

    def tile(t):
        col, ic = TILE.get(t["slug"], ("#0d7a55", ICON[t["icon"]]))
        return (f'<a class="tile" href="{t["slug"]}/" data-g="{t["group"]}" data-k="{KW.get(t["slug"], "")}">'
                f'<span class="tic" style="--c:{col}">{ic}</span><span class="tn">{t["name"]}</span><span class="td">{t["card"]}</span></a>')

    extra = ""
    for par in [m for m in mains if any(x.get("parent") == m["slug"] for x in T)]:
        kids = [x for x in T if x.get("parent") == par["slug"]]
        extra += (f'<div class="xrow"><a class="xp" href="{par["slug"]}/">{par["name"]}</a>'
                  + "".join(f'<a href="{k["slug"]}/" title="{html.escape(k["name"])}">{n}</a>' for k, n in zip(kids, short_names(kids))) + "</div>")

    home = ('<div class="hero3"><h1>Free tools for every PDF, photo and document</h1>'
            '<p class="sub">All tools run in your browser. Your files never leave your device.</p>'
            '<div class="bigsearch" role="search"><input type="search" id="q" placeholder="Search tools, e.g. compress pdf" aria-label="Search tools" autocomplete="off"></div></div>'
            '<div id="results" hidden><div class="tgrid" id="rgrid"></div><p class="note" id="rnone" hidden>No tool matches that yet. <a href="contact/">Ask us for it</a>.</p></div>'
            '<div id="browse"><div id="recent" hidden><h2 class="h2">Recently used</h2><div class="chips" id="rchips"></div></div>'
            '<div class="filters" role="group" aria-label="Filter tools" id="all">'
            + "".join(f'<button type="button" class="flt" data-f="{k}" aria-pressed="{"true" if k == "all" else "false"}">{lbl}</button>' for k, lbl in FILTERS)
            + '</div><div class="tgrid" id="tgrid">' + "".join(tile(t) for t in mains) + '</div>'
            + f'<ul class="trust"><li>{TICK}Files stay on your device</li><li>{TICK}No sign-up, no watermark, no limits</li><li>{TICK}Works on any phone or computer</li></ul>'
            + '<section class="why" aria-labelledby="why-h"><h2 class="h2" id="why-h">Why Tools for World</h2><div class="whygrid">'
              '<div><h3>Your files stay with you</h3><p>PDFs, photos and scans are processed inside your browser. They are never sent to a server, so a passport scan or a payslip never leaves your device. <a href="guides/check-files-never-uploaded/">Check it yourself in one minute</a>.</p></div>'
              '<div><h3>Made for real forms</h3><p>Job portals, visa forms and universities ask for exact sizes: a photo under 50 KB, a PDF under 2 MB, a 35&nbsp;×&nbsp;45&nbsp;mm passport photo. Each of these has its own ready-set page.</p></div>'
              '<div><h3>Free without catches</h3><p>No account, no watermark, no daily limit and no "upgrade to download". The site is paid for by ads, which never see your files.</p></div>'
              '<div><h3>Tested on every update</h3><p>Every tool is run automatically in a real browser each time the site changes, and official sizes link to the government pages they come from.</p></div>'
              '</div>'
              '<div class="scroll"><table class="t cmp"><caption>How this compares with many online converters</caption><thead><tr><th></th><th>Tools for World</th><th>Many online converters</th></tr></thead><tbody>'
              '<tr><td>Your file is uploaded to a server</td><td>Never</td><td>Usually</td></tr>'
              '<tr><td>Account needed</td><td>No</td><td>Often, for bigger files or more uses</td></tr>'
              '<tr><td>Watermark on results</td><td>No</td><td>Sometimes, on free plans</td></tr>'
              '<tr><td>Daily limit</td><td>No</td><td>Often, on free plans</td></tr>'
              '<tr><td>Exact size presets (KB, pixels, mm)</td><td>Yes</td><td>Varies</td></tr>'
              '</tbody></table></div></section>'
            + f'<details class="xall"><summary>All sizes, countries and languages</summary>{extra}</details></div>'
            + '<p class="aka">Tools for World (also written ToolsForWorld or Tools 4 World) is at toolsforworld.com.</p>')
    write("index.html", page("", "Tools for World – Free PDF, Image & Everyday Tools Online",
                             "Free online tools: PDF to Word, Word to PDF, compress PDF and images, background remover, HEIC to JPG, OCR, QR code generator, MP4 to MP3 and more. Private: files never leave your device.",
                             BASE, home, f'<script src="assets/calc.js?v={_v("calc.js")}"></script>', ' class="home"',
                             jsonld=[{"@context": "https://schema.org", "@type": "WebSite", "name": "Tools for World", "alternateName": BRAND_NAMES, "url": BASE},
                                     {"@context": "https://schema.org", "@type": "Organization", "name": "Tools for World", "alternateName": BRAND_NAMES, "url": BASE, "logo": BASE + "logo.png",
                                      "email": "hello@toolsforworld.com"}], keywords=BRAND_KEYWORDS))

    info = {
        "about": ("About Tools for World", "Tools for World makes free, simple and private online tools for everyday tasks.",
                  '''<h1>About Tools for World</h1><p>Tools for World is a free collection of everyday online tools: PDF and Word converters, image compressors and converters, a background remover, OCR in many languages, passport photo makers, a QR code generator, a password generator and simple calculators.</p>
<h2>Why we built it</h2><p>Most people meet these tasks at awkward moments: a job portal wants a photo under 50 KB, a visa form wants a PDF under 300 KB, or a scanned letter needs to become editable text. Many sites that do this ask you to sign up, add watermarks, or upload private documents to unknown servers. Tools for World was built to do these jobs quickly, for free, without any of that.</p>
<h2>Who makes it</h2><p>Tools for World is an independent project built and maintained by <b>Mehroz Shabir</b>. Every tool is designed, written and tested by hand, and new tools are added based on what visitors ask for.</p>
<h2>How the tools work</h2><p>All tools run inside your browser. Files you open are processed on your own device and are never uploaded to our servers. Where a tool needs extra code, such as the OCR language data or the background-removal model, your browser downloads that code, and then the work happens locally. This is why the tools keep working on slow connections once a page has loaded, and why your documents stay private.</p>
<h2>What we promise</h2><ul><li><b>Free:</b> no sign-up, no limits on use and no watermarks.</li><li><b>Private:</b> your files stay on your device. See our <a href="../privacy/">privacy policy</a>.</li><li><b>Accurate guidance:</b> pages about official sizes, such as passport photos, link to the rules and remind you to check the latest requirements with the official authority.</li><li><b>Tested:</b> every tool is checked automatically in a real browser whenever the site is updated.</li></ul>
<h2>Don't just take our word for it</h2><p>You can confirm that your files are not uploaded using the developer tools built into every desktop browser. Our short guide shows how: <a href="../guides/check-files-never-uploaded/">how to check that your files never leave your device</a>.</p>
<h2>How the site is funded</h2><p>The site is kept free by advertising. Ads never change how a tool works, and they never have access to your files.</p>
<h2>Get in touch</h2><p>Found a bug or want a new tool? Write to us via the <a href="../contact/">contact page</a>. Many of our tools were added because someone asked for them.</p>
<p>You may also see us written as ToolsForWorld, Tools4World or Tools 4 World. It's the same site: <a href="https://toolsforworld.com/">toolsforworld.com</a>.</p>'''),
        "privacy": ("Privacy Policy – Tools for World", "How Tools for World handles your data: files are processed on your device, plus how ads, cookies and analytics work.",
                    f'''<h1>Privacy Policy</h1><p>Last updated: __LASTMOD__</p>
<h2>Your files and numbers</h2><p>Tools for World tools work entirely in your browser. Images, PDFs, Word documents and the numbers you type are processed on your device and are not sent to or stored on our servers.</p>
<h2>Cookies and advertising</h2><p>We may show ads from Google AdSense. Google and its partners use cookies to show ads based on your visits to this and other websites. You can turn off personalised ads in <a href="https://adssettings.google.com">Google Ads Settings</a>. Learn more at <a href="https://policies.google.com/technologies/ads">How Google uses information from sites that use its services</a>.</p>
<h2>Your consent choices</h2><p>Visitors in the European Economic Area, the UK and Switzerland are asked for consent before personalised ads and analytics cookies are used, using Google's certified consent message. You can choose not to consent, and you can change your choice later from the same message or by clearing this site's cookies.</p>
<h2>Analytics</h2><p>We use Google Analytics to understand how visitors use the site, such as which pages and tools are opened, which country visitors come from and what kind of device they use. Google Analytics uses cookies and similar technologies, and the data is processed by Google. It never receives the content of your files. You can learn how Google uses this data at <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites that use its services</a>, and opt out with the <a href="https://tools.google.com/dlpage/gaoptout">Google Analytics opt-out browser add-on</a>.</p><p>We also use Cloudflare Web Analytics to count page visits and measure page speed. It does not use cookies.</p>
<h2>Stored in your browser</h2><p>The home page shows the tools you opened recently. That list is kept only in your browser's local storage, is never sent to us, and disappears when you clear this site's data.</p>
<h2>Third-party code</h2><p>Some tools load open-source libraries (pdf-lib, PDF.js, Mammoth, html2pdf.js, Tesseract.js, heic2any, lamejs, JSZip, qrcode-generator, IMG.LY background removal) and fonts. See <a href="../credits/">open-source credits</a> for their licences. These libraries and fonts load from public CDNs such as cdnjs, jsDelivr and Google Fonts, and the OCR language data and background-removal AI model are downloaded from their publishers' servers. These services may see your IP address when your browser downloads them, but they never receive your files: the files are processed on your device after the code has been downloaded.</p>
<h2>Children</h2><p>Tools for World is a general-audience site and does not knowingly collect personal information from children.</p>
<h2>Contact</h2><p>Questions about this policy: see our <a href="../contact/">contact page</a>.</p>'''),
        "terms": ("Terms of Use – Tools for World", "The terms for using Tools for World's free online PDF, image and text tools, including limits of liability.",
                  f'''<h1>Terms of Use</h1><p>Last updated: __LASTMOD__</p><p>Tools for World tools are free to use for personal and business purposes. They are provided “as is”, without any warranty, and we are not liable for any loss arising from their use.</p>
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
                    '''<h1>Contact</h1><p>Found a bug, or want a new tool? We would love to hear from you.</p><p>Email: <b>hello@toolsforworld.com</b>. We read every message and usually reply within a few working days.</p>
<h2>Reporting a problem</h2><p>Tell us which tool you used, your device and browser (for example “iPhone, Safari” or “Windows, Chrome”), and what happened. A screenshot of any error message helps a lot. Please don't send us private documents: our tools never need your files, because everything runs in your browser.</p>
<h2>Suggesting a tool</h2><p>Describe the job you are trying to do, for example “I need to turn a photo into a 35 × 45 mm print with a blue background”. If a form or website asks for a specific size or format, include its exact wording.</p>
<h2>Before you write</h2><ul><li>Questions about how your data is handled are answered in our <a href="../privacy/">privacy policy</a>.</li><li>Rules for using the site are in our <a href="../terms/">terms of use</a>.</li><li>The open-source software we use is listed on the <a href="../credits/">credits page</a>.</li></ul>'''),
    }
    for slug, (title, desc, content) in info.items():
        write(f"{slug}/index.html", page("../", title, desc, BASE + slug + "/", f'<section class="bench how" style="max-width:70ch">{content}</section>'))
        urls.append(BASE + slug + "/")

    import guides as G
    gl = []
    for g in G.GUIDES:
        r = "../../"; canon = BASE + "guides/" + g["slug"] + "/"
        faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in g["faq"])
        nice = datetime.date.fromisoformat(g["date"]).strftime("%-d %B %Y")
        body = (f'<section class="bench how" style="max-width:75ch"><p class="note"><a href="{r}guides/">Guides</a></p><h1>{g["h1"]}</h1>'
                f'<p class="note">By {G.AUTHOR} · Updated {nice}</p><p class="lead">{g["lead"]}</p>'
                + g["body"].replace("{R}", r) + f'<h2>Questions</h2>{faq}</section>')
        ld = [{"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"],
               "author": {"@type": "Person", "name": G.AUTHOR}, "publisher": {"@type": "Organization", "name": "Tools for World", "logo": {"@type": "ImageObject", "url": BASE + "logo.png"}},
               "datePublished": g["date"], "dateModified": g["date"], "mainEntityOfPage": canon, "image": BASE + "og-image.png"},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}]
        write(f"guides/{g['slug']}/index.html", page(r, g["title"], g["desc"], canon, body, jsonld=ld))
        urls.append(canon)
        gl.append(f'<li><a href="{g["slug"]}/"><b>{g["h1"]}</b></a><br>{g["desc"]}</li>')
    write("guides/index.html", page("../", "Guides – Photo, PDF and Image Size Help | Tools for World",
          "Practical guides to passport photo sizes, compressing photos and PDFs for online forms, and social media image sizes.",
          BASE + "guides/", f'<section class="bench how" style="max-width:75ch"><h1>Guides</h1><p class="lead">Practical, step-by-step help for the jobs our tools do: photo sizes for applications, file-size limits on forms and image sizes for social media.</p><ul>{"".join(gl)}</ul></section>'))
    urls.append(BASE + "guides/")

    write("404.html", page(BASE, "Page not found – Tools for World", "Page not found.", None, f'<section class="bench"><h1>Page not found</h1><p class="lead">This page does not exist. <a href="{BASE}">See all tools</a>.</p></section>'))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"  <url><loc>{u}</loc><lastmod>{PAGE_DATE.get(u, TODAY)}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    if not PREVIEW:
        live = set(urls)
        json.dump({u: v for u, v in sorted(LASTMOD.items()) if u in live}, open(LASTMOD_FILE, "w"), indent=0)
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    write("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="31" fill="#0d7a55"/><g fill="none" stroke="#fff" stroke-width="3.6"><circle cx="32" cy="32" r="19"/><ellipse cx="32" cy="32" rx="8.5" ry="19"/><path d="M13.6 26h36.8M13.6 38h36.8"/></g></svg>')
    if ADSENSE_CLIENT:
        write("ads.txt", f"google.com, {ADSENSE_CLIENT.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    write(".nojekyll", "")
    print(f"built {len(urls)} pages")

if __name__ == "__main__":
    build()
