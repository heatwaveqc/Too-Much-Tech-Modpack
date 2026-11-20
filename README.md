# Too Much Tech — Minecraft 1.21.1 NeoForge

**Status: repository bootstrap; no installed mods or game-tested build.**

Too Much Tech is a technology-focused Minecraft modpack project and a **separate sister project** to [Too Much Magic](https://github.com/heatwaveqc/Too-Much-Magic-Modpack). Its intended themes are engineering, machines, power, automation, logistics, industrial systems, and meaningful technical progression. Its eventual mod roster, gates, balance, and release criteria are **not yet approved**.

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
- [docs/WORKFLOW.md](docs/WORKFLOW.md): branches, PRs, ownership, and integration.
- [docs/QA.md](docs/QA.md): source checks versus authorized Minecraft testing.
- [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md): candidate/installed mod research protocol.
- [docs/ROADMAP.md](docs/ROADMAP.md): milestones without fictional completion claims.
- [docs/REPO-SETTINGS.md](docs/REPO-SETTINGS.md): manual GitHub administration checklist.
- [manifest/mods.json](manifest/mods.json): initially empty mod-intake register.
- [pack.toml](pack.toml), [index.toml](index.toml): minimal empty packwiz bootstrap.
- [scripts/validate_repo.py](scripts/validate_repo.py): local and CI metadata validation.

## Working model

`main` is the project policy and accepted-source branch. `test/full-integration` is the planned source-integration and QA candidate branch. Work happens on scoped temporary feature branches, normally through PRs. See [docs/WORKFLOW.md](docs/WORKFLOW.md).

Run the *quick*, non-Minecraft checks from a checkout:

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

These checks do **not** assemble the modpack, launch a server/client, generate a Prism package, or certify mod compatibility. Full pack assembly, full server smoke, Prism packaging, and release promotion require separate owner authorization.

## Next decisions

Before adding actual tech mods, record the intended power systems, storage/logistics philosophy, automation style, desired progression gates, and whether any overlaps with Too Much Magic should be shared as maintained components. Track proposed choices in [docs/DESIGN.md](docs/DESIGN.md) and concrete mods in the manifest. The first decision workstream is [Issue #1](https://github.com/heatwaveqc/Too-Much-Tech-Modpack/issues/1).

**No stable, alpha, or playable build exists at bootstrap.**
