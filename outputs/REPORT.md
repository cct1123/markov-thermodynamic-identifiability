# Publication-readiness audit: exact entropy fibers and stability

**Verdict 1: ready for narrowly scoped manuscript preparation.** The exact two-point entropy theorem survives independent whole-proof review, and the audit strengthens the stability results to a necessary-and-sufficient criterion for every fixed state count. The candidate contribution is this precise physical theorem combination. Finite positive-realization fibers, entropy singularities and general confidence-limit impossibility have clear precedents; originality is not certified by this review. [Decision D023](../evidence/RECORDS.md#d023), [paper structure](PAPER-STRUCTURE.md).

This is the final synthesis of the requested audit, dated 2026-09-11 UTC. The [human brief](../PROJECT.md) is preserved. The complete [mathematical specification](../analysis/publication-theorems.md) defines all classes, observation maps, equivalence relations, topologies and quantifiers. The [legacy inventory](../analysis/publication-legacy-audit.md) rigorously states the earlier supporting results and their boundaries.

## What has been proved

Use finite irreducible simple bidirected row CTMCs, one channel per ordered state pair, even states under time reversal, and fixed physical time units. Only the individual transitions x→y and y→x are observed, with known endpoints. Every present rate is finite and positive in both directions; competitor topology is unknown, with no positive rate floor. The observation is the complete **joint** next-mark/time kernel, including its amplitudes:

\[
\Psi_Q(t)=R e^{Tt}B,\qquad T=Q-E_{xy}-E_{yx},
\]

where T retains Q's diagonals, R resets to the known post-event endpoint, and B contains the two observed escape columns. Equal kernels define observational equivalence; only hidden permutations are identified as the same physical description. A prescribed state count, a state cap and a minimal-realization restriction are different classes.

For the stationary law pi, entropy is

\[
\sigma(Q)=\sum_{i<j:q_{ij}>0}(\pi_iq_{ij}-\pi_jq_{ji})
\log\frac{\pi_iq_{ij}}{\pi_jq_{ji}}.
\]

Natural logs and k_B=1 give inverse-time units. A paired absent edge contributes zero. Every admitted model has finite entropy; an unbounded fiber means arbitrarily large finite values. Interpreting this generator functional as all physical dissipation requires sufficiently resolved thermodynamic channels.

**Exact identifiability** concerns the entropy image of the entire exact kernel fiber. A **robust finite upper ceiling** means that some positive neighborhood of the observed law has a finite supremum of compatible entropy. The main data metric is maximum row TV of the two probability measures on waiting time × next mark; the positive results also specify weak row-law convergence. Stationary finite-window records form a separate experiment.

### The exact two-point result

In the class with at most five states, consider

\[
Q(z)=\begin{pmatrix}
-11&1&2&0&8\\2&-20&0&7&11\\3&0&-7&4&0\\
0&6&5&-11&0\\z&z&0&0&-2z
\end{pmatrix},\quad z>0.
\]

Let z_* be the unique positive root of

\[
352z^4-3168z^3-4644z^2-11340z-7623=0,
\qquad z_*\simeq10.5571496686650.
\]

| Parameter | Entire entropy fiber |
| --- | --- |
| 0<z<z_* | Unbounded above |
| z=z_* | Exactly two distinct finite values |
| z>z_* | Singleton; the entire generator is unique |

At z_* there are exactly two generators modulo hidden labels: the source and one connected-hidden path, defined by exact algebraic formulas in the [endpoint construction](../analysis/theta-balanced-boundary.md). Their certified entropy enclosures are **[0.062946400236, 0.062946400237]** and **[0.065579685966, 0.065579685967]**. Every balanced source has minimal linear order five. The earlier four-state theorem makes five the smallest cap allowing bounded thermodynamic nonuniqueness in this observation class. [E051–E052](../evidence/RECORDS.md#e051), [fresh audit E059](../evidence/RECORDS.md#e059).

The proof globally exhausts connected hidden supports through a Perron-normalized invariant triangle and its unique equality case; a separate residue argument exhausts disconnected supports. Independent physical-path elimination yields the same quartic. A new exact cone-to-path construction matches every generator coefficient. Feasibility and entropy separation have separate exact certificates. Thus this is neither a count of sampled models nor a count within one canonical topology.

A separate rate cap is unnecessary because similarity fixes trace. Exact derivatives 0–9 suffice under cap five. Full irreducibility follows from nonnegative generator constraints, exact minimal data and the cap. The cap can be replaced by requiring every competitor to be linearly minimal; allowing a sixth nonminimal state makes entropy unbounded by splitting. Reciprocal support and known resolved incidence remain substantive. Pole coincidences, coordinate-chart failures and the full subcritical covering were checked; z=0 is excluded.

### Three states: stable inverse, possibly unstable entropy

For every irreducible three-state source, the kernel Laplace matrices at **any three distinct positive arguments** determine all six physical rates. The inverse is locally rational with nonzero denominators, including at either hidden-leaf tree. It is locally Lipschitz in row TV and continuous under weak row-law convergence among candidates under cap three. Neither observed rates, trace nor an upper rate bound must be supplied in advance. [T2 and full formula](../analysis/publication-theorems.md#3-three-state-identifiability-and-cap-free-continuity), [E060](../evidence/RECORDS.md#e060).

This removes the prior rate-cap assumption from the saved joint-kernel continuity result. At a strictly positive triangle, stationary entropy is consequently locally Lipschitz. At a tree, the rates are still stably recoverable but entropy is unbounded nearby.

The simplest fixed-trace witness is

\[
Q(e,k)=\begin{pmatrix}-1-e&1&e\\1&-2+k&1-k\\k&1-e&-1+e-k\end{pmatrix},
\qquad0<k<e<1/2.
\]

Its source Q(0,0) is the reversible unit tree x-y-h. Every displayed kernel has minimal order three and a unique generator under cap three. All rates are at most one and trace is exactly -4. With Z=3+e+2k-e²-ek-k²,

\[
\sigma(Q(e,k))=\frac{(e-k)(1-e-k)}Z
\log\frac{e(1-e)}{k(1-k)}.
\]

Choosing k=exp(-1/e²) gives e sigma→1/3 while Q(e,k)→Q(0,0). Row TV is below 4e, and stationary observed-record TV on any fixed horizon H is at most 11e/18+2eH. At fixed small e, taking k to zero proves unboundedness inside a fixed positive neighborhood. Two states cannot show this because their stationary entropy is always zero. These are analytic limits and bounds, independently checked. [E057](../evidence/RECORDS.md#e057), [fresh stability audit](../analysis/publication-stability-audit.md).

### The broader exact stability criterion

For **exactly N states**, one known resolved pair and unknown bidirected topology:

| Source | Finite local entropy upper ceiling? |
| --- | --- |
| N=2 | Yes; entropy is zero |
| N=3, complete triangle | Yes; entropy is locally Lipschitz |
| N=3, tree | No |
| Every N>=4 source | No |

The same criterion holds with source observed rates and trace fixed, and for weak row-law topology. This is a general theorem for arbitrary fixed N. It is stronger than the explicit three-state example. [T6](../analysis/publication-theorems.md#5-sparse-boundaries-hidden-ambiguity-and-sharp-local-ceilings), [E061](../evidence/RECORDS.md#e061).

Two mechanisms explain it. At any noncomplete irreducible microscopic generator, opening a missing pair at rates e and exp(-1/e²), with compensation in an existing rate, yields divergent entropy while preserving trace and the source's maximum rate cap. This also works with full microscopic finite-record observation. At any source with two fully hidden states, including complete sources, fixed-trace completion followed by exact hidden-pair mixing makes every observational neighborhood entropy-unbounded. Those high-entropy generators need not approach the source entrywise. [E055](../evidence/RECORDS.md#e055), [T4–T5](../analysis/publication-theorems.md#5-sparse-boundaries-hidden-ambiguity-and-sharp-local-ceilings).

The scientific distinction is therefore precise: exact thermodynamic identifiability does not imply a stable upper ceiling, and the obstruction can arise either from the entropy functional or from hidden observational ambiguity. This does not introduce the general distinction between identifiability and stability as a new concept.

## Boundaries and targeted counterexamples

The audit actively challenged stronger statements and retained the failures:

- **An arbitrary extra rate cap changes the theorem.** Four states, trace -12 and all rates<=1 force every offdiagonal rate to be one; the class is a singleton despite two hidden states. The general construction's sufficient cap is the trace mass, not every tighter cap containing the source.
- **A compact limiting set is insufficient without support control.** The divergent three-state sequence converges to the singleton unit tree. The corrected sufficient criterion requires the approaching competitors' supports eventually equal the fixed support of the compact irreducible limit set.
- **A ratio bound needs activity control.** A three-cycle with clockwise rates 2c and reverse rates c has ratio two and entropy c log2. A uniform activity bound Amax together with ratio R gives sigma<=Amax log R; a trace or rate cap can bound activity.
- **Fixed support, spare states and incidence matter.** A prescribed tree has zero entropy; a spare hidden state permits exact-law splitting; blurred/unknown incidence changes the inverse map. Freezing all positive rates and trace can prevent chord opening.

The earlier first-order threshold was falsified by an exact rational witness; local isolation does not imply global uniqueness; and finite-Hankel positivity does not impose dynamical invariance. Those failed ideas and their replacements remain recorded. No failure to find a counterexample is used as proof.

The finite-window confidence result remains valid with its exact quantifiers: uniform modelwise coverage over a class containing a divergent-entropy sequence with converging stationary record laws forces an infinite upper bound with probability at least its coverage at the limiting source. It is an application of established statistical impossibility theory. It does not invalidate lower estimators, restricted priors or pointwise asymptotic methods. The new cap-free Laplace argument does **not** remove the rate cap in the separate positive fixed-window continuity proof. [T7–T8](../analysis/publication-theorems.md#6-statistical-consequence-and-sufficient-regularity-conditions).

## Novelty and significance assessment

The [realization audit](../evidence/publication-realization-novelty.md) and [thermodynamic audit](../evidence/publication-thermodynamics-novelty.md) give a closest-result comparison for every candidate theorem, with versions, exact locators, access limitations and backward/forward citation trails. The search covered hidden/aggregated CTMCs, PH and marked PH, MAP/BMAP, positive realization, observational equivalence, identified sets, inverse stability and relative-entropy singularities. [E062](../evidence/RECORDS.md#e062).

| Result | Closest known work | Precise remaining publication case |
| --- | --- | --- |
| Whole two-point entropy fiber | Finite factorization alternatives, invariant PH polytopes and positive-HMM equivalence | Exhaust all physical bidirected supports with the prescribed resets, certify exactly two entropy values, and prove the sharp transition. |
| Three-state divergence | Vanishing reverse-rate entropy and reverse-Pinsker failures | A minimal fixed-trace example with unique, stably recovered rates; useful supporting content, weak as a standalone originality claim. |
| Three-state inverse/continuity | Canonical MAP inversion and HMM inverse regularity | Recover the actual six physical rates, including leaves, from bounded transform tests; a supporting specialization. |
| All-N local-ceiling criterion | Hidden thermodynamic ambiguity and inverse-stability frontiers | Necessary-and-sufficient count/support classification under one resolved pair, even at fixed trace and observed rates. |
| Confidence and regularity corollaries | Gleser–Hwang-type results and rate-ratio entropy bounds | Physical applicability and sharp assumptions; the general mechanisms are credited. |

The full Vanluyten–Willems–De Moor journal paper and Horváth–Telek preprint closed earlier access gaps. The closest inspected results do not supply the project's physical whole-fiber count or its all-N ceiling criterion. That comparison supports manuscript preparation; it does not establish an exhaustive claim of novelty. Larget and other specifically listed originals remain access gaps after new routes, so an exceptional construction or theorem there could change attribution. A numerical absence or missing matching phrase is never the basis of the verdict.

A narrowly scoped theorem paper has a defensible contribution now; another unrelated theorem is unnecessary. The [paper structure](PAPER-STRUCTURE.md) lays out the central theorem sequence, four purposeful figures, proof appendices, reproducibility package and prior-work positioning. A regular article in the statistical-physics/stochastic-process scope of Physical Review E is a plausible initial fit; this is a scope judgment, not an acceptance prediction.

## Evidence status and resumable conclusion

The core results are **conventionally proved and independently checked, not formally verified**. Fresh verification includes coefficientwise exact cone/path agreement, four endpoint script replays with writes intercepted, exact rational inverse identities, an alternative exact trace reconstruction, and independent 160-digit direct-resolvent/stationary calculations. The root's new checker passed six inverse cases, three exact interpolation cases and twelve chord diagnostics; both independent embedded exact checks passed. Accepted historical outputs were preserved. Detailed coverage distinguishes full proof/implementation reads, saved evidence checks and fresh execution. [E059–E061](../evidence/RECORDS.md#e059), [new output](publication-audit-checks.json), [independent replays](publication-independent-replays.json).

The main remaining risk is precise originality and expert scrutiny of the long global endpoint exhaustion. Full off-balanced theta/general five-six-state exact classifications and cap-free stationary-window continuity remain open; none is silently claimed solved. The audit stops because its objective has been handled and further generic searches or numerical examples have low expected value.

**Single highest-value next action:** assemble the self-contained theorem-and-proof core for the exact balanced entropy fiber and all-N local-ceiling criterion, following [PAPER-STRUCTURE.md](PAPER-STRUCTURE.md), with the primary-work comparison attached. Preserve all exceptional cases and exact certificates. No polished introduction is needed first. [STATE.md](../STATE.md) records this handoff. No commit or push was performed.
