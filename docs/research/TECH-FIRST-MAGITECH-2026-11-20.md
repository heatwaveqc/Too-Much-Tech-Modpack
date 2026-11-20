> **Owner decision update (2026-11-20):** Botania Revived and preferred Embers Re-Ignited were approved as optional tech-leaning inclusion targets. The original recommendations below are retained for provenance. The competing port Embers Reborn remains **research-only fallback**, not a second intended installed JAR. Neither target has a packwiz pin, dependency lock, or runtime acceptance. See [TMT-0026](../DECISIONS.md).

# Engineering-first magitech: Botania and Embers for Too Much Tech

**Research / recommendation, 2026-11-20.** This is not an owner selection or installed JAR. User asked whether they should be included "for the memes" versus keeping the pack strictly nonmagical.

## Recommendation: include both, with a tech-first identity

**TMT's theme is engineering, not a ban on supernatural power sources.** We recommend these as unusual technology pathways because their play is factory and automation engineering despite magic-inspired presentation. Avoid any requirement to progress through Botania or Embers to reach normal Oritech / Mekanism / Create / Draconic machines.

### Botania Revived

- **Official source/port:** [Botania Revived](https://www.curseforge.com/minecraft/mc-mods/botania-revived), [1.21.1 NeoForge 2.0.4 file](https://www.curseforge.com/minecraft/mc-mods/botania-revived/files/9695259), release **2026-11-19**. This is an **unofficial** port; the original official [Botania](https://www.curseforge.com/minecraft/mc-mods/botania/files/all) currently chiefly releases for 1.20.1 rather than official 1.21.1.
- **Tech angle:** build configurable mana-generating/consuming factories from flowers, spreaders, sparks, pools, redstone, spatial automation, item transformations, and automated crafting; complexity mainly in machine design.
- **Scope:** optional botanical engineering subsystem, not a universal mandatory energy prerequisite, not a magic-first questline.
- **QA:** dependency review (Patchouli/Ponder libs, verify release manifest), product bees/flower interaction, server automation claims, plant/worldgen changes, mana spreader ray/beam TPS, FE/OP adapters only when actually implemented. Some versions/ports have patch-dependent interactions with Productive Bees; exact tested versions matter.

### Embers (choose one implementation of the original)

- **Preferred source candidate:** [Embers Re-Ignited](https://modrinth.com/mod/embers-re-ignited), [NeoForge 1.21.1 1.5.9](https://modrinth.com/mod/embers-re-ignited/version/1.21.1-1.5.9), **release**, a forward port of Embers Rekindled with advertised Create and Sable support.
- **Alternative port:** [Embers Reborn](https://www.curseforge.com/minecraft/mc-mods/embers-reborn), **1.21.1 NeoForge 1.1.0**, November 14, 2026. Distinct unofficial *port*, not an Embers addon.
- **Tech angle:** dwarven extraction/melting/metalworking, ember-powered machines, pipes and item handling, processing, clockwork tools and elaborate installations, with magic-looking alchemy as optional flavor.
- **QA:** verify exact NeoForge artifact/portal content, original mod ID/registry overlap (likely `embers`) and choose one port, Create/Sable dependencies, material/ore duplicates, dimensional structures and source integration licenses. Both ports as separate **technology branches** would not make sense if they share underlying mod IDs: this is a binary conflict, not simply gameplay overlap.

## Engineering-first boundaries and gameplay

1. Keep the full mainstream tech roster independent: existing electrical, mechanical, logistics, biotech and space progression must not require Botania or Embers.
2. Make an optional **Magitech & Experimental Power** quest chapter framing them as alternative engineering, not casting schools. Do not port TMM's magic-specific world/skills or require magical transformation.
3. Don't remove overlap with conventional pipes, farms, or resource factories. Technical duplication is allowed; tune recipes or throughput later if actual exploits or gameplay warrant.
4. Prefer native configs and standard tags/recipes for cross-mod components. Avoid fragile global-tick bridges to convert Mana/Ember/FE/OP simply to claim all power systems are unified.
5. Preserve TMT's distinctive personality: where TMM explores the magical fantasy, TMT explores **how to industrialize it**.

**Current decision state:** the owner selected **both** themes. Botania Revived and Embers Re-Ignited are targeted, while Embers Reborn remains an unselected fallback implementation. No packwiz or runtime QA performed.

**Sources checked:** CurseForge/Modrinth product pages and release listings 2026-11-20. Exact dependencies, JAR hashes and terms still need normal source review.
