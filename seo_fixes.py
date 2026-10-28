"""Fixes from the Semrush site audit of 28 Oct 2026 (low word count on two calculator pages).
Adds worked examples people actually search for. Every number below was checked by hand."""

EXTRA = {
    "heic-to-pdf": ('''<h2>Stop your iPhone saving HEIC (optional)</h2>
<p>If you often need JPG or PDF files, you can make the camera save JPG from now on: open <b>Settings → Camera → Formats</b> and choose <b>Most Compatible</b>. Photos take a little more storage, but every website and Windows PC opens them. Photos you already took stay in HEIC, which is what this converter is for.</p>
<h2>Sending documents from an iPhone to an office</h2>
<p>Offices, banks and schools often ask for "one PDF" of a document you photographed, such as a signed form or several pages of a contract. Add the HEIC photos in page order, choose A4 or Letter so the pages print at a normal size, and send the single PDF. The receiver doesn't need an Apple device to open it.</p>''',
        [("Does converting HEIC to PDF lower the quality?", "Each photo is converted to a high-quality JPG inside the PDF, so the difference is very hard to see. Only if you set a maximum PDF size are the photos compressed further to fit.")]),
    "webp-to-png": ('''<h2>Animated WebP files</h2>
<p>Some WebP files are short animations, like GIFs. PNG can only hold a single picture, so converting an animated WebP gives you the first frame as a still image. To keep the animation, you need a GIF or video converter instead.</p>
<h2>Editing the converted PNG</h2>
<p>PNG opens in every editor, including Paint, Photoshop, GIMP, Canva and PowerPoint. Because PNG is lossless, you can edit and save it many times without the picture getting worse, which makes it a good working copy. When the design is finished, export a JPG or WebP if you need a smaller file for the web.</p>''',
        [("Why is my PNG bigger than the WebP?", "WebP compresses photos much more tightly than PNG, which keeps every pixel exactly. The PNG is larger but has the same picture, with transparency kept.")]),
    "percentage-calculator": ('''<h2>Reverse percentages: finding the original number</h2>
<p>When you know the result <i>after</i> a change, divide instead of subtracting. A price that is 120 after a 20% rise was 120 ÷ 1.2 = <b>100</b>, not 96. A salary of 1,700 after a 15% cut was 1,700 ÷ 0.85 = <b>2,000</b>.</p>
<p>The same idea answers "45 is 30% of what?": 45 ÷ 0.30 = <b>150</b>.</p>
<h2>Percent vs percentage points</h2>
<p>If an interest rate goes from 4% to 5%, it rose by <b>1 percentage point</b>, but by <b>25 percent</b> (1 ÷ 4 × 100). News reports mix these up often; use the "From … to …" row above for the percent change.</p>
<h2>Why +10% then −10% is not zero</h2>
<p>Each change uses a new starting value. 100 plus 10% is 110; 110 minus 10% is 99. Two equal changes in opposite directions always leave you slightly below where you started.</p>
<h2>Quick everyday sums</h2>
<ul><li><b>Tip</b>: 15% of a 64 bill is 64 × 0.15 = 9.60.</li><li><b>Test score</b>: 18 out of 25 is 18 ÷ 25 × 100 = 72%.</li><li><b>Growth</b>: followers going from 800 to 1,000 is a 25% increase.</li></ul>''',
        [("How do I find the original price before a percentage increase?", "Divide the new price by (1 + percent ÷ 100). For 120 after a 20% increase: 120 ÷ 1.2 = 100."),
         ("What is the difference between percent and percentage points?", "Percentage points are the plain gap between two percentages (4% to 5% is 1 point). Percent change compares that gap with the starting value (1 ÷ 4 = 25%).")]),
    "discount-calculator": ('''<h2>Find the original price from a sale price</h2>
<p>Divide the sale price by (1 − discount ÷ 100). An item that costs 75 after 25% off was 75 ÷ 0.75 = <b>100</b> before the sale.</p>
<h2>"Buy one, get one half price" in percent</h2>
<p>Two items at 40 each normally cost 80. With the second at half price you pay 40 + 20 = 60, which is <b>25% off</b> the pair, not 50%.</p>
<h2>Discount first, then tax</h2>
<p>Shops usually apply the discount before sales tax. A price of 80 with 25% off is 60; adding 10% tax gives <b>66</b>. Because both are percentages, doing them in the other order gives the same total.</p>
<h2>Which deal is better?</h2>
<ul><li><b>30% off, then an extra 20% off</b>: 0.70 × 0.80 = 0.56, so you pay 56%, which is <b>44% off</b>.</li><li><b>A flat 45% off</b> is slightly better than that.</li><li>To compare a percent discount with an amount off, work out both sale prices with the calculator above.</li></ul>''',
        [("How do I calculate the original price before a discount?", "Divide the sale price by (1 − discount ÷ 100). For 75 after 25% off: 75 ÷ 0.75 = 100."),
         ("Is 30% off plus an extra 20% off the same as 50% off?", "No. 30% then 20% off leaves you paying 0.70 × 0.80 = 56% of the price, so the total discount is 44%.")]),
}


def enrich(T):
    for t in T:
        if t["slug"] in EXTRA:
            body, faq = EXTRA[t["slug"]]
            t["body"] = t["body"] + body
            t["faq"] = list(t.get("faq", [])) + faq
