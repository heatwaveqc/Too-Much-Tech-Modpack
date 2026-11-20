# Ready-for-live-test inclusion register

Based on [TMM's inclusion contract](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/docs/qa/LIVE-TEST-INCLUSION-REGISTER.md), but starts with **no active tech features**.

An agent/chat/issue/PR that says "ready for next test build", "ready to playtest", "next integration target", "source ready for live QA" or equivalent must add the case to `manifest/live-test-inclusion.json` (and link the PR/issue). This is **not an authorization to start a build** and not a test PASS.

Before **each** comprehensive owner-authorized full build, the integration writer reconciles all reported-ready features including those not previously registered; each must be:

- `included` — exact source paths, mod pins and frozen SHAs are present in the candidate and verification attempted;
- `blocked` — evidence-backed technical blocker, with owner-facing scope consequence;
- `owner_deferred` — explicit owner approval for omitting this ready item from **this specific run** only;
- `pending` — entry awaiting reconciliation; **not acceptable** for a claimed fully reconciled test scope.

A previous "deferred pending runtime" or owner deferral does not automatically carry forward to subsequent comprehensive builds. Reconcile newly finished feature work every time. The register represents *scope and inclusion*, not in-game test outcomes. Those go in [current test results](CURRENT-TEST-STATUS.md) and [feature acceptance](../../manifest/feature-checklist.json).

## Current state

`manifest/live-test-inclusion.json` has no entries. No assembled Tech test candidate exists, so nothing has been included or deferred. A future data entry needs stable `id`, `title`, `status`, `source_commit` (if available), linked workstream, evidence/reason and per-build outcome when applicable.

Owner omissions and build-level authorization remain separate explicit decisions under [AGENTS.md](../../AGENTS.md). Do not treat an inclusion audit as permission to dispatch.
