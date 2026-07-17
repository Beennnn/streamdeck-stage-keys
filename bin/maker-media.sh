#!/bin/sh
# Regenerate the Elgato Maker Console upload assets for this pack
# (thumbnail 1920x960, 5 icon previews 144x144, gallery >=3 at 1920x960).
# Output → maker-media/ (gitignored). Uses the sdicons toolkit.
# See the sdicons publishing docs for how to use them in the submission wizard.
set -e
ROOT="$(git rev-parse --show-toplevel)"
SD="${SDICONS:-$ROOT/../streamdeck-toolkit/bin/sdicons}"
command -v sdicons >/dev/null 2>&1 && SD="sdicons"
"$SD" maker-media "$ROOT" --out-dir "$ROOT/maker-media" \
  --subtitle "92 full-colour instruments + split Layer/Split combos · GM/XP + modern synths" \
  --previews ep-rhodes,saxophone,drum-machine,synth-saw,layer_piano-strings \
  --animated "$ROOT/animated/icons"   # → gallery-animated.mp4 for the listing
