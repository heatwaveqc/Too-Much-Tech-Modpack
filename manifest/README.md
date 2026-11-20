# Mod intake register

`mods.json` records **research and approval state**, not a downloadable mod inventory. The 2026-11-20 survey adds core tech approvals and proposed TMM food/QoL carryover **without** adding any packwiz files. Packwiz `index.toml` is the source of truth for files that would actually be included in a build.

Example record (illustrative; NOT an approved mod):

```json
{
  "id": "example-mod",
  "name": "Example Mod",
  "status": "researching",
  "source": "modrinth",
  "project_url": "https://modrinth.com/mod/example-mod",
  "notes": "Verify NeoForge and exact Minecraft release"
}
```

Allowed `status` values: `proposed`, `researching`, `approved`, `pinned`, `held`, `excluded`.
For a `pinned` entry, require `version` and `packwiz_file`, with that metadata path already listed in `index.toml`. Additional research keys (`survey_version`, `release_channel`, `carryover_priority`, `tmm_observed_version`, `tmm_index_path_detected`) are descriptive snapshots, **not** install authorization, resolved source hashes or proof of active TMT pins. Additional keys are allowed for dependencies, file IDs, license, approval issue/decision, load side, SHA-256 and QA results. Do not confuse a `pinned` entry with a boot-tested mod.

Use `python3 scripts/validate_repo.py` locally and the GitHub `Quick checks` job on PRs. Co-edit register and packwiz on one integration-writer branch to avoid collisions.

## Owner target flags (2026-11-20)

All 102 previously surveyed tech and TMM food/QoL entries now carry `targeted_inclusion:true`. Their `selection_state` is `targeted`, `targeted_alternative` for competing Ender IO implementations, or `conditional_target` where an actual 1.21.1 compatible release/artifact is missing or suspect. These are intended inclusions **not** packwiz pins; `packwiz_installed:false` stays true. Core mod Draconic Evolution and independent Thermal-inspired FACTAS are explicit targets.

The 12 newly researched robot/cybernetic mob entries have `targeted_inclusion:false` and are not approved by the user's request for an initial survey. Do not equate a reported version with a downloaded hash-pinned mod.
