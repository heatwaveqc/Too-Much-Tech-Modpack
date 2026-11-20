# Too Much Tech — QA hub

**Working integration branch:** `test/full-integration`. Initial environment: Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21 (provisional).

## Starting points

- [Canonical eight test levels](TEST-LEVELS-AND-TERMINOLOGY.md) — exact names and what each PASS proves.
- [Mandatory A/B/C execution handoff](QA-EXECUTION-TYPES.md) — offline analysis, exact in-game commands and real play/setup.
- [Live-test inclusion register](LIVE-TEST-INCLUSION-REGISTER.md) — promises to test must be reconciled against the next comprehensive test.
- [Acceptance status registry](../../manifest/feature-checklist.json) — durable evidence-backed feature state, currently empty.
- [Build channels](../BUILD-CHANNELS-AND-TESTING.md), [frozen source contract](../INTEGRATION-SOURCES.md), [agent policy](../../AGENTS.md).
- [Bootstrap QA status](CURRENT-TEST-STATUS.md) — actual evidence/limitations of the latest tested snapshot.

## Operating procedure

1. Read current integration SHA, actual packwiz index/manifest and frozen source lock. A PR reported SOURCE READY may not yet be installed in the artifact.
2. Before proposing a comprehensive build, search all chats/PR handoffs/issues/branch references for reported ready-for-test work; reconcile every one in inclusion register as INCLUDED / BLOCKED with evidence / explicit OWNER-DEFERRED.
3. Start with existing A offline source/fixture/log results. Do not run any Minecraft process without the relevant new owner authorization.
4. Prepare B commands only after verifying syntax in actual installed mod/version, required permissions, expected output and cleanup in disposable world. If unknown, mark unverified; **do not invent commands**.
5. Prepare C gameplay setup for machines, wiring, energy transfer, worldgen, UI, progression and multiplayer. Never equate spawned creative components with ordinary survival acquisition.
6. Use separate test IDs and PASS/FAIL/BLOCKED/NOT RUN statuses per QA level and feature, with exact run/build SHA and evidence. Preserve accepted prior results, rerun only changed/affected behavior.
7. Report test constraints and what's not yet run. No auto Stable promotion or gameplay PASS by extrapolation.

**At bootstrap:** metadata CI is tested; Module CI and full modded stages are unrun. There is no actual server/client test, game build, Prism ZIP or accepted gameplay feature.
