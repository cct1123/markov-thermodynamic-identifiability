# Compact physical rate priors and shrinking-tolerance upper bounds

Date: 2026-09-15. Status: conventionally proved below; no formal-verification or numerical-optimization claim. This is an agent-owned correctness addition. It does not depend on the five-state support-exhaustion theorem.

## Statement and topology

Fix a physical time unit, an integer state cap `nbar >= 2`, two named microscopic endpoints `x,y`, their observed resolved reverse pair, and constants `0 < m < M < infinity`. Let `K` consist of all row generators with `2 <= N <= nbar`, connected reciprocal support containing `xy`, and **each supported rate in the closed interval `[m,M]`**. Absent reciprocal pairs remain allowed. Observed incidence is fixed; the values `r,s` can vary in `[m,M]`. Fixing their numerical values or imposing additional **closed** constraints only restricts the compact class, provided the resulting class is nonempty.

For each dimension, use labeled states `(x,y,h_1,...,h_{N-2})`, ordinary matrix topology, and then the finite disjoint union over dimensions. Quotienting by the finite hidden-label permutation groups does not affect compactness, observations, entropy, or extrema. This disjoint-union convention does not identify a vanishingly occupied extra physical state with a lower-dimensional model.

Write `O(Q)=R exp(T_Q t) B_Q`, with `T_Q=Q-E_+-E_-` retaining the original diagonal. Let `d` be maximum row total variation of the two joint next-mark/time probability laws. For a **feasible exact datum** `D in O(K)` define closed-tolerance constraints and their upper value by

\[
 K_\eta(D)=\{Q\in K:d(O(Q),D)\le\eta\},\qquad
 U_D(\eta)=\max_{Q\in K_\eta(D)}\sigma(Q),\quad \eta\ge0.
\]

Then `K` is compact, `O` is continuous in row TV, and `sigma` is continuous. Every displayed maximum exists and is finite, and

\[
 U_D(\eta)\downarrow U_D(0)\quad\text{as }\eta\downarrow0.
\]

The same conclusion holds if `d` is a metric generating weak convergence of joint row probability laws, such as a bounded-Lipschitz metric for a fixed compatible time/mark metric. It also holds for any specified continuous finite-dimensional observation map, but its zero-tolerance fiber then means equality of those measurements, not automatically equality of all waiting laws.

## Compactness, including support and dimension changes

For fixed `N` there are finitely many connected undirected supports containing `xy`. For each such support `G`, the generator is the continuous image of `[m,M]^{2|G|}`: supported ordered rates are free coordinates, missing rates are zero, and diagonals are negative row sums. The image is compact and all its generators remain irreducible. A finite union over supports and then dimensions is compact.

Equivalently, in an entrywise-convergent fixed-dimensional sequence, each off-diagonal belongs to `{0} union [m,M]`. Once all entries are within less than `m/2` of their limits, the support has stabilized. A sequence can alternate supports, but it cannot converge while continuing to open or close an edge. Every sequence has a subsequence of constant dimension and support. The limiting support is the same connected graph, not a disconnected boundary graph.

This step would be false with `0 < q_ij <= M` and no common positive floor. Connected reciprocal models could then converge to a disconnected generator, or to the sparse entropy singularity already exhibited in the manuscript. Replacing the closed interval by an open rate box also removes the stated attainment argument.

## Explicit uniform stationary and killed-process bounds

Set

\[
 \nu=(\bar n-1)M,\quad a=m/\nu\in(0,1),\quad
 t_0=1/\nu,\quad b=e^{-1}a^{\bar n}/\bar n!>0.
\]

All total escape rates are at most `nu`. The normalized stationary law exists and is unique. For any supported edge `i -> j`, stationarity implies

\[
 \pi_j\nu\ge \pi_j(-q_{jj})\ge \pi_i q_{ij}\ge m\pi_i.
\]

Start at a state with stationary mass at least `1/N` and follow a simple path to `j`, of length at most `N-1`. Thus

\[
 \pi_j\ge\bar n^{-1}a^{\bar n-1}>0
\]

uniformly over the entire class. This is a direct elementary check that stationary mass cannot disappear within these priors; no matrix-tree theorem is needed.

To control waiting times, append an absorbing cemetery state and send each observed jump there. The transient block is exactly `T_Q`. Uniformize this augmented chain at the common rate `nu`. From every microscopic state there is a path to an observed jump and then the cemetery in at most `N <= nbar` steps, each nontrivial step having probability at least `a`. If the path encounters an observed jump sooner, killing has already succeeded. After absorption, remaining steps stay at the cemetery. Hence the chance of absorption within `nbar` uniformized steps is at least `a^nbar`. During time `t0`, the probability of exactly `nbar` Poisson events is `exp(-1)/nbar!`, giving

\[
 \Pr_i^Q\{\tau_{\rm mark}\le t_0\}\ge b,
 \qquad
 \sup_{Q\in K,i}\Pr_i^Q\{\tau_{\rm mark}>t\}
 \le(1-b)^{\lfloor t/t_0\rfloor}.
\]

The Markov property gives the second inequality by repeating the first bound in time blocks. In particular,

