# Tool definitions for build.py (international tools). Each tool = one page.
HEIC = '<script src="https://cdn.jsdelivr.net/npm/heic2any@0.0.4/dist/heic2any.min.js" integrity="sha384-OTofQ0MEeiSgh62havBcemCIK0gqj809wX6UA0uPISNMRnR6NZyCdGzX3SbLrgwL" crossorigin="anonymous"></script>'
TESS = '<script src="https://cdn.jsdelivr.net/npm/tesseract.js@5.1.0/dist/tesseract.min.js" integrity="sha384-1zP4ZOtlk2FXAOiUArpMuWf7INJJKe/ROfYFAVSeUa11DEfXdKWGiPI3dVma2Gt0" crossorigin="anonymous"></script>'
LAME = '<script src="https://cdn.jsdelivr.net/npm/lamejs@1.2.1/lame.min.js" integrity="sha384-xuasJXVcyv3hZq0eYpelEkBC8l4yufatZXDsKuyCU2rqfhDCb+ftuE/mSfZAteiK" crossorigin="anonymous"></script>'
JSZIP = '<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js" integrity="sha384-+mbV2IY1Zk/X1p/nWllGySJSUN8uMs+gUAN10Or95UBH0fpj6GfKgPmgC5EXieXG" crossorigin="anonymous"></script>'
QRLIB = '<script src="https://cdn.jsdelivr.net/npm/qrcode-generator@1.4.4/qrcode.js" integrity="sha384-8FWZA6BGMXhsfO+BLtrJK0We6gg5o1JyO8xQm6peWDEUs17ACA5ziE/NIAkl9z2k" crossorigin="anonymous"></script>'


