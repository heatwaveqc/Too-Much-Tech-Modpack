# Decision log

This ledger separates confirmed owner direction, bootstrap technical assumptions, and unresolved questions. Add an ID, date, decision authority, rationale, alternatives and follow-up for substantive changes. Do not upgrade a *provisional* item to *approved* without owner direction.

| ID | Date | State | Subject | Decision / current assumption |
| --- | --- | --- | --- | --- |
| TMT-0001 | 2026-11-20 | Owner-directed | Project | Create a distinct Too Much Tech modpack repository. |
| TMT-0002 | 2026-11-20 | Bootstrap provisional | Version | Start with Minecraft 1.21.1, NeoForge 21.1.265 and Java 21 for familiar tooling; reassess before roster selection. |
| TMT-0003 | 2026-11-20 | Bootstrap provisional | Tooling | packwiz for declarative indexing; Prism for eventual test delivery; Python standard-library repository validator. |
| TMT-0004 | 2026-11-20 | Bootstrap process | QA safety | Automate lightweight static checks; require distinct owner authorization for full assembly/boot/package/release. |
| TMT-0005 | 2026-11-20 | Open | Mod roster | No tech, worldgen, QoL or progression mod has been approved, pinned, or installed. |
| TMT-0006 | 2026-11-20 | Open | Progression | Power, automation, storage, machines, gating and endgame design remain unspecified. |
| TMT-0007 | 2026-11-20 | Open | Licensing | License for new original repository content and rights for redistributed mod assets must be determined. |
| TMT-0008 | 2026-11-20 | Bootstrap process | Branches | Use `main` for accepted foundation and `test/full-integration` for source integration; temporary scoped PR branches. |

See [DESIGN.md](DESIGN.md) for the specific choices awaiting discussion.
