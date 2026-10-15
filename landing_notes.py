# Page-specific content for the SEO landing pages, so each preset page explains
# its own use case instead of repeating the parent tool's text.
# Platform sizes change from time to time: every note tells the reader to check
# the platform's current help page.

RESIZE_NOTES = {
    (1080, 1080): ('''<h2>Getting a square Instagram post right</h2><p>1080 × 1080 px is the classic 1:1 Instagram post. Instagram shows feed images 1080 px wide, so a bigger square is scaled down anyway and a smaller one looks soft on modern phones.</p>
<ul><li><b>Keep the subject in the middle.</b> The profile grid shows a taller, cropped preview of each post, so edges near the top and bottom may be hidden there.</li><li><b>Text:</b> leave about 60 px of space on every side so captions and buttons never sit on top of your words.</li><li><b>Carousels:</b> every slide uses the shape of the first one. Resize all slides to 1080 × 1080 before uploading.</li></ul>
<p>Same square also works for Facebook feed posts and LinkedIn image posts.</p>''',
                   ("Should I use 1080×1080 or 1080×1350 for Instagram?", "Square is safest for grids and carousels. Portrait 1080×1350 takes more space in the feed, so it often gets more attention. See the 1080×1350 page.")),
    (1080, 1920): ('''<h2>Stories, Reels and TikTok: mind the safe zone</h2><p>1080 × 1920 px is the full-screen vertical 9:16 shape used by Instagram Stories and Reels, TikTok, YouTube Shorts, Facebook Stories and WhatsApp status.</p>
<ul><li><b>Top 250 px:</b> covered by the profile name, progress bar and close button.</li><li><b>Bottom 350 px:</b> covered by the caption, reply box and music label.</li><li><b>Right edge:</b> on Reels and TikTok the like, comment and share buttons sit here.</li></ul>
<p>Put important text and faces in the central area. If your photo is landscape, choose <b>Fit with white border</b> to keep all of it, or <b>Crop to fill</b> and make sure the subject is in the centre.</p>''',
                   ("Why does my story photo look zoomed in?", "The photo was not 9:16, so the app cropped it to fill the screen. Resize it to 1080×1920 first and you decide what gets cut.")),
    (1200, 630): ('''<h2>The size behind link previews</h2><p>When you share a link on Facebook, LinkedIn, X, WhatsApp or Slack, the preview picture comes from the page's Open Graph image. 1200 × 630 px (about 1.91:1) is the size most of these apps are built around.</p>
<ul><li><b>Keep text big and central.</b> Some apps crop the preview to a square or show it as a small thumbnail.</li><li><b>Website owners:</b> save the result as JPG under 1 MB and set it in the <code>og:image</code> tag of your page.</li><li><b>Refresh the cache:</b> apps remember old previews. Facebook's Sharing Debugger and LinkedIn's Post Inspector can fetch the new image.</li></ul>''',
                  ("Can I use 1200×630 for normal Facebook posts?", "Yes. It shows as a wide landscape image. For a post that fills more of the feed, use a square or 4:5 portrait size instead.")),
    (1280, 720): ('''<h2>YouTube thumbnail checklist</h2><p>YouTube recommends custom thumbnails of 1280 × 720 px (16:9), at least 640 px wide, saved as JPG, PNG or GIF and kept under its upload limit (2 MB at the time of writing).</p>
<ul><li><b>Bottom-right corner:</b> the video length badge covers it, so keep text and faces away from there.</li><li><b>Readable when tiny:</b> thumbnails often show at phone size. Use 3–5 large words at most.</li><li><b>Too big a file?</b> Run the resized image through the <a href="../compress-image-to-500kb/">500 KB compressor</a>.</li></ul>
<p>1280 × 720 is also standard HD (720p) for slides and video frames.</p>''',
                  ("Why is my YouTube thumbnail rejected?", "Usually because the file is over the size limit. Resize to 1280×720 and compress it below 2 MB, then upload again.")),
    (600, 600): ('''<h2>Digital passport and visa uploads</h2><p>Several online photo uploads, including the US passport and visa systems, ask for a square digital photo. 600 × 600 px is the common minimum: 2 × 2 inches at 300 dpi.</p>
<ul><li>This page only changes the pixel size. For head size, background colour and other rules, use the <a href="../us-passport-photo/">US passport photo maker</a>, which crops around your face.</li><li>Many systems also limit the file size. After resizing, use <a href="../compress-image-to-200kb/">compress to 200 KB</a> if your file is too big.</li><li>Rules change: always check the latest requirements on the official government website before you submit.</li></ul>''',
                 ("Is 600×600 the same as 2×2 inches?", "Yes, when printed at 300 dots per inch: 600 ÷ 300 = 2 inches. Online forms care about the pixels; printers care about the dpi.")),
    (400, 400): ('''<h2>Profile pictures are shown as circles</h2><p>LinkedIn, Discord, Slack, Zoom, Google and most forums display your profile photo as a circle, but you upload a square. 400 × 400 px is sharp on every screen without being heavy.</p>
<ul><li><b>Corners are cut off.</b> Keep your face in the middle, with a little space above your head.</li><li><b>Fill the frame:</b> head and shoulders should take up about 60% of the picture, so you are recognisable at small sizes.</li><li><b>Plain background:</b> a busy background is distracting at thumbnail size. Try the <a href="../remove-background/">background remover</a> first.</li></ul>''',
                 ("Will 400×400 look blurry on LinkedIn?", "No. LinkedIn shows profile photos much smaller than 400 px, so it stays sharp. Start from a clear photo; resizing can't add detail that isn't there.")),
    (1920, 1080): ('''<h2>Full HD for screens, slides and video</h2><p>1920 × 1080 px (1080p) is the most common screen resolution, and the 16:9 shape of PowerPoint and Google Slides widescreen decks, YouTube videos and most TVs.</p>
<ul><li><b>Wallpapers:</b> fills a Full HD laptop or monitor exactly. For a 4K screen, a 3840 × 2160 original looks sharper.</li><li><b>Slides:</b> a 1920 × 1080 background image fills a widescreen slide edge to edge without stretching.</li><li><b>Video:</b> a still frame at this size drops into a 1080p video editor timeline without black bars.</li></ul>
<p>Vertical phone photos can't fill a landscape frame. Choose <b>Fit with white border</b> to keep the whole photo.</p>''',
                   ("Is 1920×1080 the same as 16:9?", "Yes. 1920 ÷ 1080 = 16 ÷ 9. Other 16:9 sizes include 1280×720 (HD) and 2560×1440 (QHD).")),
    (1584, 396): ('''<h2>LinkedIn banner: what actually shows</h2><p>LinkedIn's personal profile background is 1584 × 396 px, a wide 4:1 strip.</p>
<ul><li><b>Bottom-left is hidden</b> behind your profile photo, on desktop and even more on mobile.</li><li><b>Mobile crops the sides,</b> so keep text and logos in the centre and right-hand side.</li><li><b>Keep it simple:</b> a tagline, your website or a clean photo works better than a lot of small text.</li></ul>
<p>Company pages use a different cover size, so check LinkedIn's help page for business pages.</p>''',
                  ("Why is my LinkedIn banner blurry?", "The image was smaller than 1584 px wide and LinkedIn stretched it. Start from a large photo and resize it down to 1584×396.")),
    (1500, 500): ('''<h2>X (Twitter) header tips</h2><p>The header on an X profile is 1500 × 500 px, a 3:1 strip.</p>
<ul><li><b>Bottom-left</b> is covered by your round profile picture.</li><li><b>Top and bottom</b> are trimmed on some screens, so keep the important part in the middle band.</li><li><b>JPG or PNG</b> both work. Use PNG for logos and text so the edges stay crisp.</li></ul>
<p>Uploading a wide photo? <b>Crop to fill</b> gives a full header with no white edges.</p>''',
                  ("Can I use the same image for LinkedIn and X?", "Not exactly: X is 3:1 and LinkedIn is 4:1. Resize the same photo twice, once to 1500×500 and once to 1584×396.")),
    (2560, 1440): ('''<h2>YouTube banner and the safe area</h2><p>YouTube channel art is uploaded at 2560 × 1440 px (16:9), but different devices show different parts of it.</p>
<ul><li><b>Safe area:</b> only a central strip of about 1546 × 423 px is visible everywhere, including phones. Put your channel name, logo and upload schedule there.</li><li><b>TVs</b> show the whole image; desktops show a wide band across the middle.</li><li><b>Minimum size</b> is 2048 × 1152 px, and the file must be under 6 MB at the time of writing.</li></ul>''',
                   ("Why is my YouTube banner text cut off on mobile?", "It was outside the central safe area. Move text into the middle 1546×423 px and upload again.")),
    (1080, 1350): ('''<h2>Why 4:5 portrait wins in the feed</h2><p>1080 × 1350 px is the tallest shape Instagram allows for feed photos (4:5). It fills about 25% more of the screen than a square, so people see more of your photo while scrolling.</p>
<ul><li><b>Phone photos</b> are usually 3:4, a little taller than 4:5. Crop to fill trims a thin strip from the top and bottom.</li><li><b>Carousels:</b> the first slide sets the shape for all slides, so resize every image to 1080 × 1350.</li><li><b>Facebook</b> also shows 4:5 portrait images in full.</li></ul>''',
                   ("Will Instagram crop a 1080×1350 photo?", "Not in the feed: 4:5 is shown in full. The profile grid shows a slightly different crop, so keep the subject centred.")),
    (851, 315): ('''<h2>Facebook cover photo: desktop vs phone</h2><p>851 × 315 px is the long-standing Facebook cover size for pages and profiles. Desktop shows a wide strip; phones show a taller crop and cut off the left and right edges.</p>
<ul><li><b>Keep important content in the centre.</b> Anything near the edges may be hidden on phones.</li><li><b>Profile photo overlap:</b> on some layouts your profile picture covers the bottom-left.</li><li><b>Sharper result:</b> for logos and text, save as PNG. Facebook compresses JPG covers more.</li></ul>
<p>Facebook adjusts its layout from time to time, so preview your cover on both desktop and phone after uploading.</p>''',
                 ("Why does my Facebook cover look different on my phone?", "The mobile app crops the sides to fit a taller shape. Keep text and faces in the middle so they show on every device.")),
    (1000, 1500): ('''<h2>Pinterest pins that stand out</h2><p>Pinterest recommends a 2:3 vertical shape, and 1000 × 1500 px is the standard pin size.</p>
<ul><li><b>Much taller pins get cut off</b> in the feed, so 2:3 is the safest choice.</li><li><b>Add a text overlay</b> describing what people will get, like “5 tips for…”. It helps pins get saved and clicked.</li><li><b>Brand subtly:</b> a small logo or website name at the bottom keeps the pin linked to you when it is re-shared.</li></ul>''',
                   ("Can I pin a square image?", "Yes, but vertical 2:3 pins take up more space in the feed and usually perform better.")),
    (500, 500): ('''<h2>Profile pictures for WhatsApp, Telegram and Signal</h2><p>Chat apps show your photo as a small circle and compress it heavily. 500 × 500 px is plenty and uploads instantly on slow connections.</p>
<ul><li><b>Circle crop:</b> keep your face in the centre; the corners are never seen.</li><li><b>Group icons</b> work the same way. A logo or simple symbol is easier to recognise than a busy photo.</li><li><b>Business accounts:</b> use your logo on a plain background so customers recognise you in their chat list.</li></ul>''',
                 ("Why does WhatsApp cut my DP?", "WhatsApp needs a square and crops anything else. Resize to 500×500 with Fit with white border to keep the whole picture.")),
    (1024, 1024): ('''<h2>App icons, logos and AI images</h2><p>1024 × 1024 px is a common master size for square artwork.</p>
<ul><li><b>Apple App Store</b> asks for a 1024 × 1024 px icon, and Apple's guidelines say it should have no transparency.</li><li><b>Google Play</b> uses a 512 × 512 px icon. Make it from the same 1024 px master.</li><li><b>AI tools:</b> many image generators and editors work with square 1024 × 1024 inputs and outputs.</li><li><b>Favicons and social logos</b> can all be cut down from a 1024 px original without losing quality.</li></ul>
<p>Always design big and scale down: enlarging a small logo makes it blurry.</p>''',
                   ("Can I make an app icon from a rectangular logo?", "Yes. Choose Fit with white border to place the whole logo on a white square, or crop to fill if the logo has space around it.")),
    (3000, 3000): ('''<h2>Cover art for music and podcasts</h2><p>Music distributors that deliver to Spotify, Apple Music and other stores commonly ask for square cover art of 3000 × 3000 px. Apple Podcasts accepts square artwork between 1400 and 3000 px.</p>
<ul><li><b>Start from a big image.</b> Enlarging a small photo to 3000 px makes it bigger but not sharper, and some distributors reject blurry art.</li><li><b>Readable at thumbnail size:</b> covers are mostly seen tiny, so keep the title short and bold.</li><li><b>Format:</b> JPG or PNG in RGB colour is the usual requirement. Check your distributor's current rules.</li></ul>''',
                   ("Is 3000×3000 too big to upload?", "Usually not. If your distributor has a file-size limit, compress the result with the 2 MB or 5 MB compressor.")),
}

