# TASKS — streamdeck-stage-keys

## v1.0 (static, 83 icons) — SUBMITTED, pending Elgato review
- ☐ Wait for review outcome of version 1 (maker.elgato.com → product → Versions)

## v1.1 (animated, 166 icons) — PREPARED, blocked on v1.0 review
Every instrument now ships a static icon + an animated "(playing)" variant
(the active state). Built, validated (166 icons ✓), packaged, animated gallery
generated. **Cannot submit yet**: Maker Console disables "Create version" while
v1.0 is Pending review.
- ☐ Once v1.0 is approved/rejected: product → Versions → Create version 1.1.0
  - upload dist/com.beennnn.stagekeys.streamDeckIconPack (166 icons)
  - Media: add gallery-animated.mp4 (from bin/maker-media.sh → maker-media/)
  - Release notes: "Animated icons — each instrument now has an animated
    '(playing)' variant for the active state (Stream Deck state 1, via a MIDI
    plugin's feedback). 166 icons total."

## v1.2 (92 base icons + split buttons) — AUTHORED, not yet built/submitted
9 new full-colour base icons added to `src/` (pack 83 → 92): `vibanet`,
`bass-flute`, `woodwinds-section`, `synth-{saw,square,talkbox,glide,resonator,
sweep}`. Tagged in `tags.json`. Plus `bin/gen_duo.py` (split-view combo
generator: `--matrix` live-rig 126, `--presets` 13 classic consumer-piano
Dual/Split). Committed locally (3 commits), NOT pushed, NOT built.
- ☐ Animated `-playing` variants for the 9 new icons → parity (currently 92
  static vs 83 animated). Via `bin/build-animated.py` (design motion per icon).
- ☐ Rebuild pack: `bin/build.sh` → regenerates `icons/`, `icons.json`, `dist/`
  with the 92 icons (currently pre-existing uncommitted `dist/`+`icons.json`
  changes sit in the tree — reconcile before building).
- ☐ Bump `manifest.json` Version (→ 1.2.0) + move CHANGELOG `[Unreleased]`
  → `[1.2.0]` with date.
- ☐ Regenerate listing media with the new icons: `bin/maker-media.sh`.
- ☐ Push GitHub `Beennnn/streamdeck-stage-keys` (3 local commits).
- ☐ Submit via Maker Console once v1.0/v1.1 ordering is resolved (v1.1 is
  blocked on v1.0 review — decide whether 1.2 supersedes or stacks after 1.1).
- 🤔 Decide: ship the split buttons (`duo/`) in the Marketplace pack too (e.g. a
  "Layers & Splits" set from `--presets`), or keep `duo/` as personal-rig only?

## Build
- `bin/build.sh` → static+animated pack · `bin/build-animated.py` → animated variants + showcase · `bin/maker-media.sh` → listing media incl. gallery-animated.mp4. All via the sdicons toolkit.
