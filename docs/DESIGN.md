# Too Much Tech — initial design brief

**State: open design, not an approved feature specification (2026-11-20).**

## Intent

Build an ambitious, technology-centered Minecraft pack in which machinery, engineering, energy, networks, logistics, automation, materials processing and industrial-scale problem solving matter. It is a distinct sibling to Too Much Magic, **not** its mod list with the exclusion signs reversed.

The repository's purpose is to turn that broad intent into an evidence-backed, reproducible pack, without deciding core progression by accident while scaffolding the repository.

## Design areas awaiting owner choices

1. **Production and automation:** primary factory/contraption ecosystems, realistic complexity versus convenience, and whether overlap or redundant automation systems are desirable.
2. **Power:** which energy systems (including FE/OP/RF naming/compatibility), generation tiers, storage, cross-mod conversion and intended throughput limits.
3. **Storage and logistics:** networked storage, pipes, item/fluid routing, autocrafting, inventory shortcuts, player transport and infrastructure progression.
4. **Resources and materials:** ores, alloys, unified tags, processing ratios, mining, recycling, worldgen and dimension dependencies.
5. **Progression:** early survival/hand tools, machine ages, advanced production, late-game objectives, and whether endgame equivalence/cross-over with Too Much Magic is desired.
6. **World and challenges:** exploration, structures, bosses, automation-friendly farming and performance considerations.
7. **Modpack identity:** how much magic, food, cosmetic, quest, skill, and custom-code content belongs in a technology-centered pack; whether the projects share data libraries or remain fully independent.
8. **Practical limits:** target client/server hardware, player count, intended pack size, acceptable load time, and release/testing cadence.

**No named third-party mod is approved merely by appearing in an issue, a comparison, or the sibling repository.** Choose a roster with supporting version evidence, then explicitly record approvals in `manifest/mods.json` and [docs/DECISIONS.md](DECISIONS.md).

## Provisional technology choices (not gameplay commitments)

Minecraft 1.21.1, NeoForge 21.1.265 and Java 21 are initial engineering defaults inherited from tool familiarity with the sister project. Packwiz is the versioned installer/index, and Prism Launcher is the intended initial test delivery target. If a compelling tech ecosystem needs a different Minecraft version or mod loader, make a recorded decision **before** building a conflicting mod roster.

## Acceptance principles

- Version-pinned dependency graph, no silently floating releases.
- Known ownership for configs, patches, custom modules and shared files.
- No "compatible" claim without matching loader/game version and appropriate smoke evidence.
- Source CI, assembly, dedicated server, client launch and gameplay acceptance remain different checkboxes.
- Design choices, tradeoffs, and changes are explicit rather than hidden in automated mod installation.
