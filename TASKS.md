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

## v1.2 (226 icons: 92 instruments + 21 combos, static+animated) — BUILT, pending submit
ONE pack (no split — size is a non-issue: Elgato has no pack cap, only ≤1 MB/
icon; ours ~4 MB). 9 new generic-use instruments (vibanet, bass-flute,
woodwinds-section, 6 voiced synth leads) + 21 generic Dual/Split combos IN the
pack, all static + animated. `manifest` 1.2.0, `validate` clean, `dist/` +
media rebuilt. The 126-combo live-rig matrix (`duo/*__*`) stays LOCAL, unpublished.
- ☐ Push GitHub `Beennnn/streamdeck-stage-keys` (local commits ahead).
- ☐ Submit via Maker Console — BLOCKED: "Create version" is disabled while a
  prior version is *Pending review*. Check v1.0/v1.1 status first; 1.2 supersedes
  1.1 (1.1 was never submitted), so submit 1.2 once v1.0 clears review.
  - Product → Versions → Create version **1.2.0**
  - Upload `dist/com.beennnn.stagekeys.streamDeckIconPack` (226 icons)
  - Media from `maker-media/`: thumbnail-1920x960 + 5 previews + gallery
    (incl. gallery-animated.mp4). AI-content disclosure = YES.
  - Release notes: see the v1.2 block in this session / README-side draft.

## Build
- `bin/build.sh` → static+animated pack · `bin/build-animated.py` → animated variants + showcase · `bin/maker-media.sh` → listing media incl. gallery-animated.mp4. All via the sdicons toolkit.
