"""Third round (29 Oct 2026, owner asked for every page above 60% unique three-word phrases).
Practical, page-specific text appended to each page. Wording is deliberately not shared between pages."""

M = {}

# ---------------- main tools ----------------
M["passport-photo-maker"] = ('''<h2>Five checks before you print</h2>
<ol><li><b>Eyes level:</b> both eyes should sit on the same horizontal line. If your head is tilted, retake the photo with the camera held straight.</li>
<li><b>Even skin tone:</b> one side of the face much darker than the other means the light came from the side. Retake it facing a window.</li>
<li><b>Background edges:</b> look at the area around the hair. Patterned curtains, door frames or a second person's shoulder must not show.</li>
<li><b>Expression:</b> relaxed and neutral, mouth shut. Raised eyebrows and big smiles are a frequent reason for rejection.</li>
<li><b>Print scale:</b> after printing, hold a ruler against one photo. If it measures a few millimetres short, the printer shrank it to fit the paper; reprint at 100%.</li></ol>
<p>Keeping the downloaded single photo is handy: the same file works for later online forms that ask for an ID-style picture.</p>''', [])

M["pdf-to-png"] = ('''<h2>PNG or JPG for PDF pages?</h2>
<p>Pick PNG when the page is mostly text, tables, diagrams or line drawings, and you want edges that stay razor sharp when someone zooms in. That makes it the better choice for slides pasted into a report, a chart reused in a presentation or a contract page attached to a support ticket. JPG suits pages that are mostly photographs, where the file is several times lighter and the difference can't be seen.</p>
<p>The transparent background option removes the white paper colour, so a logo or diagram drawn on a PDF page can be placed over a coloured slide. Pages with a scanned image keep that image, because a scan has no transparent areas to begin with.</p>
<p>Expect large files: a full A4 page at the highest setting can be a few megabytes as PNG.</p>''', [])

M["compress-image"] = ('''<h2>What the controls do</h2>
<ul><li><b>Quality</b> (10–95%) decides how much fine detail is thrown away. Around 70% is the sweet spot where most people can't tell the result from the original.</li>
<li><b>Max width</b> shrinks the picture's dimensions. A blog or shop rarely shows images wider than 1600 pixels, so anything bigger only adds weight.</li>
<li><b>Output</b> switches between JPG, accepted everywhere, and WebP, which is smaller but not accepted by every upload form.</li>
<li><b>Target size</b> overrides quality: type a number of KB and the tool searches for the best version that fits.</li></ul>
<p>Photos with lots of tiny detail, like grass, gravel or crowds, compress less well than portraits or skies, so the same settings give different sizes for different pictures.</p>''', [])

M["jpg-to-pdf"] = ('''<h2>Common jobs people use this for</h2>
<ul><li><b>Homework and assignments:</b> photograph each handwritten page and submit one PDF instead of a dozen loose images.</li>
<li><b>ID copies for a landlord or employer:</b> front and back of a licence or national ID as a two-page file.</li>
<li><b>Signed forms:</b> print, sign, photograph and return a document when there is no scanner nearby.</li>
<li><b>Receipts for tax time:</b> one PDF per month is easier for an accountant than a folder of photos.</li></ul>
<p>Phone screenshots work too. They are tall and narrow, so choose "Same as image" for the page size if the PDF will only be read on a phone, or A4 with a margin if it will be printed.</p>''', [])

M["png-to-pdf"] = ('''<h2>Keeping text in screenshots readable</h2>
<p>Screenshots taken on high-resolution phones and laptops are often 2–3 times larger than they appear on screen, so they print sharply even on an A4 page. If you join screenshots from different devices, check that the small text is a similar size on every page; very large phone screenshots placed on A4 can look much smaller than laptop ones.</p>
<p>Before converting, crop away status bars, notification icons and browser tabs you don't want the reader to see, such as the battery level or other open websites.</p>''', [])

M["pdf-to-word"] = ('''<h2>Getting the best Word file</h2>
<p>PDFs exported from Word, Google Docs or another editor contain real text, so their paragraphs and larger headings come through ready to edit, with a page break after each page. Pictures, columns and the exact layout aren't carried over, so expect to reformat tables and add images back. Scanned PDFs are pictures of paper, so there is no text inside to convert. For those, run the pages through Image to Text first, or retype short documents.</p>
<p>That makes it ideal for reusing the wording of a letter, report or contract, rather than reproducing its design.</p>''', [])

