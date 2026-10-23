# Changes driven by real Google Search Console data (queries the site already shows up for).
# Week of 16 Oct 2026: 28-day data, 38 impressions, 21 queries, average position 43.
# Rules from GROWTH.md: max 5 title/description rewrites a week (pages with impressions but CTR < 1%),
# and answers/FAQs that match the exact searches people typed.

# slug -> (title, description). Pages with impressions and 0 clicks.
TITLES = {
    "resize-image-to-3000x3000": (
        "Resize Image to 3000x3000 – Convert Any Photo to 3000 x 3000",
        "Convert any image to exactly 3000 × 3000 pixels in seconds: square cover art for Spotify, Apple Music and podcasts. Free, no upload, no watermark."),
    "resize-image-to-1080x1920": (
        "1080x1920 Resize – Make Any Photo 1080 x 1920 (9:16) Free",
        "Turn any photo into the 1080 × 1920 px vertical format (9:16) for Instagram Stories, Reels, TikTok and WhatsApp status. Free, no upload, no watermark."),
    "resize-image-to-2560x1440": (
        "Resize Image to 2560x1440 px (QHD / 1440p) Free Online",
        "Resize any photo to exactly 2560 × 1440 pixels (QHD, 16:9) for YouTube banners, wallpapers and screens. Free, works in your browser, no upload."),
    "compress-pdf-to-1mb": (
        "Compress PDF to 1MB – Make a PDF Less Than 1 MB Free",
        "Reduce PDF size to under 1 MB for email, WhatsApp and upload forms. The sharpest quality that fits is picked for you. Free, no upload, no sign-up."),
    "remove-background": (
        "Remove Background from Image Free – Transparent PNG",
        "Remove the background from any photo in one click and download a transparent PNG. Free with no limits or credits: the AI runs in your browser."),
}

# slug -> (quick answer shown at the top of the page text, [extra FAQs])
ANSWERS = {
    "resize-image-to-3000x3000": (
        "To convert an image to 3000 × 3000 px: choose your photo, leave the size at 3000 × 3000, pick <b>Crop to fill</b> for a full square (or <b>Fit with white border</b> to keep the whole picture), then press <b>Resize</b> and download.",
        [("My photo is smaller than 3000 px. Will it work?", "Yes, it is enlarged to 3000 × 3000. Enlarging cannot add detail, though, so start from the largest original you have. Music distributors may reject cover art that looks blurry or pixelated."),
         ("Is 3000 × 3000 px a square?", "Yes, it is a 1:1 square. A rectangular photo has to be cropped or given a border to become square, and you choose which.")]),
    "resize-image-to-1080x1920": (
        "1080 × 1920 is the vertical Full HD format: 1080 px wide and 1920 px tall, a 9:16 shape. It is the same as 1920 × 1080 turned on its side, and it fills a phone screen exactly.",
        [("What is 1080x1920 format?", "A vertical 9:16 image or video frame, 1080 pixels wide and 1920 tall. Stories, Reels, TikTok, YouTube Shorts and WhatsApp status all use it."),
         ("Is 1080x1920 the same as 1920x1080?", "Same number of pixels, different direction. 1920 × 1080 is landscape (16:9); 1080 × 1920 is portrait (9:16).")]),
    "resize-image-to-2560x1440": (
        "2560 × 1440 px is QHD, often called 1440p or 2K: a 16:9 widescreen size with four times the pixels of 1280 × 720. Choose a photo, keep the size at 2560 × 1440 and press <b>Resize</b>.",
        [("Is 2560x1440 the same as 1440p or QHD?", "Yes. 2560 × 1440 is called QHD or 1440p, and it is also sold as “2K” on many monitors. It is a 16:9 shape."),
         ("Can I use a 2560x1440 image as a wallpaper?", "Yes. It fills a 1440p monitor exactly and looks sharp on a 1080p screen too.")]),
    "resize-image-to-600x600": (
        "To make a picture 600 × 600 pixels: choose the photo, leave the size at 600 × 600, choose <b>Crop to fill</b> so there is no empty space, press <b>Resize</b> and download. It works on phones too.",
        [("How do I make a picture 600x600 pixels on my phone?", "Open this page in your phone's browser, choose the photo from your gallery and press Resize. No app is needed, and the photo is not uploaded.")]),
    "resize-image-to-400x400": (
        "To make an image 400 × 400 px: choose it, keep the size at 400 × 400, pick <b>Crop to fill</b> for a full square and press <b>Resize</b>.",
        [("What is a 400x400 image used for?", "Mostly profile pictures (LinkedIn, Discord, Slack, forums), small logos and product thumbnails. It's a 1:1 square.")]),
    "resize-image-to-1280x720": (
        None,
        [("Is 1280x720 the same as 720p HD?", "Yes. 1280 × 720 is 720p HD, a 16:9 shape. 1920 × 1080 is Full HD (1080p).")]),
    "resize-image-to-1920x1080": (
        None,
        [("Is this 1920x1080 resizer really free?", "Yes. There is no sign-up, limit or watermark, and the photo is resized on your device without being uploaded.")]),
    "compress-pdf-to-1mb": (
        "To make a PDF less than 1 MB: choose the file, keep the target at 1 MB and press <b>Compress PDF</b>. The tool keeps the sharpest version that still fits under 1 MB.",
        [("How do I check if my PDF is under 1 MB?", "On Windows, right-click the file and choose Properties. On a Mac, select it and press Cmd + I. On a phone, open the file's details in your Files app. 1 MB is 1,024 KB.")]),
    "compress-pdf-to-100kb": (
        None,
        [("Can every PDF get under 100 KB?", "Short documents and single-page scans usually can. Long PDFs with many photos may need to be split into parts first.")]),
    "compress-image-to-10kb": (
        None,
        [("What does a 10 KB photo look like in pixels?", "A 10 KB JPG is usually around 150 × 200 pixels, enough for a signature or a tiny form photo. The exact size depends on how much detail the picture has.")]),
    "passport-photo-maker": (
        None,
        [("How is a passport size photo measured?", "Most countries use 35 × 45 mm (3.5 × 4.5 cm, about 1.4 × 1.8 inches), measured on the printed photo. The US uses 2 × 2 inches (51 × 51 mm). At 300 dpi, 35 × 45 mm is about 413 × 531 pixels.")]),
    "china-visa-photo": (
        None,
        [("How do I crop a photo for a China visa?", "Choose your photo here: the frame is already set to 33 × 48 mm. Move and zoom until your head fits the guide, then download. Check the online visa form's pixel and file-size limits before uploading.")]),
    "password-generator": (
        None,
        [("How long should a strong password be?", "Longer is stronger. Security guidance commonly recommends at least 12–16 characters, and a password manager makes long random passwords easy to use.")]),
}

# Compress-to-KB pages: how to check the size, matched to "photo size" searches.
KB_CHECK = ("How do I check my photo's size in KB?", "On Windows, right-click the photo and choose Properties. On a Mac, select it and press Cmd + I. On Android or iPhone, open the photo and look at its details or info. The tool also shows the new size after compressing.")


def enrich(T):
    for t in T:
        s = t["slug"]
        if s in TITLES:
            t["title"], t["desc"] = TITLES[s]
        if s in ANSWERS:
            quick, faqs = ANSWERS[s]
            if quick:
                t["body"] = f'<p class="quick"><b>Quick answer:</b> {quick}</p>' + t["body"]
            t["faq"] = list(t.get("faq", [])) + faqs
        if t.get("parent") == "compress-image":
            t["faq"] = list(t.get("faq", [])) + [KB_CHECK]