PDF_NOTES = {
    100: ('''<h2>What fits in 100 KB?</h2><p>100 KB is a very tight limit. Roughly, it fits one or two scanned pages at readable quality, for example an ID card (front and back), a single certificate or a fee receipt.</p>
<ul><li><b>Scan in black and white or greyscale</b> if colour isn't required. It halves the size.</li><li><b>One page per file:</b> if the portal lets you upload documents separately, split them with <a href="../split-pdf/">Split PDF</a>.</li><li><b>Crop the scan</b> to the document edges before making the PDF: table and background add size.</li></ul>''',
          ("Can a 10-page PDF fit in 100 KB?", "Rarely, unless it is plain text. For scanned pages, upload fewer pages or ask whether the portal allows a larger file.")),
    200: ('''<h2>What fits in 200 KB?</h2><p>200 KB comfortably fits two to four scanned pages, such as a mark sheet, a degree certificate or a short letter.</p>
<ul><li><b>Combine front and back</b> of a card on one page before scanning: one page is smaller than two.</li><li><b>Phone scans:</b> take the photo in daylight on a dark surface. Clean, even backgrounds compress much better than shadows.</li><li><b>Needs to be under 200 KB exactly?</b> The tool aims just under the limit, so the file is accepted even by strict portals.</li></ul>''',
          ("Why is my scanned PDF so big?", "Phone cameras save very detailed pictures. Each page is a large photo inside the PDF. Compressing re-saves those pictures smaller.")),
    300: ('''<h2>What fits in 300 KB?</h2><p>300 KB is common on visa and admission forms. It holds roughly three to six scanned pages: a short bank statement, a reference letter or a set of transcripts.</p>
<ul><li><b>Remove blank pages</b> and cover sheets before compressing.</li><li><b>Merge first, then compress:</b> if a form wants all documents in one file, join them with <a href="../merge-pdf/">Merge PDF</a> and then set the target to 300 KB.</li><li><b>Check readability:</b> zoom in on small print such as account numbers before you submit.</li></ul>''',
          ("Should I merge before or after compressing?", "Merge first, then compress the single file to the limit. Compressing pieces separately often ends up larger than the limit when joined.")),
    500: ('''<h2>What fits in 500 KB?</h2><p>500 KB is a comfortable size for emails and most upload forms. It fits around five to ten scanned pages, or a CV with a photo and a few pages of text.</p>
<ul><li><b>CVs and résumés</b> exported from Word are usually already small. If yours is large, a high-resolution photo inside is the likely cause.</li><li><b>Text-only PDFs</b> made from Word or Google Docs are often under 500 KB already. Try uploading the original first.</li><li><b>Readable on phones:</b> at 500 KB scans stay clear when recruiters open them on a phone.</li></ul>''',
          ("Will compressing my CV make the text unselectable?", "Yes: pages are saved as images, so text can't be copied. If the employer's system reads CVs automatically, send the original Word export instead when it fits.")),
    1024: ('''<h2>What fits in 1 MB?</h2><p>1 MB is the limit on many university and job portals. It holds roughly ten to twenty scanned pages at good quality, or a short report with photos.</p>
<ul><li><b>Application packs:</b> merge your certificates, ID and letters into one file, then compress to 1 MB.</li><li><b>Photos inside:</b> PDFs full of photos shrink the most.</li><li><b>Sharing on WhatsApp or email:</b> a 1 MB PDF opens quickly even on slow mobile data.</li></ul>''',
           ("My PDF is 1.2 MB. Will compressing to 1 MB hurt quality?", "Barely. The tool only lowers quality as much as needed, so a small cut like this is usually invisible.")),
    2048: ('''<h2>What fits in 2 MB?</h2><p>2 MB fits twenty to forty scanned pages, a thesis chapter with figures or a full set of supporting documents for an application.</p>
<ul><li><b>Large scanned books or notes:</b> split them into chapters with <a href="../split-pdf/">Split PDF</a> if they still don't fit.</li><li><b>Figures and charts</b> stay readable at 2 MB, but check small labels after compressing.</li><li><b>Text PDFs</b> exported from Word rarely need compressing. Their size usually comes from embedded images.</li></ul>''',
           ("How many pages can I fit in 2 MB?", "It depends on the content. Plain text pages are tiny; colour photo pages are big. For typical phone scans, expect twenty to forty pages.")),
    5120: ('''<h2>What fits in 5 MB?</h2><p>5 MB is a generous limit: large reports, design portfolios, photo-heavy presentations saved as PDF and long scanned documents.</p>
<ul><li><b>Email:</b> most email services accept attachments much bigger than 5 MB, but smaller files send faster and fit in mailboxes with limited space.</li><li><b>Portfolios:</b> at 5 MB photos still look sharp on a laptop screen.</li><li><b>Still over 5 MB?</b> Very long scans may need to be split into two files.</li></ul>''',
           ("Is 5 MB small enough for email?", "Yes, for almost every email service. Some company mail servers set lower limits; compress to 2 MB if a message bounces.")),
}

