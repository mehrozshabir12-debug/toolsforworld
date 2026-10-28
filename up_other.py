"""Unique content: resize-to-size and OCR language presets."""

P = {}

# ---------------- resize image to WxH ----------------
P["resize-image-to-1080x1920"] = ('''<h2>Turning a landscape photo into a 9:16 story</h2>
<p>Most photos are taken horizontally, but stories are tall. Cropping a landscape photo to 1080 × 1920 keeps only a narrow vertical strip of it, so choose the part with your subject before pressing Resize. If you'd rather keep the whole picture, pick Fit with white border: the photo sits in the middle with bands above and below, which you can cover with text or stickers in the app.</p>''',
[("Can I use 1080x1920 for a phone wallpaper?", "Yes. It fills most phone screens. Newer, taller phones may crop a little from the top and bottom.")])

P["resize-image-to-600x600"] = ('''<h2>Checking a 600 × 600 photo before upload</h2>
<p>Open the downloaded file and look at its details: on Windows right-click and choose Properties, then Details; on a Mac open it in Preview and choose Tools, Show Inspector. Both width and height should read 600. If the visa form complains about the head position rather than the size, go back to the <a href="../us-passport-photo/">US passport photo maker</a>, which lines the face up with the guides before saving.</p>
<h2>600 × 600 for the US visa form</h2>
<p>The DS-160 online visa form accepts square photos from 600 × 600 up to 1200 × 1200 pixels, and 600 × 600 is the smallest that passes, so it uploads fastest. The form also checks the file stays under 240 KB, which a 600 × 600 JPG almost always does.</p>
<p>The same square size is useful for marketplace and shop listings, where product photos are shown in square tiles, and for small square logos in email signatures and invoices.</p>''',
[("Is 600x600 the same as 2x2 inches?", "At 300 dpi, yes: 2 inches × 300 dots per inch = 600 pixels on each side.")])

P["resize-image-to-1920x1080"] = ('''<h2>Wallpapers, slides and video thumbnails</h2>
<p>1920 × 1080 is Full HD, the 16:9 shape of most laptop screens, TVs and presentation slides in PowerPoint and Google Slides. Using images at exactly this size means they fill the screen with no black bars or stretching.</p>
<p>Phone photos are 4:3, a little taller than 16:9, so Crop to fill trims a strip from the top and bottom. For screenshots or slides you'd rather not cut, use Fit with white border instead. For a 4K screen, 3840 × 2160 is the same shape at double the size: type it in the boxes.</p>''',
[("Is 1920x1080 the same as 1080p?", "Yes. 1080p means 1080 pixels tall, and the matching width for a 16:9 screen is 1920.")])

P["resize-image-to-1500x500"] = ('''<h2>Designing a 3:1 header that survives cropping</h2>
<p>An X (Twitter) header is very wide: three times wider than it is tall. On phones the bottom-left corner is covered by your profile picture, and the edges can be trimmed on some screens, so keep text and faces in the central area and away from the lower left.</p>
<p>A group photo or landscape works better than a portrait. If your image has text, check the result on both a phone and a computer after uploading, because each shows a slightly different part.</p>''',
[("Can I use 1500x500 for other sites?", "It works for some blogs and newsletter headers too. LinkedIn banners use 1584 × 396, which is even wider: type it in the size boxes.")])

P["resize-image-to-500x500"] = ('''<h2>Profile pictures shown in a circle</h2>
<p>WhatsApp, Telegram and most apps show your profile photo as a circle, so the corners of the 500 × 500 square are hidden. Centre your face and leave a little space around your head, or the top of your hair and your chin may be cut off in the circle.</p>
<p>500 × 500 is large enough to stay sharp when someone opens your photo full size, yet small enough to upload quickly. It's also a common size for forum avatars, Discord servers and small square product thumbnails.</p>''',
[("Why does WhatsApp crop my DP?", "WhatsApp shows the photo as a circle and asks you to crop to a square. A square 500 × 500 photo with your face centred avoids losing parts of it.")])

P["resize-image-to-1024x1024"] = ('''<h2>App icons and AI image inputs</h2>
<p>Apple asks for a 1024 × 1024 pixel app icon for the App Store, and many icon generators start from that size to make every smaller one. Keep the important part of the icon within the centre, because platforms round the corners or mask the icon into a circle or squircle.</p>
<p>Many AI image tools also work in 1024 × 1024 squares, so resizing a reference photo to this size first avoids the tool cropping it in a way you didn't choose. For square logos, use a PNG with a plain background so edges stay sharp.</p>''',
[("Should a 1024x1024 icon have transparent corners?", "For the App Store, no: the icon should be a full square without transparency, and Apple rounds the corners itself."),
 ("Is 1024x1024 1:1?", "Yes. It's a square, the same 1:1 shape as 500 × 500 or 3000 × 3000.")])

P["resize-image-to-3000x3000"] = ('''<h2>Cover art for music and podcasts</h2>
<p>Music distributors generally ask for square cover art of 3000 × 3000 pixels, and Apple Podcasts accepts square artwork between 1400 × 1400 and 3000 × 3000. Starting at 3000 × 3000 means your cover looks sharp on large TV apps and still works when the platform makes smaller copies.</p>
<p>Avoid making a small image bigger: if your artwork is 800 pixels wide, resizing it to 3000 adds pixels without adding detail, and it will look soft. Design or export the artwork at 3000 × 3000 from the start, and keep text large enough to read when the cover is shown as a small thumbnail.</p>''',
[("JPG or PNG for album covers?", "Most distributors accept both. JPG is smaller and widely accepted; PNG is better for artwork with flat colours and text.")])

