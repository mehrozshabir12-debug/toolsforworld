"""Checks the LIVE site: HTTP headers, ads.txt, robots, sitemap, and whether AdSense actually serves ads.
Writes tests/live_report.json."""
import json, os, re, subprocess, urllib.request
from playwright.sync_api import sync_playwright

B = "https://toolsforworld.com/"
rep = {}
def get(u):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 audit"}), timeout=30)
    return r.status, dict(r.headers), r.read().decode("utf-8", "replace")
for path in ("", "ads.txt", "robots.txt", "sitemap.xml", "pdf-to-word/", "does-not-exist-xyz/"):
    try:
        st, h, body = get(B + path)
    except urllib.error.HTTPError as e:
        st, h, body = e.code, dict(e.headers), ""
    except Exception as e:
        rep[path or "/"] = {"error": str(e)[:200]}; continue
    keep = {k: v for k, v in h.items() if k.lower() in ("strict-transport-security", "content-security-policy", "x-frame-options", "x-content-type-options",
                                                         "referrer-policy", "permissions-policy", "cache-control", "server", "content-type", "age", "via")}
    rep[path or "/"] = {"status": st, "headers": keep, "bytes": len(body), "start": body[:160] if path in ("ads.txt", "robots.txt") else None,
                        "sitemap_urls": len(re.findall("<loc>", body)) if path == "sitemap.xml" else None}
try:
    rep["http_redirect"] = subprocess.run(["curl", "-sI", "http://toolsforworld.com/"], capture_output=True, text=True, timeout=30).stdout[:300]
    rep["www_redirect"] = subprocess.run(["curl", "-sI", "https://www.toolsforworld.com/"], capture_output=True, text=True, timeout=30).stdout[:300]
except Exception as e:
    rep["redirect_error"] = str(e)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, ctxargs in (("desktop", {}), ("mobile", p.devices["Pixel 7"])):
        ctx = b.new_context(**ctxargs); pg = ctx.new_page(); reqs = []
        pg.on("request", lambda r: reqs.append(r.url) if re.search(r"googlesyndication|doubleclick|adtrafficquality|fundingchoices", r.url) else None)
        pg.goto(B + "compress-image/", wait_until="load", timeout=60000); pg.wait_for_timeout(9000)
        pg.mouse.wheel(0, 3000); pg.wait_for_timeout(4000)
        info = pg.evaluate("""() => ({
            ins: [...document.querySelectorAll('ins.adsbygoogle')].map(e => ({status: e.dataset.adStatus || null, w: e.offsetWidth, h: e.offsetHeight, auto: e.className})),
            adIframes: [...document.querySelectorAll('iframe')].filter(f => /google|doubleclick/.test(f.src || f.id || '')).length,
            consent: !!document.querySelector('.fc-consent-root, .fc-dialog-container')})""")
        rep["ads_" + name] = {**info, "ad_requests": len(reqs), "ad_request_kinds": sorted({re.sub(r"\?.*", "", u)[:90] for u in reqs})[:12]}
        ctx.close()
    b.close()
json.dump(rep, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "live_report.json"), "w"), indent=1)
print(json.dumps(rep, indent=1)[:4000])
