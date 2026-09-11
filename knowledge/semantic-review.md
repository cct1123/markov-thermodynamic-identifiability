# Semantic review of the research map

2026-09-11 UTC. Scope: compare the knowledge-map representation with accepted research; no new research, scientific replay, commit or push. This review owns only this file. It is a semantic/provenance review, not a new proof audit.

**Final integration outcome:** the merged graph resolves the four source-review findings below. No remaining semantic correction was identified. All eight true counterexamples are separated from their falsified hypotheses, verification scope is explicit, and no accepted result is supported through a rejected statement. The final integration snapshot and checks are recorded at the end; the earlier source findings are retained as review history.

## Source-review outcome

The theorem statements, exact versus neighborhood classes, entropy convention, exceptional parameter qualifications, prior-work comparisons and main open questions agree with the current specification and report. No new mathematical inconsistency was found. The remaining required corrections concern how statuses and relationships communicate the strength of that evidence.

1. **Saved provenance checks must not acquire an independent-proof badge.** In `source-claims.json`, `check_legacy_saved` has `status: independently_verified` and is referenced by the `independent_verification` fields of T1 and the legacy theorem nodes. Its actual content is inspection of accepted outputs and five source hashes, with no fresh scientific replay during the legacy/map audit. Its prose says this correctly, but a badge reading “INDEPENDENT CHECK” and an unqualified `verified_by` edge can erase the distinction. Use a saved-output/provenance-review label or an equally visible mandatory scope field on the node and edges. A source-hash match establishes provenance consistency; it does not independently reproduce a calculation or prove a universal theorem. The separate `proof_legacy_classifications` node may retain its conventional analytic-audit status.

2. **Assumption relationships are not all necessity claims.** Do not generate “requires” or “necessary condition” from every member of the `assumptions` arrays. Examples: T1's even-state/channel convention is retained model context rather than an algebraic premise of finite-jet equality or similarity; T3's full irreducibility follows from nonnegative normalization, exact minimal data and the cap; its cap can be replaced by minimal-only competitors. T8's support-controlled compact inverse is sufficient, not necessary. T5's two fully hidden states are sufficient for its every-source neighborhood conclusion, not necessary for instability: T4a already has one. The assumption-kind metadata and source limitations contain these distinctions; edge explanations and badges must preserve them.

3. **True witnesses must stay true when rejected hypotheses are split out.** The coordinator is already separating `hypothesis_*` from `cex_*`. The former should be falsified, while the explicit witness remains proved/checked at its recorded scope. In particular do not retain `cex_compact_limit_support -> theorem_t8` or `cex_ratio_without_activity -> theorem_t8` as “corrected_by”: T8 does not correct the true witness. Appropriate directions are `cex -> hypothesis` falsifies, and `theorem_t8 -> hypothesis` revises, or `cex -> theorem_t8` motivates. The existing first-order/local-isolation examples likewise motivate stronger proofs; the accepted endpoint must not depend logically on a falsified hypothesis.

4. **Scope numerical verification edges.** `check_publication_independent` checks specified inverse/interpolation examples and chord diagnostics. `check_precision_examples` checks the displayed physical sequences. When attached to T2a/T4/T6/T7, these checks corroborate identities and examples; they do not independently prove universal continuity, all-N exhaustion, divergent limits or the confidence-transfer implication. Those conclusions have separate analytic proof nodes. The source node limitations correctly state this; retain the qualification in the graph's edge details and inspector. The independent endpoint construction verifies coefficientwise cone/path agreement and the witnessed algebra; global support exhaustion comes from the analytic audit, not from finite replay agreement.

These are presentation-strength corrections to the map. They do not reopen the accepted mathematical theorem statuses.

## Coverage and substantive checks

Read `source-claims.json` in full, including T1–T8, the legacy theorem statements, supporting lemmas, proof/check nodes and supplied edges. Read all context-node summaries, statements as needed, limitation/access fields and relationships. Compared against:

