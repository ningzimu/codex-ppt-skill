#!/usr/bin/env python3
"""Print codex-ppt slide generation job status."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

from slide_run_state import (
    active_slides,
    deck_dir_from_target,
    dispatch_slots_available,
    dispatchable_slides,
    load_jobs,
    load_run_state,
    max_concurrent_slides,
    slide_ids,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck", help="Deck directory or slide_jobs.json")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    deck_dir = deck_dir_from_target(args.deck)
    jobs = load_jobs(deck_dir)
    state = load_run_state(deck_dir)
    by_status = defaultdict(list)
    for slide in jobs.get("slides", []):
        by_status[slide.get("status", "unknown")].append(slide.get("slide_id"))
    summary = {
        "deck_dir": str(deck_dir),
        "run_status": state.get("status"),
        "slide_count": len(jobs.get("slides", [])),
        "selected_backend": jobs.get("selected_backend"),
        "max_concurrent_slides": max_concurrent_slides(jobs),
        "active_dispatches": slide_ids(active_slides(jobs)),
        "dispatch_slots_available": dispatch_slots_available(jobs),
        "dispatchable_slides": slide_ids(dispatchable_slides(jobs)),
        "counts": dict(Counter(slide.get("status", "unknown") for slide in jobs.get("slides", []))),
        "slides": dict(sorted(by_status.items())),
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    print(f"deck_dir={summary['deck_dir']}")
    print(f"run_status={summary['run_status']}")
    print(f"selected_backend={summary['selected_backend'] or '-'}")
    print(f"max_concurrent_slides={summary['max_concurrent_slides']}")
    print(f"active_dispatches={', '.join(summary['active_dispatches']) if summary['active_dispatches'] else '-'}")
    print(f"dispatch_slots_available={summary['dispatch_slots_available']}")
    print(f"dispatchable_slides={', '.join(summary['dispatchable_slides']) if summary['dispatchable_slides'] else '-'}")
    for status, slides in summary["slides"].items():
        print(f"{status}: {', '.join(slides) if slides else '-'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
