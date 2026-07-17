# TASKS — streamdeck-stage-keys

## v1.2.1 — poster fix done, RESUBMIT to Maker Console (manual, Benoît only)
Elgato rejected 1.2 on 2026-07-17: *"the preview images of the GIFs aren't
loading, please ensure this icon pack is packaged correctly via iconpackman."*
Root cause: animated icons had no companion static poster the Icon Library
renders in the grid. FIXED — 113 `<base>-playing.png` posters generated,
manifest → 1.2.1, `dist/com.beennnn.stagekeys.streamDeckIconPack` rebuilt and
`sdicons verify` is green (0 errors). Guarded going forward by `sdicons verify`.

- ☐ Maker Console → Products → Music Instruments for Stage Keys → Versions →
  the Rejected 1.2 → **re-upload `dist/com.beennnn.stagekeys.streamDeckIconPack`**
  (now 1.2.1, carries the 113 posters) → resubmit for review.
- 🤔 Optional polish (not a rejection cause): 6 animations run below Elgato's
  suggested 10–20 fps (arpeggio ~2, drum-machine ~4, applause/gunshot/orchestra-
  hit/telephone ~7). Deliberate slow pulses — bump only if a reviewer flags it.

## Build
- `bin/build.sh` → static+animated pack · `bin/maker-media.sh` → listing media.
  Posters + container: `sdicons package` (auto-generates posters) or
  `sdicons posters .` then `sdicons verify .` before every resubmit.
