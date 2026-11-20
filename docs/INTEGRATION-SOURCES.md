# Frozen integration sources and write authority

This adapts Too Much Magic's immutable source-donor contract without importing its historical feature streams, old implementations, or assembly workflow. At TMT bootstrap the register is intentionally empty.

## Manifest

`manifest/integration-sources.json` has:

- `schema: 1`, `baseline: "test/full-integration"`, `channel: "integration"`, and `streams: []`.
- Each nonempty stream requires `name`, `branch`, `source_commit` (full 40-hex immutable SHA), `paths` (explicit owned relative file paths or narrowly scoped paths), `mode`, `note`, and `integrated_into_baseline`.
- `branch` records the currently relevant source ref; it is **not** permission to fetch its moving HEAD as the candidate source. Use the exact frozen `source_commit`.
- For baseline-owned streams, use `integrated_into_baseline: true` and `branch: "test/full-integration"`; retain `merged_from`, `merged_pr` and `merged_commit` where applicable so deleted branches do not erase provenance.
- New external donors must stay independent until reviewed, with a unique named owner, exact SHA, dependency/prerequisite and a justified `mode`. Paths that collide with existing baseline/shared ownership cannot be overwritten without an explicit path-specific reviewed override.
- Do not duplicate path ownership among live external streams. If source is removed or superseded, retain source history/decision link, update manifest and dependent PRs before retiring refs.

A read-only validator checks schema, SHA shape, path safety and duplicate ownership. It does **not** download donor commits or assemble source. Before any real assembly, extend it to verify GitHub commit reachability, donor path membership, divergence and explicit approved overrides against exact SHA. If no safe verification exists, block assembly rather than guessing.

## Integration checkpoints

A reviewed PR to `test/full-integration` freezes the new candidate source, packwiz index, mod register, conflicts resolved, and feature inclusion register. The integration writer is the only person merging/writing shared manifest and packwiz lock data. A green preflight means **read-only preflight success**, not executable behavior.

Ordinary pushes/PRs must not assemble donors or resolve the full mod roster. The eventual Integration Assembly runner must be manual, opt-in and detached from automatic quick CI. See [QA](qa/TEST-LEVELS-AND-TERMINOLOGY.md) and [build channels](BUILD-CHANNELS-AND-TESTING.md).
