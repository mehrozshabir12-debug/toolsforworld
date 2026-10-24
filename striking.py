# Pages close to Google's first page (Search Console, 28 days to 19 Oct 2026, checked 22 Oct):
# resize-image-to-1080x1920 (avg position ~15-31), resize-image-to-1500x500 ("500 x 1550" at 6, "1550 x 500" at 11),
# OCR language pages at 11-15 (French, Indonesian, Russian, Turkish; "ocr turkish text" at 3, "image to text türkçe" at 27).
# Each gets content that answers what those searchers want. OCR pages get one line in the page's own language,
# because native-language searches ("türkçe ocr") reach them.

R1080 = '''<h2>1080 × 1920 at a glance</h2>
<div class="scroll"><table class="t"><tbody>
<tr><th>Shape</th><td>9:16 vertical (portrait)</td></tr>
<tr><th>Total pixels</th><td>2,073,600 (about 2.1 megapixels)</td></tr>
<tr><th>Same as</th><td>1920 × 1080 Full HD, turned upright</td></tr>
<tr><th>Print size at 300 dpi</th><td>3.6 × 6.4 inches (9.1 × 16.3 cm)</td></tr>
<tr><th>Used for</th><td>Instagram Stories and Reels, TikTok, YouTube Shorts, WhatsApp status, phone wallpapers</td></tr>
</tbody></table></div>
<p>Apps show buttons, names and captions over the top and bottom of a 1080 × 1920 frame, so keep faces and text near the middle. Need the landscape version? Use <a href="../resize-image-to-1920x1080/">1920 × 1080</a>. Need a square post instead? Use <a href="../resize-image-to-1080x1080/">1080 × 1080</a>.</p>'''

R1500 = '''<h2>1500 × 500 and other banner sizes</h2>
<div class="scroll"><table class="t"><thead><tr><th>Banner</th><th>Pixels</th><th>Shape</th></tr></thead><tbody>
<tr><td>X (Twitter) header</td><td>1500 × 500</td><td>3:1</td></tr>
<tr><td>LinkedIn profile banner</td><td><a href="../resize-image-to-1584x396/">1584 × 396</a></td><td>4:1</td></tr>
<tr><td>Facebook cover</td><td><a href="../resize-image-to-851x315/">851 × 315</a></td><td>about 2.7:1</td></tr>
<tr><td>YouTube channel banner</td><td><a href="../resize-image-to-2560x1440/">2560 × 1440</a></td><td>16:9</td></tr>
</tbody></table></div>
<p>1500 × 500 is 750,000 pixels in a 3:1 shape: three times as wide as it is tall. Need it the other way round, 500 × 1500 for a tall side banner? Open <a href="../resize-image/">Resize Image</a>, untick <b>Keep ratio</b> and enter width 500 and height 1500. Other sizes such as 1500 × 400 work the same way.</p>'''

OCR_NATIVE = {
    "urd": ("ur", "rtl", "تصویر سے اردو متن نکالیں: تصویر یا اسکرین شاٹ منتخب کریں اور اردو تحریر کاپی کر لیں۔ آپ کی تصویر کہیں اپ لوڈ نہیں ہوتی۔"),
    "ara": ("ar", "rtl", "استخراج النص العربي من الصور: اختر صورة أو لقطة شاشة وانسخ النص. لا يتم رفع صورتك إلى أي خادم."),
    "hin": ("hi", "ltr", "फ़ोटो से हिंदी टेक्स्ट निकालें: फ़ोटो या स्क्रीनशॉट चुनें और टेक्स्ट कॉपी करें। आपकी फ़ोटो कहीं अपलोड नहीं होती।"),
    "spa": ("es", "ltr", "Extrae texto en español de una imagen: elige una foto o captura de pantalla y copia el texto. Tu imagen no se sube a ningún servidor."),
    "fra": ("fr", "ltr", "Extraire du texte français d’une image : choisissez une photo ou une capture d’écran et copiez le texte. Votre image n’est envoyée sur aucun serveur."),
    "deu": ("de", "ltr", "Text aus Bildern auf Deutsch erkennen: Foto oder Screenshot wählen und den Text kopieren. Ihr Bild wird nicht hochgeladen."),
    "por": ("pt", "ltr", "Extraia texto em português de uma imagem: escolha uma foto ou captura de tela e copie o texto. Sua imagem não é enviada para nenhum servidor."),
    "ita": ("it", "ltr", "Estrai testo in italiano da un’immagine: scegli una foto o uno screenshot e copia il testo. La tua immagine non viene caricata su alcun server."),
    "rus": ("ru", "ltr", "Распознать русский текст на картинке: выберите фото или скриншот и скопируйте текст. Ваше изображение никуда не загружается."),
    "tur": ("tr", "ltr", "Resimden Türkçe metne (OCR): bir fotoğraf veya ekran görüntüsü seçin ve metni kopyalayın. Görseliniz hiçbir sunucuya yüklenmez."),
    "ben": ("bn", "ltr", "ছবি থেকে বাংলা লেখা বের করুন: একটি ছবি বা স্ক্রিনশট বেছে নিন এবং লেখা কপি করুন। আপনার ছবি কোথাও আপলোড হয় না।"),
    "ind": ("id", "ltr", "Ubah gambar menjadi teks bahasa Indonesia (OCR): pilih foto atau tangkapan layar, lalu salin teksnya. Gambar Anda tidak diunggah ke server mana pun."),
    "chi_sim": ("zh-Hans", "ltr", "图片转文字（中文 OCR）：选择照片或截图，然后复制识别出的文字。您的图片不会上传到任何服务器。"),
}

