#!/usr/bin/env python3
"""gen_duo.py — build "split-view" combo buttons from two pack instruments.

A split button shows TWO instruments on one 144x144 Stream Deck key, divided
diagonally: instrument A in the lower-left ↙, instrument B in the upper-right ↗,
over a dark tile with a thin diagonal separator. Use it for a key that layers or
morphs two sounds (e.g. piano + brass), so the pairing reads at a glance under
stage lighting — the same design goal as the single-instrument icons.

It composes the pack's own full-colour sources in src/*.svg (no redraw), so a
combo always matches the single icons it is made of.

Usage:
    bin/gen_duo.py                      # build the default combo set (below)
    bin/gen_duo.py piano-upright trumpet
    bin/gen_duo.py ep-rhodes saxophone rhodes+sax
        A = lower-left, B = upper-right, optional 3rd arg = output basename.

Output: duo/<name>.png (144x144) + duo/svg/<name>.svg. Any two of the pack's
instruments work — pass source basenames from src/ (see README / GM-MAP.md).
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(ROOT, "src")          # full-colour instrument sources
OUT = os.path.join(ROOT, "duo")          # generated combo buttons
SVGOUT = os.path.join(OUT, "svg")

BG = "#13151b"      # dark tile (matches an unlit Stream Deck key)
SEP = "#3b3b46"     # discreet diagonal separator

# Per-instrument natural centre + scale — the sources are not all centred the
# same way (a grand piano sits lower-right of its viewBox, a trumpet is wide).
# cx,cy = the drawing point placed on the quadrant target; s = scale in-quadrant.
# Instruments absent here fall back to DEFAULT_ANCHOR; add an entry to fine-tune.
DEFAULT_ANCHOR = (72, 72, 0.50)
ANCHOR = {
    "piano-grand":     (74, 77, 0.50),
    "piano-upright":   (72, 74, 0.50),
    "ep-rhodes":       (72, 72, 0.50),
    "ep-wurlitzer":    (72, 72, 0.50),
    "organ-tonewheel": (72, 72, 0.50),
    "trumpet":         (72, 72, 0.46),
    "saxophone":       (60, 68, 0.50),
    "french-horn":     (70, 73, 0.48),
    "trombone":        (72, 72, 0.46),
    "brass-section":   (72, 72, 0.48),
    "vibanet":         (72, 68, 0.50),
    "bass-flute":      (72, 76, 0.47),
    "woodwinds-section": (74, 66, 0.48),
    "synth-saw":       (72, 70, 0.48),
    "synth-square":    (72, 70, 0.48),
    "synth-talkbox":   (72, 70, 0.48),
    "synth-glide":     (72, 70, 0.48),
    "synth-resonator": (72, 70, 0.48),
    "synth-sweep":     (72, 69, 0.48),
    "choir":           (72, 80, 0.47),
    "synth-pad":       (72, 70, 0.48),
    "harpsichord":     (74, 76, 0.50),
    "vibraphone":      (72, 82, 0.46),
    "harp":            (74, 74, 0.50),
    "double-bass":     (72, 74, 0.46),
    "bass-electric":   (72, 72, 0.48),
    "synth-bass":      (72, 70, 0.48),
    "synth-lead":      (72, 70, 0.48),
    "synth-brass":     (72, 70, 0.48),
}

TARGET_BL = (48, 98)   # lower-left  quadrant centre (instrument A)
TARGET_TR = (98, 46)   # upper-right quadrant centre (instrument B)


def inner(name):
    """Return the inner markup of a pack source SVG (its <svg> wrapper stripped)."""
    path = os.path.join(KIT, f"{name}.svg")
    if not os.path.exists(path):
        sys.exit(f"gen_duo: no such instrument source: src/{name}.svg")
    with open(path) as f:
        s = f.read()
    s = re.sub(r"^.*?<svg[^>]*>", "", s, count=1, flags=re.S)   # drop opening <svg ...>
    s = re.sub(r"</svg>\s*$", "", s, flags=re.S)                # drop closing </svg>
    return s.strip()


def place(name, target):
    tx, ty = target
    cx, cy, s = ANCHOR.get(name, DEFAULT_ANCHOR)
    return f'<g transform="translate({tx},{ty}) scale({s}) translate({-cx},{-cy})">{inner(name)}</g>'


def duo_svg(a, b):
    """a = lower-left ↙, b = upper-right ↗."""
    sep = f'<path d="M14,20 L128,128" stroke="{SEP}" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>'
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="0 0 144 144">'
        f'<rect width="144" height="144" rx="22" fill="{BG}"/>{sep}'
        f"{place(b, TARGET_TR)}{place(a, TARGET_BL)}</svg>"
    )


def build(a, b, name):
    os.makedirs(SVGOUT, exist_ok=True)
    sp = os.path.join(SVGOUT, f"{name}.svg")
    with open(sp, "w") as f:
        f.write(duo_svg(a, b))
    subprocess.run(
        ["rsvg-convert", "-w", "144", "-h", "144", sp, "-o", os.path.join(OUT, f"{name}.png")],
        check=True,
    )
    return name


# Default combo set — piano paired with each brass voice. The upright piano has a
# visible wood body, so it reads on the dark tile where the near-black grand does
# not. Edit freely; any two src/ basenames compose.
DEFAULT_PAIRS = [
    ("piano-upright", "trumpet",      "piano+trumpet"),
    ("piano-upright", "saxophone",    "piano+sax"),
    ("piano-upright", "french-horn",  "piano+frenchhorn"),
    ("piano-upright", "brass-section", "piano+brasssection"),
]


# Live-rig matrix — Benoît's two sound-select rows, bottom (Track 1 keyboards) x
# top (Track 2 leads). A split key = a Track-1 voice layered under a Track-2 lead.
# (label, kit source). Labels come from the deck; sources from src/. Output name
# is "<t1>__<t2>" so the two "strings" (keyboard pad vs SWAM) never collide.
TRACK1 = [
    ("piano", "piano-upright"), ("clav", "clavinet"), ("vibanet", "vibanet"),
    ("wurli", "ep-wurlitzer"), ("rhodes", "ep-rhodes"),
    ("organ", "organ-tonewheel"), ("strings", "strings-section"),
]
TRACK2 = [
    ("strings", "strings-section"), ("violin", "violin"), ("viola", "viola"), ("cello", "cello"),
    ("woodwinds", "woodwinds-section"), ("piccolo", "piccolo"), ("flute", "flute"), ("bassflute", "bass-flute"),
    ("brass", "brass-section"), ("trumpet", "trumpet"), ("sax", "saxophone"), ("trombone", "trombone"),
    ("sub37hs", "synth-saw"), ("sub37vint", "synth-square"), ("leadtb", "synth-talkbox"),
    ("portahorn", "synth-glide"), ("resonator", "synth-resonator"), ("gx1", "synth-sweep"),
]


def build_matrix():
    n = 0
    for t1, a in TRACK1:
        for t2, b in TRACK2:
            build(a, b, f"{t1}__{t2}")
            n += 1
    print(f"OK live-rig matrix: {n} split buttons ({len(TRACK1)}x{len(TRACK2)}) -> duo/")


# Classic Dual/Layer & Split presets that mainstream consumer digital pianos
# (Yamaha P/Clavinova, Roland FP, Casio Privia, Korg) ship as factory combos.
# LAYER: a foundation keyboard (↙) under a colour voice (↗). SPLIT: a bass in the
# left hand (↙) under the right-hand voice (↗). (source_bottom, source_top, name).
PRESETS = [
    # --- Dual / Layer ---
    ("piano-upright", "strings-section", "layer_piano-strings"),   # the classic
    ("piano-upright", "choir",           "layer_piano-choir"),
    ("piano-upright", "synth-pad",       "layer_piano-pad"),
    ("piano-upright", "ep-rhodes",       "layer_piano-epiano"),
    ("ep-rhodes",     "strings-section", "layer_epiano-strings"),
    ("harpsichord",   "strings-section", "layer_harpsi-strings"),
    ("piano-upright", "vibraphone",      "layer_piano-vibes"),
    ("piano-upright", "harp",            "layer_piano-harp"),
    ("organ-tonewheel", "strings-section", "layer_organ-strings"),
    ("strings-section", "choir",         "layer_strings-choir"),
    ("strings-section", "brass-section", "layer_strings-brass"),   # orchestra
    # --- Split (left-hand bass) ---
    ("double-bass",   "piano-upright",   "split_acbass-piano"),    # jazz split
    ("bass-electric", "ep-rhodes",       "split_bass-epiano"),
    ("bass-electric", "organ-tonewheel", "split_bass-organ"),
    # --- Consumer-synth Dual/Split (Roland Juno/FA, Yamaha PSR/MODX, Korg,
    #     Casio CT-X) — the layer/split performances those manuals ship as
    #     factory combis. Split voice = a bass in the left hand, per the manuals. ---
    ("synth-saw",   "synth-pad",       "layer_lead-pad"),          # solo lead over a pad
    ("synth-saw",   "synth-square",    "layer_saw-square"),        # detuned dual lead
    ("synth-brass", "synth-saw",       "layer_synthbrass-lead"),   # fat brass lead
    ("strings-section", "synth-pad",   "layer_strings-pad"),       # lush pad
    ("synth-bass",  "synth-saw",       "split_synthbass-lead"),    # EDM/dance split
    ("bass-electric", "synth-saw",     "split_bass-lead"),         # bass under a lead
    ("synth-bass",  "piano-upright",   "split_synthbass-piano"),   # synth bass + piano
]


def build_presets():
    for a, b, name in PRESETS:
        build(a, b, name)
    print(f"OK classic piano presets: {len(PRESETS)} split buttons -> duo/")


def main(argv):
    if argv and argv[0] == "--matrix":
        build_matrix()
        return
    if argv and argv[0] == "--presets":
        build_presets()
        return
    if len(argv) >= 2:
        a, b = argv[0], argv[1]
        name = argv[2] if len(argv) >= 3 else f"{a}+{b}"
        build(a, b, name)
        print(f"OK split button: duo/{name}.png")
        return
    n = sum(1 for _ in (build(a, b, name) for a, b, name in DEFAULT_PAIRS))
    print(f"OK split buttons: {n} PNG -> duo/")


if __name__ == "__main__":
    main(sys.argv[1:])
