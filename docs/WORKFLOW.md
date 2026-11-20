# Too Much Tech — workstream and integration workflow

Canonical procedure: [branch lifecycle](BRANCH-LIFECYCLE.md), [source locks](INTEGRATION-SOURCES.md), [agent contract](../AGENTS.md) and [build channels](BUILD-CHANNELS-AND-TESTING.md). These adapted TMM standards supersede the earlier short bootstrap workflow.

- **main** is accepted policy/bootstrap, not stable. **test/full-integration** is the single changing source integration branch, not a boot-tested pack. Temporary research/feature/fix/policy branches use scoped PRs.
- Discover current PRs/issues/branches/source pins before starting. Reuse prior chats' workstreams, one writer per shared branch/path. Draft/ready PR within 24 hours. Each handoff states owner, scope, exact SHA, owned files, dependencies, checks, blockers, next step.
- Feature branches own isolated source/data; a designated integration writer owns shared packwiz, manifests, cross-mod configs/quest runtime, collisions and frozen source promotions. New shared runtime behavior belongs in the designated engine module, not hidden feature-specific executable code. Add subsystem branches only when approved.
- Approved coherent source PRs may be merged without per-merge owner approval after current-head quick CI, provenance and collisions review. **Never conflate merge with server or gameplay PASS.** New gameplay decisions/major roster selections need owner direction.
- Mod intake progresses proposed → researching → approved → pinned. `pinned` requires exact indexed packwiz file, still not runtime evidence. Later test levels are separately evidenced. Track features in `manifest/feature-checklist.json` and ready live tests in `manifest/live-test-inclusion.json`.
- Do not run source assembly, server smoke, Prism build, release, or destructive cleanup merely because a PR passed. These use explicit owner authorization per run/batch.
- Finish by reconciling integration source-locks, QA obligations and branch retention. Budget <=20 normal, 21–30 review, >30 maintenance, advisory only. Daily read-only inventory/collision report is permitted.

Refer to [TMM parity mapping](SISTER-PROJECT-PARITY.md) for adopted versus deliberately excluded procedures.
