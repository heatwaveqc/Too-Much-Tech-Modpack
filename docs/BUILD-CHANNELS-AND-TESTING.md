# Build channels, source integration and acceptance

Adapted from the Too Much Magic [build channel policy](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/docs/BUILD-CHANNELS-AND-TESTING.md). No functional build pipeline or release exists for Too Much Tech yet.

## Channels

- **Integration (UNSTABLE):** source under active development at `test/full-integration`. May be incomplete or broken; quick CI is mandatory but does not imply gameplay.
- **Candidate:** an owner-authorized assembled/tested *frozen full commit*, exact pinned dependencies and recorded artifact digest. Candidate is a reviewable target, not a moving branch pointer.
- **Stable:** immutable explicitly owner-promoted release after client launch and targeted gameplay/multiplayer acceptance, with release notes, known issues and rollback path. No stable exists now.
- **Rolling unstable download:** useful only *after* a canonical Prism QA pipeline has demonstrated assembly/server/package and immutable provenance. A publication-only job may replace its link with an already-verified approved artifact, retaining the prior valid asset on failure. It may never launch/retry a full build, and never imply Stable.

## Preflight and build scope

For every candidate, the integration writer audits live feature readiness and source ownership: ready-for-live-test items must be INCLUDED, BLOCKED with evidence or OWNER-DEFERRED explicitly. A previous blocked/deferred build is not blanket permission to omit a ready feature from the next comprehensive test. See [live-test inclusion](qa/LIVE-TEST-INCLUSION-REGISTER.md).

Review the actual packwiz index (not merely the wish-list in `manifest/mods.json`) and compatible upstream versions of every active mod and dependency before any full build. Stable compatible fixes may be proposed as version-pinned PRs. Risky/unavailable/breaking releases remain held with rationale; no floating latest or stealth game/loader switch. Recompute hashes, validate source SHAs and run quick CI. Freeze exact source SHA, dependency lock, selected first-party JARs and test scope.

## Owner gate per run

Automated push/PR steps may perform **Repository CI**, **Module CI** and **read-only Integration Preflight** only. Complete source assembly, full NeoForge boot, full Prism pack creation, full artifact publication and release promotion cannot be triggered by push, PR or schedule. A future build runner requires a new explicit owner authorization for the **specific** SHA/scope and guarded `workflow_dispatch` options.

Do not port TMM's existing `/tmm smoke`, `/tmm prism`, issue numbers, nonce receipts or publication tags. They are wired to a different repository and cannot be reused as TMT authorization. A TMT bridge, if eventually needed, requires an independent authenticated/replay-guarded implementation and authorization review.

## Accepted evidence

Use [8 canonical QA levels](qa/TEST-LEVELS-AND-TERMINOLOGY.md) and [A/B/C execution types](qa/QA-EXECUTION-TYPES.md). An archived GitHub Actions success does not prove a graphical client launched; an imported Prism ZIP does not prove game progression. Publish a per-build frozen manifest and QA ledger before claiming Candidate. Stable requires explicitly confirmed acceptance from the owner; never silently retag a QA snapshot as stable.

For personal QA preferences, use only opt-in local profiles on a specific QA release; do not commit personal `options.txt`, saves or keybindings, and strip QA-only preference glue from stable packages.