M["compress-pdf"] = ('''<h2>Why some PDFs barely shrink</h2>
<p>A PDF made of typed text is already tiny, so there's little to remove, and the tool may tell you the file can't get much smaller. The big savings come from PDFs containing photos or scans: phone scans, brochures, slide exports and image-heavy reports. Those can often drop by 70–90% while staying readable.</p>''', [])

M["jfif-to-jpg"] = ('''<h2>Why Windows saves JFIF</h2>
<p>On some Windows computers, images saved from the web arrive as .jfif because of a file-type setting in the registry, even though the image itself is an ordinary JPEG. Renaming them works too, but converting here is quicker for a batch and doesn't need any settings changed.</p>''', [])

M["jpg-to-png"] = ('''<h2>Will PNG improve a blurry JPG?</h2>
<p>No. Converting can't bring back detail that JPG compression already removed. PNG simply stops any further loss when the image is edited and saved again, which makes it a good format for files you plan to keep editing.</p>''', [])

M["webp-to-jpg"] = ('''<h2>Saving web images for printing</h2>
<p>Print shops and photo kiosks usually ask for JPG. WebP images saved from websites are often compressed heavily for speed, so check that one is large enough before ordering a print: aim for at least 1200 pixels on the long side for a 6 × 4 inch photo.</p>''', [])

M["resize-image"] = ('''<h2>Pixels, inches and dpi</h2>
<p>Pixel size is what screens and upload forms care about. Inches and centimetres only matter when printing: divide the pixels by the print resolution. A 1800 × 1200 pixel photo printed at 300 dpi is 6 × 4 inches.</p>''', [])

M["pdf-to-jpg"] = ('''<h2>Posting a PDF on social media</h2>
<p>Instagram, Facebook and WhatsApp status can't show PDFs, but they show images. Convert the pages, then post them in order as a carousel, which is a common way to share flyers, menus and event schedules.</p>''', [])

M["video-to-mp3"] = ('''<h2>Audio from screen recordings and lectures</h2>
<p>Screen recordings and recorded lectures are often hundreds of megabytes, but the speech in them fits into a few megabytes of MP3. That's much easier to listen to on a commute or to send to a transcription service.</p>''', [])

M["mp4-to-mp3"] = ('''<h2>Voice notes and interviews</h2>
<p>Interviews recorded on a phone camera can be turned into MP3 so they open in any audio editor or podcast app, and are small enough to email.</p>''', [])

M["image-to-text"] = ('''<h2>Better results from phone photos</h2>
<p>Hold the phone parallel to the page, avoid shadows from your hand and tap to focus on the text before taking the photo.</p>''', [])

M["heic-to-jpg"] = ('''<h2>Sending iPhone photos to Android and Windows</h2>
<p>Some Android phones and older Windows PCs can't open HEIC. Converting to JPG first means the photos open everywhere.</p>''', [])

M["heic-to-pdf"] = ('''<h2>Several HEIC photos as one document</h2>
<p>Pick the photos in page order, check the list, and reorder with the arrows if needed. Each photo becomes one page, so a three-page lease photographed on an iPhone becomes a three-page PDF ready to email.</p>''', [])

M["png-to-jpg"] = ('''<h2>Shrinking screenshots for email</h2>
<p>A folder of PNG screenshots can be tens of megabytes. Converting to JPG at about 85% quality usually cuts that to a few megabytes with the text still clear.</p>''', [])

M["jpeg-to-jpg"] = ('''<h2>Upload forms that insist on .jpg</h2>
<p>JPEG and JPG are the same format; the shorter extension dates from old Windows systems that allowed only three letters. Some strict upload checks look only at the letters after the dot, so a perfectly valid .jpeg photo is refused. This tool gives it the .jpg ending without re-saving the picture, so the quality stays exactly as it was.</p>''', [])

M["remove-background"] = ('''<h2>Best photos for cut-outs</h2>
<p>A clear subject in front of a contrasting background gives the cleanest edges.</p>''', [])

M["txt-to-pdf"] = ('''<h2>Logs and code listings</h2>
<p>Choose Monospace (Courier) so columns and indentation stay aligned.</p>''', [])

