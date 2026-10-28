"""Fourth round (29 Oct 2026): main tool pages, so they also clear 60% unique three-word phrases."""

M = {}

M["jpg-to-pdf"] = ('''<h2>Which order do pages end up in?</h2>
<p>Pages follow the list from top to bottom. Phones often list photos newest first, so a document photographed page 1 to page 5 can arrive reversed; glance at the list and move any pages that are out of place before creating the file. Mixed portrait and landscape shots are fine: wide pictures get a sideways page automatically, so nothing is squashed.</p>
<h2>Sending the PDF from a phone</h2>
<p>Once the file is saved, share it straight from the Downloads or Files app into Gmail, Outlook, WhatsApp or a portal's upload button. On iPhone, tap the share icon after the download finishes and choose "Save to Files" first if the portal needs to find it later.</p>''', [])

M["pdf-to-png"] = ('''<h2>Using the images afterwards</h2>
<p>Drop a converted page into Google Slides, Canva or PowerPoint as a picture, mark it up in any drawing app, or attach it to a chat where PDFs can't be previewed. Designers often export a single diagram page this way to place it on a web page without the PDF viewer around it.</p>''', [])

M["jpeg-to-jpg"] = ('''<h2>Renaming by hand versus converting</h2>
<p>On a computer you could rename each file yourself, but Windows and macOS hide extensions by default, so people end up with names like photo.jpg.jpeg. Doing a whole batch here avoids that mistake, and phones, where renaming extensions is awkward, can do it in a couple of taps.</p>''', [])

M["pdf-to-jpg"] = ('''<h2>Password-protected and very long PDFs</h2>
<p>A PDF locked with an opening password can't be read until it's unlocked in the app that created it. Long files with hundreds of pages take a while, especially at the highest setting; on a phone, convert big documents in smaller parts with Split PDF.</p>''', [])

M["mp4-to-mp3"] = ('''<h2>Trimming silence and long intros</h2>
<p>The MP3 keeps the full length of the video. To cut a quiet start or a long ending, open the file in a free audio editor such as Audacity afterwards, which handles MP3 directly.</p>''', [])

M["webp-to-jpg"] = ('''<h2>Batch converting a whole folder</h2>
<p>Select every WebP file at once and each one is converted with its original name kept, which is much faster than opening and re-saving images one by one in an editor.</p>''', [])

M["jfif-to-jpg"] = ('''<h2>Is a JFIF file safe to open?</h2>
<p>Yes. It's an ordinary photo container, the same as JPEG, not a program, so it can't run anything on your computer.</p>''', [])

M["compress-image"] = ('''<h2>Before and after sizes</h2>
<p>After compressing, each file shows its old and new size, so you can see at a glance which photos shrank the most and whether any still exceed the limit you need.</p>''', [])

M["video-to-mp3"] = ('''<h2>Formats from different devices</h2>
<p>iPhones record MOV, Android phones usually MP4, screen recorders often WebM, and older phones 3GP. All of them can usually be turned into MP3 here as long as the browser can play the sound.</p>''', [])

M["heic-to-jpg"] = ('''<h2>Live Photos and Portrait mode</h2>
<p>A Live Photo is saved as a still picture plus a short video. Only the still part is converted.</p>''', [])

M["jpg-to-png"] = ('''<h2>Adding transparency later</h2>
<p>A JPG has a solid background, and PNG alone doesn't remove it. To cut out the background, run the PNG through the Background Remover.</p>''', [])

M["compress-pdf"] = ('''<h2>Exact target or best effort</h2>
<p>Type a number of KB to aim for a portal limit, or leave it empty and pick a level when you simply want a lighter file for sharing.</p>''', [])

M["png-to-jpg"] = ('''<h2>Product photos with white backgrounds</h2>
<p>Shop images exported as PNG are often far bigger than needed. As JPG they look the same on a white page.</p>''', [])

M["passport-photo-maker"] = ('''<h2>Countries with their own preset</h2>
<p>Ready-made frames exist for the US, UK, Canada, Australia, India, Pakistan, the Schengen area and China. For other countries, choose the matching size from the list.</p>''', [])

M["png-to-pdf"] = ('''<h2>Chat exports and receipts</h2>
<p>Screenshots of a conversation, in order, make a tidy record for disputes or insurance.</p>''', [])

M["heic-to-pdf"] = ('''<h2>Mixing HEIC with other photos</h2>
<p>JPG and PNG files can be added to the same list, so photos from different phones end up in one document.</p>''', [])

M["resize-image"] = ('''<h2>Batch resizing</h2>
<p>Choose many photos and every one gets the same width and height, handy for a gallery or catalogue.</p>''', [])

M["webp-to-png"] = ('''<h2>Stickers</h2>
<p>Messaging stickers saved as WebP become PNGs with transparency kept.</p>''', [])

M["pdf-to-word"] = ('''<h2>Headings in the Word file</h2>
<p>Lines printed in a larger size are kept as bold, bigger text, so the structure of a report stays easy to follow.</p>''', [])

M["image-to-text"] = ('''<h2>Long documents</h2>
<p>Work one page image at a time and paste each result into your document as you go.</p>''', [])

M["remove-background"] = ('''<h2>Hair and fine edges</h2>
<p>Curly hair and fur are the hardest parts; a plain wall behind the person helps most.</p>''', [])

M["merge-pdf"] = ('''<h2>Joining scans with typed pages</h2>
<p>Scanned and digital PDFs can be combined in one file; each page keeps its own size.</p>''', [])

M["txt-to-pdf"] = ('''<h2>Line wrapping</h2>
<p>Long lines wrap at the page margin, so nothing is cut off.</p>''', [])
