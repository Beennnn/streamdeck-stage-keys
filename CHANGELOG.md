# Changelog

All notable changes to **Music Instruments for Stage Keys**. Format based on
[Keep a Changelog](https://keepachangelog.com/); versions follow the pack's
`manifest.json` Version.

## [Unreleased]
### Added
- **9 new base icons** (pack now **92 static**): `vibanet`, `bass-flute`,
  `woodwinds-section`, and six voiced synth-lead variants — `synth-saw`,
  `synth-square`, `synth-talkbox`, `synth-glide`, `synth-resonator`,
  `synth-sweep` — for live-rig voices GM has no program for. Names + tags in
  `tags.json`. (Animated `-playing` variants for these are still pending.)
- **Split-view combo buttons** — `bin/gen_duo.py` composes two of the pack's
  full-colour instrument sources onto one 144 × 144 key, divided diagonally
  (A lower-left ↙, B upper-right ↗) over a dark tile. For keys that layer or
  morph two sounds (piano + brass, Rhodes + sax…). Any two `src/` instruments
  compose; default set + per-instrument `ANCHOR` tuning. Output in `duo/`.
- **`bin/gen_duo.py --matrix`** — builds the full two-row live-rig set
  (Track 1 keyboards × Track 2 leads = 126 split buttons). `TRACK1`/`TRACK2`
  tables in the script map a deck to kit sources.
- **`bin/gen_duo.py --presets`** — 21 Dual/Layer & Split combos that mainstream
  consumer keyboards ship as factory performances, pianos **and synths**
  (Yamaha PSR/MODX, Roland Juno/FA, Casio CT-X, Korg). Piano-side (Piano +
  Strings/Choir/Pad, E.Piano + Strings, Harpsichord + Strings, Strings + Brass,
  left-hand-bass splits) + synth-side (Lead + Pad, detuned Saw + Square, Synth-
  Brass + Lead, Strings + Pad, Synth-Bass / Lead EDM split, Bass / Lead).
  `PRESETS` table in the script.

## [1.1.0] — 2026-07-14
### Added
- **Animated "(playing)" variant for every instrument** — the *active state*.
  On a Stream Deck, wire state 0 = the static icon (idle) and state 1 = the
  animated one (playing), driven by a MIDI plugin's state feedback. The pack now
  ships **166 icons** (83 static + 83 animated, looping 144×144 WEBP,
  transparent, ~12 fps).
- Motion inspired by **how the instrument is played**: struck instruments
  bounce, held winds sway, plucked strings wobble, the accordion's bellows
  stretch, a cymbal spins; synths, vocoder, drum machine and mellotron get
  bespoke internal motion (scrolling waveforms, dancing bars, chasing LEDs,
  spinning reels).
- Animated Marketplace gallery (`gallery-animated.mp4`).
- `bin/build-animated.py` + `bin/maker-media.sh --animated` (via the sdicons
  toolkit) to regenerate the animated variants, showcase and listing media.

## [1.0.0] — 2026-07-14
### Added
- Initial release — **83 full-colour instrument icons** covering the complete
  **General MIDI / XP** sound set (128 programs, 16 families) plus modern synth
  categories (synthesizer, drum kit, drum machine, sampler/MPC, arpeggio,
  mellotron, vocoder).
- [`GM-MAP.md`](GM-MAP.md): program-number → icon table (doubles as an XP patch
  guide), so each Stream Deck key can both show and select a patch.
- MIDI-plugin pairing docs (free *Midi Button* by Tom Kelly, or Trevligaspel's
  *MIDI*) to send Program Change from a key.
- Published on the [Elgato Marketplace](https://marketplace.elgato.com/product/music-instruments-for-stage-keys-f4ce84f5-2eda-4431-9a36-d847e5094fa9) (**CC-BY-4.0**).
