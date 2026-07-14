#!/usr/bin/env python3
"""Build the ANIMATED variants of Stage Keys icons + a grid showcase.

Concept: an animated icon is the ACTIVE state of a sound. On a Stream Deck,
wire state 0 = the static icon (idle) and state 1 = the animated one (playing),
driven by the MIDI plugin's state feedback. So each animated instrument here is
meant to be used as its "active/playing" image.

Each motion is phase(t)->svg for t in [0,1); rendered to a looping 144x144 WEBP
via the sdicons toolkit (animate_svg), and composited into one grid GIF for the
README (like wled-assets' effects-grid.gif).
"""
import math, os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / ".." / "stream-deck-icons"))
from sdicons.animate import render_phases, save_animated  # noqa: E402
from PIL import Image  # noqa: E402

H = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 144 144">'
KEYS = ('<rect x="14" y="78" width="116" height="16" rx="2" fill="#e6e6e6"/><g fill="#26262c">'
        '<rect x="22" y="78" width="3.5" height="10"/><rect x="32" y="78" width="3.5" height="10"/>'
        '<rect x="47" y="78" width="3.5" height="10"/><rect x="57" y="78" width="3.5" height="10"/>'
        '<rect x="67" y="78" width="3.5" height="10"/><rect x="82" y="78" width="3.5" height="10"/>'
        '<rect x="92" y="78" width="3.5" height="10"/><rect x="107" y="78" width="3.5" height="10"/>'
        '<rect x="117" y="78" width="3.5" height="10"/></g>')

def _knobs(fill="#3a3a44"):
    return f'<g fill="{fill}"><circle cx="24" cy="54" r="4"/><circle cx="36" cy="54" r="4"/><circle cx="48" cy="54" r="4"/></g>'

def synth(panel, screen, wave_fn, accent):
    """A synth: panel + screen with an animated wave, over the keybed."""
    def f(t):
        return (H + f'<rect x="14" y="46" width="116" height="34" rx="4" fill="{panel}"/>' + _knobs()
                + f'<rect x="70" y="50" width="52" height="20" rx="2" fill="{screen}"/>'
                + '<defs><clipPath id="sw"><rect x="70" y="50" width="52" height="20"/></clipPath></defs>'
                + f'<g clip-path="url(#sw)">{wave_fn(t, accent)}</g>'
                + KEYS + f'<rect x="16" y="80" width="6" height="12" rx="2" fill="{accent}"/></svg>')
    return f

def scroll_wave(t, c):
    dx = -16 * t
    return (f'<path transform="translate({dx:.2f} 0)" d="M56 60 q4 -7 8 0 t8 0 t8 0 t8 0 t8 0 t8 0 t8 0 t8 0 t8 0 t8 0" '
            f'fill="none" stroke="{c}" stroke-width="2"/>')
def soft_wave(t, c):
    dx = -20 * t
    return (f'<path transform="translate({dx:.2f} 0)" d="M52 60 q10 -8 20 0 t20 0 t20 0 t20 0 t20 0" '
            f'fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" opacity="0.9"/>')
def deep_wave(t, c):
    dx = -24 * t
    return (f'<path transform="translate({dx:.2f} 0)" d="M48 60 q12 -12 24 0 t24 0 t24 0 t24 0" '
            f'fill="none" stroke="{c}" stroke-width="3.4" stroke-linecap="round"/>')
def fx_wave(t, c):
    dx = -18 * t
    return (f'<path transform="translate({dx:.2f} 0)" d="M52 60 q9 -10 18 0 t18 0 t18 0 t18 0 t18 0" fill="none" stroke="{c}" stroke-width="2.5"/>'
            f'<path transform="translate({-dx:.2f} 0)" d="M52 62 q9 8 18 0 t18 0 t18 0 t18 0 t18 0" fill="none" stroke="#3ee0c8" stroke-width="2" opacity="0.6"/>')

