#!/usr/bin/env python3
"""Validate structure, accessibility, and self-containment of an HTML slide deck."""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
RASTER_EXTENSIONS = ("png", "jpe?g", "webp", "gif", "bmp", "tiff?")
DATA_OR_ANCHOR = re.compile(r"^(?:data:|#|mailto:|tel:)", re.IGNORECASE)


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.doctype = False
        self.html_lang = ""
        self.viewport = False
        self.ids: list[str] = []
        self.slides: list[dict[str, Any]] = []
        self.current_slide: dict[str, Any] | None = None
        self.slide_depth: int | None = None
        self.depth = 0
        self.in_style = False
        self.in_script = False
        self.styles: list[str] = []
        self.scripts: list[str] = []
        self.external_assets: list[str] = []
        self.images: list[dict[str, Any]] = []
        self.script_sources: list[str] = []
        self.stylesheet_links: list[str] = []
        self.frames: list[str] = []
        self.object_tags = 0

    @staticmethod
    def _attrs(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {key: value or "" for key, value in attrs}

    def handle_decl(self, decl: str) -> None:
        if decl.lower().strip() == "doctype html":
            self.doctype = True

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = self._attrs(attrs)
        classes = set(values.get("class", "").split())
        if tag not in VOID_TAGS:
            self.depth += 1

        if tag == "html":
            self.html_lang = values.get("lang", "").strip()
        elif tag == "meta" and values.get("name", "").lower() == "viewport":
            self.viewport = bool(values.get("content", "").strip())
        elif tag == "style":
            self.in_style = True
        elif tag == "script":
            self.in_script = True
            if values.get("src"):
                self.script_sources.append(values["src"])
        elif tag == "link" and "stylesheet" in values.get("rel", "").lower().split():
            self.stylesheet_links.append(values.get("href", ""))
        elif tag in {"iframe", "frame"}:
            self.frames.append(values.get("src", ""))
        elif tag in {"object", "embed"}:
            self.object_tags += 1

        element_id = values.get("id", "").strip()
        if element_id:
            self.ids.append(element_id)

        if tag == "section" and "slide" in classes and "data-slide" in values:
            slide = {
                "id": element_id,
                "aria_label": values.get("aria-label", "").strip(),
                "aria_labelledby": values.get("aria-labelledby", "").strip(),
                "headings": 0,
                "text_chars": 0,
                "notes": 0,
            }
            self.slides.append(slide)
            self.current_slide = slide
            self.slide_depth = self.depth
        elif self.current_slide is not None:
            if tag in {"h1", "h2", "h3"}:
                self.current_slide["headings"] += 1
            if tag == "aside" and "speaker-notes" in classes:
                self.current_slide["notes"] += 1

        if tag == "img":
            src = values.get("src", "").strip()
            self.images.append({"src": src, "alt": values.get("alt", ""), "alt_present": "alt" in values})
            if src and not DATA_OR_ANCHOR.match(src):
                self.external_assets.append(src)
        elif tag in {"audio", "video", "source", "track"}:
            src = values.get("src", "").strip()
            if src and not DATA_OR_ANCHOR.match(src):
                self.external_assets.append(src)

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self.in_style = False
        elif tag == "script":
            self.in_script = False

        if tag == "section" and self.current_slide is not None and self.slide_depth == self.depth:
            self.current_slide = None
            self.slide_depth = None

        if tag not in VOID_TAGS:
            self.depth = max(0, self.depth - 1)

    def handle_data(self, data: str) -> None:
        if self.in_style:
            self.styles.append(data)
        elif self.in_script:
            self.scripts.append(data)
        elif self.current_slide is not None:
            self.current_slide["text_chars"] += len("".join(data.split()))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck", help="HTML deck to validate")
    parser.add_argument("--expect-slides", type=int, help="Require an exact slide count")
    parser.add_argument("--allow-external", action="store_true", help="Allow non-embedded assets and network dependencies")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def inspect_deck(path: Path, args: argparse.Namespace) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if path.suffix.lower() not in {".html", ".htm"}:
        errors.append("Deck must use the .html or .htm extension.")

    text = path.read_text(encoding="utf-8")
    parser = DeckParser()
    try:
        parser.feed(text)
        parser.close()
    except Exception as exc:  # HTMLParser errors are rare, but report them cleanly.
        errors.append(f"HTML parsing failed: {exc}")

    css = "\n".join(parser.styles)
    js = "\n".join(parser.scripts)
    lowered = text.lower()

    if not parser.doctype:
        errors.append("Missing <!doctype html> declaration.")
    if not parser.html_lang:
        errors.append("The <html> element must declare lang.")
    if not parser.viewport:
        errors.append("Missing viewport meta tag.")
    if not parser.slides:
        errors.append('No <section class="slide" data-slide> elements found.')
    if args.expect_slides is not None and len(parser.slides) != args.expect_slides:
        errors.append(f"Expected {args.expect_slides} slides, found {len(parser.slides)}.")

    duplicate_ids = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicate_ids:
        errors.append(f"Duplicate element ids: {', '.join(duplicate_ids)}")

    known_ids = set(parser.ids)
    slide_ids: list[str] = []
    for number, slide in enumerate(parser.slides, start=1):
        slide_id = slide["id"]
        if not slide_id:
            errors.append(f"Slide {number} is missing an id.")
        else:
            slide_ids.append(slide_id)
        if not slide["aria_label"] and not slide["aria_labelledby"]:
            errors.append(f"Slide {number} needs aria-label or aria-labelledby.")
        if slide["aria_labelledby"] and slide["aria_labelledby"] not in known_ids:
            errors.append(f"Slide {number} references missing label id: {slide['aria_labelledby']}")
        if slide["headings"] == 0:
            warnings.append(f"Slide {number} has no h1, h2, or h3 heading.")
        if slide["text_chars"] < 8:
            warnings.append(f"Slide {number} has very little readable text.")

    if len(set(slide_ids)) != len(slide_ids):
        errors.append("Slide ids must be unique.")

    if parser.script_sources:
        message = f"External script sources: {', '.join(parser.script_sources)}"
        (warnings if args.allow_external else errors).append(message)
    if parser.stylesheet_links:
        message = f"External stylesheet links: {', '.join(parser.stylesheet_links)}"
        (warnings if args.allow_external else errors).append(message)
    if parser.frames:
        message = f"Embedded frames are not self-contained: {', '.join(parser.frames)}"
        (warnings if args.allow_external else errors).append(message)
    if parser.object_tags:
        errors.append("Object/embed elements are not allowed in the default self-contained contract.")
    if parser.external_assets:
        message = f"Non-embedded media assets: {', '.join(sorted(set(parser.external_assets)))}"
        (warnings if args.allow_external else errors).append(message)

    for number, image in enumerate(parser.images, start=1):
        if not image["alt_present"]:
            warnings.append(f"Image {number} is missing alt text; use alt=\"\" for decoration.")

    css_external_urls = [
        value.strip(" \"'")
        for value in re.findall(r"url\(([^)]+)\)", css, flags=re.IGNORECASE)
        if not DATA_OR_ANCHOR.match(value.strip(" \"'"))
    ]
    if css_external_urls:
        message = f"CSS references non-embedded URLs: {', '.join(sorted(set(css_external_urls)))}"
        (warnings if args.allow_external else errors).append(message)
    if re.search(r"@import\s+", css, flags=re.IGNORECASE):
        message = "CSS @import is not self-contained."
        (warnings if args.allow_external else errors).append(message)

    raster_pattern = rf"(?:origin_image|slide[_-]?\d+\.(?:{'|'.join(RASTER_EXTENSIONS)}))"
    if re.search(raster_pattern, lowered, flags=re.IGNORECASE):
        errors.append("Detected a full-slide raster or origin_image reference.")
    if re.search(r"\.(?:png|jpe?g|webp|gif|bmp|tiff?)[\"')\s]", lowered) and not parser.images:
        warnings.append("Raster filename found outside an <img>; verify it is a required content asset, not a slide background.")
    if re.search(r"\.to(?:dataurl|blob)\s*\(", lowered) or "html2canvas" in lowered:
        errors.append("Detected canvas/screenshot export code, which violates the HTML-only contract.")

    compact_css = re.sub(r"\s+", "", css.lower())
    if "--canvas-width:1600px" not in compact_css or "--canvas-height:900px" not in compact_css:
        errors.append("Missing fixed 1600×900 canvas variables.")
    if "@mediaprint" not in compact_css:
        warnings.append("Missing print stylesheet.")
    if "prefers-reduced-motion" not in css:
        warnings.append("Missing reduced-motion support.")

    for token in ("ArrowRight", "ArrowLeft", "PageDown", "PageUp", "Home", "End"):
        if token not in js:
            errors.append(f"Navigation runtime is missing {token} handling.")
    if "requestFullscreen" not in js:
        warnings.append("Missing fullscreen support.")
    if "location.hash" not in js:
        warnings.append("Missing hash-based slide navigation.")
    if "data-counter" not in lowered:
        warnings.append("Missing visible slide counter.")

    status = "ok" if not errors and not (args.strict and warnings) else "failed"
    return {
        "status": status,
        "deck": str(path),
        "slide_count": len(parser.slides),
        "self_contained": not any((parser.script_sources, parser.stylesheet_links, parser.external_assets, css_external_urls, parser.frames)),
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    args = parse_args()
    path = Path(args.deck).expanduser().resolve()
    if not path.is_file():
        raise SystemExit(f"Deck not found: {path}")
    result = inspect_deck(path, args)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Deck: {result['deck']}")
        print(f"Slides: {result['slide_count']}")
        print(f"Self-contained: {str(result['self_contained']).lower()}")
        for error in result["errors"]:
            print(f"ERROR: {error}")
        for warning in result["warnings"]:
            print(f"WARNING: {warning}")
        print(f"Result: {result['status'].upper()}")
    return 0 if result["status"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