def define(tool, F, N, SEL, RESULT, PDFLIB, PDFJS, MAMMOTH, H2PDF):
    # ================= PDF & documents =================
    tool(slug="pdf-to-word", group="pdf", icon="word", name="PDF to Word", ftool="pdf2word", libs=PDFJS + JSZIP,
         card="Turn a PDF into an editable Word file.",
         title="PDF to Word Converter – Free, No Upload | Tools for World",
         desc="Convert PDF to an editable Word document (.docx) for free. Runs in your browser, so your file is never uploaded. No sign-up, no watermark.",
         h1="PDF to Word converter", lead="Turn the text of a PDF into an editable Word document. Your file is processed on your device and never uploaded.",
         body='''<h2>How to convert PDF to Word</h2><ol><li>Choose a PDF file.</li><li>Press <b>Convert to Word</b>.</li><li>Download the .docx file and open it in Word, Google Docs or LibreOffice.</li></ol>
<h2>What gets converted</h2><p>The text of every page, in reading order, with paragraphs and headings. Each PDF page starts on a new page in Word. Pictures, tables, columns and exact fonts are not copied, so check the layout after converting.</p>
<p>A scanned PDF is just pictures of pages, with no real text inside. Use <a href="../image-to-text/">Image to Text (OCR)</a> to read it.</p>''',
         faq=[("Is it really free?", "Yes. There is no limit, sign-up or watermark."),
              ("Is my PDF uploaded to a server?", "No. The conversion runs inside your browser, so the file never leaves your device."),
              ("Why is my Word file empty?", "The PDF is probably a scan. Scans contain images, not text; run them through OCR first.")])

    tool(slug="word-to-pdf", group="pdf", icon="word", name="Word to PDF", ftool="word2pdf", libs=MAMMOTH + H2PDF,
         card="Turn a .docx document into a PDF.",
         title="Word to PDF Converter – DOCX to PDF Free | Tools for World",
         desc="Convert Word documents (.docx) to PDF for free in your browser. No upload and no sign-up. Ideal for CVs, letters and assignments.",
         h1="Word to PDF converter", lead="Convert a Word document (.docx) to PDF without uploading it. Ideal for CVs, cover letters, forms and assignments.",
         extra='<div id="doc-preview" hidden></div><p><button class="btn ghost" id="printbtn" hidden onclick="const w=window.open(\'\');w.document.write(\'<html><head><title>Print</title><style>body{font:15px/1.5 Georgia,serif;margin:20mm}img{max-width:100%}table{border-collapse:collapse}td,th{border:1px solid #999;padding:4px 6px}</style></head><body>\'+document.getElementById(\'doc-preview\').innerHTML+\'</body></html>\');w.document.close();w.focus();w.print()">Print / Save as PDF (selectable text)</button></p>',
         body='''<h2>How to convert Word to PDF</h2><ol><li>Choose your .docx file.</li><li>Pick the page size and orientation.</li><li>Press <b>Convert to PDF</b> and download it.</li></ol>
<div class="warnbox">Text, headings, lists, pictures and simple tables convert well. Complex layouts (columns, text boxes, headers and footers, special fonts) may look different from Word. For those, use Word's File → Save As → PDF.</div>
<p>Want text you can select and search in the PDF? After converting, use “Print / Save as PDF” and choose “Save as PDF” as the printer.</p>''',
         faq=[("Does it work with .doc files?", "Only .docx. Open an old .doc in Word or Google Docs and save it as .docx first."),
              ("Is my document uploaded?", "No, it never leaves your device.")])

    tool(slug="compress-pdf", group="pdf", icon="pdf", name="PDF Compressor", ftool="pdfcompress", libs=PDFLIB + PDFJS,
         card="Make large PDFs smaller.",
         title="Compress PDF – Reduce PDF File Size Free | Tools for World",
         desc="Compress PDF files online for free. Shrink scanned PDFs and PDFs with photos for email and upload limits. No upload, works in your browser.",
         h1="Compress PDF", lead="Shrink large PDFs, especially scans and documents full of photos, so they fit email and upload limits.",
         body='''<h2>How to compress a PDF</h2><ol><li>Choose a PDF.</li><li>Pick a level: <b>Strong</b> suits most scans, <b>Light</b> keeps more detail.</li><li>Press <b>Compress PDF</b> and download the smaller file.</li></ol>
<h2>Good to know</h2><p>Each page is re-saved as a compressed image. That is why scanned PDFs often get 60–90% smaller. Text in the result can no longer be selected or searched. If your PDF is mostly typed text, it is probably already small.</p>''',
         faq=[("How much smaller will my PDF get?", "Scanned and photo-heavy PDFs usually shrink by 50–90%. Text-only PDFs may not shrink."),
              ("Is there a file size limit?", "No fixed limit. Very large PDFs (hundreds of pages) can be slow on phones.")])

    tool(slug="merge-pdf", group="pdf", icon="pdf", name="Merge PDF", ftool="merge", libs=PDFLIB,
         card="Join several PDFs into one file.",
         title="Merge PDF – Combine PDF Files Free Online | Tools for World",
         desc="Merge PDF files into one document in the order you choose. Free, private, no upload and no watermark.",
         h1="Merge PDF", lead="Combine several PDF files into one, in the order you choose. Use the arrows to reorder.",
         body='''<h2>How to merge PDF files</h2><ol><li>Choose two or more PDFs.</li><li>Put them in order with the ▲ ▼ arrows.</li><li>Press <b>Merge PDFs</b> and download the combined file.</li></ol><p>Bookmarks and form fields are not kept; pages, text and images are.</p>''',
         faq=[("Can I merge password-protected PDFs?", "No. Remove the password first in a PDF reader."), ("Is there a limit on how many PDFs?", "No fixed limit.")])

    tool(slug="split-pdf", group="pdf", icon="pdf", name="PDF Splitter", ftool="split", libs=PDFLIB,
         card="Extract pages or split every page.",
         title="Split PDF – Extract Pages from a PDF Free | Tools for World",
         desc="Split a PDF or extract the pages you need, like 1-3 and 5. Or split every page into its own file. Free and private.",
         h1="Split PDF", lead="Extract the pages you need, like 1-3, 5, or split every page into its own PDF.",
         body='''<h2>How to split a PDF</h2><ol><li>Choose a PDF.</li><li>Type the pages to keep, for example <code>1-3, 5, 8-10</code>, or choose “every page”.</li><li>Press <b>Split PDF</b>.</li></ol>''',
         faq=[("Does splitting lower the quality?", "No. Pages are copied exactly as they are.")])

    tool(slug="jpg-to-pdf", group="pdf", icon="pdf", name="JPG to PDF", ftool="img2pdf", libs=PDFLIB,
         card="Turn photos or scans into one PDF.",
         title="JPG to PDF Converter – Images to PDF Free | Tools for World",
         desc="Convert JPG, PNG and WebP images to one PDF. Reorder pages and choose A4 or Letter. Free, private, works on phones.",
         h1="JPG to PDF converter", lead="Combine photos or scanned pages into a single PDF. Use the arrows to change the page order.",
         body='''<h2>How to convert JPG to PDF</h2><ol><li>Choose one or more images.</li><li>Reorder them and pick a page size.</li><li>Press <b>Create PDF</b>.</li></ol><p>Great for receipts, ID copies, homework photos and scanned documents.</p>''',
         faq=[("Can I add PNG files too?", "Yes, JPG, PNG and WebP all work.")])

    tool(slug="pdf-to-jpg", group="pdf", icon="pdf", name="PDF to JPG", ftool="pdf2jpg", libs=PDFJS,
         card="Save every PDF page as an image.",
         title="PDF to JPG – Convert PDF Pages to Images Free | Tools for World",
         desc="Convert each page of a PDF into a high-quality JPG image. Free, no upload.",
         h1="PDF to JPG converter", lead="Convert each page of a PDF into a high-quality JPG image.",
         body='''<h2>How to convert PDF to JPG</h2><ol><li>Choose a PDF.</li><li>Pick the quality.</li><li>Press <b>Convert to JPG</b> and save the pages you need.</li></ol>''', faq=[])

    tool(slug="image-to-text", group="pdf", icon="text", name="Image to Text (OCR)", ftool="ocr", libs=TESS,
         card="Copy text from a photo or screenshot.",
         title="Image to Text Converter (OCR) – Extract Text from Images Free | Tools for World",
         desc="Extract text from images, photos and screenshots with free OCR. Supports English, Spanish, French, German, Arabic, Hindi, Chinese and more. Runs in your browser.",
         h1="Image to text (OCR)", lead="Pull the text out of a photo, scan or screenshot so you can copy and edit it.",
         body='''<h2>How to extract text from an image</h2><ol><li>Choose a photo or screenshot.</li><li>Pick the language of the text.</li><li>Press <b>Extract text</b>, then copy it or download a .txt file.</li></ol>
<h2>Tips for better results</h2><ul><li>Use a sharp, well-lit photo taken straight on.</li><li>Crop away everything except the text.</li><li>Printed text works much better than handwriting.</li></ul>''',
         faq=[("Which languages are supported?", "English, Spanish, French, German, Portuguese, Italian, Russian, Turkish, Arabic, Urdu, Hindi, Bengali, Indonesian and Simplified Chinese."),
              ("Can it read handwriting?", "Clear handwriting sometimes works, but OCR is built for printed text.")])

    # ================= Image =================
    tool(slug="compress-image", group="img", icon="img", name="Image Compressor", ftool="compress", libs="",
         card="Make JPG, PNG or WebP photos smaller in KB.",
         title="Reduce Image Size in KB – Free Image Compressor (JPG, PNG)",
         desc="Reduce image size in KB online for free: compress JPG, PNG and WebP photos for forms, email and websites, or set an exact target like 100 KB. No upload.",
         h1="Image compressor: reduce image size in KB", lead="Reduce photo file size for online forms, email and websites. Lower quality gives a smaller file.",
         body='''<h2>How to compress an image</h2><ol><li>Choose one or more photos.</li><li>Set the quality (70% keeps photos sharp for most uses).</li><li>Press <b>Compress</b> and save each smaller file.</li></ol><p>Need a photo under a fixed size for an application form? Type it in <b>Target size</b>, or open a ready preset: <a href="../compress-image-to-20kb/">20 KB</a>, <a href="../compress-image-to-50kb/">50 KB</a>, <a href="../compress-image-to-100kb/">100 KB</a>, <a href="../compress-image-to-200kb/">200 KB</a>, <a href="../compress-image-to-1mb/">1 MB</a>.</p>
<p>Need exact pixel dimensions instead (like 1080 × 1080)? Use the <a href="../resize-image/">Image Resizer</a>.</p>''',
         faq=[("Are my photos uploaded?", "No. Compression happens inside your browser.")])

    tool(slug="resize-image", group="img", icon="img", name="Image Resizer", ftool="resize", libs="",
         card="Change width and height in pixels or percent.",
         title="Image Resizer – Resize Photos in Pixels Free | Tools for World",
         desc="Resize images to any width and height in pixels or by percent while keeping the aspect ratio. Free and private.",
         h1="Image resizer", lead="Set an exact size in pixels or scale by percent. Keep the ratio so photos do not stretch.",
         body='''<h2>How to resize an image</h2><ol><li>Choose one or more images.</li><li>Enter a width or height, or a percentage.</li><li>Press <b>Resize</b>.</li></ol><p>Common sizes: 1080 × 1080 for Instagram posts, 1200 × 630 for link previews, 1920 × 1080 for HD.</p>
<h2>Need a size in KB, not pixels?</h2><p>Forms that say “resize image to 20 KB” mean the file size. That's a job for the compressor: <a href="../compress-image-to-20kb/">20 KB</a>, <a href="../compress-image-to-50kb/">50 KB</a>, <a href="../compress-image-to-100kb/">100 KB</a> or <a href="../compress-image/">any size you type</a>.</p>''',
         faq=[("How do I resize an image to 20 KB or 100 KB?", "KB is file size, not width and height. Use Compress Image to 20 KB or 100 KB: it lowers the file size and only shrinks the pixels if it has to."),
              ("Will resizing make my photo blurry?", "Making a photo smaller keeps it sharp. Making it much larger than the original can look soft, because no new detail is added.")])

    tool(slug="remove-background", group="img", icon="img", name="Background Remover", ftool="bgremove", libs="",
         card="Cut out the background of a photo.",
         title="Background Remover – Remove Image Background Free | Tools for World",
         desc="Remove the background from photos automatically with AI, for free. Get a transparent PNG. Runs in your browser, no upload.",
         h1="Background remover", lead="Remove the background from a photo automatically and download a transparent PNG.",
         body='''<h2>How to remove a background</h2><ol><li>Choose a photo.</li><li>Press <b>Remove background</b>. The first time, the AI model downloads once.</li><li>Download the transparent PNG.</li></ol>
<p>Works best when the subject (a person, product or pet) stands out clearly from the background. Use the PNG for profile pictures, product photos and designs.</p>''',
         faq=[("Is it free with no limits?", "Yes. The AI runs on your own device, so there are no credits or limits."),
              ("Why is the first run slow?", "The AI model downloads the first time (tens of MB). After that, your browser keeps it.")])

    tool(slug="png-to-jpg", group="img", icon="img", name="PNG to JPG", ftool="png2jpg", libs="",
         card="Convert PNG images to JPG.",
         title="PNG to JPG Converter – Free & Private | Tools for World",
         desc="Convert PNG to JPG online for free. Batch convert many images at once, no upload.",
         h1="PNG to JPG converter", lead="Convert PNG images to smaller JPG files. Transparent areas become white.",
         body='<h2>Why convert PNG to JPG?</h2><p>JPG files are much smaller for photos, and every website and form accepts them.</p>', faq=[])

    tool(slug="jpg-to-png", group="img", icon="img", name="JPG to PNG", ftool="jpg2png", libs="",
         card="Convert JPG images to PNG.",
         title="JPG to PNG Converter – Free & Private | Tools for World",
         desc="Convert JPG to PNG online for free. Batch convert images in your browser, no upload.",
         h1="JPG to PNG converter", lead="Convert JPG photos to lossless PNG files.",
         body='<h2>When to use PNG</h2><p>PNG is lossless, so it suits screenshots, graphics and images you will edit again. It does not make a JPG sharper, and the file will be larger.</p>', faq=[])

    tool(slug="webp-to-jpg", group="img", icon="img", name="WebP to JPG", ftool="webp2jpg", libs="",
         card="Convert WebP images to JPG.",
         title="WebP to JPG Converter – Free & Private | Tools for World",
         desc="Convert WebP images to JPG for free. Open images saved from websites in any app. No upload.",
         h1="WebP to JPG converter", lead="Convert WebP images, often saved from websites, to JPG so they open everywhere.",
         body='<h2>What is WebP?</h2><p>WebP is a modern image format used by many websites. Some apps and forms do not accept it, so converting to JPG is the easy fix.</p>', faq=[])

    tool(slug="heic-to-jpg", group="img", icon="img", name="HEIC to JPG", ftool="heic2jpg", libs=HEIC,
         card="Convert iPhone HEIC photos to JPG.",
         title="HEIC to JPG Converter Free – iPhone HEIC to JPEG",
         desc="Convert iPhone HEIC and HEIF photos to JPG (JPEG) for free. Batch convert in your browser with no upload, then download one by one or as a ZIP.",
         h1="HEIC to JPG converter", lead="Convert iPhone photos (.heic / .heif) to JPG so they open on Windows, Android and any website.",
         body='''<h2>How to convert HEIC to JPG</h2><ol><li>Choose one or more .heic photos.</li><li>Set the quality.</li><li>Press <b>Convert to JPG</b>.</li></ol><p>Tip: on iPhone, Settings → Camera → Formats → “Most Compatible” saves new photos as JPG.</p>
<h2>HEIC to PDF</h2><p>Convert the photos to JPG here first, then put them into one PDF with <a href="../jpg-to-pdf/">JPG to PDF</a>. Need the photos smaller for an upload? Run them through the <a href="../compress-image/">Image Compressor</a>.</p>''',
         faq=[("Why can't I open HEIC files?", "HEIC is Apple's photo format. Many Windows PCs, Android phones and websites don't support it."),
              ("Is JPEG the same as JPG?", "Yes. JPG and JPEG are two spellings of the same format; the files are identical.")])

    tool(slug="passport-photo-maker", group="img", icon="user", name="Passport Photo Maker", ftool="passport", libs="",
         card="Passport photos and a 4×6 print sheet.",
         title="Passport Photo Maker – 35×45 mm & 2×2 inch Free | Tools for World",
         desc="Make passport and visa photos online: 35×45 mm (UK, EU, Australia, India), 2×2 inch (US) and more. Get a ready-to-print 4×6 sheet.",
         h1="Passport photo maker", lead="Crop a photo to passport size and get a ready-to-print 4×6 inch sheet.",
         body='''<h2>Tips for a good passport photo</h2><ul><li>Face the camera, plain light background, no shadows.</li><li>Use the zoom slider so the head fills most of the frame; the guide lines show where the chin and top of head should be.</li><li>Print the 4×6 sheet at a photo shop or at home at 100% scale.</li></ul><p>Always check the latest rules of the office you are applying to.</p>''', faq=[])

    # ================= Text & utility =================
    tool(slug="qr-code-generator", group="util", icon="qr", name="QR Code Generator", calc="qr", libs=QRLIB,
         card="Make a QR code for a link, text or Wi-Fi.",
         title="QR Code Generator – Free, No Sign-up, No Expiry | Tools for World",
         desc="Create QR codes for free: links, text, phone numbers and Wi-Fi. Pick colours and size, download PNG. Codes never expire.",
         h1="QR code generator", lead="Type a link or text and download a QR code. Free, with no sign-up, and the code never expires.",
         ui=f'''<div class="calc"><div class="pp"><canvas id="qrc" width="300" height="300" aria-label="QR code preview" style="background:#fff"></canvas><div style="display:grid;gap:12px">
{F("Link or text", '<textarea id="qt" rows="3" style="width:100%;font:inherit;padding:8px 10px;border-radius:8px;border:1px solid var(--line);background:var(--sunk);color:var(--fg)">https://example.com</textarea>')}
<div class="row" style="gap:8px"><button class="btn ghost" type="button" data-qt="https://">Link</button><button class="btn ghost" type="button" data-qt="WIFI:T:WPA;S:MyNetwork;P:password;;">Wi-Fi</button><button class="btn ghost" type="button" data-qt="tel:+10000000000">Phone</button><button class="btn ghost" type="button" data-qt="mailto:name@example.com">Email</button></div>
<div class="fields">{F("Size", SEL("qs", [("256", "Small (256 px)"), ("512", "Medium (512 px)"), ("1024", "Large (1024 px)"), ("2048", "Print (2048 px)")], "512"))}
{F("Error correction", SEL("qe", [("L", "Low (7%)"), ("M", "Medium (15%)"), ("Q", "High (25%)"), ("H", "Highest (30%)")], "M"))}
{F("Colour", '<input type="color" id="qfg" value="#000000">')}{F("Background", '<input type="color" id="qbg" value="#ffffff">')}</div>
<div class="row"><button class="btn" id="qdl" type="button">Download PNG</button><span class="note" id="qinfo"></span></div><p class="note err" id="qerr" hidden></p></div></div></div>''',
         body='''<h2>How to make a QR code</h2><ol><li>Type or paste a link, text, phone number or Wi-Fi details.</li><li>Choose the size and colours.</li><li>Download the PNG and print or share it.</li></ol>
<h2>Tips</h2><ul><li>Keep strong contrast: dark code on a light background scans best.</li><li>Use “High” error correction if the code will be printed small or might get scratched.</li><li>Always test-scan before you print hundreds of copies.</li></ul>''',
         faq=[("Do these QR codes expire?", "No. The data is stored in the code itself, so it works forever."),
              ("Can I make a Wi-Fi QR code?", "Yes. Press the Wi-Fi button and replace the network name and password.")])

    tool(slug="word-counter", group="util", icon="text", name="Word Counter", calc="words", libs="",
         card="Count words, characters and reading time.",
         title="Word Counter – Count Words & Characters Online Free | Tools for World",
         desc="Free word counter: count words, characters with and without spaces, sentences and paragraphs, plus reading and speaking time.",
         h1="Word counter", lead="Paste or type your text to count words, characters, sentences and reading time instantly.",
         ui=f'''<div class="calc"><textarea id="wt" rows="10" style="width:100%;font:inherit;padding:12px;border-radius:10px;border:1px solid var(--line);background:var(--sunk);color:var(--fg)" placeholder="Start typing or paste your text here…">Tools for World counts your words as you type. Paste an essay, article or social media post to see the word count, character count and reading time.</textarea>
<div class="row"><button class="btn ghost" id="wclear" type="button">Clear text</button></div>
<div class="result"><div class="kv" id="out-kv"></div><div class="scroll"><table class="t"><thead><tr><th>Most used words</th><th class="n">Times</th><th class="n">Share</th></tr></thead><tbody id="out-top"></tbody></table></div></div></div>''',
         body='''<h2>What it counts</h2><ul><li><b>Words</b> and <b>characters</b>, with and without spaces.</li><li><b>Sentences</b> and <b>paragraphs</b>.</li><li><b>Reading time</b> at 238 words a minute and <b>speaking time</b> at 140.</li></ul>
<h2>Common limits</h2><ul><li>X (Twitter) post: 280 characters.</li><li>Meta description: about 155 characters.</li><li>College essays: often 250–650 words.</li></ul>''',
         faq=[("Is my text saved?", "No. The counting happens in your browser and nothing is stored.")])

    tool(slug="password-generator", group="util", icon="lock", name="Password Generator", calc="pass", libs="",
         card="Strong random passwords in one click.",
         title="Password Generator – Strong Random Passwords Free | Tools for World",
         desc="Generate strong, random passwords with letters, numbers and symbols. Uses your browser's secure random generator. Nothing is sent or stored.",
         h1="Password generator", lead="Create strong random passwords. They are made on your device with a secure random generator and never sent anywhere.",
         ui=f'''<div class="calc"><div class="row"><label>Length <input type="range" id="pl" min="8" max="64" value="16"> <b id="plv" class="sz">16</b></label></div>
<div class="row"><label class="check"><input type="checkbox" id="p_upper" checked> A–Z</label><label class="check"><input type="checkbox" id="p_lower" checked> a–z</label><label class="check"><input type="checkbox" id="p_digits" checked> 0–9</label><label class="check"><input type="checkbox" id="p_symbols" checked> !@#$</label><label class="check"><input type="checkbox" id="p_sim"> Avoid look-alikes (O, 0, l, 1)</label></div>
<div class="result"><div id="out-strength"></div><div class="files" id="out-list"></div><p><button class="btn" id="pgen" type="button">Generate new passwords</button></p></div></div>''',
         body='''<h2>What makes a password strong?</h2><ul><li><b>Length</b> matters most: use 16 characters or more.</li><li>Mix upper and lower case letters, numbers and symbols.</li><li>Use a different password for every account, and keep them in a password manager.</li></ul>''',
         faq=[("Are these passwords safe to use?", "Yes. They are generated on your device with crypto.getRandomValues, the browser's cryptographic random generator, and are never sent or saved.")])

    tool(slug="age-calculator", group="util", icon="calc", name="Age Calculator", calc="age", libs="",
         card="Exact age in years, months and days.",
         title="Age Calculator – Calculate Exact Age by Date of Birth | Tools for World",
         desc="Calculate your exact age in years, months and days from your date of birth. Also see total days, weeks and your next birthday.",
         h1="Age calculator", lead="Enter a date of birth to get the exact age in years, months and days, and the countdown to the next birthday.",
         ui=f'''<div class="calc"><div class="fields">{F("Date of birth", '<input type="date" id="adob" value="2000-01-15">')}{F("Age on this date", '<input type="date" id="ato">', "Today by default")}</div>{RESULT(kv=True, note=False)}</div>''',
         body='''<h2>How age is calculated</h2><p>Full years are counted first, then whole months, then the remaining days. That's the method used for forms and official documents. Total days include leap days.</p>''',
         faq=[("How do I find my age on a past or future date?", "Change the “Age on this date” field to any date.")])

    tool(slug="percentage-calculator", group="util", icon="calc", name="Percentage Calculator", calc="pct", libs="",
         card="Percent of, percent change and discounts.",
         title="Percentage Calculator – Percent of a Number, % Change | Tools for World",
         desc="Free percentage calculator: find X% of a number, what percent one number is of another, percentage increase or decrease, and add or subtract a percentage.",
         h1="Percentage calculator", lead="Five quick percentage calculators in one place. Results update as you type.",
         ui='''<div class="calc">
<div class="row">What is <input type="number" id="p1a" value="15" style="width:90px">% of <input type="number" id="p1b" value="200" style="width:110px">? <b class="big" style="font-size:1.4rem" id="r1"></b></div>
<div class="row"><input type="number" id="p2a" value="30" style="width:110px"> is what % of <input type="number" id="p2b" value="120" style="width:110px">? <b class="big" style="font-size:1.4rem" id="r2"></b></div>
<div class="row">From <input type="number" id="p3a" value="80" style="width:110px"> to <input type="number" id="p3b" value="100" style="width:110px"> is <b class="big" style="font-size:1.4rem" id="r3"></b></div>
<div class="row">Add <input type="number" id="p4a" value="18" style="width:90px">% to <input type="number" id="p4b" value="1000" style="width:110px"> = <b class="big" style="font-size:1.4rem" id="r4"></b></div>
<div class="row">Take <input type="number" id="p5a" value="25" style="width:90px">% off <input type="number" id="p5b" value="1000" style="width:110px"> = <b class="big" style="font-size:1.4rem" id="r5"></b></div>
</div>''',
         body='''<h2>Percentage formulas</h2><ul><li>X% of Y = X ÷ 100 × Y</li><li>X is what % of Y = X ÷ Y × 100</li><li>% change = (new − old) ÷ old × 100</li><li>Add X% = Y × (1 + X ÷ 100) · Take X% off = Y × (1 − X ÷ 100)</li></ul>''',
         faq=[("How do I calculate a discount?", "Use “Take X% off”: 25% off 1000 is 750.")])

    # ================= Audio & video =================
    tool(slug="mp4-to-mp3", group="media", icon="music", name="MP4 to MP3", ftool="mp4mp3", libs=LAME,
         card="Extract the audio from a video as MP3.",
         title="MP4 to MP3 Converter – Extract Audio from Video Free | Tools for World",
         desc="Convert MP4 videos to MP3 audio for free. Extract sound from MP4, MOV and WebM files in your browser, no upload.",
         h1="MP4 to MP3 converter", lead="Extract the audio from a video file and save it as MP3. The file stays on your device.",
         body='''<h2>How to convert MP4 to MP3</h2><ol><li>Choose a video (MP4, MOV, WebM).</li><li>Pick the quality: 192 kbps suits most music and speech.</li><li>Press <b>Convert to MP3</b>.</li></ol>
<div class="warnbox">Only convert videos you own or have permission to use. Downloading from YouTube is not supported.</div>''',
         faq=[("Is there a size limit?", "No fixed limit, but very long videos need a lot of memory and can fail on phones. Use a computer for videos over about 200 MB.")])


