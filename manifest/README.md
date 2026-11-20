# Mod intake register

`mods.json` records **research and approval state**, not a downloadable mod inventory. Initially the `mods` array is empty. Packwiz `index.toml` is the source of truth for files that would actually be included in a build.

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
For a `pinned` entry, require `version` and `packwiz_file`, with that metadata path already listed in `index.toml`. Additional keys are allowed for dependencies, file IDs, license, approval issue/decision, load side, SHA-256 and QA results. Do not confuse a `pinned` entry with a boot-tested mod.

Use `python3 scripts/validate_repo.py` locally and the GitHub `Quick checks` job on PRs. Co-edit register and packwiz on one integration-writer branch to avoid collisions.