# Competitor gap (OpenSEO, India, 23 Oct 2026): "passport size photo size in cm / in inches / in india" have keyword
# difficulty 0-2 and the top results average only ~4 referring domains; 123passportphoto ranks 11-29 there with
# query-string URLs. imgsmaller.com ranks 37-54 for "whatsapp dp size" (difficulty 0). Answer those exact questions.
INDIA_UNITS = '''<h2>Passport size photo size in India: cm, inches and pixels</h2>
<div class="scroll"><table class="t"><tbody>
<tr><th>Centimetres</th><td>3.5 × 4.5 cm</td></tr>
<tr><th>Millimetres</th><td>35 × 45 mm</td></tr>
<tr><th>Inches</th><td>about 1.38 × 1.77 inches</td></tr>
<tr><th>Pixels at 300 dpi</th><td>413 × 531 px (what this tool makes)</td></tr>
<tr><th>Shape</th><td>portrait, width to height 7:9</td></tr>
</tbody></table></div>
<p>All rows describe the same photo in different units. Online forms usually also set a file size: make the photo here first, then use <a href="../compress-image-to-50kb/">Compress image to 50 KB</a> or the limit your form gives. A square 2 × 2 inch photo (51 × 51 mm) is a different size, used for the Indian e-Visa and some missions abroad.</p>'''

WHATSAPP_DP = '''<h2>WhatsApp DP size</h2>
<p>WhatsApp shows your profile photo as a circle cut from a square, so any square image works. 500 × 500 px is a safe size: sharp on every phone and small enough to upload quickly. If your photo is a rectangle, WhatsApp asks you to crop it; to keep the whole picture instead, choose <b>Fit with white border</b> here first. Keep your face in the middle, because the corners are hidden by the circle.</p>'''

# Pakistan passport page (owner approved 24 Oct 2026). Facts only from DGI&P's online-passport page, as already used in
# the passport-size guide: colour, white background, 350 x 467 px, JPG/JPEG, max 3 MB. No head size is published for it.
PAK_TITLE = "Pakistan Passport Photo 350×467 px – Free Online Maker"
PAK_DESC = "Make a photo for the Pakistan online passport application: 350 × 467 pixels, white background, JPG under 3 MB. Free, no upload, works on your phone."
PAK_BODY = '''<h2>Pakistan passport photo requirements (online application)</h2>
<div class="scroll"><table class="t"><tbody>
<tr><th>Size</th><td>350 × 467 pixels (this page makes exactly that)</td></tr>
<tr><th>Format</th><td>JPG / JPEG</td></tr>
<tr><th>File size</th><td>3 MB at most; a 350 × 467 photo is far smaller</td></tr>
<tr><th>Background</th><td>White</td></tr>
<tr><th>Colour</th><td>Colour photo</td></tr>
<tr><th>Head size</th><td>Not published by DGI&amp;P for the online upload; keep your face centred and the whole head in the frame</td></tr>
</tbody></table></div>
<p>For the online form you only need the single photo, not the 4×6 print sheet. If you apply in person at a passport office, your photo is taken there. 350 × 467 px is a 3:4 shape, a little narrower than a 35 × 45 mm print, so use this pixel size for the online upload rather than resizing a printed photo.</p>
<p class="quick" lang="ur" dir="rtl">پاکستانی پاسپورٹ کی آن لائن درخواست کے لیے تصویر: 350 × 467 پکسل، سفید پس منظر، رنگین، JPG فارمیٹ اور زیادہ سے زیادہ 3 MB۔ یہ صفحہ آپ کی تصویر بالکل اسی سائز میں بناتا ہے، اور تصویر کہیں اپ لوڈ نہیں ہوتی۔</p>
<p>Official source: <a href="https://dgip.gov.pk/eServices/online-passport.php" rel="nofollow">DGI&amp;P – Online passport (document requirements)</a>. See also <a href="../guides/passport-photo-size-by-country/">passport photo sizes by country</a>.</p>'''
PAK_FAQ = [("What is the Pakistan passport photo size in pixels?", "350 × 467 pixels for the online application, in JPG with a white background and no more than 3 MB."),
           ("Is 350 × 467 px the same as 35 × 45 mm?", "No. 350 × 467 px is a 3:4 shape, a little narrower than 35 × 45 mm. For the online passport form, use the pixel size DGI&P gives.")]


def enrich(T):
    for t in T:
        s = t["slug"]
        if s == "resize-image-to-1080x1920":
            t["body"] += R1080
        elif s == "resize-image-to-1500x500":
            t["body"] += R1500
        elif s == "india-passport-photo":
            t["body"] += INDIA_UNITS
            t["faq"] = list(t.get("faq") or []) + [
                ("What is the passport size photo size in cm in India?", "3.5 × 4.5 cm (35 × 45 mm), which is about 1.38 × 1.77 inches. At 300 dpi that is 413 × 531 pixels."),
                ("How many KB should a passport size photo be?", "There is no single rule: each online form sets its own limit, often between 20 KB and 200 KB. Make the photo here, then compress it to the limit your form shows.")]
        elif s == "pakistan-passport-photo":
            t["title"], t["desc"] = PAK_TITLE, PAK_DESC
            t["body"] += PAK_BODY
            t["faq"] = list(t.get("faq") or []) + PAK_FAQ
        elif s == "resize-image-to-500x500":
            t["body"] += WHATSAPP_DP
            t["faq"] = list(t.get("faq") or []) + [
                ("What is the WhatsApp DP size?", "Any square photo works because WhatsApp crops it to a circle. 500 × 500 px is a good, safe size.")]
        elif t.get("parent") == "image-to-text":
            code = (t.get("preset") or {}).get("#ol")
            if code in OCR_NATIVE:
                lang, d, line = OCR_NATIVE[code]
                t["body"] = f'<p class="quick" lang="{lang}" dir="{d}">{line}</p>' + t["body"]
