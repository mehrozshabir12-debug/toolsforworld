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
Owner's rules: NO new tools, NO new pages unless approved below, no redesign, no paid services, keep every URL (exception: the 15 pages in `retire.py`, folded into their main tool with owner approval on 28 Oct),
never change DNS/account settings, never open AdSense, never invent numbers (mark unavailable data).

1. **Measure** (read-only, only if a browser with Search Console is available): last 7 days vs previous 7 days —
   clicks, impressions, CTR, average position, top queries/pages; Pages report (indexed count, reasons not indexed).
   Cloudflare Web Analytics: visits and referrers. Write the numbers in the log below; unavailable = "n/a".
2. **Improve existing pages** from that data only: max 5 title/description rewrites a week (pages with impressions
   but CTR < 1%), and better examples/FAQs on pages ranking 8–30. No data yet → no wording changes.
3. **Test before live:** `python3 build.py`, push to branch `audit`, wait for "Deep audit" (results on `audit-results`:
   `report.json` and `audit_report.json` fully passing), then push the same commit to `main`; "Test all tools" must pass.
4. Log the week below (numbers + what changed and why). Report to the owner in Roman Urdu.

Approved page additions: compress image/PDF to 2 MB and 5 MB (done 13 Oct). On 22 Oct the owner gave a free hand for growth ("kro jo tmri mrzi"): JPG to PDF max-size option + under 100/200/500 KB pages and the file-size-limits guide added under that approval.
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
- 2026-10-29 (owner: "green walon ko target kro sab jaga", high-volume + low-difficulty keywords, OpenSEO US 29 Oct): 5 new main tools, each with own content, 5-6 FAQs and tests: png-to-pdf (90.5K/mo, KD 12; img2pdf engine, PNGs embedded losslessly), pdf-to-png (74K, KD 15; new pdf2png engine with optional transparent background), webp-to-png (165K, KD 27; keeps alpha), date-calculator (673K, KD 31; new calc: days between dates incl. weekdays, add/subtract days/weeks/months/years/business days), video-to-mp3 (110K, KD 18; same engine as mp4-to-mp3, page covers MOV/WebM/MKV/3GP). Max 3-gram Jaccard vs sibling pages 0.15. PNG to JPG / JPG to PNG titles now "Convert PNG to JPG Free" / "Convert JPG to PNG Free". Cross-links added between sibling converters and age/date calculators; home tiles + related tools. Skipped on purpose: youtube to mp3 (1.8M, copyright/AdSense risk) and KD 50+ heads (pdf to word, compress pdf, qr code, background remover) until DR grows. New OpenSEO US weekly mobile rank tracker (73 keywords, depth 100). Regression 38/38, deep audit 72/72. 82 -> 87 pages.
- 2026-10-28 (AdSense still "account wasn't approved"; its help page says no ad code on auto-generated pages): the 43 template pages (compress-image-to-*, compress-pdf-to-*, resize-image-to-*, image-to-text-*, jpg-to-pdf-under-*, passport/visa country pages) no longer load adsbygoogle.js; they keep the google-adsense-account meta tag. Main tools, guides, home and info pages keep the ad script (39 pages). On no-ad pages GA4 sets consent mode default "denied" for the EEA, UK and Switzerland, because Google's consent message comes with the ad script. Put the ad code back on these pages only after approval (build.py `is_template`). Owner told not to press Resubmit until the content changes have been crawled (~2 weeks).
- 2026-10-28 (AdSense rejected again 26 Oct, second "needs attention" after 18 Oct; owner approved folding thin pages, "han kro sahi ha"): new `retire.py` folds 15 preset pages into their main tool: 5 OCR languages (Spanish, Turkish, Portuguese, Italian, Bengali), 9 resize sizes (400x400, 1080x1080, 1280x720, 1000x1500, 2560x1440, 1080x1350, 1200x630, 851x315, 1584x396) and WhatsApp QR. Rule: ~10-20 searches/month (OpenSEO US + India + Pakistan, 28 Oct) AND Search Console average position worse than ~25. Kept on purpose: Urdu OCR (~540/month Pakistan, KD 0-6), Wi-Fi QR (2,900/month US), French/Russian/Indonesian/German OCR and 1080x1920/1500x500 (positions 6-22). Old folders are redirect pages (meta refresh 0 + canonical + noindex) to the main tool with `#p=<slug>`, which applies the preset; main tools show them as one-click buttons; internal links rewritten at build time. 97 -> 82 pages. Tests updated to kept slugs. Redirected URLs submitted to IndexNow by hand (the workflow only sends new sitemap lines).
- 2026-10-24 (page 1 without backlinks, owner approved "dono karo"): SERP check showed weak page-1 results for "pakistan passport photo size" (YouTube x2, sites 3-7 days old; our passport guide already at 16), "passport size photo size in cm" India (Quora, Pinterest, Facebook) and "whatsapp dp size". New page pakistan-passport-photo (passport tool preset 29.63x39.54 mm = exactly 350x467 px at 300 dpi; facts only from DGI&P online-passport page: colour, white, JPG, max 3 MB; Urdu summary line; 2 FAQs; max 3-gram Jaccard vs other passport pages 0.42). Passport guide Pakistan row/steps now link it. Home page got a visible "Popular exact sizes" block linking the 10 pages closest to page one (previously only inside the collapsed "All sizes" list). 97 pages.
- 2026-10-23 (competitor gaps, OpenSEO India, top 100 ranked keywords of imgsmaller.com, pdf4me.com, 123passportphoto.com): weakest SERPs are "passport size photo size in cm / inches / in india" (KD 0-2, top results avg ~4 referring domains, 123passportphoto at 11-29 via query-string URLs), "whatsapp dp size" (KD 0, imgsmaller 37-54), "compress image to 20kb / 15kb / 30kb photo size" (KD 0, avg RD < 1, imgsmaller 18-28; our pages already answer these). Big brands (iLovePDF, Smallpdf, Adobe, PDF24) are absent from the exact-size top 10 ("compress pdf to 200kb"). Changes: India passport page got a cm/mm/inch/pixel table + 2 FAQs; 500x500 page got a WhatsApp DP size section + FAQ; passport 'a Australia/India' grammar fixed; compress-PDF leads say "Reduce PDF size to under X"; image-to-text lead uses "extract text from an image". Not done (needs new pages, owner said no new pages for now): PAN card photo (KD 0, avg RD ~0.1), crop PDF, PPT to PDF.
- 2026-10-23 (titles + rank tracking): OpenSEO audit flagged 9 titles at 61-63 chars, build found 6 more; all 96 titles now <= 60 (fit_title drops brand above 60, resize presets pick longest wording that fits, passport/visa fall back to "... Requirements"; remove-background and 3000x3000 trimmed, keywords kept). Audit 64/64. OpenSEO: backlinks 36 from 4 domains (nav-ai.net 28, firstsited.com 6), rank 0. New India mobile rank tracker (depth 100, manual) with 20 keywords for existing pages; first check run 23 Oct.
- 2026-10-23 (authority): Ahrefs free checker: DR 0, 2 backlinks from 2 sites (stackscope.dev DR 28 and firstsited.com DR 0, both launch-day lists from 14 Oct). SaaSHub listing not yet in Ahrefs' index.
- 2026-10-23 (Search Console check): Pages report 78 indexed (was 35 on 22 Oct), 11 not indexed: 8 'Discovered, not indexed' (new pages), 3 redirects, 0 'Crawled, not indexed' (was 35). Daily Oct 14-20: impressions 128 -> 208, avg position 53.5 -> 47.4. Last 24 h (22 Oct): 175 impressions, 0 clicks, avg position 41.1.
- 2026-10-22 (positions, striking distance from Search Console 28 days): resize-image-to-1080x1920 got an at-a-glance table (shape, MP, print size, uses) and links to 1920x1080/1080x1080; resize-image-to-1500x500 got a banner-size comparison and how to make 500x1500 / 1500x400 (queries '500 x 1550' pos 6, '1550 x 500' pos 11); 13 OCR language pages got one line in their own language (lang/dir set), for native searches like 'image to text türkçe'; image-resolution guide got a quick-answers table and FAQs for '1080p photo size', '1080p portrait/square', 'hd pixel size', '4k square size' (pos 5-11).
- 2026-10-22 (owner: free hand for growth): JPG to PDF got a Max PDF size option (any KB limit; sharpest level that fits, binary search) plus 3 pages jpg-to-pdf-under-100kb/200kb/500kb, each with its own example, tips and FAQ (max Jaccard with siblings now < 0.6). New guide file-size-limits-kb-mb-explained. Audit 64/64 (48 MP photo -> 91 KB under 100 KB; 3 photos -> 164 KB under 200 KB), tests 33/33. 96 pages. AdSense: site review in progress since 20 Oct, all steps done, Policy center shows no issues, ads.txt live and correct (AdSense shows 'Not found' until it re-crawls). Do not re-request review while it is pending.
- 2026-10-22 (long-tail, from Google autocomplete + Search Console): 17 compress-to-size pages got FAQs answering “below / less than / up to X” and “without losing quality” (PDF pages) in their own size; no-upload FAQs on compress-pdf, compress-image and jpg-to-pdf (matches “compress pdf without uploading”); JPG to PDF links to the PDF size-limit pages for “jpg to pdf under 200kb” searches. No new pages, no title changes. Audit 62/62, tests 32/32. Strongest new-page demand seen in autocomplete (needs owner approval): compress PDF to 150KB, compress image to 150KB/15KB/250KB, JPG/image to PDF under X KB (new tool), signature resize (new tool), increase image size in KB (new tool).
- 2026-10-22 (10-point SEO audit, Search Console 28 days to 19 Oct: 8 clicks, ~1.03K impressions, avg position 53): all 92 sitemap URLs return 200 with no redirect chains; http/www/no-slash redirect to https canonical in one hop; 404 returns 404; robots.txt and sitemap fine (sitemap read 21 Oct, 92 discovered); canonicals, schema JSON, internal links (0 broken, 0 orphans, weakest page has 3 inbound links) and duplicate content (no pair above 0.6 Jaccard) all clean. Indexing: 35 indexed, 35 'crawled, not indexed' (all crawled 13–14 Oct, before the 19 Oct content upgrade; validation started 19 Oct). Core Web Vitals: no field data yet; live page loads in ~1 s, gzip on; Lighthouse 95–100 perf. Changes: 4 guide titles shortened to 51–62 chars (were 75–92, cut off in Google); homepage logo link was empty, now ./. Main limit is authority: most queries rank 40–90, so backlinks matter more than on-page changes now.
- 2026-10-19 (content quality round 2): preset_content.py adds language-specific checks to 13 OCR pages and size-specific advice to 10 compress-image pages; within-family similarity mean ~0.68 → 0.59, max 0.83 → 0.72. Kept AdSense script on preset pages because it also delivers the EEA consent message. Audit 62/62.
- 2026-10-19 (AdSense "needs attention" email, likely low-value content): added core_content.py with unique uses/tips/troubleshooting/FAQs on 26 main tool pages (thinnest pages were 180–300 words, now 330–600), expanded Terms page. Audit 62/62. Next: owner checks exact reason in AdSense → Sites, then requests review.
- 2026-10-16 (Search Console, 28 days = 11–13 Oct data): 2 clicks, 38 impressions, CTR 5.3%, avg position 43.2, 21 queries, 34 pages. GA4: 0 (tag added 15 Oct, verified live). Changes (`query_boost.py`): 5 title/description rewrites (3000x3000, 1080x1920, 2560x1440, compress PDF to 1MB, remove background at pos 7.2 with 0 clicks); quick answers + FAQs matching real queries (600x600, 400x400, 1280x720, 1920x1080, 1080x1920, PDF 1MB/100KB, 10KB, passport measure, China visa crop, password length, KB check on compress presets); new guide image-resolution-sizes-explained (owner approved); marketing/directory-kit.md for SaaSHub/AlternativeTo/Product Hunt.
- 2026-10-13 (SEO): real sitemap dates, 404 noindex, IndexNow changed-only; wording from Google autocomplete (reduce image size in KB, resize photo to N KB, HEIC to JPEG, passport size & requirements); internal links; home exact-size row; +4 presets (image/PDF 2 MB, 5 MB) → 85 pages. Search Console/Cloudflare numbers: n/a (browser offline).
- 2026-10-13 (audit): fixed Word-to-PDF long docs (1 page → full), passport mobile overflow, compressor growing files, input validation, OCR crash; lazy-loaded libraries; search, recent/popular, related tools, progress, ZIP; content for thin/duplicate pages. Live mobile Lighthouse 54–78 → 97–100. Deep audit: `tests/audit.py` (push to branch `audit`, results on `audit-results`).
- 2026-10-13: 62 → 80 pages. Added 10 OCR languages, 6 resize sizes, character counter, discount calculator.
  Earlier the same day: compress-PDF-to-size pages, 7 passport/visa pages, more image sizes; sitemap resubmitted.

## 2026-10-25 – CTR: custom-size wording on all 16 resize pages
- GSC (28 d): resize pages show for many odd sizes people type ("3000 x 400", "700*500", "600*125", "500 x 1550") at positions 2–12, but 0 clicks: the snippet only says the preset size.
- Change: meta descriptions + lead + 1 FAQ on every resize-image-to-* page now say any custom width/height works (descriptions only, titles unchanged).
- Check on 8 Nov: CTR of resize-image-to-* pages vs. 28 days before.
