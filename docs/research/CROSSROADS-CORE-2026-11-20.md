# Crossroads — fifth core technology selection and integration plan

**Owner selection: 2026-11-20.** Platform target **Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21**. Crossroads is a **core gameplay system**, not optional, a surveyed-only project, or another generic FE machine tier. Its recommended runtime files are *candidate provider releases*, and neither packwiz JARs nor client/server launches have been performed.

## Selected project files and identity

| Role | Project | Release evidence | Current state |
| --- | --- | --- | --- |
| **Fifth core mod** | [Crossroads MC](https://www.curseforge.com/minecraft/mc-mods/crossroads-mc), by Technomancer_isTaken | [crossroads-1.21.1-2.12.1.jar](https://www.curseforge.com/minecraft/mc-mods/crossroads-mc/files/9386883), 2026-10-31, **1.21.1 NeoForge** | `approved/targeted`, unpinned |
| **Required dependency** | [Essentials, by Technomancer](https://www.curseforge.com/minecraft/mc-mods/essentials) | [essentials-1.21.1-2.17.6.jar](https://www.curseforge.com/minecraft/mc-mods/essentials/files/8384593); Crossroads 2.11.8+ requires Essentials 2.17.6+ | `approved/targeted`, unpinned |
| **User-selected in-game guidebooks** | [Patchouli](https://www.curseforge.com/minecraft/mc-mods/patchouli) | [Patchouli-1.21.1-93-NEOFORGE.jar](https://www.curseforge.com/minecraft/mc-mods/patchouli/files/7730942) | `approved/targeted`, unpinned |

**Important:** `Essentials` above is **not** [FTB Essentials](https://www.curseforge.com/minecraft/mc-mods/ftb-essentials-forge). Both can be considered independently. Crossroads upstream labels Patchouli an **optional dependency** because its mod functions without the books; **the TMT owner explicitly requests it**, so the pack target includes the guidebooks.

## Preserve the unusual engineering

- **Heat:** design thermal transport, heat gradients and thermal limits, rather than blanket FE replacements.
- **Rotary power:** gear ratios, speed and torque, physical couplings and failure mechanics.
- **Steam:** native thermal-mechanical conversion, independent of conventional RF/FE behavior.
- **Beams and beacon machines:** optical extraction, redirection/reflection, splitters, alignment combinations, the Beacon Harness and late-game technomancy.
- **Ore processing and alchemy:** deliberately distinct multistage chemical engineering with hazard mechanics and resource production. Avoid forced grind outside native systems.
- **Bioengineering:** an independent creative approach to live organisms, complementary to TMT's other targeted biotech.
- **Three native specialization paths:** Alchemy, Technomancy, Bioengineering. The Crossroads [Path introduction](https://github.com/Crossroads-Development/Crossroads/blob/1.21/src/main/resources/python/docs/src/en_us/entries/intro/path.json) says the first specialization normally unlocks in **late midgame** after discovering beam alignments; normally only one initially, with additional paths earned via advancements (configurable). This is NOT the future TMT first-party character specialization set (Cyborg/Meatbag/Alien). Preserve native configs and path distinctions until playtesting, with no owner-approved override yet.

## Atmospheric FE: distinctive native infrastructure

[Original Crossroads in-game manual source](https://github.com/Crossroads-Development/Crossroads/blob/1.21/src/main/resources/python/docs/src/en_us/entries/alchemy/atmos_fe.json) documents the **Atmospheric Attenuator** (registry item `crossroads:atmos_charger`), with four vanilla lightning rods stacked over it:

- **One shared, server-wide reservoir**, referenced through overworld SavedData even when operating in another dimension ([source](https://github.com/Crossroads-Development/Crossroads/blob/1.21/src/main/java/com/Da_Technomancer/crossroads/api/alchemy/AtmosChargeSavedData.java)).
- **1,000,000,000 FE capacity by default**; **20,000 FE/t throughput per attenuator**; no player/range restriction, no transport loss.
- Toggle **deposit** or **withdraw** with native wrench; circuits can read charge percentage and automate control.
- At **above 50%** charge, lightning strikes become more common even in clear weather; **above 90%**, creepers can spawn charged. Crossroads server configs include **`atmos_effects`** bitmask (0=off, 1=lightning, 2=charged creepers, 3=both) and a capacity setting, allowing safety tuning **without custom code**.
- The intended behavior is a global/public common resource. Do not implement exclusive ownership, spectrum access, private wireless IDs, external FE battery simulation, or a cross-mod bypass without a separate owner decision.

This one subsystem is worth a dedicated multiplayer and dimension test: deposit 20,000 FE/t in one location, withdraw in another; compare player access, rejoin/save, stress in dimensions created by RFTools/Ad Astra/Infinite Dimensions, redstone monitoring, capacity overcharge consequences, and chunk claims/protection. Verify actual current runtime instead of assuming the manual's description proves the packed artifact runs.

## Version-qualified integration and QA gates

1. **Exact provider files**: confirm file metadata/hashes, release-specific dependency relation, licensing and allowed pack redistribution. Never dynamically fetch latest into an immutable assembled build.
2. **Boot**: only when separately authorized, run minimal **Crossroads + Essentials + Patchouli** on NeoForge 21.1.265 first, then combined server/client; verify Patchouli Crossroads and Essentials manuals are visible and link to valid item recipes.
3. **Native engineering**: inspect heat safety, rotary speed/torque and spinning machines, gears across chunks, steam/boiler transfer, beam optics and Beacon Harness, ore doubling/tripling recipes and JEI/EMI visibility. Validate configurable native progression without skipping beam prerequisites.
4. **Atmospheric effects**: test per-world and cross-dimensional persisted charges, multiplayer deposit and withdrawal, even-world recreation, overcharge lightning/charged creeper threshold, environment grief/claims and commands/config toggles. Avoid source edits when `atmos_effects` already solves a problem.
5. **Mod interactions**: verify OP/FE display with Draconic, RF/FE IO with Mekanism/Oritech, mechanical power relation to Create, ore-processor duplication/recipes, and Crossroads genetics with other targeted biotech. Overlap is welcome, but report actual game-breaking feedback/exploits.
6. **Progression treatment**: respect the in-mod `Detailed Crafter` branching and advancement framework, without treating it as a fourth alternative to future Cyborg/Meatbag/Alien TMT paths.
7. **Acceptance**: source/provider review != `pinned`; static CI != boot; boot != gameplay PASS. All actual acceptance must be attached to a specific built artifact and captured QA level, with owner authorization for game/build stages.

No new KubeJS bridge, Java code, modpack recipe changes, cross-pack source import, universal FE/OP converter or special-made manual files have been authorized. Retain the native oddball mechanics that led to this core selection.
