# TASKS — streamdeck-stage-keys

## Publish to the Elgato Marketplace
- ☐ Verify install: double-click dist/com.beennnn.stagekeys.streamDeckIconPack → "Music Instruments for Stage Keys" shows in Stream Deck with names + tags
- ☐ Submit through Maker Console (console.elgato.com) — CC-BY-4.0, 3 previews in previews/, follow branding guidelines. Needs Benoit's Elgato login.

## Optional polish
- 🤔 Per-icon polish if wanted: grand piano a touch dark; oboe/clarinet & violin/viola/cello read similar (expected within a family); gunshot vs orchestra-hit are both bursts
- 🤔 Extend further: mellotron variants, handpan, turntable/DJ

## Build
- `bin/build.sh` (needs the sdicons toolkit) → submit-ready .streamDeckIconPack.
  Icon Pack Man is NOT required. If you use it anyway, it drops names/tags on
  import — fix with `sdicons repair <export> --tags tags.json`.
