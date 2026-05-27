---
name: cubase-carnatic-engineering
description: Version-aware Cubase guidance for recording, editing, mixing, mastering, sound engineering, room-constrained production, and Carnatic music workflows. Use when the user asks about Cubase setup, UI, preferences, audio/MIDI routing, VST instruments, plug-ins, mixing, mastering, recording vocals or instruments, Carnatic production, or troubleshooting sound quality.
---

# Cubase Carnatic Engineering

## Operating Rule

Use the local wiki at `/Users/rangaprakash/.codex/knowledge/cubase-carnatic` as the persistent knowledge base. Treat it as a maintained wiki, not a one-off notes folder.

Before giving actionable settings, load saved defaults from `wiki/user-defaults.md`. Treat the saved Cubase version as configuration, not a question to repeat every time.

- Cubase version and edition. Default saved version: Cubase 13. Use this unless the user changes it, the local install check contradicts it, or the current request explicitly involves another version.
- Operating system, audio interface, microphone or instrument input path, monitoring chain, and available plug-ins.
- Room condition: treated/untreated, noise sources, recording distance, and whether loud monitoring is possible.
- Musical context: Carnatic vocal, violin, veena, mridangam, morsing, flute, tanpura, hybrid production, speech, or other material.

Never offer a setting, menu path, plug-in, or workflow as available until it is known to exist in the user's Cubase version/edition. If unsure, check official Steinberg documentation or the local wiki first. State uncertainty plainly when a detail is inferred.

When local environment matters, run `scripts/detect_cubase.py` before advising. Use it to find installed Cubase apps, Steinberg utilities, common VST folders, and basic audio/MIDI tool availability. If detection differs from saved config, mention the mismatch and ask before changing `wiki/user-defaults.md`.

## Answer Workflow

1. Read `/Users/rangaprakash/.codex/knowledge/cubase-carnatic/wiki/index.md` first.
2. Read `wiki/user-defaults.md` for saved version and preferences.
3. Search the wiki with `rg` for the topic, Cubase version, and instrument/mix context.
4. Run `scripts/detect_cubase.py` when installation, local plug-ins, audio setup, or tool availability could change the answer.
5. If the answer is version-sensitive or not covered locally, verify against official Steinberg documentation first. Use tutorial videos or community posts only as secondary practical evidence, never as the source of truth for feature availability.
6. Give simple step-by-step guidance. Prefer exact Cubase UI paths when verified for the configured version.
7. For non-ideal rooms, recommend capture-first fixes before mix fixes: mic placement, gain staging, noise control, monitoring level, and performance consistency.
8. If the question reveals new durable knowledge, update the wiki and append a log entry.

## Carnatic Priorities

Preserve performance identity before applying modern polish:

- Intonation, gamaka continuity, sahitya clarity, sruti stability, and tala feel matter more than loudness.
- Avoid aggressive pitch correction, time correction, de-essing, gating, or quantization unless the user explicitly wants a stylized result.
- For vocals and melodic instruments, protect microtonal movement and transients. Use narrow corrective EQ and gentle dynamics before broad processing.
- For percussion such as mridangam, preserve attack, bass resonance, and room realism. Avoid over-compression that flattens nadai and stroke articulation.
- For tanpura or sruti box, keep it stable, low-noise, and supportive; do not let it mask vocal fundamentals or important overtones.

## Knowledge Base Maintenance

Use the wiki pattern from the LLM Wiki idea:

- `raw/`: immutable source captures or notes from web docs, videos, PDFs, user observations, and session notes.
- `sources/`: source cards with URL, title, date accessed, Cubase version/edition, reliability, and summary.
- `wiki/`: maintained synthesis pages, concept pages, version pages, instrument pages, and workflows.
- `wiki/index.md`: catalog of pages and their scope.
- `wiki/log.md`: chronological record of ingests, queries, contradictions, and updates.

When ingesting a source:

1. Create or update a source card under `sources/`.
2. Update relevant wiki pages instead of dumping raw notes.
3. Note version and edition explicitly.
4. Record contradictions or version drift.
5. Append to `wiki/log.md` with `## [YYYY-MM-DD] type | title`.

## Reference Files

- Read `references/wiki-schema.md` before adding or reorganizing wiki pages.
- Read `references/guidance-checklist.md` before answering complex recording, mixing, mastering, or troubleshooting requests.