def vocoder(t):
    bars = ""
    for i, x in enumerate([62,74,86,98,110]):
        h = 30 + 14*math.sin(2*math.pi*t + i*1.2); y = 92 - h
        bars += f'<rect x="{x}" y="{y:.1f}" width="9" height="{h:.1f}" fill="#3ee0c8"/>'
    return (H + '<rect x="20" y="34" width="18" height="40" rx="9" fill="#3a3d44"/>'
            '<rect x="27" y="74" width="4" height="14" fill="#6a6e78"/><rect x="18" y="90" width="22" height="5" rx="2" fill="#6a6e78"/>'
            '<rect x="52" y="38" width="74" height="62" rx="6" fill="#20222a"/>' + bars + '</svg>')

def mellotron(t):
    a = t*360
    def reel(cx):
        return (f'<circle cx="{cx}" cy="66" r="15" fill="#2a2a2e"/><circle cx="{cx}" cy="66" r="15" fill="none" stroke="#c9ccd2" stroke-width="2"/>'
                f'<g stroke="#8a8e94" stroke-width="2" transform="rotate({a} {cx} 66)"><line x1="{cx}" y1="53" x2="{cx}" y2="79"/><line x1="{cx-13}" y1="66" x2="{cx+13}" y2="66"/></g>'
                f'<circle cx="{cx}" cy="66" r="4" fill="#c9ccd2"/>')
    return (H + '<rect x="18" y="40" width="108" height="64" rx="6" fill="#6b4322"/><rect x="18" y="40" width="108" height="12" rx="6" fill="#7d5028"/>'
            + reel(46) + reel(98)
            + '<rect x="24" y="90" width="96" height="14" rx="2" fill="#f2ede0"/><g fill="#2a1c10"><rect x="30" y="90" width="4" height="9"/><rect x="40" y="90" width="4" height="9"/><rect x="54" y="90" width="4" height="9"/><rect x="64" y="90" width="4" height="9"/><rect x="78" y="90" width="4" height="9"/><rect x="92" y="90" width="4" height="9"/><rect x="106" y="90" width="4" height="9"/></g></svg>')

def drum_machine(t):
    step = int(t*7) % 7
    cells = ""
    for i in range(7):
        x = 24 + i*14
        on = (i == step)
        cells += f'<rect x="{x}" y="64" width="10" height="8" rx="2" fill="{"#f4d06a" if on else "#e8a53a"}"/>'
        cells += f'<rect x="{x}" y="80" width="10" height="8" rx="2" fill="{"#f27a6a" if (i==(step+3)%7) else "#d8484a"}"/>'
    return (H + '<rect x="16" y="40" width="112" height="64" rx="8" fill="#2a2c33"/><rect x="16" y="40" width="112" height="16" rx="8" fill="#c0392b"/>'
            '<g fill="#e0e2e6"><circle cx="30" cy="48" r="4"/><circle cx="46" cy="48" r="4"/><circle cx="62" cy="48" r="4"/></g>'
            '<rect x="92" y="44" width="28" height="10" rx="2" fill="#69e069"/>' + cells + '<rect x="24" y="92" width="94" height="8" rx="2" fill="#e8c23a"/></svg>')

def arpeggio(t):
    lit = int(t*4) % 4
    steps = ""
    ys = [66,56,46,36]; xs=[24,42,60,78]
    for i in range(4):
        c = "#f2c14e" if i==lit else "#3ee0c8"
        steps += f'<rect x="{xs[i]}" y="{ys[i]}" width="14" height="8" rx="2" fill="{c}"/>'
    return (H + KEYS.replace('#e6e6e6','#ece8df')
            + '<rect x="16" y="82" width="112" height="0" />' + steps
            + '<path d="M100 30 l10 -10 10 10" fill="none" stroke="#f2c14e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><line x1="110" y1="20" x2="110" y2="34" stroke="#f2c14e" stroke-width="3" stroke-linecap="round"/></svg>')