# ---------------- compress image presets ----------------
M["compress-image-to-2mb"] = ('''<h2>Photographers sending previews</h2>
<p>Wedding and event photographers often send clients a preview set before the final gallery. Bringing each photo to 2 MB keeps the colours and sharpness clients care about, while a set of 50 previews stays around 100 MB instead of 500 MB, which makes cloud links and downloads far quicker.</p>
<h2>Phone storage</h2>
<p>If your phone is full, compressing old photos to 2 MB can free a lot of space while keeping them good enough to print at 6 × 4 inches. Keep the originals of the photos that matter most, such as family portraits, on a computer or cloud backup.</p>''', [])

M["compress-image-to-1mb"] = ('''<h2>Blog posts and websites</h2>
<p>Speed tests such as Google PageSpeed Insights flag large images because they slow pages down on phones. Compressing a header photo to 1 MB and resizing it to about 2000 pixels wide keeps it sharp on large screens without the warning.</p>
<h2>Several photos, one email</h2>
<p>Ten photos at 1 MB each make a 10 MB email, which every provider accepts and which downloads quickly on mobile data. Straight from the camera, the same ten photos could be 40 MB or more.</p>''', [])

M["compress-image-to-50kb"] = ('''<h2>Fixing "file size exceeds 50 KB" errors</h2>
<p>The portal checks the size in kilobytes, and some count 1 KB as 1000 bytes while others use 1024. A file of 50.2 KB can therefore fail. The result here aims slightly under 50 KB, so it passes either way. If a form says "between 20 KB and 50 KB", the result lands near the top of that range, which keeps the most quality.</p>
<p>Also confirm the format: some portals accept only .jpg, not .png or .webp, even when the size is right.</p>''', [])

M["compress-image-to-5mb"] = ('''<h2>Photo competitions and stock sites</h2>
<p>Many photo contests and community galleries cap entries at 5 MB. Judges look at full-screen detail, so compress by quality instead of shrinking dimensions where possible. Leave Max width empty and let the target size do the work, which keeps the full resolution in most cases.</p>''', [])

M["compress-image-to-20kb"] = ('''<h2>Making the signature itself</h2>
<p>Sign on plain white paper with a thick black or dark blue pen, then photograph it from directly above in daylight. Crop tightly so only the signature remains, with a small white margin around it. A clean, tightly cropped signature usually ends up well under 20 KB with sharp strokes.</p>''', [])

M["compress-image-to-100kb"] = ('''<h2>Resume photos and profile pictures</h2>
<p>Job sites and CV builders often limit profile photos to 100 KB. A head-and-shoulders photo in good light, cropped square or 4:5, looks professional at this size and loads instantly for recruiters.</p>''', [])

M["compress-image-to-500kb"] = ('''<h2>Online marketplaces</h2>
<p>Classified and second-hand marketplaces often recommend photos under 500 KB, so buyers on mobile data can swipe through a listing quickly.</p>''', [])

M["compress-image-to-30kb"] = ('''<h2>Photo and signature together</h2>
<p>When a form wants both under 30 KB, compress them separately rather than in one image.</p>''', [])

M["compress-image-to-200kb"] = ('''<h2>Email newsletters</h2>
<p>Images under 200 KB keep newsletters quick to open.</p>''', [])

M["compress-image-to-10kb"] = ('''<h2>Old government portals</h2>
<p>Some legacy systems still use 10 KB fields.</p>''', [])

# ---------------- compress PDF presets ----------------
M["compress-pdf-to-300kb"] = ('''<h2>When the portal shows "invalid file"</h2>
<p>A file under 300 KB can still be refused if the PDF is password-protected, if it contains a form that hasn't been flattened, or if the name contains unusual characters. Rename it to something simple like <code>experience-letter.pdf</code>, and remove any password before compressing. Mobile scanning apps sometimes add a password option by default.</p>''', [])

M["compress-pdf-to-1mb"] = ('''<h2>E-filing and online claims</h2>
<p>Insurance claims, court e-filing and tax portals often accept up to 1 MB per attachment. Keep one document per file, such as an invoice, a medical bill or a police report, and give each a clear name, so the person reviewing it can find what they need without opening every file.</p>
<p>A 1 MB PDF also prints fine on an office printer.</p>''', [])

