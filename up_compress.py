"""Unique content: compress image, compress PDF and JPG to PDF size presets."""

P = {}

# ---------------- compress image to <size> ----------------
P["compress-image-to-10kb"] = ('''<h2>What 10 KB can and can't hold</h2>
<p>10 KB is about the weight of one paragraph of formatted text in a Word file, so a photo has to be tiny to fit: roughly 200 × 100 pixels for a signature, or about 120 × 150 pixels for a face. That is enough for a portal to display a thumbnail, and it's why these limits mostly appear for signatures and very old government systems.</p>
<p>Black ink on white paper is the easiest thing to squeeze into 10 KB, because large areas of plain white cost almost nothing. A colourful selfie is the hardest. If you're asked for a 10 KB photo of a face, crop very tightly to the head first.</p>''',
[("Why does my 10 KB signature look pixelated?", "The image was scaled down a lot to fit. Crop out the empty paper so the signature fills the picture, and the strokes keep more pixels.")])

P["compress-image-to-20kb"] = ('''<h2>Signatures, thumb prints and small photos at 20 KB</h2>
<p>At 20 KB a signature can be about 300–400 pixels wide and still look crisp, and a cropped face photo of around 200 × 230 pixels stays recognisable. Recruitment and exam portals often pair a 20 KB signature limit with a separate 50 KB photo limit, so keep the two files apart and name them clearly.</p>
<p>Scanned signatures sometimes look grey and smudgy. Before compressing, increase the contrast in your phone's photo editor so the paper turns white and the ink dark: the file becomes smaller and the signature sharper at the same time.</p>''',
[("My form says 10–20 KB. What target should I use?", "Leave the target at 20 KB. The result lands just under 20 KB, inside the range. If the form also gives pixel dimensions, resize to those first.")])

P["compress-image-to-30kb"] = ('''<h2>Exam and admit-card photos</h2>
<p>A 30 KB face photo is common on school, college and exam applications, where the picture is later printed small on an admit card or ID. Printed at 3.5 × 4.5 cm, a 30 KB photo of around 300 × 380 pixels looks fine; nobody can see the difference from a larger file at that size.</p>
<p>What gets photos rejected at this size is rarely the KB number. It's a dark background, a face too small in the frame or a sideways crop. Fix those before compressing, because the portal may check the shape and the size separately.</p>''',
[("Can a colour photo be 30 KB?", "Yes. A cropped head-and-shoulders photo in colour fits under 30 KB easily. You don't need to convert it to black and white.")])

P["compress-image-to-50kb"] = ('''<h2>Why 50 KB is the most common photo limit</h2>
<p>Many government, bank and exam portals were built years ago, when servers stored thousands of applicant photos and storage was expensive. A limit of 50 KB keeps every applicant's photo small while still being clear enough to identify someone, and the number has stuck.</p>
<p>A typical phone photo is 2–5 MB, about 40 to 100 times too big. The tool first lowers JPG quality, which removes detail you can't see, and only reduces the pixel size if quality alone isn't enough. A cropped face photo usually reaches 50 KB while still around 600 pixels wide.</p>''',
[("Is 50 KB enough for a passport-size photo?", "Yes. A passport-size face photo looks sharp at 50 KB on screen and when printed at 3.5 × 4.5 cm.")])

P["compress-image-to-100kb"] = ('''<h2>100 KB on a phone, step by step</h2>
<p>On Android and iPhone alike, choose the photo straight from your gallery, wait for the size to appear under the file name, and download. The new file is saved next to your other downloads, usually named with "compressed" added, so you can tell it apart from the original when the form asks you to pick a file.</p>
<h2>Photos for job portals and visa forms</h2>
<p>100 KB is a typical limit on job sites, embassy forms and university applications. For a face photo it's comfortable: you'll usually keep 800–1000 pixels on the long side with no visible loss. It gets tight with whole-page document photos, like a bank statement or certificate photographed with a phone, where small print needs pixels.</p>
<p>For documents, flatten the page, photograph it straight from above in good light and crop to the edges of the paper. A sharp, well-lit document photo at 100 KB is easier to read than a blurry one at 1 MB.</p>''',
[("How many KB is a normal phone photo?", "Usually 2–6 MB, which is 2,000–6,000 KB. Getting to 100 KB means making it 20 to 60 times smaller, which the tool does automatically.")])

