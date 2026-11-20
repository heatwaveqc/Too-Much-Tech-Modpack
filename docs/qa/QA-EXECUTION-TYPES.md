# A / B / C QA execution types

Adopted from TMM's [2026-11-17 A/B/C standard](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/docs/qa/QA-EXECUTION-TYPES.md). These execution types complement, and **do not replace**, the [eight evidence levels](TEST-LEVELS-AND-TERMINOLOGY.md). Required for every test-build handoff.

| Type | Who/how | Required instructions | Boundary |
| --- | --- | --- | --- |
| **A — Codex / automated offline** | Read exact committed sources, packwiz, JAR manifests, copied saves, logs; use static validators and isolated unit/compile tests | File paths, frozen source SHA, exact commands and observed result | Cannot newly certify in-world behavior or start Minecraft |
| **B — in-game commands** | In an already authorized disposable world, use *verified* paste-ready commands plus minimal immediate physical actions | Starting mode, player/OP permissions, preparation, exact commands, expected changes/messages, cleanup | Actual runtime command-scoped evidence; not normal survival |
| **C — in-game play/setup** | Real crafting, machine networks, multi-block structures, automation, GUI, power/fluid flow, dimension travel, worldgen or multiplayer | Starting state, items/setup, steps, expected/observed result and persistence/reload checks | Only the named tested player behavior |

A first; hand B/C to the owner/player after reporting offline blockers. Break features into independently judgeable cases. Do not repeat previously accepted unchanged tests without a reason, but do retest behavior touched by version updates, overlapping changes or regression risk.

Use `PASS`, `FAIL`, `PARTIAL`, `BLOCKED`, `NOT BUILT`, `NOT RUN` with evidence. Never invent modded command names or claim operator-only QA rigs prove survival acquisition. Confirm exact command syntax from the installed pinned version; otherwise write `command not verified`. A test plan or downloaded ZIP is **not** consent to run a new server/client/build. No worlds, credentials, player preferences or personal logs in public repository.
