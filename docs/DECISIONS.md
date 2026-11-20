# Decision log

This ledger separates confirmed owner direction, bootstrap technical assumptions, and unresolved questions. Add an ID, date, decision authority, rationale, alternatives and follow-up for substantive changes. Do not upgrade a *provisional* item to *approved* without owner direction.

| ID | Date | State | Subject | Decision / current assumption |
| --- | --- | --- | --- | --- |
| TMT-0001 | 2026-11-20 | Owner-directed | Project | Create a distinct Too Much Tech modpack repository. |
| TMT-0002 | 2026-11-20 | Bootstrap provisional | Version | Start with Minecraft 1.21.1, NeoForge 21.1.265 and Java 21 for familiar tooling; reassess before roster selection. |
| TMT-0003 | 2026-11-20 | Bootstrap provisional | Tooling | packwiz for declarative indexing; Prism for eventual test delivery; Python standard-library repository validator. |
| TMT-0004 | 2026-11-20 | Bootstrap process | QA safety | Automate lightweight static checks; require distinct owner authorization for full assembly/boot/package/release. |
| TMT-0005 | 2026-11-20 | Owner-directed | Core tech roster | Oritech, Just Dire Things (JDT), Mekanism and Draconic Evolution are intended inclusions; published 1.21.1 NeoForge builds exist, but none is pinned/installed in TMT. Draconic's 1.21.1 release is beta. |
| TMT-0006 | 2026-11-20 | Owner-directed | Progression tone | Fun with tech; explicitly **not** a GregTech pack or deliberately grindy slog. Power, storage and system overlap decisions remain open. |
| TMT-0007 | 2026-11-20 | Open | Licensing | License for new original repository content and rights for redistributed mod assets must be determined. |
| TMT-0008 | 2026-11-20 | Bootstrap process | Branches | Use `main` for accepted foundation and `test/full-integration` for source integration; temporary scoped PR branches. |
| TMT-0009 | 2026-11-20 | Owner-directed | Sister-project development policy | Adopt the mature TMM governance, frozen donor, QA, build authorization, branch hygiene, inclusion and quest-teaching methods; adapt to TMT without copying magic-only gameplay or old command consoles. See [parity map](SISTER-PROJECT-PARITY.md). |
| TMT-0010 | 2026-11-20 | Bootstrap process | Safe reporting | A read-only daily branch inventory and PR collision advisory is permitted; no automatic branch deletion or full build authorization. |
| TMT-0011 | 2026-11-20 | Owner-directed / conditional | Thermal Expansion | Include if a compatible release exists. Official Thermal Expansion/Foundation/Dynamics have no confirmed 1.21.1 NeoForge release; hold for now. FACTAS is a separate beta candidate, not a replacement approval. |
| TMT-0012 | 2026-11-20 | Owner-directed / broad intent | TMM carryover | Port **most** food and QoL/performance conveniences from TMM after exact-version, dependency and non-magic-config review. No blanket approval for individual TMM mechanics or old pins. |
| TMT-0013 | 2026-11-20 | Research only | Additional tech candidates | Recorded release metadata for Create, Immersive Engineering, PneumaticCraft, AE2/RS, Powah, Extreme Reactors, Ender IO, Industrial Foregoing, Ad Astra and others. None added to packwiz. |

See [DESIGN.md](DESIGN.md) for the specific choices awaiting discussion.
