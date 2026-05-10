# Retro Board Patterns

## Section Catalog

Use these sections as building blocks. Keep the active board compact.

| Section | Use when | Prompt |
| --- | --- | --- |
| Sentiment Check | Start the session with a low-friction signal | How do you feel about the last sprint? |
| Confidence Vote | Release, delivery, or planning confidence matters | How confident are you about our direction? |
| Energy Check | Burnout, focus, or capacity is relevant | What is your current energy level? |
| Went Well | Capture repeatable wins | What should we keep doing? |
| Did Not Go Well | Surface blockers and friction | What made work harder? |
| Ideas | Generate improvement experiments | What should we try next sprint? |
| Action Items | Commit to follow-up | What will we do, who owns it, and by when? |
| Start / Stop / Continue | Improve habits and working agreements | What should we start, stop, and continue? |
| Mad / Sad / Glad | Explore emotional signals | What made us mad, sad, or glad? |
| Kudos | Recognize helpful behavior | Who helped the team and how? |
| Puzzles / Questions | Capture ambiguity | What do we not understand yet? |
| Metrics / Facts | Ground discussion in evidence | What data should inform the retro? |
| Parking Lot | Keep scope under control | What should we revisit later? |

## Default Board

Use this when the user provides little detail:

1. Session goal
2. Sentiment check
3. Went Well
4. Did Not Go Well
5. Ideas
6. Action Items
7. Sticky-note and dot-voting pool

Default capacity: size each active column for at least 10 sticky notes. Use a 2 x 5 note grid for dense boards or a 1 x 10 list for tall boards.

Ask for capacity when it is not known:

```text
How many post-its should fit in each column?
```

## Visual Bar

For polished boards, use the provided examples as style targets:

1. Build the board itself by default: title, themed sections, sticky-note areas, and facilitation widgets.
2. Do not copy screenshot chrome from examples. Avoid fake host-tool menus, sidebars, browser bars, toolbar buttons, cursors, or navigation unless the user explicitly asks for an in-tool screenshot or UI mockup.
3. Make each column a large themed scene, not a plain container.
4. Reserve most of the column height for participant notes.
5. For Draw.io hybrid boards, put the illustration, column regions, optional titles, and read-only visual widgets in the background. Add sticky notes, icon palettes, vote tokens, and movable participant inputs as editable Draw.io objects. Do not add foreground labels that duplicate background labels.
6. Put the illustration behind or below the sticky-note area so notes stay readable.
7. Use tactile cards: paper texture, shadows, folded corners, doodle strokes, stickers, badges, or icon chips.
8. Use real or generated raster artwork for showcase PNG/JPG boards when available.
9. Use editable Draw.io shapes for Draw.io boards, but make them resemble a designed whiteboard rather than a generic diagram.

## Alignment Contract

Use an alignment contract for every hybrid Draw.io board before image generation:

1. Define the page size.
2. Define a title band where no editable objects will be placed.
3. Define each column rectangle.
4. Define each column's header and prompt area.
5. Define a note-safe rectangle inside each column.
6. Define any diagnostic widget zones.
7. Define the copy/paste pool and icon palette zone.
8. Place editable Draw.io objects only inside their assigned zones.

Post-it placement:

1. For 5 notes per column, use a 1 x 5 grid.
2. For 10 notes per column, use a 2 x 5 grid.
3. For 15 notes per column, use a 3 x 5 grid.
4. Center the grid inside the note-safe rectangle.
5. Keep equal horizontal and vertical gaps.
6. Keep notes away from column titles, prompts, badges, separators, diagnostics, and decorative props.
7. Do not let note corners touch or cross column borders.
8. Move notes down, shrink them, or reduce decorative overlay density when alignment is uncertain.

Delivery check:

1. Verify the note count in each column.
2. Verify each note bounding box is inside the expected note-safe rectangle.
3. Verify no editable object overlaps baked-in text.
4. Verify the copy/paste pool has its own clear zone.

## Intake Question Bank

Use one concise question when the visual direction is ambiguous:

```text
Do you want this as an editable vector board, a polished generated-image board, or a hybrid?
```

Use this shorter version when the user already selected a format:

```text
Should the visuals be editable/vector-style, generated/raster-style, or a hybrid?
```

## Format Presets

### Classic Improvement Retro

