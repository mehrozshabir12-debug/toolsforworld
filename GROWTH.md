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

## Weekly routine (from 13 Oct 2026: traffic first, monetization second, new tools later)
Owner's rules: NO new tools, NO new pages unless approved below, no redesign, no paid services, keep every URL,
never change DNS/account settings, never open AdSense, never invent numbers (mark unavailable data).

1. **Measure** (read-only, only if a browser with Search Console is available): last 7 days vs previous 7 days —
   clicks, impressions, CTR, average position, top queries/pages; Pages report (indexed count, reasons not indexed).
   Cloudflare Web Analytics: visits and referrers. Write the numbers in the log below; unavailable = "n/a".
2. **Improve existing pages** from that data only: max 5 title/description rewrites a week (pages with impressions
   but CTR < 1%), and better examples/FAQs on pages ranking 8–30. No data yet → no wording changes.
3. **Test before live:** `python3 build.py`, push to branch `audit`, wait for "Deep audit" (results on `audit-results`:
   `report.json` and `audit_report.json` fully passing), then push the same commit to `main`; "Test all tools" must pass.
4. Log the week below (numbers + what changed and why). Report to the owner in Roman Urdu.

Approved page additions: compress image/PDF to 2 MB and 5 MB (done 13 Oct). Nothing else is approved.
Sitemap `lastmod` comes from `lastmod.json` (content hash per page); IndexNow sends only changed URLs.

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
- 2026-10-19 (content quality round 2): preset_content.py adds language-specific checks to 13 OCR pages and size-specific advice to 10 compress-image pages; within-family similarity mean ~0.68 → 0.59, max 0.83 → 0.72. Kept AdSense script on preset pages because it also delivers the EEA consent message. Audit 62/62.
- 2026-10-19 (AdSense "needs attention" email, likely low-value content): added core_content.py with unique uses/tips/troubleshooting/FAQs on 26 main tool pages (thinnest pages were 180–300 words, now 330–600), expanded Terms page. Audit 62/62. Next: owner checks exact reason in AdSense → Sites, then requests review.
- 2026-10-16 (Search Console, 28 days = 11–13 Oct data): 2 clicks, 38 impressions, CTR 5.3%, avg position 43.2, 21 queries, 34 pages. GA4: 0 (tag added 15 Oct, verified live). Changes (`query_boost.py`): 5 title/description rewrites (3000x3000, 1080x1920, 2560x1440, compress PDF to 1MB, remove background at pos 7.2 with 0 clicks); quick answers + FAQs matching real queries (600x600, 400x400, 1280x720, 1920x1080, 1080x1920, PDF 1MB/100KB, 10KB, passport measure, China visa crop, password length, KB check on compress presets); new guide image-resolution-sizes-explained (owner approved); marketing/directory-kit.md for SaaSHub/AlternativeTo/Product Hunt.
- 2026-10-13 (SEO): real sitemap dates, 404 noindex, IndexNow changed-only; wording from Google autocomplete (reduce image size in KB, resize photo to N KB, HEIC to JPEG, passport size & requirements); internal links; home exact-size row; +4 presets (image/PDF 2 MB, 5 MB) → 85 pages. Search Console/Cloudflare numbers: n/a (browser offline).
- 2026-10-13 (audit): fixed Word-to-PDF long docs (1 page → full), passport mobile overflow, compressor growing files, input validation, OCR crash; lazy-loaded libraries; search, recent/popular, related tools, progress, ZIP; content for thin/duplicate pages. Live mobile Lighthouse 54–78 → 97–100. Deep audit: `tests/audit.py` (push to branch `audit`, results on `audit-results`).
- 2026-10-13: 62 → 80 pages. Added 10 OCR languages, 6 resize sizes, character counter, discount calculator.
  Earlier the same day: compress-PDF-to-size pages, 7 passport/visa pages, more image sizes; sitemap resubmitted.