# ---------------- OCR language pages ----------------
P["image-to-text-urdu"] = ('''<h2>Urdu from WhatsApp images, books and newspapers</h2>
<p>Much of the Urdu text people want to copy arrives as images: poetry shared on WhatsApp and Facebook, newspaper cuttings, and pages of books. Clear, large screenshots of digital text give the best results. For a book page, lay it flat in daylight and photograph it straight on; curved pages near the spine are the hardest part to read.</p>''',
[("Can it read handwritten Urdu?", "Not reliably. It's built for printed and on-screen text; handwriting gives many mistakes.")])

P["image-to-text-arabic"] = ('''<h2>Persian and Pashto text</h2>
<p>Persian uses the Arabic alphabet plus four extra letters (پ چ ژ گ), and Pashto adds several more. The Arabic model may misread or skip these letters, so Persian and Pashto results need careful checking, especially in names. Urdu text has its own page with a model built for its letters.</p>
<h2>Arabic from documents, signs and screenshots</h2>
<p>Common uses are copying text from scanned contracts, government letters, receipts from Gulf countries, and Quranic or religious texts shared as images. Text with full diacritics (tashkeel) is harder to read accurately than everyday text without them, so check the vowel marks carefully if they matter to you.</p>''',
[("Does it keep right-to-left order?", "Yes. The result is Unicode Arabic, which shows right to left in any app that supports Arabic.")])

P["image-to-text-hindi"] = ('''<h2>Hindi from notices, forms and textbooks</h2>
<p>People use Hindi OCR for school textbooks, government notices and circulars, news screenshots and old typed documents. Text that mixes Hindi and English, such as forms with English labels, mostly comes out correctly, but check English words, which the Hindi model may read as Devanagari.</p>''',
[("Can it read Marathi or Nepali?", "Both use Devanagari, so much of the text is read correctly, but some letters and words specific to those languages may need fixing.")])

P["image-to-text-french"] = ('''<h2>French from course notes, letters and menus</h2>
<p>Students copy French from textbooks and slides, travellers from menus and signs, and people abroad from official letters from banks or the préfecture. Check numbers and dates in letters: French writes 1 234,56 with a space and a comma, and OCR may join the parts differently.</p>''',
[("Does it work for Canadian French?", "Yes. Quebec French uses the same alphabet and accents, so the same model reads it well.")])

P["image-to-text-german"] = ('''<h2>Umlauts, ß and copying into forms</h2>
<p>If you paste the result into a website that doesn't accept umlauts, such as some airline or booking forms, the usual replacements are ae for ä, oe for ö, ue for ü and ss for ß. Names on official documents should follow the spelling in the passport, which may already use these replacements.</p>
<h2>German from official letters and old documents</h2>
<p>A common use is copying text from letters from German authorities, insurers and landlords, so it can be pasted into a translator. Old documents printed in Fraktur (blackletter) type, common before the 1940s, are not read well by this model; it's built for modern Latin type.</p>''',
[("Can I translate the text after OCR?", "Yes. Copy the result into any translator; because it's real text, the translation is much better than with a photo.")])

P["image-to-text-russian"] = ('''<h2>Transliterating names after OCR</h2>
<p>Names copied from Russian documents often need to be written in Latin letters for forms abroad. Passports issued in Russia use a fixed transliteration system, so a name such as Юлия becomes Iuliia rather than Yulia. Copy the name exactly as it appears in the Latin line of the passport instead of transliterating it yourself.</p>
<h2>Russian from screenshots, scans and signs</h2>
<p>Russian OCR is used for copying text from scanned books and articles, screenshots of messages, product labels and documents for translation. Italic Cyrillic is harder to read because some italic letters look like Latin ones (italic т looks like m), so check italic passages more carefully.</p>''',
[("Can I search the text after extracting it?", "Yes. The result is normal Unicode Cyrillic, so you can search, edit and translate it.")])

P["image-to-text-indonesian"] = ('''<h2>Old and new spelling</h2>
<p>Documents from before 1972 use the old spelling, with dj, tj and oe where today's Indonesian writes j, c and u (Djakarta, Soekarno). The model copies the letters exactly as printed and doesn't modernise them, which is what you want for names, but you may want to update other words yourself.</p>
<h2>Indonesian from documents and screenshots</h2>
<p>Typical uses include copying text from KTP-style forms, letters from offices, school materials and screenshots of WhatsApp messages. Addresses with abbreviations and numbers, such as "Jl. Sudirman No. 12, RT 03/RW 05", are worth checking digit by digit.</p>''',
[("Does it work for Malay?", "Yes. Malay uses the same Latin letters and similar spelling, so the model reads it well.")])

P["image-to-text-chinese"] = ('''<h2>Mixed Chinese and English text</h2>
<p>Product labels, business cards and menus often mix Chinese with English words, brand names and numbers. The Chinese model reads the Latin letters too, but spacing around them can come out uneven, and look-alike pairs such as O and 0 or l and 1 are worth checking in phone numbers and model codes.</p>
<h2>Chinese from screenshots, menus and documents</h2>
<p>People use Chinese OCR to copy text from WeChat screenshots, product packaging, menus and documents so they can translate or search it. Small characters are where errors happen, because many characters differ by a single stroke. Zoom in or crop to the text before running OCR to give each character more pixels.</p>''',
[("Can I copy the text into a translator?", "Yes. The result is Unicode Simplified Chinese, which any translator or search engine accepts.")])
