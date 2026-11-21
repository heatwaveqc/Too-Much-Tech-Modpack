# Too Much Tech — initial design brief

**State: owner-selected core tech systems, with other features still open for design (2026-11-20).**

## Intent

Build an ambitious, technology-centered Minecraft pack in which machinery, engineering, energy, networks, logistics, automation, materials processing and industrial-scale problem solving matter. It is a distinct sibling to Too Much Magic, **not** its mod list with the exclusion signs reversed.

The repository's purpose is to turn that broad intent into an evidence-backed, reproducible pack, without deciding progression or additional systems by accident.

## Locked design direction (2026-11-20)

- **Owner-selected technology backbone:** Oritech, Just Dire Things, Mekanism, Draconic Evolution **and Crossroads** (fifth core system). These are selected in principle, not actually pinned, installed, built or gameplay-tested. Crossroads' required **Technomancer Essentials** and owner-requested **Patchouli** are targeted too; **FTB Essentials is unrelated**.
- **Desired if feasible:** the official Thermal Expansion family, currently **held** because no official 1.21.1 NeoForge release was found. The independent FACTAS beta is explicitly targeted, without representing it as an official Thermal port.
- **Crossroads native engineering:** preserve distinct **heat**, **rotary speed/torque**, steam, optical beams/alignments, ore processing, native Alchemy/Technomancy/Bioengineering specializations, and the shared atmospheric FE reservoir with optional native overcharge hazards. Prefer its native configs, not a new invented unified-power adapter. Crossroads specialization paths are its own mechanic, independent of future Cyborg/Meatbag/Alien character progression. [Design and QA](research/CROSSROADS-CORE-2026-11-20.md).
- **Progression tone:** **fun with technology, not GregTech-style enforced grind.** Prefer machines, spatial engineering, power networks, and clever automation puzzles over repeated mandatory crafting loops, laborious subcomponents, dozens of arbitrary gating stages or one required mod chained through another for its own sake.
- **Inclusion philosophy:** first pass is inclusive: **feature overlap is not a reason for exclusion**. Only a verified crash, incompatible save/state behavior, unresolved hard mod-ID conflict, unsupported artifact or comparably severe functional incompatibility blocks co-installation. Lowering overpowered quickhacks or changing cross-mod outputs is a future balance/config task, not a prerequisite for selecting a mod.
- **Cybernetic targets:** Oritech plus Cybernetics, Synthetics, Matter Overdrive (Unofficial Port), NeoSync and Create: Chromeware. Different player-upgrade mechanics can co-exist when technically safe. Matter Overdrive forks/ports need one matching JAR implementation since identical mod IDs/content are a hard conflict, not just conceptual overlap.
- **Future shared Progression:** import TMM's `compat/progression` engine only after upstream readiness; author three future TMT discipline packages **Cyborg, Meatbag, Alien** as goals, without locking their exclusivity or inventing abilities now. [Goal register](../manifest/progression-goals.json).
- **Dimensions:** Ad Astra was already selected. **Primary additional goals** are Ad Astra: Planets, Stargate Journey, RFTools Dimensions, Infinite Dimensions, and Deep Space; **isolated experimental goals** are MACHINA and Create: Universe. Planet definitions with seeded terrain and runtime-generated dimensions are distinct implementations. [Dimension survey](research/THEMATIC-DIMENSIONS-2026-11-20.md).
- **Owner-selected optional magitech:** target **Botania Revived** and **Embers Re-Ignited** as industrial/automation disciplines. Neither should become a prerequisite for mainstream electric/industrial progression. Embers Reborn remains a fallback port for research, not a co-installed alternative JAR. See [magitech assessment](research/TECH-FIRST-MAGITECH-2026-11-20.md).
- **Bosses and encounter research:** **science fiction, industrial, robotic and biotechnology first**; allow fantasy bosses as optional flavor rather than the combat backbone. The initial 18 general and second 14 tech-focused boss candidates remain **research-only**, not owner inclusion targets. Review [general survey](research/BOSS-AND-ENCOUNTERS-2026-11-20.md) and [tech-heavy follow-up](research/TECH-HEAVY-BOSSES-2026-11-20.md); then build a verified boss/elite census and test scalable fights without rendering engineering/guns obsolete.
- **Sister-pack convenience:** port most appropriate TMM food and quality-of-life mods, but independently verify artifact versions/compatibility and **do not** port magic-only progression or invalid historical pins.

**Biotechnology now targeted:** a broad technology family of genetic augmentation, industrial breeding/cloning, living factories, pathology and alien biology. All 24 surveyed version-compatible mods are now selected as **inclusion goals**; select one underlying Biomancy binary (two port alternatives) before install, and keep NEEPMeat a conditional future goal due 1.20.1 Fabric-only. See [biotech survey](research/BIOTECH-2026-11-20.md). Existing Cyborg/Meatbag/Alien shared Progression goals can incorporate biology later without silently locking a fourth class or exclusivity.

See [current research](research/TECH-MODS-2026-11-20.md), [TMM carryover](research/TMM-FOOD-QOL-CARRYOVER-2026-11-20.md), and [owner decisions](DECISIONS.md). All 102 pre-existing tech and TMM food/QoL survey items are targeted for future inclusion subject to compatibility checks. Cybernetics from the robot-mob survey is now owner-targeted, while the other 11 mob candidates and all 20 new dimension survey candidates remain research-only.

## Design areas awaiting owner choices

1. **Production and automation:** primary factory/contraption ecosystems, realistic complexity versus convenience, and whether overlap or redundant automation systems are desirable.
2. **Power:** which energy systems (including FE/OP/RF naming/compatibility), generation tiers, storage, cross-mod conversion and intended throughput limits.
3. **Storage and logistics:** networked storage, pipes, item/fluid routing, autocrafting, inventory shortcuts, player transport and infrastructure progression.
4. **Resources and materials:** ores, alloys, unified tags, processing ratios, mining, recycling, worldgen and dimension dependencies.
5. **Progression:** early survival/hand tools, machine ages, advanced production, late-game objectives, and whether endgame equivalence/cross-over with Too Much Magic is desired.
6. **World and challenges:** exploration, structures, bosses, automation-friendly farming and performance considerations.
7. **Modpack identity:** how much magic, food, cosmetic, quest, skill, and custom-code content belongs in a technology-centered pack; whether the projects share data libraries or remain fully independent.
8. **Practical limits:** target client/server hardware, player count, intended pack size, acceptable load time, and release/testing cadence.

**No additional named third-party mod is selected merely by appearing in a research survey.** Owner-selected targets now include the earlier 102-entry tech/TMM carryover survey, five additional cybernetic mods, and a deferred first-party shared Progression engine. The remaining 11 robotic and 13 dimension entries remain exploratory. Record subsequent selections with version evidence in `manifest/mods.json` and [DECISIONS.md](DECISIONS.md).

## Provisional technology choices (not gameplay commitments)

Minecraft 1.21.1, NeoForge 21.1.265 and Java 21 are initial engineering defaults inherited from tool familiarity with the sister project. Packwiz is the versioned installer/index, and Prism Launcher is the intended initial test delivery target. If a compelling tech ecosystem needs a different Minecraft version or mod loader, make a recorded decision **before** building a conflicting mod roster.

## Acceptance principles

- Version-pinned dependency graph, no silently floating releases.
- Known ownership for configs, patches, custom modules and shared files.
- No "compatible" claim without matching loader/game version and appropriate smoke evidence.
- Source CI, assembly, dedicated server, client launch and gameplay acceptance remain different checkboxes.
- Design choices, tradeoffs, and changes are explicit rather than hidden in automated mod installation.
