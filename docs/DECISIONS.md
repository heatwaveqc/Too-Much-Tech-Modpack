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
| TMT-0011 | 2026-11-20 | Owner-directed / conditional | Thermal Expansion | Include if a compatible release exists. Official Thermal Expansion/Foundation/Dynamics have no confirmed 1.21.1 NeoForge release; hold for now. FACTAS is now an explicitly targeted independent beta candidate, not an official Thermal port. |
| TMT-0012 | 2026-11-20 | Owner-directed / broad intent | TMM carryover | Port **most** food and QoL/performance conveniences from TMM after exact-version, dependency and non-magic-config review. All 56 researched TMM food/QoL entries are now targeted for future inclusion, subject to version/compatibility checks; no blanket approval for TMM-specific mechanics or old pins. |
| TMT-0013 | 2026-11-20 | Research only | Additional tech candidates | Recorded release metadata for Create, Immersive Engineering, PneumaticCraft, AE2/RS, Powah, Extreme Reactors, Ender IO, Industrial Foregoing, Ad Astra and others. None added to packwiz. |

| TMT-0014 | 2026-11-20 | Owner-directed | Target inclusion lock | Target all 102 previously surveyed technology and TMM food/QoL entries, explicitly including FACTAS and Draconic Evolution. This is an inclusion goal, not an installed/pinned artifact. Hold unavailable official Thermal modules and invalid version sources; include official Ender IO base with dependent Ender IO: Evolution addon after compatible-version verification. |
| TMT-0015 | 2026-11-20 | Research only | Cybernetic and mechanical mobs | Survey 12 robotic/cybernetic mob mods, including Cybernetics from Integrated Boogaloo. None is approved for installation yet. |

| TMT-0016 | 2026-11-20 | Research correction | Ender IO architecture | Ender IO: Evolution is an **unofficial Ender IO addon**, not a competing base mod. The 1.21.1 NeoForge Evolution 3.x line depends on official Ender IO 8.2.0+; target both base 8.2.14-beta and addon 3.1.6, with artifact/version verification before installation. |

| TMT-0017 | 2026-11-20 | Owner-directed | Inclusion philosophy | **Inclusive first pass.** Mechanical overlap, competing methods or duplicate upgrade functions alone are not reasons to exclude mods. Only actual incompatibility/bugs, unsupported game versions or comparable hard technical blockers justify withholding an included target; balance through configs and QA later. |
| TMT-0018 | 2026-11-20 | Owner-directed | Cybernetic expansion | Target **Cybernetics, Synthetics, Matter Overdrive (Unofficial Port), NeoSync, Create: Chromeware** in addition to existing Oritech. Research exact 1.21.1 NeoForge artifacts; exclude competing Matter Overdrive port JARs until selecting an implementation, not other enhancement mods solely for overlap. |
| TMT-0019 | 2026-11-20 | Owner-directed / deferred | Shared Progression | Target shared TMM `compat/progression` engine for TMT, with **Cyborg, Meatbag, Alien** as goal paths. Wait for upstream API/runtime readiness before source import. Preserve single engine with declarative TMT path packages, no fork or invented runtime PASS. Exclusivity, skill trees, reward triggers and biology providers undecided. |
| TMT-0020 | 2026-11-20 | Research only | Thematic dimensions and planets | Survey 20 1.21.1-target dimension/procedural-space candidates. Ad Astra already targeted; extra candidates are **not** auto-selected by a survey request. Investigate custom Ad Astra planet JSON plus worldgen, and true runtime procedural alternatives with hard technical QA gates. |

| TMT-0021 | 2026-11-20 | Owner-directed | Planet/dimension inclusion goals | **Primary targeted:** Ad Astra: Planets, Stargate Journey, RFTools Dimensions, Infinite Dimensions, Deep Space (Unofficial Port). **Targeted isolated experiments:** MACHINA and Create: Universe. Existing Ad Astra remains targeted. All seven are goals, **not** installed packwiz JARs; experiment outcomes, version/dependency checks, stable save/restart, return routes and performance required before promoting their implementation. Overlap alone is not disqualifying. |

See [DESIGN.md](DESIGN.md) for the specific choices awaiting discussion.
