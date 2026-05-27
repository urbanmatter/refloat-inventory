"""Generate a professional app icon for ReFloat Inventory."""
import math
from PIL import Image, ImageDraw, ImageFilter

W = 1024            # supersampled canvas
C = W / 2           # center
SS = 4              # extra supersample factor for crisp edges
N = W * SS

PRIMARY = (91, 75, 225)     # #5B4BE1
ACCENT  = (124, 110, 240)   # #7C6EF0
WHITE   = (255, 255, 255)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


# ---- base canvas (RGBA, transparent) ----
img = Image.new("RGBA", (N, N), (0, 0, 0, 0))

# ---- vertical gradient (accent top -> primary bottom) ----
grad = Image.new("RGB", (N, N))
gd = ImageDraw.Draw(grad)
for y in range(N):
    gd.line([(0, y), (N, y)], fill=lerp(ACCENT, PRIMARY, y / N))

# ---- rounded-square mask ----
mask = Image.new("L", (N, N), 0)
md = ImageDraw.Draw(mask)
md.rounded_rectangle([0, 0, N - 1, N - 1], radius=int(N * 0.225), fill=255)
img.paste(grad, (0, 0), mask)

draw = ImageDraw.Draw(img)
cx = cy = N / 2

# ============================================================
# Circular arrows (circular-economy loop) around the pane
# ============================================================
R = N * 0.325          # ring radius
LW = int(N * 0.052)    # ring stroke width
ah = N * 0.085         # arrowhead size

def deg(a):
    return a * math.pi / 180

def pt(angle):
    return (cx + R * math.cos(deg(angle)), cy + R * math.sin(deg(angle)))

def arrowhead(angle, color):
    """Triangle pointing along the clockwise tangent at `angle`."""
    a = deg(angle)
    px, py = cx + R * math.cos(a), cy + R * math.sin(a)
    # clockwise tangent (screen coords, y down)
    tx, ty = -math.sin(a), math.cos(a)
    nx, ny = math.cos(a), math.sin(a)          # radial (outward)
    tip = (px + tx * ah, py + ty * ah)
    b1  = (px + nx * (LW * 0.95), py + ny * (LW * 0.95))
    b2  = (px - nx * (LW * 0.95), py - ny * (LW * 0.95))
    draw.polygon([tip, b1, b2], fill=color)

bbox = [cx - R, cy - R, cx + R, cy + R]
# two arcs leaving gaps for the arrowheads
draw.arc(bbox, start=28, end=178, fill=WHITE, width=LW)
draw.arc(bbox, start=208, end=358, fill=WHITE, width=LW)
arrowhead(178, WHITE)
arrowhead(358, WHITE)

# ============================================================
# Glass pane in the centre (two offset panes = flat glass)
# ============================================================
def pane(offx, offy, half, alpha, radius):
    layer = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    box = [cx - half + offx, cy - half + offy, cx + half + offx, cy + half + offy]
    ld.rounded_rectangle(box, radius=radius, fill=(255, 255, 255, alpha))
    img.alpha_composite(layer)
    return box

half = N * 0.150
rad = int(N * 0.045)
# back pane (slightly translucent, offset up-left)
pane(-N * 0.028, -N * 0.028, half, 150, rad)
# front pane (solid)
front = pane(N * 0.022, N * 0.022, half, 255, rad)

# diagonal "shine" on the front pane
shine = Image.new("RGBA", (N, N), (0, 0, 0, 0))
sd = ImageDraw.Draw(shine)
x0, y0, x1, y1 = front
w = x1 - x0
sd.polygon([
    (x0 + w * 0.16, y0), (x0 + w * 0.40, y0),
    (x0 + w * 0.10, y1), (x0 - w * 0.14, y1),
], fill=(124, 110, 240, 70))
# clip shine to the front pane
pmask = Image.new("L", (N, N), 0)
ImageDraw.Draw(pmask).rounded_rectangle(front, radius=rad, fill=255)
img.paste(shine, (0, 0), Image.composite(shine.split()[3], Image.new("L", (N, N), 0), pmask))

# ---- downscale to crisp 1024, then export .ico ----
final = img.resize((W, W), Image.LANCZOS)
final.save("icon_preview.png")

sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (24, 24), (16, 16)]
final.save("ReFloat.ico", format="ICO", sizes=sizes)
print("Saved ReFloat.ico and icon_preview.png")