M["compress-pdf-to-200kb"] = ('''<h2>Scanning certificates at the right settings</h2>
<p>If you use a flatbed or office scanner, choose 150–200 dpi and greyscale for certificates and mark sheets. That gives clean, readable pages that already come close to 200 KB, so compression has little work left and the stamps and seals stay crisp.</p>''', [])

M["compress-pdf-to-2mb"] = ('''<h2>Research papers and dissertations</h2>
<p>Journal submission and thesis systems sometimes cap files at 2 MB. Figures saved at print resolution are usually the cause. Compressing keeps text and equations sharp, but check charts with thin lines and small labels.</p>''', [])

M["compress-pdf-to-5mb"] = ('''<h2>Learning platforms</h2>
<p>School and university submission systems commonly set 5 MB, and a late upload because the file is too big is avoidable: compress a day early.</p>''', [])

M["compress-pdf-to-100kb"] = ('''<h2>Exam and scholarship portals</h2>
<p>Some exam and scholarship sites still ask for each certificate as a PDF under 100 KB. Upload one certificate per file, scanned in greyscale, and the text and grades stay readable.</p>''', [])

M["compress-pdf-to-500kb"] = ('''<h2>Rental and loan applications</h2>
<p>Agents and lenders often ask for payslips and ID as PDFs under 500 KB each; one document per file is easiest for them to check.</p>''', [])

# ---------------- JPG to PDF presets ----------------
M["jpg-to-pdf-under-100kb"] = ('''<h2>Typical 100 KB document requests</h2>
<p>Caste, income and domicile certificates, fee receipts, and a single ID card side are the kind of uploads that usually come with a 100 KB PDF limit. Photograph the page in daylight, crop to the paper, and add only that one photo: a single-page PDF under 100 KB stays clear enough for an officer to read every line.</p>
<p>If the result looks too soft, it usually means the original photo was dark or out of focus, not that 100 KB is too small. Retake it with the phone held steady and the page flat.</p>''', [])

M["jpg-to-pdf-under-500kb"] = ('''<h2>Medical and school records</h2>
<p>Clinics, schools and insurers often ask for reports, vaccination records or report cards as one PDF. Several photographed pages fit under 500 KB with tables and handwriting still legible. Put the most recent page first, since that's the one the reader usually needs.</p>
<p>For a two-sided page, photograph both sides and keep them next to each other in the list, so the PDF reads in the same order as the paper.</p>''', [])

M["jpg-to-pdf-under-200kb"] = ('''<h2>Naming the file</h2>
<p>Give the PDF a name that says what it is, such as <code>marksheets-2025.pdf</code>, before uploading. Reviewers download dozens of files, and a clear name avoids your document being opened last or mixed up with someone else's.</p>''', [])

# ---------------- resize presets ----------------
M["resize-image-to-500x500"] = ('''<h2>Shop thumbnails and forum avatars</h2>
<p>Online shops often display product thumbnails as squares, and 500 × 500 is a common size that stays crisp on high-resolution phones. Put the item in the centre on a plain background, and choose Fit with white border for tall items like bottles, so the top and bottom aren't cut off.</p>
<p>For a forum or gaming avatar, a bold, simple image reads better than a detailed photo at small sizes.</p>''', [])

M["resize-image-to-1500x500"] = ('''<h2>Newsletter and blog banners</h2>
<p>The same wide 3:1 shape works well as a header for email newsletters, blog posts and event pages. Keep any text large and short, a title plus one line at most, because headers are shown small on phones. Dark text on a light, simple background is the easiest to read.</p>''', [])

M["resize-image-to-1920x1080"] = ('''<h2>Zoom and Teams backgrounds</h2>
<p>Video call apps recommend 1920 × 1080 images for virtual backgrounds. Choose a calm picture with no text near the centre, where your head will cover it. A slightly blurred photo looks more natural behind you than a sharp, busy one.</p>''', [])

M["resize-image-to-600x600"] = ('''<h2>Square images for email signatures and invoices</h2>
<p>Email signatures and invoice templates usually display a logo at 100–200 pixels, so a 600 × 600 source stays sharp on high-resolution screens without bloating every email you send.</p>
<h2>Printing a 2 × 2 inch photo from it</h2>
<p>At 300 dots per inch, 600 pixels is exactly 2 inches, so a printer set to 300 dpi prints the file at 2 × 2 inches. Place it on a 4 × 6 sheet in a photo app and choose "actual size" to avoid scaling.</p>''', [])

