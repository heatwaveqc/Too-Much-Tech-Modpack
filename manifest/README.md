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

All 102 previously surveyed tech and TMM food/QoL entries now carry `targeted_inclusion:true`. Their `selection_state` is `targeted`, `targeted` for Ender IO **and dependent Evolution addon**, or `conditional_target` where an actual 1.21.1 compatible release/artifact is missing or suspect. These are intended inclusions **not** packwiz pins; `packwiz_installed:false` stays true. Core mod Draconic Evolution and independent Thermal-inspired FACTAS are explicit targets.

One of the 12 previously researched robot mods (**Cybernetics**) is now owner-targeted, leaving 11 unselected mob survey entries. Five cybernetic targets and one deferred shared TMM Progression engine are now also in the register. Do not equate a reported version with a downloaded hash-pinned mod.

### Dimension survey / Progression goals

20 dimension and procedural-space research entries have `selection_state: "unselected_dimension_survey"`, not an owner inclusion target, except preexisting Ad Astra. Their published version strings are source discovery only, not tested or pinned.

The new `manifest/progression-goals.json` locks a first-party **reuse target** for the TMM `compat/progression` engine and three **future** data-defined TMT paths (Cyborg, Meatbag, Alien). These are not runnable path data JSONs, skill trees, shared repo imports, grants or completed gameplay. Frozen TMM inspect SHA is provenance; import donor SHA must be reconfirmed after upstream core completion and owner QA contract.

## Dimension inclusion goals — 2026-11-20

The owner explicitly promoted seven dimensional entries from `unselected_dimension_survey` to `targeted`: **five primary** (`ad-astra-planets`, `stargate-journey`, `rftools-dimensions`, `infinite-dimensions`, `deep-space-unofficial-port`) and **two isolated-experiment** (`machina-mod`, `create-universe`). The `goal_phase` marks implementation priority and QA isolation, **not** an installed/approved runtime artifact or proof that the claimed feature exists. Thirteen remaining new dimension candidates remain research-only. Existing `ad-astra` target is unchanged. All seven have `packwiz_installed:false` until separately reviewed exact pins.
