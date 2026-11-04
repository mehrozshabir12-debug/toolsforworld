"""Bing-driven titles and descriptions (5 Nov 2026).

Bing Webmaster Tools (data to 2 Nov) shows the resize pages at average positions 2-8 for searches such as
"1920x1080 image resizer", "change image to 1920x1080", "crop image to 1920x1080", "convert photo to 3000x3000 pixels",
"3000 x 3000 px cover art", "make image 500x500" and "pfp 500x500", but almost no clicks. Bing Keyword Research
(3 months to 1 Nov, all countries) gives the wording people use most:
  image resizer 243.7K, resize image 188.8K, photo resizer 79.6K, image resizer in kb 25.0K,
  jpeg to jpg 85.2K, jpeg to jpg converter 15.3K, convert jpeg to jpg 14.6K,
  percentage calculator 526.8K, percentage increase calculator 59.5K, days between dates 93.1K.
Bing's top results for the size searches are small exact-match sites titled "WxH Image Resizer" or
"Resize image to WxH pixels online free". Titles here use that wording; descriptions name the tasks people search
for. Only claims the tools already do (crop or fit, custom size, KB target, % increase/decrease) are used.
"""

TITLE = {
    "resize-image-to-1920x1080": "1920x1080 Image Resizer – Resize or Crop Photo to 1920x1080",
    "resize-image-to-1080x1920": "1080x1920 Image Resizer – Resize Photo to 1080x1920 (9:16)",
    "resize-image-to-3000x3000": "3000x3000 Image Converter – Photo to 3000x3000 Pixels Free",
    "resize-image-to-500x500": "500x500 Image Resizer – Make Any Photo or PFP 500x500 Free",
    "resize-image-to-600x600": "600x600 Image Resizer – Resize Photo to 600x600 Pixels Free",
    "resize-image-to-1500x500": "1500x500 Image Resizer – X (Twitter) Header Size Free",
    "resize-image": "Image Resizer – Free Photo Resizer Online (Any Pixel Size)",
    "compress-image": "Image Resizer in KB – Reduce Image Size in KB Free (JPG/PNG)",
    "jpeg-to-jpg": "JPEG to JPG Converter – Convert JPEG to JPG Online Free",
    "percentage-calculator": "Percentage Calculator – % of a Number, % Increase & Decrease",
}

DESC = {
    "resize-image": "Free image resizer and photo resizer: resize JPG, PNG or WebP to any width and height in pixels or by percent, keeping the aspect ratio. No upload.",
    "resize-image-to-1920x1080": "Change any image to 1920x1080 pixels (Full HD, 16:9) in seconds: crop to fill or fit with borders, for wallpapers, slides and YouTube. Free, no upload.",
    "resize-image-to-1080x1920": "Resize any photo to 1080x1920 pixels (9:16) for Instagram Stories, Reels, TikTok and WhatsApp status. Crop or fit, or type any size. Free, no upload.",
    "resize-image-to-3000x3000": "Convert any photo to 3000x3000 pixels for album cover art on Spotify, Apple Music and podcasts, or type any size like 3000 x 400. Free, no upload.",
    "resize-image-to-500x500": "Make any image 500x500 pixels for a profile picture (PFP), avatar or shop listing. Crop to fill or fit, or type any custom size. Free, no upload.",
}


def enrich(T):
    for t in T:
        s = t["slug"]
        if s in TITLE:
            t["title"] = TITLE[s]
        if s in DESC:
            t["desc"] = DESC[s]
