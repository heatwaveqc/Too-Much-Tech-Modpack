# Mod intake and compatibility evidence

**Current installed mods: none.** This page describes the evidence required before installing a candidate. The machine-readable register is [manifest/mods.json](../manifest/mods.json).

## Candidate review

For each candidate, record the canonical project URL, provider (Modrinth/CurseForge/GitHub/other), exact file/version, Minecraft version, loader/build compatibility, client/server side, dependencies and conflicts, source license and redistribution conditions, provenance, and explicit owner approval status.

Prefer primary release pages and changelogs. Verify the *specific* version: "NeoForge available" for a different Minecraft version is not evidence of compatibility with this pack. When adding mods, calculate transitive dependencies and review known incompatibilities and bundled libraries. Avoid redundant mod overlap unless designed and approved.

Research states are `proposed`, `researching`, `approved`, `pinned`, `held`, `excluded`. Only `pinned` means indexed as a packwiz file; it is still not verified by launching the game. A pinned record must include `version` and `packwiz_file`; the repository validator verifies that the file is indexed. Full gameplay confidence comes only from level-specific test evidence.

## Shared fixes and other projects

Too Much Magic is a useful workflow and potential compatibility reference, **not** an automatic mod donor or authority for Too Much Tech's choices. Reuse open code/config only after reviewing ownership, functionality, version and applicable license. Any cross-pack custom library should have an explicit maintenance owner and release/pinning policy.

## Update policy

Before an explicitly authorized full assembly or release, survey the *active* packwiz roster and compatible upstream update candidates, including dependencies. Record update/hold/up-to-date/unknown and why. Do not fetch "latest" dynamically inside a frozen build. Pin exact versions and preserve rollback evidence.
