# Thermodynamic identifiability: exact results and the five-state frontier

**Research synthesis, 2026-09-10 UTC.** The problem is well posed once the observed data and admissible state budget are fixed. With one resolved observed pair, exactly four states have only unique or unbounded entropy-production fibers. The plausible open gap is whether a minimal five-state kernel can have a bounded, non-singleton entropy range under a five-state cap and unknown bidirected topology. The inspected prior literature does not settle that precise gap; publication novelty remains unestablished.

The latest analysis proves broad unbounded regions of a two-parameter five-state family, including both repeated-eigenvalue lines. One line admits no connected hidden realization at its minimal points, yet its entropy is still unbounded. Earlier work proves that an exactly isolated generator can coexist with a distant unbounded component. These results rule out two tempting shortcuts: local isolation and absence of a complete representative do not establish finite entropy bounds. The human [research brief](../PROJECT.md) is preserved; this is a working synthesis, not a paper draft.

## Precise question

Use a finite irreducible row CTMC on a simple bidirected graph, with finite positive rates in both directions of every present edge. States are even under time reversal; each ordered state pair has one thermodynamic channel. Observed marks resolve individual directed edges with known endpoint incidence. The nonempty observed set is closed under reversal.

The data are the exact joint next-mark/time densities ψIJ(t), including amplitudes, next-mark probabilities and absolute time scale. They are not merely separately normalized dwell shapes. Removing only observed off-diagonal rates from Q gives the killed generator T, retaining its original diagonals. Then

$$
\Psi(t)=R e^{Tt}B,\qquad
\sigma(Q)=\sum_{i<j:q_{ij}>0}
(\pi_iq_{ij}-\pi_jq_{ji})
\log\frac{\pi_iq_{ij}}{\pi_jq_{ji}},
\qquad \pi Q=0.
$$

Boltzmann's constant is one; entropy rate has inverse-time units. For an explicitly chosen class C, determine

$$
\mathcal S_{\mathcal C}(\Psi)
=\{\sigma(Q):Q\in\mathcal C,\ R e^{Tt}B=\Psi(t)\ \text{for all }t\ge0\}.
$$

A feasible entropy set is a singleton, bounded but non-singleton, or unbounded above. Empty compatibility means inconsistent data and assumptions. Exact state count, state cap, fixed topology, unknown topology, unrestricted finite cardinality and minimal-realization restrictions define different classes. There is no common positive lower rate cutoff.