Use for most scrum teams.

1. Went Well
2. Did Not Go Well
3. Ideas
4. Action Items

### Start / Stop / Continue

Use when the team wants behavior or process changes.

1. Start Doing
2. Stop Doing
3. Continue Doing
4. Action Items

### Mad / Sad / Glad

Use when morale, trust, or team health is central.

1. Mad
2. Sad
3. Glad
4. What We Need
5. Actions

### Learning Retro

Use after releases, incidents, spikes, discovery work, or experiments.

1. Facts
2. What Helped
3. What Hurt
4. What We Learned
5. Experiments
6. Actions

### Celebration Retro

Use after a difficult sprint, milestone, or release.

1. Wins
2. Kudos
3. Surprises
4. Improvements
5. Next Tiny Experiments

## Theme Ideas

Use the theme to name sections and choose visual props. Do not let it obscure the facilitation flow.

| Theme | Best for | Section naming idea |
| --- | --- | --- |
| Space Mission | delivery, exploration, releases | Launches, Asteroids, Course Corrections, Next Orbit |
| Time Machine | sprint review, learning | Keep, Rewind, Fast Forward, Next Jump |
| Arcade | fun team reset | High Scores, Bugs, Power-Ups, Next Level |
| Garden | sustainable improvement | Blooms, Weeds, Seeds, Care Plan |
| Weather Station | sentiment-heavy retros | Sunshine, Clouds, Storms, Forecast |
| Road Trip | planning and blockers | Smooth Roads, Roadblocks, Detours, Next Stop |
| Kitchen | process improvement | Tasty Wins, Burnt Bits, New Recipes, Prep List |
| Detective Board | incident or mystery solving | Clues, Red Herrings, Leads, Case Actions |
| Mountain Trek | hard sprint or long goal | Basecamp, Avalanches, Gear Upgrades, Summit Plan |
| Festival | morale and celebration | Headliners, Feedback, New Acts, Crew Tasks |

## Seasonal Suggestions

Use only when culturally appropriate and not distracting.

| Timing | Theme ideas |
| --- | --- |
| January | New Year reset, expedition map, fresh-start garden |
| Spring | garden, weather, renewal lab |
| Summer | road trip, festival, beach cleanup |
| Autumn | harvest, campfire, detective case |
| December | year-end wrap, snow basecamp, gift exchange of kudos |
| Release week | launch pad, control room, race pit |
| Incident follow-up | learning lab, detective board, safety review |

## Facilitation Blocks

Include these blocks on editable boards when space allows.

1. Goal: one sentence describing what the retro is for.
2. Theme-native diagnostic widget: choose one or two signals that fit the session, such as mood, readiness, clarity, risk, alignment, confidence, celebration, fatigue, or focus.
3. Mood board: emoji cards, weather tiles, metaphor cards, or team-energy snapshots when emotional check-in matters.
4. Gauge widgets: confidence meter, risk meter, energy battery, or "ready to ship" dial only when the measurement helps the facilitation.
5. Icon palette: emoji markers, reaction chips, owner tags, due-date tags, risk markers, kudos markers, and vote dots.
6. Working agreement: focus on process, systems, and improvement.
7. Timebox: suggested minutes for each section.
8. Voting: each participant gets 3 dots unless the team size or timebox suggests another number.
9. Grouping: combine duplicates before voting.
10. Actions: each action needs owner, due date, and success measure.
11. Follow-up: review previous actions before creating new ones.

## Theme-Native Diagnostic Widgets

Do not place mood, confidence, energy, and risk on every board by habit. Pick the smallest useful set, usually one widget for opening sentiment and one widget for delivery readiness or risk.

Use this decision rule:

1. Use `Mood` when psychological safety, morale, or engagement matters.
2. Use `Confidence` when release, planning, or decision readiness matters.
3. Use `Energy` when sustainability, fatigue, or capacity matters.
4. Use `Risk` when deadlines, production stability, incidents, compliance, or dependencies matter.
5. Replace generic labels with theme-native labels and visuals.

