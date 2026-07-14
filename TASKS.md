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

## Build
- `bin/build.sh` → static+animated pack · `bin/build-animated.py` → animated variants + showcase · `bin/maker-media.sh` → listing media incl. gallery-animated.mp4. All via the sdicons toolkit.
