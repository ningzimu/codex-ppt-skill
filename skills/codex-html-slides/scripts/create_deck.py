#!/usr/bin/env python3
"""Create a self-contained HTML slide deck from the bundled template."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path


THEMES = (
    "clean-professional",
    "creative-magazine",
    "e-ink-magazine",
    "data-dashboard",
    "retro-flat",
    "handdrawn-technical",
    "handdrawn-whiteboard",
    "warm-handmade",
    "scientific-defense",
    "consulting",
    "party-red",
    "teaching-courseware",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", help="Destination .html file")
    parser.add_argument("--title", default="Untitled presentation", help="Deck title")
    parser.add_argument("--lang", default="zh-CN", help="HTML language tag, such as zh-CN or en")
    parser.add_argument("--theme", choices=THEMES, default="clean-professional")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing output file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = Path(args.output).expanduser().resolve()
    if output.suffix.lower() not in {".html", ".htm"}:
        raise SystemExit(f"Output must use .html or .htm: {output}")
    if output.exists() and not args.force:
        raise SystemExit(f"Output already exists: {output} (pass --force to overwrite)")
    if not re.fullmatch(r"[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*", args.lang):
        raise SystemExit(f"Invalid language tag: {args.lang}")

    template = Path(__file__).resolve().parents[1] / "assets" / "deck-template.html"
    content = template.read_text(encoding="utf-8")
    replacements = {
        "{{DECK_TITLE}}": html.escape(args.title, quote=True),
        "{{DECK_LANG}}": args.lang,
        "{{DECK_THEME}}": args.theme,
    }
    for marker, value in replacements.items():
        content = content.replace(marker, value)

    unresolved = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", content)))
    if unresolved:
        raise SystemExit(f"Template contains unresolved markers: {', '.join(unresolved)}")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(output),
                "theme": args.theme,
                "title": args.title,
                "self_contained": True,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

