# CelesTech — high-priority alpha inclusion target

**Reviewed and owner-selected: 2026-11-21.** TMT target: **Minecraft 1.21.1 · NeoForge 21.1.265 · Java 21**. Intended inclusion only; none of the artifacts below is pinned/downloaded or run in the TMT pack. **Priority: high. QA: isolated-alpha first.** This is not a sixth core prerequisite.

## Publisher release and dependency evidence

| Role | Provider | Published research snapshot |
| --- | --- | --- |
| High-priority tech mod | [CelesTech by RushOnly](https://www.curseforge.com/minecraft/mc-mods/celestech) | [0.1.4 alpha, file ID 9741328](https://www.curseforge.com/minecraft/mc-mods/celestech/files/9741328); published November 21, 2026; exact file `celestech-0.1.4-alpha-1.21.1-neoforge.jar` |
| Required library | [GeckoLib](https://www.curseforge.com/minecraft/mc-mods/geckolib) | [NeoForge 1.21.1 4.9.3, file ID 8893490](https://www.curseforge.com/minecraft/mc-mods/geckolib/files/8893490) — meets the author's GeckoLib 4.9.3+ minimum |
| Optional integrations | [JEI](https://www.curseforge.com/minecraft/mc-mods/jei), [Curios](https://www.curseforge.com/minecraft/mc-mods/curios) and [Flywheel](https://www.curseforge.com/minecraft/mc-mods/flywheel) | JEI = recipe display, Curios = Neural Visor slot; Flywheel **not required** by 0.1.4 even though older 0.1.x versions had an erroneous dependency. Existing targeted JEI/Curios should be reused, not duplicated. |

CelesTech's project lists Java 21, NeoForge 21.1+ and **client & server**; the earliest file documentation specifies NeoForge 21.1.264+, within our 21.1.265 target. Its CurseForge license is **All Rights Reserved**, but its public FAQ says *yes* to inclusion in a modpack. Do a license/packaging verification before distribution rather than inferring broad rights to fork or redistribute source/assets.

## What makes it a TMT candidate

- **Stellar energy:** star radar, cannon, harvest stellar matter, nebula condensers and star-building machinery, 16 astronomical objects over 5 tiers, black-hole production and a late-game Penrose engine.
- **Rocket-powered resources:** renewable asteroid-mining missions with resource-return cargo and liquid-hydrogen/oxygen preparation; note this is not necessarily the same as an explorable Ad Astra destination.
- **Factory engineering:** multiblock holographic assemblers, configurable machines, kinetic-looking fabricator arms, ore processes and tiered FE infrastructure.
- **Automated defense:** combat drone hangars and player-protection AI.
- **Cybernetics:** surgery chair, eight implant regions and 40+ implant options, Neural Visor HUD.
- **Universe visuals:** replacement live night sky, stars shared between multiplayer observers, radar targets and galactic effects.

Owner asked for a **high-priority technology candidate**, not to replace Ad Astra, Mekanism, Draconic Evolution, or existing cyberware. Feature overlap is welcome. Preserve interesting distinctions and test where mechanisms genuinely collide.

## Early-alpha status and current known bugs

Version 0.1.4's publisher notes fixes for a Flywheel incompatibility, JEI naming, cable network throughput, multiplayer sky consistency, rocket cargo, holographic assembly and other rendering/processing defects, with provisional solar/star balance. Open issues remain around transparent blocks near charger, Dwarf Reactor textures, shipyard cable/assembly effects, and other visual/shadow/monitor behavior. Do not claim that these reports are resolved or the mod is production-stable. New alpha releases can change processing and quest balance rapidly.

## Isolated test acceptance checklist (not executed)

1. **Artifact/dependency review (A):** resolve exact NeoForge file IDs/metadata/hash and full Maven/JAR dependency set, shared GeckoLib version, NeoForge minimum and client/server side; no duplicate GeckoLib/Flywheel jars; verify pack distribution license.
2. **Minimal dedicated boot (requires future owner authorization):** CelesTech + GeckoLib alone, then with JEI/Curios, then with Ad Astra + other space/sky mods; catch renderer classloading, optional Flywheel, handshake/config synchronization and dimension transitions.
3. **Astronomy/sky:** in a multiplayer world, verify star radar targeting, stellar cannon impact events, saved sky targets and synchrony after rejoin; assess shaders and night-sky replace behavior with Ad Astra planets, custom worlds and optional Starfield-like systems.
4. **Industrial production:** validate resource outputs, stellar generation, server-side FE balances, nebula machines, hologram assembly and break/rebuild, cargo persistence, multi-chunk factory operations, storage insert/extract, and JEI recipe visibility.
5. **Cybernetic state:** implant slot registration, death and respawn, dimension travel, armor/model overlays, entity polymorphism and body changes with NeoSync, Synthetics, Cybernetics, Chromeware and eventual Cyborg/Meatbag/Alien Progression.
6. **Security and game performance:** drone AI in claimed chunks, hostilities/spawn rules, remote mining renewable economy, server ticks/large visuals/multiple multiblocks, no item loss or dupes during chunk unloading.
7. **Exit criteria:** only after isolated client/server and gameplay evidence review should integration consider a packwiz pin/combined pack candidate. A green static CI alone does not fulfill this.

## Integration state

- Registry `celestech`: `approved` + `targeted`, `priority:"high"`, `goal_phase:"isolated-experiment"`, `packwiz_installed:false`.
- Registry `geckolib`: mandatory shared library; version-qualified 4.9.3 NeoForge, not a separate gameplay mod.
- No authorized full build or in-game test, no actual mod downloads, no packwiz `index.toml` changes and no production release.