P["compress-image-to-200kb"] = ('''<h2>200 KB for profiles and online shops</h2>
<p>200 KB is where photos start to look properly good on screen. Profile photos on professional sites, product photos for small shops and photos in blog posts commonly target this size, because they need to look sharp but also load quickly on a phone.</p>
<p>Product photos: shoot on a plain background and crop close to the item. Plain backgrounds compress very efficiently, so more of the 200 KB goes to the product itself. For a set of photos, compress them together so every image in the listing ends up a similar size.</p>''',
[("Will 200 KB look good on a website?", "Yes, for images up to about 1600 pixels wide. For full-screen banners on large monitors, 300–500 KB may look better.")])

P["compress-image-to-500kb"] = ('''<h2>Good-quality photos that still upload fast</h2>
<p>500 KB keeps photos detailed enough to zoom into, which matters for things like property listings, rental applications, insurance claims and car sale ads, where the other person wants to look closely at a scratch or a room. At this size a photo can usually stay at 2000 pixels or more on the long side.</p>
<p>If a form limits the total upload, for example 5 MB for all photos together, divide the limit by the number of photos you need to send. Ten photos for a 5 MB limit means about 500 KB each.</p>''',
[("Can I see any quality difference at 500 KB?", "Rarely on a phone or laptop screen. Differences only show if you zoom far into fine detail such as leaves, hair or small text.")])

P["compress-image-to-1mb"] = ('''<h2>Large photos under a 1 MB limit</h2>
<p>A 1 MB limit is easy for most photos: phone photos are usually 2–5 MB, so they only need to lose half to three quarters of their weight, which barely changes how they look. This is a good choice when a site rejects your original photo as "too large" but you still want the best possible quality.</p>
<p>Screenshots are different. PNG screenshots of a phone screen can be bigger than 1 MB because PNG keeps every pixel exactly. Saving them as JPG at the 1 MB target shrinks them a lot, but very small text can get slightly soft, so check the result.</p>''',
[("Is 1 MB the same as 1000 KB?", "Close. This tool counts 1 MB as 1024 KB, which is what most upload forms use. Aiming just under that passes either way.")])

P["compress-image-to-2mb"] = ('''<h2>When a 2 MB limit catches you out</h2>
<p>Modern phone cameras save photos of 3–8 MB, so a 2 MB limit on a form can reject a photo that looks perfectly normal. Compressing to 2 MB keeps nearly all the detail: a 12-megapixel photo usually fits without changing its width and height at all.</p>
<p>It also helps with email. Many providers accept attachments of 20–25 MB in total, so ten photos straight from a phone can fail to send. Bring each to 2 MB and the whole set fits in one message.</p>''',
[("Will compressing to 2 MB change the photo's dimensions?", "Usually not. Most phone photos reach 2 MB by quality alone, so the width and height stay the same.")])

P["compress-image-to-5mb"] = ('''<h2>Keeping print quality under 5 MB</h2>
<p>5 MB is a generous limit, mostly needed for photos from 48–200 megapixel phone modes, drone cameras and DSLRs, which can produce 10–25 MB files. Under 5 MB these photos still print well at A4 and larger, and they're accepted by most photo competitions, print shops and stock sites that set this cap.</p>
<p>If you edit photos afterwards, keep your original file too. Every time a JPG is saved again it loses a little detail, so it's better to edit the original and compress once at the end.</p>''',
[("Can I print a 5 MB photo as a poster?", "For A4 and A3, yes. For very large posters, keep the original file if the print shop accepts it.")])

