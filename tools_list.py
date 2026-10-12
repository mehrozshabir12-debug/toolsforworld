# Tool definitions for build.py (international tools). Each tool = one page.
HEIC = '<script src="https://cdn.jsdelivr.net/npm/heic2any@0.0.4/dist/heic2any.min.js"></script>'
TESS = '<script src="https://cdn.jsdelivr.net/npm/tesseract.js@5.1.0/dist/tesseract.min.js"></script>'
LAME = '<script src="https://cdn.jsdelivr.net/npm/lamejs@1.2.1/lame.min.js"></script>'
JSZIP = '<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>'
QRLIB = '<script src="https://cdn.jsdelivr.net/npm/qrcode-generator@1.4.4/qrcode.js"></script>'


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
         desc="Extract text from images, photos and screenshots with free OCR. Supports English, Urdu, Arabic and Hindi. Runs in your browser.",
         h1="Image to text (OCR)", lead="Pull the text out of a photo, scan or screenshot so you can copy and edit it.",
         body='''<h2>How to extract text from an image</h2><ol><li>Choose a photo or screenshot.</li><li>Pick the language of the text.</li><li>Press <b>Extract text</b>, then copy it or download a .txt file.</li></ol>
<h2>Tips for better results</h2><ul><li>Use a sharp, well-lit photo taken straight on.</li><li>Crop away everything except the text.</li><li>Printed text works much better than handwriting.</li></ul>''',
         faq=[("Which languages are supported?", "English, Urdu, Arabic and Hindi, plus English and Urdu together."),
              ("Can it read handwriting?", "Clear handwriting sometimes works, but OCR is built for printed text.")])

    # ================= Image =================
    tool(slug="compress-image", group="img", icon="img", name="Image Compressor", ftool="compress", libs="",
         card="Make JPG, PNG or WebP photos smaller in KB.",
         title="Image Compressor – Compress JPG & PNG to 100KB Free | Tools for World",
         desc="Compress JPG, PNG and WebP images online for free. Reduce photo size in KB for forms, email and websites. No upload.",
         h1="Image compressor", lead="Reduce photo file size for online forms, email and websites. Lower quality gives a smaller file.",
         body='''<h2>How to compress an image</h2><ol><li>Choose one or more photos.</li><li>Set the quality (70% keeps photos sharp for most uses).</li><li>Press <b>Compress</b> and save each smaller file.</li></ol><p>Need a photo under 100 KB or 50 KB for an application form? Lower the quality and set a maximum width such as 1200 px.</p>''',
         faq=[("Are my photos uploaded?", "No. Compression happens inside your browser.")])

    tool(slug="resize-image", group="img", icon="img", name="Image Resizer", ftool="resize", libs="",
         card="Change width and height in pixels or percent.",
         title="Image Resizer – Resize Photos in Pixels Free | Tools for World",
         desc="Resize images to any width and height in pixels or by percent while keeping the aspect ratio. Free and private.",
         h1="Image resizer", lead="Set an exact size in pixels or scale by percent. Keep the ratio so photos do not stretch.",
         body='''<h2>How to resize an image</h2><ol><li>Choose one or more images.</li><li>Enter a width or height, or a percentage.</li><li>Press <b>Resize</b>.</li></ol><p>Common sizes: 1080 × 1080 for Instagram posts, 1200 × 630 for link previews, 1920 × 1080 for HD.</p>''', faq=[])

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
         title="HEIC to JPG Converter – iPhone Photos to JPG Free | Tools for World",
         desc="Convert iPhone HEIC and HEIF photos to JPG for free. Batch convert in your browser with no upload.",
         h1="HEIC to JPG converter", lead="Convert iPhone photos (.heic / .heif) to JPG so they open on Windows, Android and any website.",
         body='''<h2>How to convert HEIC to JPG</h2><ol><li>Choose one or more .heic photos.</li><li>Set the quality.</li><li>Press <b>Convert to JPG</b>.</li></ol><p>Tip: on iPhone, Settings → Camera → Formats → “Most Compatible” saves new photos as JPG.</p>''',
         faq=[("Why can't I open HEIC files?", "HEIC is Apple's photo format. Many Windows PCs, Android phones and websites don't support it.")])

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
    for kb, use in ((20, "signature uploads and tiny form fields"), (50, "government and exam application forms"),
                    (100, "job portals, visa forms and email"), (200, "website uploads and online profiles"),
                    (500, "high-quality photos that still upload fast")):
        t(slug=f"compress-image-to-{kb}kb", group="img", icon="img", name=f"Compress Image to {kb}KB", ftool="compress", libs="",
          parent="compress-image", preset={"#tkb": kb},
          card=f"Make any photo under {kb} KB automatically.",
          title=f"Compress Image to {kb}KB Online Free – JPG Under {kb} KB | Tools for World",
          desc=f"Compress JPG, PNG or WebP images to {kb}KB or less in one click. Free, no upload: the photo is resized in your browser until it is just under {kb} KB.",
          h1=f"Compress image to {kb}KB", lead=f"Choose a photo and it is made just under {kb} KB automatically, keeping as much quality as possible. Ideal for {use}.",
          body=f'''<h2>How to compress a photo to {kb}KB</h2><ol><li>Choose your photo (JPG, PNG or WebP).</li><li>The target is already set to <b>{kb} KB</b>. Change it if you need a different size.</li><li>Press <b>Compress</b> and download the photo.</li></ol>
<h2>How it works</h2><p>The tool tries many quality levels and picks the highest one that stays under {kb} KB. If the photo is still too big at the lowest quality, it is scaled down a little at a time until it fits. Everything happens on your device, so your photo is never uploaded.</p>
<h2>Tips</h2><ul><li>Crop away empty background first: less detail means better quality at {kb} KB.</li><li>Most forms want JPG. Keep the output on JPG unless WebP is allowed.</li></ul>''',
          faq=[(f"Will my photo still look good at {kb}KB?", "For most photos, yes. The tool keeps the best quality that fits. Very large, detailed photos may be scaled down to fit."),
               (f"Can I compress several photos to {kb}KB at once?", "Yes. Choose several files and each one is compressed to the target size.")])

    for w, h, label, use in ((1080, 1080, "Instagram post", "square Instagram and Facebook posts"),
                             (1080, 1920, "Instagram story / Reels", "Instagram stories, Reels, TikTok and WhatsApp status"),
                             (1200, 630, "Facebook & link preview", "Facebook posts, link previews and Open Graph images"),
                             (1280, 720, "YouTube thumbnail", "YouTube thumbnails and HD slides"),
                             (600, 600, "passport photo 2×2 inch", "online US passport and visa photo uploads (2×2 inch at 300 dpi)"),
                             (400, 400, "profile picture", "profile pictures on LinkedIn, Discord, forums and apps")):
        t(slug=f"resize-image-to-{w}x{h}", group="img", icon="img", name=f"Resize to {w}×{h}", ftool="resize", libs="",
          parent="resize-image", preset={"#rm": "px", "#rw": w, "#rh": h, "#rk": False, "#rf": "crop"},
          card=f"{label}: exactly {w}×{h} px.",
          title=f"Resize Image to {w}x{h} Pixels Online Free ({label}) | Tools for World",
          desc=f"Resize any photo to exactly {w}×{h} pixels for {use}. Crop to fill or add a border. Free and private: works in your browser.",
          h1=f"Resize image to {w}×{h} pixels", lead=f"Get a photo that is exactly {w} × {h} px for {use}. Choose crop to fill, or fit with a white border.",
          body=f'''<h2>How to resize to {w}×{h}</h2><ol><li>Choose one or more images.</li><li>The size is already set to <b>{w} × {h}</b>.</li><li>Pick <b>Crop to fill</b> (no empty space) or <b>Fit with white border</b> (nothing cut off), then press <b>Resize</b>.</li></ol>
<h2>Why exact size matters</h2><p>Platforms crop or blur images that are the wrong shape. Uploading at exactly {w} × {h} px keeps your photo sharp and framed the way you want.</p>''',
          faq=[("Will my photo be stretched?", "No. Crop to fill keeps the proportions and trims the edges; Fit with white border keeps the whole photo and adds a border.")])

    for code, lang, extra in (("urd", "Urdu", "Nastaliq printed text from books, newspapers and screenshots"),
                              ("ara", "Arabic", "printed Arabic text, documents and screenshots"),
                              ("hin", "Hindi", "printed Devanagari text from documents and screenshots")):
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