| Theme | Instead of mood check | Instead of confidence | Instead of energy | Instead of risk heat |
| --- | --- | --- | --- | --- |
| Space mission | Crew status helmets | Launch readiness dial | Fuel cell level | Re-entry risk radar |
| Easter | Egg-face nest | Hatch readiness | Basket fullness | Cracked-shell meter |
| Summer starts | Sunglasses vibe row | Sun-dial certainty | Cooler level | UV index |
| New pope | Candle mood medallions | White-smoke clarity | Candle flame strength | Conclave delay signals |
| Labubu / toy shelf | Toy-face shelf | Blind-box confidence | Sparkle charge | Mischief meter |
| Smals 80 years | Service pulse badges | Trust and continuity dial | Team bandwidth meter | Legacy friction heatmap |
| Go-live celebration | Party badge mood | Production confidence | Support stamina | Incident radar |
| Garden | Seedling mood | Growth confidence | Watering-can level | Weed pressure |
| Detective board | Case-room vibe | Evidence strength | Investigator focus | Red-herring risk |
| Mountain trek | Basecamp mood | Summit visibility | Oxygen level | Avalanche risk |

Use visual forms beyond gauges:

1. Token rows: helmets, eggs, candles, badges, toy faces, suns, leaves.
2. Scene meters: fuel tanks, thermometers, tide lines, progress ropes, trail markers.
3. Choice maps: risk constellations, heat islands, chapel arches, garden beds, radar screens.
4. Physical props: coolers, baskets, lanterns, launch consoles, ticket stubs, service dashboards.
5. Themed voting: moon rocks, confetti dots, flower seeds, sun coins, candle flames, data pips.

Keep diagnostics readable:

1. Use the theme for the label and image.
2. Keep the underlying question plain enough for participants to understand.
3. Avoid more than two diagnostics unless the user asks for a workshop-style board.
4. Leave editable markers nearby so participants can interact with the widget.
5. Do not use generic labels such as `Mood Check`, `Confidence Gauge`, `Team Energy`, or `Risk Heat Meter` in generated backgrounds when a theme-native alternative is available.

## Visual Widget Catalog

Use these elements to keep boards expressive and usable.

| Widget | Use when | Examples |
| --- | --- | --- |
| Mood board | Starting emotional check-in | Real Unicode emoji cards for happy, neutral, tense, tired, or ready-to-launch states |
| Weather vote | Team atmosphere matters | `sunny`, `cloudy`, `rainy`, `stormy`, `rainbow` weather cards |
| Confidence gauge | Release or delivery confidence matters | 1-5 dial, red-yellow-green arc |
| Energy battery | Sustainability or capacity matters | low / medium / full battery meter |
| Risk thermometer | Incident, quality, or deadline risk matters | cool / warm / hot risk scale |
| Theme-native diagnostic | A generic widget would feel dull or bolted on | launch readiness, service pulse, UV index, candle flame, oxygen level |
| Icon palette | Editable boards need copy/paste markers | check, warning, idea, kudos, question, pin icons |
| Theme prop pool | Fun boards need reusable props | eggs, suns, snowflakes, clouds, rockets, coins |

## Anti-Pattern Checks

Fix these before delivering the board:

1. More than 6 active columns without a strong reason.
2. No action-item area.
3. No voting or prioritization path.
4. No owner/due-date fields for actions.
5. Theme names that participants cannot map back to the actual retro purpose.
6. Visuals that make text hard to read.
7. Color-only meaning without labels.
8. Blame-focused prompts.
9. No visible sentiment or diagnostic widget on a board intended for a live retrospective.
10. Generic rectangles where sticky-note, card, icon, or theme-specific shapes would be more natural.
11. Columns that only fit 2-4 notes when the team needs a usable live retro board.
12. Generated images that look like screenshots of a tool instead of the board artifact requested by the user.
13. Draw.io hybrid backgrounds that already contain non-editable sticky notes or icon palettes.
14. ASCII-only mood markers such as `:)`, `:/`, or `:D` when the user asked for real Unicode emoji or icon palettes.
15. Foreground text labels that repeat background labels such as copy/paste pool, icon palette, vote tokens, column titles, or mood-board headings.
16. Draw.io sticky notes that overflow column boundaries.
17. Backgrounds that leave no room for editable overlay layers such as icon palettes, copy/paste pools, or action cards.
18. Adding mood, confidence, energy, and risk widgets all at once without a facilitation reason.
19. Generic labels such as `Mood Check`, `Confidence`, `Team Energy`, or `Risk Heat` when a theme-native label would be clearer and more memorable.
