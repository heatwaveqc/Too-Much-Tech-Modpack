# Branch lifecycle, integration authority and clean retirement

Adapted from TMM's owner-approved 2026-11-19 [branch lifecycle](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/main/docs/BRANCH-LIFECYCLE.md). TMT scope is independent and its permanent branch allowlist is intentionally smaller. This document supplements [AGENTS.md](../AGENTS.md).

## Before writing

Search active PRs, issues, branches, the integration-source lock, releases and existing code. Reuse an active workstream even after a failed conversation. One writer per shared branch/path group. Branches represent reviewable scoped changes rather than individual chats/checkpoints; ideas go in issues.

A temporary branch must have a draft or ready PR within 24 hours, preferably immediately. Include writer, linked issue/decision, target base, owned paths, current exact SHA, dependency stack, quick checks, blockers, accepted scope, and next action. Keep handoff current. Do not continue writing on a branch with another designated writer without an explicit ownership handoff.

## Branch tiers and ownership

- `main`: accepted policy, common tooling, baseline source history. **Not a proven stable pack.**
- `test/full-integration`: shared modpack integration, the latest candidate source, manifest and config reconciliation. **Not a proven playable pack.**
- Temporary `feature/*`, `fix/*`, `policy/*`, `research/*`, `maintenance/*`: owned PR branches with a concrete scope.
- Future long-lived subsystem branches (for example `dev/automation`) require owner approval, a designated writer, documented promotion path and a single runtime-code owner. Do **not** automatically copy TMM's `dev/progression` / `dev/art` branch topology.

Module writers own their own executable code and tests. Feature configs should remain declarative where practical; shared engine changes belong with the engine owner. The designated integration writer exclusively reconciles shared packwiz, configs, quests, sources, version locks and cross-module compatibility. No concurrent writers on the integration branch.

## Continuous delivery of safe slices

The integration writer may reconcile and merge already-approved coherent source changes, routine fixes and metadata after checking current heads, CI and source provenance. No full game boot is necessary merely to merge source changes. Do not let clean CI masquerade as gameplay acceptance. New design choices, major roster shifts, balancing/architecture and run authorizations remain with the owner.

Inspect PR base and head SHAs just before merge; reconcile collision reports manually, require applicable quick CI and meaningful PR description. Prefer reviewed PRs to direct writes on shared branches; never replace shared directories from old donors or bypass branch protection.

When merging or retiring donor work, move the integration-source record to baseline-owned, preserve source commit/merged_from/PR/merge commit, retarget dependent PRs before deleting their base, and ensure every ready-for-live-test item is still tracked. Do not let automatic GitHub source-branch cleanup break unreconciled dependencies.

## Completion and branch budget

Workstream completion means: source integrated or explicitly deferred, decisions and tests documented, dependency/source locks reconciled, and temporary head retired or retained with named owner/review date. Do not abandon finished PR branches indefinitely.

Permanent branch allowlist: `main`, `test/full-integration`. Target remote branch count <=20, review 21–30, maintenance >30. Review triggers: 24h without PR, 24h ready waiting, 72h inactive development, 24h after meaningful merge with surviving ref, 7d unresolved donor. These are advisory and not automatic consent to delete.

A scheduled read-only [branch inventory](../.github/workflows/branch-lifecycle-report.yml) may report branch tips, open PRs, integration donor references and duplicate changed paths; it cannot merge/delete and cannot prove runtime acceptance. Age computed from last commit is only a proxy for activity, not time since the last chat or review.

## Retirement procedure: reviewed exact-SHA batch only

1. Inventory candidate refs and compare against integration source-locks, protected branches, all open PR heads **and bases**, dependent source branches, accepted merged history and QA readiness obligations.
2. Preserve useful source, dependency chains and immutable provenance before nomination. If otherwise unreachable, archive exact history through an owner-reviewed immutable Git tag; verify reachability before deletion.
3. Prepare a **new** batch-specific manifest in `maintenance/branch-retirement/<batch>.json` with each exact ref name, full 40-hex head SHA, reason and evidence. Review on a dedicated maintenance PR; never reuse a historical TMM batch or assume all old branches are disposable.
4. Perform a read-only dry run against current live refs, re-check SHA, PR dependencies and frozen donors. Explicitly exclude anything active, protected, ambiguous or changed.
5. Obtain owner approval **for that specific verified batch and digest**. Only then may a separate manual execution workflow be developed/used with lease-guarded per-ref delete and final verification. A merged manifest or generic cleanup policy is not approval to run deletion.
6. Verify archived commits, deleted/skipped refs, surviving allowed branches, and record operation provenance. Do not replay uncertain outcomes or create dummy PRs solely to retire old branches.

**At bootstrap no destructive branch retirement workflow, deletion console or approved batch exists.** The read-only lifecycle report is the only implemented maintenance automation.

## GitHub administration

Branch protection, PR review requirements, automatic source branch deletion and Actions permissions need explicit GitHub Settings configuration. The CODEOWNERS file is advisory until enforced by a ruleset. See [docs/REPO-SETTINGS.md](REPO-SETTINGS.md).
