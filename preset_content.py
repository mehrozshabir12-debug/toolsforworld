"""Second round of unique content for the preset pages that were most alike (2026-10-19, AdSense
content-quality review): OCR language pages and compress-image-to-size pages averaged ~0.67–0.69
text similarity within their family. Each block below is specific to one language or one size."""

OCR = {
"urd": '''<h2>Using Urdu text after OCR</h2><p>The result is standard Unicode Urdu, so it pastes straight into Word, Google Docs, WhatsApp and Facebook. To make it look like a printed book, set the font to a Nastaliq face such as Jameel Noori Nastaleeq or Noto Nastaliq Urdu; with a default font it shows in the plainer Naskh style, but the letters are the same.</p>
<p>Check these spots first: dots on letters like ب پ ت ٹ ث (a missing or extra dot changes the letter), the small ط mark on ٹ ڈ ڑ, and words where ے and ی are swapped. Numbers may come out as Urdu digits (۱۲۳) or English digits depending on the source.</p>''',
"ara": '''<h2>Checking Arabic results</h2><p>Look closely at letters that differ only by dots, such as ب ت ث ن ي and ج ح خ, and at the joined form lam-alef (لا). Elongated words stretched with a tatweel line in headings may come out with extra ـ characters you can delete.</p>
<p>Numbers are recognised as written, so a document using Eastern Arabic digits (٠١٢٣) gives those digits, not 0123. If the text is actually Urdu (letters like ٹ ڈ ے), open the Urdu version of this tool instead, because the Arabic model doesn't expect those letters.</p>''',
"hin": '''<h2>Old Hindi fonts and Unicode</h2><p>Many Hindi documents in offices were typed in legacy fonts like Kruti Dev, which look like Hindi but store English letters underneath, so copying from them gives gibberish. Taking a screenshot or photo and running OCR here gives proper Unicode Hindi instead, which works in Google Docs, email and translators.</p>
<p>Proofread the matras (ि ी ु ू े ै), the nukta in letters like क़ ज़ फ़, and the halant (्) in half letters. Hindi printed in a very thin or decorative font is harder; plain newspaper and textbook fonts give the best results.</p>''',
"spa": '''<h2>Common Spanish OCR slips</h2><ul><li><b>ñ read as n</b>: it changes the word (año vs ano), so search the result for words that should have it.</li><li><b>Missing accents</b> on words that change meaning, like sí/si, tú/tu and él/el.</li><li><b>¿ and ¡</b> at the start of sentences, which small or blurry text can lose.</li><li>Words split by a hyphen at the end of a printed line; join them back up.</li></ul>
<p>For long documents, paste the result into a spell checker set to Spanish; it catches most dropped accents quickly.</p>''',
"fra": '''<h2>French typography in the result</h2><p>Printed French puts a small space before <code>; : ! ?</code> and inside « guillemets ». OCR may keep, drop or double these spaces, so tidy them if the text is going into a formal document.</p>
<p>Other things to check: words cut with a hyphen at the end of a line, the œ in words like cœur and sœur (sometimes read as oe), and capital letters with accents (É, À), which some fonts print without the accent. A French spell checker fixes most of these in a minute.</p>''',
"deu": '''<h2>Tips for German documents</h2><ul><li><b>Long compound words</b> are often hyphenated across lines in letters and contracts. Search the result for “- ” and join the parts.</li><li><b>ß and ss</b>: Swiss German uses ss everywhere, so don't “correct” Swiss text.</li><li><b>Umlauts</b> can lose their dots in small print (ü → u). Words like “für” and “über” are the usual victims.</li><li>Capitalised nouns help you spot errors: a noun in lower case is often a misread letter.</li></ul>''',
"por": '''<h2>Brazilian and European Portuguese</h2><p>Both use the same alphabet, so the model reads either. The spelling differs in some words (for example facto/fato and many words after the 1990 spelling agreement), and OCR copies whatever is printed, so don't expect it to switch spelling for you.</p>
<p>Check the tilde in ã and õ, which small print can lose (mão vs mao), the cedilla in ç, and hyphenated pronoun forms like “disse-me”, which can be confused with words broken across lines.</p>''',
"ita": '''<h2>Accents and elisions in Italian</h2><p>Italian uses both grave and acute accents: <i>è</i> (is) and <i>perché</i> look similar at small sizes, and OCR may swap them or drop them. Final accented vowels in words like città, più and così are worth checking.</p>
<p>Elided words (l'anno, dell'acqua, un'altra) depend on the apostrophe. If it's lost, the words run together or split with a space. A quick search for “l ” and “dell ” in the result finds most of these.</p>''',
"rus": '''<h2>Cyrillic look-alike letters</h2><p>Several Russian letters look exactly like Latin ones: а, е, о, р, с, х, у. Text that mixes Russian with English words, brand names or codes can come out with the wrong alphabet in places. It looks fine but breaks search and spell checking, so retype product codes and email addresses by hand.</p>
<p>Also check ё, which is often printed as е in Russian books (the model follows the print), and the hard and soft signs ъ and ь, which small fonts make hard to tell apart.</p>''',
"tur": '''<h2>The four Turkish i's</h2><p>Turkish has dotted <b>i/İ</b> and dotless <b>ı/I</b>, and they are different letters: “sıra” and “sira” are not the same word. Small or blurry print often loses the dot, so these are the first things to check in the result.</p>
<p>Also look at ğ (yumuşak g), which can be read as g, and ş and ç, whose small tails disappear in low-resolution scans. If you change the result to upper case later, use a Turkish-aware tool, or i becomes I instead of İ.</p>''',
"ben": '''<h2>Bangla conjuncts and vowel signs</h2><p>Bengali packs consonants together into conjuncts (যুক্তাক্ষর) such as ক্ষ, ঞ্জ and ন্ত. These are the most common source of OCR errors, followed by vowel signs that sit before, above or after a letter (ি ী ে ৈ).</p>
<p>Assamese uses nearly the same script but has its own letters ৰ and ৱ, so Assamese text read with the Bengali model may need corrections. Older Bangla books printed with worn type are harder than modern newspapers and screenshots.</p>''',
"ind": '''<h2>Why Indonesian usually reads well</h2><p>Indonesian uses the plain Latin alphabet with no accents, so OCR is generally very accurate on clear printed text. Most mistakes are the same ones English OCR makes: rn read as m, l read as 1, and O read as 0 in numbers.</p>
<p>Check reduplicated words written with a hyphen (anak-anak, kupu-kupu), which can lose the hyphen, and abbreviations such as Jl., Kec. and RT/RW in addresses. Malay text uses the same letters and usually works with this model too.</p>''',
"chi_sim": '''<h2>Simplified vs Traditional Chinese</h2><p>This page uses the Simplified Chinese model, the script used in mainland China, Singapore and Malaysia. Traditional characters from Taiwan, Hong Kong and older books are recognised less reliably, because many characters have different forms (for example 国/國, 书/書).</p>
<p>Chinese has no spaces between words, so the result is one continuous line of characters, which is normal. Horizontal text works best; vertical columns from books and signs may come out in the wrong order. Full-width punctuation (，。) may be read as English commas and full stops.</p>''',
}

