---
name: retro-board-creator
description: Use when creating fun, visually engaging agile or scrum retrospective boards in Mermaid, Draw.io, PNG/SVG, Microsoft Whiteboard guidance, or similar formats, and when interpreting completed retro boards from photos, screenshots, Mermaid, Draw.io, or text to produce summaries, action items, follow-up notes, Jira/Confluence-ready output, or facilitation artifacts.
---

# Retro Board Creator

## 1. Choose the Workflow

1. Use **Board Creation** when the user wants a new retrospective board, template, theme, visual, diagram, whiteboard, Mermaid file, Draw.io board, PNG, or facilitation pack.
2. Use **Post-Retro Interpretation** when the user provides a completed board, photo, screenshot, export, Mermaid, Draw.io XML, or sticky-note text and asks for a summary, follow-up, todos, Jira items, Confluence notes, or insights.
3. Use both workflows when the user wants to prepare a board and define the expected summary/action-item output before the session.

## 2. Intake the Request

1. Identify the retrospective context:
   - team, sprint, project, release, incident, or milestone
   - session duration
   - remote, in-person, hybrid, or async mode
   - audience size and facilitation constraints
2. Identify the requested output:
   - `drawio`
   - `mermaid`
   - `png`
   - `svg`
   - `microsoft-whiteboard`
   - `text`
   - `confluence`
   - `jira`
   - another explicit format
3. Identify the visual mode:
   - Ask whether the board should be `editable vector`, `generated real/raster images`, or `hybrid` when the user has not already made this clear.
   - Use `editable vector` for Draw.io, Mermaid, SVG, and whiteboard layouts where later editing matters most.
   - Use `generated real/raster images` for polished PNG/JPG boards, moodboards, hero illustrations, and visually immersive retro templates.
   - Use `hybrid` when the user wants both: generate rich visual direction or background art, then create an editable board with large sticky-note areas and reusable widgets.
   - Skip this question only when the user says `I feel lucky`, explicitly asks for a specific format, or asks the agent to decide.
4. Identify the theme:
   - Use the user's theme when provided.
   - If the user asks for suggestions, propose 3 concise themes.
   - If the user says `I feel lucky`, choose the theme, layout, sections, and output format without asking for approval.
5. Identify sections to include or exclude:
   - sentiment check
   - went well
   - did not go well
   - ideas or experiments
   - action items
   - start / stop / continue
   - mad / sad / glad
   - kudos
   - puzzles or questions
   - metrics or facts
   - dot voting
   - grouping or clustering
   - previous action review
6. Ask how many post-its or content cards should fit per column when creating a team-ready board.
   - Default to 10 per column only when the user says `I feel lucky`, asks the agent to decide, or previously gave a capacity.
   - Use the answer to size columns, sticky-note grids, and copy/paste pools.
7. Ask at most 3 questions when required information is missing and the user did not grant autonomy.
8. Skip questions when the user requests speed, says `I feel lucky`, or provides enough constraints to infer safely.

## 3. Create a New Board

1. Read [references/board-patterns.md](references/board-patterns.md) when selecting sections, themes, facilitation elements, or anti-pattern checks.
2. Read [references/output-recipes.md](references/output-recipes.md) when producing Mermaid, Draw.io, PNG/SVG, or Microsoft Whiteboard output.
3. Select a compact retro structure:
   - Default to `Sentiment Check`, `Went Well`, `Did Not Go Well`, `Ideas`, and `Action Items`.
   - Use `Start / Stop / Continue` for behavior/process retros.
   - Use `Mad / Sad / Glad` for emotional safety and team health.
   - Use `Kudos` when morale, recognition, or celebration matters.
   - Use `Puzzles / Questions` when ambiguity, discovery, or dependencies are central.
