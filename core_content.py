"""Extra, page-specific help content for the main tool pages (added 2026-10-19 after the AdSense
"low value content" review). Each entry is unique to its tool: real use cases, limits, troubleshooting
and format background. Keep claims true to what the tool actually does (see assets/files.js / calc.js)."""

CORE = {
"pdf-to-word": ('''<h2>When PDF to Word is the right choice</h2><p>Use it when you need to <b>edit the words</b> of a document you only have as a PDF: updating an old CV, reusing paragraphs from a report, fixing a typo in a letter, or pulling notes out of lecture slides. You get a .docx file with the text in reading order, which you can restyle in Word, Google Docs or LibreOffice Writer.</p>
<p>If you need the PDF to look exactly the same, editing it as Word is the wrong route: fonts, columns and image positions are rebuilt from scratch, not copied. In that case keep the PDF and add notes or a signature in a PDF reader instead.</p>
<h2>Checking the result</h2><ul><li>Scroll through quickly and look for words joined together or split across lines. Multi-column layouts are the usual cause.</li><li>Re-apply headings with Word's built-in styles so the document has a proper outline.</li><li>Add pictures back by hand from the original file if you need them.</li></ul>''',
 [("Can I convert a PDF on my phone?", "Yes. It works in the browser on Android and iPhone. Open the .docx in the Word or Google Docs app."),
  ("Why are some words in the wrong order?", "PDFs store text as positioned fragments. Tables, columns and text boxes can come out in an unexpected order, so check those parts.")]),

"word-to-pdf": ('''<h2>Why send a PDF instead of a Word file?</h2><p>A PDF looks the same on every phone and computer, it can't be changed by accident, and almost every job portal, university system and government form accepts it. That's why CVs, cover letters, assignments and signed letters are normally sent as PDF.</p>
<h2>Getting the best result</h2><ul><li>Use common fonts (Calibri, Arial, Times New Roman). Unusual fonts may be replaced.</li><li>Keep the layout simple: one column, normal tables and pictures placed "in line with text" convert most faithfully.</li><li>Check page breaks in the PDF preview before you send it, especially for one-page CVs.</li><li>Name the file clearly, for example <code>Firstname-Lastname-CV.pdf</code>.</li></ul>
<p>Need the final PDF smaller for an upload limit? Run it through <a href="../compress-pdf/">Compress PDF</a>. Need to join it with a transcript or certificate? Use <a href="../merge-pdf/">Merge PDF</a>.</p>''',
 [("Will my hyperlinks still work?", "Use the “Print / Save as PDF” option for a PDF with selectable text; links usually survive that route. The direct conversion produces page images."),
  ("Can I convert Google Docs?", "Yes. In Google Docs choose File → Download → Microsoft Word (.docx), then convert that file here.")]),

"compress-pdf": ('''<h2>Which level should I pick?</h2><ul><li><b>Light</b>: for documents people will read on screen or print, such as contracts or reports with photos. Keeps the most detail.</li><li><b>Recommended</b> or <b>Strong</b>: for scanned forms, ID copies and receipts that only need to be readable. Usually the best balance for upload portals.</li><li><b>Extreme</b>: only when a portal has a very small limit. Small print may become hard to read, so zoom in and check before you submit.</li></ul>
<h2>Why some PDFs barely shrink</h2><p>A PDF made directly from Word or a website is mostly text and vector shapes, which are already tiny. Most of the size in a big PDF comes from photos and scans, and those are what this tool squeezes. If your file is text-only and still too large, it may contain embedded fonts or a few huge images; splitting it into parts with <a href="../split-pdf/">Split PDF</a> can also help.</p>
<p>Need a fixed size? Use a preset such as <a href="../compress-pdf-to-1mb/">1 MB</a>, <a href="../compress-pdf-to-500kb/">500 KB</a> or <a href="../compress-pdf-to-200kb/">200 KB</a>.</p>''',
 [("Will compressing remove my signature or stamp?", "No. Everything visible on the page is kept, only at a lower image quality."),
  ("Can I still search the text after compressing?", "No. Pages become images, so the text is no longer selectable. Keep the original if you need searchable text.")]),

"merge-pdf": ('''<h2>Common reasons to merge PDFs</h2><ul><li>Job and university applications that accept a single file: CV, cover letter, transcripts and certificates in one PDF.</li><li>Visa and government applications: passport scan, bank statement and forms in the order the checklist asks for.</li><li>Expense claims: several receipts in one document for your manager or accountant.</li><li>Study notes: lecture handouts for a whole unit in one file.</li></ul>
<h2>Tips</h2><p>Put the files in the exact order the instructions ask for, and add a cover page if the portal wants one. After merging, check the total size: many portals cap uploads at 2–5 MB. If yours is larger, run the merged file through <a href="../compress-pdf/">Compress PDF</a>. To take a few pages back out, use <a href="../split-pdf/">Split PDF</a>.</p>
<p>Have photos or phone scans instead of PDFs? Turn them into a PDF first with <a href="../jpg-to-pdf/">JPG to PDF</a>, then merge.</p>''',
 [("Does merging change the page quality?", "No. Pages are copied as they are, so text stays sharp and searchable."),
  ("Can I merge PDFs on my phone?", "Yes. Choose several files from your Files app or Downloads, reorder them and merge.")]),

"split-pdf": ('''<h2>What you can do with it</h2><ul><li><b>Extract a few pages</b>: send only the signed page of a contract, or one chapter of a textbook you own.</li><li><b>Remove pages</b>: list every page except the ones you don't want, for example <code>1-4, 6-12</code> to drop page 5.</li><li><b>Split every page</b>: turn a scanned stack of forms into separate files, one per page.</li><li><b>Reorder</b>: list pages in a new order, like <code>3, 1, 2</code>.</li></ul>
<h2>Writing page ranges</h2><p>Separate items with commas and use a dash for ranges. <code>2-5</code> means pages 2, 3, 4 and 5. Spaces are fine. Page numbers are the real position in the file, which can differ from the numbers printed on the pages if the document has a cover or roman-numbered intro.</p>
<p>Want to combine the pieces with other files later? Use <a href="../merge-pdf/">Merge PDF</a>.</p>''',
 [("Is the original file changed?", "No. Your original PDF stays as it is; you download new files."),
  ("Can I split a password-protected PDF?", "Remove the password first by opening it in a PDF reader and saving a copy without protection.")]),

"jpg-to-pdf": ('''<h2>Making a clean PDF from phone photos</h2><ul><li>Photograph documents flat, in daylight, from straight above, so the page isn't skewed.</li><li>Crop away the table or floor around the page before adding it.</li><li>Keep pages in order: the arrows let you fix the order before you create the PDF.</li><li>Choose <b>A4</b> for most countries and <b>Letter</b> for the US and Canada, so the PDF prints at the right size.</li></ul>
<h2>Typical uses</h2><p>Submitting handwritten homework, sending receipts for reimbursement, sharing ID or certificate copies, and keeping a digital copy of letters. Phone photos are large, so a 10-page PDF can easily pass 20 MB; if a form has a limit, run the result through <a href="../compress-pdf/">Compress PDF</a>.</p>
<p>iPhone photos in HEIC format? Convert them first with <a href="../heic-to-jpg/">HEIC to JPG</a>.</p>''',
 [("How many images can I put in one PDF?", "There's no fixed limit. Dozens work fine; very large batches are slower on phones."),
  ("Will the photo quality drop?", "The images are placed into the PDF as they are, so the quality matches your photos.")]),

"pdf-to-jpg": ('''<h2>Why convert PDF pages to images?</h2><ul><li>Post a page on social media or in a chat app that doesn't preview PDFs.</li><li>Upload a document to a form that only accepts JPG.</li><li>Put a slide or a chart into a presentation or a design.</li><li>Make a quick thumbnail of a report's cover page.</li></ul>
<h2>Choosing the quality</h2><p>Higher quality renders the page at more pixels, which keeps small text readable but makes larger files. For reading on a phone or posting online, a medium setting is plenty. For printing, or when the page has fine print you need to zoom into, use the highest setting.</p>
<p>Need the JPGs smaller afterwards? Use the <a href="../compress-image/">Image Compressor</a>. Need the text from the page rather than a picture of it? Try <a href="../pdf-to-word/">PDF to Word</a>.</p>''',
 [("Is every page converted?", "Yes, each page becomes its own JPG, which you can save one by one or together."),
  ("Is my PDF uploaded?", "No. Pages are drawn by your browser on your device.")]),

"image-to-text": ('''<h2>What OCR is good for</h2><p>OCR (optical character recognition) turns the letters in a picture into text you can copy. People use it to grab text from screenshots, copy quotes from a photographed book page, digitise printed letters and notices, or pull a phone number or address from a photo.</p>
<h2>Why results are sometimes wrong</h2><ul><li><b>Wrong language selected</b>: pick the language the text is written in; this matters most for Urdu, Arabic, Hindi and Chinese.</li><li><b>Blurry or tilted photo</b>: retake it closer, with steady hands and good light.</li><li><b>Busy background</b>: text on patterns or photos is harder to read than black on white.</li><li><b>Stylised fonts and handwriting</b>: decorative fonts and joined-up writing often fail.</li></ul>
<p>Always proofread names, numbers and dates before you use the text. Have a scanned PDF instead of an image? Save the pages as images with <a href="../pdf-to-jpg/">PDF to JPG</a> first.</p>''',
 [("Is my image uploaded for OCR?", "No. The recognition engine runs in your browser, so the image stays on your device."),
  ("Why is the first run slower?", "The language data downloads the first time you use a language; later runs are faster.")]),

"compress-image": ('''<h2>Quality vs. file size</h2><p>JPG and WebP compression throws away detail the eye barely notices. Between 60% and 80% quality, most photos look the same on a phone screen but are several times smaller than the original. Below about 40% you start to see blocky patches, especially in skies and skin.</p>
<h2>Which format compresses best?</h2><ul><li><b>JPG</b>: best for photos; works everywhere.</li><li><b>WebP</b>: often smaller than JPG at the same quality; good for websites.</li><li><b>PNG</b>: lossless, so photos stay big. Screenshots and logos are fine as PNG; for photos convert with <a href="../png-to-jpg/">PNG to JPG</a> first.</li></ul>
<h2>Typical targets</h2><p>Exam and government forms often ask for photos under 20–100 KB and signatures under 10–30 KB. Email works best under 1–2 MB per photo, and website images load fastest under 200 KB.</p>''',
 [("What if my image is already small?", "If compressing would make the file bigger, the tool keeps your original and tells you, so you never get a larger \"compressed\" file."),
  ("Can I compress many photos at once?", "Yes. Choose several files and download them one by one or as a ZIP.")]),

"resize-image": ('''<h2>Pixels, aspect ratio and cropping</h2><p>Resizing changes how many pixels wide and tall an image is. With “keep ratio” on, you set one side and the other follows, so faces and logos don't stretch. If you need a different shape, such as a square from a portrait photo, the picture has to be cropped or padded, because squeezing it would distort it.</p>
<h2>Popular sizes</h2><ul><li><a href="../resize-image-to-1080x1080/">1080 × 1080</a> Instagram square post · <a href="../resize-image-to-1080x1350/">1080 × 1350</a> portrait post</li><li><a href="../resize-image-to-1080x1920/">1080 × 1920</a> Stories, Reels and TikTok</li><li><a href="../resize-image-to-1280x720/">1280 × 720</a> YouTube thumbnail · <a href="../resize-image-to-1200x630/">1200 × 630</a> link previews</li><li><a href="../resize-image-to-1584x396/">1584 × 396</a> LinkedIn banner · <a href="../resize-image-to-1500x500/">1500 × 500</a> X header</li></ul>
<p>Unsure what resolution means? Read <a href="../guides/image-resolution-sizes-explained/">image resolution sizes explained</a>.</p>''',
 [("Does resizing reduce the file size?", "Making an image smaller in pixels usually makes the file smaller too. For an exact KB limit, use the Image Compressor."),
  ("Can I resize several images to the same size?", "Yes. Choose several files and they are all resized with the same settings.")]),

"remove-background": ('''<h2>Where a transparent background helps</h2><ul><li><b>Product photos</b> for online shops and marketplaces that want a clean white or plain background.</li><li><b>Profile pictures</b> on a coloured circle for LinkedIn, CVs or team pages.</li><li><b>Designs</b>: put a person or object onto a poster, thumbnail or card.</li><li><b>Stickers</b> for chat apps.</li></ul>
<h2>Getting a clean cut-out</h2><p>The AI separates the main subject from everything else, so it works best with one clear subject, good light and some contrast with the background. Fine hair, glass, smoke and objects the same colour as the wall are the hardest parts; zoom in on the edges before you use the result in print.</p>
<p>The output is a PNG, because JPG can't store transparency. Need a white background instead? Open the PNG and convert it with <a href="../png-to-jpg/">PNG to JPG</a>, which fills transparent areas with white.</p>''',
 [("Is my photo sent to an AI server?", "No. The AI model runs inside your browser on your own device."),
  ("Can I use it for passport photos?", "Many passport rules ban edited backgrounds. Check the rules first, or take the photo against a plain light wall.")]),

"png-to-jpg": ('''<h2>PNG vs JPG in short</h2><p><b>PNG</b> stores every pixel exactly and supports transparency, which is ideal for screenshots, logos and graphics with sharp edges. <b>JPG</b> uses lossy compression that suits photos, making files far smaller. A photo saved as PNG can be 3–10 times bigger than the same photo as JPG.</p>
<h2>When to convert</h2><ul><li>A form or website only accepts JPG.</li><li>A PNG photo is too big to email or upload.</li><li>You want to put an image with a transparent background on white.</li></ul>
<h2>When not to</h2><p>Keep PNG for logos and images you still need transparent, and for screenshots with small text, where JPG can add faint blur around letters.</p>
<p>Need the JPG under a certain size? Use the <a href="../compress-image/">Image Compressor</a> next.</p>''',
 [("What happens to the transparent parts?", "They become white, since JPG can't store transparency."),
  ("Can I convert several PNGs at once?", "Yes. Choose multiple files and download them separately or as a ZIP.")]),

"jpg-to-png": ('''<h2>Good reasons to convert JPG to PNG</h2><ul><li>An app, printer or upload form specifically asks for PNG.</li><li>You'll edit the image several times. Re-saving a JPG again and again adds a little more blur each time; PNG doesn't lose anything when re-saved.</li><li>You're adding the picture to a design project that works in PNG.</li></ul>
<h2>What conversion can't do</h2><p>Converting doesn't restore detail that the JPG already lost, and it doesn't add a transparent background: the background stays as it is. For a cut-out, use the <a href="../remove-background/">Background Remover</a>, which produces a transparent PNG directly.</p>
<p>Expect the PNG to be noticeably larger than the JPG. If you only need a smaller file, stay with JPG and use the <a href="../compress-image/">Image Compressor</a> instead.</p>''',
 [("Will the PNG look better than the JPG?", "It will look the same. PNG keeps exactly what is in the JPG; it can't add back lost detail."),
  ("Is my photo uploaded?", "No. The conversion happens in your browser.")]),

"webp-to-jpg": ('''<h2>Why you end up with WebP files</h2><p>Many websites serve images as WebP because the files are smaller and pages load faster. When you right-click and save a picture, it often lands on your device as <code>.webp</code>. Newer browsers and phones open it, but older photo editors, some printers, and many upload forms still expect JPG or PNG.</p>
<h2>How to use the converted files</h2><ul><li>Edit them in any photo app, including older versions of Photoshop and Windows Photos.</li><li>Upload them to forms and marketplaces that reject WebP.</li><li>Put them into Word, PowerPoint or a PDF with <a href="../jpg-to-pdf/">JPG to PDF</a>.</li></ul>
<p>Only use images you have the right to use; saving a picture from a website doesn't give you permission to reuse it.</p>''',
 [("Is quality lost when converting WebP to JPG?", "A little, as with any JPG save, but at high quality the difference isn't visible."),
  ("Do animated WebP files work?", "Only the first frame is converted, since JPG can't store animation.")]),

"heic-to-jpg": ('''<h2>What is HEIC?</h2><p>Since iOS 11, iPhones save photos as HEIC (High Efficiency Image Container) by default. The files are about half the size of JPG at similar quality, which saves storage. The catch is support: many Windows PCs, older Android phones, upload forms and printing kiosks don't open them.</p>
<h2>Ways around HEIC</h2><ul><li><b>Convert here</b> when you already have HEIC files on a computer or phone.</li><li><b>Share as JPG from iPhone</b>: when you email or AirDrop photos, iOS often converts them automatically, but not always when you copy files directly by cable.</li><li><b>Change the camera setting</b> to “Most Compatible” if you regularly need JPG.</li></ul>
<p>Photos keep their pixel size when converted, so a 12-megapixel iPhone photo stays 12 megapixels.</p>''',
 [("Do I lose quality converting HEIC to JPG?", "At high quality settings the difference is not visible in normal use, though JPG files are larger."),
  ("Can I convert Live Photos?", "The still image of a Live Photo converts; the short video part does not.")]),

"passport-photo-maker": ('''<h2>Common photo sizes</h2><ul><li><b>35 × 45 mm</b>: UK, Schengen countries, Australia, India, Pakistan and many others.</li><li><b>2 × 2 inch (51 × 51 mm)</b>: US passports and visas.</li><li><b>33 × 48 mm</b>: China visa.</li></ul>
<p>See every country's rules in our <a href="../guides/passport-photo-size-by-country/">passport photo size guide</a>, or open a ready preset: <a href="../us-passport-photo/">US</a>, <a href="../uk-passport-photo/">UK</a>, <a href="../india-passport-photo/">India</a>, <a href="../australia-passport-photo/">Australia</a>, <a href="../canada-passport-photo/">Canada</a>, <a href="../schengen-visa-photo/">Schengen visa</a>.</p>
<h2>Why photos get rejected</h2><ul><li>Shadows on the face or background, or a background that isn't plain.</li><li>Head too small or too large in the frame.</li><li>Glasses with glare, or a smile showing teeth where a neutral face is required.</li><li>Printing at the wrong scale. Always print at 100% / actual size, never “fit to page”.</li></ul>''',
 [("Can I use this photo for an online application?", "Yes. Many online applications want a digital photo instead of a print; download the single photo and check their pixel and KB limits."),
  ("Is my photo uploaded?", "No. Cropping and the print sheet are made in your browser.")]),

"qr-code-generator": ('''<h2>Static QR codes that never expire</h2><p>The code made here stores your link or text directly inside the pattern. There's no redirect through our server, so it keeps working as long as the link itself works, with no subscription. The trade-off is that you can't change where it points after printing; to change it, make a new code.</p>
<h2>Making a code that scans every time</h2><ul><li>Keep strong contrast: dark code on a light background. Light-on-dark codes fail on some phones.</li><li>Leave a clear margin around the code.</li><li>Print it at least 2 × 2 cm, larger if people scan from a distance.</li><li>Use higher error correction if the code may get scratched or partly covered.</li><li>Test it with two different phones before printing hundreds.</li></ul>
<p>Ready presets: <a href="../wifi-qr-code-generator/">Wi-Fi QR code</a> and <a href="../whatsapp-qr-code-generator/">WhatsApp QR code</a>.</p>''',
 [("Can I track how many people scan it?", "No. Static codes don't pass through a server, so there is no tracking. That's also what keeps them private."),
  ("Can I use the QR code commercially?", "Yes. Codes you make here are yours to use on menus, flyers, packaging and cards.")]),

"word-counter": ('''<h2>Typical word counts</h2><ul><li>University essay: often 1,500–3,000 words, usually with a ±10% allowance; check your unit guide.</li><li>Abstract: 150–300 words.</li><li>Cover letter: 250–400 words, about one page.</li><li>Blog post: 800–2,000 words.</li><li>Speech: about 130–150 words per minute of speaking.</li></ul>
<h2>How words are counted</h2><p>Anything separated by spaces counts as a word, so “well-known” is one word and “U.S.” is one word. Numbers count as words. Different apps can disagree by a few words because of hyphens, dashes and symbols, so if a deadline system counts differently, use their number for the final check.</p>
<p>Need only characters, for a post or bio? Try the <a href="../character-counter/">Character Counter</a>.</p>''',
 [("Do references count towards my word limit?", "It depends on your course; many exclude the reference list. Check the assignment brief."),
  ("Does it work with Urdu, Arabic or Hindi text?", "Yes. Words in any language separated by spaces are counted.")]),

"password-generator": ('''<h2>How long should a password be?</h2><p>Each extra character multiplies the number of guesses an attacker needs. A random 8-character password can be cracked quickly with modern hardware if a site's password database leaks, while a random 16-character one with mixed characters is far beyond practical guessing. For important accounts such as email and banking, 16–20 characters is a good habit.</p>
<h2>Using generated passwords safely</h2><ul><li>Save each one in a password manager (the one built into your browser or phone works) instead of a note or screenshot.</li><li>Turn on two-step verification for email, banking and social accounts.</li><li>Never reuse a password: one leak then unlocks every account that shares it.</li><li>Turn on “avoid look-alikes” if you'll ever type the password by hand.</li></ul>''',
 [("Can you see the passwords I generate?", "No. They're created in your browser and never sent over the internet."),
  ("Should I include symbols?", "Yes when the site allows them. If a site rejects some symbols, turn them off and add a few characters of length instead.")]),

"age-calculator": ('''<h2>Where exact age matters</h2><ul><li><b>Application forms</b> that ask for age in years and months on a specific date, such as school admissions or exams with an age limit.</li><li><b>Eligibility cut-offs</b>, for example “must be under 30 on 1 January”. Set “Age on this date” to that cut-off date.</li><li><b>Milestones</b>: how many days old you are, or how long until your next birthday.</li></ul>
<h2>Leap years and month lengths</h2><p>Months have different lengths, so “1 month” isn't a fixed number of days. The calculator moves forward full calendar months, then counts the days left, which matches how ages are worked out on official forms. Someone born on 29 February is counted as turning a year older on 1 March in non-leap years; some countries use 28 February legally, so check if it matters for your form.</p>''',
 [("Can I calculate the time between any two dates?", "Yes. Enter the start date as the date of birth and the end date in “Age on this date”."),
  ("Is my date of birth stored?", "No. The calculation runs in your browser.")]),

"percentage-calculator": ('''<h2>Everyday examples</h2><ul><li><b>Exam marks</b>: 42 out of 60 is 42 ÷ 60 × 100 = 70%.</li><li><b>Pay rise</b>: from 2,500 to 2,750 is a 10% increase.</li><li><b>Tax</b>: adding 10% GST to 150 gives 165; adding 18% to 1,000 gives 1,180.</li><li><b>Sale</b>: 25% off 1,000 is 750. See also the <a href="../discount-calculator/">Discount Calculator</a>.</li></ul>
<h2>Percent vs. percentage points</h2><p>If an interest rate rises from 4% to 5%, it went up by 1 percentage point, but by 25% in relative terms. News reports mix these up often, so check which one is meant.</p>
<p>A rise and a fall of the same percent don't cancel out: 100 up 20% is 120, and 120 down 20% is 96.</p>''',
 [("How do I find the original price before a discount?", "Divide the sale price by (1 − discount ÷ 100). For 80 after 20% off: 80 ÷ 0.8 = 100."),
  ("How do I remove tax from a price?", "Divide by (1 + tax ÷ 100). For 110 including 10% tax: 110 ÷ 1.1 = 100.")]),

"mp4-to-mp3": ('''<h2>What people use it for</h2><ul><li>Saving the audio of a lecture or meeting you recorded, to listen to on the go.</li><li>Turning a voice note or interview video into audio for transcription.</li><li>Extracting music or narration from your own video project.</li></ul>
<h2>Choosing a bitrate</h2><p>Bitrate decides quality and file size. Speech sounds clear at 96–128 kbps and an hour-long lecture stays fairly small. Music sounds good at 192 kbps, and 256–320 kbps is close to the original for most listeners but makes bigger files. A higher bitrate can't improve audio that was poor in the video.</p>
<h2>Supported files</h2><p>MP4 and MOV from phones and cameras, and WebM from screen recorders and browsers usually work. If a file won't open, it may use an unusual audio codec; try exporting it again from the app that made it.</p>''',
 [("Is my video uploaded?", "No. The audio is extracted and encoded on your device."),
  ("Can I convert on iPhone?", "Yes, in Safari. Longer videos need more memory, so use a computer for very large files.")]),

"character-counter": ('''<h2>Why character limits differ between apps</h2><p>Some platforms count every Unicode code unit, so an emoji or an Urdu, Arabic or Hindi letter with marks can count as two or more. Others count what you see. If a post is close to the limit, leave a few characters spare, and check the count shown in the app itself before posting.</p>
<h2>Writing within a limit</h2><ul><li>Lead with the most important words: search results and previews cut off the end.</li><li>Replace long phrases with short ones (“in order to” → “to”).</li><li>Remove filler words like “really”, “very” and “just”.</li><li>Use numbers instead of words where it reads naturally.</li></ul>
<p>Counting words for an essay instead? Use the <a href="../word-counter/">Word Counter</a>.</p>''',
 [("Are line breaks counted?", "Yes. Line breaks count as characters, as they do on most platforms."),
  ("What is the limit for an SMS?", "160 characters with basic Latin letters, or 70 when the message contains emoji or non-Latin script.")]),

"discount-calculator": ('''<h2>Spotting a real bargain</h2><ul><li><b>Compare the final price</b>, not the percent. 30% off an inflated price can cost more than 10% off elsewhere.</li><li><b>“Buy one, get one 50% off”</b> is 25% off both items, not 50%.</li><li><b>Price per unit</b>: for groceries, divide the price by weight or count to compare pack sizes.</li><li><b>Shipping and fees</b> can wipe out a small discount; add them before comparing.</li></ul>
<h2>Discounts and tax</h2><p>In most places the discount is applied first and tax is added to the reduced price. If you see a price including tax, the saving shown here is also tax-inclusive. For adding or removing tax, use the <a href="../percentage-calculator/">Percentage Calculator</a>.</p>''',
 [("How much do I save with 15% off 2,400?", "15% of 2,400 is 360, so you pay 2,040."),
  ("Is 50% off then 20% off the same as 70% off?", "No. It's 60% off in total: 100 → 50 → 40.")]),

"wifi-qr-code-generator": ('''<h2>Where to put a Wi-Fi QR code</h2><ul><li>Guest room, living room or the fridge door at home.</li><li>Café tables, reception desks and waiting rooms.</li><li>Holiday rentals and Airbnb welcome books.</li><li>Office meeting rooms with a separate guest network.</li></ul>
<h2>Keep your network safe</h2><p>Anyone who scans the code can join and see the password, so only display it where you'd happily tell people the password. For a shop or rental, set up a separate <b>guest network</b> on your router and use that in the code. If you change the Wi-Fi password, make and print a new code.</p>
<p>The network name and password are case-sensitive, and special characters such as <code>;</code>, <code>,</code>, <code>:</code> or <code>\\</code> need a backslash in front of them inside the code.</p>''',
 [("Do guests need an app to scan it?", "No. The built-in camera on modern iPhones and Android phones reads Wi-Fi codes."),
  ("Does it work for hidden networks?", "Yes. Add H:true; just before the final ;; in the box.")]),

"whatsapp-qr-code-generator": ('''<h2>Ideas for using a WhatsApp QR code</h2><ul><li><b>Shops and home businesses</b>: on the counter, packaging or receipts so customers can order or ask questions.</li><li><b>Restaurants</b>: on menus for takeaway orders.</li><li><b>Tutors and freelancers</b>: on business cards and flyers.</li><li><b>Events</b>: on posters so people can register by message.</li></ul>
<h2>Writing the pre-filled message</h2><p>Keep it short and specific, for example “Hi, I'd like to order” or “Hello, I saw your flyer”. Spaces in the message are fine in the box; the link still works. The customer sees the message ready to send and can edit it before pressing send, so nothing is sent without their action.</p>
<p>Use the full number with country code and no leading zero: Pakistan 0300 1234567 becomes <code>923001234567</code>.</p>''',
 [("Does it work with WhatsApp Business?", "Yes. wa.me links open chats with both normal and Business accounts."),
  ("Can people see my number?", "Yes. The number is part of the link, so anyone who scans the code can see it.")]),
}


def enrich(T):
    for t in T:
        c = CORE.get(t["slug"])
        if c:
            html_, faqs = c
            t["body"] = t["body"] + "\n" + html_
            t["faq"] = list(t.get("faq", [])) + faqs
