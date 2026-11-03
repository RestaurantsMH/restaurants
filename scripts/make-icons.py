"""Generate the app icons (needs Pillow). Run from the repo root: python3 scripts/make-icons.py"""
from PIL import Image, ImageDraw

BG, PLATE, RIM, ACC = (22, 18, 17), (244, 238, 232), (200, 190, 180), (232, 128, 90)  # dark warm background, white plate, terracotta

def draw(size, safe):
    s = size * 4
    img = Image.new("RGB", (s, s), BG)  # full-bleed so the maskable version survives any mask shape
    d = ImageDraw.Draw(img)
    box = s * safe
    cx = cy = s / 2
    r = box * 0.40
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=PLATE)
    r2 = r * 0.70
    d.ellipse([cx - r2, cy - r2, cx + r2, cy + r2], outline=RIM, width=max(2, int(box * 0.012)))
    # a terracotta dot in the middle of the plate: the table you booked
    r3 = r * 0.20
    d.ellipse([cx - r3, cy - r3, cx + r3, cy + r3], fill=ACC)
    return img.resize((size, size), Image.LANCZOS)

draw(192, 0.80).save("icon-192.png")
draw(512, 0.80).save("icon-512.png")
draw(512, 0.60).save("icon-maskable-512.png")
print("icons written")
