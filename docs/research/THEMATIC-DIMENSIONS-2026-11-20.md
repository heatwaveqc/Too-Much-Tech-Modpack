# Tech-themed dimensions and procedural planet survey

**As of 2026-11-20.** Target platform **Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21** (provisional). Owner favors an inclusive first pass. **Seven of the 20 newly surveyed dimension entries are now targeted goals; 13 remain research-only.** Existing Ad Astra was already targeted. No new dimensions or JARs installed, packwiz pinned, built or gameplay tested.

## Owner-selected inclusion goals (2026-11-20)

| Phase | Target | Intended capability |
| --- | --- | --- |
| Primary | [Ad Astra: Planets](https://www.curseforge.com/minecraft/mc-mods/ad-astra-planets) | Curated solar system, custom planet definitions and seeded terrain |
| Primary | [Stargate Journey](https://www.curseforge.com/minecraft/mc-mods/sgjourney) | Parallel Stargate travel to Ad Astra and compatible dimensions |
| Primary | [RFTools Dimensions](https://www.curseforge.com/minecraft/mc-mods/rftools-dimensions) | Player-built powered, programmable dimensions |
| Primary | [Infinite Dimensions](https://www.curseforge.com/minecraft/mc-mods/infinite-dimensions) | Runtime procedural destination generation with save persistence |
| Primary | [Deep Space (Unofficial Port)](https://www.curseforge.com/minecraft/mc-mods/deep-space-unofficial-port) | Galaxies, ringworlds, spacecraft and optional procedural star systems |
| Isolated experiment | [MACHINA](https://modrinth.com/mod/machina-mod) | Investigate claimed infinite procedural planets; verify genuine content and stable multiplayer persistence |
| Isolated experiment | [Create: Universe](https://www.curseforge.com/minecraft/mc-mods/create-universe) | Investigate procedural cosmos and seamless spacecraft transitions; isolate complex physics/dependencies |

**Selection is a development goal, not a readiness verdict.** Exact Minecraft/NeoForge/provider artifact and transitive dependencies, licensing, combined worldgen, travel/return path, player save/load and server performance are still to be checked. Both experimental targets should first run on disposable standalone worlds before any combined inclusion attempt. Conceptual overlap is not a reason for removal; a proven hard incompatibility is.



## Findings worth pursuing

**Ad Astra can support *custom planets* without a new runtime engine.** The current 1.21.1 branch has a JSON planet data loader. [Ad Astra: Planets modpack guide](https://github.com/duduslugee/ad-astra-planets/blob/main/docs/MODPACK.md) documents custom solar-system JSON, planet definitions, orbits, a Minecraft dimension JSON per explorable destination, noise/biomes/density functions and placed features. A planet lacking a corresponding dimension remains a non-explorable map entry. Ad Astra views an object without an orbit as a station, not selectable planet. This makes **a finite designed collection of planets with seed-varied terrain** feasible with pack-authored datapacks. It does **not** establish an in-game API for unlimited runtime planet creation.

**Ad Astra: Planets 1.0.1** ([release](https://www.curseforge.com/minecraft/mc-mods/ad-astra-planets)) is an unusually helpful 1.21.1 example: outer Solar System worlds and moons (Europa ice/ocean, Io sulfur, Titan methane lakes), tier 5–10 rockets, many JSON settings, KubeJS boarding/arrival hooks and environmental equipment data. It requires Ad Astra 1.16.26+, GeckoLib and Ad Astra libs. Its hard tier progression is a configurable design input, **not** an instruction to create forced recipe grind.

**Procedural dimensions at runtime are a different problem.** [Infinite Dimensions](https://www.curseforge.com/minecraft/mc-mods/infinite-dimensions) implements dynamic dimension registration, 2.7.3 on NeoForge 1.21.1. [RFTools Dimensions](https://www.curseforge.com/minecraft/mc-mods/rftools-dimensions) implements player-built powered dimensions, 12.0.4 beta. [Deep Space](https://www.curseforge.com/minecraft/mc-mods/deep-space-unofficial-port) can use Infinite Dimensions to create procedural star systems, with its Sable ship and Hyper Relay gameplay. [MACHINA](https://modrinth.com/mod/machina-mod) and [Create: Universe](https://www.curseforge.com/minecraft/mc-mods/create-universe) also advertise generated solar systems with many more simulation/physics dependencies. Claims of 'infinite' do not establish server scalability or save compatibility.

**Travel integration:** [Stargate Journey](https://www.curseforge.com/minecraft/mc-mods/sgjourney) latest 1.21.1 beta 0.6.54 explicitly supports Ad Astra destinations and CC:Tweaked dialing. This is ideal as a parallel way to reach selected destinations without replacing rocket or spaceship methods. [Modded Gateways](https://www.curseforge.com/minecraft/mc-mods/modded-gateways) adds cross-dimension structure/config support; confirm specific dimensions rather than assuming all work.

## Survey inventory (20 research entries; 7 now targeted goals)

| Mod / source | Candidate version | Category | Compatibility notes |
| --- | --- | --- | --- |
| [Ad Astra: Galaxies](https://www.curseforge.com/minecraft/mc-mods/ad-astra-galaxies) | 1.0.0 · release | creative-tabs-by-star-system | Adds creative tabs for Planets+ systems, NOT new planets as primary feature; hard dependency on Ad Astra and adastraplanets, exact addon identity must be resolved. |
| [Ad Astra: Planets](https://www.curseforge.com/minecraft/mc-mods/ad-astra-planets) | 1.0.1 · release | solar-system-expansion | Adds Mercury, outer planets/moons, tier 5–10 rockets, biome/worldgen JSON, solar maps, environmental protection; 1.21.1 NeoForge, requires Ad Astra 1.16.26+, GeckoLib, libraries. Data-first strong custom planet blueprint. |
| [Ad Astra: Planets+ (datapack)](https://modrinth.com/datapack/planetsplus) | unverified-current · datapack | additional-planets-and-star-systems | Ad Astra datapack/resource pack adding more planets and solar systems. Need verify exact 1.21.1 Ad Astra 1.16.26 compatibility and overlap with Ad Astra: Planets addon before enabling. |
| [Advanced Rocketry 3](https://modrinth.com/mod/advanced-rocketry-3) | exact-file-pending · incomplete | json-planets-rocket-ships-and-terraforming | Custom JSON planet definitions, station warp, modular rockets, satellites, asteroid mining and terraforming. Author says incomplete with no included recipes/loot tables; good dev sandbox, not ready survival target. |
| [Beyond Overworld](https://www.curseforge.com/minecraft/mc-mods/beyond-overworld) | 0.0.1-p2 · alpha | flyable-starships-alien-planets | No Man's Sky-inspired flyable starships, planet hazards, towns, warp routes; very early alpha, dedicated server listed but new-world only; minimum NeoForge 21.1.252. |
| [Big Bang](https://www.curseforge.com/minecraft/mc-mods/big-bang) | 26.7 · release | galacticraft-inspired-planets | Space exploration with Moon/Mars/Venus destinations; 1.21.1 NeoForge file exists, but overlaps established Ad Astra travel content; inclusion preference can be decided by tested stability. |
| [Continuum (Space)](https://www.curseforge.com/minecraft/mc-mods/continuum-space) | 0.2.2 · release | planetary-bodies-in-space | Solar systems with planet bodies in common space, Dyson shells, star phenomena, unique orbital exploration; early niche release, investigate world simulation/performance. |
| [Create: Dimension — Steamworks Realm](https://www.curseforge.com/minecraft/mc-mods/create-dimension-steamworks-realm) | 2.0.0 · release | industrial-mining-realm | Technological mining dimension, rich ore veins and steam aesthetic; potentially enjoyable automate-in-another-world destination. |
| [Create: Universe](https://www.curseforge.com/minecraft/mc-mods/create-universe) | 2.1 · release | seamless-fully-procedural-cosmos | Claims seamless transitions and procedural stars/planets/mobs/worldgen; dependencies Create, Sable, Create Aeronautics, Create Propulsion Simulated, Create New Age, Gravity Control, Cloth Config. Very large compatibility/physics/performance surface; isolated smoke essential. |
| [Deep Space (Unofficial Port)](https://www.curseforge.com/minecraft/mc-mods/deep-space-unofficial-port) | 1.0.1 · release | galaxy-ringworlds-and-flyable-ships | Planets, ringworlds, Hyper Relays, Sable ships, galaxy map. Infinite Dimensions optional strongly preferred for procedural star systems. Required Veil, Sable, Sable Schematic API, GeckoLib. |
| [Dimension Expansion](https://www.curseforge.com/minecraft/mc-mods/dimension-expansion) | 1.2.9 · release | deep-beneath-stoneblock-and-mining | Adds Deep Beneath and non-decorated mining realm, Stoneblock-like world; data driven. Industrial underground option without space theming. |
| [Galacticraft Boobcat Edition](https://www.curseforge.com/minecraft/mc-mods/galacticraft-boobcat-edition) | 5.4.20-prealpha · prealpha | galacticraft-style-planetary-exploration | Unofficial 1.21.1 NeoForge Galacticraft fork with planets, bosses, space weather, stations and machines; prealpha, hard coexistence conflicts possible with Ad Astra spacecraft mechanics. |
| [Infinite Dimensions](https://www.curseforge.com/minecraft/mc-mods/infinite-dimensions) | 2.7.3+1.21.1 · release | runtime-random-dimensional-registry | Runtime creation of billions of quirky procedural dimensions from book + quill and portals; 1.21.1 NeoForge. Works as optional random-dimension engine for Deep Space; persistent save/runtime registration QA high. |
| [MACHINA](https://modrinth.com/mod/machina-mod) | exact-file-pending · release-listing | infinite-procedural-planets-and-tech | Claims infinite physically accurate explorable solar systems, unique biome planets, factories and ships. Relatively small/new project: verify exact version, real worldgen maturity, safe server persistence. |
| [Modded Gateways (Stargate Journey addon)](https://www.curseforge.com/minecraft/mc-mods/modded-gateways) | 1.0.0.5 · release | cross-mod-gate-generation | Addon places Stargates in other mod dimensions with compatible recipes; exact target dimension coverage must be verified. |
| [RFTools Dimensions](https://www.curseforge.com/minecraft/mc-mods/rftools-dimensions) | 1.21-12.0.4 · beta | player-constructed-powered-dimensions | Player-built dimension generation via dimlets and dimension builder; power consumption creates a real technology-driven dimension progression. Needs RFTools Base + McJtyLib/version chain. |
| [Space dimension exploration pilot (TMT)](https://github.com/heatwaveqc/Too-Much-Tech-Modpack) | not-implemented · design-only | future-data-driven-procedural-pilot | Proposed first-party integration pilot, not third-party mod: three deterministic planet archetypes, one JSON definition each plus seeded noise/biomes/features; only after choosing an API and QA owner. |
| [Space Explore](https://modrinth.com/mod/space-explore) | version-pending · singleplayer-only | procedural-singleplayer-galaxy | Supports procedural planets but provider explicitly marks SINGLEPLAYER ONLY; hold from any multiplayer/default full integration until dedicated-server support. |
| [Starfold](https://www.curseforge.com/minecraft/mc-mods/starfold) | 0.1.1 · beta | continuous-flight-planets | Uses Create Aeronautics and Sable crafts for seamless transitions, early beta. Complex dependency and currently reported multiplayer restrictions need verification. |
| [Stargate Journey](https://www.curseforge.com/minecraft/mc-mods/sgjourney) | 0.6.54 · beta | gate-network-to-other-dimensions | Find and activate ancient Stargates; author explicitly supports Ad Astra destinations and CC:Tweaked integration. Unique alternative travel system; migration/network compatibility to verify. |

## Planets: three progressively harder ways to generate variety

### Level 1 — curated planets, procedural *terrain*

Create a datapack with a fixed list of named planets, each with vanilla/Minecraft `worldgen` noise, biome, density function and features keyed by world seed. Planet IDs/orbits and atmosphere/temperature behavior are configured using Ad Astra's documented JSON format. No runtime dynamically created dimensions are needed.

Suggested small integration pilot **(examples, NOT locked features):**
- **Scrapyard moon** — rocky barren landscape, layered industrial ruins, metal salvage and rover wrecks
- **Cryosea** — ice crust over a dark ocean, vent/chimney POIs and pressure/heat logistics
- **Bioforge** — alien fungus/highland biomes, unusual chemistry, controlled resource niches

Test each biome/noise config against built-in Ad Astra worldgen, new-world loading, correct rockets/return trip, ores, no forced grind, and actual interesting points of interest. Naming a planet without landmarks isn't meaningful depth. Seeded worldgen provides diversity without requiring infinitely many dimensions.

### Level 2 — pack-generated catalog before world creation

A version-controlled generator could emit a finite number of planet/dimension JSONs from a deterministic build seed, varying atmosphere/biomes/ore placement/landmark tables. Once a world starts, **freeze dimension IDs and registries**; changing/replacing a generated catalog risks breaking player world saves and navigation. This is a proposed build-time tool, not an installed feature.

### Level 3 — truly runtime-created worlds

Separate systems like Infinite Dimensions / RFTools / Deep Space / MACHINA / Create: Universe can generate worlds during gameplay, with their own registration/storage/travel systems. Begin isolated QA: create 1, 10 and 50 destinations, restart server, revisit, transfer inventory/shell/Progression attachments and vehicles, measure memory/disk/load performance. Do not conflate 'procedural terrain' with 'new dimension registered on demand.' Test server multiplayer before broad inclusion.

## Integration hazards to verify, not reasons for automatic exclusion

1. **Planet/space engine overlaps**: runtime dimension registry IDs, JSON/worldgen namespace collision, recipe/satellite IDs, space travel portals, atmosphere checks and gravity systems. If technical coexistence is real, keep the mods; if two implementations share a mod ID, select one.
2. **Cross-dimension saved data**: NeoSync shells, Cybernetics implants, TMM Progression XP/abilities, teleporter destinations, CC:Tweaked program data, linked storage networks, chunkload state and return gates must survive restart.
3. **Transport**: Ad Astra rocket flight, Stargates, RFTools dimension builders, Sable ships and any other launch mechanism should all retain sensible/allowed travel paths; avoid accidentally trapping players.
4. **Resource economy**: many extra dimensions can multiply ore access, Galacticraft/Ad Astra resource gates and tech progression; control loot/spawn/ore tags later **without removing overlapping mods as a first response**.
5. **Performance**: dimension count, procedural generation and ship physics are the primary technical risks. Worldgen TPS spikes and SaveData persistence demand real server tests.
6. **License, deps and providers**: beta/alpha is not an automatic exclusion under owner's policy, but missing files, unsupported loader, repeated mod ID, known crash or non-redistributable assets need specific handling.
7. **Special holds**: Space Explore declares singleplayer-only and should not be assumed safe on a multiplayer server; Advanced Rocketry 3 says no default recipes/loot and unfinished. They remain research, not asserted stable game-ready.

## Recommendation

Prioritize **Ad Astra + its Planets addon as the authored-world platform** and **RFTools Dimensions + Infinite Dimensions / Deep Space as dynamic-world experiments**. Evaluate MACHINA and Create: Universe in a clean disposable test environment because their claims and dependencies imply a much larger QA burden. Stargate Journey is an especially thematic parallel travel system. Seven have been explicitly targeted by the owner. All still require release/dependency verification and separately authorized build/QA; 13 others remain survey-only.

Sources: linked upstream project pages and the [Ad Astra: Planets MODPACK guide](https://github.com/duduslugee/ad-astra-planets/blob/main/docs/MODPACK.md). Dates/versions are research snapshots only.
