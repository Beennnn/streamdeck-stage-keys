#!/bin/sh
# Regenerate the Elgato Maker Console upload assets for this pack
# (thumbnail 1920x960, 5 icon previews 144x144, gallery >=3 at 1920x960).
# Output → maker-media/ (gitignored). Uses the sdicons toolkit.
# See the sdicons publishing docs for how to use them in the submission wizard.
set -e
ROOT="$(git rev-parse --show-toplevel)"
SD="${SDICONS:-$ROOT/../stream-deck-icons/bin/sdicons}"
command -v sdicons >/dev/null 2>&1 && SD="sdicons"
"$SD" maker-media "$ROOT" --out-dir "$ROOT/maker-media" \
  --subtitle "83 full-colour icons · complete General MIDI / XP + modern synths" \
  --previews piano-grand,ep-rhodes,organ-tonewheel,saxophone,drum-machine \
  --animated "$ROOT/animated/icons"   # → gallery-animated.mp4 for the listing
