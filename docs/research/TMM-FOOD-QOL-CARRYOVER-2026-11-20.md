# TMM → TMT food, quality-of-life and performance carryover survey

**Date:** 2026-11-20. **Authoritative donor snapshot:** [TMM `test/full-integration` mod register](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/manifest/mods.json), [packwiz index](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/index.toml), inspected around revision `7d1be155bf1334995b65ebe88566bd4d7ae54635`.

TMT owner intent is to port **most** food/QoL from TMM, not necessarily every odd edge case. The register below includes **56** TMM records from food (9), beverages (2), QoL (37), performance (5), server utilities (2) and compatibility (1). Two old unpinned/retired proposal records (`construction-gadgets` and `formation-wand`) were deliberately **not** carried over as active candidates.

**This is an intake ledger, not a 56-mod installation.** Even records apparently indexed by TMM do not automatically carry tested version/QA evidence into a new pack.

## Food baseline recommended to carry over

- **Pam's HarvestCraft 2 quartet**: Food Core, Crops, Trees, Food Extended. Retain their ingredient breadth and renewable farm complexity without forcing 100-step food chains.
- **Farmer's Delight**, **My Nether's Delight**, **Cooking for Blockheads**, **Farming for Blockheads**, **Aquaculture 2** — all have metadata pins in TMM's current index and are compelling in a tech pack, particularly automated kitchens, bulk farms, food-processing factories and fishing.
- **Harvest with Ease** (filed under QoL in TMM) is important for replant-compatible farm harvesting. Check Pam's/Farmer's multi-stage crops and automated harvesters; do not assume no item duplication.
- **Brewin' and Chewin' / Cocktails Delight** are optional theme extras; check whether they fit tech-oriented agriculture and brewing rather than making them mandatory.
- **Recipe/tag bridges:** inspect existing TMM food cross-compat data and take **only reusable, non-magic-specific recipes/tags** with clear licensing/ownership, tests and one designated integration writer. Do not copy species diet restrictions, vampiric food logic or magical progression.

## QoL baseline

Strong candidates include JEI, Jade, AppleSkin, Mouse Tweaks, Inventory Tweaks—ReFoxed, Crafting Tweaks, Controlling, Polymorph, Just Zoom, TrashSlot, Clumps, Comforts, Leaves Be Gone, HT's TreeChop, Harvest with Ease, Nature's Compass, More Overlays, Lootr, Default Options, Simple Backups, spark and standard performance tooling.

Preserve `Almost Unified` as a **tool for ore/tag data ownership**, but its TMM material selection must be rebuilt for Mekanism/Oritech/Create/Immersive Engineering, not copied wholesale. KubeJS and FTB Quests/FTB Chunks have their own shared-infrastructure research records; only install what the approved feature architecture requires.

### Important exceptions and conflict review

- **Get It Together, Drops!** — TMM's supplied download URL contains `neoforge-1.21.5-1.4.jar` even though TMM targets 1.21.1. This is a **version red flag**. Held until the exact artifact/JAR metadata is checked. Do not transfer the existing pin blindly.
- **Corail Tombstone vs Smart Keep Inventory:** both influence death/recovery. Decide policy and verify compatibility; TMM's Newbie/boss-specific KubeJS data is not transferable by default.
- **Akashic Tome and Oracle Index:** may be handy with multiple mod manuals and ore tables, but evaluate tech-specific benefits before selecting.
- **KeyBind Bundles vs KeySets:** avoid duplicating controls and unnecessary startup/key conflicts; choose coherent defaults after client tests.
- **More Darkness:** optional presentation/gameplay change, not baseline neutral QoL.
- **Bountiful:** relevant to a bounty/contract shop, but TMM's custom magic rewards and beta dependencies are not direct Tech defaults.
- **Prefab:** optional prefabricated buildings; avoid importing magic-themed prefab structures or rights-restricted templates.
- **Performance tools:** TMM documents Embeddium, ModernFix, ImmediatelyFast, Entity Culling and FerriteCore. Recheck every exact NeoForge version and interactions before copying. Some appear under different file names than their manifest IDs; don't equate naive name matching to true absence.
- **TMM-specific modded worldgen/skills/magic:** not part of this carryover request. Food/survival/decor mods may have library dependencies; research closure rather than copying the whole 60+ dependency list.