M["resize-image-to-1024x1024"] = ('''<h2>Favicons and smaller icon sizes</h2>
<p>Start from 1024 × 1024 and make smaller copies, such as 512, 192 and 32 pixels, rather than enlarging a small logo.</p>''', [])

M["resize-image-to-3000x3000"] = ('''<h2>Checking your cover before release</h2>
<p>View the finished cover at thumbnail size on your phone. If the title can't be read, make it bigger.</p>''', [])

M["resize-image-to-1080x1920"] = ('''<h2>WhatsApp status</h2>
<p>WhatsApp status also uses the tall 9:16 shape, so the same 1080 × 1920 image fills the screen there.</p>''', [])

# ---------------- passport presets ----------------
M["india-passport-photo"] = ('''<h2>Photos for OCI and Indian visas</h2>
<p>Overseas Citizenship of India (OCI) and Indian visa applications made online ask you to upload a digital photo, and their rules differ from the 35 × 45 mm print used for Indian passport forms. The OCI and e-Visa portals generally want a square photo with a plain light background. Use the 2 × 2 inch size in the passport photo maker for those, and check the portal's current pixel and KB limits before uploading.</p>
<p>For very young children, the Passport Seva checklist may ask parents to bring a recent photo with a white background; check the current document list for minors before the appointment.</p>''', [])

M["china-visa-photo"] = ('''<h2>Photos for children</h2>
<p>Children applying for a Chinese visa need their own photo meeting the same 33 × 48 mm rules. Toddlers are easiest to photograph seated on a parent's lap in front of a white sheet, as long as the parent's hands and clothes are out of the frame. Take several shots and choose one where the child looks straight at the camera with eyes open.</p>''', [])

M["australia-passport-photo"] = ('''<h2>Children and babies</h2>
<p>Children need their own passport and photo, with the same size and background rules. For babies, lay them on a plain white sheet and photograph from above, so no hands are needed to hold them up. Take several shots and pick one where the baby faces the camera with nothing else in the frame.</p>''', [])

M["canada-passport-photo"] = ('''<h2>Finding a studio that does it right</h2>
<p>Many pharmacies and photo shops in Canada take passport photos. Ask them to confirm that the photos are "Canadian passport size, 50 × 70 mm" and that they will stamp the back with the studio name, address and date; that stamp is the part most often missing when an application is returned.</p>''', [])

M["uk-passport-photo"] = ('''<h2>Photo codes from shops</h2>
<p>Some UK photo booths and shops give you a photo code instead of, or as well as, prints. The online application accepts this code, which avoids uploading a photo yourself. If you take the photo at home instead, the online service will tell you straight away if it fails a check.</p>''', [])

M["pakistan-passport-photo"] = ('''<h2>Photos for other Pakistani forms</h2>
<p>Job applications for government posts, university admissions and scholarship forms in Pakistan often ask for a passport-size photo with a white background, either printed or uploaded. Keep the single photo file from this page so you can reuse it for these forms.</p>''', [])

M["schengen-visa-photo"] = ('''<h2>Family applications</h2>
<p>Each traveller, including babies, needs their own photo, even when the family applies together.</p>''', [])

M["us-passport-photo"] = ('''<h2>Photos for children</h2>
<p>Children of all ages need their own passport photo. For babies, photograph them lying on a white sheet.</p>''', [])

# ---------------- OCR presets ----------------
M["image-to-text-french"] = ('''<h2>Ligatures</h2>
<p>Old books may print fi and fl as joined ligatures; check those words.</p>''', [])
M["image-to-text-russian"] = ('''<h2>Pre-reform spelling</h2>
<p>Books printed before 1918 use letters like ѣ and і, which the model may misread.</p>''', [])
M["image-to-text-arabic"] = ('''<h2>Persian text</h2>
<p>Persian adds letters such as پ چ ژ گ; check them after OCR.</p>''', [])
M["image-to-text-urdu"] = ('''<h2>Poetry layout</h2>
<p>Two-column verses may come out as one line; split them again.</p>''', [])
M["image-to-text-hindi"] = ('''<h2>Sanskrit words</h2>
<p>Sanskrit passages with rare conjuncts need extra proofreading.</p>''', [])
