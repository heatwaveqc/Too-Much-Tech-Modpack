# Canonical eight QA levels — Too Much Tech

Adopted from the sister project's [canonical test taxonomy](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/docs/qa/TEST-LEVELS-AND-TERMINOLOGY.md). Use these exact names and IDs in CI, PRs, test plans and release notes.

| ID | Level | Evidence of PASS | Typical gate | Must not imply |
| --- | --- | --- | --- | --- |
| CI-REPO | Repository CI | Static index, exact hash chain, schema/source/feature policy checks | Automatic push/PR | Java compiles, assembled pack, game boot |
| CI-MODULE | Module CI | Isolated module compile, unit and source checks | Automatic push/PR | Loaded world behavior |
| CI-PREFLIGHT | Integration Preflight | **Read-only** source/provenance/path/pin consistency, later verified frozen donor reachability | Automatic push/PR | Source assembly or complete runtime |
| QA-ASSEMBLY | Integration Assembly | Approved full source/roster staged with exact pins, donor SHAs and reproducible manifest | Manual owner opt-in | Server running or Prism ZIP tested |
| QA-SERVER | Server Boot Smoke | Exact assembled NeoForge dedicated server boots to ready and expected JARs loaded | Explicit owner approval for each run | Client GUI or real recipes |
| QA-PRISM | Prism QA Package | Frozen launcher ZIP has validated manifest, sources, hash chain, provenance | Explicit owner approval, after server success in canonical pipeline | ZIP imports or client launches |
| QA-CLIENT | Client Launch Smoke | Actual Prism instance resolves pack, launches GUI and enters disposable world | Explicit client QA | Survival mechanics, multiplayer |
| QA-GAMEPLAY | Gameplay Acceptance | Named craft/machine/power/automation/quest/multiplayer behavior demonstrated | Explicit play/testing | Other untested features or stable approval |

**Quick CI = CI-REPO + CI-MODULE (when present) + CI-PREFLIGHT.** A check not yet implemented is `NOT RUN`, not PASS. An empty source-lock schema check is a *bootstrap-level* preflight, not reachability validation of external donors.

## Status vocabulary

`NOT BUILT`, `SOURCE READY`, `PREFLIGHT PASS`, `ASSEMBLED`, `SERVER PASS`, `PRISM PACKAGED`, `CLIENT PASS`, `GAMEPLAY PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, `OWNER-DEFERRED`.

A "full integration test" is a **scope claim**, not a ninth level: every ready-for-live-test workstream must have an explicit included/blocked/owner-deferred outcome. A narrow/partial test cannot be represented as the entire comprehensive build without owner approval.

## Required provenance

Record: date, source HEAD, exact donor SHAs and pin versions, job/command/run link, OS/Java/loader and relevant environment, input fixtures, expected/observed outcome, applicable level ID, exact artifact and hashes (if created), resulting status, test owner and future A/B/C steps. For B/C include disposable-world identity and note whether cheating/OP/testing scaffolds were used.

No automatic full Minecraft assembly/boot/package/release. Preserve prior successful artifact for rollback and do not create fake PASS markers.