IMG_NOTES = {
    10: ('''<h2>Where 10 KB limits appear</h2><p>10 KB is the smallest common limit, and it is mostly used for <b>signature</b> and <b>thumb impression</b> uploads on exam and government forms. A full colour photo cannot look good at 10 KB, so crop tightly around the signature, and use black ink on white paper.</p>''',
         ("Can a passport-size photo be 10 KB?", "Only at a very small size. Most forms that ask for 10 KB want a signature, not a photo. Check whether the photo field allows 20–50 KB.")),
    20: ('''<h2>Where 20 KB limits appear</h2><p>Many forms ask for a <b>signature under 20 KB</b> and a <b>photo under 50 KB</b>. If the form gives a range like “10–20 KB”, set the target to 20 KB so you stay above the minimum. Convert the result to JPG if the portal does not accept PNG.</p>''',
         ("My file is 21 KB. Why is it rejected?", "Portals count 1 KB as 1024 bytes and check the exact number. This tool aims just under the target, so the result passes strict checks.")),
    30: ('''<h2>Where 30 KB limits appear</h2><p>30 KB is typical for <b>small face photos</b> on exam admit cards and student forms. At this size a passport-style head-and-shoulders photo still looks clear, as long as it is cropped first. Make the correct shape with the <a href="../passport-photo-maker/">passport photo maker</a>, then compress.</p>''',
         ("Should I crop before compressing?", "Yes. Cropping removes pixels you don't need, so the remaining face keeps more detail at 30 KB.")),
    50: ('''<h2>Where 50 KB limits appear</h2><p>50 KB is one of the most common photo limits on <b>government, exam and recruitment portals</b>. Many forms ask for a photo between 20 and 50 KB together with a size in centimetres. Follow the size in cm first, then use this page to bring the file under 50 KB.</p>''',
         ("Will 50 KB be clear enough for an ID card?", "Yes, for a cropped face photo. 50 KB keeps a passport-size photo sharp at the size it is printed on cards.")),
    100: ('''<h2>Where 100 KB limits appear</h2><p>100 KB is common on <b>job portals, visa forms and scholarship applications</b>, both for photos and for single-page scans such as an ID card. It is also a good size for photos you send by email to many people.</p>''',
          ("Can I compress a scanned document to 100 KB?", "Yes, if it is one page. Save it as JPG and compress here. For multi-page documents, use Compress PDF to 100 KB.")),
    200: ('''<h2>Where 200 KB limits appear</h2><p>200 KB suits <b>online profiles, marketplace listings and website images</b>. Smaller images make web pages load faster, which helps both visitors and search rankings, while 200 KB still looks sharp on phones and laptops.</p>''',
          ("Is 200 KB good for website images?", "Yes. For blog photos and product images, 100–200 KB is a good balance of quality and speed.")),
    500: ('''<h2>Where 500 KB limits appear</h2><p>500 KB is useful for <b>high-quality photos that still upload quickly</b>: online shop products, portfolios, real-estate listings and photos sent over mobile data. Viewers can still zoom in a little without seeing blur.</p>''',
          ("Is 500 KB enough to print a photo?", "For small prints such as 4×6 inch, usually yes. For larger prints, keep a bigger original.")),
    1024: ('''<h2>Where 1 MB limits appear</h2><p>Many <b>forms, CMS uploads and email systems</b> set a 1 MB limit per image. A phone photo is often 3–5 MB, so it needs compressing, but at 1 MB it still looks nearly identical to the original on any screen.</p>''',
           ("Is 1 MB the same as 1000 KB?", "Not exactly. Most upload forms treat 1 MB as 1024 KB. This tool uses 1024 KB, so the result passes either way.")),
    2048: ('''<h2>Where 2 MB limits appear</h2><p>2 MB is a common limit on <b>job, university and support-ticket portals</b>, and for profile photos on some sites. At 2 MB a typical phone photo keeps almost all its detail, so this is a good choice when quality matters.</p>''',
           ("My photo is 2.4 MB. Will it look worse at 2 MB?", "You won't see a difference. The tool removes only as much as needed to get under 2 MB.")),
    5120: ('''<h2>Where 5 MB limits appear</h2><p>5 MB limits are common for <b>contest entries, print-shop uploads and attachment fields</b> in online forms. Newer phones with 48 MP or larger cameras often save photos over 5 MB, so they need a light compression to fit.</p>''',
           ("Do I need to compress a 12-megapixel photo for a 5 MB limit?", "Often not: most 12 MP JPG photos are 2–5 MB already. If it is under 5 MB, the tool keeps it as it is.")),
}

