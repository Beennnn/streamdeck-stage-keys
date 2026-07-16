# Changelog

All notable changes to **Music Instruments for Stage Keys**. Format based on
[Keep a Changelog](https://keepachangelog.com/); versions follow the pack's
`manifest.json` Version.

## [Unreleased]
### Added
- **Split-view combo buttons** — `bin/gen_duo.py` composes two of the pack's
  full-colour instrument sources onto one 144 × 144 key, divided diagonally
  (A lower-left ↙, B upper-right ↗) over a dark tile. For keys that layer or
  morph two sounds (piano + brass, Rhodes + sax…). Any two `src/` instruments
  compose; default set + per-instrument `ANCHOR` tuning. Output in `duo/`.

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