def vibraphone(t):
    bars = ""
    for i,x in enumerate([24,40,56,72,88,104]):
        o = 0.55 + 0.45*abs(math.sin(2*math.pi*t + i*0.9))
        bars += f'<rect x="{x}" y="44" width="12" height="24" rx="2" fill="#c9a24a" opacity="{o:.2f}"/>'
    bars2 = ""
    for i,x in enumerate([22,41,60,79,98]):
        o = 0.55 + 0.45*abs(math.sin(2*math.pi*t + i*0.9 + 1))
        bars2 += f'<rect x="{x}" y="74" width="15" height="30" rx="2" fill="#e0c266" opacity="{o:.2f}"/>'
    return (H + f'<g>{bars}</g><g>{bars2}</g><rect x="18" y="104" width="108" height="6" rx="3" fill="#6b6b70"/>'
            '<g fill="#8a8a90"><rect x="26" y="110" width="4" height="14"/><rect x="52" y="110" width="4" height="16"/><rect x="80" y="110" width="4" height="14"/><rect x="106" y="110" width="4" height="12"/></g></svg>')

MOTIONS = {
  "mellotron": mellotron,
  "vocoder": vocoder,
  "synth-lead": synth("#26262c", "#0f2a2a", scroll_wave, "#3ee0c8"),
  "synth-pad": synth("#2a2436", "#231633", soft_wave, "#b47cf0"),
  "synth-bass": synth("#20262e", "#0e1a26", deep_wave, "#3a86e0"),
  "synth-fx": synth("#241a36", "#150e26", fx_wave, "#b47cf0"),
  "drum-machine": drum_machine,
  "arpeggio": arpeggio,
  "vibraphone": vibraphone,
}

import json as _json
from PIL import ImageDraw
OUT = Path("animated"); (OUT/"icons").mkdir(parents=True, exist_ok=True)
N, FPS = 24, 12

def pulse_frames(png, n, ph):
    """Subtle 'active' breathing + bob of a static icon (for non-bespoke ones)."""
    base = Image.open(png).convert("RGBA"); out = []
    for k in range(n):
        u = 2*math.pi*(k/n) + ph
        s = 1 + 0.06*math.sin(u); w = max(1, int(144*s))
        bob = int(round(2*math.sin(u + 1)))
        r = base.resize((w, w)); f = Image.new("RGBA", (144,144), (0,0,0,0))
        f.alpha_composite(r, ((144-w)//2, (144-w)//2 + bob)); out.append(f)
    return out

# bespoke motions -> also saved as standalone active-state WEBP assets
allframes = {}
for name, fn in MOTIONS.items():
    fr = render_phases(fn, N); allframes[name] = fr
    save_animated(fr, OUT/"icons"/f"{name}.webp", FPS)

# full showcase: EVERY icon animated — bespoke where defined, else a subtle
# staggered active pulse of the static icon.
order = list(_json.load(open("tags.json")))
for idx, slug in enumerate(order):
    if slug not in allframes:
        png = Path("icons")/f"{slug}.png"
        if png.exists():
            allframes[slug] = pulse_frames(png, N, idx*0.4)
order = [s for s in order if allframes.get(s)]
cols = 10; cell = 108; pad = 6
rows = (len(order)+cols-1)//cols
W = cols*cell+(cols+1)*pad; Hh = rows*cell+(rows+1)*pad
grid = []
for k in range(N):
    im = Image.new("RGBA",(W,Hh),(20,20,24,255)); d = ImageDraw.Draw(im)
    for i,slug in enumerate(order):
        r,c = divmod(i,cols); x=pad+c*(cell+pad); y=pad+r*(cell+pad)
        d.rounded_rectangle([x,y,x+cell,y+cell],radius=12,fill=(28,28,31,255),outline=(52,52,60,255))
        im.alpha_composite(allframes[slug][k].resize((cell-14,cell-14)),(x+7,y+7))
    grid.append(im)
grid[0].save("animated-showcase.webp", format="WEBP", save_all=True,
             append_images=grid[1:], duration=int(1000/FPS), loop=0,
             quality=80, method=6)
print(f"wrote animated-showcase.webp ({len(order)} icons) + animated/icons/*.webp")