OCR_USES = {
    "urd": ("Urdu", "Students copy passages from Urdu textbooks and digests, writers pull quotes from newspaper cuttings, and families digitise old letters and Islamic books printed in Nastaliq.", "Urdu books and documents"),
    "ara": ("Arabic", "People use it to copy text from Arabic documents, contracts, Gulf job offers, menus and screenshots of messages, and to search printed books.", "official documents from Gulf countries"),
    "hin": ("Hindi", "Common uses include copying text from Hindi newspapers, government notices, school books and WhatsApp forwards shared as images.", "government notices and newspapers"),
    "spa": ("Spanish", "Useful for copying text from Spanish textbooks, receipts, contracts and screenshots, and for pasting it into a translator.", "letters, receipts and contracts"),
    "fra": ("French", "Students and professionals use it for French course material, administrative letters, forms and printed articles.", "administrative letters and forms"),
    "deu": ("German", "Handy for German letters from offices (Behörden), contracts, invoices and university material, especially before translating them.", "official letters and invoices"),
    "por": ("Portuguese", "Used for documents from Brazil and Portugal: bills, contracts, school material and screenshots of messages.", "bills and contracts"),
    "ita": ("Italian", "Useful for Italian recipes, printed articles, university notes and documents that need translating.", "printed articles and notes"),
    "rus": ("Russian", "Copies Cyrillic text from Russian documents, books, scanned articles and screenshots, so you can edit or translate it.", "books and scanned articles"),
    "tur": ("Turkish", "Copies Turkish text, including letters such as ç, ğ, ı, ö, ş and ü, from documents, books and screenshots.", "documents and books"),
    "ben": ("Bengali", "Used for Bangla newspapers, textbooks, government circulars and images shared on social media.", "newspapers and circulars"),
    "ind": ("Indonesian", "Copies Indonesian text from letters, receipts, school material and screenshots, ready to edit or translate.", "receipts and letters"),
    "chi_sim": ("Chinese", "Copies Simplified Chinese text from documents, product labels, signs and screenshots of chat apps, ready to paste into a translator.", "product labels and screenshots"),
}

