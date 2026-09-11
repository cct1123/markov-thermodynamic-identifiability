# Manuscript reproducibility and figure review

2026-09-11 UTC. Scope: independent computational replay, figure production,
repository coverage, and provenance review for the manuscript task. No historical
scientific output, state, evidence record, or human-owned brief was edited. This
review does not establish novelty or independently prove universal support
exhaustion.

The reproducible package is in
[manuscript/scripts/reproduce.py](../manuscript/scripts/reproduce.py), with
[instructions](../manuscript/scripts/README.md) and the complete
[computational manifest](../manuscript/supplementary/computational-results.json).
All 15 deterministic scientific scripts replay successfully. After excluding
timestamps and other run provenance, their scientific payloads match the accepted
historical outputs exactly. The 22 historical top-level scientific JSON outputs
are unchanged by SHA-256 comparison. No scientific discrepancy was found in the
replayed calculations.

## Coverage and what was actually checked

The review read the current brief/state, analysis index, endpoint and fixed-trace
proofs, the relevant cone/path and precision checker sources, computational
helpers, requirements, infrastructure/formal documentation, map generators and
validator, the semantic map review, and all 98 source-shard node summaries. It
examined central checker implementations in detail, parsed all 26 Python sources
under `analysis/`, inspected the structure and provenance of all 22 saved
top-level scientific JSON artifacts, and executed the following 15 scientific
scripts with their intended writes intercepted in memory:

| Scope | Replayed scripts |
| --- | --- |
| Small-state identification and four-state classification | `check_small_networks.py`, `check_four_state_classification.py`, `check_observable_criterion.py` |
| State splitting and five-state constructions | `check_state_splitting.py`, `check_five_state_extensions.py`, `check_theta_residue_construction.py` |
| Global theta/balanced boundary supporting algebra | `check_theta_fast_spectral.py`, `check_balanced_boundary_witness.py`, `derive_balanced_path.py`, `check_balanced_cone_bound.py`, `check_balanced_cone_sufficiency.py`, `check_balanced_fold.py` |
| Entropy instability and physical inversion | `check_finite_precision_instability.py`, `check_three_state_precision.py`, `check_publication_audit.py` |

All assertions executed with Python optimization disabled. The manifest contains
the full fresh results and every historical result's original hash, rather than
only a pass/fail summary. This is a replay of established methods, not an
independent proof solely because another agent ran them.

An additional exact calculation executes the separate cone-to-path construction
in [publication-endpoint-audit.md](publication-endpoint-audit.md). It constructs
the generator from the modal cone equality conditions in a quadratic extension
of `Q(z_*)` and agrees coefficientwise with the path witness, with cancellation
back to `Q(z_*)`. This differs from the physical exit-chart method but shares
the same modal data and SymPy arithmetic engine. The extracted code has its own
hash in the new manifest.

A separately implemented symbolic check derives the three-state stationary tree
weights directly from cofactors of `-Q`, verifies all three oriented stationary
currents, the cycle rate ratio, row sums, trace, and source mean next-mark times.
The figure computation uses fresh 100-digit stationary solves and independently
sums stationary edge-flux entropy. The resulting endpoint entropies lie inside
the previously certified rational intervals:

\[
\sigma_\theta=0.0629464002368743529116869537648\ldots,\qquad
\sigma_p=0.0655796859668414456518918852964\ldots.
\]

The displayed decimal digits are numerical diagnostics. The accepted interval
endpoints and positive separation come from rational root/sign/logarithm bounds
re-executed by `check_balanced_fold.py`. Its ten exact marked derivative matrices
at orders 0 through 9 give all-time equality under the five-state cap. No finite
floating-point time grid is substituted for that certificate.

The seeded discovery probes were inventoried but not rerun: their outcomes are
historical discovery evidence and do not establish the final exclusion theorem.
The new figure calculations use no optimizer or random seed. One replayed legacy
construction checker runs deterministic LP diagnostics, which are separate from
its exact certificates and not exclusion proofs. The driver uses no graph
enumeration, external data, or network. Infrastructure smoke/solver demonstrations remain separate from
scientific evidence. General graph counts do not certify the continuous-rate
classification.

## Publication figures

