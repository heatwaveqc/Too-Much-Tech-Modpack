# Shared Progression in Too Much Tech — Cyborg, Meatbag, Alien

**State:** selected future target, **not implemented**. Owner request 2026-11-20. [Machine-readable goal design](../../manifest/progression-goals.json).

## Reuse one engine; don't fork it

TMM owns the [standalone Unified Progression engine](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/tree/test/full-integration/compat/progression), examined around exact parent commit `7d1be155bf1334995b65ebe88566bd4d7ae54635`. Current `compat/progression/README.md` calls it a source-level pilot (0.1.0-dev, NeoForge 1.21.1 Java 21) not an in-world accepted pack JAR. It provides a strict `data/<namespace>/tmm_progression/paths/<name>.json` datapack path loader, validated activities/milestones/skills and optional trusted ProgressionApi adapters. It needs upstream runtime/API completion before TMT imports an approved snapshot.

**Architectural intent:** TMM is the *single runtime owner*. TMT consumes a reviewed stable Gradle/JAR artifact or exact frozen donor (with licensing/ownership review) and authors TMT-specific data-defined paths and trusted integration adapters only when needed. Do not duplicate Java handlers in three classes, copy TMM's Monk/Hunter/vampire/witchery-specific gameplay, or edit its code from this TMT research branch.

## Future path themes (not committed powers)

| Path | Fun identity | Candidate hooks | Design constraints |
| --- | --- | --- | --- |
| **Cyborg** | Upgrade yourself, a machine at a time; synthetic body and neural capability | Oritech permanent augmentation, Cybernetics installation, Synthetics manufacturing, Chromeware surgery, Matter Overdrive android form, NeoSync shells | Award **actual** equipment/implant acceptance on server; prevent duplicate grants, preserve state on body switching and relog |
| **Meatbag** | Biology and unaugmented ingenuity, preparation, resilience, food/chemistry, physical specialization | Shared Progression core, Farmer's Delight/Pam's food, future verified biological providers | Avoid unasked 'no augments ever' rules and arbitrary exclusion; mechanics/powers open |
| **Alien** | Off-world discovery, ecological adaptation, alien physiology and lifeforms | Ad Astra/Planets, custom dimensions, future alien mobs and biology | Recognize verified travel and science; don't assume an alien species mod is selected |

Whether paths are exclusive, alternate or combinable is **deliberately undecided**. Being inclusive toward cybernetic mods does not prove that every character should get every path; determine that at skill-tree design stage. If a path later needs an additional event hook, build it in the shared Progression engine through the correct integration ownership process.

## Integration workflow

1. Wait for TMM engine source/API readiness, integrated release evidence, and issue/PR authorization. Reinspect TMM head, freeze exact source SHA; do not treat today's inspect commit as a production release.
2. Verify mod/license ownership and packaging; prevent `tmm_progression` namespace/version collisions with another bundled JAR or duplicate copy.
3. Author three TMT path JSONs using validated schema with clear XP/milestone sources. Avoid claiming a path is usable until source and in-world acceptance.
4. Adapt event sources (post-install, actual off-world arrival, synthesized body activation, food/crafting activity), avoiding KubeJS global tick scans or fragile UI-only checks.
5. Test standalone and mixed setups: no augmentation; each augmented system; simultaneous installed systems; NeoSync transfer; death/shell resume; off-world dimension transfer; re-login; multiplayer.
6. Balance paths and author educational FTB quests only after verified systems work. No new Progression code is imported in this survey.

The goal is player choice and new capabilities, not forcing a full technology chain or punitive grind.
