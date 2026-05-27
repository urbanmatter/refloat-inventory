"""Embed ReFloat.ico into index.html as a base64 favicon + header logo."""
import base64, io
from PIL import Image

# load the icon and render a crisp 128px PNG
im = Image.open("ReFloat.ico")
im.size  # touch
im = im.convert("RGBA").resize((128, 128), Image.LANCZOS)
buf = io.BytesIO()
im.save(buf, format="PNG")
uri = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

html = open("index.html", encoding="utf-8").read()

# 1) favicon in the tab bar
if 'rel="icon"' not in html:
    html = html.replace(
        "<title>ReFloat Inventory</title>",
        '<title>ReFloat Inventory</title>\n<link rel="icon" type="image/png" href="' + uri + '">',
    )

# 2) header logo (replace the ◆ glyph with the icon image)
html = html.replace(
    '<span class="hd-mark">◆</span>',
    '<img class="hd-mark" src="' + uri + '" alt="ReFloat Inventory">',
)

open("index.html", "w", encoding="utf-8").write(html)
print("done. data-uri bytes:", len(uri))
