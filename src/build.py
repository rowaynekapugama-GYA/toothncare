#!/usr/bin/env python3
"""Inline ./assets images into index.html as base64 data URLs -> dist/toothncare-home.html"""
import base64, mimetypes, pathlib, re, sys

root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text()

def to_data_url(m):
    rel = m.group(1)
    p = root / rel
    if not p.exists():
        print(f"  !! missing asset: {rel}", file=sys.stderr)
        return m.group(0)
    mime = mimetypes.guess_type(p.name)[0] or "image/webp"
    b64 = base64.b64encode(p.read_bytes()).decode()
    print(f"  inlined {rel} ({p.stat().st_size//1024} KB)")
    return f'src="data:{mime};base64,{b64}"'

out = re.sub(r'src="(assets/[^"]+)"', to_data_url, html)
dist = root / "dist"; dist.mkdir(exist_ok=True)
target = dist / "toothncare-home.html"
target.write_text(out)
print(f"wrote {target} ({target.stat().st_size//1024} KB)")
