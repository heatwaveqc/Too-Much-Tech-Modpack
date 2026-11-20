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

## Research ledgers (2026-11-20)

- [Technology mods and 1.21.1 release evidence](research/TECH-MODS-2026-11-20.md) — 42 prospects including the four owner-selected core mods and explicit Thermal hold.
- [TMM food/QoL carryover intake](research/TMM-FOOD-QOL-CARRYOVER-2026-11-20.md) — 56 donor records, historical TMM versions and pitfalls.
- [Machine-readable research register](../manifest/mods.json) — current statuses: approved core, researching candidates, held mismatches. This research file is **not** an installed-mod index.

Any TMT packwiz pin requires separate exact current source artifact, hash, dependencies, client/server side, redistribution check and reviewed integration PR. TMM's current integration files are an important provenance input but do not grant automatic compatibility or runtime PASS. The next comprehensive build must honor live-test inclusion and owner authorization rules.

## Selected cyberware and themed dimensions — 2026-11-20

Five additional selected systems: Cybernetics, Synthetics, Matter Overdrive (Unofficial Port as tentative single implementation), NeoSync, Create: Chromeware. **Overlap itself is allowed.** Compare actual mod IDs/dependencies, player save attachment ownership, avatar/shell cloning, death and resurrection, accelerated effects, and rendering/client hooks. The only upfront exclusion is incompatible artifacts or conflicting *implementations of the same mod*; ordinary gameplay overlap is deferred to runtime/balance testing.

[Dimension survey](research/THEMATIC-DIMENSIONS-2026-11-20.md) distinguishes Ad Astra's data-defined custom destinations and seeded terrain from runtime-created new dimensions. Its extra 20 research-only entries are not installed or preapproved. Even confirmed version support does not prove that two dimensions can coexist safely or preserve existing worlds.

[Shared Progression target](../manifest/progression-goals.json) records a future reviewed source reuse only; the TMM core remains in development and should not be copied or built until frozen and authorized.

## Broad biotechnology target and magitech review — 2026-11-20

All 24 compatible-version biotechnology candidates were promoted to owner targets, but there are hard technical gates for two **alternative Biomancy implementation JARs** and the held 1.20.1 Fabric-only **NEEPMeat**. Do not exclude other genetics mods solely for functional overlap. Test disease propagation, entity genome serialization, cybernetic and synthetic body transfers, stable saves, metabolism/food handling and automation integration. Beta/alpha mods go through isolated QA first when risks warrant.

Botania Revived and the Embers 1.21.1 NeoForge port options are recommended research-only, not owner-selected. The **two Embers ports** may share original Embers mod IDs/content; choose one actual JAR implementation after verification. Botania Revived has its own recipe/energy automation and potential compatibility considerations with Productive Bees and claims automation; no cross-mod magic gate should be imposed on TMT's mainstream machine progression without explicit decision. [Magitech assessment](research/TECH-FIRST-MAGITECH-2026-11-20.md).

## Boss fights, enemy encounters and selected optional magitech — 2026-11-20

Botania Revived and preferred Embers Re-Ignited are now owner targets; Embers Reborn stays unselected as an alternative port that likely conflicts with Re-Ignited's mod identity. Verify both selected ports against actual NeoForge 1.21.1 release artifacts, dependencies, original licenses and 1.21.1 server runtime before pinning.

[Boss survey](research/BOSS-AND-ENCOUNTERS-2026-11-20.md) covers 18 additional **unselected** candidate mods. Validate biome/structure placement, modded drops, generated arenas, boss resummoning, compatibility with ranged/energy weapons, boss bar IDs, dedicated server packet behavior and fight attribution. For mob mutation/boss affix frameworks (Apotheosis, Brutal Bosses, Mob Champions), avoid triple multipliers or infinite elite spawn farms as unintended errors—use native configs when available. TMT's inclusive selection policy still applies: overlapping encounters are not automatically excluded.

The two Alex's Caves NeoForge port candidates have likely duplicate registry/mod IDs, so choose at most one actual binary for a real pack; this is an implementation conflict, not an argument against cave bosses. The Twilight Forest final boss addon explicitly depends on matching Twilight Forest versions; pairing is normal.

## Industrial and science-fiction bosses — 2026-11-20

[Focused report](research/TECH-HEAVY-BOSSES-2026-11-20.md) adds ten provider-listed NeoForge 1.21.1 tech-coded encounters and four old-version holds. No JAR installed. Mechafauna (already in the robot-mob survey) has a genuinely multipart Mothership: verify whether projectiles/explosives, lasers, weaponized drones and machine defenses can target independently destructible weapon components. Hostile Civilization introduces item-stealing and player-carrying drones/raids, so test protected base/chunk claims, equipment recovery and server-owner settings. Gearworld adds bespoke inverted gravity and FM/FE power with experimental multiplayer and unplayed boss fights. Stellix has six giant alien-world titans, and Thermal Shock registers extensive new entity/world content. All are genuine technical QA hazards, not reasons to drop an otherwise fun mod for merely overlapping content. RIFTFALL, MechMonstrosity, Mecha Pillager and Exo Mechs are version-blocked (Forge 1.20.1 or older, no verified 1.21.1 NeoForge port), so must remain research-only.
