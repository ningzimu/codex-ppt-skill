#!/usr/bin/env python3
"""Record that a codex-ppt slide job was dispatched to a subagent."""

from __future__ import annotations

import argparse
from pathlib import Path

from slide_run_state import (
    deck_dir_from_target,
    find_slide,
    load_jobs,
    now_iso,
    rel_to_deck,
    resolve_deck_path,
    save_jobs,
    set_run_status,
    sha256_file,
    update_jobs_run_status,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck", help="Deck directory or slide_jobs.json")
    parser.add_argument("--slide", required=True, help="slide_01 or 1")
    parser.add_argument("--agent-id", required=True)
    parser.add_argument("--agent-nickname")
    parser.add_argument("--prompt-file", help="Prompt file path. Defaults to the job file in slide_jobs.json.")
    args = parser.parse_args()

    deck_dir = deck_dir_from_target(args.deck)
    jobs = load_jobs(deck_dir)
    slide = find_slide(jobs, args.slide)
    if slide.get("status") != "pending":
        raise SystemExit(f"{slide['slide_id']} must be pending before dispatch; got {slide.get('status')}")

    prompt_ref = args.prompt_file or slide.get("job")
    if not prompt_ref:
        raise SystemExit(f"{slide['slide_id']} has no prompt job path.")
    prompt_path = resolve_deck_path(deck_dir, prompt_ref)
    try:
        prompt_path.relative_to(deck_dir)
    except ValueError as exc:
        raise SystemExit(f"Prompt file must live inside deck dir: {prompt_path}") from exc
    if not prompt_path.exists():
        raise SystemExit(f"Prompt file does not exist: {prompt_path}")

    slide["dispatch"] = {
        "agent_id": args.agent_id,
        "agent_nickname": args.agent_nickname,
        "prompt": rel_to_deck(deck_dir, prompt_path),
        "prompt_sha256": sha256_file(prompt_path),
        "dispatched_at": now_iso(),
    }
    slide["status"] = "dispatched"
    update_jobs_run_status(jobs)
    save_jobs(deck_dir, jobs)
    if jobs.get("run_status") == "slides_dispatched":
        set_run_status(deck_dir, "slides_dispatched", "all slide jobs dispatched")
    print(f"{slide['slide_id']} -> dispatched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
