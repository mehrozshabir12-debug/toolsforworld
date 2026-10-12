"""Builds the Tools for World static site: one folder per tool, plus home, about, privacy, terms, sitemap.
Run:  python3 build.py            (BASE = public URL used for canonical links and the sitemap)
"""
import json, os, html, datetime

ROOT = os.environ.get("TK_OUT") or os.path.dirname(os.path.abspath(__file__))
PREVIEW = bool(os.environ.get("TK_PREVIEW"))
import re
BASE = os.environ.get("TK_BASE", "https://toolsforworld.com/")
TODAY = datetime.date.today().isoformat()
PDFLIB = '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js"></script>'
PDFJS = '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>'
MAMMOTH = '<script src="https://cdn.jsdelivr.net/npm/mammoth@1.8.0/mammoth.browser.min.js"></script>'
H2PDF = '<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>'

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

FILE_UI = '''<label class="drop" id="drop" tabindex="0"><input type="file" id="fin"><strong id="d-main">Choose files</strong><span id="d-sub">or drag and drop them here</span></label>
<div class="panel" id="panel" hidden><div class="files" id="list"></div><div id="opts"></div>
<div class="row"><button class="btn" id="go">Start</button><button class="btn ghost" id="clear">Clear</button><span class="note" id="status" role="status"></span></div>
<div class="out" id="out"></div>EXTRA</div>'''

# ------------------------------------------------------------------ tools
T = []
def tool(**k): T.append(k)
import tools_list
tools_list.define(tool, F, N, SEL, RESULT, PDFLIB, PDFJS, MAMMOTH, H2PDF)

GROUPS = [("pdf", "PDF & document tools"), ("img", "Image tools"), ("util", "Text & everyday tools"), ("media", "Audio & video")]
NAV = {"pdf": "PDF", "img": "Image", "util": "Utilities", "media": "Audio"}

# ------------------------------------------------------------------ layout
def page(rel_root, title, desc, canon, body, scripts="", body_attr="", jsonld=None, active=""):
    nav = "".join(f'<a href="{rel_root}#{g}"{" aria-current=true" if active == g else ""}>{NAV[g]}</a>' for g, l in GROUPS)
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{canon}"><meta property="og:type" content="website"><meta property="og:site_name" content="Tools for World">
<link rel="icon" href="{rel_root}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Figtree:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">
<link rel="stylesheet" href="{rel_root}assets/style.css">
{ld}
</head>
<body{body_attr}>
<header><div class="wrap"><a class="logo" href="{rel_root}" aria-label="Tools for World home"><svg viewBox="0 0 32 32" width="40" height="40" aria-hidden="true"><circle cx="16" cy="16" r="15" fill="var(--accent)"/><g fill="none" stroke="var(--accent-ink)" stroke-width="1.8"><circle cx="16" cy="16" r="9.5"/><ellipse cx="16" cy="16" rx="4.2" ry="9.5"/><path d="M6.8 13h18.4M6.8 19h18.4"/></g></svg><span>Tools <i>for</i> World</span></a><nav aria-label="Main">{nav}</nav></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap"><span>© <span id="yr">{datetime.date.today().year}</span> Tools for World · Free tools that run in your browser.</span>
<span><a href="{rel_root}about/">About</a> · <a href="{rel_root}privacy/">Privacy Policy</a> · <a href="{rel_root}terms/">Terms</a> · <a href="{rel_root}contact/">Contact</a></span></div></footer>
{scripts}
</body>
</html>
'''

def cards(rel_root, items):
    return '<div class="grid">' + "".join(
        f'<a class="tool" href="{rel_root}{t["slug"]}/"><span class="ic">{ICON[t["icon"]]}</span><span><h2>{t["name"]}</h2><p>{t["card"]}</p></span></a>' for t in items) + "</div>"

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
        related = [x for x in T if x["group"] == t["group"] and x["slug"] != t["slug"]][:4]
        if "ftool" in t:
            ui = FILE_UI.replace("EXTRA", t.get("extra", ""))
            scripts = t["libs"] + f'<script src="{r}assets/files.js"></script>'
            attr = f' data-tool="{t["ftool"]}"'
        else:
            ui = t["ui"]; scripts = t.get("libs", "") + f'<script src="{r}assets/calc.js"></script>'; attr = f' data-calc="{t["calc"]}"'
        group_name = dict(GROUPS)[t["group"]]
        body = f'''<p class="crumbs"><a href="{r}">Home</a> › <a href="{r}#{t["group"]}">{group_name}</a></p>