The [formulation](../analysis/formulation.md) defines the observation process and stationary frequencies precisely. Resolved marks reset the state, making the full kernel sufficient for the observed event process. Equality of Markov parameters through order n+n′−1 certifies all-time equality for a candidate pair of dimensions n,n′. These are exact-statistics results; numerical stability requires separate work. [E016](../evidence/RECORDS.md#e016).

## Frontier and prior-art constraints

| Category | Inspected evidence | Implication |
| --- | --- | --- |
| Already known | Resolved-transition kernels, absorbing representations, boundary-rate recovery, affinity inference and compatible-model entropy minimization | These are established infrastructure. [E001–E006](../evidence/RECORDS.md#e001), [E014](../evidence/RECORDS.md#e014) |
| Known under restrictions | Exact recovery on prescribed cycle structures; aggregate equivalence and reconstruction under observation, rank and topology restrictions | Retain the theorem's original model class. [E007](../evidence/RECORDS.md#e007), [E009](../evidence/RECORDS.md#e009), [E022](../evidence/RECORDS.md#e022) |
| What bounds do not determine | Lower bounds need not determine upper bounds or uniqueness; a known upper bound requires microscopic rate-ratio information absent under partial observation | Fixed trace and bounded rates alone do not bound entropy. [E025](../evidence/RECORDS.md#e025), [E037](../evidence/RECORDS.md#e037) |
| Known non-identifiability | Exact hidden similarities, equilibrium ambiguity, one-way boundaries, finite Coxian alternatives and numerical growing entropy over equivalence classes | Neither ambiguity nor local/global distinctions in general realization theory are new. [E008](../evidence/RECORDS.md#e008), [E010](../evidence/RECORDS.md#e010), [E025](../evidence/RECORDS.md#e025), [E037](../evidence/RECORDS.md#e037) |
| Established mathematical machinery | Positive matrix realizations and invariant polyhedral cones | A cone with extra rays can require extra states; strict input/output factors and the fixed order must be checked. [E040](../evidence/RECORDS.md#e040) |
| Unresolved here | Full entropy images for general minimal five-state kernels, global positive-realization components, and finite-data stability | The checked examples and subclasses do not settle these questions. [D007](../evidence/RECORDS.md#d007) |
| Plausible small contribution | Complete four-state classification; exact five-state coexistence of isolation and unbounded alternatives; sharper global criteria for sparse models | Publication novelty remains conditional on theorem-level comparison. [E030](../evidence/RECORDS.md#e030), [E033–E035](../evidence/RECORDS.md#e033) |

[Ehrich (2021)](https://arxiv.org/html/2105.08803v2), section 4, exactly parameterizes a four-state discrete-time aggregate-equivalence class and reports growing sampled entropy with a near-one-way mechanism. [Wagner–Timmer (2000)](https://doi.org/10.1016/S0006-3495(00)76529-5) establishes exact equilibrium ambiguity; [Siekmann (2026)](https://doi.org/10.1007/s11538-025-01558-3), Eq. (62), explicitly constructs equivalent one-way CTMC boundaries. These are strong antecedents, with different observation assumptions.

The new close-source check found finite isolated alternatives within Coxian representations: [Rizk–Burke–Walsh (2019)](https://arxiv.org/pdf/1901.03849v2), Theorem 2 and Algorithm 1. Their one-way transient form and single entrance do not exhaust our bidirected stationary model class. The marked-absorption extension and its restrictions are recorded in [E037](../evidence/RECORDS.md#e037). A finite list of generators also need not have different entropy values.

[Nishiyama–Hasegawa (2023)](https://arxiv.org/pdf/2306.15251v2), Eq. (8), gives an entropy upper bound using dynamical activity and the maximal microscopic forward/reverse rate ratio. A fixed minimal orbit bounds activity through its trace, but does not supply a uniform rate-ratio bound.

Closed minimal orbits and endpoint inverse-Jacobi reconstruction are established theory. Their CTMC specializations are attributed in [E025](../evidence/RECORDS.md#e025) and [E034](../evidence/RECORDS.md#e034). The [latest frontier memo](../evidence/five-state-frontier-followup.md) records exact locators, bounded citation tracing and the focused disconnected-fiber search. No matching coexistence theorem was located; that does not certify novelty. Larget's full canonical theorem, some original PH canonical results and the original Xiang reconstruction proof remain access gaps.

[Van den Hof (1997)](https://ir.cwi.nl/pub/127/0127D.pdf), Theorems 3.1 and 4.2, supplies continuous-time invariant-cone existence and minimality conditions. For the minimal theta fiber, a common trace-based shift reduces complete CTMC feasibility exactly to a strict order-three discrete-time matrix realization; normalization follows automatically. The primary theorem does not guarantee the required three-ray cone. Förster–Nagy's strict-realization theorem is a close lead, but its full dimension and input/output hypotheses remain an access gap. [Primary-source assessment](../evidence/positive-realization-frontier.md), [E040](../evidence/RECORDS.md#e040).

## Latest result: parameter regions and exceptional lines

Replace the last row of the generator below by `(a,b,0,0,−a−b)`, with a,b>0. Put

$$
s=a+b,\qquad \alpha=9-2\sqrt6,\qquad \beta=9+2\sqrt6.
$$

The full kernel is minimal of dimension five everywhere except
`(a,b)=(2sqrt(6)−3,12−4sqrt(6))`, where its linear dimension is four. An explicit compatible complete four-state CTMC exists there, so a spare hidden state supplies an unbounded five-state family. The singular exit-coordinate line `2a+b=6` is otherwise fully minimal: chart failure is not a model-order reduction. [E039](../evidence/RECORDS.md#e039).

The following regions have **unbounded entropy within five states**:

| Parameter region | Exact mechanism |
| --- | --- |
| `s<alpha` | A three-coordinate perturbation opens a complete generator. |
| `s=alpha`, every positive a,b | Redistribute the repeated dominant residue, then construct a connected hidden pair with identical external neighborhoods. |
| `s<=beta`, `a>35sqrt(6)/88`, `b>sqrt(6)/4` | Reassign one positive spectral residue to a singleton and realize the remaining two modes in an explicit positive cone. |
| `s>=beta`, `a/b>11(s−11)^2/1120` or `b/a>14(s−7)^2/55` | Exact necessary and sufficient inequalities for strict first-order opening of every missing rate. |

The last two rows together cover **the entire fast-coincidence line `s=beta`**, including the single ratio where strict first-order opening fails. These are sufficient global entropy results; their complement is not classified. [Construction proof](../analysis/theta-family-construction-audit.md), [E041](../evidence/RECORDS.md#e041).

At every minimal point on the slow line, the dominant hidden-response residue has rank two. An irreducible hidden block would expose a rank-one Perron residue. Hence **every compatible hidden graph is disconnected**, while entropy remains unbounded by the second row. The proof preserves the full shared matrix kernel and uses no minimality assumption for its construction. [Slow-line proof](../analysis/positive-realization-obstructions.md), [E039–E041](../evidence/RECORDS.md#e039).

Five exact checks over the rational field extended by sqrt(6) verify generator signs, reciprocal support, stationarity, ranks and kernel derivatives 0–9. They include both repeated-pole lines, the nonminimal exception and a slow-line point outside the direct coordinate thresholds. The resulting identities certify equality at all times. [Saved exact results](theta-residue-checks.json), [E043](../evidence/RECORDS.md#e043).

For `s>beta`, every compatible model with a disconnected hidden graph is the original theta generator up to hidden labels. The signed fast residue excludes every other spectral assignment. A distinct model must therefore have a connected hidden graph. Any hidden triangle gives unbounded entropy by the embedded-pair theorem; only hidden paths could support a bounded distinct component. This narrows the gap without establishing that any such component exists. [E042](../evidence/RECORDS.md#e042).

## Local isolation and unbounded entropy coexist

Observe only x↔y in the five-state generator, ordered (x,y,h,k,l),

$$
Q=\begin{pmatrix}
-11&1&2&0&8\\
2&-20&0&7&11\\
3&0&-7&4&0\\
0&6&5&-11&0\\
3&3&0&0&-6
\end{pmatrix}.
$$

The unobserved routes are x-h-k-y and x-l-y. This source survives more than a pairwise test: it is **isolated among all nearby compatible five-state generators, including topology changes**.

An exact positive-dual certificate proves local isolation in generator space. Nevertheless, an explicit rational hidden similarity produces a distant complete generator Q* with the same full kernel; its smallest off-diagonal rate is 139/500. The matrices, stationary law and proof are retained in the [theta audit](../analysis/theta-global-audit.md).

| Compatible realization | Entropy rate |
| --- | --- |
| Isolated sparse Q | Approximately 0.0428244846 |
| Distant complete Q* | Approximately 0.4376183787 |
| Exact family issuing from Q* | Unbounded above |

An explicit pair similarity from Q* reaches a one-way boundary with positive opposing stationary flux. All rates stay bounded above and all stationary probabilities retain positive limits, while entropy diverges logarithmically. The exact boundary and coefficient are recorded in [E035](../evidence/RECORDS.md#e035).

Every member remains minimal of dimension five and has the same complete observed kernels. The source is an isolated component, while Q* belongs to a distinct positive family. The compatible **generator set is disconnected**, even modulo hidden relabeling. No disconnectedness claim is made for the entropy image itself. [Exact proof and coordinates](../analysis/theta-global-audit.md), [E035](../evidence/RECORDS.md#e035).

The witness was discovered by a bounded numerical search with thirteen starts, then replaced by an exact rational certificate. Only two starts found the distant positive component; local successful termination often returned the isolated model. The mathematical conclusion uses exact signs, stationary equations, rank and kernel identities, not optimizer status. [E036](../evidence/RECORDS.md#e036).

## What is now classified

| Admissible class and condition | Proved outcome |
| --- | --- |
| At most three states; one resolved observed pair | Every rate is identified. [E017](../evidence/RECORDS.md#e017) |
| Exactly four states; one resolved observed pair; fixed or unknown bidirected topology; no minimality assumption | Entropy is a singleton or unbounded. Complete unknown-topology uniqueness test uses derivatives through order three. [E023–E031](../evidence/RECORDS.md#e023) |
| Five-state representative with one resolved observed pair, no hidden-hidden edges and three distinct hidden escapes; competitors under a five-state cap | Unique precisely for incidence {x}, {y}, {x,y} with the shared state faster than both exclusive states; otherwise unbounded. [E033](../evidence/RECORDS.md#e033) |
| Any minimal dimension with a suitable pair of fully hidden states having identical or nested external neighborhoods | Explicit pair similarities prove unboundedness under the stated support/rate conditions. [E032](../evidence/RECORDS.md#e032) |
| Cap N≥3; one resolved observed pair; the first nonzero derivative of Kxy is order N−1 | The cap forces the killed graph to be a path through all N states; all rates are globally identified. [E034](../evidence/RECORDS.md#e034) |
| Unrestricted finite cardinality, fixed observed incidence | Zero visible row deficits imply full generator uniqueness; any positive deficit implies unbounded entropy. [E028](../evidence/RECORDS.md#e028) |

For unknown topology at **exactly four states with only x↔y observed**, the two global uniqueness cases are: opposite singleton hidden neighbors at x and y; or an unjoined hidden pair with one shared state, one endpoint-specific state, and the shared state faster. Fixed topology permits additional entropy-unique cases, including trees and distinct-escape full diamonds. [Four-state observable criterion](../analysis/observable-four-state-criterion.md), [nonminimal extension](../analysis/nonminimal-four-state-audit.md).

The new diagonal-hidden five-state classification excludes arbitrary three-coordinate mixing in its unique case. A hidden component touching both visible endpoints must expose a positive dominant-pole residue. The observed cross response contains only the fastest shared pole, so no larger bridging component can contain either slower exclusive mode. This forces three singleton hidden components and permits exact reconstruction. A checked unique example has entropy 2 log(2)/37; a nearby unbounded example has divergence coefficient 8/93. [Sparse audit](../analysis/five-state-sparse-audit.md).

The pair criterion checks neighborhoods against **all other states**, including hidden states. Matching visible incidence alone is insufficient. Incomparable neighborhoods can obstruct every two-coordinate change while a three-coordinate change remains possible, as explicitly checked on the same two-path topology. Thus pair tests are useful exclusions, not a complete classifier. [Pair audit](../analysis/hidden-pair-boundary-audit.md).

The cap-dependent path result has a direct observable proof: the first nonzero Kxy derivative equals the shortest unobserved path length. Length N−1 exhausts a cap of N states; every additional bidirected edge would create a shortcut. Endpoint resolvent recursion then identifies the diagonals and opposing-rate products, and row sums split those products into individual rates. This uses established inverse-Jacobi machinery with an additional cap argument. [Path proof](../analysis/path-cap-uniqueness-audit.md).

## Why the state budget remains essential

If a compatible realization contains a fully hidden state, splitting that state into two clones preserves all marked kernels and makes entropy unbounded using only one additional state. This enlargement is nonminimal. Under a cap Nmax, any compatible hidden-state model using at most Nmax−1 states therefore already proves unboundedness within the cap.

Conversely, the observed rates and first derivatives determine the full visible block QVV. If its deficits dv=−Σw∈V Qvw all vanish, irreducibility excludes any additional hidden states. This supplies the unrestricted finite-cardinality dichotomy above. [State-splitting proof](../analysis/state-splitting-audit.md).

A five-state model with a fully hidden state therefore makes the class N≤6 unbounded, while a kernel requiring six states can remain unique under that cap, as the path theorem demonstrates. Minimum positive CTMC realization order must not be equated with minimum linear realization dimension in general.

## Validation, rejected candidate and limitations

The [analysis index](../analysis/README.md) links the exact identities, stationary laws, rank checks, boundary limits and numerical controls. Maintenance review replayed all six deterministic scripts and both seeded probes. It fixed a validator that accepted disconnected chains with positive stationary laws, and confirmed that all scientific results remained unchanged. [E044](../evidence/RECORDS.md#e044).

A proposed finite ambiguity obtained by reallocating hidden-response residues between two paths was rejected as an entropy counterexample: both hidden paths have the same forward/reverse product ratio, so entropy reduces to an observable current times a fixed affinity and is identical in the proposed alternatives. This does not exclude other compatible models carrying hidden circulation. [E038](../evidence/RECORDS.md#e038).

The corrected computational provenance records an initial inappropriate symmetric-eigenvalue diagnostic, unsuccessful optimizer starts, and bound-clipping warnings. At theta(100,100), no complete witness was found; the best returned margin was zero. This is not an infeasibility result. A proposed local-opening extension also fails: every source in `alpha<s<=7` is locally isolated, including points outside the constructive residue region. Exact certificates are separated from discovery diagnostics. No graph enumeration or large inference framework was built. [E036](../evidence/RECORDS.md#e036), [E042](../evidence/RECORDS.md#e042), [D009](../evidence/RECORDS.md#d009).

The results do not establish entropy minima for every unbounded fiber, finite-sample stability, unknown mark incidence, blurred observations, or channel-resolved dissipation. Bounded rate closure alone is insufficient, and a common positive lower rate cutoff would define a different problem.

## Remaining question and single next action

The precise unresolved question remains whether a minimal five-state kernel under a five-state cap, with unknown bidirected topology, can have a bounded non-singleton entropy range. The new counterexample shows why answering it requires a global component analysis.

**The single next action is to decide exact connected-hidden feasibility for theta(100,100).** Its kernel is minimal, its source is exactly locally isolated, and every disconnected-hidden alternative is globally excluded. The [fast-case audit](../analysis/theta-fast-case-audit.md) supplies rational global exit-triangle coordinates, fixed entrance points and the explicit inward vector field. Reciprocal support and connectivity must also hold.

A global exclusion of connected hidden graphs would prove generator uniqueness. A hidden-triangle witness would prove unboundedness. A hidden-path witness would require full boundary and component analysis before classifying entropy; a bounded-nonunique claim must exhibit distinct entropy values and control the entire fiber. More random starts or another local test would not provide that proof.

The main correctness risk is now explicit: local isolation or exclusion of complete representatives can miss divergent alternatives. The main novelty risk is subsumption by prior positive-realization and aggregate-equivalence theory, especially the inaccessible strict-realization hypotheses. The inspected literature constrains the candidate contribution without resolving that risk.

The accessible local, residue and Perron arguments do not decide the remaining connected-support feasibility. The full five/six-state program remains unresolved. [STATE.md](../STATE.md) and [D009](../evidence/RECORDS.md#d009) preserve the research resumption point; [D010](../evidence/RECORDS.md#d010) records the subsequent maintenance review.
