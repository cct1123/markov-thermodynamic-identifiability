# Semantic map schema, version 1

[graph.json](graph.json) is a **derived interface** to the scientific sources, not an independent claim registry or proof authority. Its summaries, statuses and relations must be reviewed against the referenced proofs and stable evidence anchors. A build never promotes status or invents an edge.

## Nodes

Required fields are `id`, `type`, `title`, `status`, `summary`, `provenance` and `level`. IDs are stable lowercase ASCII with underscores. A corrected result keeps its ID; retain a rejected claim and connect its witness with `falsifies`.

| Field | Meaning |
| --- | --- |
| `map_label` | Optional short display wording; the full title and statement stay available. |
| `intuition`, `statement`, `why_it_matters` | Human explanation, exact claim/scope, and scientific consequence. The browser never substitutes intuition for the formal statement. |
| `assumptions` | IDs of explicitly retained statement conditions. They are **not all asserted necessary**. |
| `assumption_notes`, `assumption_kind` | Derived, replaceable, sufficient, physical, observation, structural or technical roles; describe tested weakenings. |
| `evidence` | Supporting proof/check entity IDs. A lemma may instead use `supporting_artifacts` for its direct derivation, avoiding a trivial duplicate node. |
| `independent_verification`, `verification_scope` | Independent routes and their exact coverage. Saved-output/manifest inspection alone does not qualify. Example checks do not establish universal quantifiers. |
| `falsification_attempts`, `limitations` | Preserved failed/inconclusive attempts, scope boundaries and reopening conditions. |
| `novelty` | `status`, comparison summary and `comparisons` containing closest-prior node IDs. Novelty is not implied by analytic proof. |
| `literature` | Authors/year, setting, observation, inferred quantity, result kind, assumptions, mathematical difference and actual access limitation. These paper-level conditions are text, distinct from a project theorem's assumption IDs. |
| `paper_sources` | Individual LiteratureSource IDs beneath a prior-work comparison group. Fourteen groups are KnownPriorResult; the unresolved Larget access gap remains a LiteratureSource. Thirty paper/version records keep separate access limitations. |
| `provenance` | Objects with root-relative `path`, optional Markdown `anchor`, human `label`, and optional primary `url`. Local paths are validated; online routes are inherited from the saved source audit, not freshly retrieved by map construction. |

Current types include ResearchQuestion, Concept, Definition, MathematicalObject, ObservationModel, Assumption, ParameterConstraint, LiteratureSource, Theorem, Lemma, TheoremCandidate, Counterexample, EvidenceRecord, SymbolicResult, NumericalResult, Method, OpenQuestion, NoveltyRisk, PublicationClaim and ResearchAction. The schema permits extending the vocabulary when it adds scientific meaning.

Current statuses distinguish established prior result, reproduced prior result, numerical observation, strong numerical evidence, conjecture, theorem candidate, analytically proved, independently verified, provenance checked, formally verified, falsified, superseded, unresolved, interpretation, assumption and definition. Values use underscores, such as `analytically_proved`. **No current scientific node is formally verified.** A future formal label requires an inspected theorem identifier, successful build log and axiom audit in `formal_certificate`; structural validation does not execute Lean or audit its content.

The counterexample and its rejected hypothesis are different nodes: `cex_*` is analytically proved; `hypothesis_*` is falsified. A search that found nothing remains a numerical observation, with its inconclusiveness stated. `check_legacy_saved` has `provenance_checked`, while an independent conventional proof/scope review is a separate entity.

## Relationships and direction

Each edge has `source`, `target`, `relation` and a scientific `explanation`. Avoid generic relatedness.

| Direction | Meaning |
| --- | --- |
| claim → condition, `assumes` | Retained scope, with necessity/weakening explained separately. |
| claim → lemma, `depends_on` / `derived_from` | Logical proof dependence. |
| evidence → claim, `supports` | Evidence supports the stated claim within its declared coverage. |
| claim → check, `verified_by` | Independent route; read `verification_scope`. |
| witness → rejected hypothesis, `falsifies` | Exact contradiction of the old statement. |
| corrected claim → old hypothesis, `revises` | The new statement supersedes the old quantifiers. A true witness is not revised away. |
| result → frontier, `leaves_open` | The theorem does not settle this identified question. |
| claim ↔ prior result, `novelty_compared_with` | The arrow records a directed comparison, **not mathematical implication**. Its explanation and literature fields specify the difference. |
| result → interpretation, `supports` / `explains` | A scientific inference with its own status. |
| failure → later result, `motivates` | Discovery history, never a proof dependency. |
| individual paper → prior-work group, `documents` | Source attribution and version lineage, not independent replication or a mathematical implication. |

Other permitted relations include defines, implies, strongly_supports, tests, contradicts, limits, generalizes, special_case_of, equivalent_to, distinguished_from, resolves, extends, reproduces, uses_method, emerges_from, differs_from, potentially_overlaps, novelty_unresolved, next_action, weakens and requires_review. An unresolved live `contradicts` edge is flagged unless a resolution is recorded. A causal or discovery story does not confer deductive necessity.

## Views, coverage and provenance freshness

`views` contains twelve curated small subsets, column layouts, descriptions and reading cues. The executive view contains twelve major nodes. The theorem/evidence/assumption selectors derive focused neighborhoods from the **same graph**; there is no per-view scientific copy. The common-model display group contains only the three declared baseline conditions; complete per-theorem assumptions remain in the detail panel.

Levels are 0 (overview/story), 1 (scientific structure), 2 (evidence and individual paper comparisons), and 3 (raw artifact provenance). The selected node remains synchronized across navigation. The browser supports a readable list alternative, keyboard selection and panning, status filtering, global search and exact source excerpts. Static SVGs are curated defaults; they do not reflect a later interactive claim selection. An abstract-only paper node remains unresolved where its exact theorem comparison is unverified, even if the abstract reports a result.

`report_coverage` is a reviewed mapping of the seven substantive report sections to their consequential entities. `source_hashes` fingerprints the exact referenced scientific versions. Any change prompts re-review. **This is not an automatic semantic completeness detector:** an unchanged curated coverage list cannot prove that every sentence was understood. The independent semantic audit supplies that additional check. Volatile operational STATE.md is linked conceptually but excluded from scientific version fingerprints during concurrent manuscript work; stable D023/PAPER-STRUCTURE references ground the next action.

`validate.py` detects missing fields, links, anchors and comparison/verification references; rejected logical dependencies; unresolved contradictions; orphan evidence; unmotivated frontiers; missing report mappings; stale sources; and unsupported formal badges. A clean graph is not a proof or a novelty certificate. Ten injected corruptions test the consequential detection paths in [validation-checks.json](validation-checks.json).