# ================= SEO landing pages (presets of the main tools) =================
LANDING = []


def landing(define_tool):
    t = define_tool
    for kb, use in ((10, "signatures and thumbnail-size form fields"), (20, "signature uploads and tiny form fields"),
                    (30, "exam forms that ask for a small photo"), (50, "government and exam application forms"),
                    (100, "job portals, visa forms and email"), (200, "website uploads and online profiles"),
                    (500, "high-quality photos that still upload fast"), (1024, "photos that must stay under 1 MB"),
                    (2048, "email attachments and portals with a 2 MB limit"), (5120, "upload forms that cap files at 5 MB")):
        lab = f"{kb // 1024}MB" if kb >= 1024 else f"{kb}KB"; lab_s = f"{kb // 1024} MB" if kb >= 1024 else f"{kb} KB"
        t(slug=f"compress-image-to-{lab.lower()}", group="img", icon="img", name=f"Compress Image to {lab}", ftool="compress", libs="",
          parent="compress-image", preset={"#tkb": kb},
          card=f"Make any photo under {lab_s} automatically.",
          title=f"Compress Image to {lab} – Resize Photo to {lab_s} Free",
          desc=f"Compress JPG, PNG or WebP images to {lab} or less in one click. Free, no upload: the photo is resized in your browser until it is just under {lab_s}.",
          h1=f"Compress image to {lab}", lead=f"Choose a photo and it is made just under {lab_s} automatically, keeping as much quality as possible. Ideal for {use}.",
          body=f'''<h2>How to compress a photo to {lab}</h2><ol><li>Choose your photo (JPG, PNG or WebP).</li><li>The target is already set to <b>{lab_s}</b>. Change it if you need a different size.</li><li>Press <b>Compress</b> and download the photo.</li></ol>
<h2>How it works</h2><p>The tool tries many quality levels and picks the highest one that stays under {lab_s}. If the photo is still too big at the lowest quality, it is scaled down a little at a time until it fits. Everything happens on your device, so your photo is never uploaded.</p>
<h2>Tips</h2><ul><li>Crop away empty background first: less detail means better quality at {lab_s}.</li><li>Most forms want JPG. Keep the output on JPG unless WebP is allowed.</li></ul>''',
          faq=[(f"Is this the same as “resize image to {lab_s}”?", f"Yes. When a form asks you to resize a photo to {lab_s}, it means the file size. This tool lowers the file size to {lab_s} and only reduces the width and height if it has to."),
               (f"Will my photo still look good at {lab}?", "For most photos, yes. The tool keeps the best quality that fits. Very large, detailed photos may be scaled down to fit."),
               (f"Can I compress several photos to {lab} at once?", "Yes. Choose several files and each one is compressed to the target size.")])

    for w, h, label, use in ((1080, 1080, "Instagram post", "square Instagram and Facebook posts"),
                             (1080, 1920, "Instagram story / Reels", "Instagram stories, Reels, TikTok and WhatsApp status"),
                             (1200, 630, "Facebook & link preview", "Facebook posts, link previews and Open Graph images"),
                             (1280, 720, "YouTube thumbnail", "YouTube thumbnails and HD slides"),
                             (600, 600, "passport photo 2×2 inch", "online US passport and visa photo uploads (2×2 inch at 300 dpi)"),
                             (400, 400, "profile picture", "profile pictures on LinkedIn, Discord, forums and apps"),
                             (1920, 1080, "Full HD", "Full HD wallpapers, presentations and video frames"),
                             (1584, 396, "LinkedIn banner", "LinkedIn profile background banners"),
                             (1500, 500, "X / Twitter header", "X (Twitter) profile header images"),
                             (2560, 1440, "YouTube banner", "YouTube channel banners (keep text in the centre)"),
                             (1080, 1350, "Instagram portrait", "portrait Instagram posts that fill more of the feed"),
                             (851, 315, "Facebook cover", "Facebook page and profile cover photos"),
                             (1000, 1500, "Pinterest pin", "Pinterest pins in the recommended 2:3 shape"),
                             (500, 500, "WhatsApp DP", "WhatsApp, Telegram and Signal profile pictures"),
                             (1024, 1024, "app icon", "app icons, logos and square AI-image inputs"),
                             (3000, 3000, "album cover", "Spotify, Apple Music and podcast cover art")):
        t(slug=f"resize-image-to-{w}x{h}", group="img", icon="img", name=f"Resize to {w}×{h}", ftool="resize", libs="",
          parent="resize-image", preset={"#rm": "px", "#rw": w, "#rh": h, "#rk": False, "#rf": "crop"},
          card=f"{label}: exactly {w}×{h} px.",
          title=f"Resize Image to {w}x{h} Pixels Free ({label})" if len(label) > 16 else f"Resize Image to {w}x{h} Pixels Online Free ({label})",
          desc=f"Resize any photo to exactly {w}×{h} pixels for {use}. Crop to fill or add a border. Free and private: works in your browser.",
          h1=f"Resize image to {w}×{h} pixels", lead=f"Get a photo that is exactly {w} × {h} px for {use}. Choose crop to fill, or fit with a white border.",
          body=f'''<h2>How to resize to {w}×{h}</h2><ol><li>Choose one or more images.</li><li>The size is already set to <b>{w} × {h}</b>.</li><li>Pick <b>Crop to fill</b> (no empty space) or <b>Fit with white border</b> (nothing cut off), then press <b>Resize</b>.</li></ol>
<h2>Why exact size matters</h2><p>Platforms crop or blur images that are the wrong shape. Uploading at exactly {w} × {h} px keeps your photo sharp and framed the way you want.</p>''',
          faq=[("Will my photo be stretched?", "No. Crop to fill keeps the proportions and trims the edges; Fit with white border keeps the whole photo and adds a border.")])

    for code, lang, extra in (("urd", "Urdu", "Nastaliq printed text from books, newspapers and screenshots"),
                              ("ara", "Arabic", "printed Arabic text, documents and screenshots"),
                              ("hin", "Hindi", "printed Devanagari text from documents and screenshots"),
                              ("spa", "Spanish", "printed Spanish text from documents, books and screenshots"),
                              ("fra", "French", "printed French text, including accents, from documents and screenshots"),
                              ("deu", "German", "printed German text, including umlauts, from documents and screenshots"),
                              ("por", "Portuguese", "printed Portuguese text from documents and screenshots"),
                              ("ita", "Italian", "printed Italian text from documents and screenshots"),
                              ("rus", "Russian", "printed Cyrillic text from documents and screenshots"),
                              ("tur", "Turkish", "printed Turkish text from documents and screenshots"),
                              ("ben", "Bengali", "printed Bangla text from documents and screenshots"),
                              ("ind", "Indonesian", "printed Indonesian text from documents and screenshots"),
                              ("chi_sim", "Chinese", "printed Simplified Chinese text from documents and screenshots")):
        t(slug=f"image-to-text-{lang.lower()}", group="pdf", icon="text", name=f"{lang} Image to Text", ftool="ocr", libs=TESS,
          parent="image-to-text", preset={"#ol": code},
          card=f"Copy {lang} text from a photo (OCR).",
          title=f"{lang} OCR – Image to Text in {lang} Online Free | Tools for World",
          desc=f"Free {lang} OCR: extract {lang} text from images, photos and screenshots and copy it. Runs in your browser, no upload.",
          h1=f"{lang} image to text (OCR)", lead=f"Extract {lang} text from a photo or screenshot so you can copy, edit and search it. Works for {extra}.",
          body=f'''<h2>How to convert {lang} image to text</h2><ol><li>Choose a clear photo or screenshot.</li><li>The language is already set to <b>{lang}</b>.</li><li>Press <b>Extract text</b> and copy the result.</li></ol>
<h2>Tips for accurate {lang} OCR</h2><ul><li>Use a sharp image with dark text on a light background.</li><li>Crop to the text only, and keep lines straight.</li><li>Printed text works much better than handwriting.</li></ul>''',
          faq=[(f"Is {lang} OCR free?", "Yes, with no limits. The text recognition runs on your own device."),
               ("Why are some words wrong?", "Blurry photos, unusual fonts and handwriting reduce accuracy. Try a clearer, cropped image.")])

    t(slug="wifi-qr-code-generator", group="util", icon="qr", name="Wi-Fi QR Code", calc="qr", libs=QRLIB, parent="qr-code-generator",
      preset={"#qt": "WIFI:T:WPA;S:MyNetwork;P:MyPassword;;"},
      card="Guests scan to join your Wi-Fi.",
      title="Wi-Fi QR Code Generator – Share Wi-Fi Without Typing the Password | Tools for World",
      desc="Make a free Wi-Fi QR code: guests scan it with their phone camera to join your network. No sign-up, works offline once loaded.",
      h1="Wi-Fi QR code generator", lead="Create a QR code that connects phones to your Wi-Fi in one scan. Replace the network name and password in the box.",
      ui=None, body='''<h2>How to make a Wi-Fi QR code</h2><ol><li>In the box, replace <code>MyNetwork</code> with your Wi-Fi name and <code>MyPassword</code> with the password.</li><li>Keep <code>T:WPA</code> for most routers (use <code>T:WEP</code> for very old ones, or <code>T:nopass</code> for open networks).</li><li>Download the PNG and print it for guests.</li></ol>
<p>iPhone and Android cameras both read Wi-Fi QR codes and offer to join the network.</p>''',
      faq=[("Is my Wi-Fi password sent anywhere?", "No. The QR code is made in your browser and nothing is uploaded.")])

    t(slug="whatsapp-qr-code-generator", group="util", icon="qr", name="WhatsApp QR Code", calc="qr", libs=QRLIB, parent="qr-code-generator",
      preset={"#qt": "https://wa.me/15551234567?text=Hello"},
      card="Customers scan to message you on WhatsApp.",
      title="WhatsApp QR Code Generator – Free QR for Your WhatsApp Number | Tools for World",
      desc="Create a WhatsApp QR code for your number with a ready message. Customers scan to start a chat. Free, no sign-up, never expires.",
      h1="WhatsApp QR code generator", lead="Make a QR code that opens a WhatsApp chat with you. Put your number (with country code) in the link.",
      ui=None, body='''<h2>How to make a WhatsApp QR code</h2><ol><li>In the box, replace <code>15551234567</code> with your number in international format, without + or spaces (for example 923001234567 for Pakistan or 61412345678 for Australia).</li><li>Change the text after <code>?text=</code> to the first message you want customers to send, or delete it.</li><li>Download the PNG and put it on your shop counter, menu, card or flyer.</li></ol>''',
      faq=[("Does the QR code expire?", "No. It's a normal wa.me link stored in the code, so it works forever.")])

    # ---- Compress PDF to an exact size ----
    PDFLIBS = ('<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js" integrity="sha384-weMABwrltA6jWR8DDe9Jp5blk+tZQh7ugpCsF3JwSA53WZM9/14PjS5LAJNHNjAI" crossorigin="anonymous"></script>'
               '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js" integrity="sha384-/1qUCSGwTur9vjf/z9lmu/eCUYbpOTgSjmpbMQZ1/CtX2v/WcAIKqRv+U1DUCG6e" crossorigin="anonymous"></script>')
    for kb, use in ((100, "online application forms and portals with a strict 100 KB limit"),
                    (200, "job applications, university forms and government portals"),
                    (300, "visa and admission forms that allow up to 300 KB"),
                    (500, "email attachments and most upload forms"),
                    (1024, "email, WhatsApp and portals with a 1 MB limit"),
                    (2048, "job and university portals with a 2 MB upload limit"),
                    (5120, "email attachments and portals that allow up to 5 MB")):
        lab = f"{kb // 1024}MB" if kb >= 1024 else f"{kb}KB"; lab_s = f"{kb // 1024} MB" if kb >= 1024 else f"{kb} KB"
        t(slug=f"compress-pdf-to-{lab.lower()}", group="pdf", icon="pdf", name=f"Compress PDF to {lab}", ftool="pdfcompress", libs=PDFLIBS,
          parent="compress-pdf", preset={"#ptkb": kb},
          card=f"Shrink a PDF to under {lab_s} automatically.",
          title=f"Compress PDF to {lab} Online Free – PDF Under {lab_s} | Tools for World",
          desc=f"Compress a PDF to {lab} or less for free. The best quality that fits under {lab_s} is picked for you. No upload: works in your browser.",
          h1=f"Compress PDF to {lab}", lead=f"Choose a PDF and it is made just under {lab_s}, keeping as much quality as possible. Ideal for {use}.",
          body=f'''<h2>How to compress a PDF to {lab}</h2><ol><li>Choose your PDF.</li><li>The target is already set to <b>{lab_s}</b>. Change it if your form allows a different size.</li><li>Press <b>Compress PDF</b> and download the smaller file.</li></ol>
<h2>How it works</h2><p>Each page is re-saved as a compressed image. The tool tries several quality levels and keeps the sharpest one that still fits under {lab_s}. Your file never leaves your device.</p>
<h2>Tips</h2><ul><li>Scanned documents and PDFs full of photos shrink the most.</li><li>Fewer pages means better quality at {lab_s}. Remove pages you don't need with <a href="../split-pdf/">Split PDF</a> first.</li><li>Text in the result can no longer be selected or searched, which is fine for forms and scans.</li></ul>''',
          faq=[(f"What if my PDF can't get under {lab}?", "The tool shows the smallest size it could reach. Split the PDF into parts or remove pages, then try again."),
               ("Is my PDF uploaded?", "No. Compression happens inside your browser, so the file stays on your device.")])

    # ---- Passport and visa photos by country ----
    for slug, country, ps, size_txt, bg in (
            ("us-passport-photo", "US", "50.8x50.8", "2 × 2 inches (51 × 51 mm)", "plain white or off-white"),
            ("uk-passport-photo", "UK", "35x45", "35 × 45 mm", "plain light grey or cream"),
            ("canada-passport-photo", "Canada", "50x70", "50 × 70 mm", "plain white or light-coloured"),
            ("australia-passport-photo", "Australia", "35x45", "35 × 45 mm", "plain light-coloured"),
            ("india-passport-photo", "India", "35x45", "35 × 45 mm", "plain white"),
            ("schengen-visa-photo", "Schengen visa", "35x45", "35 × 45 mm", "plain light-coloured"),
            ("china-visa-photo", "China visa", "33x48", "33 × 48 mm", "plain white")):
        t(slug=slug, group="img", icon="user", name=f"{country} Passport Photo" if "visa" not in country else f"{country} Photo",
          ftool="passport", libs="", parent="passport-photo-maker", preset={"#ps": ps},
          card=f"{size_txt}, plus a 4×6 print sheet.",
          title=f"{country.replace(' visa', ' Visa')} {'Passport ' if 'visa' not in country else ''}Photo Maker – {size_txt.split(' (')[0]}, Size & Requirements",
          desc=f"Make a {country} {'passport ' if 'visa' not in country else ''}photo online for free: crop to {size_txt} and get a ready-to-print 4×6 inch sheet. No upload, works on your phone.",
          h1=f"{country} {'passport ' if 'visa' not in country else ''}photo maker",
          lead=f"Crop your photo to the {country} size of {size_txt} and download a single photo plus a 4×6 inch sheet to print.",
          body=f'''<h2>How to make a {country} {'passport ' if 'visa' not in country else ''}photo</h2><ol><li>Take a photo facing the camera against a {bg} background, with even light and no shadows.</li><li>Choose the photo. The size is already set to <b>{size_txt}</b>.</li><li>Use zoom and the sliders so the top of the head is near the upper guide line and the chin near the lower one.</li><li>Press <b>Make sheet</b>. Print the 4×6 sheet at 100% scale at home or at a photo shop, or use the single photo for online applications.</li></ol>
<h2>Photo checklist</h2><ul><li>Size: {size_txt}.</li><li>Background: {bg}, with no patterns or objects.</li><li>Neutral expression, mouth closed, eyes open and visible.</li><li>No glasses glare, hats or filters.</li></ul>
<p>Applying online? Many portals set a file-size limit: <a href="../compress-image-to-50kb/">compress the photo to 50 KB</a>, <a href="../compress-image-to-100kb/">100 KB</a> or <a href="../compress-image-to-200kb/">200 KB</a> after making it here.</p>
<div class="warnbox">Rules change from time to time. Always check the latest photo requirements on the official government website before you apply.</div>''',
          faq=[(f"What size is a {country} {'passport ' if 'visa' not in country else ''}photo?", f"{size_txt}. This tool crops your photo to exactly that size at 300 dpi."),
               ("Is my photo uploaded?", "No. Cropping and the print sheet are made in your browser, so the photo stays on your device.")])

    # ---- Utility variants ----
    t(slug="character-counter", group="util", icon="text", name="Character Counter", calc="words", libs="", parent="word-counter",
      card="Count characters with and without spaces.",
      title="Character Counter – Count Characters Online Free | Tools for World",
      desc="Free character counter: count characters with and without spaces, plus words and sentences. Check limits for X posts, meta descriptions, SMS and bios.",
      h1="Character counter", lead="Paste your text to count characters with and without spaces as you type. Handy for posts, bios, ads and SMS.",
      ui=None, body='''<h2>Common character limits</h2><ul><li>X (Twitter) post: 280 characters.</li><li>SMS: 160 characters per message (70 with emoji or non-Latin letters).</li><li>Instagram bio: 150 characters.</li><li>Google meta description: about 155 characters before it gets cut off.</li><li>Google Ads headline: 30 characters; description: 90.</li></ul>
<p>Emoji and many non-Latin letters count as one character here, the way people read them.</p>''',
      faq=[("Do spaces count as characters?", "Usually yes. That's why both numbers are shown: with spaces and without spaces."),
           ("Is my text saved?", "No. Counting happens in your browser and nothing is stored.")])

    t(slug="discount-calculator", group="util", icon="calc", name="Discount Calculator", calc="pct", libs="", parent="percentage-calculator",
      preset={"#p5a": 20, "#p5b": 100},
      card="Sale price after a % discount.",
      title="Discount Calculator – Price After % Off | Tools for World",
      desc="Free discount calculator: find the sale price after a percentage off, how much you save, and the percent change between two prices.",
      h1="Discount calculator", lead="Use “Take X% off” to see the sale price. The other rows show savings as a percent and the change between two prices.",
      ui=None, body='''<h2>How to calculate a discount</h2><ol><li>In “Take X% off”, enter the discount (for example 20) and the original price.</li><li>The sale price appears instantly: 20% off 100 is 80.</li><li>To find the discount you got, enter the old and new price in the “From … to …” row.</li></ol>
<p>Formula: sale price = price × (1 − discount ÷ 100). Stacked discounts multiply: 20% then 10% off is 28% off in total, not 30%.</p>''',
      faq=[("How do I work out two discounts in a row?", "Apply them one after the other: 20% off 100 is 80, then 10% off 80 is 72. That's 28% off in total.")])


