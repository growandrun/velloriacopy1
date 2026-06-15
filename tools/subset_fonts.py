#!/usr/bin/env python3
"""Subset the 3 Korean font families to exactly the glyphs used in
tools/index.template.html, embed them as base64 woff2, and write index.html.

Re-run this whenever the Korean copy changes (new syllables need re-subsetting).
Requires: fonttools + brotli  (pip install "fonttools[woff]" brotli)
"""
import base64, io, re, sys
from pathlib import Path
from fontTools.subset import Subsetter, Options
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
TEMPLATE = ROOT / "index.template.html"
OUT = REPO / "index.html"
FONTS = ROOT / "fonts"

# token in template  ->  source font file
FACES = {
    "__SUIT_LIGHT__":    "SUIT-Light.otf",
    "__SUIT_MEDIUM__":   "SUIT-Medium.otf",
    "__SUIT_SEMIBOLD__": "SUIT-SemiBold.otf",
    "__SUIT_EXTRABOLD__": "SUIT-ExtraBold.otf",
    "__PRE_REGULAR__":   "Pretendard-Regular.otf",
    "__PRE_MEDIUM__":    "Pretendard-Medium.otf",
    "__SCD5__":          "SCDream5.otf",
}

# Always-include baseline so UI chrome never breaks even if a glyph isn't in copy.
BASELINE = (
    " !\"#$%&'()*+,-./0123456789:;<=>?@"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`"
    "abcdefghijklmnopqrstuvwxyz{|}~"
    " ·–—‘’“”…→※₩✕✦☆★"
)

def build_charset(html: str) -> set:
    # strip the @font-face src tokens so they don't add stray glyphs, then take
    # every remaining character (visible copy + markup). Markup is ASCII anyway.
    txt = html
    for tok in FACES:
        txt = txt.replace(tok, "")
    chars = set(txt) | set(BASELINE)
    chars.discard("\n"); chars.discard("\t"); chars.discard("\r")
    return chars

def subset_woff2(src: Path, unicodes: set) -> bytes:
    opt = Options()
    opt.flavor = "woff2"
    opt.desubroutinize = True
    opt.layout_features = ["*"]
    opt.name_IDs = []          # drop name table -> smaller
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

def main():
    html = TEMPLATE.read_text(encoding="utf-8")
    charset = build_charset(html)
    print(f"glyphs to embed: {len(charset)} unique characters")
    total = 0
    for token, fname in FACES.items():
        src = FONTS / fname
        if not src.exists():
            sys.exit(f"missing font source: {src}\n  -> copy the 6 .otf files into tools/fonts/ (see README)")
        data = subset_woff2(src, charset)
        b64 = base64.b64encode(data).decode("ascii")
        uri = f"data:font/woff2;base64,{b64}"
        if token not in html:
            sys.exit(f"token {token} not found in template")
        html = html.replace(token, uri)
        total += len(data)
        print(f"  {fname:24} {len(data)/1024:7.1f} KB  (woff2)")
    OUT.write_text(html, encoding="utf-8")
    size = OUT.stat().st_size
    print(f"embedded font payload: {total/1024:.1f} KB")
    print(f"wrote {OUT}  ({size/1024:.1f} KB total)")
    # safety: no leftover tokens
    leftover = re.findall(r"__[A-Z0-9_]+__", OUT.read_text(encoding="utf-8"))
    if leftover:
        sys.exit(f"ERROR leftover tokens: {set(leftover)}")

if __name__ == "__main__":
    main()
