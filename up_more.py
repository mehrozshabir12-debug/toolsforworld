"""Second round (29 Oct 2026 re-audit): extra page-specific text for the pages that were still
below ~48% unique three-word phrases. Appended to the end of each page's body and FAQ."""

MORE = {}

MORE["resize-image-to-600x600"] = ('''<h2>Getting a sharp 600 × 600 from a phone photo</h2>
<p>A phone photo is around 3000 × 4000 pixels, so making it 600 × 600 throws away most of the pixels, and that's fine: the result is still sharp. The real decision is the crop. For a face photo, choose Crop to fill and frame it so the head is centred with a little space above the hair. For a product photo, Fit with white border keeps the whole item visible, which shops prefer to a cut-off corner.</p>''',
[("Why is my 600x600 photo rejected by the visa form?", "Usually because of the face, not the pixel size: head too small or too large, shadows on the background, or glasses glare. Use the US passport photo maker to frame the face, which also gives you a 600 × 600 file.")])

MORE["heic-to-pdf"] = ('''<h2>Stop the iPhone saving HEIC</h2>
<p>If you often need JPG or PDF files, you can make the iPhone save photos as JPG: open Settings › Camera › Formats and choose <b>Most Compatible</b>. New photos are then JPG, while photos you already took stay HEIC, which is what this page converts. The HEIC setting saves storage, so many people keep it and convert only when a form asks for something else.</p>
<p>Scanning documents? The Notes and Files apps on iPhone can scan straight to PDF, which skips HEIC entirely. For photos already in your library, choose them here in the order you want the pages.</p>''',
[("Can I convert HEIC photos to PDF on Windows?", "Yes. The conversion runs in the browser, so it works in Chrome or Edge on Windows without installing an HEIC extension.")])

MORE["webp-to-png"] = ('''<h2>Where WebP files come from</h2>
<p>Many websites now serve images as WebP because the files are smaller, so a picture saved from a shop, a news site or a search result often turns out to be .webp even if it looked like any other image. Older editing apps, some printing services and many upload forms don't accept WebP yet, which is why converting to PNG helps.</p>
<p>PNG keeps transparent backgrounds, so logos and stickers stay cut out. Animated WebP files are converted as a still image of the first frame.</p>''',
[("Is PNG bigger than WebP?", "Usually, yes, often two to five times bigger, because PNG doesn't throw away any detail. If the size matters more than transparency, convert to JPG instead.")])

MORE["pdf-to-jpg"] = ('''<h2>Choosing the quality setting</h2>
<p><b>Normal</b> suits sharing a page on WhatsApp or showing it on a website. <b>High</b>, the default, keeps small text readable when the image is zoomed, and is the safe choice for documents. <b>Very high</b> makes large images for printing or for cropping a detail out of a page, such as a chart or a signature, and the files are noticeably bigger.</p>
<p>Each page becomes its own JPG, named with the page number, so a 10-page PDF gives ten images in the right order.</p>''',
[("Can I convert just one page of a PDF to JPG?", "Convert the PDF and keep the image you need, or first take that page out with Split PDF and convert only it.")])

MORE["png-to-jpg"] = ('''<h2>When to keep PNG instead</h2>
<p>JPG is the right choice for photos and anything a form or website asks for as JPG. Keep PNG for logos, icons and images with transparent backgrounds, because JPG has no transparency: those areas become white. Screenshots full of small text also stay crisper as PNG, though JPG at high quality is usually good enough and much smaller.</p>''',
[("Why is my JPG smaller than the PNG?", "JPG uses lossy compression, which drops detail the eye barely notices. A PNG photo of 5 MB often becomes a JPG of under 1 MB.")])

MORE["compress-image"] = ('''<h2>Compress by quality, or to an exact size</h2>
<p>There are two ways to use this tool. Leave the target empty and choose a quality to shrink photos while keeping them looking the same, which is good for websites and sharing. Or type a target such as 50 KB, and each photo is made just under that size, which is what upload forms need. Both work on several photos at once.</p>''',
[])

MORE["compress-image-to-100kb"] = ('''<h2>A batch of photos at 100 KB</h2>
<p>Choose several photos at once and each one is brought under 100 KB separately, so a set of ten document photos for an application takes one click instead of ten. The files keep their names with "compressed" added, so you can still tell which one is which when you upload them.</p>''',
[])

MORE["compress-image-to-1mb"] = ('''<h2>Photos for school and work systems</h2>
<p>Learning platforms, HR systems and intranets often cap profile pictures and attachments at 1 MB. A photo straight from the phone is usually 2–5 MB and gets refused; at 1 MB it looks the same on screen and uploads in seconds, even on mobile data.</p>''',
[])

MORE["compress-image-to-2mb"] = ('''<h2>Insurance claims and rental inspections</h2>
<p>Claims and inspection forms often ask for several photos of damage or rooms, each under 2 MB. At this size the photos keep enough detail to zoom into scratches, cracks and stains, which is what the person reviewing them needs to see.</p>''',
[])

MORE["jpg-to-pdf-under-200kb"] = ('''<h2>If the portal also limits pages</h2>
<p>Some portals cap both the size and the number of pages, for example "one PDF, maximum 3 pages, under 200 KB". Combine the front and back of a card into one photo before adding it, or leave out pages that only repeat information, so the PDF fits both rules.</p>''',
[])

MORE["jpg-to-pdf-under-500kb"] = ('''<h2>Receipts and bills for expense claims</h2>
<p>Expense and reimbursement systems often take one PDF per claim. Photograph each receipt on a dark surface, crop them, and put them in date order here: a month of receipts usually fits under 500 KB with every amount still readable.</p>''',
[])

MORE["compress-pdf-to-5mb"] = ('''<h2>Pencil and light handwriting</h2>
<p>Scans of pencil notes are faint to begin with, and compression makes faint lines fainter. If your assignment is in pencil, scan it with the app's "document" or high-contrast mode before compressing, so the writing stays dark enough to read.</p>''',
[])

MORE["compress-pdf-to-500kb"] = ('''<h2>Visa and immigration uploads</h2>
<p>Online visa systems usually ask for each supporting document separately: passport bio page, bank statements, invitation letter. Compress each one on its own rather than combining them, so every file stays well under 500 KB and is labelled correctly in the application.</p>''',
[])