# ================= Extra, page-specific content (makes each page genuinely different and more useful) =================
def _add(T, slug, body="", faq=()):
    for t in T:
        if t["slug"] == slug:
            t["body"] = t["body"] + body
            t["faq"] = list(t.get("faq", [])) + list(faq)
            return


OCR_NOTES = {
    "urd": ("Urdu is written right to left in Nastaliq, a sloping, stacked script that is one of the hardest for OCR. Large, clear printed text (book pages, headlines, screenshots) gives the best results; small newspaper columns are harder. The result box switches to right-to-left automatically. For pages that mix Urdu and English, choose “English + Urdu” in the language menu.",
            ("Why is Urdu OCR less accurate than English?", "Nastaliq letters join and overlap diagonally, which makes them hard to separate. Use a sharp, large image and crop to one column of text.")),
    "ara": ("Arabic is read right to left and its letters join, so a clean, high-contrast image matters. Short vowel marks (harakat) are often dropped from the result, and decorative calligraphy fonts are not recognised well. The result box switches to right-to-left automatically.",
            ("Does it keep Arabic diacritics?", "Often not. The base letters are recognised; harakat and tashkeel marks may be missing, so check religious or teaching texts carefully.")),
    "hin": ("Hindi is written in Devanagari, with letters hanging from a top line (shirorekha). Printed text from books, forms and screenshots works well; joined conjunct letters are the most common source of mistakes. Marathi and Nepali also use Devanagari but have their own language models, so expect a few errors with them here.",
            ("Can it read Marathi or Nepali?", "It can read the Devanagari letters, but it uses the Hindi dictionary, so some words may be wrong. Check the result before using it.")),
    "spa": ("The Spanish model recognises accented letters (á é í ó ú), ñ and the opening ¿ and ¡ marks. Accents are small, so a sharp image matters: if accents go missing, use a larger or clearer photo.",
            ("Does it work for Latin American Spanish?", "Yes. The written language is the same, so any printed Spanish text works.")),
    "fra": ("The French model reads accents (é è ê à ç), the œ ligature and guillemets (« »). Accents are the first thing to suffer in a blurry photo, so check them in the result.",
            ("Why are some accents wrong?", "Accents are tiny marks. Take the photo closer, in good light, and crop to the text to keep them.")),
    "deu": ("The German model reads umlauts (ä ö ü) and ß. It is built for modern printed fonts: old blackletter (Fraktur) books from before about 1940 are not recognised well.",
            ("Can it read old Fraktur (blackletter) text?", "Not reliably. This model is trained on modern fonts.")),
    "por": ("The Portuguese model reads ã, õ, ç and the other accented vowels, for both Brazilian and European Portuguese printed text.",
            ("Does it work for Brazilian Portuguese?", "Yes. Both Brazilian and European spelling are printed with the same letters.")),
    "ita": ("The Italian model reads accented vowels (à è é ì ò ù) and apostrophes in words like l'acqua. A sharp, straight photo keeps accents and apostrophes accurate.",
            ("Does it keep apostrophes?", "Usually yes. Blurry photos can turn them into spaces, so check words like dell' and un'.")),
    "rus": ("The Russian model reads the Cyrillic alphabet, including ё. Ukrainian, Belarusian and Bulgarian also use Cyrillic but have letters Russian does not (such as і, ї, є, ў), so those may be misread.",
            ("Can it read Ukrainian?", "Partly. Shared Cyrillic letters are read, but Ukrainian-only letters like ї and є may come out wrong.")),
    "tur": ("The Turkish model reads ç, ğ, ş, ö, ü and both the dotted İ/i and dotless I/ı. Check i and ı in the result: they are easy to confuse in small or blurry text.",
            ("Why does it mix up i and ı?", "The only difference is a tiny dot. A sharper, closer photo fixes most of these.")),
    "ben": ("Bengali (Bangla) text has many joined conjunct letters (juktakkhor). Printed text at a normal reading size works well; very small print loses detail. Assamese uses a very similar script but has letters of its own.",
            ("Can it read Assamese?", "Many letters are shared, but Assamese has its own letters and words, so expect some mistakes.")),
    "ind": ("Indonesian uses the Latin alphabet without accents, so OCR is usually very accurate on clear printed text. Malay is written very similarly and often comes out well too.",
            ("Does it work for Malay?", "Usually yes, because Malay and Indonesian share most spelling. Check names and less common words.")),
    "chi_sim": ("This model reads Simplified Chinese (mainland China, Singapore). Traditional characters used in Taiwan and Hong Kong are less accurate. Horizontal text works best; text printed in vertical columns may come out in the wrong order.",
            ("Can it read Traditional Chinese?", "Some characters are shared, but accuracy is lower. This page uses the Simplified Chinese model.")),
}

