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

## Additional owner-approved Create energy and nuclear targets (2026-11-22)

| Name | Verified release and source | Decision | Dependencies / integration QA |
| --- | --- | --- | --- |
| Create: New Age | https://www.curseforge.com/minecraft/mc-mods/create-new-age/files/8215216 — **1.2.0**, `create-new-age-1.2.0+neoforge-mc1.21.1.jar`, Minecraft 1.21.1 NeoForge | **APPROVED TARGET** | Electrical generators from kinetic coils and magnets, electric motors, energiser, cables, heat pipes, multiblock *nuclear reactors*, solar thermal. No petroleum refining / oil extraction in published feature list. Verify Create 6.0.10 compatibility; audit FE/kinetic conversion loops with Create Crafts & Additions. Reactor overheating/explosion and CC:Tweaked integration are version-relevant QA items. Author confirms Create Crafts & Additions compatibility in project FAQ; not a full TMT runtime test. |
| Create: Going Nuclear | https://www.curseforge.com/minecraft/mc-mods/going-nuclear — `goingnuclear-0.512-6.jar` for Minecraft 1.21.1 NeoForge 21.1.x (2026-10-30, **not** later 1.20.1 Forge artifact) | **APPROVED TARGET** | Uranium process chain, centrifuge enrichment, BWR/RBMK reactors, advanced physics, radiation, cooling, spent fuel and accident modes. Requires Create 6.0.x. Explicitly supports New Age via reactor heat port to New Age heat pipes and turbine FE output. Also optional integration with Mekanism uranium. Test radiation overlap, heat/energy transfer and destructive disaster modes; configure safer defaults before any multiplayer test. |

**Complementarity:** New Age is an electricity / heat and simpler nuclear system; Going Nuclear adds advanced fuel-cycle / operator / reactor physics and explicitly integrates with New Age heat pipes. The nuclear overlap is intentional, consistent with inclusive-first-pass, and should be assessed through configs and tests, not a reason to omit either target.

## Already targeted Create family (do not duplicate)

Read the actual live integration manifest before intake; 2026-11-22 `test/full-integration` survey already contains:

- Create (6.0.10), Create Crafts & Additions (1.7.2) — FE/kinetic bridge, Steam 'n' Rails Neoforge unofficial port (0.2.1).
- Create: Chromeware; Create: Biotech; Create: Bio-Chemical Genetics & Fermentation; Create: Bio-Factory (port); and Create: Universe, among other TMT targets.
- Existing port-specific dependencies and experimental status must be preserved. The survey record alone does not mean these are installed.

## Remaining Create add-on suggestions — **research only**, not owner selected

| Priority | Candidate | Verified 1.21.1 NeoForge metadata | TMT value / caveat |
| --- | --- | --- | --- |
| Medium / alternative nuclear | Create: Atomic | https://www.curseforge.com/minecraft/mc-mods/createatomic — 1.3.2 | Another Create multiblock nuclear / turbine option with radioisotope heat generation and meltdown mechanics. Distinct from New Age; overlap acceptable under inclusive survey policy. |
| Under consideration | Create: Diesel Generators | https://www.curseforge.com/minecraft/mc-mods/create-diesel-generators — latest seen 1.3.16, released 2026-11-21 | Crude oil pumpjacks and refining into gasoline/diesel plus combustion engines, fermenters, chemical sprayers/turrets, casting. **Not duplicative with New Age oil**: New Age does not include oil. Compare instead with Immersive Petroleum / other petroleum providers; check cross-mod fuel tags, engine balance and recipes before owner inclusion decision. |
| Not selected (existing alternatives) | Create Ore Excavation | https://www.curseforge.com/minecraft/mc-mods/create-ore-excavation — 1.6.8 | Already has substantial ore extraction alternatives across tech roster; no new selection, reconsider only for distinct useful mechanics. |
| Not selected (existing alternatives) | Create: Power Loader | https://www.curseforge.com/minecraft/mc-mods/create-power-loader — 2.0.5 | FTB Chunks already targeted for chunkloading; no new selection. Reconsider if persistent moving train chunkloading cannot be supplied by existing systems. |
| Medium | Create: Connected | https://www.curseforge.com/minecraft/mc-mods/create-connected — 1.3.3 | More mechanical/logistics building blocks and contraption options. |
| Medium | Create: Escalated | https://www.curseforge.com/minecraft/mc-mods/create-escalated — 1.3.2 | Rotation-powered escalators and walkways for factories/stations; check moving-player collision and server physics. |
| Medium | Create Railways Navigator | https://www.curseforge.com/minecraft/mc-mods/create-railways-navigator — 0.9.1 beta | Schedules, route-finding and stations; assess against unofficial Steam 'n' Rails port. |
| Medium | Create: Enchantment Industry | https://www.curseforge.com/minecraft/mc-mods/create-enchantment-industry — 2.5.4b for Create 6.0.10 | Automate XP/enchanting; optional tech-facing fantasy overlap. |
| Medium | Create Slice & Dice | https://www.curseforge.com/minecraft/mc-mods/slice-and-dice — 4.3.4 | Link Create with Farmer's Delight food processing and automation. |
| Low / decorative | Create Deco | https://www.curseforge.com/minecraft/mc-mods/create-deco — 2.1.3 | Industrial/urban building. |
| Low / decorative | Create: Copycats+ | https://www.curseforge.com/minecraft/mc-mods/copycats — 3.0.11 | Build-shaping and disguises for industrial machinery. |

The following is deliberately **held for version verification**, not silently approved: Create: The Factory Must Grow (https://www.curseforge.com/minecraft/mc-mods/create-industry). Its source listing presents releases with ambiguous `1.21` filename but `1.20.1` metadata; do not claim a verified 1.21.1 NeoForge artifact without inspecting the exact file.

## Integration handoff

1. Integration writer records the **five owner approvals** (Scorched Guns 2, Gunsmithing, Big Cannons, New Age, Going Nuclear) in canonical `docs/DECISIONS.md` and `manifest/mods.json`, preserving explicit target-vs-installed distinction and avoiding duplicate Create entry.
2. Research exact published 1.21.1/NeoForge mod files and transitive JAR dependencies; compare Scorched Guns 2 unofficial ports, select one, verify license/provenance.
3. Lock hashes and packwiz entries through shared-path ownership and normal PR review only; no compilation/server/smoke/Prism build without the required per-run owner authorization.
4. Test unusual risks: duplicate gun registries, ammo generation/crafting, Create dependency mix, artillery destruction and chunk safety, Scorched Guns mobs/raids, client controls, dedicated server stability; plus New Age nuclear heat/energy compatibility, FE-to-kinetic loops, Going Nuclear radiation/world-destruction configuration, multiblock steam / spent-fuel lifecycle and save/reload reliability.
5. Keep all other suggested addons as **research-only** (Diesel Generators under comparison, Ore Excavation and Power Loader not selected given existing alternatives) until a later explicit owner inclusion decision.