- `analysis/publication-theorems.md` and `analysis/publication-legacy-audit.md`;
- `outputs/REPORT.md`, including all result tables, boundary examples, novelty assessments and stopping/next-action claims;
- `evidence/RECORDS.md`, especially E055–E062 and D023, preserving E058's superseded joint-kernel rate-cap claim and its still-retained stationary-window cap;
- the endpoint, stability, hidden-pair and neighborhood proof notes previously audited, for exact count, completion/family positivity and limits;
- the saved realization and thermodynamic novelty memos for the existing source-attribution/access statements. No original web source was newly retrieved, so this is a consistency check against those memos, not a fresh source verification.

The important report claims are represented: the exact two-point fiber and three parameter regimes; minimal order and cap-five/cap-six distinction; three-Laplace recovery and positive-triangle continuity; the minimal fixed-trace sparse witness; fixed-N local-ceiling criterion; the two distinct instability mechanisms; confidence obstruction and positive-triangle qualification; corrected compact-support and activity/ratio conditions; all four principal rejected strengthenings; conservative manuscript/novelty assessment; source-access gaps; off-balanced/general classification and window-continuity frontiers; and the saved proof-core next action. The broader legacy inventory is separately represented rather than mislabeled as an exhaustive five/six-state classification.

The literature nodes preserve key qualifications: Mond's static full-space example and the repository-derived scalar lift are distinguished; sampled hidden-entropy growth is not made an analytic universal theorem; Larget remains abstract-only; inaccessible originals do not establish novelty; MAP/BMAP and Coxian statements are compared under their own observation/reset and topology assumptions. The activity-ratio prior agrees with the saved source memo, including the stronger `(R-1)/(R+1)` factor. No new novelty conclusion is made here.

No supplied logical dependency direction was found to reverse a mathematical implication. “Supports,” “motivates,” “compares with,” and “limits interpretation” must remain distinct from proof dependency in the merged graph. The planned witness/hypothesis split needs the explicit directional correction above.

## Review snapshot and integration status

At this source-review checkpoint, `knowledge/graph.json` had not yet been created. Integration therefore remains unreviewed; source-shard agreement does not certify the eventual merged graph. The coordinator was sent the concrete corrections while constructing it. A later integration check should inspect derived assumption/verification edges, all split witness statuses, and the report-coverage mapping without rerunning scientific calculations.

SHA-256 snapshots, in the listed order, taken 2026-09-11 01:52 UTC:

| File | SHA-256 |
| --- | --- |
| `knowledge/source-claims.json` | `27dc33a86979531896a22441434c8be52a097bc1cd227633c15d33bc6f487644` |
| `knowledge/source-context.json` | `7456d1455d0545944690ab2b431b836887bae1bcaa0dfcf134b433f9710317b6` |
| `analysis/publication-theorems.md` | `53417bdf64e954bf011986e3b4c58f10569d86a18a4b240e0e502ece04f7bb1f` |
| `analysis/publication-legacy-audit.md` | `26d6d857d64ca5237688ad2abb3882d0e9f378e69ac5790bf53fea8db054972d` |
| `outputs/REPORT.md` | `4d6f535402e58b09fb2f6d9ac5e32888cf274a7629426c8436b5843802e1c67c` |

Read-only inspection used PowerShell `Get-Content`, `rg`, `Get-FileHash`, and Python `json.load` under `.venv/Scripts/python.exe -B -`. An initial JSON terminal print hit Windows' code-page limitation; ASCII-escaped output resolved it. Two guessed integration-script filenames did not exist; no execution or write resulted. No scientific failures or new scientific validation are claimed by these inspection operations.

## Final merged-graph review

Reviewed `knowledge/graph.json`, SHA-256 `2609cac2b9ccd1a3faaaf8d9f665420a79586000f507991ebe4ff5e7c8f3dbc3`, containing 110 nodes and 386 typed edges. The four earlier findings are resolved:

- `check_legacy_saved` now has `provenance_checked`, a “SAVED PROVENANCE” display label and an explicit saved-output/hash scope. No node's `independent_verification` field refers to it. The legacy claims instead point to the separate conventional proof/scope audit.
- Assumption edges explicitly say retained scope is not a universal necessity assertion. T1/T3/T6 carry additional context, derived-assumption and strengthening notes. T5/T8 retain their sufficient-condition qualifications. The inspector renders `assumption_notes` and `verification_scope`.
- All eight `cex_*` nodes are `analytically_proved`; each has a `falsifies` edge to its separate `hypothesis_*` node with status `falsified`. The corrected theorem's `revises` arrows point to rejected hypotheses, not to true witnesses.
- Numerical checks' scope explicitly limits them to listed algebra/examples/diagnostics; analytic audit nodes carry universal-statement verification. No formal scientific proof is claimed: the formal scaffold remains unresolved and explicitly uncompiled.

An independent read-only graph traversal treated `supports`, `strongly_supports`, `implies` and `reproduces` as forward support, and reversed `depends_on`, `derived_from` and `verified_by` into support direction. There were **zero** paths from any falsified/superseded node to any analytically proved or independently verified node. Motivational, contrast and revision edges were intentionally not treated as proof implications. No rejected hypothesis is smuggled into a proof chain by a different edge direction.

Executed from the project root:

```powershell
.\.venv\Scripts\python.exe -B knowledge/validate.py --no-write
```

Result: passed, zero errors, zero warnings; 110 nodes, 386 edges, 12 views, seven report sections mapped, 56 source snapshots, logical dependency graph acyclic. This checks graph/provenance consistency, not scientific proof validity. The independent semantic traversal additionally covers support/verification directions beyond the validator's narrower dependency DAG.

The report mapping contains the main exact-fiber, three-state inverse/instability, all-N stability, counterexample, novelty and verification/frontier claims previously checked. The next-action node links stable D023 and `PAPER-STRUCTURE.md` and explicitly states manuscript preparation is occurring concurrently. The volatile whole `STATE.md` is absent from the scientific fingerprint set; this prevents a legitimate concurrent task-state update from impersonating scientific source drift. Accepted scientific sources remained consistent in validation.

One packaging observation was sent to the coordinator: at inspection time `interactive/data.js` still embedded an earlier validation failure caused by `STATE.md` drift, while the reviewed graph and fresh no-write validation already passed. A final validate/build must refresh that generated browser payload. This is not a remaining graph semantic defect, and this review did not overwrite the payload or the concurrent manuscript's state. No visual layout or browser interaction audit is claimed here.

## Coordinator packaging note

The two initial review-input files were moved unchanged to [review-inputs/source-claims.json](review-inputs/source-claims.json) and [review-inputs/source-context.json](review-inputs/source-context.json); the hashes above still identify them. They are archival review inputs, not maintained registries. The final graph adds one explicit display grouping of the three already declared common model conditions, giving 111 nodes and 389 edges. Complete theorem assumptions remain unchanged. Short map labels and the balanced search's actual two positivity-floor settings were clarified. The current generated browser payload has been rebuilt from a passing validation; browser and reader checks are separately recorded in [validation-notes.md](validation-notes.md). These packaging changes are coordinator checks, not an extension of the independent scientific proof audit.

The final literature drill-down adds 30 individual paper/version records, integrated from the unchanged [paper review input](review-inputs/paper-details.json), for **141 nodes and 419 edges**. Each `documents` arrow supplies attribution to one of 15 existing comparison groups; it is not a proof or independent-support arrow. The Larget original and abstract-only 2016 BMAP successor retain unresolved exact-comparison status. The 2012 BMAP preprint remains separate. Mond's static result remains separate from the repository's scalar CTMC lift. The corrected Telek-first author order was cross-checked against the saved later referee literature note; that is its only role here. These final integrations and source links were checked by the coordinator, not represented as a new independent proof audit. The browser payload and all 30 interaction checks were regenerated after integration.