# ---------------- compress PDF to <size> ----------------
P["compress-pdf-to-100kb"] = ('''<h2>What a 100 KB PDF looks like</h2>
<p>100 KB is a strict limit, usually set by older government and exam portals. One typed page without images is often only 20–60 KB, so typed documents fit easily. Scans are the challenge: a single A4 scan from a phone can be 1–3 MB, and fitting it into 100 KB means saving the page at a lower resolution, which still reads well for normal-sized text.</p>
<h2>Getting a scan under 100 KB</h2>
<ul><li>Scan in black and white or greyscale if the portal allows it; colour costs three times as much.</li><li>Upload only the pages they ask for. A two-page certificate is easier at 100 KB than a five-page bundle.</li><li>Use a scanning app's "document" mode, which whitens the background. Grey, shadowy paper compresses badly.</li></ul>
<p>After compressing, zoom to 100% and read the smallest text on the page, such as roll numbers or dates. If it isn't clear, split the document and upload the most important page.</p>''',
[("Why does my one-page scan not fit in 100 KB?", "It was probably scanned at a high resolution in colour. The tool lowers the quality step by step; if it still can't reach 100 KB, rescan in greyscale or with document mode and try again.")])

P["compress-pdf-to-200kb"] = ('''<h2>200 KB uploads for admissions and jobs</h2>
<p>University admissions, scholarship forms and job applications often cap each document at 200 KB: a CV, a degree certificate, a transcript or an ID card. A typed CV exported from Word is usually already under 200 KB, unless it contains a large photo or decorative images. Scanned certificates are the files that typically need compressing.</p>
<p>A CV that is too big is usually caused by a high-resolution photo or logo inside it. Compressing the PDF shrinks those images while keeping the text sharp.</p>
<h2>Check before you submit</h2>
<p>Open the compressed file and check three things: every page is there, the stamps and signatures are still visible, and the text is readable at normal zoom. Portals rarely tell you a document was hard to read; the reviewer just sees a blurry page.</p>''',
[("Can I compress a CV to under 200 KB?", "Yes. Most CVs fit easily. If your CV has a photo, the photo is the part that gets compressed, while the text stays sharp.")])

P["compress-pdf-to-300kb"] = ('''<h2>The 300 KB limit on scanned documents</h2>
<p>300 KB gives a little more room than 200 KB, roughly one extra scanned page at the same quality. It's common on portals where you upload proofs of address, income certificates or experience letters, which are often two pages long.</p>
<ul><li><b>Two-page letters:</b> usually fit with clear text.</li><li><b>Photos of documents taken at an angle</b> waste space on the table around the page; crop them before turning them into a PDF.</li><li><b>Stamped and signed pages:</b> blue ink stamps can fade when compressed hard. Look at them in the result before uploading.</li></ul>
<p>If you're making the PDF from phone photos, <a href="../jpg-to-pdf/">JPG to PDF</a> can create it directly under 300 KB: type 300 in its maximum size box.</p>''',
[("Is 300 KB enough for a two-page scanned document?", "Usually, yes. Two A4 pages in greyscale fit comfortably and stay readable.")])

P["compress-pdf-to-500kb"] = ('''<h2>500 KB: room for several pages</h2>
<p>With 500 KB, a PDF of five to ten scanned pages can stay readable, which suits bank statements, rental documents, tax forms and project reports. Visa and immigration portals often use 500 KB or 1 MB per document.</p>
<p>Bank statements downloaded from online banking are usually typed PDFs and already small. Scanned statements, or statements printed and then photographed, are the ones that need compressing.</p>
<h2>Many pages and a 500 KB limit</h2>
<p>For long documents, remove the pages you don't need first, such as blank backs, terms and conditions pages and duplicate copies. Use <a href="../split-pdf/">Split PDF</a> to keep only the pages you want, then compress. Every page you remove leaves more room for the others to stay sharp.</p>''',
[("How many pages fit in a 500 KB PDF?", "Typed pages: hundreds. Scanned pages: usually five to ten in greyscale with readable text, depending on how much each page contains.")])

P["compress-pdf-to-1mb"] = ('''<h2>1 MB per document</h2>
<p>1 MB is a common limit on job portals, government services and court or tribunal e-filing systems. It's enough for most scanned documents of up to 15–20 pages, or a shorter document with photos.</p>
<p>Presentation exports are a frequent problem: a PDF saved from PowerPoint or Canva can be 10–50 MB because each slide contains full-resolution images. Compressing to 1 MB makes the images lighter while keeping slide text readable.</p>
<h2>Email and messaging</h2>
<p>1 MB is also a good size for sending PDFs over WhatsApp, Telegram or email to someone on a slow connection. The file opens quickly on any phone, and there is little visible difference from the original on a small screen.</p>''',
[("Why is my PDF from PowerPoint so big?", "Slides usually contain full-size photos and graphics. Compressing re-saves those images at a lower size, which brings the file down a lot.")])

