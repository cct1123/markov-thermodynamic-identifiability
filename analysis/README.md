# Reproducible analysis

The recorded investigation uses exact derivations, small deterministic checks and bounded seeded discovery probes. Those results do not rely on graph enumeration or a general inference framework.

For new work, the [scientific stack guide](../docs/research-stack.md) adds an isolated Python environment, shared CTMC/high-precision helpers, symbolic mathematics, small graph enumeration and adversarial search. [Capability tests](capabilities/README.md) exercise these tools on generic examples, separately from the scientific results below. Optional [exact constraint tools](../docs/optional-tools.md) and [formal verification](../formal/README.md) are available when justified. The historical scripts, pins and scientific outputs remain unchanged by this infrastructure upgrade.

## Derivations

| Artifact | Purpose |
| --- | --- |
| [formulation.md](formulation.md) | Model, full joint data, admissible classes, entropy image, finite exact kernel certificate |
| [small-network-audit.md](small-network-audit.md) | At-most-three-state recovery; lumpable and minimal four-state examples |
| [compatibility-orbit.md](compatibility-orbit.md) | Minimal hidden-similarity parameterization and fixed full-diamond classification |
| [four-state-classification-audit.md](four-state-classification-audit.md) | Fixed-topology minimal four-state dichotomy; independent geometric boundary proof |
| [unknown-topology-audit.md](unknown-topology-audit.md) | Two global uniqueness cases; constructive divergent paths and support openings |
| [nonminimal-four-state-audit.md](nonminimal-four-state-audit.md) | Extension to every four-state realization; automatic minimality and lumpable exceptions |
| [observable-four-state-criterion.md](observable-four-state-criterion.md) | Complete unknown-topology uniqueness test from derivatives through order three; explicit reconstruction |
| [state-splitting-audit.md](state-splitting-audit.md) | One additional fully hidden state gives unbounded entropy; visible-deficit test and state-cap implications |
| [hidden-pair-boundary-audit.md](hidden-pair-boundary-audit.md) | Fixed-dimension pair constructions, neighborhood obstructions and independent embedded checks |
| [five-state-sparse-audit.md](five-state-sparse-audit.md) | Complete distinct-diagonal five-state subclass; two exact examples with embedded executable checks |
| [path-cap-uniqueness-audit.md](path-cap-uniqueness-audit.md) | Maximal derivative delay under a state cap forces a path and unique directed rates |
| [theta-global-audit.md](theta-global-audit.md) | Isolated minimal five-state model with a distant unbounded component; exact global exit-triangle coordinates |
| [theta-parameter-strata-audit.md](theta-parameter-strata-audit.md) | Exact minimality and chart strata, Perron obstruction, and a complete four-state realization at the exception |
| [theta-family-construction-audit.md](theta-family-construction-audit.md) | Constructive unbounded regions, local-opening criteria, reducible-hidden rigidity and rejected coverage shortcut |
| [positive-realization-obstructions.md](positive-realization-obstructions.md) | Strict fixed-order cone reduction and the entire slow-coincidence unboundedness proof |
| [theta-fast-case-audit.md](theta-fast-case-audit.md) | Exact local isolation, global coordinates and inconclusive targeted search at theta(100,100) |
| [theta-fast-hidden-paths.md](theta-fast-hidden-paths.md) | Independent incidence exhaustion and exact polynomial exclusion of potentially bounded hidden paths |
| [theta-fast-spectral-audit.md](theta-fast-spectral-audit.md) | Global generator uniqueness at theta(100,100), balanced rates z≥40 and an open parameter region |
| [balanced-boundary-witness.md](balanced-boundary-witness.md) | Exact rational counterexample to the proposed first-order threshold; independent cone and endpoint audits |
| [balanced-cone-bound.md](balanced-cone-bound.md) | Sharp global balanced-theta exclusion and rigid endpoint triangle |
| [theta-balanced-boundary.md](theta-balanced-boundary.md) | Exact quartic endpoint, complete two-model fiber and certified differing entropy |
| [entropy-neighborhood-audit.md](entropy-neighborhood-audit.md) | Every positive observational neighborhood is entropy-unbounded with two fully hidden states; exact trace, bounded rates and finite-horizon coverage consequence |
| [finite-precision-instability.md](finite-precision-instability.md) | Explicit four-state exact-kernel families approaching a uniquely identified source; independent coupling and entropy checks |
| [three-state-fixed-trace-audit.md](three-state-fixed-trace-audit.md) | Smallest fixed minimal dimension for instability, preserving trace −4 and rate cap one |
| [one-hidden-robustness-audit.md](one-hidden-robustness-audit.md) | Tree/positive-triangle local stability classification under cap three; distinction from globally honest confidence limits |
| [three-state-precision-audit.md](three-state-precision-audit.md) | Globally unique two-state zero-deficit data have unbounded finite-precision neighborhoods with a third state |

The current synthesis is [REPORT.md](../outputs/REPORT.md). The later proofs resolve the earlier four-state question and several five-state subclasses. The balanced quartic endpoint now proves the existence of a minimal five-state bounded-nonunique entropy fiber; the general five/six-state classification and publication novelty remain unresolved.