EXTRA_TOOLS = {
    "password-generator": ('''<h2>How long should a password be?</h2><p>Each extra character multiplies the number of possible passwords. A random 16-character password using letters, numbers and symbols has so many combinations that guessing it is not practical with today's computers. Short passwords and real words are the weak point.</p>
<h2>Generated on your device</h2><p>Passwords are created in your browser with its built-in secure random number generator. They are never sent to us or stored anywhere. Copy the password straight into your password manager.</p>''',
                           [("Is it safe to use an online password generator?", "Yes, if it runs in your browser like this one. Nothing is sent over the internet, so no one else sees the password.")]),
    "percentage-calculator": ('''<h2>Common percentage questions</h2><ul><li><b>What is 15% of 80?</b> Multiply: 80 × 15 ÷ 100 = 12.</li><li><b>20 is what percent of 80?</b> Divide: 20 ÷ 80 × 100 = 25%.</li><li><b>Change from 50 to 65?</b> (65 − 50) ÷ 50 × 100 = 30% increase.</li></ul>
<p>For shopping prices, the <a href="../discount-calculator/">discount calculator</a> shows the final price and how much you save.</p>''',
                              [("How do I add a percentage to a number?", "Multiply by 1 plus the percentage. For example, 200 plus 10% = 200 × 1.10 = 220.")]),
    "word-counter": ('''<h2>Common word limits</h2><ul><li><b>University essays</b> often allow 10% above or below the set word count. Check your course rules.</li><li><b>Personal statements and cover letters</b> are usually 400–650 words.</li><li><b>Abstracts</b> are often limited to 150–300 words.</li></ul>
<p>Your text stays in your browser and is never uploaded. Need a character limit instead? Use the <a href="../character-counter/">character counter</a>.</p>''',
                     [("Does the word counter count hyphenated words as one?", "Yes. Words joined by a hyphen, like “well-known”, count as one word, the same as most word processors.")]),
}


