#!/usr/bin/env python3
"""Generate a portable Draw.io retrospective board.

The script has no third-party dependencies. It creates uncompressed .drawio XML
that can be opened in draw.io/diagrams.net and edited as a normal board.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


PALETTE = [
    ("#fff2cc", "#d6b656"),
    ("#d5e8d4", "#82b366"),
    ("#dae8fc", "#6c8ebf"),
    ("#f8cecc", "#b85450"),
    ("#e1d5e7", "#9673a6"),
    ("#ffe6cc", "#d79b00"),
]

STICKY_COLORS = [
    ("#fff2cc", "#d6b656"),
    ("#d5e8d4", "#82b366"),
    ("#dae8fc", "#6c8ebf"),
    ("#f8cecc", "#b85450"),
]


def cell(root: ET.Element, cell_id: str, **attrs: str) -> ET.Element:
    attrs["id"] = cell_id
    return ET.SubElement(root, "mxCell", attrs)


def geometry(parent: ET.Element, x: int, y: int, width: int, height: int) -> None:
    ET.SubElement(
        parent,
        "mxGeometry",
        {
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "as": "geometry",
        },
    )


def add_vertex(
    root: ET.Element,
    cell_id: str,
    label: str,
    style: str,
    x: int,
    y: int,
    width: int,
    height: int,
    parent: str = "1",
) -> None:
    node = cell(root, cell_id, value=label, style=style, vertex="1", parent=parent)
    geometry(node, x, y, width, height)


def base_style(fill: str, stroke: str, extra: str = "") -> str:
    return (
        "rounded=1;whiteSpace=wrap;html=1;arcSize=8;"
        f"fillColor={fill};strokeColor={stroke};fontColor=#1f2933;"
        f"{extra}"
    )


def sticky_style(fill: str, stroke: str, extra: str = "") -> str:
    return (
        "shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.08;"
        f"fillColor={fill};strokeColor={stroke};fontColor=#1f2933;"
        f"{extra}"
    )


def text_style(size: int = 16, bold: bool = False) -> str:
    font_style = "1" if bold else "0"
    return (
        "text;html=1;strokeColor=none;fillColor=none;align=left;"
        f"verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize={size};fontStyle={font_style};"
    )


def parse_columns(raw: str | None, spec: dict) -> list[dict]:
    if "columns" in spec:
        columns = spec["columns"]
        normalized = []
        for index, item in enumerate(columns):
            if isinstance(item, str):
                fill, stroke = PALETTE[index % len(PALETTE)]
                normalized.append({"title": item, "prompt": "", "fill": fill, "stroke": stroke})
            else:
                fill, stroke = PALETTE[index % len(PALETTE)]
                normalized.append(
                    {
                        "title": str(item.get("title", f"Column {index + 1}")),
                        "prompt": str(item.get("prompt", "")),
                        "fill": str(item.get("fill", fill)),
                        "stroke": str(item.get("stroke", stroke)),
                    }
                )
        return normalized

    titles = (raw or "Went Well|Did Not Go Well|Ideas|Action Items").split("|")
    result = []
    for index, title in enumerate(t.strip() for t in titles if t.strip()):
        fill, stroke = PALETTE[index % len(PALETTE)]
        result.append({"title": title, "prompt": "", "fill": fill, "stroke": stroke})
    return result


def load_spec(path: str | None) -> dict:
    if not path:
        return {}
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Could not read spec JSON: {exc}") from exc


def build_board(spec: dict, args: argparse.Namespace) -> ET.ElementTree:
    title = str(spec.get("title") or args.title)
    theme = str(spec.get("theme") or args.theme)
    sentiment = str(spec.get("sentiment") or args.sentiment)
    columns = parse_columns(args.columns, spec)
    if len(columns) < 2:
        raise SystemExit("Create at least two columns.")
    if len(columns) > 8:
        raise SystemExit("Use 8 or fewer columns to keep the board readable.")

    notes_per_column = int(spec.get("notes_per_column") or args.notes_per_column)
    if notes_per_column < 1:
        raise SystemExit("notes-per-column must be at least 1.")
    if notes_per_column > 20:
        raise SystemExit("Use 20 or fewer notes per column to keep the board manageable.")

    column_width = 360
    gap = 26
    board_x = 40
    board_y = 170
    note_width = 150
    note_height = 70
    note_gap_x = 18
    note_gap_y = 20
    note_cols = 2 if notes_per_column > 5 else 1
    note_rows = (notes_per_column + note_cols - 1) // note_cols
    column_height = max(620, 120 + note_rows * (note_height + note_gap_y) + 35)
    board_width = len(columns) * column_width + (len(columns) - 1) * gap
    pool_x = board_x + board_width + 50
    canvas_width = pool_x + 310
    canvas_height = max(980, board_y + column_height + 190)

    mxfile = ET.Element("mxfile", {"host": "drawio", "version": "26.0.0"})
    diagram = ET.SubElement(mxfile, "diagram", {"name": "Retro Board"})
    model = ET.SubElement(
        diagram,
        "mxGraphModel",
        {
            "dx": str(canvas_width),
            "dy": str(canvas_height),
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": str(canvas_width),
            "pageHeight": str(canvas_height),
            "math": "0",
            "shadow": "0",
        },
    )
    root = ET.SubElement(model, "root")
    cell(root, "0")
    cell(root, "1", parent="0")

    add_vertex(
        root,
        "title",
        f"{title}\nTheme: {theme}",
        text_style(size=26, bold=True),
        40,
        25,
        board_width,
        60,
    )
    add_vertex(
        root,
        "goal",
        "Goal: learn, improve, and leave with owned next steps.",
        base_style("#f5f5f5", "#666666", "fontSize=14;"),
        40,
        95,
        board_width,
        50,
    )
    add_vertex(
        root,
        "sentiment",
        f"Sentiment Check\n{sentiment}",
        base_style("#e1d5e7", "#9673a6", "fontSize=14;fontStyle=1;"),
        pool_x,
        40,
        260,
        80,
    )

    next_id = 100
    for index, column in enumerate(columns):
        x = board_x + index * (column_width + gap)
        add_vertex(
            root,
            f"col-{index}",
            column["title"],
            (
                "swimlane;html=1;startSize=42;rounded=1;arcSize=6;"
                f"fillColor={column['fill']};strokeColor={column['stroke']};"
                "fontColor=#1f2933;fontSize=16;fontStyle=1;whiteSpace=wrap;"
            ),
            x,
            board_y,
            column_width,
            column_height,
        )
        if column["prompt"]:
            add_vertex(
                root,
                f"prompt-{index}",
                column["prompt"],
                text_style(size=12),
                12,
                52,
                column_width - 24,
                50,
                parent=f"col-{index}",
            )
        for sticky_index in range(notes_per_column):
            fill, stroke = STICKY_COLORS[(index + sticky_index) % len(STICKY_COLORS)]
            note_col = sticky_index % note_cols
            note_row = sticky_index // note_cols
            add_vertex(
                root,
                f"sticky-{index}-{sticky_index}",
                "Add note",
                sticky_style(fill, stroke, "fontSize=13;spacing=8;size=16;shadow=1;"),
                18 + note_col * (note_width + note_gap_x),
                105 + note_row * (note_height + note_gap_y),
                note_width,
                note_height,
                parent=f"col-{index}",
            )
        next_id += 10

    add_vertex(root, "pool-title", "Copy/Paste Pool", text_style(size=18, bold=True), pool_x, 145, 260, 35)
    for index, (fill, stroke) in enumerate(STICKY_COLORS):
        add_vertex(
            root,
            f"pool-sticky-{index}",
            "Blank sticky",
            sticky_style(fill, stroke, "fontSize=13;spacing=8;size=16;shadow=1;"),
            pool_x,
            190 + index * 85,
            125,
            65,
        )

    for index in range(6):
        add_vertex(
            root,
            f"vote-{index}",
            "",
            "ellipse;html=1;fillColor=#1f2933;strokeColor=#1f2933;",
            pool_x + 155 + (index % 3) * 34,
            200 + (index // 3) * 34,
            22,
            22,
        )

    add_vertex(
        root,
        "action-card",
        "Action\nOwner:\nDue date:\nSuccess measure:",
        base_style("#ffffff", "#666666", "fontSize=13;spacing=8;"),
        pool_x + 150,
        290,
        140,
        130,
    )
    add_vertex(
        root,
        "legend",
        "Legend\nYellow: ideas\nGreen: wins\nBlue: facts\nPink: pain points\nBlack dots: votes",
        base_style("#f5f5f5", "#666666", "fontSize=12;spacing=8;"),
        pool_x,
        545,
        290,
        125,
    )
    add_vertex(
        root,
        "facilitation",
        "Flow\n1. Mood check\n2. Silent writing\n3. Group similar notes\n4. Dot vote\n5. Commit actions",
        base_style("#f5f5f5", "#666666", "fontSize=12;spacing=8;"),
        40,
        board_y + column_height + 25,
        min(board_width, 720),
        115,
    )

    return ET.ElementTree(mxfile)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate an editable Draw.io retrospective board.")
    parser.add_argument("--title", default="Sprint Retrospective", help="Board title.")
    parser.add_argument("--theme", default="I Feel Lucky", help="Visual theme label.")
    parser.add_argument(
        "--columns",
        default=None,
        help="Pipe-separated column titles, for example 'Went Well|Did Not Go Well|Ideas|Action Items'.",
    )
    parser.add_argument(
        "--sentiment",
        default="Pick a mood, weather, or confidence score before writing notes.",
        help="Sentiment check prompt.",
    )
    parser.add_argument("--spec", default=None, help="Optional JSON spec with title, theme, sentiment, and columns.")
    parser.add_argument("--notes-per-column", type=int, default=10, help="Sticky-note placeholders per active column.")
    parser.add_argument("--output", required=True, help="Output .drawio path.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    spec = load_spec(args.spec)
    tree = build_board(spec, args)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    ET.indent(tree, space="  ")
    tree.write(output, encoding="utf-8", xml_declaration=True)
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
