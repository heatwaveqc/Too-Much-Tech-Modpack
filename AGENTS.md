# Too Much Tech — repository-wide contributor and agent contract

Applies to AI agents, human contributors, scheduled maintenance, coding sessions and all branches. **Read this, [branch lifecycle](docs/BRANCH-LIFECYCLE.md), [integration sources](docs/INTEGRATION-SOURCES.md) and [QA standards](docs/qa/README.md) before writing.**

Policy parity: adapted from the Too Much Magic (TMM) project's [main governance](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/main/AGENTS.md), [branch lifecycle](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/main/docs/BRANCH-LIFECYCLE.md) and [active integration rules](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/AGENTS.md), audited 2026-11-20. This copy is **independently authoritative for TMT**: future TMM edits do not silently alter TMT.

## Identity and authoritative sources

- TMT is an independent tech-first modpack. TMM is a sibling project and an engineering reference; its roster, magic exclusions, skill trees, progression architecture and game design are **not** inherited.
- Provisional baseline: Minecraft 1.21.1, NeoForge 21.1.265, Java 21. Reassess before committing to an incompatible tech ecosystem.
- The mod intent/approval register is `manifest/mods.json`; the **actually indexed** pack contents are `pack.toml` and `index.toml`; `manifest/integration-sources.json` records frozen source ownership/provenance; `manifest/feature-checklist.json` is acceptance tracking. Proposals are not pins, pins are not boot evidence, and merged source is not necessarily runtime-activated.
- Decisions live in `docs/DECISIONS.md`; issue descriptions, assistant suggestions and research do not silently supersede owner decisions.
- No mod is installed and no full pack or gameplay test has occurred as of bootstrap. Do not fabricate runtime results, commands, downloads, or releases.

## Ownership, independent workstreams and code placement

- **One designated integration writer** owns shared `test/full-integration`, packwiz locks, source manifests, version pins, cross-mod configs, quest runtime, staged sources and build/release decisions. Feature agents write isolated PR branches; do not directly overwrite shared integration trees.
- Search existing issues, PRs, branches, already integrated code, and current donor records **before starting/resuming**. Reuse the same workstream after chat failure; don't duplicate a completed implementation. Exactly one writer per shared branch and owned path set.
- Every temporary branch gets a meaningful draft/ready PR promptly, within 24 hours. PR handoff must list owner, scope, base/head and exact commit, touched paths, dependencies, current checks, blockers, A/B/C QA, and next action.
- **Source architecture:** keep reusable executable functionality in its single, designated engine/module; feature-specific declarative data, recipes, configs and tags in their feature owners. A feature needing shared runtime hooks uses a reviewed engine PR, not a new competing implementation or ad hoc KubeJS copy. Do not create a TMM-style permanent Progression subsystem branch until TMT actually needs one and owner approves it.
- Prefer native config/data/tag interoperability first; custom Java/KubeJS/other runtime code requires a demonstrated need, ownership, versioning and tests. Track source and content licenses, dependencies, intentional conflicts and rollback.
- Source-ready coherent slices within **already owner-approved scope** may be merged by the designated integration writer after quick checks and provenance review without asking for every routine merge again. This does **not** delegate novel gameplay/balance/roster/architectural choices or any full build authorization.

## Frozen donor provenance and safe merges

- New source streams must use a **full immutable 40-hex commit SHA**, source branch and narrowly owned paths. Dynamic branch heads must never be the assembly input. The [integration source contract](docs/INTEGRATION-SOURCES.md) and read-only source preflight apply before merging.
- If a stream becomes integrated, mark its paths baseline-owned and preserve its original branch, PR and commit provenance. Never leave a deleted temporary branch as the sole documented build dependency.
- No stale directory replay, bulk snapshots that replace current shared files, unapproved overrides, hidden source assembly on push, or blind merge conflict resolution. Validate duplicate path ownership, packwiz hashes, source reachability and code collisions on current integration HEAD.
- `SOURCE READY` means reviewed implementation, **not** assembled, installed, server-tested, client-tested or gameplay-accepted.
- A claim of 'ready for next live test' creates an **inclusion attempt obligation**. Register it in [the live-test intake](docs/qa/LIVE-TEST-INCLUSION-REGISTER.md). For a comprehensive build, every ready feature must be INCLUDED, BLOCKED with evidence, or explicitly OWNER-DEFERRED. Earlier deferrals do not silently carry forward.