KB = {
10: '''<h2>Getting a signature to 10 KB without blur</h2><p>Signature uploads are judged on whether the strokes are clear, not on colour. Sign a little larger than normal with a dark blue or black pen, photograph it on a flat surface without shadows, and crop so the signature fills almost the whole image. A wide strip of empty paper wastes bytes that the ink needs.</p>
<p>If the result still looks fuzzy, the photo had too many pixels to begin with: resize it to about 300 pixels wide with the <a href="../resize-image/">Image Resizer</a>, then compress again.</p>''',
20: '''<h2>Thumb impressions and small scans</h2><p>Some forms ask for a left-thumb impression or a small document image under 20 KB. Press the thumb on an ink pad, then on white paper, and photograph it straight from above. Crop to just the print; ridges show more clearly in a tight crop than in a wide one.</p>
<p>Check the dimensions as well as the size. If the form says something like “140 × 60 pixels”, resize to that first, because a 20 KB file at the wrong shape is still rejected.</p>''',
30: '''<h2>A worked example</h2><p>A 3 MB phone selfie for an exam portal that wants 20–30 KB: first crop to head and shoulders with the <a href="../passport-photo-maker/">passport photo maker</a>, which also fixes the shape. That crop alone often brings the photo to a few hundred KB. Compressing it here to 30 KB then only needs to drop a little quality, so the face stays sharp.</p>
<p>Skipping the crop means the whole room is squeezed into 30 KB and the face ends up blurry.</p>''',
50: '''<h2>Photo and signature on the same form</h2><p>Forms that want a photo under 50 KB usually also want a signature under 20 KB, and they're easy to swap by mistake. Name your files clearly before uploading, for example <code>photo-50kb.jpg</code> and <code>signature-20kb.jpg</code>.</p>
<p>If the portal shows your photo stretched or squashed after upload, the shape was wrong rather than the size. Check the width-to-height ratio it asks for (3.5 × 4.5 cm is a ratio of 7:9) and crop to that before compressing.</p>''',
100: '''<h2>When 100 KB is too much or too little</h2><p>For a face photo, 100 KB is generous; a clean crop usually looks perfect at 50–70 KB, so the tool may stop well under the target. For a full A4 document photographed with a phone, 100 KB is tight: crop off the table around the page and make sure the text is in focus, or small print may become hard to read.</p>
<p>For a document, check readability at 100% zoom before uploading. If it isn't readable, upload it as a PDF with <a href="../compress-pdf-to-100kb/">Compress PDF to 100 KB</a> if the form allows PDFs.</p>''',
200: '''<h2>200 KB for web and listings</h2><p>For a blog, shop or marketplace, image weight affects how fast pages open on mobile data. Around 200 KB per main image is a common target. For extra photos in a gallery you can often go to 100 KB, since they are shown smaller.</p>
<p>Resize to the width the site actually displays (often 1200–1600 pixels) before compressing. A 4000-pixel photo squeezed to 200 KB looks worse than a 1500-pixel photo at the same size, because the bytes are spread over fewer pixels.</p>''',
500: '''<h2>Sending photos over chat and email</h2><p>WhatsApp and many chat apps already compress photos you send, sometimes heavily. If you want the other person to get good quality, compress to about 500 KB yourself and send it as a document or file, so the app doesn't compress it again.</p>
<p>500 KB also suits CV photos, portfolio images and property listings, where people zoom in. For a batch of holiday photos, compressing them all to 500 KB can cut a 100 MB album to around 15 MB.</p>''',
1024: '''<h2>Is 1 MB enough to print?</h2><p>For prints up to 6 × 4 inches (10 × 15 cm), a 1 MB photo usually prints well, because printers need about 1800 × 1200 pixels for that size at photo quality. For A4 posters or framing, keep the original instead.</p>
<p>1 MB is also a common limit for profile and cover images on school, university and company systems. If your photo is under 1 MB already, the tool keeps it as it is rather than making it worse.</p>''',
2048: '''<h2>2 MB limits on job and visa portals</h2><p>Many application systems cap each upload at 2 MB. That limit is meant for documents, so a single photo rarely needs to be close to it. If you're uploading a photo of a certificate or ID card, crop it to the document first; this keeps the text sharp and the file well under 2 MB.</p>
<p>Several images for one upload field? Combine them into one PDF with <a href="../jpg-to-pdf/">JPG to PDF</a>, then use <a href="../compress-pdf-to-2mb/">Compress PDF to 2 MB</a> if the PDF is too big.</p>''',
5120: '''<h2>Photos from modern phones and cameras</h2><p>Phones with 48–200 megapixel cameras and DSLR cameras can produce photos of 8–25 MB, which many websites, email providers and cloud forms refuse. Bringing them to 5 MB keeps them detailed enough for large prints and editing.</p>
<p>If your phone saves in HEIC, convert with <a href="../heic-to-jpg/">HEIC to JPG</a> first, since most upload forms want JPG. RAW files (.dng, .cr2, .nef) aren't supported; export them as JPG from your photo app.</p>''',
}


def enrich(T):
    for t in T:
        p = t.get("preset") or {}
        extra = None
        if t.get("parent") == "image-to-text":
            extra = OCR.get(p.get("#ol"))
        elif t.get("parent") == "compress-image":
            extra = KB.get(p.get("#tkb"))
        if extra:
            t["body"] = t["body"] + "\n" + extra
