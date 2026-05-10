# Examples

Curated hybrid Draw.io retro boards generated with `retro-board-creator`.

Each example uses the **hybrid** visual mode: a generated raster background provides the theme, scenery, and decorative diagnostics, while the retro structure (sticky notes, vote tokens, action cards) is laid down as editable Draw.io objects on top.

The `.drawio` source files live in the `sandbox/` workspace and are exported here as PNGs for quick preview.

## Inventory

| Theme | Sample prompt | Preview |
|-------|---------------|---------|
| Artemis II launch | "Make a hybrid Draw.io retro for our release sprint with an Artemis II launch theme. I feel lucky." | [artemis-ii-generated-background-retro.drawio.png](./artemis-ii-generated-background-retro.drawio.png) |
| Easter | "Spring-themed Easter retro, hybrid Draw.io, kudos column, mood check." | [easter-generated-background-retro.drawio.png](./easter-generated-background-retro.drawio.png) |
| Go-live celebration | "We just shipped — make a celebratory go-live retro board, hybrid Draw.io, kudos + lessons + next bets." | [go-live-celebration-generated-background-retro.drawio.png](./go-live-celebration-generated-background-retro.drawio.png) |
| Labubu | "Playful Labubu-themed retro for our team health check, hybrid Draw.io, mad/sad/glad + kudos." | [labubu-generated-background-retro.drawio.png](./labubu-generated-background-retro.drawio.png) |
| New pope | "Topical 'new pope' themed retro for our discovery sprint, hybrid Draw.io, puzzles + experiments." | [new-pope-generated-background-retro.drawio.png](./new-pope-generated-background-retro.drawio.png) |
| Summer starts | "Summer-kickoff retro board, hybrid Draw.io, light tone, energy meter." | [summer-starts-generated-background-retro.drawio.png](./summer-starts-generated-background-retro.drawio.png) |

## What These Demonstrate

- a single layout contract drives both the background prompt and the editable overlay coordinates
- post-its are real Draw.io objects, not painted into the background
- one post-it color per column, with a copy/paste pool in mixed colors
- theme-native diagnostic widgets (mood, energy, readiness) are rendered as decorative scenery in the background and overlaid with editable emoji/vote markers
- titles and column labels appear once — in the background — and are not duplicated as editable text
- bottom and side margins leave room for the copy/paste pool, vote tokens, and overflow widgets

## Reproducing an Example

The hybrid path is documented in [../references/output-recipes.md](../references/output-recipes.md). The general flow:

1. agree on a layout contract: page size, title zone, column header zones, note-safe rectangles, diagnostics zone, copy/paste pool zone
2. generate the background image with that contract baked into the prompt
3. drop editable Draw.io sticky notes, icons, and action cards onto the same coordinates
4. validate against the [SKILL.md](../SKILL.md) hybrid-board checklist