P["compress-pdf-to-2mb"] = ('''<h2>2 MB: the usual limit for applications</h2>
<p>2 MB per file is one of the most common upload limits, used by many universities, visa portals and job sites. Typed documents almost never reach it. It's mostly long scans, photos inside PDFs and portfolio PDFs that go over.</p>
<ul><li><b>Portfolios:</b> designers and architects often send PDFs of 20–100 MB. Compressing to 2 MB keeps the layout and makes images lighter, which is fine for a first application; offer the full version on request.</li><li><b>Theses and reports</b> with many charts and photos usually reach 2 MB without visible loss of text.</li><li><b>Scanned books and notes:</b> greyscale scans fit far more pages than colour.</li></ul>''',
[("Will my PDF still be printable at 2 MB?", "For typed documents and most scans, yes. Photo-heavy portfolios will look fine on screen but less sharp on large prints.")])

P["compress-pdf-to-5mb"] = ('''<h2>5 MB for big documents</h2>
<p>A 5 MB limit is common in email systems, learning platforms such as school and university assignment portals, and some legal and insurance submission systems. It suits long scanned documents of 30–60 pages, or reports full of photos.</p>
<p>Scanned assignments: phone scanning apps often save each page as a large colour image, so a 20-page handwritten assignment can reach 40 MB. Compressing to 5 MB keeps the handwriting easy to read. Check pages written in pencil, which are lighter and suffer first.</p>
<p>If one PDF is still too big after compressing, split it into two parts with <a href="../split-pdf/">Split PDF</a> and upload "Part 1" and "Part 2" if the system allows several files.</p>''',
[("Can a 60-page scan fit in 5 MB?", "Usually, if it's in greyscale. Colour scans of that length may need splitting into two files.")])

# ---------------- JPG to PDF under <size> ----------------
P["jpg-to-pdf-under-100kb"] = ('''<h2>Photos to one small PDF in a single step</h2>
<p>Many forms ask for documents as a PDF under 100 KB but you only have photos on your phone. Rather than making a PDF and then compressing it, this page does both together: the photos are resized and re-saved only as much as needed so the finished PDF lands under 100 KB.</p>
<p>At this size, one or two pages work best: the front and back of an ID card, a single certificate or a fee receipt. If you add more pages, each one gets less space and small text gets harder to read.</p>''',
[("Should I crop the photos first?", "Yes. Crop each photo to the edges of the document. The table and background around the paper take up space the text could use.")])

P["jpg-to-pdf-under-200kb"] = ('''<h2>Naming the PDF for the portal</h2>
<p>Portals often show uploaded files only by name, and reviewers see dozens. Rename the downloaded PDF to say what it is, for example <code>marksheets-2025.pdf</code> or <code>id-card-front-back.pdf</code>, and avoid spaces and special characters, which some older upload systems reject.</p>
<h2>Several document photos in one 200 KB PDF</h2>
<p>200 KB is a practical limit for a short set of document photos: three or four pages such as mark sheets, a certificate and an ID card. The page order follows the order in the list, so put the most important page first; reviewers often only look at page one.</p>
<p>Photograph every page the same way, flat, from straight above and with the same light. Pages that are evenly lit look alike after compression and are much easier to read than a mix of bright and dark photos.</p>''',
[("Can I mix JPG and PNG photos in one PDF?", "Yes. Add both; each is placed on its own page, and the PDF is still made under 200 KB.")])

P["jpg-to-pdf-under-500kb"] = ('''<h2>A longer document under 500 KB</h2>
<p>500 KB leaves room for a document of six to ten photographed pages, such as a lease agreement, a medical report or a set of bills, while keeping normal text readable. It's also a good size for sending a multi-page document by email or chat.</p>
<p>Choose A4 or Letter as the page size so the PDF prints properly if the receiver prints it. "Same as image" makes each page the size of the photo, which looks fine on screen but prints at odd sizes.</p>''',
[("Will a 500 KB PDF print clearly?", "For text documents of up to about ten pages, yes. Photos with fine detail print better from a larger file.")])
