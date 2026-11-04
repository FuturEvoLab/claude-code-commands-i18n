#!/usr/bin/env python3
"""Make docs/assets/social.png (1200x630 link-preview card) and shrink the screenshots.

Run after scripts/screenshots.sh. Needs Pillow (pip install pillow); the site build does not.
Screenshots are flat UI colours, so a 256-colour palette keeps text sharp at a fraction of the size.
"""
from pathlib import Path

from PIL import Image

ASSETS = Path(__file__).resolve().parent.parent / "docs/assets"


def save_small(img, path):
    img.convert("RGB").quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(path, optimize=True)


src = Image.open(ASSETS / "preview-en.png").convert("RGB")
w = src.width
card = src.crop((0, 0, w, round(w * 630 / 1200))).resize((1200, 630), Image.Resampling.LANCZOS)
save_small(card, ASSETS / "social.png")

for p in sorted(ASSETS.glob("preview-*.png")):
    before = p.stat().st_size
    save_small(Image.open(p), p)
    print(f"{p.name}: {before // 1024} KB -> {p.stat().st_size // 1024} KB")
print(f"social.png: {(ASSETS / 'social.png').stat().st_size // 1024} KB")
