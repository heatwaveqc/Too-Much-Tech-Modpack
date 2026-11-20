# TMM → TMT engineering policy adoption

**Audit date:** 2026-11-20. TMM sources inspected on its `main` and `test/full-integration` branches. This is a deliberate **fork of methods, not cross-repository authority**. TMT's own files are definitive for TMT changes. There is no automatic future sync.

## Adopted now

| Proven TMM practice | TMT implementation |
| --- | --- |
| Repository-wide agent contract | `AGENTS.md` |
| Continuous single-writer PR delivery, interrupted-chat recovery, scoped feature branches, branch budget | `docs/BRANCH-LIFECYCLE.md`, PR template |
| Frozen donor SHAs, path ownership, no stale directory replay, preflight versus assembly | `manifest/integration-sources.json`, `docs/INTEGRATION-SOURCES.md`, static validation |
| Integration, Candidate, Stable and intentionally separate rolling unstable QA | `docs/BUILD-CHANNELS-AND-TESTING.md` |
| Eight evidence-bounded test levels, mandatory A/B/C handoff | `docs/qa/TEST-LEVELS-AND-TERMINOLOGY.md`, `docs/qa/QA-EXECUTION-TYPES.md` |
| Explicit owner gate for complete assembly/smoke/Prism; no automatic retries | `AGENTS.md`, `docs/QA.md`, CI workflow |
| Every ready feature attempted or owner-deferred in next comprehensive QA | `docs/qa/LIVE-TEST-INCLUSION-REGISTER.md` |
| Feature and test evidence separated, no fabricated PASS | `manifest/feature-checklist.json`, validation, QA hub |
| Daily branch inventory and PR changed-path collision warnings | read-only GitHub Actions lifecycle report |
| Safe SHA-guarded branch retirement only by batch-specific owner approval | documented procedure; no deletion workflow installed |
| Practical complete-mod walkthrough quests and no fake quest completion | `docs/QUEST-WALKTHROUGH-STANDARD.md` |
| License/pin/source provenance and native-config-first integration | `docs/COMPATIBILITY.md`, `AGENTS.md` |

## Deliberately not copied

- Magic-specific mods, constraints, dimensions, pathways, economy balance, food rules, rites or quest content.
- `dev/progression`, `dev/art`, class-path branch ownership, TMM Java module boundaries, and TMM's historical branch allowlists.
- Build-and-smoke scripts, workflows that download hundreds of mods, Prism artifacts, release tags, frozen B-series snapshots, hashes and prior gameplay test results.
- TMM command consoles, bridge issue IDs, nonce formats, retirement batch manifests or tokens. Those are **repository-specific security controls**.
- Assumption that a feature accepted in TMM is selected for TMT. Shared code requires explicit license/ownership/version approval.

## Parity upgrades that remain conditional

When the first actual donor stream exists: implement a comprehensive read-only remote commit/diff/pin verification and narrow, owner-authorized assembly procedure, instead of treating the current local schema validator as complete Integration Preflight.

When a validated full pack exists: add manual-only assembly/server/prism workflows, immutable candidate metadata, QA-only preference handling and separately guarded rolling unstable publication. Future full builds still require fresh owner permission.

When a module merits its own long-lived development branch: establish an explicit single writer and runtime/config separation with a promotion PR to integration. When remote branch counts grow: develop reviewed SHA-allowlist retirement tooling but **not scheduled deletion**.

## Source references

- [TMM agent contract on main](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/main/AGENTS.md)
- [TMM active integration agent contract](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/AGENTS.md)
- [TMM branch lifecycle](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/main/docs/BRANCH-LIFECYCLE.md)
- [TMM source manifest](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/manifest/integration-sources.json)
- [TMM test-level standard](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/docs/qa/TEST-LEVELS-AND-TERMINOLOGY.md)
- [TMM A/B/C execution standard](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/docs/qa/QA-EXECUTION-TYPES.md)
- [TMM quest walkthrough standard](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/docs/QUEST-WALKTHROUGH-STANDARD.md)
