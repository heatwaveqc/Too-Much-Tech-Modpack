# Too Much Tech — contributor and agent operating contract

This file applies to AI agents, work sessions, coding agents, automation, and human contributors. Read [docs/WORKFLOW.md](docs/WORKFLOW.md) and [docs/QA.md](docs/QA.md) before acting.

## Project and sources of truth

- This repository is a **separate** technology-focused Minecraft modpack. Its relationship to [Too Much Magic](https://github.com/heatwaveqc/Too-Much-Magic-Modpack) is sibling/reference only. Never silently import its exclusion rules, balancing, feature designs, third-party binaries, licenses, secrets, or histories.
- Initial game baseline: Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21; **provisional** pending actual mod compatibility decisions.
- The tracked `pack.toml` and `index.toml` are the packwiz bootstrap. `manifest/mods.json` is the mod research and intent register. Only packwiz-indexed, version-pinned files are pack inputs; entries in the research register do not install a mod.
- Owner decisions are recorded in `docs/DECISIONS.md`. An idea or issue is not approval to implement gameplay. Do not claim an installed mod, test PASS, tested release, or runtime compatibility without evidence.
- This bootstrap has **zero installed third-party mods**. No final mod roster, automation progression, custom modules, or public release is authorized by bootstrap alone.

## Coordination and branches

- `main`: accepted policy/bootstrap and controlled source history. `test/full-integration`: integrated development candidate; NOT automatically game-tested or stable. All other branches are scoped and temporary unless owner approves otherwise.
- Before work, inspect current branches, PRs, issues, and relevant files. Reuse the existing workstream; a fresh chat does not justify a duplicate branch.
- Use a single writer per shared branch/path set. Work on a scoped temporary branch and open a draft/ready PR promptly (within 24 hours). Record owner, scope, touched paths, dependencies, baseline, changes, checks, blockers, and next action. Avoid direct concurrent changes to shared packwiz/manifest files.
- Integrate reviewed, already-approved source slices continuously, with checked current head/CI, without re-authorizing every routine metadata fix. New gameplay choices, incompatible architecture changes, major roster expansions, or balance decisions require owner direction.
- Do not force-push or delete remote branches without specific evidence, coordination and authorization. Preserve source provenance before retiring donor branches. Never assume merge == tested.
- Avoid creating a permanent subsystem hierarchy or branch-retirement machinery before actual work justifies it.

## Build and test authority

- **Quick CI only** may run on pushes/PRs: TOML/JSON/packwiz index validation, linting, unit tests, limited compilation and source preflight. These do not boot Minecraft.
- **No unattended full builds.** Never automatically download/assemble the full mod roster, run a full NeoForge server, generate a Prism package, publish an artifact/release, or update stable on push, PR, schedule, workflow_call, or generic "run tests".
- Full Integration Assembly, Server Boot Smoke, Prism QA Package, Client Launch Smoke and Gameplay Acceptance must be distinguished as separate evidence levels. Full assembly/boot/package needs a separate **explicit owner authorization for each execution**; no scheduled/retry/indirect execution.
- A future build-capable GitHub workflow must use `workflow_dispatch` and default-false opt-in guard(s), with its actual build jobs gated on the exact manual event **and** opt-in. The owner instruction must identify intended scope; never silently broaden it.
- Before any authorized full build, survey active pinned mods/dependencies and compatible updates; reconcile changes by reviewed source PR, run quick checks and freeze the exact build SHA. Never treat upstream availability as demonstrated interoperability.
- No stable label, release tag, or success badge from metadata-only checks. See [docs/QA.md](docs/QA.md).

## Content and security

- Prefer native mod configs/tags and data-driven compatibility before new runtime code. A runtime hook must have a documented reason and tests.
- Record mod version, loader compatibility, dependencies, provenance and license/redistribution obligations before installation. Do not commit third-party mod JARs, private modpacks, copyrighted assets, credentials, tokens, personal configs, saves or crash logs.
- New custom code and new external redistribution require conscious licensing decisions. No repository license has yet been selected.
- Protect rollback checkpoints; record exact Git SHAs and links in PRs. Never rewrite historical evidence to manufacture a green test.

## Minimal change handoff

For each PR report: **what changed; why; exact branch/SHA; owned paths; linked decision/issue; quick checks run; integration risk; what remains; required A/B/C QA**. Label source-only work `SOURCE READY` at most, never `SERVER PASS` or `GAMEPLAY PASS`.
