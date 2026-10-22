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


def enrich(T):
    for t in T:
        s = t["slug"]
        if s == "resize-image-to-1080x1920":
            t["body"] += R1080
        elif s == "resize-image-to-1500x500":
            t["body"] += R1500
        elif t.get("parent") == "image-to-text":
            code = (t.get("preset") or {}).get("#ol")
            if code in OCR_NATIVE:
                lang, d, line = OCR_NATIVE[code]
                t["body"] = f'<p class="quick" lang="{lang}" dir="{d}">{line}</p>' + t["body"]
