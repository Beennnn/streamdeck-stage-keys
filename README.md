# Music Instruments for Stage Keys

> A Stream Deck icon pack for the live keyboardist (short name: **Stage Keys**).

**Full-colour sound-select icons for the live keyboardist.** One Stream Deck
key per voice, covering the complete **General MIDI / XP** sound set (all 128
programs, 16 families) **plus the modern synth categories** best-selling synths
expose that GM has no program for. Recognise the sound at a glance under stage
lighting — no menu-diving, no patch numbers.

![Stage Keys palette](preview.png)

## Why a keyboardist needs this

A keyboard player rarely holds a single sound through a whole song. The verse
is on a **Rhodes**, the chorus opens up on a **synth pad**, the bridge moves to
**strings**, the solo jumps to **organ**, the intro was **acoustic piano**. In
the studio there's time; **live, the change has to land exactly on the beat,
without looking away from the keys**.

This pack turns a Stream Deck into a dedicated **sound selector** beside the
keyboard:

- **One physical key = one voice.** No scrolling through programs, no aiming at
  a tiny screen mid-phrase.
- **Read the sound by shape + colour, not text.** Under low light and stress you
  recognise an object (an organ, a sax, the red Rhodes rail) far faster than an
  abstract colour code or a patch name — which is why these are full-colour
  illustrations, not monochrome silhouettes.
- **See the sound before you press it.** No landing on the wrong program at the
  wrong moment.

## What's inside (83 icons)

Organised around the **General MIDI (GM 1) sound map** — the same 16 banks a
Roland XP / SC / GS and any GM workstation expose — so it doubles as an XP patch
→ icon guide. 76 icons give every one of the 128 GM programs a dedicated icon
(only same-instrument variations reuse a drawing), plus **7 modern synth
categories**. Full program-by-program table: **[GM-MAP.md](GM-MAP.md)**.

- **Piano** — grand, upright, Rhodes, Wurlitzer, FM/DX, clavinet, harpsichord
- **Chromatic percussion** — celesta, glockenspiel, music box, vibraphone,
  marimba, xylophone, tubular bells, dulcimer
- **Organ** — drawbar, combo/rock, church/pipe, accordion, harmonica
- **Guitar / bass** — acoustic & electric guitar, electric & double bass
- **Strings** — violin, viola, cello, ensemble, harp, timpani
- **Ensemble** — choir/voice, orchestra hit
- **Brass** — trumpet, trombone, tuba, french horn, brass section
- **Reed / pipe** — saxophone, oboe, english horn, bassoon, clarinet, piccolo,
  flute, recorder, pan flute, blown bottle, shakuhachi, whistle, ocarina
- **Synth** — lead, pad, brass, bass, FX
- **Ethnic / percussive** — sitar, banjo, shamisen, koto, kalimba, bagpipe,
  tinkle bell, agogo, steel drums, woodblock, taiko, melodic tom, synth drum,
  reverse cymbal
- **Sound effects** — breath, seashore, bird tweet, telephone, helicopter,
  applause, gunshot
- **Beyond GM (modern synth categories)** — synthesizer, drum kit, drum
  machine, sampler/MPC, arpeggio/seq, mellotron, vocoder

## Install

Download **[`dist/com.beennnn.stagekeys.streamDeckIconPack`](dist/)** and
double-click it — the pack installs into Stream Deck's Icon Library, with
per-icon names and searchable tags.

## Rebuild from source

Icons are authored as parametric SVGs in [`src/`](src/) and rendered to
144 × 144 PNG. Built with **[sdicons](https://github.com/Beennnn/stream-deck-icons)**
(the generic Stream Deck icon-pack toolkit):

```sh
# with the sdicons toolkit cloned alongside this repo:
bin/build.sh
# → regenerates icons/, icons.json and a submit-ready
#   dist/com.beennnn.stagekeys.streamDeckIconPack
```

Names and tags come from [`tags.json`](tags.json); pack metadata is in
[`manifest.json`](manifest.json).

## Publishing to the Elgato Marketplace

`bin/build.sh` produces a **submit-ready** `.streamDeckIconPack` (the correct
`com.beennnn.stagekeys.sdIconPack/` container) — double-click to install, or
upload straight to the **[Maker Console](https://maker.elgato.com/)** after
review. Elgato's [Icon Pack Man](https://iconpackman.elgato.com/) web tool is
*optional* (and drops icon names/tags on import — `sdicons repair` fixes its
exports). The Marketplace listing media (thumbnail, icon previews, gallery) is
generated at the console's exact dimensions by `bin/maker-media.sh`
(→ `maker-media/`, gitignored). Full process: [sdicons publishing docs](https://github.com/Beennnn/stream-deck-icons/blob/main/docs/publishing.md).

## License

Icons: **CC-BY-4.0** (see [LICENSE](LICENSE)) — free to use with attribution.
