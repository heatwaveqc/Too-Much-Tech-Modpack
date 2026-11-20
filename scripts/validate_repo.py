#!/usr/bin/env python3
"""Quick-only static metadata validation. Does not download mods or boot Minecraft."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import tomllib

ALLOWED_STATES = {"proposed", "researching", "approved", "pinned", "held", "excluded"}
HEX64 = re.compile(r"^[0-9a-fA-F]{64}$")
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


def read_toml(root: Path, rel: str, errors: list[str]) -> dict:
    try:
        return tomllib.loads((root / rel).read_text(encoding="utf-8"))
    except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"{rel}: {exc}")
        return {}


def safe_relpath(value: object) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and all(part not in {".", ".."} for part in value.split("/"))


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    pack = read_toml(root, "pack.toml", errors)
    index_spec = pack.get("index", {}) if isinstance(pack.get("index"), dict) else {}
    versions = pack.get("versions", {}) if isinstance(pack.get("versions"), dict) else {}

    if pack.get("pack-format") != "packwiz:1.1.0":
        errors.append("pack.toml: expected pack-format = packwiz:1.1.0")
    if not versions.get("minecraft") or not versions.get("neoforge"):
        errors.append("pack.toml: both Minecraft and NeoForge versions must be explicit")
    if index_spec.get("hash-format") != "sha256":
        errors.append("pack.toml: index hash-format must be sha256")

    index_path = index_spec.get("file")
    index: dict = {}
    if not safe_relpath(index_path):
        errors.append("pack.toml: unsafe/missing index path")
    else:
        path = root / index_path
        try:
            raw = path.read_bytes()
            actual = hashlib.sha256(raw).hexdigest()
            if index_spec.get("hash") != actual:
                errors.append(f"pack.toml: index checksum mismatch (expected {actual})")
            index = tomllib.loads(raw.decode("utf-8"))
        except (OSError, UnicodeDecodeError, ValueError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"{index_path}: {exc}")

    if index.get("hash-format") != "sha256":
        errors.append("index.toml: hash-format must be sha256")

    indexed_files: set[str] = set()
    entries = index.get("files", [])
    if not isinstance(entries, list):
        errors.append("index.toml: files must be an array")
        entries = []
    for n, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"index.toml: files[{n}] must be a table")
            continue
        rel = entry.get("file")
        if not safe_relpath(rel):
            errors.append(f"index.toml: files[{n}] unsafe path")
            continue
        if rel in indexed_files:
            errors.append(f"index.toml: duplicate file {rel}")
        indexed_files.add(rel)
        actual_path = root / rel
        if not actual_path.is_file():
            errors.append(f"index.toml: indexed file missing: {rel}")
            continue
        algorithm = entry.get("hash-format", index.get("hash-format"))
        checksum = entry.get("hash")
        if algorithm != "sha256" or not isinstance(checksum, str) or not HEX64.fullmatch(checksum):
            errors.append(f"index.toml: {rel} missing valid sha256 hash")
        elif hashlib.sha256(actual_path.read_bytes()).hexdigest().lower() != checksum.lower():
            errors.append(f"index.toml: checksum mismatch for {rel}")

    try:
        register = json.loads((root / "manifest/mods.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"manifest/mods.json: {exc}")
        return errors
    if not isinstance(register, dict) or register.get("schema_version") != 1:
        errors.append("manifest/mods.json: schema_version must be 1")
        return errors
    mods = register.get("mods")
    if not isinstance(mods, list):
        errors.append("manifest/mods.json: mods must be an array")
        return errors
    seen: set[str] = set()
    for n, mod in enumerate(mods):
        prefix = f"manifest/mods.json: mods[{n}]"
        if not isinstance(mod, dict):
            errors.append(f"{prefix} must be an object")
            continue
        mod_id = mod.get("id")
        if not isinstance(mod_id, str) or not ID_PATTERN.fullmatch(mod_id):
            errors.append(f"{prefix} requires a lowercase slug id")
        elif mod_id in seen:
            errors.append(f"{prefix} duplicate id: {mod_id}")
        else:
            seen.add(mod_id)
        if not isinstance(mod.get("name"), str) or not mod["name"].strip():
            errors.append(f"{prefix} missing name")
        if mod.get("status") not in ALLOWED_STATES:
            errors.append(f"{prefix} invalid status")
        url = mod.get("project_url")
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append(f"{prefix} needs canonical https project_url")
        # Target-selection is policy intent, not a provider/version pin.
        selected = mod.get("targeted_inclusion")
        if selected is not None and not isinstance(selected, bool):
            errors.append(f"{prefix} targeted_inclusion must be boolean")
        selection = mod.get("selection_state")
        accepted_states = {"targeted", "targeted_alternative", "conditional_target", "unselected_mob_survey", "unselected_dimension_survey", "unselected_biotech_survey"}
        if selection is not None and selection not in accepted_states:
            errors.append(f"{prefix} invalid selection_state")
        if selected is True and selection not in {"targeted", "targeted_alternative", "conditional_target"}:
            errors.append(f"{prefix} targeted entry needs compatible selection_state")
        if selected is False and selection in {"targeted", "targeted_alternative", "conditional_target"}:
            errors.append(f"{prefix} unselected entry cannot claim owner target")
        if selection == "conditional_target" and mod.get("status") != "held":
            errors.append(f"{prefix} conditional target must remain held")
        if selected is True and mod.get("packwiz_installed") is False and mod.get("status") == "pinned":
            errors.append(f"{prefix} status pinned conflicts with packwiz_installed false")
        if mod.get("packwiz_installed") is True and mod.get("status") != "pinned":
            errors.append(f"{prefix} installed index claim requires pinned status")
        if mod.get("status") == "pinned":
            if not isinstance(mod.get("version"), str) or not mod["version"].strip():
                errors.append(f"{prefix} pinned mod needs exact version")
            rel = mod.get("packwiz_file")
            if not safe_relpath(rel) or rel not in indexed_files:
                errors.append(f"{prefix} pinned mod needs packwiz_file in index.toml")
    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    errors = validate(repo_root)
    if errors:
        print("STATIC METADATA FAIL:")
        for error in errors:
            print(f" - {error}")
        return 1
    print("STATIC METADATA PASS — packwiz index and mod register only; Minecraft not run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