## Audit inventory

`tmm_index_path_detected` is a **simple same-name path check**, not an authoritative installed or launch-tested field. For example, `ferrite-core.pw.toml` may differ from a manifest ID such as `ferritecore`. All the historical version strings are candidates for upstream update review.

### food — 9

| Mod | TMM observed version | Index match* | Port tier | Status |
|---|---|---|---|---|
| [Aquaculture 2](https://www.curseforge.com/minecraft/mc-mods/60028) | Aquaculture-1.21.1-2.7.22 | index match | strong | researching |
| [Cooking for Blockheads](https://modrinth.com/mod/cooking-for-blockheads/version/MQCIy6VF) | 21.1.24+neoforge-1.21.1 | index match | strong | researching |
| [Farmer's Delight](https://www.curseforge.com/minecraft/mc-mods/398521) | FarmersDelight-1.21.1-1.3.4 | index match | strong | researching |
| [Farming for Blockheads](https://www.curseforge.com/minecraft/mc-mods/261924) | farmingforblockheads-neoforge-1.21.1-21.1.14 | index match | strong | researching |
| [My Nether's Delight](https://www.curseforge.com/minecraft/mc-mods/my-nethers-delight/files/8854319) | MyNethersDelight-1.21.1-1.10.4.1.jar | index match | strong | researching |
| [Pam's HarvestCraft 2 — Crops](https://www.curseforge.com/minecraft/mc-mods/361385) | pamhc2crops-NEOFORGE-1.21.1-1.0.9 | index match | strong | researching |
| [Pam's HarvestCraft 2 — Food Core](https://www.curseforge.com/minecraft/mc-mods/372534) | pamhc2foodcore-NEOFORGE-1.21.1-1.0.4 | index match | strong | researching |
| [Pam's HarvestCraft 2 — Food Extended](https://www.curseforge.com/minecraft/mc-mods/402231) | pamhc2foodextended-NEOFORGE-1.21.1-1.0.0 | index match | strong | researching |
| [Pam's HarvestCraft 2 — Trees](https://www.curseforge.com/minecraft/mc-mods/365460) | pamhc2trees-NEOFORGE-1.21.1-1.0.9 | index match | strong | researching |

### food beverage — 2

| Mod | TMM observed version | Index match* | Port tier | Status |
|---|---|---|---|---|
| [Brewin' And Chewin'](https://modrinth.com/mod/brewin-and-chewin/version/MbcR48Ou) | 4.5.0+1.21.1-neoforge | index match | optional | researching |
| [Cocktails Delight](https://www.curseforge.com/minecraft/mc-mods/cocktails-delight/files/9482953) | Cocktails-Delight-1.21.1-NeoForge-1.1.12.jar | index match | optional | researching |

### qol — 37

| Mod | TMM observed version | Index match* | Port tier | Status |
|---|---|---|---|---|
| [Akashic Tome](https://www.curseforge.com/minecraft/mc-mods/250577) | AkashicTome-1.8-30 | index match | optional | researching |
| [AppleSkin](https://modrinth.com/mod/EsAfCjCV) | appleskin-neoforge-mc1.21-3.0.9 | index match | standard | researching |
| [AttributeFix](https://www.curseforge.com/minecraft/mc-mods/attributefix/files/7115922) | attributefix-neoforge-1.21.1-21.1.3 | index match | standard | researching |
| [Better Advancements](https://www.curseforge.com/minecraft/mc-mods/272515) | BetterAdvancements-NeoForge-1.21.1-0.4.3.21 | index match | strong | researching |
| [Bountiful](https://modrinth.com/mod/bountiful/version/swTb6NU9) | 8.0.0-beta.2 | index match | optional | researching |
| [Clumps](https://modrinth.com/mod/Wnxd13zP) | 19.0.0.1 | index match | standard | researching |
| [Colorful Hearts](https://modrinth.com/mod/colorful-hearts/version/us0gze50) | 10.5.9 | index match | optional | researching |
| [Comforts](https://modrinth.com/mod/comforts/version/3kpPjcTc) | comforts-neoforge-9.0.5+1.21.1 | index match | strong | researching |
| [Controlling](https://modrinth.com/mod/xv94TkTM) | Controlling-neoforge-1.21.1-19.0.5 | index match | standard | researching |
| [Corail Tombstone](https://modrinth.com/mod/YT5K34AB) | tombstone-neoforge-1.21.1-9.5.6 | index match | optional | researching |
| [Crafting Tweaks](https://www.curseforge.com/minecraft/mc-mods/233071) | craftingtweaks-neoforge-1.21.1-21.1.11 | index match | standard | researching |
| [Default Options](https://modrinth.com/mod/WEg59z5b/version/1zt17WsC) | defaultoptions-neoforge-1.21.1-21.1.8 | index match | strong | researching |
| [Enchantment Descriptions](https://www.curseforge.com/minecraft/mc-mods/250419) | enchdesc-neoforge-1.21.1-21.1.11 | index match | standard | researching |
| [Extreme Sound Muffler](https://modrinth.com/mod/5IIKsxiL) | 3.57-1.21.1 | index match | standard | researching |
| [FTB Essentials (NeoForge)](https://www.curseforge.com/minecraft/mc-mods/ftb-essentials/files/8442866) | 2101.1.10 | index match | strong | researching |
| [Get It Together, Drops!](https://modrinth.com/mod/T0OUgf8P) | v1.4 | index match | hold-verification | held |
| [Harvest with Ease](https://www.curseforge.com/minecraft/mc-mods/602171) | harvest-with-ease-neoforge-1.21-9.4.0 | index match | standard | researching |
| [HT's TreeChop](https://modrinth.com/mod/treechop/version/iLXWmfax) | 0.19.3 | index match | standard | researching |
| [Inventory Tweaks — ReFoxed](https://www.curseforge.com/minecraft/mc-mods/inventory-tweaks-refoxed/files/all) | invtweaks-1.21.1-1.3.2 | index match | standard | researching |
| [Jade](https://modrinth.com/mod/nvQzSEkH) | Jade-1.21.1-NeoForge-15.10.6 | index match | standard | researching |
| [Just Enough Items](https://modrinth.com/mod/u6dRKJwZ) | jei-1.21.1-neoforge-19.64.0.455 | index match | standard | researching |
| [Just Enough Resources (JER)](https://modrinth.com/mod/just-enough-resources-jer/version/A2G7NFcD) | 1.6.0.57 | index match | standard | researching |
| [Just Zoom](https://modrinth.com/mod/iAiqcykM) | justzoom_neoforge_3.1.0_MC_1.21.1 | index match | standard | researching |
| [KeyBind Bundles](https://www.curseforge.com/minecraft/mc-mods/1172594) | keybindbundles-1.5.0 | index match | optional | researching |
| [KeySets](https://github.com/Meneleet-official/keyset/releases/tag/v1.3.0) | keyset-neoforge-1.3.0+mc1.21.1 | index match | optional | researching |
| [Leaves Be Gone](https://modrinth.com/mod/leaves-be-gone/version/kAbmpvF3) | v21.1.1-1.21.1-NeoForge | index match | standard | researching |
| [LootJS](https://modrinth.com/mod/fJFETWDN) | 1.21.1-3.7.0+neoforge | index match | tooling | researching |
| [Lootr](https://modrinth.com/mod/EltpO5cN) | lootr-neoforge-1.21.1-1.11.38.127 | index match | standard | researching |
| [More Darkness](https://modrinth.com/mod/more-darkness/version/6jywYHaX) | 2.0.1+1.21.1+neoforge | index match | optional | researching |
| [More Overlays Updated](https://www.curseforge.com/minecraft/mc-mods/391382) | moreoverlays-1.24.2-mc1.21.1-neoforge | index match | strong | researching |
| [Mouse Tweaks](https://modrinth.com/mod/aC3cM3Vq) | MouseTweaks-neoforge-mc1.21-2.26.1 | index match | standard | researching |
| [Nature's Compass](https://www.curseforge.com/minecraft/mc-mods/252848) | NaturesCompass-1.21.1-3.4.0-neoforge | index match | standard | researching |
| [Oracle Index](https://www.curseforge.com/minecraft/mc-mods/1206582) | oracle_index-neoforge-1.4.1 | index match | optional | researching |
| [Polymorph](https://modrinth.com/mod/tagwiZkJ) | polymorph-neoforge-1.2.0+1.21.1 | index match | standard | researching |
| [Prefab](https://modrinth.com/mod/prefab/version/1.0.9) | 1.0.9 NeoForge 1.21.1 | index match | optional | researching |
| [Smart Keep Inventory](https://modrinth.com/mod/smart-keep-inventory/version/1.21.1-1.0.1-neoforge) | 1.21.1-1.0.1-neoforge | index match | optional | researching |
| [TrashSlot](https://modrinth.com/mod/trashslot/version/HY8Ybozd) | 21.1.11+neoforge-1.21.1 | index match | standard | researching |

### performance — 5

| Mod | TMM observed version | Index match* | Port tier | Status |
|---|---|---|---|---|
| [Embeddium](https://modrinth.com/mod/sk9rgfiA) | embeddium-1.0.15+mc1.21.1 | index match | strong | researching |
| [Entity Culling](https://modrinth.com/mod/NNAgCjsB) | entityculling-neoforge-1.12.1-mc1.21.1 | index match | strong | researching |
| [FerriteCore](https://modrinth.com/mod/uXXizFIs) | ferritecore-7.0.3-neoforge | index match | strong | researching |
| [ImmediatelyFast](https://modrinth.com/mod/5ZwdcRci) | ImmediatelyFast-NeoForge-1.6.15+1.21.1 | index match | strong | researching |
| [ModernFix](https://modrinth.com/mod/nmDcB62a) | modernfix-neoforge-5.27.27+mc1.21.1 | index match | strong | researching |

### server utility — 2

| Mod | TMM observed version | Index match* | Port tier | Status |
|---|---|---|---|---|
| [Simple Backups](https://www.curseforge.com/minecraft/mc-mods/583228) | SimpleBackups-1.21-4.0.30 | index match | strong | researching |
| [spark](https://www.curseforge.com/minecraft/mc-mods/361579) | spark-1.10.124-neoforge | index match | strong | researching |

### compatibility — 1

| Mod | TMM observed version | Index match* | Port tier | Status |
|---|---|---|---|---|
| [Almost Unified](https://modrinth.com/mod/almostunified/version/e8iYxxI3) | AlmostUnified-NeoForge-1.21.1-1.4.2 | index match | standard | researching |

## Next carryover implementation

1. Start with the food core, farming/bulk harvest and high-utility player QoL shortlist, plus the performance baseline. Use TMM exact provider links as provenance but check newer compatible releases and dependencies first.
2. Classify exact version/load side/redistribution/license and transitive libraries; adjust `manifest/mods.json` `status` only after distinct approval/pinning. There are zero actual indexed TMT mods now.
3. Integrate clean configs/tags when useful; reauthor Tech-specific cooking automation and ore processing rather than copying TMM's magical gameplay KubeJS.
4. Test A (offline pins, recipes, configs), B (verified in-game commands if any), C (real farm/kitchen/transport client tests), then update feature ledger. No TMM runtime PASS carries over.

This page and its machine registry entries are a research handoff, not a new gameplay balance or full-build authorization.