## Eight QA levels and hard authorization

Use [the canonical levels](docs/qa/TEST-LEVELS-AND-TERMINOLOGY.md):
1. Repository CI; 2. Module CI; 3. read-only Integration Preflight (**Quick CI**);
4. Integration Assembly; 5. Server Boot Smoke; 6. Prism QA Package;
7. Client Launch Smoke; 8. Gameplay Acceptance.

- Only the first three may run automatically on PR/push. Quick CI cannot download/assemble the complete pack, start the modded game, or produce a distributable Prism ZIP.
- **Each** complete assembly, full Minecraft server smoke, Prism package or release requires new explicit owner authorization for the exact run and scope. Preparing a build, asking for readiness, running quick checks, or a green PR does not grant this permission. Do not re-dispatch, retry, schedule, or indirectly invoke a full run without fresh authorization.
- Any future full-build workflow must use `workflow_dispatch`, default-false opt-in input(s) and a job-level guard requiring **both** the exact manual event and approval, including every OR branch; no push/PR/schedule/workflow_call backdoor.
- Before each authorized full build, review the **entire active packwiz roster** and dependencies against compatible upstream versions, decide update/hold/unknown, run lightweight checks, freeze exact source SHA/pins and preserve a rollback path. Review is not itself permission to build.
- The canonical rolling **unstable** artifact is a future channel, not automatically enabled. Only a previously successful *authorized* Prism artifact may be published/reconciled automatically; publication cannot start/retry a build and failed publication preserves the old asset. Candidate and Stable require explicit approval and immutable provenance.
- Follow [A/B/C execution types](docs/qa/QA-EXECUTION-TYPES.md) for every live-test handoff. A = offline/source/Codex; B = verified in-game commands; C = manual play/UI/setups. Never mark in-world PASS from A evidence.
- No client options, saves, world files or personal keys in public QA/stable packages. Any QA-only preference helper must be opt-in, private, version-checked, and absent from Stable.

## Branch hygiene and maintenance

- Permanent branches: `main` and `test/full-integration`. Add permanent branches only by owner decision. Health thresholds: <=20 remote branches normal, 21–30 review, >30 maintenance priority; **not automatic deletion permission**.
- A read-only daily inventory and PR changed-path collision advisory may run without approval. Review un-PR'd temporary branches after 24h, ready PR waits after 24h, inactivity after 72h, surviving merged branches after 24h, unresolved donor holds after 7d. Retain explicit exceptions.
- **Never perform automatic destructive branch retirement.** New deletion batches require reviewed per-ref SHA allowlist, independent dry run, preservation of PRs/dependencies/source commits, owner approval for that exact batch, SHA-lease checks and post-run verification. Do not copy TMM's historical batch/nonce/console IDs or blindly delete uncertain refs.
- Nightly maintenance is constrained to safe existing ownership, documentation, tests and small approved source fixes; it is not authorization to invent feature work, run full builds or prune refs. Record useful changes in GitHub, and do not manufacture work on a healthy repo.
- No force pushes, fake/dummy merges, blanket branch deletion, silent release mutation, or `[skip ci]` on meaningful changes.

## Minimum handoff and status truth

Every PR/release/test summary supplies exact branch/commit, affected paths and dependencies, source and pin provenance, actual quick checks (with links), what was **not** run, observed failures, next workstream action and A/B/C acceptance tasks. Use `SOURCE READY`, `PREFLIGHT PASS`, `ASSEMBLED`, `SERVER PASS`, `PRISM PACKAGED`, `CLIENT PASS`, `GAMEPLAY PASS`, `BLOCKED`, `FAIL` and `NOT RUN` correctly. An automatically generated ZIP does not imply a launched client or stable release.

Repository settings, CODEOWNERS, branch protections and Actions permissions must be verified in GitHub; documents alone do not enforce them. See [admin checklist](docs/REPO-SETTINGS.md).
