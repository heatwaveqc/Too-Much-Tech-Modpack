#!/usr/bin/env python3
"""TMT quick preflight: local read-only schema/provenance checks; NO assembly."""
from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
import re
import sys

SHA40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
SLUG = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
FEATURE_STATES = {
    "proposed", "in_development", "source_ready", "in_qa", "blocked",
    "not_built", "gameplay_pass", "owner_deferred",
}
INCLUSION_STATES = {"pending", "included", "blocked", "owner_deferred"}


def safe_path(value: object) -> bool:
    if not isinstance(value, str) or not value or "\\" in value or "*" in value:
        return False
    p = PurePosixPath(value)
    return not p.is_absolute() and all(part not in ("", ".", "..") for part in value.split("/"))


def load(root: Path, path: str, errors: list[str]) -> object:
    try:
        return json.loads((root / path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append(f"{path}: {exc}")
        return {}


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    sources = load(root, "manifest/integration-sources.json", errors)
    if not isinstance(sources, dict) or sources.get("schema") != 1:
        errors.append("integration-sources: schema must be 1")
        sources = {}
    if sources.get("baseline") != "test/full-integration" or sources.get("channel") != "integration":
        errors.append("integration-sources: unexpected baseline/channel")
    streams = sources.get("streams", [])
    if not isinstance(streams, list):
        errors.append("integration-sources: streams must be a list")
        streams = []
    names: set[str] = set()
    owned: dict[str, str] = {}
    for n, stream in enumerate(streams):
        name = f"streams[{n}]"
        if not isinstance(stream, dict):
            errors.append(f"{name}: must be an object")
            continue
        key = stream.get("name")
        if not isinstance(key, str) or not SLUG.fullmatch(key) or key in names:
            errors.append(f"{name}: missing, invalid or duplicate name")
        else:
            names.add(key)
        sha = stream.get("source_commit")
        if not isinstance(sha, str) or not SHA40.fullmatch(sha):
            errors.append(f"{name}: source_commit must be immutable lowercase 40-hex")
        if not isinstance(stream.get("branch"), str) or not stream["branch"].strip():
            errors.append(f"{name}: missing branch provenance")
        if not isinstance(stream.get("mode"), str) or not stream["mode"].strip():
            errors.append(f"{name}: missing mode")
        if not isinstance(stream.get("note"), str) or not stream["note"].strip():
            errors.append(f"{name}: source handoff needs note")
        integrated = stream.get("integrated_into_baseline")
        if not isinstance(integrated, bool):
            errors.append(f"{name}: integrated_into_baseline must be boolean")
        elif integrated and stream.get("branch") != "test/full-integration":
            errors.append(f"{name}: baseline-integrated source must name integration branch")
        paths = stream.get("paths")
        if not isinstance(paths, list) or not paths:
            errors.append(f"{name}: paths must be a nonempty list")
            continue
        for path in paths:
            if not safe_path(path):
                errors.append(f"{name}: unsafe or wildcard path {path!r}")
                continue
            if path in owned and owned[path] != key:
                errors.append(f"{name}: duplicate path owner {path} (also {owned[path]})")
            owned[path] = str(key)
    for kind, key in (("feature-checklist", "features"), ("live-test-inclusion", "features")):
        manifest = f"manifest/{kind}.json"
        doc = load(root, manifest, errors)
        if not isinstance(doc, dict) or doc.get("schema_version") != 1:
            errors.append(f"{manifest}: schema_version must be 1")
            continue
        rows = doc.get(key)
        if not isinstance(rows, list):
            errors.append(f"{manifest}: {key} must be a list")
            continue
        seen: set[str] = set()
        for i, row in enumerate(rows):
            loc = f"{manifest}: {key}[{i}]"
            if not isinstance(row, dict):
                errors.append(f"{loc}: must be object")
                continue
            fid = row.get("id")
            if not isinstance(fid, str) or not SLUG.fullmatch(fid) or fid in seen:
                errors.append(f"{loc}: id missing, invalid or duplicate")
            else:
                seen.add(fid)
            if not isinstance(row.get("title"), str) or not row["title"].strip():
                errors.append(f"{loc}: title missing")
            state = row.get("status")
            allowed = FEATURE_STATES if kind == "feature-checklist" else INCLUSION_STATES
            if state not in allowed:
                errors.append(f"{loc}: invalid status")
            if kind == "feature-checklist" and state == "gameplay_pass":
                if not isinstance(row.get("evidence_url"), str) or not row["evidence_url"].startswith("https://"):
                    errors.append(f"{loc}: gameplay_pass needs evidence_url")
                if not isinstance(row.get("tested_commit"), str) or not SHA40.fullmatch(row["tested_commit"]):
                    errors.append(f"{loc}: gameplay_pass needs exact tested_commit")
            if kind == "live-test-inclusion" and state in {"blocked", "owner_deferred"}:
                if not isinstance(row.get("reason"), str) or not row["reason"].strip():
                    errors.append(f"{loc}: blocked/deferred needs reason")
                if state == "owner_deferred" and (
                    not isinstance(row.get("owner_approval_url"), str)
                    or not row["owner_approval_url"].startswith("https://")
                ):
                    errors.append(f"{loc}: owner_deferred needs owner_approval_url with https evidence")
            if kind == "live-test-inclusion" and state == "included":
                if not isinstance(row.get("candidate_commit"), str) or not SHA40.fullmatch(row["candidate_commit"]):
                    errors.append(f"{loc}: included needs frozen candidate_commit")
    releases = load(root, "manifest/release-registry.json", errors)
    if not isinstance(releases, dict) or releases.get("schema_version") != 1:
        errors.append("release-registry: schema_version must be 1")
    else:
        if releases.get("integration_branch") != "test/full-integration":
            errors.append("release-registry: invalid integration_branch")
        if not isinstance(releases.get("releases"), list):
            errors.append("release-registry: releases must be a list")
        for channel in ("candidate", "stable"):
            item = releases.get(channel)
            if item is not None:
                if not isinstance(item, dict):
                    errors.append(f"release-registry: {channel} must be object or null")
                else:
                    if not isinstance(item.get("source_commit"), str) or not SHA40.fullmatch(item["source_commit"]):
                        errors.append(f"release-registry: {channel} requires exact source_commit")
                    if not isinstance(item.get("sha256"), str) or not HEX64.fullmatch(item["sha256"]):
                        errors.append(f"release-registry: {channel} requires artifact sha256")
                    if not isinstance(item.get("evidence_url"), str) or not item["evidence_url"].startswith("https://"):
                        errors.append(f"release-registry: {channel} requires evidence_url")
    return errors


def main() -> int:
    errors = validate(Path(__file__).resolve().parents[1])
    if errors:
        print("INTEGRATION SOURCE PREFLIGHT FAILED (LOCAL SCHEMA ONLY):")
        for error in errors:
            print(" - " + error)
        return 1
    print("INTEGRATION SOURCE PREFLIGHT PASS (LOCAL SCHEMA ONLY; donor reachability not tested; Minecraft not run)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
