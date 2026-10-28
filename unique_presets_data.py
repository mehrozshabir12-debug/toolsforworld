"""All hand-written preset content, merged (see unique_presets.py)."""
import up_passport, up_compress, up_other

PAGES = {}
for mod in (up_passport, up_compress, up_other):
    for k, v in mod.P.items():
        assert k not in PAGES, k
        PAGES[k] = v