The following new figures are generated in vector PDF/SVG and 300-dpi PNG by the
same script. Both PNG renderings were visually inspected and revised to remove
overlapping titles, edge crossings through nodes, and an overlong panel title.
The final legends distinguish rounded values, exact identities, analytic bounds,
and asymptotes.

1. [Balanced fiber](../manuscript/figures/balanced-fiber.pdf). The upper panels use
   the actual supports decoded from the exact endpoint coefficient matrices:
   six undirected edges for the theta generator and seven for the path generator.
   Bidirectional arrows indicate reciprocal support, not equal rates. The red
   pair is the only observed pair. Hidden labels follow the exact matrix order;
   their geometric layout changes to avoid crossings. The bottom boxes state
   the three proved entropy-fiber regimes for the at-most-five-state class.
   They are a qualitative classification table, not a parameter-scale plot or
   an invented continuous entropy curve.
2. [Three-state instability](../manuscript/figures/three-state-instability.pdf).
   The left panel plots the independently computed entropy of the exact
   fixed-trace family with `kappa=exp(-1/epsilon**2)` and its proved asymptote.
   The right panel plots the exact maximum-entry error `epsilon` and the proved
   bound `2*(epsilon+kappa)` for maximum joint-kernel row total variation. The TV
   line is not a measured distance. The parameter axis decreases to the right.
   At the smallest plotted opening `epsilon=0.003`, the numerical entropy is
   about `110.6616534`, the generator error is `0.003`, and the displayed TV bound
   rounds to `0.006`; the reverse rate remains strictly positive in arbitrary
   precision, with logarithm about `-111111.1111`.

The 100 plotted parameter values and outputs are retained as decimal strings.
The reverse rates are never converted to machine floats, clipped, or
regularized. The check compares direct entropy with the cycle formula to
relative tolerance `1e-90` at 100 decimal digits. Rates and entropy are expressed
in the fixed inverse-time units of the displayed generators, with natural logs
and `k_B=1`; total variation is dimensionless. The plot illustrates the analytic
limit proof rather than proving a divergent limit from samples.

At the initial checkpoint no usable existing publication figure was present. The only existing image was
the generic capability sweep. `knowledge/build.py` contains an educational
three-state plotting routine, but its generated views were absent. That routine
was inspected for formula consistency; publication figures were made separately.

## Knowledge-map and formal-status qualifications

At the first computational checkpoint, the map contained three authored source
shards with 29 claim, 36 concept/assumption, and 33 context nodes; no merged graph
or rendered view existed. This earlier review checkpoint records that historical
snapshot; the final driver inventory records the completed map's presence.
Concurrent authorized map work subsequently completed the integration.
On resumed inspection, `knowledge/graph.json`, twelve views, the browser data,
and validation records were present. I reran the validator without writing:
all 111 nodes, 389 typed relationships, twelve views, seven mapped report sections,
and 56 source fingerprints passed, with no errors or warnings at that checkpoint.
The former status defects are corrected in the live graph:
`check_legacy_saved` has `provenance_checked`, and all eight `cex_*` witnesses have
`analytically_proved`, distinct from their falsified conjectures. The generated
quantitative teaching figure was visually inspected and agrees with the same
three-state formula. Its TV line uses the valid looser bound `min(1,4e)`, whereas
the publication figure uses `2(e+k)`. Saved browser/validation mutation tests were
read as UI checks, not scientific proof. The final graph remains a navigational
interface to the proof records rather than an independent proof source.

`formal/` contains only a pinned scaffold and smoke theorem. There is no accepted
formal build manifest or compilation log. Nothing in the manuscript package is
formally verified, and no new Lean installation/build was attempted. The
general support and neighborhood theorems retain conventional proof status.

## Environment, commands and limitations

The completed run uses Python 3.9.12, NumPy 2.0.1, SciPy 1.13.1, SymPy 1.14.0,
mpmath 1.3.0 and Matplotlib 3.9.4 on Windows. The matching research requirements
and complete platform-specific lock are preserved. A fresh
`.venv/Scripts/python.exe -m pip check` returned `No broken requirements found.`
The complete scientific replay command is:

```powershell
.\.venv\Scripts\python.exe -B manuscript/scripts/reproduce.py
```

