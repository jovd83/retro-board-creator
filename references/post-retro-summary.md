# Post-Retro Summary Guide

## Extraction Workflow

1. Identify the source format:
   - photo
   - screenshot
   - PNG/SVG
   - Mermaid
   - Draw.io XML
   - Microsoft Whiteboard export
   - raw text
2. Extract all visible notes section by section.
3. Preserve original wording where readable.
4. Mark uncertain notes as `[unclear]`.
5. Do not infer missing sticky-note text from nearby context.
6. Count votes when visible.
7. Capture colors only when they encode meaning.
8. Capture reactions, mood markers, or confidence votes.

## Clustering Workflow

1. Normalize near-duplicates.
2. Cluster by theme, not by identical wording only.
3. Keep dissenting or minority notes when they reveal risk.
4. Separate facts from interpretations.
5. Keep kudos separate from improvement items.
6. Move unrelated but useful notes into a parking-lot section.

## Summary Output

Use this structure by default:

```text
Retro Summary

Context:
- ...

Overall sentiment:
- ...

Top themes:
1. ...
2. ...
3. ...

What went well:
- ...

What needs attention:
- ...

Decisions:
- ...

Action items:
| Action | Owner | Due date | Success measure | Source |
| --- | --- | --- | --- | --- |

Risks and open questions:
- ...

Follow-up for next retro:
- ...
```

## Action Item Rules

Convert notes into actions only when a next step is clear. If the note is only a complaint or observation, turn it into an experiment proposal and mark missing fields.

Good action:

```text
Run a 2-week experiment where refinement includes a 10-minute dependency check.
Owner: Product owner
Due date: next sprint planning
Success measure: fewer blocked stories caused by unknown dependencies
```

Weak action to fix:

```text
Communicate better.
```

Rewrite:

```text
Add a 5-minute risk/dependency round to Tuesday standup for the next sprint.
Owner: [needs owner]
Due date: [needs date]
Success measure: blockers are raised within 24 hours.
```

## Jira Draft Rules

Create one Jira draft per committed action, not per sticky note.

Use this structure:

```text
Summary: <verb-led action>
Description:
  Retro theme:
  Source notes:
  Proposed change:
  Success measure:
Acceptance criteria:
  - Given ...
  - When ...
  - Then ...
Labels: retrospective, continuous-improvement
```

## Confluence Rules

Use Confluence output for narrative summaries. Keep action items in a table. Put unresolved questions in their own section so they are not lost.

## Confidence Labels

Use confidence labels when interpreting images:

| Label | Meaning |
| --- | --- |
| High | Text is readable and section placement is clear |
| Medium | Text is readable but grouping or votes are uncertain |
| Low | Text is partially unreadable or source quality is poor |

## Anti-Hallucination Rules

1. Do not invent owner names.
2. Do not invent dates.
3. Do not treat color as meaning unless a legend exists or the user confirms it.
4. Do not drop low-vote notes if they contain safety, quality, or trust concerns.
5. Do not attribute negative notes to individuals unless the board explicitly does so and the user needs that preserved.

