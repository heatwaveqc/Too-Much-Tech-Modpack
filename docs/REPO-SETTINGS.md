# GitHub repository settings — manual owner checklist

This document describes controls that **repository files alone cannot enforce**. Initial bootstrap was completed through the GitHub connector, whose file/PR capabilities do not write GitHub administration settings. The items below are **not confirmed enabled**.

## Protect permanent branches

In GitHub **Settings → Rules → Rulesets** (or branch-protection rules):

- [ ] Apply appropriate protection to `main` and `test/full-integration`.
- [ ] Block force pushes and accidental deletion of protected branches.
- [ ] For PRs, require the **Verify bootstrap / metadata** CI job once GitHub has discovered the check on both branches.
- [ ] Decide how to enforce PR review given the repository may have a single owner; do not configure an impossible self-review requirement.
- [ ] Choose bypass permissions deliberately for the owner and any integration automation; do not allow broad unreviewed bot force pushes.

## Workflow and security review

- [ ] Confirm GitHub Actions is enabled for the repository and default `GITHUB_TOKEN` permissions are minimal.
- [ ] Confirm required checks run on PRs targeting each permanent branch. Current `quick-checks.yml` has read-only token permissions and checks both packwiz and integration-source/evidence schemas.
- [ ] Review `.github/CODEOWNERS`; remember it is advisory until an enforced ruleset requires review.
- [ ] Verify `branch-lifecycle-report.yml` only has read permissions. It runs a scheduled branch inventory and on-PR collision checks; it **never** deletes branches or builds Minecraft.
- [ ] Confirm GitHub Actions schedule runs on the default branch, not on a moving external feature branch.
- [ ] If adding a full-build command console later, implement a fresh TMT-scoped owner-ID, exact-SHA, nonce/receipt, replay, read-only check and audit contract. Do **not** reuse TMM's issue IDs or /tmm commands.
- [ ] Keep full modded assembly/boot/Prism publication workflows **absent** until an explicitly authorized, manual opt-in workflow exists.
- [ ] Review whether to enable automatic deletion of source branches after meaningful PR merges; preserve dependent PRs and source provenance first.
- [ ] Review repository visibility and secrets. The project is currently **public**; no secrets should be committed.
- [ ] Decide an original-content `LICENSE` file before publishing reusable code/assets. Do not conflate the pack's license with third-party mod redistribution rights.

## Known starting state

- `main` and `test/full-integration` both existed and passed `Verify bootstrap / metadata` on 2026-11-20.
- [Main run](https://github.com/heatwaveqc/Too-Much-Tech-Modpack/actions/runs/44813083684).
- [Integration run](https://github.com/heatwaveqc/Too-Much-Tech-Modpack/actions/runs/44813094904).
- No branch protection, required-check enforcement, review rules, or licensing decisions are claimed as configured by this document. The report workflow is read-only, not a retirement executor.