The exact command, current source and historical-output hashes, execution time,
package versions, selected precision and tolerances, deterministic input rule,
full captured replay outputs, numerical figure inputs, and output figure hashes
are in the new manifest. Reproduction requires the surrounding repository,
because the driver intentionally reuses the preserved scientific sources and
exact proof artifact. An archival submission should include those dependencies.

The first exploratory run passed all calculations but identified a timestamp
field `created_utc` as a changed scientific path; this was corrected in the
metadata exclusion rule. Figure layout and decimal-label presentation were also
revised, followed by a complete stable-source replay. No scientific identity or
historical output changed. A read-only shard print initially used Windows'
default encoding and failed; it was rerun with explicit UTF-8 and ASCII-escaped
terminal output. These transient inspection/presentation failures supply no
scientific counterevidence.

The major remaining correctness risk is the long global conventional support
exhaustion, not a failed numerical check. Neither unchanged output hashes nor
successful replays independently prove that every admissible support was
included. The manuscript's statement and proof audit must retain all denominator,
positivity, state-cap, irreducibility, mark-incidence, boundary and topology
conditions. The main scientific originality risk remains comparison with the
closest physical/positive-realization theorem, which lies outside this
computational review.

## Resumed manuscript, archive, and collective coverage review

The finished `manuscript/main.tex` and `manuscript/supplementary/proofs.tex` were
read in full against the exact checkers and figure content. The following
manuscript corrections were sent to the coordinator: restore the missing `-k`
in the displayed stationary weight `w_h=1-k+2e-ek`; describe the Figure 1 numbers
as rounded values rather than displayed intervals; relate Figure 2's
epsilon/kappa notation to the article's e/k; and repair the damaged killed-block
subscript in the Schur-complement formula. The underlying exact scripts and
entropy formula were already correct. The mathematical referee independently
found the stationary-weight error and the LP-description qualification.

The manuscript's stronger whole-interval table bounds were independently checked
by replaying the interval checker after substituting `z=21/2+xi`, keeping every
operation rational. All twelve printed lower bounds pass. The critical lower
endpoints are above `171.9173`, `0.03048437`, and `0.07071919`, respectively,
which justify the table's `170`, `3/100`, and `7/100`. The executable calculation
is [check_table_bounds.py](../manuscript/scripts/check_table_bounds.py), and the
full exact output is [table-bound-checks.json](../manuscript/supplementary/table-bound-checks.json).
This reuses the historical geometric formulas and interval routines, whereas the
mathematical reviewer separately implemented the same shifted check from scratch
in [manuscript-math-independent-check.py](manuscript-math-independent-check.py).
Their agreement does not supply a second symbolic-arithmetic engine.

The completed team review has the following explicit coverage, with different
levels kept distinct:

