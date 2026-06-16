#!/usr/bin/env python3
"""Build the standalone Velloria bracelet detail page (detail.html).

Two passes in one script:
  1) subset the 7 Korean/Latin font faces to exactly the glyphs used in
     detail.template.html  ->  base64 woff2  ->  replace __TOKEN__ in markup
  2) compress + base64-inline the product photos referenced as src="ASSET:key"

The ASSET keys map to files by *substring* so we never have to hardcode the
awkward real filenames (spaces, apostrophes, an ellipsis char, mixed .jpg/.jpeg).

Requires: pip install "fonttools[woff]" brotli Pillow
"""
import base64, io, re, sys
from pathlib import Path
from fontTools.subset import Subsetter, Options
from fontTools.ttLib import TTFont

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
TEMPLATE = ROOT / "detail.template.html"
OUT = REPO / "detail.html"
FONTS = ROOT / "fonts"
ASSETS = REPO / "assets"

FACES = {
    "__SUIT_LIGHT__":     "SUIT-Light.otf",
    "__SUIT_MEDIUM__":    "SUIT-Medium.otf",
    "__SUIT_SEMIBOLD__":  "SUIT-SemiBold.otf",
    "__SUIT_EXTRABOLD__": "SUIT-ExtraBold.otf",
    "__PRE_REGULAR__":    "Pretendard-Regular.otf",
    "__PRE_MEDIUM__":     "Pretendard-Medium.otf",
    "__SCD5__":           "SCDream5.otf",
}

BASELINE = (
    " !\"#$%&'()*+,-./0123456789:;<=>?@"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`"
    "abcdefghijklmnopqrstuvwxyz{|}~"
    " ·–—‘’“”…→※₩✕✦☆★&"
)

# ASSET:key  ->  (filename substring, max width px, jpeg quality)
IMAGES = {
    "silk_smoke":   ("silk_smoke",        1600, 82),  # cover
    "spotlight":    ("spotlight",         1400, 82),  # the object
    "clasp_and_links": ("clasp_and_links",1200, 80),  # one line
    "macro":        ("IMG-03",            1100, 80),  # detail
    "velvet":       ("velvet",            1100, 80),  # detail
    "wrist_main":   ("IMG-02",            1000, 80),  # on the wrist (main)
    "wrist_sub":    ("on_woman",          1400, 80),  # on the wrist (full)
    "look1":        ("IMG-04",             900, 80),  # styling
    "look2":        ("IMG-05",             900, 80),
    "look3":        ("IMG-06",             900, 80),
    "look4":        ("IMG-07",             900, 80),
    "life1":        ("on_books",          1000, 80),  # in your day
    "life2":        ("granite",           1000, 80),
    "life3":        ("monstera",          1000, 80),
    "bowl":         ("in_bowl",           1400, 80),  # the set
    "box":          ("IMG-08",            1100, 80),  # in the box
    "closing":      ("IMG-09",            1300, 82),  # close
}


def build_charset(html: str) -> set:
    txt = html
    for tok in FACES:
        txt = txt.replace(tok, "")
    chars = set(txt) | set(BASELINE)
    for ch in "\n\t\r":
        chars.discard(ch)
    return chars


def subset_woff2(src: Path, unicodes: set) -> bytes:
    opt = Options()
    opt.flavor = "woff2"
    opt.desubroutinize = True
    opt.layout_features = ["*"]
    opt.name_IDs = []
    opt.notdef_outline = True
    opt.recalc_bounds = True
    opt.ignore_missing_unicodes = True
    opt.drop_tables += ["FFTM"]
    font = TTFont(str(src))
    ss = Subsetter(options=opt)
    ss.populate(unicodes=[ord(c) for c in unicodes])
    ss.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    return buf.getvalue()


def find_asset(substr: str) -> Path | None:
    for p in sorted(ASSETS.iterdir()):
        if p.is_file() and substr.lower() in p.name.lower():
            return p
    return None


def compress(path: Path, max_w: int, quality: int) -> bytes:
    from PIL import Image
    img = Image.open(path).convert("RGB")
    if img.width > max_w:
        h = int(img.height * max_w / img.width)
        img = img.resize((max_w, h), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=quality, optimize=True, progressive=True)
    return buf.getvalue()


def main():
    if not TEMPLATE.exists():
        sys.exit(f"missing template: {TEMPLATE}")
    html = TEMPLATE.read_text(encoding="utf-8")

    # ---- pass 1: fonts ----
    charset = build_charset(html)
    print(f"glyphs to embed: {len(charset)} unique characters")
    ftotal = 0
    for token, fname in FACES.items():
        src = FONTS / fname
        if not src.exists():
            sys.exit(f"missing font source: {src}")
        data = subset_woff2(src, charset)
        b64 = base64.b64encode(data).decode("ascii")
        html = html.replace(token, f"data:font/woff2;base64,{b64}")
        ftotal += len(data)
        print(f"  {fname:24} {len(data)/1024:7.1f} KB  (woff2)")
    print(f"embedded font payload: {ftotal/1024:.1f} KB")

    # ---- pass 2: images ----
    itotal_before = itotal_after = 0
    missing = []
    for key, (substr, max_w, q) in IMAGES.items():
        token = f"ASSET:{key}"
        if token not in html:
            print(f"  WARN token not used in template: {token}")
            continue
        src = find_asset(substr)
        if not src:
            missing.append((key, substr))
            print(f"  MISSING asset for '{key}' (substr '{substr}')")
            continue
        data = compress(src, max_w, q)
        itotal_before += src.stat().st_size
        itotal_after += len(data)
        b64 = base64.b64encode(data).decode("ascii")
        html = html.replace(token, f"data:image/jpeg;base64,{b64}")
        print(f"  {key:12} <- {src.name[:34]:34} {src.stat().st_size//1024:5}KB -> {len(data)//1024:4}KB")
    if missing:
        sys.exit(f"ERROR: {len(missing)} asset(s) not found: {missing}")

    OUT.write_text(html, encoding="utf-8")

    # ---- safety checks ----
    out_html = OUT.read_text(encoding="utf-8")
    leftover_tok = re.findall(r"__[A-Z0-9_]+__", out_html)
    leftover_ast = re.findall(r"ASSET:[a-z0-9_]+", out_html)
    if leftover_tok:
        sys.exit(f"ERROR leftover font tokens: {set(leftover_tok)}")
    if leftover_ast:
        sys.exit(f"ERROR leftover asset tokens: {set(leftover_ast)}")

    print(f"\nimages: {itotal_before//1024}KB original -> {itotal_after//1024}KB compressed")
    print(f"wrote {OUT}  ({OUT.stat().st_size/1024:.0f} KB total)")
    print("OK — no leftover tokens.")


if __name__ == "__main__":
    main()
