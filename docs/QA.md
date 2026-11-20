# Too Much Tech — QA and authorization entry point

**Use [the QA hub](qa/README.md) for live testing and records.** Adapted from Too Much Magic's current test taxonomy and owner-approved build authorization contracts.

Eight levels are [documented here](qa/TEST-LEVELS-AND-TERMINOLOGY.md): (1) Repository CI, (2) Module CI, (3) Integration Preflight (quick/read-only), (4) Integration Assembly, (5) Server Boot Smoke, (6) Prism QA Package, (7) Client Launch Smoke, (8) Gameplay Acceptance. Do not infer later levels from earlier PASS.

Every live-test handoff uses [A/B/C execution types](qa/QA-EXECUTION-TYPES.md), linked to exact frozen sources and a test evidence ledger. First run offline A checks, then give verified command-based B tests and genuine manual C gameplay setups. No invented command syntax.

**Owner approval is required per full execution** for assembly, full NeoForge server boot, Prism package and release. No push/PR/schedule-triggered builds or automatic retries; new build workflow must be gated by explicit manual event + default-false owner opt-in. A full build request first triggers a read-only update review of the active pinned mod roster, dependency verification, quick CI, frozen SHA and rollback documentation. It never automatically approves scope expansion or broken-mod exclusions.

Comprehensive QA must account for **all** work ready for live testing with [inclusion register](qa/LIVE-TEST-INCLUSION-REGISTER.md). Each entry must be included, evidence-blocked or owner-deferred for the specific run. Preserve previous acceptance evidence and run only meaningful regressions.

At bootstrap, no Minecraft server/client or assembly has been run. See [current test status](qa/CURRENT-TEST-STATUS.md) and [build channels](BUILD-CHANNELS-AND-TESTING.md).