| Repository material | Review and validation coverage |
| --- | --- |
| `PROJECT.md`, `STATE.md`, `AGENTS.md`, root README/architecture, theorem specification, report and paper structure | Coordinator and reviewers reconstructed current intent and the two central theorem scopes; operational instructions are not scientific evidence. |
| `publication-endpoint-audit.md`, `balanced-cone-bound.md`, `theta-balanced-boundary.md`, `theta-fast-spectral-audit.md`, `theta-family-construction-audit.md`, `theta-parameter-strata-audit.md`, `compatibility-orbit.md`, and hidden-pair/splitting notes | Detailed current mathematical review and self-contained proof transcription, with independent arithmetic and all central deterministic replays; see [mathematical review](manuscript-mathematical-review.md) and [referee report](manuscript-referee-math.md). |
| `publication-stability-audit.md`, `entropy-neighborhood-audit.md`, three-state fixed-trace/precision and one-hidden robustness notes, four-state finite-precision notes | The current theorem, coupling, inverse, trace/rate assumptions, generator-versus-entropy distinction, and stationary-window scope were compared explicitly; example/inverse arithmetic was replayed. Older common-cap hypotheses are sufficient older results, superseded only for the joint-kernel result. |
| `small-network-audit.md`, `four-state-classification-audit.md`, `unknown-topology-audit.md`, `nonminimal-four-state-audit.md`, `observable-four-state-criterion.md`, `five-state-sparse-audit.md`, `path-cap-uniqueness-audit.md` | Older scopes and mechanisms were read or traced through the detailed legacy inventory, with relevant scripts replayed. Selected original proof sections were reread during this follow-up. These classify narrower classes and do not contradict the selected manuscript; the article omits the separate smallest-cap claim rather than importing its entire proof dependency. |
| `theta-global-audit.md`, `theta-fast-case-audit.md`, `theta-fast-hidden-paths.md`, `positive-realization-obstructions.md`, balanced boundary witness and discovery probes | Local isolation, chart singularities, repeated poles, finite-Hankel positivity, failed first-order threshold and bounded search limitations were retained. Later analytic classifications supersede older open conclusions; unsuccessful searches remain inconclusive. Exact witnesses/identities were replayed where in the deterministic suite. |
| All 26 pre-existing Python analysis sources and 22 top-level scientific JSON outputs | Syntax/JSON/provenance inventory; fifteen actual deterministic script replays with full captured output. Three seeded discovery searches were inspected as historical diagnostics and not rerun. New manuscript arithmetic sources/outputs are additional files. |
| Every literature memorandum in `evidence/`, `RECORDS.md`, and manuscript bibliography | Assigned literature reviewer and coordinator audited the source comparisons and verified actual manuscript citations against primary sources; see [literature review](manuscript-literature-review.md) and [literature referee review](manuscript-referee-literature.md). This computational reviewer does not claim fresh retrieval of those papers. |
| `docs/`, research helpers, capabilities sources and saved checks, dependency pins | Capability/proof-status distinctions, total-escape convention, exact/high-precision support handling, graph enumeration boundaries, and historical environment state were inspected. A fresh dependency check passes. Capability examples are not promoted to scientific evidence. |
| `formal/` | Scaffold, pins, smoke statement and documented axiom/build requirements were inspected. No research formal proof or successful Lean build is present. |
| `knowledge/` sources, complete merged graph, validation/schema/reader notes, UI code, generated views and geometry | Initial shard summaries and later merged statuses checked; fresh read-only structural validation passes. Quantitative teaching geometry visually inspected. Browser/corruption checks were read as saved UI validation; this reviewer did not repeat browser automation. No map status independently certifies science. |
| `manuscript/main.tex`, `supplementary/proofs.tex`, figures, checker manifests | Full equation/proof/figure comparison by current reviewers, followed by coordinator corrections and compile/visual QA. |

One consequential historical notation defect is confirmed: the hidden-pair
summary in `publication-legacy-audit.md` describes lambda as external escape
sums but then uses the total-escape shear formula. The original hidden-pair note,
fresh independent checker, and assembled manuscript correctly use
`lambda_h=m+sum(Y_h)`, `lambda_k=n+sum(Y_k)`. No theorem should use the abbreviated
legacy phrase to redefine those quantities. No other consequential contradiction
with the selected manuscript was found in this coverage pass.

[package.py](../manuscript/scripts/package.py) supplies a portable root-relative
archive at `outputs/manuscript-package.zip`. It collects the manuscript plus the
complete small scientific source/evidence/documentation trees, their saved
outputs, pins, and maps. This avoids fragile hand-pruning of imported helpers and
source-hash inputs: `reproduce.py` needs the fifteen historical scripts, their
local imports, their accepted JSON outputs, the endpoint proof block, and the
proof notes listed in their hash manifests. The archive also contains the new
independent math/table scripts and outputs. It excludes environments, Git,
prompt history, caches, compiler binaries, temporary/build auxiliaries, manuscript
PNG duplicates and browser QA screenshots. The generated `PACKAGE-MANIFEST.json`
lists every included byte length and SHA-256; the script verifies the zip CRC and
every member hash after creation. `--list` was executed successfully without
writing the archive. The coordinator invokes the final archive after its README,
PDF, provenance, and review artifacts are final. Archive extraction preserves
the root-relative commands and does not require access to the original checkout.

Final figure QA removed the redundant observed-edge annotation, aligned the
generator titles with the article as `Q(z_*)` and `Q_*`, and replaced undefined
fiber-symbol shorthand with the words "Unbounded entropy", "Two entropy values",
and "Unique generator". The final PNG was inspected. One complete stable-source
driver run after these edits passed all fifteen replays with identical scientific
payloads, unchanged hashes for all 22 protected JSON files, and verified hashes
for the driver and all six figure exports. The archive was not created in this
assignment; final invocation remains with the coordinator after its final files
are saved.
