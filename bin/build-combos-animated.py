#!/usr/bin/env python3
"""Animated (playing) variants of the split combo tiles.

A combo tile is opaque (dark bg + diagonal separator), so a whole-tile gesture
would tear (the tile would shift and reveal a gap). Instead each half gets TRUE
internal motion: we reuse `frames_for(slug)` from build-animated.py to animate
each instrument, then composite the two moving halves into the fixed tile — the
same diagonal placement gen_duo.py uses for the static version.

Run AFTER static render (needs icons/<instrument>.png for gesture instruments)
and independently of build-animated.py. Outputs animated/icons/<combo>.webp.
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

BIN = Path(__file__).resolve().parent


def _load(mod_name, filename):
    spec = importlib.util.spec_from_file_location(mod_name, BIN / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# gen_duo: PRESETS + placement (ANCHOR/targets/tile colours). build-animated:
# per-instrument frames + save_animated + N/FPS. Both live in bin/.
gd = _load("gen_duo", "gen_duo.py")
ba = _load("build_animated", "build-animated.py")

from PIL import Image  # noqa: E402


def tile_base():
    """Render the empty combo tile (bg + separator) once, as a 144 RGBA image."""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="0 0 144 144">'
           f'<rect width="144" height="144" rx="22" fill="{gd.BG}"/>'
           f'<path d="M14,20 L128,128" stroke="{gd.SEP}" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>'
           f'</svg>')
    svgp = ba.OUT / "_tilebase.svg"
    ba.OUT.mkdir(parents=True, exist_ok=True)
    svgp.write_text(svg)
    pngp = ba.OUT / "_tilebase.png"
    subprocess.run(["rsvg-convert", "-w", "144", "-h", "144", str(svgp), "-o", str(pngp)], check=True)
    img = Image.open(pngp).convert("RGBA")
    svgp.unlink(); pngp.unlink()
    return img


def place(frame, target, anchor):
    """Scale a 144 instrument frame by anchor and return (scaled, offset)."""
    cx, cy, s = anchor
    sc = frame.resize((round(144 * s), round(144 * s)))
    off = (round(target[0] - cx * s), round(target[1] - cy * s))
    return sc, off


def main():
    base = tile_base()
    outdir = ba.OUT / "icons"; outdir.mkdir(parents=True, exist_ok=True)
    n = 0
    for a, b, name in gd.PRESETS:
        fa = ba.frames_for(a)
        fb = ba.frames_for(b)
        if fa is None or fb is None:
            print(f"  skip {name}: missing frames for "
                  f"{a if fa is None else ''}{b if fb is None else ''}")
            continue
        anc_a = gd.ANCHOR.get(a, gd.DEFAULT_ANCHOR)
        anc_b = gd.ANCHOR.get(b, gd.DEFAULT_ANCHOR)
        frames = []
        for k in range(ba.N):
            tile = base.copy()
            # draw B (upper-right) then A (lower-left) on top — matches gen_duo.
            sb, ob = place(fb[k], gd.TARGET_TR, anc_b); tile.paste(sb, ob, sb)
            sa, oa = place(fa[k], gd.TARGET_BL, anc_a); tile.paste(sa, oa, sa)
            frames.append(tile)
        ba.save_animated(frames, outdir / f"{name}.webp", ba.FPS)
        n += 1
    print(f"wrote {n} animated combo tiles -> animated/icons/*.webp")


if __name__ == "__main__":
    main()
