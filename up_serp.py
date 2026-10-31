"""SERP-driven changes (1 Nov 2026). The owner exported the Google top 10 for 14 keywords. Pages ranking there for
1024x1024, 3000x3000, 500x500 and 1080x1920 are mostly small sites (DR 0-31) whose titles say "Image Converter"
(Search Console also shows "1024x1024 image converter" and "3000x3000 image converter" queries) and whose pages
explain the size in more depth. Here: matching titles and a size-facts section with figures computed from the pixels."""

TITLE = {
    "resize-image-to-1024x1024": "1024x1024 Image Converter – Resize Image to 1024x1024 Free",
    "resize-image-to-3000x3000": "3000x3000 Image Converter – Resize Image to 3000x3000 Free",
    "resize-image-to-500x500": "500x500 Image Converter – Resize a Photo or PFP to 500x500",
}


def _table(w, h, rows):
    body = "".join(f"<tr><td>{d} dpi</td><td>{a}</td><td>{b}</td></tr>" for d, a, b in rows)
    return (f'<div class="scroll"><table class="t"><caption>{w} × {h} pixels printed at common resolutions</caption>'
            f'<thead><tr><th>Print resolution</th><th>Inches</th><th>Centimetres</th></tr></thead><tbody>{body}</tbody></table></div>')


SECTIONS = {
    "resize-image-to-1024x1024": ('''<h2>1024 × 1024 in numbers</h2>
<p>A 1024 × 1024 image is a 1:1 square of about 1.05 megapixels. That is a fraction of a phone photo (usually 12 megapixels or more), so a phone picture always has enough detail to fill it without looking soft.</p>'''
        + _table(1024, 1024, [(72, "14.22 × 14.22", "36.12 × 36.12"), (150, "6.83 × 6.83", "17.34 × 17.34"), (300, "3.41 × 3.41", "8.67 × 8.67")]) + '''
<h2>Converting a rectangular photo to 1024 × 1024</h2>
<ul><li><b>Crop to fill</b> cuts the long sides so the square is filled edge to edge: best for faces, products and icons.</li><li><b>Fit with white border</b> keeps the whole picture and adds white bars: best for logos, screenshots and documents.</li><li>To keep a transparent background for an icon, start from a PNG; JPG files have no transparency.</li></ul>''',
        [("What is 1024x1024 in inches?", "It depends on the print resolution: 3.41 × 3.41 inches at 300 dpi, 6.83 inches at 150 dpi and 14.22 inches at 72 dpi. On screens only the pixels matter."),
         ("Is 1024x1024 good quality?", "Yes for icons, profile pictures and web images. For large prints, 3000 × 3000 or the original photo is better.")]),
    "resize-image-to-3000x3000": ('''<h2>3000 × 3000 in numbers</h2>
<p>3000 × 3000 pixels is a 1:1 square of 9 megapixels. Printed at 300 dpi it is exactly 10 × 10 inches (25.4 cm), which is why it is the usual size for album covers and print-ready square artwork.</p>'''
        + _table(3000, 3000, [(72, "41.67 × 41.67", "105.83 × 105.83"), (150, "20 × 20", "50.8 × 50.8"), (300, "10 × 10", "25.4 × 25.4")]) + '''
<h2>Upscaling a small image to 3000 × 3000</h2>
<p>The converter can enlarge any image to 3000 × 3000, but enlarging adds pixels, not detail. A 1000-pixel logo stretched to 3000 pixels will look slightly soft up close. If a distributor rejects your cover for low quality, export it again from the original design file at 3000 × 3000.</p>''',
        [("How many megapixels is 3000x3000?", "9 megapixels (3000 × 3000 = 9,000,000 pixels)."),
         ("What is 3000x3000 in inches?", "10 × 10 inches at 300 dpi, 20 × 20 inches at 150 dpi.")]),
    "resize-image-to-500x500": ('''<h2>500 × 500 in numbers</h2>
<p>500 × 500 pixels is a 1:1 square of a quarter of a megapixel, small enough to load instantly as a profile picture (PFP) or avatar, yet sharp on phone screens.</p>'''
        + _table(500, 500, [(72, "6.94 × 6.94", "17.64 × 17.64"), (150, "3.33 × 3.33", "8.47 × 8.47"), (300, "1.67 × 1.67", "4.23 × 4.23")]) + '''
<h2>Making a good 500 × 500 PFP</h2>
<ul><li>Fill most of the square with your face or logo; small details disappear at avatar size.</li><li>Use a plain or blurred background so the picture still reads when shown as a tiny circle.</li><li>JPG is fine for photos; use PNG for logos with flat colours or transparency.</li></ul>''',
        [("Is 500x500 good for a profile picture?", "Yes. Most apps show profile pictures much smaller than 500 pixels, so 500 × 500 stays sharp everywhere while loading quickly.")]),
    "resize-image-to-1080x1920": ('''<h2>1080 × 1920 in numbers</h2>
<p>1080 × 1920 is a 9:16 portrait image of about 2.07 megapixels: the same pixels as a Full HD screen, turned on its side. If a platform asks for 9:16, 1080 × 1920 is the standard size to upload.</p>'''
        + _table(1080, 1920, [(72, "15 × 26.67", "38.1 × 67.73"), (150, "7.2 × 12.8", "18.29 × 32.51"), (300, "3.6 × 6.4", "9.14 × 16.26")]),
        [("How many megapixels is 1080x1920?", "About 2.07 megapixels (1080 × 1920 = 2,073,600 pixels).")]),
}


def enrich(T):
    for t in T:
        s = t["slug"]
        if s in TITLE:
            t["title"] = TITLE[s]
        if s in SECTIONS:
            body, faq = SECTIONS[s]
            t["body"] = t["body"] + body
            t["faq"] = list(t.get("faq", [])) + list(faq)
