# Research knowledge atlas

Open the [interactive atlas](interactive/index.html). It runs directly from a local file, with no network dependencies or account. The [executive SVG](views/research_overview.svg) and [scientific story](views/scientific_story.svg) are useful starting points for static review.

The atlas is a claim-centered interface to the completed scientific audit: **141 semantic entities, 419 typed relationships and 12 coordinated views**, including 30 individual paper records beneath 15 prior-work groups. The source of truth remains the [mathematical specification](../analysis/publication-theorems.md), [evidence records](../evidence/RECORDS.md), proofs and [report](../outputs/REPORT.md). The map does not create a new theorem or certify novelty. Concurrent manuscript preparation is preserved and is not interpreted as new scientific evidence.

## Read at four depths

- **Overview:** the research question, four main results, interpretation, publication risks and next action.
- **Scientific structure:** definitions, assumptions, proof dependencies, evolution, falsification, literature, geometry and frontier.
- **Evidence:** choose a theorem, then select its Evidence tab to inspect supporting proofs, independent checks, failed attempts and typed relationships.
- **Provenance:** open the exact referenced section, source/script/output, or recorded primary-paper route. Embedded excerpts are generated from those originals and have explicit truncation notices.

The written badge carries evidence status; color carries scientific role. An analytically proved counterexample is distinct from the falsified hypothesis it defeats. Numerical discovery and saved manifest checks never appear as analytic proofs. No formal scientific proof is claimed.

## Views

| View | What it makes visible | Static version |
| --- | --- | --- |
| A · Research overview | Question → exact/stability results → interpretation → risk/next action | [SVG](views/research_overview.svg) |
| B · Mathematical objects | Q → π → currents → σ, alongside Q → Ψ → fiber → entropy set | [SVG](views/concept_map.svg) |
| C · Theorem dependencies | Conditions, lemmas and verification for a selected theorem | [SVG](views/theorem_dependencies.svg) |
| D · Claim and evidence | Proof versus symbolic/numerical checks and raw provenance | [SVG](views/claim_evidence.svg) |
| E · Research evolution | Failures that changed the interpretation | [SVG](views/research_evolution.svg) |
| F · Counterexamples | Eight rejected claims, exact witnesses and corrected scope | [SVG](views/falsification_map.svg) |
| G · Literature and novelty | Fifteen prior-work groups, with 30 individual papers available through drill-down and search | [SVG](views/literature_novelty.svg) |
| H · Assumption sensitivity | State count, topology, positivity, trace, caps and observation experiment | [SVG](views/assumption_sensitivity.svg) |
| I · Fibers and geometry | Schematic balanced entropy sets plus the actual three-state limit | [Quantitative SVG](views/parameter_geometry.svg), [PNG](views/parameter_geometry.png), [data](views/geometry-data.json) |
| J · Open frontier | Settled fixed-count stability versus unresolved exact/observation classes | [SVG](views/open_frontier.svg) |
| S · Current scientific story | Exact knowledge can remain thermodynamically fragile | [SVG](views/scientific_story.svg) |
| ? · Publication risk | What could invalidate the narrow manuscript case | [SVG](views/publication_risk.svg) |

## The scientific story

The whole balanced five-state entropy fiber has a sharp unbounded / two-point / unique transition. Yet a perfect inverse fit need not give a finite entropy upper ceiling under any nonzero observation tolerance. A three-state tree already demonstrates a singular entropy functional despite locally Lipschitz rate recovery. Two fully hidden states introduce a second obstruction: observational ambiguity even near a complete source. The fixed-N criterion is settled for one known resolved pair and unknown bidirected topology; it is not a claim about every state cap, every extra rate constraint or every observation model.

The publication case remains provisional. Finite positive fibers, relative-entropy singularities and general confidence-limit impossibility are known mechanisms. A specifically matching prior physical theorem, particularly among the named source gaps, could change attribution. The long global endpoint exhaustion remains the main target for expert scrutiny. The saved highest-value action is the self-contained proof core for the two central results, currently being pursued by the concurrent manuscript task.

## Rebuild and validate

From the repository root:

```powershell
.\.venv\Scripts\python.exe -B knowledge/validate.py
.\.venv\Scripts\python.exe -B knowledge/build.py
.\.venv\Scripts\python.exe -B knowledge/check_validation.py
node --check knowledge/interactive/app.js
```

Accepted environment: Python 3.9.12, NetworkX 3.2.1, matplotlib 3.9.4 and mpmath 1.3.0. These packages were already available in the research environment. The graph is JSON; no database, frontend package manager, CDN or Graphviz installation is needed. NetworkX performs graph checks; the small curated SVG layouts preserve semantic grouping. Matplotlib renders the quantitative scientific figure, with 100-digit formula evaluation saved separately. Exact proofs, not the 70 plotted points, establish the limit.

`build.py` reads graph.json and its linked originals. It writes the static views, parameter illustration, and the browser's derived data payload. It does **not** run old scientific scripts or overwrite accepted outputs. The source graph is editable; generated data.js, SVGs, PNGs and geometry-data.json should be rebuilt rather than hand-edited. Browser JavaScript and CSS in `interactive/` are maintained source files.

Optional browser QA, using an isolated local Chrome/Edge profile:

```powershell
node knowledge/check_browser.mjs
```

Set `ATLAS_BROWSER` if the browser is installed elsewhere. The script uses a local file URL and a loopback debugging connection, never a signed-in profile; it needs permission to launch the browser. The temporary `.browser-qa/` profile is ignored and may be removed after the process closes. [browser-checks.json](browser-checks.json) records 30 successful interaction/layout checks, browser/runtime versions and input hashes. [validation-checks.json](validation-checks.json) records ten adversarial map corruptions detected. [semantic-review.md](semantic-review.md) records the independent scientific consistency review and its resolved findings.

The [reader walkthrough and validation notes](validation-notes.md) answer the ten requested review questions and preserve implementation failures and corrections. No external reader study is claimed.

For a local preview that serves the original Markdown/script links, run `.venv\Scripts\python.exe -B -m http.server 8765 --bind 127.0.0.1` at repository root and open `http://127.0.0.1:8765/knowledge/interactive/index.html`. No hosted deployment is created.

## Maintain the map during consequential research changes

1. Update the original proof/evidence record first. Review the exact claim, quantifiers, independent-check scope and novelty comparison.
2. Update the affected graph.json nodes/edges; preserve stable IDs and rejected statements. Add a consequential claim to the relevant report-coverage entry and focused views. Do not add scratch calculations as nodes.
3. Run validation. Inspect every flagged gap and every changed scientific source. Do not resolve a gap by inventing evidence or automatically promoting status.
4. After that review, accept the reviewed source versions with `.venv\Scripts\python.exe -B knowledge/validate.py --accept-reviewed-sources`, then rebuild. This flag records your review decision; it does not perform the scientific review.
5. Recheck the overview and skeptical view after a material interpretation change. A routine scratch calculation does not require graph maintenance.

See [schema.md](schema.md) for field and direction conventions. Historical review inputs are archived under `review-inputs/`; graph.json is the sole maintained semantic interface. [STATE.md](STATE.md) checkpoints this visualization task separately from the ongoing manuscript work.
