"""
Resize + compress images and inline them as base64 data URIs in index.html.
Replaces src="assets/IMG-XX.jpg" with src="data:image/jpeg;base64,..."
Run after subset_fonts.py (or the template will be missing font tokens).
"""
import base64, io, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
OUT = ROOT / "index.html"

# Max dimension and JPEG quality per image type
SIZES = {
    # wide hero / closeup (16:9 slots) — wider, moderate quality
    "IMG-01": (1400, 85),
    "IMG-09": (1200, 82),
    # tall look shots (3:4) — narrower on mobile
    "IMG-02": (900, 80),
    "IMG-04": (900, 80),
    "IMG-05": (900, 80),
    "IMG-06": (900, 80),
    "IMG-07": (900, 80),
    # square / 4:3
    "IMG-03": (1000, 80),
    "IMG-08": (1000, 80),
}

def compress(path, max_w, quality):
    from PIL import Image
    img = Image.open(path).convert("RGB")
    if img.width > max_w:
        h = int(img.height * max_w / img.width)
        img = img.resize((max_w, h), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=quality, optimize=True, progressive=True)
    return buf.getvalue()

html = OUT.read_text(encoding="utf-8")
total_before = sum((ASSETS / f"{k}.jpg").stat().st_size for k in SIZES if (ASSETS / f"{k}.jpg").exists())
total_after = 0

for name, (max_w, q) in SIZES.items():
    src_file = ASSETS / f"{name}.jpg"
    if not src_file.exists():
        print(f"SKIP {name} — not found in assets/")
        continue
    data = compress(src_file, max_w, q)
    total_after += len(data)
    b64 = base64.b64encode(data).decode("ascii")
    uri = f"data:image/jpeg;base64,{b64}"
    old = f'src="assets/{name}.jpg"'
    if old not in html:
        print(f"WARN: pattern not found for {name}")
        continue
    html = html.replace(old, f'src="{uri}"')
    print(f"  {name}: {src_file.stat().st_size//1024}KB -> {len(data)//1024}KB (q={q}, max_w={max_w})")

# data: URIs are already in memory — lazy loading stalls on mobile Safari/Chrome.
# Replace loading="lazy" with loading="eager" only on inlined img tags.
html = re.sub(
    r'(<img\b[^>]*src="data:image/[^"]+[^>]*)\bloading="lazy"',
    r'\1loading="eager"',
    html
)
OUT.write_text(html, encoding="utf-8")
size_total = OUT.stat().st_size
print(f"\nImages: {total_before//1024}KB original -> {total_after//1024}KB compressed")
print(f"index.html total: {size_total//1024}KB")

# Verify no leftover asset srcs
remaining = re.findall(r'src="assets/IMG', html)
if remaining:
    sys.exit(f"ERROR: {len(remaining)} asset src(s) still not inlined!")
print("All images inlined. No leftover asset srcs.")
