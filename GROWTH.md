# Tools for World: weekly growth playbook

Goal: grow organic Google traffic to 1,000 views/day by month 6 and 10,000/day by month 12–24,
mainly through long-tail keyword pages that really work.

## How the site is built
- `tools_list.py` holds every page. `define()` = the 22 main tools. `landing()` = keyword pages that reuse a
  main tool with a `preset` (field values set on load) and `parent` (the main tool's slug).
- `python3 build.py` writes every page folder, `sitemap.xml`, `robots.txt` and `index.html` in place.
- Tool engines: `assets/files.js` (file tools; `TOOLS`, `renderOpts`, `OPTX`, `RUN`) and `assets/calc.js` (calculators).
- Tests: `tests/run_tests.py` runs in GitHub Actions on every push (`Test all tools`). The report goes to the
  `test-results` branch (`git fetch origin test-results:refs/remotes/origin/test-results && git show origin/test-results:report.json`).
- On push, GitHub Pages deploys and `Notify search engines (IndexNow)` pings Bing/Yandex.

## Weekly routine
1. **Check what's working** (only if a browser with Google Search Console is available):
   Search Console → Performance (last 28 days) for queries/pages with impressions, and Pages for indexing problems.
   Note the top queries in the log below. Build more pages around topics that get impressions.
2. **Add 10–20 pages** from the backlog below (or new ideas from step 1). Rules:
   - Each page must actually do what its title says. If a preset needs a new option or feature, add it to the tool.
   - Unique title, description, H1, lead, how-to steps and 1–3 FAQs. No copy-paste filler, no keyword stuffing.
   - Facts (sizes, limits, rules) must be correct. If unsure, leave it out and tell users to check the official source.
   - Never make near-duplicate pages (e.g. "compress jpg to 100kb" next to "compress image to 100kb").
3. `python3 build.py`, add tests for any new behaviour in `tests/run_tests.py` (and edge cases in `tests/audit.py`), then commit and push.
4. Wait for `Test all tools` to pass. If anything fails, fix it before finishing.
5. Mark done items `[x]` in the backlog, add a line to the log, commit and push.
6. Report to the owner in Roman Urdu: pages added, test result, Search Console numbers if available, next week's plan.

Never: touch `CNAME`, DNS or account settings; post on social media; pay for anything; delete pages that may be indexed
(if a page must go, redirect it instead).

## Keyword backlog
### Resize presets (parent `resize-image`)
- [x] 1080×1350 Instagram portrait · 851×315 Facebook cover · 1000×1500 Pinterest · 500×500 WhatsApp DP · 1024×1024 · 3000×3000 album cover
- [ ] 1280×1280 · 800×800 YouTube profile · 2048×2048 · 1600×900 · 800×600 · 640×480 · 300×300 · 512×512
- [ ] 1200×1200 Etsy/Shopify product · 2000×2000 Amazon product · 1920×1005 Facebook event cover · 1128×191 LinkedIn company cover

### Compress presets
- [ ] Image: 15KB, 40KB, 150KB, 300KB, 2MB (parent `compress-image`, preset `#tkb`)
- [ ] PDF: 50KB, 150KB, 2MB (parent `compress-pdf`, preset `#ptkb`)

### OCR languages (parent `image-to-text`, preset `#ol`; the option must exist in the `#ol` select)
- [x] Spanish, French, German, Portuguese, Italian, Russian, Turkish, Bengali, Indonesian, Chinese
- [ ] Japanese (jpn), Korean (kor), Persian (fas), Tamil (tam), Telugu (tel), Vietnamese (vie), Thai (tha), Polish (pol), Dutch (nld), Ukrainian (ukr)

### Passport and visa photos (parent `passport-photo-maker`, preset `#ps`; add sizes to the `#ps` select if needed)
- [ ] Verify each spec on the official government site before adding: Germany, France, Ireland, Philippines, Nigeria,
      Pakistan, Bangladesh, Malaysia (35×50), Japan visa, Saudi visa, UAE visa, US visa (same as US passport: use a different angle)

### Utility variants
- [x] Character counter, discount calculator
- [ ] Percentage increase calculator, percentage decrease calculator, GST/VAT calculator (add/remove tax %),
      tip calculator (needs new calc), "how many days until" date calculator (new calc), Instagram bio character counter
- [ ] QR presets: URL, email, phone, SMS, Google review link, Instagram profile, YouTube channel

### New tools (bigger wins; one per week at most, with tests)
- [ ] Rotate PDF · Add page numbers to PDF · Delete PDF pages · Reorder PDF pages · PDF to PNG
- [ ] Crop image · Rotate/flip image · Image to WebP · Add watermark to image · Blur faces
- [ ] JPG to PDF under X KB (img2pdf + target size) · Signature resizer (crop, white background, under 20KB)
- [ ] Unit converters (length, weight, temperature) · Case converter · Remove line breaks · Lorem ipsum

### Content
- [ ] Medium guides linking to the matching pages (owner approves each before publishing)

## Log
- 2026-10-13 (audit): fixed Word-to-PDF long docs (1 page → full), passport mobile overflow, compressor growing files, input validation, OCR crash; lazy-loaded libraries; search, recent/popular, related tools, progress, ZIP; content for thin/duplicate pages. Live mobile Lighthouse 54–78 → 97–100. Deep audit: `tests/audit.py` (push to branch `audit`, results on `audit-results`).
- 2026-10-13: 62 → 80 pages. Added 10 OCR languages, 6 resize sizes, character counter, discount calculator.
  Earlier the same day: compress-PDF-to-size pages, 7 passport/visa pages, more image sizes; sitemap resubmitted.
