# Too Much Tech — current test status

**Snapshot:** bootstrap-only source, updated 2026-11-20.

| Test level | Evidence | Result |
| --- | --- | --- |
| CI-REPO | GitHub quick workflow `Verify bootstrap / metadata`, succeeded on initial main and integration source SHA `11b4ac80833e11b0b72335985bb1454eb19dfa27` | PASS for that bootstrap SHA only |
| CI-MODULE | No game module yet | NOT RUN |
| CI-PREFLIGHT | Initial metadata validator; no frozen external donors to verify | NOT RUN for full donor reachability; static schema coverage only |
| QA-ASSEMBLY | No authorized assembly runner | NOT RUN |
| QA-SERVER | No authorized NeoForge server boot | NOT RUN |
| QA-PRISM | No launcher ZIP | NOT RUN |
| QA-CLIENT | No graphical client acceptance | NOT RUN |
| QA-GAMEPLAY | No mechanics tested | NOT RUN |

[Original bootstrap main CI](https://github.com/heatwaveqc/Too-Much-Tech-Modpack/actions/runs/44813239051) and [integration CI](https://github.com/heatwaveqc/Too-Much-Tech-Modpack/actions/runs/44813244201).

**Future rule:** replace/update this ledger for a *specific frozen QA artifact* only when a new run actually occurs. Do not retroactively mark higher levels as passed after docs/CI additions. Feature-level evidence belongs in `manifest/feature-checklist.json` with per-test links; readiness belongs in `manifest/live-test-inclusion.json`.