<section class="bench"><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p>
{ui}
<div class="how">{t["body"]}{f'<h2>Questions</h2><div class="faq">{faq}</div>' if faq else ""}</div>
<div class="related"><div class="sect">More {group_name.lower()}</div>{cards(r, related)}</div></section>'''
        canon = BASE + t["slug"] + "/"
        ld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": t["name"], "url": canon, "applicationCategory": "UtilitiesApplication",
               "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": t["desc"]}]
        if t.get("faq"):
            ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]})
        write(f'{t["slug"]}/index.html', page(r, t["title"], t["desc"], canon, body, scripts, attr, ld, t["group"]))
        urls.append(canon)

    home = '''<div class="hero"><p class="brand-big" aria-hidden="true">Tools <i>for</i> World</p><h1>Free online tools that keep your files private</h1>
<p>Convert PDF and Word files, compress and edit images, remove backgrounds, make QR codes and more. No sign-up, no watermark, no limits. Every tool runs in your browser, so your files never leave your device.</p></div>'''
    for g, label in GROUPS:
        home += f'<div class="sect" id="{g}">{label}</div>' + cards("", [t for t in T if t["group"] == g])
    write("index.html", page("", "Tools for World – Free PDF, Image & Everyday Tools Online",
                             "Free online tools: PDF to Word, Word to PDF, compress PDF and images, background remover, HEIC to JPG, OCR, QR code generator, MP4 to MP3 and more. Private: files never leave your device.",
                             BASE, home, f'<script src="assets/calc.js"></script>',
                             jsonld=[{"@context": "https://schema.org", "@type": "WebSite", "name": "Tools for World", "url": BASE}]))

    info = {
        "about": ("About Tools for World", "Tools for World makes free, simple and private online tools for everyday tasks.",
                  '''<h1>About Tools for World</h1><p>Tools for World is a free collection of everyday online tools: PDF and Word converters, image compressors and converters, a background remover, OCR, a QR code generator, a password generator and more.</p>
<p>All tools run inside your browser. Files you open are processed on your own device and are never uploaded to our servers.</p>
<p>We keep the tools simple, fast and free, with no sign-up and no watermarks.</p>'''),
        "privacy": ("Privacy Policy – Tools for World", "How Tools for World handles your data.",
                    f'''<h1>Privacy Policy</h1><p>Last updated: {TODAY}</p>
<h2>Your files and numbers</h2><p>Tools for World tools work entirely in your browser. Images, PDFs, Word documents and the numbers you type are processed on your device and are not sent to or stored on our servers.</p>
<h2>Cookies and advertising</h2><p>We may show ads from Google AdSense. Google and its partners use cookies to show ads based on your visits to this and other websites. You can turn off personalised ads in <a href="https://adssettings.google.com">Google Ads Settings</a>. Learn more at <a href="https://policies.google.com/technologies/ads">How Google uses information from sites that use its services</a>.</p>
<h2>Analytics</h2><p>We may use privacy-friendly analytics to count page visits. This does not include the content of your files.</p>
<h2>Third-party code</h2><p>Some tools load open-source libraries (pdf-lib, PDF.js, Mammoth, html2pdf.js, Tesseract.js, heic2any, lamejs, JSZip, qrcode-generator, IMG.LY background removal) and fonts from public CDNs such as cdnjs, jsDelivr and Google Fonts. These services may see your IP address when your browser downloads them.</p>
<h2>Children</h2><p>Tools for World is a general-audience site and does not knowingly collect personal information from children.</p>
<h2>Contact</h2><p>Questions about this policy: see our <a href="../contact/">contact page</a>.</p>'''),
        "terms": ("Terms of Use – Tools for World", "Terms for using Tools for World tools.",
                  f'''<h1>Terms of Use</h1><p>Last updated: {TODAY}</p><p>Tools for World tools are free to use for personal and business purposes. They are provided “as is”, without any warranty.</p>
<p>Results such as conversions and calculations are provided for convenience. Check important documents and figures before you rely on them.</p>
<p>You are responsible for the files you process. Do not use the tools for anything illegal.</p>'''),
        "contact": ("Contact – Tools for World", "Contact Tools for World with feedback or tool requests.",
                    '''<h1>Contact</h1><p>Found a bug, or want a new tool? We would love to hear from you.</p><p>Email: <b>hello@toolsforworld.com</b> (active once the domain is set up).</p>'''),
    }
    for slug, (title, desc, content) in info.items():
        write(f"{slug}/index.html", page("../", title, desc, BASE + slug + "/", f'<section class="bench how" style="max-width:70ch">{content}</section>'))
        urls.append(BASE + slug + "/")

    write("404.html", page(BASE, "Page not found – Tools for World", "Page not found.", BASE, f'<section class="bench"><h1>Page not found</h1><p class="lead">This page does not exist. <a href="{BASE}">See all tools</a>.</p></section>'))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    write("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="31" fill="#0d7a55"/><g fill="none" stroke="#fff" stroke-width="3.6"><circle cx="32" cy="32" r="19"/><ellipse cx="32" cy="32" rx="8.5" ry="19"/><path d="M13.6 26h36.8M13.6 38h36.8"/></g></svg>')
    write(".nojekyll", "")
    print(f"built {len(urls)} pages")

if __name__ == "__main__":
    build()