4. Make the board visually engaging unless the user asks for a plain or serious board.
5. Keep the theme supportive of the work:
   - Use themed labels, section names, icons, colors, and small visual props.
   - Use immersive scene composition, textured surfaces, illustrated props, or generated raster artwork for showcase boards.
   - Select only the sentiment or diagnostic widgets that fit the session; do not include mood, confidence, energy, and risk together by default.
   - Rename diagnostic widgets to match the theme and facilitation purpose instead of using generic words when a themed label is clearer.
   - Create the board itself, not a screenshot of a hosting tool.
   - Do not simulate app menus, browser chrome, sidebars, toolbar buttons, or product navigation unless the user explicitly asks for an in-tool screenshot or UI mockup.
   - Preserve readability and facilitation clarity.
   - Avoid decorative clutter.
6. Include facilitation elements:
   - session goal
   - one or two theme-native diagnostic widgets when useful, such as mood, confidence, energy, risk, readiness, clarity, alignment, or celebration
   - theme-specific names and imagery for diagnostics instead of generic labels; for example `Launch Readiness`, `Heat Index`, `Smoke Signal`, `Toy Shelf Mood`, or `Service Pulse`
   - timeboxes
   - sticky-note color legend
   - dot-voting instructions
   - grouping area
   - action-item owner and due-date fields
   - previous action review when relevant
   - enough empty writing space for at least 10 sticky notes per active column unless the user asks for a compact board
7. For editable board outputs, add a copy/paste pool:
   - blank sticky notes in multiple colors
   - dot-voting markers
   - labels
   - arrows
   - small mood or energy markers
   - icons, emoji markers, meter widgets, and theme props
   - action-item cards
8. For Draw.io hybrid boards with generated image backgrounds:
   - Define a layout contract before generating the background: page size, title zone, column header zones, note-safe rectangles, diagnostics zone, and copy/paste pool zone.
   - Use the same layout contract for the image prompt and the Draw.io overlay coordinates.
   - Use the generated image as background artwork, theme, column scenery, and optionally column titles.
   - Keep static visual widgets in the background when they are decorative or read-only, such as confidence gauges, energy meters, risk heat meters, or empty mood-board helmets.
   - Do not bake post-its into the background image.
   - Do not bake the icon palette into the background image.
   - Create post-its as editable Draw.io note objects in different colors.
   - Prefer one post-it color per column unless the user asks for mixed colors.
   - Create icons, emoji, emoticons, and Unicode markers as editable/copyable Draw.io text objects.
   - Place real Unicode emoji markers over static mood-board slots when the background contains mood helmets or cards; do not use ASCII-only labels such as `:)`, `:/`, or `:D` unless the user explicitly asks for text emoticons.
   - Do not repeat titles, section labels, or helper labels as editable text when they are already visible in the background.
   - Add foreground text only when it provides new editable content, such as sticky-note labels, owner fields, due dates, or reusable action-card fields.
   - Leave enough bottom or side space in the background composition for editable copy/paste pools, icon palettes, vote tokens, and overflow widgets.
   - Keep every editable note fully inside a note-safe rectangle; do not overlap column headers, diagnostic widgets, decorative borders, or the copy/paste pool.
9. For `drawio`, generate `.drawio` XML manually or run:

   ```bash
   python scripts/generate_drawio_retro.py --title "Sprint Retro" --theme "Space Mission" --columns "Went Well|Did Not Go Well|Ideas|Action Items" --output retro.drawio
   ```

10. For `mermaid`, produce a readable board map, not a fake editable whiteboard.
11. For `microsoft-whiteboard`, provide setup instructions, section labels, sticky color legend, and export guidance unless an actual Whiteboard connector/API is available.
12. For image outputs, use image generation when available and the runtime can return or save images. Use web image search only when generation is unavailable, the user explicitly requests real-world/source imagery, or the board must use a specific real-world object/place.
13. Use original raster artwork, generated images, emoji/icon libraries, or licensed/source-attributed images for visually rich boards. Do not rely only on plain vector boxes unless the user asks for a minimal board.

## 4. Interpret a Completed Retro

1. Read [references/post-retro-summary.md](references/post-retro-summary.md).
2. Extract visible content by section.
3. Preserve uncertainty:
   - Mark illegible content as `[unclear]`.
   - Do not invent text from unreadable sticky notes.
   - Ask for a better image only when missing text affects decisions or actions.
