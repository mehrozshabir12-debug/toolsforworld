# Long-form guides. Each guide links to the tools that do the job.
# {R} is replaced with the relative path to the site root.
# Facts about official rules were checked against the official pages linked in each guide (October 2026).

AUTHOR = "Mehroz Shabir"

GUIDES = [
    dict(
        slug="passport-photo-size-by-country",
        date="2026-10-15",
        title="Passport Photo Size by Country: US, UK, Canada, Australia, India, Schengen & China",
        desc="Passport and visa photo sizes for 7 countries in one table, with head size, background colour and the mistakes that get photos rejected.",
        h1="Passport photo size by country",
        lead="Every country sets its own photo size, head size and background. Here are the rules for seven of the most common applications in one place, and how to get a photo that passes first time.",
        body='''<h2>Quick comparison</h2>
<div class="scroll"><table class="t"><thead><tr><th>Country / document</th><th>Photo size</th><th>Head size (chin to crown)</th><th>Background</th><th>Make it</th></tr></thead><tbody>
<tr><td>United States passport</td><td>2 × 2 in (51 × 51 mm)</td><td>25–35 mm</td><td>White or off-white</td><td><a href="{R}us-passport-photo/">US photo maker</a></td></tr>
<tr><td>United Kingdom passport</td><td>35 × 45 mm</td><td>29–34 mm</td><td>Plain, light-coloured</td><td><a href="{R}uk-passport-photo/">UK photo maker</a></td></tr>
<tr><td>Canada passport</td><td>50 × 70 mm</td><td>31–36 mm</td><td>White or light-coloured</td><td><a href="{R}canada-passport-photo/">Canada photo maker</a></td></tr>
<tr><td>Australia passport</td><td>35–40 × 45–50 mm</td><td>32–36 mm</td><td>Plain white or light grey</td><td><a href="{R}australia-passport-photo/">Australia photo maker</a></td></tr>
<tr><td>India passport</td><td>35 × 45 mm</td><td>Face covers most of the photo</td><td>Plain white</td><td><a href="{R}india-passport-photo/">India photo maker</a></td></tr>
<tr><td>Schengen visa</td><td>35 × 45 mm</td><td>About 32–36 mm (70–80% of the photo)</td><td>Light, plain</td><td><a href="{R}schengen-visa-photo/">Schengen photo maker</a></td></tr>
<tr><td>China visa</td><td>33 × 48 mm</td><td>28–33 mm</td><td>Plain white</td><td><a href="{R}china-visa-photo/">China photo maker</a></td></tr>
</tbody></table></div>
<p>The most common size in the world is <b>35 × 45 mm</b>, used by the UK, India, Australia, the Schengen countries and many others. The United States is the big exception with its square 2 × 2 inch photo, and Canada and China use their own sizes.</p>

<h2>Rules almost every country shares</h2>
<ul><li><b>Recent:</b> usually taken in the last six months. The UK is stricter: no more than one month old.</li>
<li><b>Neutral expression:</b> mouth closed, eyes open and looking straight at the camera.</li>
<li><b>No glasses:</b> the US does not accept glasses at all, and most other countries strongly prefer you take them off to avoid glare.</li>
<li><b>Even light:</b> no shadows on your face or behind your head.</li>
<li><b>No filters or editing:</b> beauty filters, smoothing and background replacement can get a photo rejected.</li>
<li><b>Nothing covering the face:</b> hats and head coverings are allowed only for religious or medical reasons, and your face must still be fully visible from the bottom of the chin to the top of the forehead.</li></ul>

<h2>How to take a passport photo at home</h2>
<ol><li><b>Find a plain wall</b> in the right colour. A white sheet hung flat works if your wall isn't plain.</li>
<li><b>Use daylight from a window in front of you,</b> not behind you. Stand about half a metre from the wall so your shadow doesn't fall on it.</li>
<li><b>Ask someone else to take it</b> from about 1–1.5 metres away, with the phone at your eye level. Selfies distort the face and are often rejected.</li>
<li><b>Open the photo maker for your country.</b> The size is already set; move and zoom the photo so the top of your head and your chin sit on the guide lines.</li>
<li><b>Download the 4 × 6 inch print sheet</b> and print it at 100% scale at home or at any photo shop. One sheet gives you several photos for a few cents.</li></ol>

<h2>Online applications need a digital photo</h2>
<p>More and more applications are made online, and they ask for a digital file instead of a print. These have their own rules:</p>
<ul><li><b>US visa (DS-160):</b> a square JPEG from 600 × 600 to 1200 × 1200 pixels, no larger than 240 KB.</li>
<li><b>UK online passport:</b> at least 600 pixels wide and 750 pixels tall. Upload your original photo rather than a small crop.</li>
<li><b>Other portals</b> often give a size in pixels and a limit in KB. Make the photo first, then use <a href="{R}compress-image-to-100kb/">Compress Image to 100 KB</a> or the size you need.</li></ul>

<h2>Countries where you can't print your own</h2>
<p>Canada requires passport photos taken by a commercial photographer, who stamps the studio's name, address and date on the back. Home prints are usually refused. Our Canada tool is still useful to check your framing before you go, or for documents that accept self-made photos.</p>

<h2>Why photos get rejected</h2>
<ul><li>Head too big or too small for the frame.</li>
<li>Shadows on the background or under the chin.</li>
<li>Photo printed at the wrong scale. Always print at 100%, not “fit to page”.</li>
<li>Background in the wrong colour, or with patterns or objects.</li>
<li>Glare on glasses, or hair covering the eyes.</li></ul>

<div class="warnbox">Rules change from time to time. Always check the latest requirements on the official site before you apply: <a href="https://travel.state.gov/content/travel/en/passports/how-apply/photos.html" rel="nofollow">US</a>, <a href="https://www.gov.uk/photos-for-passports" rel="nofollow">UK</a>, <a href="https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-passports/photos.html" rel="nofollow">Canada</a>, <a href="https://www.passports.gov.au/getting-passport-how-it-works/photo-guidelines" rel="nofollow">Australia</a>, <a href="https://www.passportindia.gov.in/" rel="nofollow">India</a>. For visas, follow the checklist of the embassy or visa centre you are applying to.</div>''',
        faq=[("What is the most common passport photo size?", "35 × 45 mm. It is used by the UK, India, Australia, the Schengen countries and many others. The US uses 2 × 2 inches instead."),
             ("Can I take my passport photo with my phone?", "Yes, for most countries, as long as someone else takes it in good light against a plain background. Canada is an exception: it needs a commercial photographer."),
             ("How many photos do I need?", "Usually two printed photos. A 4 × 6 inch sheet from our photo makers gives you several, so you have spares.")],
    ),
    dict(
        slug="how-to-compress-photo-to-50kb",
        date="2026-10-15",
        title="How to Reduce Photo Size to 50 KB for Online Forms (Without Losing Quality)",
        desc="Step-by-step: make a photo or signature fit the 20 KB, 50 KB or 100 KB limit on exam, job and government forms, on phone or computer, for free.",
        h1="How to reduce a photo to 50 KB for online forms",
        lead="Exam, job and government portals often reject photos that are even 1 KB over the limit. Here is how to get under 50 KB (or any size) while keeping your face sharp.",
        body='''<h2>Why phone photos are too big</h2>
<p>A modern phone camera saves photos of 12 megapixels or more, usually 2–5 MB each. That is 40 to 100 times bigger than a 50 KB limit. To fit, a photo needs two things: fewer pixels and stronger compression. Done in the right order, the result still looks clear at the size the form shows it.</p>

<h2>The quick way</h2>
<ol><li>Open <a href="{R}compress-image-to-50kb/">Compress Image to 50 KB</a>.</li>
<li>Choose your photo. The target is already set to 50 KB.</li>
<li>Press <b>Compress</b> and download the result. The tool picks the best quality that stays just under 50 KB.</li></ol>
<p>Other common limits: <a href="{R}compress-image-to-20kb/">20 KB</a>, <a href="{R}compress-image-to-30kb/">30 KB</a>, <a href="{R}compress-image-to-100kb/">100 KB</a>, <a href="{R}compress-image-to-200kb/">200 KB</a>. For any other number, type it into the <a href="{R}compress-image/">Image Compressor</a>.</p>

<h2>The way that gives the best quality</h2>
<ol><li><b>Read the form's rules first.</b> Note the file size (for example 20–50 KB), the format (usually JPG) and any size in pixels or centimetres.</li>
<li><b>Crop first.</b> Cut away everything except your head and shoulders. Every pixel of wall you remove is quality saved for your face. If the form gives a size in cm, use the <a href="{R}passport-photo-maker/">passport photo maker</a>; if it gives pixels, use <a href="{R}resize-image/">Resize Image</a>.</li>
<li><b>Then compress</b> to the limit. Set the target to the <i>maximum</i> allowed, not lower, so you keep as much detail as possible and stay above any minimum.</li>
<li><b>Check the result</b> by opening it and zooming in on your eyes. If it looks blocky, crop tighter and try again.</li></ol>

<h2>Signatures under 10–20 KB</h2>
<ul><li>Sign with a dark blue or black pen on plain white paper.</li>
<li>Photograph it in daylight, straight from above, with no shadow from the phone.</li>
<li>Crop tightly around the signature, then compress to <a href="{R}compress-image-to-10kb/">10 KB</a> or <a href="{R}compress-image-to-20kb/">20 KB</a>. A tightly cropped signature stays sharp even at 10 KB.</li></ul>

<h2>KB, pixels and centimetres: what's the difference?</h2>
<ul><li><b>KB (kilobytes)</b> is the file size: how much storage the photo takes. “Photo must be under 50 KB” is about this.</li>
<li><b>Pixels</b> are the width and height of the image on screen, like 300 × 400 px.</li>
<li><b>Centimetres</b> describe the printed size. At 300 dpi, 3.5 × 4.5 cm is about 413 × 531 pixels.</li></ul>
<p>Many forms mix these up and say “resize to 50 KB” when they mean the file size. If the instruction ends in KB, you need the compressor, not the resizer.</p>

<h2>Common reasons the form still says “file too large”</h2>
<ul><li><b>1 KB = 1024 bytes.</b> Some tools count 1 KB as 1000 bytes, so a “49 KB” file can be over the limit. Our compressor uses 1024, which strict portals expect.</li>
<li><b>Wrong format.</b> The portal wants JPG but you uploaded PNG or HEIC. Convert with <a href="{R}png-to-jpg/">PNG to JPG</a> or <a href="{R}heic-to-jpg/">HEIC to JPG</a> first.</li>
<li><b>Below the minimum.</b> Some forms reject files that are too small, like under 20 KB. Set the target to the upper limit.</li>
<li><b>Old cached file.</b> You uploaded the original instead of the compressed copy. Check the file name.</li></ul>

<h2>Is it safe for documents like ID cards?</h2>
<p>Yes. Our tools run in your browser, so the photo is compressed on your own device and never uploaded to us. That matters for ID cards, certificates and signatures.</p>''',
        faq=[("How do I compress a photo to 50 KB on my phone?", "Open Compress Image to 50 KB in your phone's browser, choose the photo from your gallery and press Compress. No app is needed."),
             ("Will my photo look blurry at 50 KB?", "Not if you crop it first. A head-and-shoulders photo stays clear at 50 KB; a full-size scene with lots of background looks worse."),
             ("What if the form asks for 20 to 50 KB?", "Set the target to 50 KB. That keeps the most quality and stays above the 20 KB minimum.")],
    ),
    dict(
        slug="reduce-scanned-pdf-size",
        date="2026-10-15",
        title="How to Reduce the Size of a Scanned PDF: 6 Methods That Work",
        desc="Why scanned PDFs are so large and six practical ways to shrink them for email and upload limits like 200 KB, 500 KB or 1 MB, without special software.",
        h1="How to reduce the size of a scanned PDF",
        lead="A few pages scanned with a phone can easily reach 10–20 MB. Here is why, and six ways to bring a scanned PDF under an upload limit while keeping it readable.",
        body='''<h2>Why scanned PDFs are so big</h2>
<p>A scanned PDF is really a set of photos, one per page. Phone cameras and scanners save each page with far more detail than you need to read it, often in full colour. A PDF made in Word, by contrast, stores text as letters, so ten pages of plain text can be under 100 KB while ten scanned pages can be 15 MB.</p>

<h2>1. Compress it to the exact size</h2>
<p>The fastest fix. Our compressor re-saves each page as a smaller image and keeps the sharpest version that fits your target. Pick the limit you need: <a href="{R}compress-pdf-to-200kb/">200 KB</a>, <a href="{R}compress-pdf-to-500kb/">500 KB</a>, <a href="{R}compress-pdf-to-1mb/">1 MB</a>, <a href="{R}compress-pdf-to-2mb/">2 MB</a>, or type any size into <a href="{R}compress-pdf/">Compress PDF</a>.</p>

<h2>2. Remove pages you don't need</h2>
<p>Blank backs of pages, cover sheets and duplicate copies all add size. Use <a href="{R}split-pdf/">Split PDF</a> to keep only the pages the form asks for. Halving the pages roughly halves the size, and leaves more room for quality on the pages that matter.</p>

<h2>3. Scan in greyscale</h2>
<p>Unless the form asks for colour, scan in black and white or greyscale. Colour stores three times as much information per pixel. Most phone scanner apps and office scanners have a greyscale setting.</p>

<h2>4. Use a sensible resolution</h2>
<p>150–200 dpi is plenty for reading and printing documents. Scanners set to 600 dpi produce files several times larger, with detail no one will see. If you photograph pages with a phone, the compressor reduces the resolution for you.</p>

<h2>5. Crop and straighten before making the PDF</h2>
<p>Tables, fingers and shadows around a page are stored as detail too. Take the photo straight from above, in daylight, on a dark plain surface, and crop to the edges of the paper. Clean, evenly lit pages compress far better.</p>

<h2>6. Split one big file into several</h2>
<p>If a portal allows several uploads, split a long document into parts with <a href="{R}split-pdf/">Split PDF</a> and compress each part. If it wants a single file, do the opposite: join everything with <a href="{R}merge-pdf/">Merge PDF</a> first, then compress the merged file once.</p>

<h2>Roughly how many scanned pages fit</h2>
<div class="scroll"><table class="t"><thead><tr><th>Limit</th><th>Typical phone-scanned pages that stay readable</th></tr></thead><tbody>
<tr><td>100 KB</td><td>1–2</td></tr><tr><td>200 KB</td><td>2–4</td></tr><tr><td>500 KB</td><td>5–10</td></tr><tr><td>1 MB</td><td>10–20</td></tr><tr><td>2 MB</td><td>20–40</td></tr></tbody></table></div>
<p>These are rough figures for greyscale or simple colour pages. Pages full of photos need more space per page.</p>

<h2>One trade-off to know</h2>
<p>After compressing a scanned PDF, the pages are images, so text can't be selected or searched. That's normal for scans and fine for forms. If you need editable text, run a page through <a href="{R}image-to-text/">Image to Text (OCR)</a>, or convert a text-based PDF with <a href="{R}pdf-to-word/">PDF to Word</a>.</p>''',
        faq=[("Why is my 3-page scan 10 MB?", "Each page is a high-resolution colour photo. Compressing re-saves the pages at a sensible size, usually cutting the file by 90% or more."),
             ("Will compressing a PDF make it unreadable?", "Not if the target is realistic for the number of pages. Check the result by zooming in on the smallest text before you submit."),
             ("Is my PDF uploaded when I compress it?", "No. Our PDF tools run in your browser, so the file stays on your device.")],
    ),
    dict(
        slug="social-media-image-sizes",
        date="2026-10-15",
        title="Social Media Image Sizes Cheat Sheet: Instagram, Facebook, YouTube, LinkedIn, X & Pinterest",
        desc="The image sizes in pixels for posts, stories, covers, banners and thumbnails on every major platform, plus the safe zones where text gets hidden.",
        h1="Social media image sizes cheat sheet",
        lead="Uploading at the wrong size makes platforms crop or blur your image. Here are the sizes that work on each platform, and where to keep your text so it isn't hidden.",
        body='''<h2>All sizes at a glance</h2>
<div class="scroll"><table class="t"><thead><tr><th>Platform</th><th>Image</th><th>Size (pixels)</th><th>Shape</th><th>Resize</th></tr></thead><tbody>
<tr><td rowspan="3">Instagram</td><td>Square post</td><td>1080 × 1080</td><td>1:1</td><td><a href="{R}resize-image-to-1080x1080/">Resize</a></td></tr>
<tr><td>Portrait post</td><td>1080 × 1350</td><td>4:5</td><td><a href="{R}resize-image-to-1080x1350/">Resize</a></td></tr>
<tr><td>Story / Reel</td><td>1080 × 1920</td><td>9:16</td><td><a href="{R}resize-image-to-1080x1920/">Resize</a></td></tr>
<tr><td rowspan="2">Facebook</td><td>Link preview / landscape post</td><td>1200 × 630</td><td>1.91:1</td><td><a href="{R}resize-image-to-1200x630/">Resize</a></td></tr>
<tr><td>Cover photo</td><td>851 × 315</td><td>about 2.7:1</td><td><a href="{R}resize-image-to-851x315/">Resize</a></td></tr>
<tr><td rowspan="2">YouTube</td><td>Thumbnail</td><td>1280 × 720</td><td>16:9</td><td><a href="{R}resize-image-to-1280x720/">Resize</a></td></tr>
<tr><td>Channel banner</td><td>2560 × 1440</td><td>16:9</td><td><a href="{R}resize-image-to-2560x1440/">Resize</a></td></tr>
<tr><td rowspan="2">LinkedIn</td><td>Profile banner</td><td>1584 × 396</td><td>4:1</td><td><a href="{R}resize-image-to-1584x396/">Resize</a></td></tr>
<tr><td>Profile photo</td><td>400 × 400</td><td>1:1</td><td><a href="{R}resize-image-to-400x400/">Resize</a></td></tr>
<tr><td>X (Twitter)</td><td>Header</td><td>1500 × 500</td><td>3:1</td><td><a href="{R}resize-image-to-1500x500/">Resize</a></td></tr>
<tr><td>Pinterest</td><td>Standard pin</td><td>1000 × 1500</td><td>2:3</td><td><a href="{R}resize-image-to-1000x1500/">Resize</a></td></tr>
<tr><td>TikTok / Shorts</td><td>Cover / full screen</td><td>1080 × 1920</td><td>9:16</td><td><a href="{R}resize-image-to-1080x1920/">Resize</a></td></tr>
<tr><td>WhatsApp / Telegram</td><td>Profile picture</td><td>500 × 500</td><td>1:1</td><td><a href="{R}resize-image-to-500x500/">Resize</a></td></tr>
</tbody></table></div>

<h2>Safe zones: where text gets hidden</h2>
<ul><li><b>Stories, Reels and TikTok:</b> the top 250 px or so is covered by your name and progress bar, and the bottom 350 px by captions and the reply box. On Reels and TikTok, the right edge holds the like and share buttons.</li>
<li><b>YouTube banner:</b> only a central area of about 1546 × 423 px shows on every device, including phones.</li>
<li><b>LinkedIn and X banners:</b> your profile photo covers the bottom-left corner.</li>
<li><b>Facebook cover:</b> phones crop the left and right edges.</li>
<li><b>YouTube thumbnail:</b> the video length badge covers the bottom-right corner.</li>
<li><b>Profile pictures</b> are shown as circles almost everywhere, so the corners are never seen.</li></ul>

<h2>Crop or add a border?</h2>
<p>When your photo is a different shape from the target, you have two choices in our resizer:</p>
<ul><li><b>Crop to fill</b> fills the whole frame and trims the edges. Best for photos where the subject is in the middle.</li>
<li><b>Fit with white border</b> keeps the whole image and adds space around it. Best for logos, screenshots and group photos where nothing can be cut.</li></ul>

<h2>Keeping images sharp</h2>
<ul><li><b>Start big, finish small.</b> Resizing a large photo down stays sharp; enlarging a small one makes it blurry.</li>
<li><b>Use PNG for text and logos,</b> JPG for photos. Platforms compress JPGs more, so fine text can look rough.</li>
<li><b>Watch file-size limits.</b> If an upload fails, run the image through the <a href="{R}compress-image-to-500kb/">500 KB</a> or <a href="{R}compress-image-to-1mb/">1 MB</a> compressor.</li></ul>

<div class="warnbox">Platforms update their layouts and recommended sizes from time to time. These sizes work at the time of writing; check each platform's help centre if something looks off after uploading.</div>''',
        faq=[("What is the best size for an Instagram post?", "1080 × 1080 for square posts or 1080 × 1350 for portrait posts, which take up more of the feed."),
             ("What size is a YouTube thumbnail?", "1280 × 720 pixels (16:9), at least 640 px wide, saved as JPG, PNG or GIF under YouTube's upload limit."),
             ("Why does my image look blurry after uploading?", "Usually because it was smaller than the size the platform shows it at, so it was stretched. Start from a larger image and resize it down.")],
    ),
]
