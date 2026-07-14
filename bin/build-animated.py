#!/usr/bin/env python3
"""Build the ANIMATED (active-state) variants of Stage Keys icons + a showcase.

Concept: an icon animates when its sound is ACTIVE (Stream Deck state 1 =
playing, state 0 = static), driven by the MIDI plugin's state feedback.

The motion should read as HOW A MUSICIAN PLAYS the instrument, and be clearly
visible — not a 2-pixel flicker:
  - struck / percussive / keys  -> a real bounce (the strike)
  - held winds & brass          -> a sway (the instrument moves as you blow)
  - plucked / bowed strings     -> a fast wobble (the strings vibrate)
  - accordion                   -> the bellows stretch in and out
  - cymbal / rotor              -> a spin
  - a hit / gunshot             -> a flash (scale burst)
  - synths / vocoder / drum machine / mellotron -> bespoke INTERNAL motion
    (scrolling waveforms, dancing bars, chasing LEDs, spinning tape reels…)

Bespoke motions are SVG phase(t)->svg rendered via the sdicons toolkit; the
gesture motions are PIL transforms of the static 144x144 icon (so every icon
moves visibly). Outputs looping 144x144 WEBP per icon + a full grid showcase.
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / ".." / "stream-deck-icons"))
from sdicons.animate import render_phases, save_animated          # noqa: E402
from PIL import Image, ImageDraw                                  # noqa: E402

# ---------------------------------------------------------------- bespoke SVG
H = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 144 144">'
KEYS = ('<rect x="14" y="78" width="116" height="16" rx="2" fill="#e6e6e6"/><g fill="#26262c">'
        '<rect x="22" y="78" width="3.5" height="10"/><rect x="32" y="78" width="3.5" height="10"/>'
        '<rect x="47" y="78" width="3.5" height="10"/><rect x="57" y="78" width="3.5" height="10"/>'
        '<rect x="67" y="78" width="3.5" height="10"/><rect x="82" y="78" width="3.5" height="10"/>'
        '<rect x="92" y="78" width="3.5" height="10"/><rect x="107" y="78" width="3.5" height="10"/>'
        '<rect x="117" y="78" width="3.5" height="10"/></g>')

def _knobs():
    return '<g fill="#3a3a44"><circle cx="24" cy="54" r="4"/><circle cx="36" cy="54" r="4"/><circle cx="48" cy="54" r="4"/></g>'

def synth(panel, screen, wave, accent):
    def f(t):
        return (H + f'<rect x="14" y="46" width="116" height="34" rx="4" fill="{panel}"/>' + _knobs()
                + f'<rect x="70" y="50" width="52" height="20" rx="2" fill="{screen}"/>'
                + '<defs><clipPath id="sw"><rect x="70" y="50" width="52" height="20"/></clipPath></defs>'
                + f'<g clip-path="url(#sw)">{wave(t, accent)}</g>' + KEYS
                + f'<rect x="16" y="80" width="6" height="12" rx="2" fill="{accent}"/></svg>')
    return f

def scroll_wave(t, c):
    return (f'<path transform="translate({-16*t:.2f} 0)" d="M56 60 q4 -7 8 0 t8 0 t8 0 t8 0 t8 0 t8 0 t8 0 t8 0 t8 0 t8 0" '
            f'fill="none" stroke="{c}" stroke-width="2"/>')
def soft_wave(t, c):
    return (f'<path transform="translate({-20*t:.2f} 0)" d="M52 60 q10 -8 20 0 t20 0 t20 0 t20 0 t20 0" '
            f'fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/>')
def deep_wave(t, c):
    return (f'<path transform="translate({-24*t:.2f} 0)" d="M48 60 q12 -12 24 0 t24 0 t24 0 t24 0" '
            f'fill="none" stroke="{c}" stroke-width="3.4" stroke-linecap="round"/>')
def square_wave(t, c):
    dx = -20*t
    return (f'<path transform="translate({dx:.2f} 0)" d="M52 66 L52 54 L62 54 L62 66 L72 66 L72 54 L82 54 L82 66 L92 66 L92 54 L102 54 L102 66 L112 66 L112 54 L122 54" '
            f'fill="none" stroke="{c}" stroke-width="2.4"/>')
def fx_wave(t, c):
    dx = -18*t
    return (f'<path transform="translate({dx:.2f} 0)" d="M52 60 q9 -10 18 0 t18 0 t18 0 t18 0 t18 0" fill="none" stroke="{c}" stroke-width="2.5"/>'
            f'<path transform="translate({-dx:.2f} 0)" d="M52 62 q9 8 18 0 t18 0 t18 0 t18 0 t18 0" fill="none" stroke="#3ee0c8" stroke-width="2" opacity="0.6"/>')

def vocoder(t):
    bars = ""
    for i, x in enumerate([62, 74, 86, 98, 110]):
        h = 32 + 18*math.sin(2*math.pi*t + i*1.2); y = 92 - h
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
    step = int(t*8) % 8
    cells = ""
    for i in range(8):
        x = 22 + i*13
        cells += f'<rect x="{x}" y="64" width="9" height="8" rx="2" fill="{"#f4d06a" if i==step else "#e8a53a"}"/>'
        cells += f'<rect x="{x}" y="80" width="9" height="8" rx="2" fill="{"#f27a6a" if i==(step+4)%8 else "#d8484a"}"/>'
    return (H + '<rect x="16" y="40" width="112" height="64" rx="8" fill="#2a2c33"/><rect x="16" y="40" width="112" height="16" rx="8" fill="#c0392b"/>'
            '<g fill="#e0e2e6"><circle cx="30" cy="48" r="4"/><circle cx="46" cy="48" r="4"/><circle cx="62" cy="48" r="4"/></g>'
            '<rect x="92" y="44" width="28" height="10" rx="2" fill="#69e069"/>' + cells + '<rect x="24" y="92" width="94" height="8" rx="2" fill="#e8c23a"/></svg>')

def arpeggio(t):
    lit = int(t*4) % 4
    xs = [24, 42, 60, 78]; ys = [66, 56, 46, 36]
    steps = "".join(f'<rect x="{xs[i]}" y="{ys[i]}" width="14" height="8" rx="2" fill="{"#f2c14e" if i==lit else "#3ee0c8"}"/>' for i in range(4))
    return (H + '<rect x="16" y="82" width="112" height="16" rx="2" fill="#ece8df"/>'
            '<g fill="#26262c"><rect x="24" y="82" width="4" height="10"/><rect x="34" y="82" width="4" height="10"/><rect x="49" y="82" width="4" height="10"/><rect x="59" y="82" width="4" height="10"/><rect x="69" y="82" width="4" height="10"/><rect x="84" y="82" width="4" height="10"/><rect x="94" y="82" width="4" height="10"/><rect x="109" y="82" width="4" height="10"/><rect x="119" y="82" width="4" height="10"/></g>'
            + steps + '<path d="M100 30 l10 -10 10 10" fill="none" stroke="#f2c14e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><line x1="110" y1="20" x2="110" y2="34" stroke="#f2c14e" stroke-width="3" stroke-linecap="round"/></svg>')

def vibraphone(t):
    # mallets strike: bounce down onto the bars
    my = 30 + 14*abs(math.sin(2*math.pi*t))
    bars = "".join(f'<rect x="{x}" y="44" width="12" height="24" rx="2" fill="#c9a24a"/>' for x in [24,40,56,72,88,104])
    bars2 = "".join(f'<rect x="{x}" y="74" width="15" height="30" rx="2" fill="#e0c266"/>' for x in [22,41,60,79,98])
    return (H + bars + bars2 + '<rect x="18" y="104" width="108" height="6" rx="3" fill="#6b6b70"/>'
            f'<line x1="60" y1="{my:.0f}" x2="112" y2="{my-48:.0f}" stroke="#7a5a2a" stroke-width="3" stroke-linecap="round"/><circle cx="60" cy="{my:.0f}" r="6" fill="#c0392b"/>'
            f'<line x1="74" y1="{my+4:.0f}" x2="122" y2="{my-40:.0f}" stroke="#7a5a2a" stroke-width="3" stroke-linecap="round"/><circle cx="74" cy="{my+4:.0f}" r="6" fill="#2b6cb0"/></svg>')

BESPOKE = {
    "mellotron": mellotron, "vocoder": vocoder, "drum-machine": drum_machine,
    "arpeggio": arpeggio, "vibraphone": vibraphone,
    "synth-lead": synth("#26262c", "#0f2a2a", scroll_wave, "#3ee0c8"),
    "synth-pad": synth("#2a2436", "#231633", soft_wave, "#b47cf0"),
    "synth-bass": synth("#20262e", "#0e1a26", deep_wave, "#3a86e0"),
    "synth-brass": synth("#2e2822", "#2e2408", square_wave, "#f0b93a"),
    "synth-fx": synth("#241a36", "#150e26", fx_wave, "#b47cf0"),
}

# ------------------------------------------------------- gesture motions (PIL)
def g_bounce(base, t, amp=9):
    dy = int(round(amp*math.sin(2*math.pi*t)))
    f = Image.new("RGBA", (144,144), (0,0,0,0)); f.alpha_composite(base, (0, dy)); return f

def g_sway(base, t, deg=7):
    return base.rotate(deg*math.sin(2*math.pi*t), resample=Image.BICUBIC, center=(72,118))

def g_wobble(base, t, amp=5, freq=3):
    dx = int(round(amp*math.sin(2*math.pi*freq*t)))
    f = Image.new("RGBA", (144,144), (0,0,0,0)); f.alpha_composite(base, (dx, 0)); return f

def g_stretch(base, t, amp=0.14):
    w = max(1, int(144*(1+amp*math.sin(2*math.pi*t))))
    f = Image.new("RGBA", (144,144), (0,0,0,0)); f.alpha_composite(base.resize((w,144)), ((144-w)//2, 0)); return f

def g_spin(base, t):
    return base.rotate(-360*t, resample=Image.BICUBIC, center=(72,72))

def g_flash(base, t, amp=0.28):
    w = max(1, int(144*(1+amp*max(0.0, math.sin(2*math.pi*t)))))
    r = base.resize((w,w)); f = Image.new("RGBA", (144,144), (0,0,0,0)); f.alpha_composite(r, ((144-w)//2, (144-w)//2)); return f

GESTURE = {"bounce": g_bounce, "sway": g_sway, "wobble": g_wobble,
           "stretch": g_stretch, "spin": g_spin, "flash": g_flash}

FAMILY = {}
def _fam(names, g):
    for n in names.split():
        FAMILY[n] = g
_fam("piano-grand piano-upright ep-rhodes ep-wurlitzer ep-fm clavinet celesta glockenspiel "
     "marimba xylophone dulcimer timpani agogo steel-drums woodblock taiko melodic-tom "
     "synth-drum drum-kit sampler music-box synthesizer tinkle-bell kalimba", "bounce")
_fam("saxophone oboe english-horn bassoon clarinet piccolo flute recorder shakuhachi whistle "
     "trumpet trombone tuba french-horn brass-section bagpipe harmonica tubular-bells "
     "organ-tonewheel organ-combo organ-pipe pan-flute blown-bottle ocarina choir "
     "breath-noise seashore bird-tweet", "sway")
_fam("guitar-acoustic guitar-electric bass-electric double-bass violin viola cello "
     "strings-section harp sitar banjo shamisen koto harpsichord", "wobble")
_fam("accordion", "stretch")
_fam("reverse-cymbal helicopter", "spin")
_fam("orchestra-hit gunshot telephone applause", "flash")

# --------------------------------------------------------------------- build
N, FPS = 24, 12
OUT = Path("animated"); (OUT/"icons").mkdir(parents=True, exist_ok=True)
order = list(json.load(open("tags.json")))
allframes = {}
for slug in order:
    if slug in BESPOKE:
        frames = render_phases(BESPOKE[slug], N)
    else:
        png = Path("icons")/f"{slug}.png"
        if not png.exists():
            continue
        base = Image.open(png).convert("RGBA")
        g = GESTURE[FAMILY.get(slug, "bounce")]
        frames = [g(base, k/N) for k in range(N)]
    allframes[slug] = frames
    save_animated(frames, OUT/"icons"/f"{slug}.webp", FPS)

order = [s for s in order if s in allframes]
cols = 10; cell = 108; pad = 6
rows = (len(order)+cols-1)//cols
W = cols*cell+(cols+1)*pad; Hh = rows*cell+(rows+1)*pad
# Showcase on a TRANSPARENT background (no tiles) — the icons themselves are
# transparent, so the README image lets the page show through behind them.
grid = []
for k in range(N):
    im = Image.new("RGBA", (W, Hh), (0, 0, 0, 0))
    for i, slug in enumerate(order):
        r, c = divmod(i, cols); x = pad+c*(cell+pad); y = pad+r*(cell+pad)
        im.alpha_composite(allframes[slug][k].resize((cell-8, cell-8)), (x+4, y+4))
    grid.append(im)
grid[0].save("animated-showcase.webp", format="WEBP", save_all=True,
             append_images=grid[1:], duration=int(1000/FPS), loop=0, quality=80, method=6)
print(f"wrote animated-showcase.webp ({len(order)} icons) + animated/icons/*.webp")
