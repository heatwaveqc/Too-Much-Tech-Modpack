# Workstream, branch, and integration workflow

## Branch purposes

- **`main`**: bootstrap, project policies, reusable tooling, accepted documentation and controlled integration promotion. It is not automatically a stable game release.
- **`test/full-integration`**: unified mod roster, compatibility patches, configs and experimental source integration. It is not automatically server-tested or playable.
- **`feature/<scope>` / `research/<scope>` / `fix/<scope>`**: temporary, narrowly owned, reviewable workstreams. No other permanent branches without owner approval.

Start work from an up-to-date appropriate base. Feature PRs normally target `test/full-integration`, while policy/bootstrap PRs target `main`. Document cross-branch promotion explicitly. Avoid cherry-picking unowned changes or copying a stale manifest over fresh integration.

## Before implementation

1. Read `AGENTS.md`, applicable decisions, active issues/PRs/branches, current packwiz pins and existing implementation.
2. Reuse or take over the existing workstream with a clear handoff. One designated writer owns each shared file set.
3. Record the owner-approved scope and concrete acceptance criteria. Open issues for ideas, not speculative runtime commits.
4. If a mod is implicated, inspect compatible releases, exact dependency closure, distribution terms and native config behavior before introducing custom patches.

## Pull request lifecycle

Open a draft PR promptly after a meaningful first commit (within 24 hours), and keep the same PR across chat/session interruptions. Its description must state:

- Workstream/issue/decision link and responsible writer.
- Base/head branch and exact checkpoint SHA; file and config ownership.
- Changes, known limitations, dependencies and collisions with other workstreams.
- Quick CI evidence and exact tests not run.
- Next action and A/B/C in-game QA needed for acceptance.

Promote a coherent reviewed source slice when it is safe and already within approved scope; no separate full modded boot is required to merge source-only work. The integration owner reconciles shared manifests and packwiz hashes on current HEAD. Missing pins, incompatible mods, or unexplained changes are blockers, not automatic exclusions. Preserve commit provenance, update dependent PRs, and retire temporary branches deliberately without sweeping deletions.

## Mod intake phases

`proposed` → `researching` → `approved` → `pinned` → tested by independently recorded QA levels.

`held` and `excluded` are explicit states. An `approved` record is not necessarily present in the pack index. A `pinned` record must name its indexed packwiz metadata file and exact upstream version. The integration writer updates `index.toml` and `pack.toml` hashes using packwiz or an equivalent deterministic source-validated procedure.

## Routine automation

CI may validate TOML, JSON, packwiz hashes, manifest entries and isolated source tests. Repository metrics and branch reports may run read-only. No scheduled full builds, no silent mod updates and no unattended destructive branch cleanup. Full assembly, game boots, Prism ZIPs and stable releases are opt-in per [QA.md](QA.md).

GitHub branch protection and required status checks must be configured by an administrator in GitHub; these markdown policies **do not** themselves enable protection.
