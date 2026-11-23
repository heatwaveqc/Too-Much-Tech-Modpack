# Guns and Create addons — owner selection and 1.21.1 NeoForge survey (2026-11-22)

## Status and scope

**Owner-selected inclusion targets** below were explicitly approved 2026-11-22. They are selected for Too Much Tech (TMT), **not** installed, indexed, hash-locked, boot-tested or guaranteed mutually compatible. This page is an isolated handoff to the designated integration writer. Do **not** edit `manifest/mods.json`, `docs/DECISIONS.md`, packwiz files, or run a full build from this research branch. The integration writer should promote the approved selections into the canonical owner register and lock only after exact artifact and dependency review.

The target platform is the provisional Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21 stack; Create 6.0.10 is already targeted in the integration register.

## New owner-approved weapon targets

| Name | Candidate source / provider evidence | Selection | Integration prerequisites / concerns |
| --- | --- | --- | --- |
| Scorched Guns 2 | Unofficial Scorched Guns 0.5.5 port: https://www.curseforge.com/minecraft/mc-mods/scorched-guns-2-0-5-5-unofficial-port (updated 2026-11-22, latest provider-listed `scguns-1.1.6.1.jar`); competing unofficial port https://modrinth.com/mod/scorched-guns-neoforged/version/1.5 | **APPROVED TARGET**, choose **one** port, not both | Compare provenance/permission, mod IDs, content parity, maintenance, version metadata, server safety, dependencies, mobs/raids, firearms/ammunition, block damage and performance before exact pin. Source releases do not establish TMT runtime safety. |
| Create: Gunsmithing | https://www.curseforge.com/minecraft/mc-mods/cgs (provider-listed `create-gunsmithing-1.21.1-1.4.9.jar`, 2026-07-24) | **APPROVED TARGET** | Verify target JAR dependencies (including any gun library) against Create 6.0.10, conflicts with Scorched Guns, recipes and server behavior. |
| Create Big Cannons | https://www.curseforge.com/minecraft/mc-mods/create-big-cannons (provider-listed v5.11.7 for NeoForge 1.21.1 and Create 6.0.7+) | **APPROVED TARGET** | Required Ritchie's Projectile Library; evaluate compatible version, cannon assembly, projectiles, chunk/entity damage, logistics, multiplayer and stability. |

These approvals are for inclusion subject to hard compatibility gates, following TMT's inclusive-first-pass policy. Ammo manufacturing / automation and tech-boss scaling are possible cross-mod balancing work; not newly approved gameplay rules.

## Already targeted Create family (do not duplicate)

Read the actual live integration manifest before intake; 2026-11-22 `test/full-integration` survey already contains:

- Create (6.0.10), Create Crafts & Additions (1.7.2) — FE/kinetic bridge, Steam 'n' Rails Neoforge unofficial port (0.2.1).
- Create: Chromeware; Create: Biotech; Create: Bio-Chemical Genetics & Fermentation; Create: Bio-Factory (port); and Create: Universe, among other TMT targets.
- Existing port-specific dependencies and experimental status must be preserved. The survey record alone does not mean these are installed.

## New Create add-on suggestions — **research only**, not owner selected

| Priority | Candidate | Verified 1.21.1 NeoForge metadata | TMT value / caveat |
| --- | --- | --- | --- |
| High / specialized | Create: Going Nuclear | https://www.curseforge.com/minecraft/mc-mods/going-nuclear — 1.21.1 NeoForge artifact `goingnuclear-0.512-6.jar` (2026-10-30) | Detailed Create-based uranium refining/enrichment, BWR/RBMK layouts, shielding/dose physics, instrumentation, spent fuel and configurable accidents; research only, test server load/world destruction and overlap with other reactors/radiation systems. |
| Medium / alternative nuclear | Create: Atomic | https://www.curseforge.com/minecraft/mc-mods/createatomic — 1.3.2 | Another Create multiblock nuclear / turbine option with radioisotope heat generation and meltdown mechanics. Distinct from New Age; overlap acceptable under inclusive survey policy. |
| High | Create: Diesel Generators | https://www.curseforge.com/minecraft/mc-mods/create-diesel-generators — latest seen 1.3.16, released 2026-11-21 | Crude-oil refining and diesel engines; verify competing petroleum systems and recipes. |
| High | Create: New Age | https://www.curseforge.com/minecraft/mc-mods/create-new-age — 1.2.0 | Electricity/electromagnetic machinery; audit energy bridge loops alongside Create Crafts & Additions. |
| High | Create Ore Excavation | https://www.curseforge.com/minecraft/mc-mods/create-ore-excavation — 1.6.8 | Kinetic, automated deposit extraction; audit resource abundance and ore/material compatibility. |
| High | Create: Power Loader | https://www.curseforge.com/minecraft/mc-mods/create-power-loader — 2.0.5 | Contraption/train chunk loading; test server memory, claim rules, forced-chunk limits. |
| Medium | Create: Connected | https://www.curseforge.com/minecraft/mc-mods/create-connected — 1.3.3 | More mechanical/logistics building blocks and contraption options. |
| Medium | Create: Escalated | https://www.curseforge.com/minecraft/mc-mods/create-escalated — 1.3.2 | Rotation-powered escalators and walkways for factories/stations; check moving-player collision and server physics. |
| Medium | Create Railways Navigator | https://www.curseforge.com/minecraft/mc-mods/create-railways-navigator — 0.9.1 beta | Schedules, route-finding and stations; assess against unofficial Steam 'n' Rails port. |
| Medium | Create: Enchantment Industry | https://www.curseforge.com/minecraft/mc-mods/create-enchantment-industry — 2.5.4b for Create 6.0.10 | Automate XP/enchanting; optional tech-facing fantasy overlap. |
| Medium | Create Slice & Dice | https://www.curseforge.com/minecraft/mc-mods/slice-and-dice — 4.3.4 | Link Create with Farmer's Delight food processing and automation. |
| Low / decorative | Create Deco | https://www.curseforge.com/minecraft/mc-mods/create-deco — 2.1.3 | Industrial/urban building. |
| Low / decorative | Create: Copycats+ | https://www.curseforge.com/minecraft/mc-mods/copycats — 3.0.11 | Build-shaping and disguises for industrial machinery. |

The following is deliberately **held for version verification**, not silently approved: Create: The Factory Must Grow (https://www.curseforge.com/minecraft/mc-mods/create-industry). Its source listing presents releases with ambiguous `1.21` filename but `1.20.1` metadata; do not claim a verified 1.21.1 NeoForge artifact without inspecting the exact file.

## Integration handoff

1. Integration writer records the **three owner approvals** in canonical `docs/DECISIONS.md` and `manifest/mods.json`, preserving explicit target-vs-installed distinction and avoiding duplicate Create entry.
2. Research exact published 1.21.1/NeoForge mod files and transitive JAR dependencies; compare Scorched Guns 2 unofficial ports, select one, verify license/provenance.
3. Lock hashes and packwiz entries through shared-path ownership and normal PR review only; no compilation/server/smoke/Prism build without the required per-run owner authorization.
4. Test unusual risks: duplicate gun registries, ammo generation/crafting, Create dependency mix, artillery destruction and chunk safety, Scorched Guns mobs/raids, client controls, dedicated server stability.
5. Keep all further suggested addons as **research-only** until a later explicit owner inclusion decision.
