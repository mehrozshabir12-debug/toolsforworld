"""Lighthouse scores (mobile + desktop) for key pages. Writes tests/lighthouse_report.json.
Usage: python tests/lighthouse.py BASE_URL   (e.g. http://localhost:8001/ or https://toolsforworld.com/)"""
import json, os, subprocess, sys
from playwright.sync_api import sync_playwright

base = sys.argv[1] if len(sys.argv) > 1 else "https://toolsforworld.com/"
label = sys.argv[2] if len(sys.argv) > 2 else "live"
pages = ["", "pdf-to-word/", "compress-image/", "remove-background/", "word-counter/", "compress-pdf-to-200kb/"]
with sync_playwright() as p:
    chrome = p.chromium.executable_path
env = dict(os.environ, CHROME_PATH=chrome)
here = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(here, "lighthouse_report.json")
report = json.load(open(out_path)) if os.path.exists(out_path) else {}
for form in ("mobile", "desktop"):
    for pg in pages:
        url = base + pg
        cmd = ["npx", "-y", "lighthouse@12.2.1", url, "--quiet", "--output=json", "--output-path=/tmp/lh.json",
               "--only-categories=performance,accessibility,best-practices,seo", "--chrome-flags=--headless=new --no-sandbox"]
        if form == "desktop": cmd.append("--preset=desktop")
        try:
            subprocess.run(cmd, env=env, check=True, timeout=240, capture_output=True)
            j = json.load(open("/tmp/lh.json")); a = j["audits"]
            fails = [k for k, v in a.items() if v.get("score") is not None and v["score"] < 0.9 and v.get("scoreDisplayMode") in ("binary", "numeric", "metricSavings")]
            report[f"{label}:{form}:/{pg}"] = {
                **{c: round(j["categories"][c]["score"] * 100) for c in j["categories"]},
                "LCP_s": round(a["largest-contentful-paint"]["numericValue"] / 1000, 2),
                "CLS": round(a["cumulative-layout-shift"]["numericValue"], 3),
                "TBT_ms": round(a["total-blocking-time"]["numericValue"]),
                "FCP_s": round(a["first-contentful-paint"]["numericValue"] / 1000, 2),
                "bytes_kb": round(a["total-byte-weight"]["numericValue"] / 1024),
                "weak_audits": fails[:15]}
        except Exception as e:
            report[f"{label}:{form}:/{pg}"] = {"error": str(e)[:200]}
        print(form, url, report[f"{label}:{form}:/{pg}"], flush=True)
json.dump(report, open(out_path, "w"), indent=1)
