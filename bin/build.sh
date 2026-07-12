#!/bin/sh
# Rebuild the Stage Keys pack from src/ using the sdicons toolkit.
#
# sdicons is the generic Stream Deck icon-pack toolkit:
#   https://github.com/Beennnn/stream-deck-icons
# This repo commits its built outputs (icons/, icons.json, dist/*), so building
# is only needed after editing SVGs in src/ or metadata in tags.json/manifest.json.
#
# Resolution order for the toolkit entrypoint:
#   1. $SDICONS env var (path to bin/sdicons)
#   2. `sdicons` on PATH
#   3. ../stream-deck-icons/bin/sdicons (toolkit cloned as a sibling)
set -e
ROOT="$(git rev-parse --show-toplevel)"

if [ -n "$SDICONS" ]; then
  SD="$SDICONS"
elif command -v sdicons >/dev/null 2>&1; then
  SD="sdicons"
elif [ -x "$ROOT/../stream-deck-icons/bin/sdicons" ]; then
  SD="$ROOT/../stream-deck-icons/bin/sdicons"
else
  echo "sdicons not found. Clone the toolkit next to this repo:" >&2
  echo "  git clone https://github.com/Beennnn/stream-deck-icons ../stream-deck-icons" >&2
  echo "or set SDICONS=/path/to/bin/sdicons" >&2
  exit 1
fi

# The repo root IS the pack folder (manifest.json + icons/ + icons.json here).
"$SD" build "$ROOT/src" "$ROOT" --out-dir "$ROOT/dist"
echo "Built. Point Icon Pack Man at this folder, or install dist/*.streamDeckIconPack."