\[
 \sup_Q\|(-T_Q)^{-1}\|_\infty
 =\sup_{Q,i}\mathbb E_i^Q\tau_{\rm mark}
 \le h_*:=t_0/b<\infty.
\]

These deliberately loose constants are existence bounds, not practical observation-time or inverse-conditioning estimates. They are uniform across supports and dimensions, and prove transience without assuming a uniform spectral gap from pointwise transience alone.

## Observation and entropy continuity

On any fixed dimension/support component, `T_Q` and `B_Q` depend continuously on the rates. Matrix exponentials give uniform convergence of the joint density on a compact time interval when `Q_j -> Q`. The preceding common tail bound makes its omitted total probability uniformly small. Splitting the row-TV integral at a large finite time therefore proves `d(O(Q_j),O(Q)) -> 0`. Finite disjoint union gives continuity on `K`.

A second direct check is available. For any two members `Q,P` of the same dimension, positivity of the killed semigroups, Duhamel's identity, and `integral exp(T_P t) B_P 1 dt = 1` give

\[
 d(O(Q),O(P))
 \le\frac{h_*}{2}\left(
 \|T_Q-T_P\|_\infty+\|B_Q-B_P\|_\infty\right).
\]

Indeed expand `exp(T_Q t)B_Q-exp(T_P t)B_P` into the `B` difference and the semigroup difference; integrate the absolute-value bound and use `R(-T_Q)^{-1}1 <= h_* 1`. This proves forward Lipschitz continuity within a dimension, including unknown observed-rate values. It is a forward bound, not an inverse condition number.

The stationary solution is continuous on each irreducible component, since the usual normalized linear system has an invertible coefficient matrix. Each supported rate and stationary mass stays positive; consequently the finite stationary entropy sum is continuous there. Missing edges contribute zero and cannot appear along a converging sequence in this class. Thus `sigma` is continuous on the whole compact union.

There is also a data-independent upper bound. Microscopic activity is at most `nu`, and the absolute edge rate log-ratio is at most `A=log(M/m)`. Stationary cancellation gives the elementary bound `sigma <= nu A`. The sharper published Nishiyama–Hasegawa bound gives

\[
 \sigma(Q)\le\nu A\tanh(A/2).
\]

This explicit bound follows from imposed microscopic priors. It is not inferred from observed activity, and its existence does not depend on inverse identification. The exact constrained maximum can be smaller.

## Attainment and zero-tolerance limit

The closed set `K_eta(D)` is a nonempty compact subset of `K`; nonemptiness uses exact feasibility of `D`. Continuity of entropy gives attainment. The sets shrink as `eta` decreases, so their maxima decrease and are bounded below by `U_D(0)`.

For any decreasing sequence `eta_j -> 0`, choose maximizers `Q_j`. Extract a convergent subsequence in `K`. Continuity of observation and `d(O(Q_j),D) <= eta_j` imply that its limit `Q_*` satisfies `O(Q_*)=D`. Entropy continuity then gives

\[
 \lim_j U_D(\eta_j)=\sigma(Q_*)\le U_D(0).
\]

Together with the opposite inequality this proves the claim; monotonicity removes dependence on the chosen tolerance sequence. The proof is just nested compact optimization after the physical compactness and continuity assumptions have been verified. It warrants no general optimization-theory novelty claim.

Use **closed** tolerance balls for the displayed maximum. An open tolerance ball need not contain a maximizer. Its supremum has the same zero-tolerance limit for `eta > 0`, by squeezing between `U_D(0)` and the closed-ball maximum; its radius-zero open ball is empty.

## What this does not prove

- It does not identify the generator or entropy. `U_D(0)` is the largest value on a possibly nonunique exact fiber. Compact priors can exclude divergent sequences while retaining several finite values.
- It does not establish two-sided continuity of the exact upper value as the **center datum** varies, or a Lipschitz/Hölder inverse bound. The parameter held fixed in this proposition is feasible `D`; only its allowed tolerance shrinks. Generic compact continuous inverse problems can fail lower semicontinuity of their maximal fiber value.
- It does not give a computational certificate that a numerical local optimizer has found the global maximum over all allowed dimensions/supports. Numerical attainment claims need their own exhaustive optimization argument.
- It does not choose the physical values `m,M,nbar`. They must be justified externally or reported as sensitivity assumptions. Sending `m` to zero or `nbar,M` to infinity is outside the uniform claim.
- It does not by itself supply a finite-sample confidence set for `D`. A raw empirical waiting-time measure is atomic, while these model laws have densities; their row-TV distance is one, however many finite observations are collected. For an actual data-based construction, use a justified fitted-density TV region or a weaker metric/measurement confidence region. The weak-metric version above is available, but it still needs a statistical coverage argument.
- It does not repair detector-model error, unresolved thermodynamic channels, odd time-reversal variables, or uncertain microscopic incidence.

## Verification and deliverables

The proof was checked by two forward-continuity arguments (uniform tails plus finite-time convergence; integrated Duhamel) and an independent stationary-mass bound. No numerical experiment is needed to promote this elementary compactness argument. No script or generated numerical output is asserted. A manuscript-ready subsection is in `compact-priors.tex`; narrow primary-source positioning is in `PRIMARY-COMPARISON.md`. The coordinating agent should review its notation and integration before incorporation.
