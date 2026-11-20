# Quality assurance and build authorization

## Eight evidence levels

| Level | Name | What counts as evidence |
| --- | --- | --- |
| 1 | Repository CI | TOML/JSON validation, packwiz metadata and schema checks |
| 2 | Module CI | Isolated module compilation and unit tests |
| 3 | Integration Preflight | Dependency and source-level compatibility checks, with explicit limitations |
| 4 | Integration Assembly | Authorized full pack materialization, pinned dependency resolution |
| 5 | Server Boot Smoke | Authorized NeoForge dedicated server actually boots/loads the full pack |
| 6 | Prism QA Package | Authorized frozen Prism-importable package with provenance |
| 7 | Client Launch Smoke | The actual assembled client launches and connects as intended |
| 8 | Gameplay Acceptance | Required survival, progression, multiplayer and cross-mod behavior manually passes |

Passing one level **does not** imply higher levels. An indexed packwiz file alone is not a validated download. A server boot is not a successful client or gameplay run. A ZIP is not evidence that its client launched.

## Three test execution types

- **A — Offline/automation**: repository metadata, source, jars, configs, logs, static tests, compilation. Link inputs, commands and evidence.
- **B — In-game commands**: verified exact commands, permissions/cheats, expected output and cleanup instructions.
- **C — In-game gameplay**: actual crafting, UI interactions, machines, automation loops, combat, worldgen, multiplayer or survival setup.

Use A evidence first, then issue targeted B/C checklists for owner playtesting. Do not invent mod commands or report manual QA PASS from source-only evidence.

## Bootstrap state

Only level 1 is implemented by the repository's `Quick checks` workflow. Levels 2–8 are **NOT RUN / NOT IMPLEMENTED**. The mod list is empty. No stable, alpha, server-tested or client-tested snapshot exists.

## Authorization policy

- PR/push/schedule CI is **quick-only**. Never assemble the full mod roster, boot Minecraft, package Prism, or publish builds as a side effect.
- Full assembly and full server/Prism work need distinct explicit owner approval for that actual run, frozen revision and scope. An instruction to prepare or validate a build is not automatic consent to execute it.
- New build workflows must use manual dispatch with default-false approval inputs and exact manual-event gates, including in job-level conditions. No automatic retries and no bypass through reusable workflows.
- Before any approved full build, audit active pinned mod updates/dependencies, hold unverified breaking changes, run quick CI on the frozen SHA, and record exact file hashes.
- Candidate and stable promotion need their own reviewed acceptance criteria and explicit owner go-ahead; stable is immutable once designated.

## Evidence ledger format (future test passes)

Record: date, build/revision SHA, packwiz hash, test level, A/B/C type, test environment, steps/command, expected/observed result, PASS/FAIL/BLOCKED/NOT RUN, evidence link and owner. No empty success placeholders.
