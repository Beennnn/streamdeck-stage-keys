#!/bin/sh
# Rebuild the Stage Keys pack from src/ using the sdicons toolkit.
#
# sdicons is the generic Stream Deck icon-pack toolkit:
#   https://github.com/Beennnn/streamdeck-toolkit
# This repo commits its built outputs (icons/, icons.json, dist/*), so building
# is only needed after editing SVGs in src/ or metadata in tags.json/manifest.json.
#
# Resolution order for the toolkit entrypoint:
#   1. $SDICONS env var (path to bin/sdicons)
#   2. `sdicons` on PATH
#   3. ../streamdeck-toolkit/bin/sdicons (toolkit cloned as a sibling)
set -e
ROOT="$(git rev-parse --show-toplevel)"

if [ -n "$SDICONS" ]; then
  SD="$SDICONS"
elif command -v sdicons >/dev/null 2>&1; then
  SD="sdicons"
elif [ -x "$ROOT/../streamdeck-toolkit/bin/sdicons" ]; then
  SD="$ROOT/../streamdeck-toolkit/bin/sdicons"
else
  echo "sdicons not found. Clone the toolkit next to this repo:" >&2
  echo "  git clone https://github.com/Beennnn/streamdeck-toolkit ../streamdeck-toolkit" >&2
  echo "or set SDICONS=/path/to/bin/sdicons" >&2
  exit 1
fi

# The repo root IS the pack folder (manifest.json + icons/ + icons.json here).
# --id sets the reverse-domain pack identity (the <id>.sdIconPack/ wrapper).
"$SD" build "$ROOT/src" "$ROOT" --out-dir "$ROOT/dist" --id com.beennnn.stagekeys
echo "Built dist/com.beennnn.stagekeys.streamDeckIconPack — submit-ready"
echo "(double-click to install, or upload to console.elgato.com)."
