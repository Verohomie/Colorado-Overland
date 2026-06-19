#!/usr/bin/env python3
"""
Turn a source tire/wheel SVG into the full home-screen icon set.

Wraps the artwork on a grey rounded-square background, centered + scaled,
then rasterizes with qlmanage and resizes with sips (macOS built-ins).

Usage:
  python3 make_icon.py [source.svg]
If no source is given, it picks the newest .svg in the project that isn't icon.svg.

Outputs: icon.svg, apple-touch-icon.png (180), icon-192.png, icon-512.png, favicon.ico
"""
import os, re, sys, glob, subprocess, struct

ROOT = os.path.dirname(os.path.abspath(__file__))

def pick_source():
    if len(sys.argv) > 1:
        return sys.argv[1]
    cands = [p for p in glob.glob(os.path.join(ROOT, "**", "*.svg"), recursive=True)
             if os.path.basename(p) != "icon.svg" and "/.git/" not in p]
    if not cands:
        sys.exit("No source SVG found. Save the tire SVG into the project (e.g. images/tire.svg) "
                 "or pass its path: python3 make_icon.py images/tire.svg")
    cands.sort(key=os.path.getmtime, reverse=True)
    return cands[0]

def build_wrapper(src_path):
    svg = open(src_path, encoding="utf-8").read()
    m = re.search(r'viewBox\s*=\s*"([\d.\- ]+)"', svg)
    if not m:
        sys.exit("Source SVG has no viewBox; can't scale it.")
    vx, vy, vw, vh = (float(x) for x in m.group(1).split())
    # inner content = everything between the opening <svg ...> tag and the final </svg>
    inner = re.sub(r'^.*?<svg[^>]*>', '', svg, count=1, flags=re.S)
    inner = re.sub(r'</svg>\s*$', '', inner, flags=re.S)

    S = 1024
    margin = 84
    usable = S - 2 * margin
    scale = min(usable / vw, usable / vh)
    offx = (S - vw * scale) / 2 - vx * scale
    offy = (S - vh * scale) / 2 - vy * scale

    out = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {S} {S}">
<defs>
<radialGradient id="bgWheel" cx="0.5" cy="0.38" r="0.9">
 <stop offset="0" stop-color="#F6B25E"/><stop offset="0.5" stop-color="#E67E22"/><stop offset="1" stop-color="#B85F12"/>
</radialGradient>
</defs>
<rect width="{S}" height="{S}" rx="224" fill="url(#bgWheel)"/>
<g transform="translate({offx:.2f},{offy:.2f}) scale({scale:.5f})">
{inner}
</g>
</svg>'''
    open(os.path.join(ROOT, "icon.svg"), "w", encoding="utf-8").write(out)
    print(f"  wrote icon.svg  (source {os.path.basename(src_path)}, viewBox {vw:.0f}x{vh:.0f}, scale {scale:.3f})")

def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def rasterize():
    tmp = "/tmp/co_icon"
    os.makedirs(tmp, exist_ok=True)
    run(["qlmanage", "-t", "-s", "1024", "-o", tmp, os.path.join(ROOT, "icon.svg")])
    big = os.path.join(tmp, "icon.svg.png")
    if not os.path.exists(big):
        sys.exit("qlmanage failed to rasterize icon.svg")
    for size, name in [(180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")]:
        run(["sips", "-z", str(size), str(size), big, "--out", os.path.join(ROOT, name)])
    # favicon.ico = ICO wrapping a 256px PNG
    run(["sips", "-z", "256", "256", big, "--out", os.path.join(tmp, "i256.png")])
    png = open(os.path.join(tmp, "i256.png"), "rb").read()
    hdr = struct.pack("<HHH", 0, 1, 1)
    ent = struct.pack("<BBBBHHII", 0, 0, 0, 0, 1, 32, len(png), 22)
    open(os.path.join(ROOT, "favicon.ico"), "wb").write(hdr + ent + png)
    print("  wrote apple-touch-icon.png (180), icon-192.png, icon-512.png, favicon.ico")

if __name__ == "__main__":
    src = pick_source()
    build_wrapper(src)
    rasterize()
    print("Done. Review apple-touch-icon.png, then commit.")