The finite-precision continuation also proves that exact finite fibers need not yield robust entropy upper ceilings, even with fixed state count, trace and bounded rates. Three-state positive triangles supply a local continuity exception under a common rate cap; the exact and approximate questions remain distinct. Independent audits and failed attempts accompany the constructive proofs. [E054–E058](../evidence/RECORDS.md#e054)

## Reproduce

From the repository root, with Python and the versions in [requirements.txt](requirements.txt):

~~~powershell
python analysis/check_small_networks.py
python analysis/check_four_state_classification.py
python analysis/check_state_splitting.py
python analysis/check_observable_criterion.py
python analysis/check_five_state_extensions.py
python analysis/probe_theta_compatibility.py
python -B analysis/check_theta_residue_construction.py
python -B analysis/probe_theta_fast_case.py
python -B analysis/check_theta_fast_spectral.py
~~~

Accepted runs used Python 3.9.12, NumPy 2.0.1 and SciPy 1.13.1 on Windows. Each script overwrites only its corresponding generated JSON file. The later scripts import small exact helpers from earlier scripts; importing does not run their checks.

| Script | Recorded output | Checks and evidence |
| --- | --- | --- |
| [check_small_networks.py](check_small_networks.py) | [small-network-checks.json](small-network-checks.json) | Small-network reconstruction, stationary laws, normalization, minimality and all-time equality; independent exponentials at 66 times; entropy formulas and two negative controls. [E020](../evidence/RECORDS.md#e020) |
| [check_four_state_classification.py](check_four_state_classification.py) | [four-state-classification-checks.json](four-state-classification-checks.json) | Three exact divergent boundaries, five support openings, two signed-grid uniqueness controls and a nonminimal guard. [E026](../evidence/RECORDS.md#e026) |
| [check_state_splitting.py](check_state_splitting.py) | [state-splitting-checks.json](state-splitting-checks.json) | Four-to-five-state cloning, stationary aggregation, exact kernels and entropy slope; two nonminimal lumped families. [E029](../evidence/RECORDS.md#e029) |
| [check_observable_criterion.py](check_observable_criterion.py) | [observable-criterion-checks.json](observable-criterion-checks.json) | Nine rational cases: four exact generator reconstructions and five nonunique controls, including repeated poles and singular coupling. [E031](../evidence/RECORDS.md#e031) |
| [check_five_state_extensions.py](check_five_state_extensions.py) | [five-state-extension-checks.json](five-state-extension-checks.json) | Exact local isolation, simultaneous three-coordinate opening, distant compatible model and divergent endpoint; five/six-state path reconstruction. [E036](../evidence/RECORDS.md#e036) |
| [probe_theta_compatibility.py](probe_theta_compatibility.py) | [theta-compatibility-probe.json](theta-compatibility-probe.json) | Bounded SLSQP discovery search: two models, thirteen starts each, seed 20260910; exact witnesses validated separately. [E036](../evidence/RECORDS.md#e036) |
| [check_theta_residue_construction.py](check_theta_residue_construction.py) | [theta-residue-checks.json](../outputs/theta-residue-checks.json) | Five exact Q(sqrt(6)) constructions, all-time kernel identities, signs, stationary laws and exceptional ranks; standard library only. [E043](../evidence/RECORDS.md#e043) |
| [probe_theta_fast_case.py](probe_theta_fast_case.py) | [theta-fast-probe.json](theta-fast-probe.json) | Exact local-isolation certificate and inconclusive thirteen-start search at theta(100,100), seed 20260911. [E042](../evidence/RECORDS.md#e042) |
| [check_theta_fast_spectral.py](check_theta_fast_spectral.py) | [check_theta_fast_spectral.json](../outputs/check_theta_fast_spectral.json) | Exact modal identities, source ranks, wedge inequalities and polynomial bounds supporting the global proof; standard library only. [E048](../evidence/RECORDS.md#e048) |
| [probe_balanced_boundary.py](probe_balanced_boundary.py) | [balanced-boundary-probe.json](balanced-boundary-probe.json) | Bounded seeded complete-support discovery near the balanced boundary; failures retained, no exclusion certificate. [E051](../evidence/RECORDS.md#e051) |
| [derive_balanced_path.py](derive_balanced_path.py) | [balanced-path-polynomial.json](balanced-path-polynomial.json) | Exact parameter-dependent hidden-path elimination and independently recovered quartic discriminant. [E051](../evidence/RECORDS.md#e051) |
| [check_balanced_boundary_witness.py](check_balanced_boundary_witness.py) | [balanced-boundary-witness.json](../outputs/balanced-boundary-witness.json) | Rational interval witness, exact second-order opening and independent full transfer identities. [E050](../evidence/RECORDS.md#e050) |
| [check_balanced_cone_bound.py](check_balanced_cone_bound.py) | [balanced-cone-bound-checks.json](balanced-cone-bound-checks.json) | Exact generic envelope, discriminant and root/sign isolation supporting the global proof. [E051](../evidence/RECORDS.md#e051) |
| [check_balanced_cone_sufficiency.py](check_balanced_cone_sufficiency.py) | [balanced-cone-sufficiency-checks.json](balanced-cone-sufficiency-checks.json) | Exact interval margins supporting complete realizations throughout the remaining subcritical interval. [E052](../evidence/RECORDS.md#e052) |
| [check_balanced_fold.py](check_balanced_fold.py) | [balanced-fold-checks.json](../outputs/balanced-fold-checks.json) | Exact algebraic endpoint, reciprocal path support, ten marked derivatives, stationary laws and rational entropy enclosures; independent numerical checks. [E051](../evidence/RECORDS.md#e051) |
| [check_finite_precision_instability.py](check_finite_precision_instability.py) | [finite-precision-checks.json](../outputs/finite-precision-checks.json) | Generic four-state identities, 12 rational all-time certificates/direct entropy checks and three semigroup TV diagnostics. [E056](../evidence/RECORDS.md#e056) |
| [check_three_state_precision.py](check_three_state_precision.py) | [three-state-precision-checks.json](../outputs/three-state-precision-checks.json) | Three explicit three-state families, stationary currents, exact rank/reconstruction identities, fixed-trace checks and 15 independent 100-digit stationary solves. [E057](../evidence/RECORDS.md#e057), [E058](../evidence/RECORDS.md#e058) |

For the new balanced-boundary scripts use `.venv\Scripts\python.exe -B analysis/<script>.py` from root and the [research environment](../docs/research-stack.md). The accepted run used Python 3.9.12, SymPy 1.14.0, mpmath 1.3.0, NumPy 2.0.1 and SciPy 1.13.1. Exact derivations have no random seed; the bounded discovery script records seed 20260910. Each writes only its listed new output. The number-field certificate uses exact root/sign and log-remainder enclosures; high precision alone is not the proof. The independent endpoint replay is separately preserved in [balanced-fold-independent-replay.json](../outputs/balanced-fold-independent-replay.json).

The two finite-precision scripts use the same root-relative command and environment. No search or random seed is used. They preserve old outputs and write only their listed JSON, including execution-time script hashes. The three-state audits and [four-state independent check](finite-precision-independent-check.md) also contain separately executed embedded calculations. Continuum sign, coupling, divergence, compactness and coverage arguments are conventional proofs in the notes; high-precision and quadrature values are independent diagnostics. None of these checks certifies publication novelty.

Inputs and rational or quadratic-algebraic parameter choices are embedded in the scripts and motivated in the linked proofs. No external dataset is used. Exact checks are deterministic; only the separate discovery probes use seeded random starts. Rates and entropy rates have inverse-time units, with Boltzmann's constant one. Numerical tolerances are explicit in each script.

The sparse, pair, path, theta-strata and theta-construction audit notes also contain executable independent checks and their recorded outputs/provenance. The new [hidden-path audit](theta-fast-hidden-paths.md) embeds its exact rational elimination and sign certificates; the [cone frontier](../evidence/three-state-cone-frontier.md) includes the finite-Hankel counterexample calculation. They validate specified identities and support classes without broad graph enumeration.

## Meaning and limits of the checks

Fraction arithmetic verifies generator constraints, stationarity, similarities and intertwining, ranks, and sufficient finite derivative identities. For dimensions n,n′, equality of Markov parameters at orders 0 through n+n′−1 certifies equality at every time by the Cayley–Hamilton argument in the formulation. A finite floating-point time grid alone does not supply that certificate.

Independent floating-point calculations compare matrix exponentials and stationary edge-flux entropy, including limiting logarithmic slopes. The sampled signed similarity grid is a falsification control; general uniqueness and support exhaustion rely on the analytic proofs. The observable-criterion audit uses selected rational eigenvalues and is not a general feasibility solver or a numerical fitting procedure.

Each JSON records its UTC run time, environment and SHA-256 of its script and imported local helpers where applicable. The accepted outputs match the current source files; [.gitattributes](../.gitattributes) preserves Python-source LF bytes across checkouts. Historical run hashes remain in the evidence notes. [E020](../evidence/RECORDS.md#e020) preserves an initial Fraction/NumPy arithmetic correction; [E036](../evidence/RECORDS.md#e036) and [E042](../evidence/RECORDS.md#e042) record discovery diagnostics and warnings. Numerical outcomes do not replace exact certificates.

[E044](../evidence/RECORDS.md#e044) records the maintenance replays: the shared generator validator now rejects disconnected chains despite positive stationary laws, and both seeded probes use the same search routine. All scientific results and 39 optimizer outcomes were unchanged. The five affected deterministic outputs and both probe outputs were regenerated with current provenance.

The scripts validate identities and counterexamples. General classifications, nonminimal extensions, pair/path theorems, disconnectedness and theta-region theorems are analytic deductions indexed in [E023–E043](../evidence/RECORDS.md#e023) and [E047–E048](../evidence/RECORDS.md#e047). Neither their proofs nor the computations certify literature novelty. The failed search at theta(100,100) remains inconclusive as numerical evidence; the later invariant-triangle proof establishes global uniqueness independently of that search.
