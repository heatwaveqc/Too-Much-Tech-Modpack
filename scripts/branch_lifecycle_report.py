#!/usr/bin/env python3
"""Read-only GitHub branch/PR inventory and changed-path collision advisory.

No ref mutations, issue comments, downloads, game launch or build dispatch.
The caller must have read-only GitHub token permissions.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO = "heatwaveqc/Too-Much-Tech-Modpack"
PERMANENT = {"main", "test/full-integration"}


def api(path: str) -> object:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        raise RuntimeError("GITHUB_TOKEN is required for live read-only report")
    url = "https://api.github.com/repos/" + REPO + path
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "TMT-readonly-branch-report"
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def paged(path: str) -> list[dict]:
    output: list[dict] = []
    for page in range(1, 101):
        suffix = ("&" if "?" in path else "?") + f"per_page=100&page={page}"
        result = api(path + suffix)
        if not isinstance(result, list):
            raise RuntimeError(f"Expected list for {path}")
        output.extend(result)
        if len(result) < 100:
            return output
    raise RuntimeError(f"Too many pages; refusing incomplete inventory: {path}")


def overlap(a: set[str], b: set[str]) -> list[str]:
    """Exact changed-file intersection: an advisory, never a full conflict check."""
    return sorted(a & b)


def paths_for_pr(number: int) -> set[str]:
    records = paged(f"/pulls/{number}/files")
    names = {item["filename"] for item in records if isinstance(item.get("filename"), str)}
    return names


def active_source_refs(repo_root: Path) -> dict[str, list[str]]:
    file = repo_root / "manifest" / "integration-sources.json"
    sources = json.loads(file.read_text(encoding="utf-8"))
    references: dict[str, list[str]] = {}
    for row in sources["streams"]:
        if not row.get("integrated_into_baseline"):
            references.setdefault(row["branch"], []).append(row["name"])
    return references


def last_commit_age_days(sha: str) -> int | None:
    info = api("/commits/" + urllib.parse.quote(sha, safe=""))
    when = info.get("commit", {}).get("committer", {}).get("date")
    if not isinstance(when, str):
        return None
    date = dt.datetime.fromisoformat(when.replace("Z", "+00:00"))
    return max(0, (dt.datetime.now(dt.timezone.utc) - date).days)


def inventory(root: Path) -> int:
    branches = paged("/branches")
    pulls = paged("/pulls?state=open")
    donors = active_source_refs(root)
    names = {row["name"] for row in branches}
    pr_heads = {p["head"]["ref"] for p in pulls if p.get("head", {}).get("repo", {}).get("full_name") == REPO}
    pr_bases = {p["base"]["ref"] for p in pulls}
    count = len(branches)
    state = "healthy" if count <= 20 else ("review" if count <= 30 else "maintenance")
    print(f"TMT BRANCH INVENTORY (READ-ONLY): {count} branches; budget: {state}")
    print(f"Open PRs: {len(pulls)}. Frozen external donor refs: {len(donors)}.")
    for branch in sorted(branches, key=lambda r: r["name"]):
        name = branch["name"]
        sha = branch["commit"]["sha"]
        age = last_commit_age_days(sha)
        kinds: list[str] = []
        if name in PERMANENT:
            kinds.append("PERMANENT")
        if name in pr_heads:
            kinds.append("OPEN_PR_HEAD")
        if name in pr_bases:
            kinds.append("OPEN_PR_BASE")
        if name in donors:
            kinds.append("FROZEN_DONOR:" + ",".join(donors[name]))
        if not kinds:
            kinds.append("UNCLASSIFIED_REVIEW")
        print(f" - {name} {sha} age~{age if age is not None else '?'}d " + " ".join(kinds))
        if name not in PERMANENT and name not in pr_heads and age is not None and age >= 1:
            print("   REVIEW: temporary branch without PR; verify owner/provenance before action")
    for name in sorted(donors):
        if name not in names:
            print(f" WARNING: external donor branch {name} is absent; inspect frozen SHA/provenance")
    for p in pulls:
        label = "DRAFT" if p.get("draft") else "READY"
        print(f" PR #{p['number']} {label}: {p['head']['ref']} → {p['base']['ref']}")
    print("Advisory only. Commit age is not inactivity proof; no deletion or release authority.")
    return 0


def collision(pr_number: int) -> int:
    pulls = paged("/pulls?state=open")
    subject = next((p for p in pulls if p["number"] == pr_number), None)
    if subject is None:
        raise RuntimeError(f"Open PR #{pr_number} not found")
    mine = paths_for_pr(pr_number)
    print(f"TMT PR COLLISION ADVISORY: PR #{pr_number}, {len(mine)} changed paths")
    found = False
    for other in pulls:
        if other["number"] == pr_number:
            continue
        if other["base"]["ref"] != subject["base"]["ref"]:
            continue
        common = overlap(mine, paths_for_pr(other["number"]))
        if common:
            found = True
            print(f" OVERLAP with PR #{other['number']}: " + ", ".join(common))
    if not found:
        print("No exact changed-path overlap with other open same-base PRs.")
    print("Advisory only; cross-base changes, semantic conflicts and frozen donors need review.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inventory", "collision"))
    parser.add_argument("--pr", type=int)
    args = parser.parse_args()
    try:
        if args.command == "inventory":
            return inventory(Path(__file__).resolve().parents[1])
        if not args.pr or args.pr <= 0:
            parser.error("collision requires --pr <positive-number>")
        return collision(args.pr)
    except (OSError, ValueError, KeyError, RuntimeError, urllib.error.URLError) as exc:
        print("Read-only lifecycle report failed closed: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
