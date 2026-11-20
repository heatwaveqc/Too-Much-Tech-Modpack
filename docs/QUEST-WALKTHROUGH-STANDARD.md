# Quest authoring — teach real systems, not item checklists

Adapted from [Too Much Magic's walkthrough standard](https://github.com/heatwaveqc/Too-Much-Magic-Modpack/blob/test/full-integration/docs/QUEST-WALKTHROUGH-STANDARD.md). The **instructional philosophy is adopted**, but exact reward amounts, chapter taxonomy and automation gates are open TMT design decisions. No quest runtime is installed yet.

## Definition of done for a substantial tech-mod chapter

A new player should be able to complete the mod's normal major progression using **the questbook + JEI/EMI (whichever is selected) + the mod's own in-game documentation**, without needing a separate wiki/tutorial. Cover entry resources, first machine, power generation/transport, input/output and automation, multiblocks and GUI controls, tiers/upgrades, troubleshooting, specialized branches, complex late-game systems, and completion milestones. Provide practical use examples (a working processing line beats a passive 'craft 10 machines' list).

Onboard each accessible in-game guide early: show how to obtain/open it and the precise section/reference. If an in-game guide is incomplete or wrong in the pinned version, supply missing steps and flag the discrepancy for versioned validation.

## Every quest should answer

- **Purpose and prerequisites:** what system it unlocks and which resources/tech tiers/power network it actually needs.
- **Action:** what to craft/connect/place, exact sided input/output/energy behavior, multiblock orientation, settings and required interactions; avoid explaining only item acquisition.
- **Reference:** exact JEI recipe/use category or in-game manual section; do not depend on a live external wiki as the only instructions.
- **Expected behavior:** inputs, outputs, throughput, power requirements, visible status and common failure symptoms where useful.
- **Detection:** what FTB Quests actually checks versus what the player learned. Do not claim the detector verifies a running multiblock merely because it sees a crafted controller.
- **Reward:** meaningful and thematic, balanced with the approved reward/economy policy; never skip real progression gates through a reward.

Cross-mod integration (e.g., conversion between machine networks or item transport) belongs in a shared Progression/Integration chapter with references to specialist chapters; do not duplicate all material. Addons should be explained within the parent ecosystem where natural. QoL-only mods deserve a concise how-to and useful tricks, not invented tier ladders.

## Mechanical and data integrity

- Use **actual native gates** in configs, recipes, advancements and source hooks; a quest arrow is not an enforceable tech gate.
- Verify task IDs, duplicate/accidental completion criteria, item rewards that auto-satisfy a later task, team/player sharing, disabled items and recipe availability. Rewards must not bypass intentionally gated systems.
- Validate that all progression paths remain completable from fresh survival without operator permissions; manual checkbox quests must not silently substitute for a broken detector.
- Record A offline, B exact-command (if legitimate), and C real crafting/setup tests for each significant quest chain.
- Keep original prose/quest layouts/assets. Do not copy TMM or other modpacks' quest text, images or copyrighted content into TMT.

No tech quest chapters are implemented or approved by this document alone.