def enrich(T):
    for t in T:
        p = t.get("preset") or {}
        note = None
        if t.get("parent") == "resize-image":
            note = RESIZE_NOTES.get((p.get("#rw"), p.get("#rh")))
        elif t.get("parent") == "compress-pdf":
            note = PDF_NOTES.get(p.get("#ptkb"))
        elif t.get("parent") == "compress-image":
            note = IMG_NOTES.get(p.get("#tkb"))
        elif t.get("parent") == "image-to-text" and p.get("#ol") in OCR_USES:
            lang, uses, src = OCR_USES[p["#ol"]]
            note = (f'<h2>What people use {lang} OCR for</h2><p>{uses}</p>'
                    f'<p>After extracting, paste the text into Word or Google Docs to fix any mistakes. For multi-page {src}, '
                    f'turn each page into an image with <a href="../pdf-to-jpg/">PDF to JPG</a> first, then extract them one by one.</p>',
                    (f"Can I extract {lang} text from a PDF?", f"Yes. Convert the PDF pages to images with PDF to JPG, then run each image through {lang} OCR. If the PDF already has selectable text, PDF to Word is faster."))
        if note:
            t["body"] += note[0]
            t["faq"] = list(t.get("faq", [])) + [note[1]]
        if t["slug"] in EXTRA_TOOLS:
            body, faq = EXTRA_TOOLS[t["slug"]]
            t["body"] += body
            t["faq"] = list(t.get("faq", [])) + faq
