# Guidance Checklist

Use this checklist before giving concrete settings.

## Version Gate

- Load saved Cubase version/edition from `wiki/user-defaults.md`. Saved default is Cubase 13.
- Do not repeatedly ask for version after it is saved. Ask only when the user changes context, a detected install conflicts with the saved config, or the answer depends on unknown edition-specific availability.
- When local setup matters, run `scripts/detect_cubase.py` and compare installed apps/tools with the saved config.
- If guidance depends on a feature introduced after the saved version, do not recommend it unless the user confirms a newer version.
- If the edition matters, ask whether the user has Pro, Artist, Elements, AI, or LE.
- Prefer official Steinberg docs for UI paths, feature names, and version changes.

## Context Questions

Ask only the questions needed for the next useful step:

- Goal: recording, editing, mix repair, mastering, export, latency, MIDI, routing, or sound design?
- Source: vocal/instrument, number of mics, audio interface, room, background noise.
- Monitoring: headphones/speakers, loudness, untreated room, reference tracks.
- Constraints: missing plug-ins, no acoustic treatment, no pop filter, shared room, time pressure.

## Recommendation Shape

- Start with the smallest reversible change.
- Give numbered steps using verified Cubase UI terms.
- Explain what to listen for in plain language.
- Provide safe starting ranges only when useful, and label them as starting points, not rules.
- Separate capture fixes from mix fixes.

## Carnatic Checks

- Protect sruti and gamaka integrity.
- Avoid hard tuning, hard quantization, and aggressive transient shaping unless requested.
- For vocals, prioritize breath/noise control, sahitya clarity, and resonant harshness management.
- For melodic instruments, preserve sustain, bow/pluck articulation, and pitch movement.
- For mridangam/percussion, preserve attack, low resonance, and natural room cues.