4. Cluster similar notes into themes.
5. Identify signals:
   - sentiment
   - repeated pain points
   - top-voted topics
   - kudos
   - risks
   - unresolved questions
   - decisions
6. Convert action items into accountable follow-up:
   - action
   - owner
   - due date
   - success measure
   - source note or theme
7. Produce the requested output:
   - text summary
   - Mermaid summary map
   - Confluence-ready notes
   - Jira issue drafts
   - team follow-up message
   - next-retro opening checklist

## 5. Quality Checklist

1. Limit the main board to 3-6 active sections unless the user asks for more.
2. Make action items specific, owned, measurable, and reviewable.
3. Include follow-up from the last retro when available.
4. Keep wording blame-free and process-focused.
5. Use accessible contrast and readable labels.
6. Avoid relying on color alone; pair colors with labels or symbols.
7. Avoid claiming a live integration succeeded unless a connector/API actually performed it.
8. Ensure the output format matches what the user can edit, share, or import.
9. Check that at least one theme-native sentiment or diagnostic widget is present by default, unless the user asks for a minimal board.
10. Check that each active column can visibly hold at least 10 sticky notes or equivalent content cards before delivering a team-ready board.
11. Check that the chosen visual mode matches the user’s preference; if not specified, state the assumption briefly.
12. Check that generated-image boards show the board with its title and content areas, not fake surrounding tool UI.
13. Check Draw.io hybrid boards:
   - background contains no baked-in post-it notes
   - post-its are editable Draw.io objects
   - post-its fit fully inside their columns
   - post-its align to a consistent grid with equal margins and row/column gaps
   - post-its do not cover baked-in titles, prompts, decorative badges, diagnostics, or the object pool
   - each column uses a consistent post-it color unless mixed colors were requested
   - icon palette is editable/copyable text or icon objects
   - read-only gauges/meters may stay in the background when they do not need editing
   - titles are not duplicated if already present in the background
   - diagnostics are theme-native and limited to the smallest useful set, usually one or two widgets

## 6. Examples

1. Input:

   ```text
   Create a fun retro board for our sprint review. I feel lucky. Draw.io please.
   ```

   Output:

   ```text
   Created a Draw.io board named "Time Machine Sprint Retro" with:
   - mood check
   - Past Wins
   - Glitches in the Timeline
   - Experiments for Next Jump
   - Action Items
   - copy/paste sticky pool
   - dot-voting tokens
   ```

2. Input:

   ```text
   Make a serious Mermaid retro for a production incident follow-up.
   ```

   Output:

   ```mermaid
   flowchart LR
     Goal["Goal: learn from the incident without blame"]
     Facts["Facts and timeline"]
     Worked["What helped"]
     Pain["What made recovery harder"]
     Improve["Prevention experiments"]
     Actions["Actions with owner and due date"]
     Goal --> Facts --> Worked --> Pain --> Improve --> Actions
   ```

3. Input:

   ```text
   Summarize this retro photo into Confluence notes and Jira action drafts.
   ```

   Output:

   ```text
   Confluence:
   - Summary
   - Themes
   - Decisions
   - Action items

   Jira drafts:
   - Title
   - Description
   - Owner
   - Due date
   - Acceptance criteria
   ```

## 7. Troubleshooting

1. If the user asks for Microsoft Whiteboard import but no connector exists, provide a board layout and manual setup steps. Do not claim direct import.
2. If a Mermaid board becomes too dense, split it into a board overview and a separate action-item table.
3. If Draw.io XML fails to open, check XML escaping, root cells `id="0"` and `id="1"`, and non-self-closing edge cells.
4. If a completed-board photo is blurry, extract only readable notes and request a sharper image for unclear action items.
5. If the board has too many sections, recommend a smaller core board plus a parking lot.
6. If actions are vague, rewrite them into experiment format: `We will try X for Y time, owned by Z, measured by W`.
7. If the user requests copyrighted or branded visuals, use generated/original visuals or ask for licensed assets.
