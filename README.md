# Too Much Tech — Minecraft 1.21.1 NeoForge

**Status: repository bootstrap with researched candidates; no installed mods or game-tested build.**

Too Much Tech is a technology-focused Minecraft modpack project and a **separate sister project** to [Too Much Magic](https://github.com/heatwaveqc/Too-Much-Magic-Modpack). Its intended themes are engineering, machines, power, automation, logistics, industrial systems, and meaningful technical progression. Its initial owner-selected tech backbone is **Oritech, Just Dire Things, Mekanism and Draconic Evolution**. All 102 original technology + TMM food/QoL entries are targeted for future inclusion, including FACTAS. Five additional cybernetic targets (Cybernetics, Synthetics, one Matter Overdrive port, NeoSync, Create: Chromeware) and the deferred **shared TMM Progression engine** are targeted too, with **Cyborg, Meatbag, Alien** paths as design goals. Functional overlap is welcome unless real bugs/incompatibilities arise. Actual artifact checks, progression balance and releases remain under research. No mods are installed yet.

## Provisional development baseline

- Minecraft **1.21.1**
- NeoForge **21.1.265**
- Java **21**
- packwiz as the declarative pack index and pinning tool
- Prism Launcher as the intended player-facing import/testing target

These choices reuse known tooling from the sister project for an efficient start. They are **provisional**, not a mandate to retain an incompatible game version or loader. No third-party mod, modpack file, asset, or license has been copied from Too Much Magic.

## Repository map

- [AGENTS.md](AGENTS.md): safety, collaboration, and change authority for agents and developers.
- [docs/DESIGN.md](docs/DESIGN.md): intent, boundaries, and unresolved gameplay choices.
- [docs/DECISIONS.md](docs/DECISIONS.md): decision ledger, including provisional assumptions.
- [Cybernetic progression goals](manifest/progression-goals.json): Cyborg / Meatbag / Alien path goals and shared TMM Progression source gate.
- [Thematic dimensions research](docs/research/THEMATIC-DIMENSIONS-2026-11-20.md): Ad Astra custom planet configuration and 20 other dimension/procedural candidates.
- [docs/WORKFLOW.md](docs/WORKFLOW.md): branches, PRs, ownership, and integration.
- [docs/BRANCH-LIFECYCLE.md](docs/BRANCH-LIFECYCLE.md): review and retirement, single-writer workstreams, branch budget.
- [docs/INTEGRATION-SOURCES.md](docs/INTEGRATION-SOURCES.md): immutable donor commits and path ownership.
- [docs/BUILD-CHANNELS-AND-TESTING.md](docs/BUILD-CHANNELS-AND-TESTING.md): unstable/candidate/stable evidence and build authorization.
- [docs/SISTER-PROJECT-PARITY.md](docs/SISTER-PROJECT-PARITY.md): exact TMM methods adopted and deliberately not copied.
- [docs/QA.md](docs/QA.md) and [QA hub](docs/qa/README.md): eight QA levels, A/B/C test handoffs and live-test inclusion.
- [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md): candidate/installed mod research protocol.
- [docs/ROADMAP.md](docs/ROADMAP.md): milestones without fictional completion claims.
- [docs/REPO-SETTINGS.md](docs/REPO-SETTINGS.md): manual GitHub administration checklist.
- [manifest/mods.json](manifest/mods.json): owner-selected core tech, version-scoped tech research, and TMM food/QoL carryover intake; **not installed**.
- [Tech mod release survey](docs/research/TECH-MODS-2026-11-20.md): 1.21.1 NeoForge target candidates and build/overlap risks.
- [Robot and cybernetic mobs](docs/research/ROBOTIC-MOBS-2026-11-20.md): enemy-focused new research, not selected.
- [TMM food/QoL carryover survey](docs/research/TMM-FOOD-QOL-CARRYOVER-2026-11-20.md): evidence-based sibling-port plan.
- [manifest/integration-sources.json](manifest/integration-sources.json): frozen source stream/provenance registry.
- [manifest/feature-checklist.json](manifest/feature-checklist.json): evidence-backed feature acceptance ledger.
- [manifest/live-test-inclusion.json](manifest/live-test-inclusion.json): ready-feature next-build inclusion obligation.
- [manifest/release-registry.json](manifest/release-registry.json): candidate/stable provenance, currently empty.
- [pack.toml](pack.toml), [index.toml](index.toml): minimal empty packwiz bootstrap.
- [scripts/validate_repo.py](scripts/validate_repo.py) and [scripts/validate_integration.py](scripts/validate_integration.py): local and CI metadata, frozen-source and evidence validation.
- [Branch lifecycle advisory](.github/workflows/branch-lifecycle-report.yml): daily read-only branch inventory and PR changed-path overlap.

## Working model

`main` is the project policy and accepted-source branch. `test/full-integration` is the planned source-integration and QA candidate branch. Work happens on scoped temporary feature branches through PRs. The single designated integration writer reconciles shared manifests and packwiz, using frozen donor commits and a ready-for-test inclusion ledger. See [docs/WORKFLOW.md](docs/WORKFLOW.md).

Run the *quick*, non-Minecraft checks from a checkout:

```bash
python3 scripts/validate_repo.py
python3 scripts/validate_integration.py
python3 -m unittest discover -s tests -v
```

These checks are **local/schema-only** until external donor verification is implemented, and do **not** assemble the modpack, launch a server/client, generate a Prism package, or certify mod compatibility. Full pack assembly, full server smoke, Prism packaging, and release promotion require separate owner authorization.

## Next decisions

Before adding actual tech mods, record the intended power systems, storage/logistics philosophy, automation style and progression gates. This is **fun with tech, not GregTech-style enforced grind**. Official Thermal Expansion is conditionally targeted but held due lack of a 1.21.1 NeoForge release; the independent Thermal-inspired FACTAS beta is explicitly targeted. Track proposed choices in [docs/DESIGN.md](docs/DESIGN.md) and concrete mods in the manifest. The first decision workstream is [Issue #1](https://github.com/heatwaveqc/Too-Much-Tech-Modpack/issues/1).

**No stable, alpha, or playable build exists at bootstrap.**
