# Too Much Tech — initial design brief

**State: owner-selected core tech systems, with other features still open for design (2026-11-20).**

## Intent

Build an ambitious, technology-centered Minecraft pack in which machinery, engineering, energy, networks, logistics, automation, materials processing and industrial-scale problem solving matter. It is a distinct sibling to Too Much Magic, **not** its mod list with the exclusion signs reversed.

The repository's purpose is to turn that broad intent into an evidence-backed, reproducible pack, without deciding progression or additional systems by accident.

## Locked design direction (2026-11-20)

- **Owner-selected technology backbone:** Oritech, Just Dire Things, Mekanism and Draconic Evolution. These are selected in principle, not actually pinned, installed, built or gameplay-tested.
- **Desired if feasible:** the official Thermal Expansion family, currently **held** because no official 1.21.1 NeoForge release was found. A separate Thermal-inspired beta such as FACTAS is not automatically approved as a substitute.
- **Progression tone:** **fun with technology, not GregTech-style enforced grind.** Prefer machines, spatial engineering, power networks, and clever automation puzzles over repeated mandatory crafting loops, laborious subcomponents, dozens of arbitrary gating stages or one required mod chained through another for its own sake.
- **Sister-pack convenience:** port most appropriate TMM food and quality-of-life mods, but independently verify artifact versions/compatibility and **do not** port magic-only progression or invalid historical pins.

See [current research](research/TECH-MODS-2026-11-20.md), [TMM carryover](research/TMM-FOOD-QOL-CARRYOVER-2026-11-20.md), and [owner decisions](DECISIONS.md). Other surveyed mod names are only **candidates**.

## Design areas awaiting owner choices

1. **Production and automation:** primary factory/contraption ecosystems, realistic complexity versus convenience, and whether overlap or redundant automation systems are desirable.
2. **Power:** which energy systems (including FE/OP/RF naming/compatibility), generation tiers, storage, cross-mod conversion and intended throughput limits.
3. **Storage and logistics:** networked storage, pipes, item/fluid routing, autocrafting, inventory shortcuts, player transport and infrastructure progression.
4. **Resources and materials:** ores, alloys, unified tags, processing ratios, mining, recycling, worldgen and dimension dependencies.
5. **Progression:** early survival/hand tools, machine ages, advanced production, late-game objectives, and whether endgame equivalence/cross-over with Too Much Magic is desired.
6. **World and challenges:** exploration, structures, bosses, automation-friendly farming and performance considerations.
7. **Modpack identity:** how much magic, food, cosmetic, quest, skill, and custom-code content belongs in a technology-centered pack; whether the projects share data libraries or remain fully independent.
8. **Practical limits:** target client/server hardware, player count, intended pack size, acceptable load time, and release/testing cadence.

**No additional named third-party mod is approved merely by appearing in an issue, a comparison, or the sibling repository.** The four explicitly owner-selected core mods are exceptions. Record subsequent selections with version evidence in `manifest/mods.json` and [DECISIONS.md](DECISIONS.md).

## Provisional technology choices (not gameplay commitments)

Minecraft 1.21.1, NeoForge 21.1.265 and Java 21 are initial engineering defaults inherited from tool familiarity with the sister project. Packwiz is the versioned installer/index, and Prism Launcher is the intended initial test delivery target. If a compelling tech ecosystem needs a different Minecraft version or mod loader, make a recorded decision **before** building a conflicting mod roster.

## Acceptance principles

- Version-pinned dependency graph, no silently floating releases.
- Known ownership for configs, patches, custom modules and shared files.
- No "compatible" claim without matching loader/game version and appropriate smoke evidence.
- Source CI, assembly, dedicated server, client launch and gameplay acceptance remain different checkboxes.
- Design choices, tradeoffs, and changes are explicit rather than hidden in automated mod installation.