PASSPORT_NOTES = {
    "us-passport-photo": ("""<h2>US passport and visa photo rules at a glance</h2><ul><li>Size 2 × 2 inches (51 × 51 mm); head 1 to 1⅜ inches (25–35 mm) from chin to top of hair.</li><li>Plain white or off-white background, taken in the last 6 months.</li><li>No glasses: the US has not accepted glasses in passport photos since November 2016.</li><li>US visa (DS-160) digital photo: a square JPEG between 600 × 600 and 1200 × 1200 pixels and no larger than 240 KB. The single photo from this tool is 600 × 600 px.</li></ul><p>Official rules: <a href="https://travel.state.gov/content/travel/en/passports/how-apply/photos.html" rel="nofollow">travel.state.gov passport photos</a>.</p>""",
                          ("Can I use this photo for a US visa (DS-160)?", "Yes, the single photo is a 600 × 600 px JPEG, usually well under 240 KB. Check it in the State Department's photo tool before submitting.")),
    "uk-passport-photo": ("""<h2>UK passport photo rules at a glance</h2><ul><li>Printed photos: 35 × 45 mm, head 29–34 mm from chin to crown.</li><li>Plain cream or light grey background, no shadows, taken in the last month.</li><li>Glasses are allowed only if you can't take them off and there is no glare; it's simplest to remove them.</li><li>Online applications use a digital photo that is at least 600 pixels wide and 750 pixels tall. The single photo from this tool is 413 × 531 px at 300 dpi, so for an online application take a new photo at full size instead of using the print crop.</li></ul><p>Official rules: <a href="https://www.gov.uk/photos-for-passports/photo-requirements" rel="nofollow">GOV.UK photo requirements</a>.</p>""",
                          ("Can I use this for the online UK passport application?", "The online service wants a larger digital photo (at least 600 × 750 px). Use this tool for printed photos, and upload your original phone photo online.")),
    "canada-passport-photo": ("""<h2>Canada passport photo rules at a glance</h2><ul><li>Size 50 × 70 mm; face 31–36 mm from chin to crown.</li><li>Plain white or light-coloured background, taken in the last 6 months.</li></ul><div class="warnbox">Canadian passport photos must be taken by a commercial photographer, who writes or stamps the date and the studio's name and full address on the back of one photo. Photos printed at home are not accepted for a Canadian passport, including for online renewals. Use this tool to practise framing, or for documents that accept self-made photos.</div><p>Official rules: <a href="https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-passports/photos.html" rel="nofollow">canada.ca passport photos</a>.</p>""",
                              ("Can I print my own Canadian passport photo?", "Usually not: Canada requires photos from a commercial photographer, with the date and studio details written or stamped on the back. Check the official page before you apply.")),
    "australia-passport-photo": ("""<h2>Australian passport photo rules at a glance</h2><ul><li>Size 35–40 mm wide and 45–50 mm high; face 32–36 mm from chin to crown. This tool uses 35 × 45 mm.</li><li>Plain white or light grey background, even lighting, no shadows.</li><li>Neutral expression, mouth closed, eyes open and clearly visible.</li></ul><p>Official rules: <a href="https://www.passports.gov.au/getting-passport-how-it-works/photo-guidelines" rel="nofollow">passports.gov.au photo guidelines</a>.</p>""",
                                 ("Is 35 × 45 mm accepted in Australia?", "Yes. Australia accepts photos from 35–40 mm wide and 45–50 mm high.")),
    "india-passport-photo": ("""<h2>Indian passport photo rules at a glance</h2><ul><li>Size 35 × 45 mm (3.5 × 4.5 cm), in colour, plain white background, dark-coloured clothes.</li><li>Head in the centre of the frame with both ears visible, eyes open, no shadows.</li><li>You only need a printed photo when applying at a District Passport Cell, Speed Post Centre or Citizen Service Centre; at a Passport Seva Kendra your photo is taken there. Indian missions abroad set their own size.</li><li>The Indian e-Visa for foreign nationals is different: it uses a square photo, so choose the 2 × 2 in size in the <a href="../passport-photo-maker/">passport photo maker</a>.</li></ul><p>Official information: <a href="https://www.passportindia.gov.in/AppOnlineProject/pdf/ApplicationformInstructionBooklet-V3.0.pdf" rel="nofollow">Passport Seva application instruction booklet (PDF)</a>.</p>""",
                             ("Is the Indian visa photo the same size?", "No. The Indian e-Visa uses a square photo. This page is for the 35 × 45 mm Indian passport photo.")),
    "schengen-visa-photo": ("""<h2>Schengen visa photo rules at a glance</h2><ul><li>Size 35 × 45 mm; German missions ask for the face to be 32–36 mm from the chin to the hairline.</li><li>Plain background in one light colour (white or light grey in most countries), taken in the last 6 months.</li><li>The same 35 × 45 mm size is used by every Schengen country, from France and Germany to Spain and Italy.</li></ul><p>Official example: <a href="https://hongkong.diplo.de/resource/blob/2572988/11fbf86d05a1668f0488a650e7d50aa6/biometric-passport-photos-d-e-data.pdf" rel="nofollow">German Missions biometric photo requirements (PDF)</a>. Each embassy or visa centre publishes its own checklist; check the one for the country you are applying to.</p>""",
                            ("Is the photo the same for every Schengen country?", "The size (35 × 45 mm) is the same. Background colour and how recent the photo must be can differ slightly by embassy.")),
    "china-visa-photo": ("""<h2>China visa photo rules at a glance</h2><ul><li>Size 33 × 48 mm; head 28–33 mm tall and 15–22 mm wide.</li><li>Plain white background, taken in the last 6 months, no hats or glasses glare.</li><li>The online visa form sets its own pixel and file-size limits. If your photo is too large, use <a href="../resize-image/">Resize Image</a> and <a href="../compress-image/">Compress Image</a> on the single photo.</li></ul><p>Official rules: <a href="https://visaforchina.cn/SGP2_EN/generalinformation/news/282849.shtml" rel="nofollow">Chinese Visa Application Service Center photo requirements</a>.</p>""",
                         ("Why is the China visa photo a different size?", "China uses 33 × 48 mm, taller and narrower than the common 35 × 45 mm, so photos for other visas usually aren't accepted.")),
}

