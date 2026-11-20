#!/usr/bin/env python3
"""Verify the three owner-selected shared-Progression goals without treating them as runtime data."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys

REQUIRED = {"tmt:cyborg", "tmt:meatbag", "tmt:alien"}
HEX40 = re.compile(r"^[0-9a-fA-F]{40}$")


def validate(root: Path) -> list[str]:
    path = root / "manifest/progression-goals.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"{path}: {exc}"]
    errors: list[str] = []
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return ["progression goals: schema_version must be 1"]
    engine = data.get("engine")
    if not isinstance(engine, dict):
        return ["progression goals: missing shared engine object"]
    if not HEX40.fullmatch(str(engine.get("inspected_commit", ""))):
        errors.append("progression goals: source SHA must be 40 hex characters")
    if engine.get("source_repository") != "heatwaveqc/Too-Much-Magic-Modpack":
        errors.append("progression goals: unexpected upstream source repository")
    if engine.get("source_subtree") != "compat/progression":
        errors.append("progression goals: unexpected upstream progression subtree")
    if engine.get("ready_for_import") is not False or engine.get("packwiz_installed") is not False:
        errors.append("progression goals: research may not claim imported/installed engine")
    paths = data.get("paths")
    if not isinstance(paths, list):
        return errors + ["progression goals: paths must be an array"]
    seen: set[str] = set()
    for n, goal in enumerate(paths):
        if not isinstance(goal, dict):
            errors.append(f"progression goals: paths[{n}] must be object")
            continue
        path_id = goal.get("id")
        if not isinstance(path_id, str) or not path_id.startswith("tmt:"):
            errors.append(f"progression goals: paths[{n}] invalid namespaced id")
            continue
        if path_id in seen:
            errors.append(f"progression goals: duplicate {path_id}")
        seen.add(path_id)
        if goal.get("stage") != "goal" or goal.get("mechanics_locked") is not False:
            errors.append(f"progression goals: {path_id} cannot claim runtime completion")
        if not isinstance(goal.get("possible_milestones"), list) or not goal["possible_milestones"]:
            errors.append(f"progression goals: {path_id} needs proposed milestones")
    if not REQUIRED.issubset(seen):
        errors.append(f"progression goals: missing {sorted(REQUIRED - seen)}")
    return errors


def main() -> int:
    errors = validate(Path(__file__).resolve().parents[1])
    if errors:
        for e in errors:
            print(e)
        return 1
    print("PROGRESSION GOALS PASS — target-only metadata, no gameplay/runtime validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
