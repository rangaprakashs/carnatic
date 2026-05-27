# Wiki Schema

Root: `/Users/rangaprakash/.gemini/antigravity/knowledge/cubase-carnatic`

## Directories

- `raw/`: source captures and rough notes. Do not edit captured source text except to add metadata.
- `sources/`: one source card per source. Prefer filenames like `steinberg-cubase-13-operation-manual.md`.
- `wiki/`: maintained synthesis pages.

## Wiki Page Frontmatter

Use this shape for new wiki pages:

```yaml
---
title: Page Title
type: concept | workflow | instrument | version | source-synthesis | user-profile
versions: [Cubase 13]
editions: [Pro, Artist, Elements, AI, LE, unknown]
last_verified: YYYY-MM-DD
reliability: source-backed | user-observed | inferred | needs-verification
---
```

## Source Card Shape

```yaml
---
title: Source Title
url: https://example.com
source_type: official-docs | official-release-notes | video | forum | article | user-note
accessed: YYYY-MM-DD
versions: [Cubase 13]
editions: [Pro]
reliability: primary | secondary | anecdotal
---
```

Then include:

- Summary
- Version/edition claims
- UI paths or settings mentioned
- Contradictions or caveats
- Wiki pages updated

## Core Pages

- `wiki/index.md`: content catalog. Update on every ingest.
- `wiki/log.md`: append-only history.
- `wiki/user-defaults.md`: saved user defaults and preferences.
- `wiki/version-cubase-13.md`: Cubase 13 feature and UI notes.
- `wiki/carnatic-production-principles.md`: Carnatic-specific engineering priorities.
- `wiki/non-ideal-room-recording.md`: practical capture guidance for untreated rooms.