KB_NOTES = {
    10: ("about 150 × 200 pixels", "Signatures: sign with a dark pen on plain white paper, photograph it in good light and crop tightly around the signature. At 10 KB, a tightly cropped signature stays sharp."),
    20: ("about 250 × 300 pixels", "Signature uploads often ask for 10–20 KB. Crop away the empty paper first so the signature itself keeps more detail."),
    30: ("about 300 × 400 pixels", "Many exam forms ask for a photo between 20 and 50 KB. If there is a minimum, set the target to the maximum allowed so you don't go under it."),
    50: ("about 400 × 500 pixels", "Government and exam portals often give both a size in cm (like 3.5 × 4.5 cm) and a KB range. Crop to the right shape first with Resize Image, then compress."),
    2048: ("about 2500 × 3300 pixels", "2 MB keeps nearly all the detail of a phone photo, and still fits most job portals and email limits."),
    5120: ("about 4000 × 3000 pixels, the full size of a 12-megapixel phone photo", "Many phone photos are already under 5 MB; if yours is, the tool keeps the original untouched."),
    100: ("about 600 × 800 pixels", "100 KB is enough for a clear face photo or a readable document scan for most job and visa portals."),
    200: ("about 900 × 1200 pixels", "At 200 KB most photos look sharp on any phone or laptop screen, which makes it a good size for profiles and website uploads."),
    500: ("about 1400 × 1900 pixels", "500 KB keeps photos detailed enough to zoom in, while still uploading quickly on mobile data."),
    1024: ("about 2000 × 2700 pixels", "A 1 MB photo is close to print quality for small prints, and it still fits email and most forms with a 1 MB limit."),
}


