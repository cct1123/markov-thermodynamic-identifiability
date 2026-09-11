# Thermodynamic identifiability: exact fibers and finite-precision instability

**Research synthesis, 2026-09-11 UTC. A minimal five-state kernel can have a bounded, non-singleton entropy-production fiber under a five-state cap and unknown bidirected topology.** At an exactly specified balanced-theta parameter, the full compatible set contains exactly two generators up to hidden labels, and their entropy rates are rigorously different. This resolves the previously open existence question in this workspace; general five-state classification and publication novelty remain unestablished. [Endpoint proof and certificate](../analysis/theta-balanced-boundary.md), [E051](../evidence/RECORDS.md#e051).

The parameter is the unique positive root **z_*≈10.5571496686650** of **352z⁴−3168z³−4644z²−11340z−7623=0**. Its two entropy rates are approximately **0.062946400237** and **0.065579685967**, with disjoint exact rational enclosures. For every z>z_*, the balanced source is globally unique. The new invariant-triangle envelope exhausts all connected hidden graphs; existing disconnected-hidden rigidity covers the rest. The root and endpoint witness were derived independently through hidden-path algebra. The earlier bound z≥40 remains valid but is superseded on this ray. [Cone proof](../analysis/balanced-cone-bound.md).

The whole balanced entropy ray is now classified: **unbounded for 0<z<z_***, **two finite values at z=z_***, and **a singleton for z>z_***. Below the fold, a strict triangle construction overlaps the prior unbounded region and closes the remaining interval. [E052](../evidence/RECORDS.md#e052).

The initial conjecture that the first-order opening threshold was globally sharp was explicitly falsified by an exact rational complete realization. Failed searches do not enter the exclusion proof. The human [research brief](../PROJECT.md) is preserved; this is a working synthesis, not a paper draft or a formally verified theorem.

**Exact finite entropy ceilings need not survive any positive observational tolerance.** At every source with two fully hidden states, unknown competitor topology and no reverse-rate floor, arbitrarily close joint waiting-time laws admit unbounded entropy while keeping the state count, observed rates and generator trace fixed. All microscopic rates remain bounded. A stationary finite-record consequence is that a uniformly valid upper confidence limit must be infinite with probability at least its nominal coverage, even at an exactly identifiable source. The conventional proof and explicit four-state witness were independently checked. [E055](../evidence/RECORDS.md#e055), [E056](../evidence/RECORDS.md#e056).

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

The [formulation](../analysis/formulation.md) defines the observation process and stationary frequencies precisely. Resolved marks reset the state, making the full kernel sufficient for the observed event process. Equality of Markov parameters through order n+n′−1 certifies all-time equality for a candidate pair of dimensions n,n′. The exact classification and the separate finite-precision results below answer different questions. [E016](../evidence/RECORDS.md#e016).

## Frontier and prior-art constraints

| Category | Inspected evidence | Implication |
| --- | --- | --- |
| Already known | Resolved-transition kernels, absorbing representations, boundary-rate recovery, affinity inference and compatible-model entropy minimization | These are established infrastructure. [E001–E006](../evidence/RECORDS.md#e001), [E014](../evidence/RECORDS.md#e014) |
| Known under restrictions | Exact recovery on prescribed cycle structures; aggregate equivalence and reconstruction under observation, rank and topology restrictions | Retain the theorem's original model class. [E007](../evidence/RECORDS.md#e007), [E009](../evidence/RECORDS.md#e009), [E022](../evidence/RECORDS.md#e022) |
| What bounds do not determine | Lower bounds need not determine upper bounds or uniqueness; a known upper bound requires microscopic rate-ratio information absent under partial observation | Fixed trace and bounded rates alone do not bound entropy. [E025](../evidence/RECORDS.md#e025), [E037](../evidence/RECORDS.md#e037) |
| Known non-identifiability | Exact hidden similarities, equilibrium ambiguity, one-way boundaries, finite Coxian alternatives and numerical growing entropy over equivalence classes | Neither ambiguity nor local/global distinctions in general realization theory are new. [E008](../evidence/RECORDS.md#e008), [E010](../evidence/RECORDS.md#e010), [E025](../evidence/RECORDS.md#e025), [E037](../evidence/RECORDS.md#e037) |
| Established mathematical machinery | Positive matrix realizations and invariant polyhedral cones | A cone with extra rays can require extra states; strict input/output factors and the fixed order must be checked. [E040](../evidence/RECORDS.md#e040) |
| Established factorization geometry | Rank-three nested triangles, disconnected factorization spaces and infinitesimal/local rigidity | Static factorization does not impose dynamical invariance. [E045](../evidence/RECORDS.md#e045), [E046](../evidence/RECORDS.md#e046) |
| Unresolved here | Full entropy images for general minimal five-state kernels and global positive-realization components | The checked examples and subclasses do not settle these questions. [D007](../evidence/RECORDS.md#d007) |
| Candidate contributions | Complete four-state classification; five-state coexistence of isolation and unbounded alternatives; global uniqueness regions; an exact two-point entropy fiber at the sharp balanced-theta boundary | Publication novelty remains conditional on theorem-level comparison, including finite positive-realization alternatives. [E030](../evidence/RECORDS.md#e030), [E035](../evidence/RECORDS.md#e035), [E048](../evidence/RECORDS.md#e048), [E051](../evidence/RECORDS.md#e051) |

[Ehrich (2021)](https://arxiv.org/html/2105.08803v2), section 4, exactly parameterizes a four-state discrete-time aggregate-equivalence class and reports growing sampled entropy with a near-one-way mechanism. [Wagner–Timmer (2000)](https://doi.org/10.1016/S0006-3495(00)76529-5) establishes exact equilibrium ambiguity; [Siekmann (2026)](https://doi.org/10.1007/s11538-025-01558-3), Eq. (62), explicitly constructs equivalent one-way CTMC boundaries. These are strong antecedents, with different observation assumptions.

An earlier close-source check found finite isolated alternatives within Coxian representations: [Rizk–Burke–Walsh (2019)](https://arxiv.org/pdf/1901.03849v2), Theorem 2 and Algorithm 1. Their one-way transient form and single entrance do not exhaust our bidirected stationary model class. The marked-absorption extension and its restrictions are recorded in [E037](../evidence/RECORDS.md#e037). A finite list of generators also need not have different entropy values.

[Nishiyama–Hasegawa (2023)](https://arxiv.org/pdf/2306.15251v2), Eq. (8), gives an entropy upper bound using dynamical activity and the maximal microscopic forward/reverse rate ratio. A fixed minimal orbit bounds activity through its trace, but does not supply a uniform rate-ratio bound.

Closed minimal orbits and endpoint inverse-Jacobi reconstruction are established theory. Their CTMC specializations are attributed in [E025](../evidence/RECORDS.md#e025) and [E034](../evidence/RECORDS.md#e034). The [earlier five-state frontier memo](../evidence/five-state-frontier-followup.md) records exact locators, bounded citation tracing and the focused disconnected-fiber search. No matching coexistence theorem was located; that does not certify novelty. Larget's full canonical theorem, some original PH canonical results and the original Xiang reconstruction proof remain access gaps.

[Van den Hof (1997)](https://ir.cwi.nl/pub/127/0127D.pdf), Theorems 3.1 and 4.2, supplies continuous-time invariant-cone existence and minimality conditions. For the minimal theta fiber, a common trace-based shift reduces complete CTMC feasibility exactly to a strict order-three discrete-time matrix realization; normalization follows automatically. The primary theorem does not guarantee the required three-ray cone. Förster–Nagy's strict-realization theorem is a close lead, but its full dimension and input/output hypotheses remain an access gap. [Primary-source assessment](../evidence/positive-realization-frontier.md), [E040](../evidence/RECORDS.md#e040).

[Krone–Kubjas](https://arxiv.org/pdf/1902.02868v3), Propositions 4.2 and 5.3, gives an infinitesimal-to-local rigidity implication and a boundary criterion quantified over every rank-size factorization. [Mond–Smith–van Straten](https://doi.org/10.1098/rspa.2003.1150), Theorems 2.4 and 4.9, supplies nested-simplex geometry and disconnected rank-three factorization spaces. These results constrain novelty, but neither imposes the operator invariance used below. The [focused frontier memo](../evidence/three-state-cone-frontier.md) records full-text locators and further abstract-only realization leads. [E045](../evidence/RECORDS.md#e045).

The renewed theorem-level comparison narrows the novelty claim further: finite minimal positive-realization fibers have a static-factorization precedent and an elementary continuous-time lift. The possible contribution is the complete **physical entropy** fiber under the specific bidirected, resolved-edge and state-cap restrictions. A canonical representative is not a count of that fiber. The general statistical impossibility argument also has established antecedents. Primary-source locators, the challenged full-space versus boundary-space interpretation, and remaining access gaps are preserved in [E054](../evidence/RECORDS.md#e054) and the [positioning memo](../evidence/two-point-entropy-positioning.md). No absence of located prior art is treated as novelty evidence.

## The finite endpoint and sharp balanced boundary

The source family is

$$
Q(z)=\begin{pmatrix}
-11&1&2&0&8\\2&-20&0&7&11\\3&0&-7&4&0\\
0&6&5&-11&0\\z&z&0&0&-2z
\end{pmatrix}.
$$

The model class and data are exactly those stated above. Let z_* be the positive quartic root. At this parameter the source's disconnected hidden graph and one alternative hidden path are the **only two** compatible models, up to hidden labels. Exact field arithmetic constructs the second model, verifies its reciprocal support, stationarity and marked derivatives of orders 0–9, and therefore certifies all-time observational equivalence. Its three hidden states form a path whose center sees x, one endpoint sees y, and the other sees both. Both full generators are irreducible and the kernel's minimum linear dimension is five. [Construction](../analysis/theta-balanced-boundary.md), [exact output](balanced-fold-checks.json).

The global bound is stronger than a search or local-isolation result. Every connected hidden realization induces an invariant triangle inside a fixed output wedge. Optimizing its necessary containment inequalities gives f₀+f₁t+f₂t²≥0 for some t>0. The discriminant is a negative positive-factor multiple of the quartic. It is negative for z>z_*, excluding all connected supports. At z_*, the quadratic touches zero at a single t and all envelope inequalities must be equality. This fixes the whole triangle, its reciprocal zeros and, after row normalization, a unique connected generator. Disconnected-hidden rigidity then gives the exact two-model fiber. A separate physical path elimination produces the same quartic. [Global argument and equality classification](../analysis/balanced-cone-bound.md), [E051](../evidence/RECORDS.md#e051).

The entropy distinction is certified with rational algebraic-root enclosures and a logarithm series with an explicit remainder bound:

| Endpoint realization | Certified enclosing interval for entropy rate |
| --- | --- |
| Source | [0.062946400236, 0.062946400237] |
| Connected hidden path | [0.065579685966, 0.065579685967] |

Their gap lies in [0.002633285729, 0.002633285730]. Arbitrary-precision evaluations at 60 and 100 digits and independent numerical stationary/exponential checks agree, but the sign claim uses the rational bounds. Thus generator nonuniqueness has not been confused with entropy nonuniqueness, and boundedness follows from exhausting the entire fiber. The fifth-state cap is essential; a sixth state restores unbounded entropy through splitting. No common positive lower rate cutoff is imposed.

The first-order threshold z_c≈10.54524979109513 was a falsified candidate for this global boundary. An exact rational similarity gives complete realizations for all 10.545≤z≤10.5455; a second-order opening explains the crossing. A 26-run bounded optimizer probe suggested the limiting path but supplies no exclusion evidence. [Witness and failed attempts](../analysis/balanced-boundary-witness.md), [E050](../evidence/RECORDS.md#e050).

For every 10.5≤z<z_*, the quadratic envelope has strictly positive maximum. Exact rational interval bounds certify all other strict geometric margins uniformly, and three sufficiently small vertex perturbations open every input, output and hidden rate. Positive row normalization then gives a complete admissible generator with exactly the same transfer; the existing hidden-pair theorem supplies a data-preserving family with divergent entropy. This is a continuum existence argument, not a parameter grid. Together with the prior constructions it proves unbounded entropy for every 0<z<z_*. It does not assert connected hidden feasibility on the exceptional slow-pole line. [Sufficiency proof](../analysis/balanced-cone-bound.md#6-sufficiency-below-the-fold-complete-compatible-generators), [E052](../evidence/RECORDS.md#e052).

## Earlier global uniqueness region for fast theta kernels

The family Q(a,b) is the displayed five-state generator below with final row `(a,b,0,0,−a−b)`. Observe only x↔y and allow unknown bidirected topology with at most five states. For `s=a+b>beta`, the three hidden modes have decay rates `alpha=9−2sqrt(6)`, `beta=9+2sqrt(6)`, and s. Their nonzero residues make the full kernel minimal of dimension five.

Any compatible connected hidden block would yield a finite invariant triangle after normalizing by its strictly positive Perron coordinate. The triangle must contain two specified input points and the origin, lie inside a fixed output wedge, and remain invariant under the contracting flow `(u,v) -> (exp(−t)u,exp(−kappa*t)v)`. These requirements force two vertices above the horizontal axis and one below. Lower-edge invariance and input containment give incompatible height bounds at theta(100,100), regardless of the lower vertex's horizontal sign. This excludes both hidden paths and triangles. Disconnected hidden blocks were already proved unique. [Proof, sections 2–8](../analysis/theta-fast-spectral-audit.md).

Thus **the complete generator and entropy are unique**, up to hidden labels. At theta(100,100), the entropy rate is approximately **0.0755509024393**, with k_B=1 in the stated rate units. The same argument proves every balanced theta(z,z), z≥40, unique and gives an explicit open two-parameter sufficient region in equation (1) of the proof. Allowing a sixth state reverses the entropy conclusion: hidden-state splitting supplies an unbounded family with the same observations. [E028](../evidence/RECORDS.md#e028), [E048](../evidence/RECORDS.md#e048).

The focused exact checker verifies modal identities, source ranks, wedge constants, strict margins and polynomial bounds for the balanced tail z≥40. A separate incidence and polynomial calculation rules out every potentially bounded hidden-path alternative at theta(100,100); it independently supports the result while proving a weaker statement. Neither argument relies on the earlier failed optimizer search. [Exact output](check_theta_fast_spectral.json), [path certificate](../analysis/theta-fast-hidden-paths.md), [E047](../evidence/RECORDS.md#e047).

A consequential rejected shortcut is also exact: **every finite block Hankel truncation of theta(100,100)'s uniformized hidden response admits strictly positive factors of inner dimension three**. The full observed kernel has minimal dimension five. A small signed similarity opens the hidden input/output zeros while creating a negative hidden transition rate, so static factorization positivity cannot replace the dynamics constraints. This does not exclude finite derivative methods that explicitly retain the generator. [Construction and reproduced calculation](../evidence/three-state-cone-frontier.md), [E046](../evidence/RECORDS.md#e046).

## Unbounded parameter regions and exceptional lines

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

The last two rows together cover **the entire fast-coincidence line `s=beta`**, including the single ratio where strict first-order opening fails. These are sufficient global entropy results; the full two-parameter complement remains unclassified, while its balanced slice is classified above. [Construction proof](../analysis/theta-family-construction-audit.md), [E041](../evidence/RECORDS.md#e041).

At every minimal point on the slow line, the dominant hidden-response residue has rank two. An irreducible hidden block would expose a rank-one Perron residue. Hence **every compatible hidden graph is disconnected**, while entropy remains unbounded by the second row. The proof preserves the full shared matrix kernel and uses no minimality assumption for its construction. [Slow-line proof](../analysis/positive-realization-obstructions.md), [E039–E041](../evidence/RECORDS.md#e039).

Five exact checks over the rational field extended by sqrt(6) verify generator signs, reciprocal support, stationarity, ranks and kernel derivatives 0–9. They include both repeated-pole lines, the nonminimal exception and a slow-line point outside the direct coordinate thresholds. The resulting identities certify equality at all times. [Saved exact results](theta-residue-checks.json), [E043](../evidence/RECORDS.md#e043).

For `s>beta`, every compatible model with a disconnected hidden graph is the original theta generator up to hidden labels. The signed fast residue excludes every other spectral assignment. A distinct model must therefore have a connected hidden graph. Any hidden triangle gives unbounded entropy by the embedded-pair theorem; only hidden paths could support a bounded distinct component. E051 now realizes and globally exhausts precisely such a path alternative at the balanced quartic endpoint. [E042](../evidence/RECORDS.md#e042), [E051](../evidence/RECORDS.md#e051).

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

## Finite-precision failure and its smallest counterexample

Measure observational error by the maximum row total variation between the complete joint next-mark/time laws. For a source Q with two fully hidden states, the [neighborhood theorem](../analysis/entropy-neighborhood-audit.md) constructs, for every tolerance and every finite target entropy, a complete bidirected model at that distance and above that target. State count, observed rates and trace remain exactly fixed; every microscopic rate is at most `-tr Q`. A trace-preserving completion makes a hidden pair available for the established exact boundary construction. Integrated semigroup and independent coupling arguments prove the observation bound. This applies to the exact five-state finite fiber above without contradicting its exact classification. [E055](../evidence/RECORDS.md#e055).

The failure already occurs at the smallest possible fixed minimal dimension, three. Observe only the unit-rate pair x↔y and use

\[
Q_{e,k}=\begin{pmatrix}
-1-e&1&e\\1&-2+k&1-k\\k&1-e&-1+e-k
\end{pmatrix},\qquad 0<k<e<\tfrac12.
\]

Every rate is at most one, the trace is exactly −4, and every model has minimal order three. The source `Q0=Q(0,0)` is the equilibrium tree x−y−h and is globally unique under cap three. Let `Z=3+e+2k-e²-ek-k²`. Direct stationary-cycle algebra gives

\[
\sigma(Q_{e,k})=
\frac{(e-k)(1-e-k)}{Z}
\log\frac{e(1-e)}{k(1-k)}.
\]

For `k=exp(-1/e²)`, this grows as `1/(3e)` while `Q(e,k)` converges entrywise to Q0. Joint-kernel row TV is below `4e`; stationary observed-window TV is at most `11e/18+2eH` on every fixed finite horizon H. For each fixed small e, taking k to zero gives arbitrarily high entropy within these same bounds. Every exact cap-three fiber along this construction is a singleton. Thus the inverse generator can be continuous while its entropy is not: an absent edge opens with forward and reverse rates vanishing at vastly different speeds. This mechanism also affects fully observed finite microscopic records, so it is not a phenomenon unique to hidden-state inference. [Exact proof](../analysis/three-state-fixed-trace-audit.md), [independent executable checks](three-state-precision-checks.json), [E057](../evidence/RECORDS.md#e057).

With a common finite rate cap and at most three states, a strictly positive triangle is different. Compactness, continuity of matrix exponentials and the exact three-state derivative reconstruction force any observationally convergent sequence to converge to its source generator. All six source rates are positive, so entropy is continuous there. At a tree, arbitrary nearby entropy remains unbounded. With cap two entropy is always zero; with cap three, even two-state equilibrium data have an unbounded observational neighborhood when trace is not separately fixed. These statements concern local population-law stability. They do not give a uniform conditioning constant over all triangles. [One-hidden-state audit](../analysis/one-hidden-robustness-audit.md), [two-state source audit](../analysis/three-state-precision-audit.md), [E058](../evidence/RECORDS.md#e058).

For stationary sampling on `[0,H]`, let U be any upper confidence limit with coverage at least `1-alpha` for **every** admissible model in the stated class. A sequence of divergent entropies whose finite-record laws converge in TV forces `P_Q0(U=+infinity)>=1-alpha`. This holds at the three-state tree even restricting to trace −4 and rates at most one. The general hidden-pair theorem gives the same conclusion at every source satisfying its premises. At locally stable positive triangles, global coverage over the entire cap-three class still forces an infinite output with positive probability, by domination of the tree's alternating-record law. Local entropy continuity and globally honest finite-sample inference are different requirements. [Confidence proof](../analysis/finite-precision-instability.md#consequence-for-uniform-finite-sample-upper-confidence-limits), [support-transfer audit](../analysis/one-hidden-robustness-audit.md), [E056](../evidence/RECORDS.md#e056), [E058](../evidence/RECORDS.md#e058).

These results do not invalidate lower entropy estimators or pointwise asymptotic methods in restricted classes. Known sparse topology or a uniform positive reverse-rate floor changes the problem. In particular, if every present rate lies in `[m,M]`, `m>0`, stationary cancellation bounds entropy by the stationary jump activity times `log(M/m)`. A rate upper bound alone supplies no such floor. Population TV neighborhoods are not empirical-TV confidence balls for continuous waiting times.

## What is now classified

| Admissible class and condition | Proved outcome |
| --- | --- |
| At most three states; one resolved observed pair | Every rate is identified. [E017](../evidence/RECORDS.md#e017) |
| Exactly four states; one resolved observed pair; fixed or unknown bidirected topology; no minimality assumption | Entropy is a singleton or unbounded. Complete unknown-topology uniqueness test uses derivatives through order three. [E023–E031](../evidence/RECORDS.md#e023) |
| Balanced theta for all z>0; exact joint kernels; unknown bidirected topology under a five-state cap | Unbounded below z_*; exactly two generators and two different finite entropy values at z_*; generator unique above z_*. [E051](../evidence/RECORDS.md#e051), [E052](../evidence/RECORDS.md#e052) |
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

The [analysis index](../analysis/README.md) links the exact identities, stationary laws, rank checks, boundary limits and numerical controls. Earlier maintenance replayed six deterministic scripts and both seeded probes, fixing a validator that accepted disconnected chains with positive stationary laws while preserving the scientific results. The earlier global-uniqueness run also checked the spectral certificate, embedded path certificate and finite-Hankel algebra. [E044](../evidence/RECORDS.md#e044), [E046–E048](../evidence/RECORDS.md#e046).

The present scoped continuation independently checked the rational threshold-crossing witness, generic cone envelope and discriminant, interval sufficiency margins, and exact algebraic endpoint/entropy certificate. The global proof and all perturbation/equality cases received independent review. Historical scientific scripts and JSON outputs were preserved; failed new optimizer starts and interrupted symbolic attempts remain recorded. [E050](../evidence/RECORDS.md#e050), [E051](../evidence/RECORDS.md#e051), [E052](../evidence/RECORDS.md#e052).

A proposed finite ambiguity obtained by reallocating hidden-response residues between two paths was rejected as an entropy counterexample: both hidden paths have the same forward/reverse product ratio, so entropy reduces to an observable current times a fixed affinity and is identical in the proposed alternatives. This does not exclude other compatible models carrying hidden circulation. [E038](../evidence/RECORDS.md#e038).

The corrected computational provenance retains unsuccessful optimizer starts, an inappropriate initial eigenvalue diagnostic and bound-clipping warnings. The old theta(100,100) search was inconclusive; the new global proof supplies the exclusion. A proposed local-opening extension still fails: every source in `alpha<s<=7` is locally isolated, including points with distant alternatives. No broad graph enumeration or large inference framework was built. [E036](../evidence/RECORDS.md#e036), [E042](../evidence/RECORDS.md#e042), [E048](../evidence/RECORDS.md#e048).

The results do not establish entropy minima for every unbounded fiber, a complete stability theory under prescribed topologies, unknown mark incidence, blurred observations, or channel-resolved dissipation. The finite-precision impossibility results above use their explicitly stated observation, rate-domain and coverage assumptions. Bounded rate closure alone is insufficient, and a common positive lower rate cutoff defines a different problem.

The final maintenance review found no further flaw in the global proof. It clarified that the dimension-three Hankel result concerns the uniformized hidden response, replayed the new certificates and pruned disposable bytecode. Scientific outputs were unchanged. [E049](../evidence/RECORDS.md#e049).

## Scope completed and conditions for resumption

The saved balanced-boundary action is complete. The upper exclusion, physical endpoint, globally finite two-model fiber, differing entropy values and subcritical unbounded interval are proved within the explicit model class. The new result answers the bounded-nonunique **existence** question; it does not give a general decision procedure for every five-state kernel.

The renewed autonomous continuation completed a bounded primary-source comparison and the finite-precision results above. The smallest counterexample, its exact-trace strengthening, the general two-hidden-state theorem and the positive-triangle exception are conventionally proved and independently checked. Failed retrievals, algebra-checker issues and an incomplete code extraction remain recorded. No formal verification or publication novelty is claimed. [E054–E058](../evidence/RECORDS.md#e054).

The stopping reason is diminishing returns in the completed directions: more numerical examples cannot strengthen a dimension-minimal construction or replace the analytic classifications, and broad citation searches have not supplied a specifically matching physical theorem. The main remaining risk is novelty. The single best next action is to obtain Larget's original canonical-equivalence theorem via a new accessible route and compare its actual physical positivity, fixed-order and observation hypotheses against the exact two-point fiber. The [source audit](../evidence/finite-fiber-prior-art.md#outstanding-original-source-gap-larget) records precise preprint leads and existing failures; lack of access is not evidence of novelty.

General two-parameter theta classification and the full five/six-state exact-fiber program remain unresolved. A new concrete primary result, a proof objection or changed assumptions can justify reopening; the report does not mark those broader objectives solved. All assignments are complete and the repository is resumable through [STATE.md](../STATE.md) and [D020](../evidence/RECORDS.md#d020). No commit or push was performed in this continuation.
