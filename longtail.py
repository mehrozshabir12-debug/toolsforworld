# Long-tail wording from Google autocomplete and Search Console (checked 22 Oct 2026).
# People type the same need many ways: "compress pdf to 200kb", "below 200kb", "less than 200kb",
# "under 200kb", "upto 200kb", "without losing quality", "without uploading".
# Each page gets one or two honest FAQs that answer those exact phrasings for its own size,
# instead of keyword lists. No new pages and no title changes here.


def _size(kb):
    return f"{kb // 1024} MB" if kb >= 1024 and kb % 1024 == 0 else f"{kb} KB"


def _pdf_quality(kb):
    if kb <= 200:
        return ("Text-based PDFs (typed letters, forms, CVs) usually stay sharp, because text takes very little space. "
                f"Scanned pages and photos have to be squeezed harder to reach {_size(kb)}, so they can look softer. "
                "The tool always keeps the sharpest version that still fits, and you can check it before you submit.")
    if kb <= 500:
        return ("For most documents the change is hard to see. Typed text stays sharp, and scans of one to five pages "
                f"usually fit under {_size(kb)} with readable text. Long scans with many photos may need splitting first.")
    return (f"Usually yes. {_size(kb)} is a generous limit, so most PDFs only lose detail you would not notice on screen. "
            "Very long scanned documents are the exception: split them or remove blank pages first.")


def _pdf_variants(kb):
    s = _size(kb)
    return (f"Does this work for “below {s}”, “less than {s}” or “up to {s}” limits?",
            f"Yes. Under, below, less than and up to {s} all mean the same thing: the file must be {s} or smaller. "
            f"The PDF is made just under {s}, so it passes any of these limits on upload forms.")


def _img_variants(kb):
    s = _size(kb)
    return (f"Does this work for “below {s}”, “less than {s}” or “up to {s}” limits?",
            f"Yes. Under, below, less than and up to {s} all mean the photo must be {s} or smaller, and the result is "
            f"made just under {s}. If a form gives a range instead, the result lands just under {s}, at the top of that range.")


NO_UPLOAD = {
    "compress-pdf": ("Can I compress a PDF without uploading it?",
                     "Yes, that is how this tool works. The PDF is compressed by your own browser, on your device, and is never sent to a server. You can even turn off Wi-Fi after the page loads and it still works."),
    "compress-image": ("Can I reduce image size without uploading the photo?",
                       "Yes. The photo is compressed by your browser on your own device and is never uploaded, which is safer for ID photos, signatures and documents."),
    "jpg-to-pdf": ("Can I convert photos to PDF without uploading them?",
                   "Yes. The PDF is built by your browser on your device, so your photos and scans are never sent to a server."),
}

JPG_TO_PDF_LIMITS = ('<h2>Need the PDF under a size limit?</h2>'
                     '<p>Many forms ask for a PDF “under 200 KB” or “less than 1 MB”. Make the PDF here first, then shrink it to the exact limit: '
                     '<a href="../compress-pdf-to-100kb/">under 100 KB</a>, <a href="../compress-pdf-to-200kb/">under 200 KB</a>, '
                     '<a href="../compress-pdf-to-300kb/">under 300 KB</a>, <a href="../compress-pdf-to-500kb/">under 500 KB</a> or '
                     '<a href="../compress-pdf-to-1mb/">under 1 MB</a>. For a single photo, it often helps to '
                     '<a href="../compress-image/">compress the image</a> before converting.</p>')


def enrich(T):
    for t in T:
        s, faq = t["slug"], list(t.get("faq", []))
        preset = t.get("preset") or {}
        if t.get("parent") == "compress-pdf" and "#ptkb" in preset:
            kb = int(preset["#ptkb"])
            faq += [_pdf_variants(kb), (f"Can I compress a PDF to {_size(kb)} without losing quality?", _pdf_quality(kb))]
        elif t.get("parent") == "compress-image" and "#tkb" in preset:
            faq.append(_img_variants(int(preset["#tkb"])))
        if s in NO_UPLOAD:
            faq.append(NO_UPLOAD[s])
        if s == "jpg-to-pdf":
            t["body"] = t["body"] + JPG_TO_PDF_LIMITS
        t["faq"] = faq