def enrich(T):
    for code, (note, fq) in OCR_NOTES.items():
        lang = {"chi_sim": "chinese"}.get(code)
        for t in T:
            if t.get("parent") == "image-to-text" and t.get("preset", {}).get("#ol") == code:
                t["body"] += f"<h2>About {t['name'].replace(' Image to Text', '')} text recognition</h2><p>{note}</p>"
                t["faq"] = list(t["faq"]) + [fq]
    for slug, (html_, fq) in PASSPORT_NOTES.items():
        for t in T:
            if t["slug"] == slug:
                t["body"] = t["body"].replace('<div class="warnbox">Rules change', html_ + '<div class="warnbox">Rules change')
                t["faq"] = list(t["faq"]) + [fq]
    for t in T:
        if t.get("parent") == "compress-image" and t.get("preset", {}).get("#tkb") in KB_NOTES:
            k = t["preset"]["#tkb"]; px, tip = KB_NOTES[k]; lab = f"{k // 1024} MB" if k >= 1024 else f"{k} KB"
            t["body"] += (f"<h2>How big is a {lab} photo?</h2><p>For a typical phone photo saved as JPG, {lab} fits roughly {px} at good quality. "
                          f"Simple images (a signature, a face on a plain wall) fit more pixels; busy scenes with lots of detail fit fewer.</p><p>{tip}</p>")

    _add(T, "png-to-jpg", '''<h2>How to convert PNG to JPG</h2><ol><li>Choose one or more PNG files.</li><li>Set the quality: 85–92% looks the same as the original for photos.</li><li>Press <b>Convert to JPG</b>, then download each file or all of them as one ZIP.</li></ol>
<h2>PNG or JPG: which should you use?</h2><ul><li><b>JPG</b> is best for photos. Files are much smaller, but there is no transparency.</li><li><b>PNG</b> is best for screenshots, logos, text and graphics with sharp edges or transparent parts. It is lossless, so files are larger.</li></ul><p>A photo saved as PNG is often 3–10 times larger than the same photo as JPG, so converting is the quickest way to get under an upload limit. To shrink it even more, use the <a href="../compress-image/">Image Compressor</a>.</p>''',
         [("What happens to transparent areas?", "They become white, because JPG can't store transparency. Keep the PNG if you need a see-through background."),
          ("Will I lose quality?", "JPG is lossy, but at 90% quality the difference is invisible in photos. Screenshots with small text may look slightly softer; keep those as PNG.")])
    _add(T, "jpg-to-png", '''<h2>How to convert JPG to PNG</h2><ol><li>Choose one or more JPG photos.</li><li>Press <b>Convert to PNG</b>.</li><li>Download each PNG, or all of them as one ZIP.</li></ol>
<h2>Good reasons to convert</h2><ul><li>An app, printer or website only accepts PNG.</li><li>You will edit and save the image many times: PNG doesn't lose quality each time it is saved.</li><li>You plan to add transparency or layers in an editor.</li></ul><p>For a transparent background, use the <a href="../remove-background/">Background Remover</a>, which outputs a transparent PNG.</p>''',
         [("Does JPG to PNG make the background transparent?", "No. The image stays exactly as it is. Use the Background Remover to get a transparent PNG."),
          ("Why is the PNG so much bigger?", "PNG is lossless, so it stores every pixel exactly. Photos are usually 2–5 times larger as PNG than as JPG.")])
    _add(T, "webp-to-jpg", '''<h2>How to convert WebP to JPG</h2><ol><li>Choose one or more .webp images.</li><li>Pick the quality (92% is a good default).</li><li>Press <b>Convert to JPG</b> and download.</li></ol>
<h2>Where WebP files come from</h2><p>Many websites serve images as WebP because the files are 25–35% smaller than JPG at similar quality. When you save an image from a website, you often get a .webp file that older apps, photo editors and upload forms won't open. JPG works everywhere.</p>''',
         [("Is WebP better than JPG?", "For websites, often yes: WebP files are smaller. For sharing and uploading, JPG is safer because every app and form accepts it."),
          ("Do animated WebP images work?", "Only the first frame is converted, because JPG can't store animation.")])
    _add(T, "pdf-to-jpg", '''<h2>Which quality should I pick?</h2><ul><li><b>Normal</b> (about 108 dpi): small files, fine for sharing on phones.</li><li><b>High</b> (about 144 dpi): sharp on any screen. The best default.</li><li><b>Very high</b> (about 216 dpi): for printing, zooming in, or running the image through OCR.</li></ul>
<p>Every page becomes its own JPG. Download the pages you need one by one, or all of them at once as a ZIP. To convert only a few pages, take them out first with <a href="../split-pdf/">Split PDF</a>.</p>''',
         [("Can I convert only some pages?", "Yes. Extract them with Split PDF first, then convert the smaller PDF."),
          ("Does it work with password-protected PDFs?", "No. Open the PDF with its password and save an unprotected copy first."),
          ("Is my PDF uploaded?", "No. Pages are drawn in your browser, so the file stays on your device.")])
    _add(T, "split-pdf", '''<h2>Examples</h2><ul><li><code>1-3</code>: pages 1, 2 and 3 in one new PDF.</li><li><code>1, 4, 7</code>: just those three pages.</li><li><code>2-10, 12</code>: drop page 1 and page 11.</li><li><b>Every page as a separate PDF</b>: one file per page, which you can download together as a ZIP.</li></ul>
<p>Pages are copied exactly, so text stays selectable and quality doesn't change.</p>''',
         [("How do I delete pages from a PDF?", "Type the pages you want to keep. For example, to remove page 5 from a 10-page PDF, type 1-4, 6-10."),
          ("Can I split a password-protected PDF?", "Remove the password first in a PDF reader, then split the unprotected copy.")])
    _add(T, "merge-pdf", '''<h2>Tips</h2><ul><li>Have photos or scans? Turn them into a PDF with <a href="../jpg-to-pdf/">JPG to PDF</a>, then merge.</li><li>Word documents: convert each one with <a href="../word-to-pdf/">Word to PDF</a> first.</li><li>Is the merged file too big for email? Shrink it with <a href="../compress-pdf/">Compress PDF</a>.</li></ul>''',
         [("Can I merge Word files?", "Convert each Word file to PDF first with Word to PDF, then merge the PDFs here."),
          ("Is my PDF uploaded?", "No. Merging happens in your browser.")])
    _add(T, "jpg-to-pdf", '''<h2>Page size options</h2><ul><li><b>A4</b>: the standard paper size in most countries.</li><li><b>Letter</b>: the standard in the US and Canada.</li><li><b>Same as image</b>: each page is exactly the size of its photo, with no white space.</li></ul>
<h2>Tips for scanning with your phone</h2><ul><li>Lay the page flat in daylight and hold the phone straight above it.</li><li>Crop away the table around the page before adding the photo.</li><li>Need the PDF under a size limit? Run it through <a href="../compress-pdf-to-200kb/">Compress PDF to 200KB</a>.</li></ul>''',
         [("How do I make the PDF smaller?", "Use Compress PDF on the result, or compress the photos first with the Image Compressor."),
          ("Can I add iPhone HEIC photos?", "Convert them with HEIC to JPG first, then add the JPGs here.")])
    _add(T, "heic-to-jpg", '''<h2>Why iPhones save HEIC photos</h2><p>Since iOS 11, iPhones save photos as HEIC (High Efficiency Image Container) by default. HEIC files are about half the size of JPG at similar quality, but many Windows PCs, Android phones, websites and upload forms can't open them. Converting to JPG makes them work everywhere.</p>
<p>Converting many photos? Choose them all at once and download the results together as a ZIP.</p>''',
         [("Will I lose quality?", "At 92% quality the JPG looks the same as the HEIC. The JPG file is usually bigger."),
          ("Does it work on Windows and Android?", "Yes, in any modern browser such as Chrome, Edge or Firefox.")])
    _add(T, "age-calculator", '''<h2>Common uses</h2><ul><li><b>Exam and job forms</b>: many notices give an age limit “as on” a cutoff date. Put that date in “Age on this date”.</li><li><b>School admission</b>: check a child's age on the admission date.</li><li><b>Retirement and pensions</b>: see exactly when an age is reached.</li></ul>''',
         [("How is age calculated for someone born on 29 February?", "In years without 29 February, the birthday is counted on 1 March."),
          ("Can I find my age on an exam's cutoff date?", "Yes. Set “Age on this date” to the cutoff date given in the notice.")])
    _add(T, "mp4-to-mp3", '''<h2>Which quality should I pick?</h2><ul><li><b>128 kbps</b>: speech, lectures and podcasts. About 1 MB per minute.</li><li><b>192 kbps</b>: music and general use. About 1.4 MB per minute.</li><li><b>320 kbps</b>: the best MP3 quality. About 2.4 MB per minute.</li></ul>
<h2>Supported files</h2><p>MP4, MOV, M4A and WebM work in most browsers. MKV and other formats work when your browser can play their audio. While converting, each minute of audio needs roughly 30–40 MB of memory, so recordings longer than about an hour can fail on phones; use a computer for those.</p>''',
         [("Can I convert a YouTube link?", "No. This tool converts files that are already on your device. Only convert videos you own or have permission to use.")])
