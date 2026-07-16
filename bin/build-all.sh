#!/bin/sh
# Full Stage Keys build: static + animated + combos, end to end.
#
# build.sh only does the static render. The animated variants live in
# animated/icons/ and must be merged INTO icons/ between render and meta —
# a step build.sh can't express (it renders+meta+packages in one shot). This
# script sequences the whole thing so the committed pack is reproducible:
#   render (static) → animate (instruments) → animate combos → merge → meta →
#   validate → package.
set -e
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

if [ -n "$SDICONS" ]; then SD="$SDICONS"
elif command -v sdicons >/dev/null 2>&1; then SD="sdicons"
elif [ -x "$ROOT/../stream-deck-icons/bin/sdicons" ]; then SD="$ROOT/../stream-deck-icons/bin/sdicons"
else echo "sdicons toolkit not found (clone github.com/Beennnn/stream-deck-icons alongside)"; exit 1; fi

echo "→ render (static, src/*.svg → icons/*.png)"
"$SD" render "$ROOT/src" "$ROOT"

echo "→ animate instruments (→ animated/icons/*.webp + showcase)"
python3 bin/build-animated.py

echo "→ animate combos (internal-motion split tiles)"
python3 bin/build-combos-animated.py

echo "→ merge animated webp into icons/ as <slug>-playing.webp"
# Convention: static = <slug>.png, animated (active state) = <slug>-playing.webp.
# Wipe old animated first so a removed source can't leave a stale -playing file.
rm -f icons/*-playing.webp
for f in animated/icons/*.webp; do
  cp "$f" "icons/$(basename "$f" .webp)-playing.webp"
done

echo "→ meta (icons.json, static + animated)"
"$SD" meta "$ROOT"

echo "→ validate"
"$SD" validate "$ROOT"

echo "→ package (dist/com.beennnn.stagekeys.streamDeckIconPack)"
"$SD" package "$ROOT" --out-dir "$ROOT/dist" --id com.beennnn.stagekeys

echo "✓ done — $(ls icons/*.png 2>/dev/null | wc -l | tr -d ' ') static + $(ls icons/*.webp 2>/dev/null | wc -l | tr -d ' ') animated icons"
