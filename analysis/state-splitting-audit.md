# One additional hidden state makes entropy unbounded

Date: 2026-09-10 UTC. Contribution: analytic audit and derivation; no numerical calculation or novelty claim. The model and observation conventions are those of [formulation.md](formulation.md). Strong-lumping antecedents and the earlier lumpable counterexample are recorded in [E001](../evidence/RECORDS.md#e001) and [E018](../evidence/RECORDS.md#e018); the general construction below must be compared with prior art before any novelty claim.

## Statement and scope

Let `Q` be any finite irreducible simple bidirected row CTMC on `N` states. A nonempty reversal-closed set of observed marks resolves individual directed edges with known incidence. Let `V` be the set of all endpoints of observed edges. Suppose there is at least one **fully hidden** state `h` outside `V`.

There is a family of irreducible simple bidirected CTMCs on **exactly `N+1` states** with the same observed marks and exactly the same full joint waiting kernels as `Q`, whose entropy production tends to infinity. All off-diagonal rates in the family are uniformly bounded above. One directional rate tends to zero while the opposing stationary flux stays positive.

Only one additional hidden state is sufficient even when `h` has only one neighbor. This is a sufficient state budget, not a claim that an additional state is necessary in every example.

The enlarged realization is nonminimal as a realization of the observed kernel: the original `N`-state model already realizes that kernel. Thus this construction applies to cardinality classes that admit nonminimal models. It does not establish unboundedness inside a fixed-dimension minimal class, a fixed topology, or a model class imposing a common positive rate lower bound.

## 1. Exact construction

Replace `h` by two states `h_1,h_2`. For each outside state `i!=h`, choose a fixed `theta_i` strictly between zero and one. Define a generator `Q_tilde(m)` by keeping all rates between outside states unchanged, and setting

\[
\widetilde q_{i h_1}=\theta_iq_{ih},\qquad
\widetilde q_{i h_2}=(1-\theta_i)q_{ih},
\]

\[
\widetilde q_{h_1 j}=\widetilde q_{h_2 j}=q_{hj}
\quad(j\ne h),
\qquad
\widetilde q_{h_1h_2}=m>0,\quad
\widetilde q_{h_2h_1}=n>0.
\]

Here `n` is held fixed; `m` will approach zero from above. Missing original edges remain missing in the displayed formulas. Diagonal entries are minus the new row escape rates. In particular, writing

\[
\lambda=\sum_{j\ne h}q_{hj}>0,
\]

the clone diagonals are `-lambda-m` and `-lambda-n`.

Every old neighbor of `h` is connected bidirectionally to both clones. The internal clone edge is bidirectional for every `m>0`. No parallel channels or self-jump channels are introduced. Connectivity of the original graph implies connectivity of the enlarged graph. The construction therefore remains in the stated admissible CTMC class for every positive `m`.

All original observed edges lie entirely outside `h`; retain them with their original rates, endpoints and marks. Both clones and their internal edge remain unobserved.

## 2. Strong lumping also preserves the killed generator

Let `C` be the `(N+1) x N` binary aggregation matrix mapping both clones to `h` and every other state to itself. For row probability vectors, coarse probabilities are `p_tilde C`. Both clone rows have the same total rate into every outside coarse state, while their internal rates cancel in the coarse `h` column. Each outside row has the original total rate into the two clones. Therefore

\[
\widetilde Q C=CQ.
\]

This is exact strong lumpability, valid at every `m,n` and every allowed choice of the split fractions.

Let `E` and `E_tilde` contain the observed off-diagonal rates, and use the killed generators `T=Q-E` and `T_tilde=Q_tilde-E_tilde`; their diagonals remain those of their full generators. Since no observed mark touches `h`,

\[
\widetilde E C=CE,\qquad
\widetilde T C=CT.
\]

Let `R,B` and `R_tilde,B_tilde` be the reset/output and observed-rate/input matrices of the full joint kernel. Every observed source and target remains an unsplit outside state, so

\[
\widetilde B=CB,\qquad \widetilde R C=R.
\]

Matrix-power induction, then the convergent exponential series, gives `exp(T_tilde t) C=C exp(T t)`. Consequently

\[
\widetilde\Psi(t)
=\widetilde R e^{\widetilde Tt}\widetilde B
=\widetilde R C e^{Tt}B
=R e^{Tt}B
=\Psi(t)
\quad(t\ge0).
\]

This proves equality of all joint next-mark/time densities, including their absolute time scale and normalization. It applies to any number of resolved reverse-closed observed marks. It is not merely equality of coarse stationary probabilities, marginal dwell distributions, or finitely many sampled times. The observed event process is Markov renewal under the stipulated resolved marks, so the equality also fixes its full event-indexed trajectory law.

## 3. Explicit stationary probabilities and divergent entropy

Let `pi` be the original stationary law, and let `pi_tilde(m)` be the stationary law of the enlarged chain. Strong lumping and irreducibility give

\[
\widetilde\pi_i=\pi_i\quad(i\ne h),\qquad
\widetilde\pi_{h_1}+\widetilde\pi_{h_2}=\pi_h.
\]

Define the stationary incoming flux assigned to the first clone and its normalization by

\[
A=\sum_{i\ne h}\pi_i\theta_iq_{ih},\qquad
\alpha=A/\pi_h.
\]

Original stationarity at `h` gives `sum_i!=h pi_i q_ih=pi_h lambda`. At least one term is positive, and every nonzero term is multiplied by a fraction strictly between zero and one. Hence

\[
0<A<\pi_h\lambda,\qquad 0<\alpha<\lambda.
\]

The first-clone balance equation is

\[
0=A+n\widetilde\pi_{h_2}-(\lambda+m)\widetilde\pi_{h_1}.
\]

Using the clone-sum identity yields the exact stationary probabilities

\[
\widetilde\pi_{h_1}
=\pi_h\frac{\alpha+n}{\lambda+m+n},\qquad
\widetilde\pi_{h_2}
=\pi_h\frac{\lambda+m-\alpha}{\lambda+m+n}.
\]

Both have strictly positive limits at `m=0`. The two internal stationary fluxes are

\[
a(m)=m\widetilde\pi_{h_1}\longrightarrow0,
\qquad
b(m)=n\widetilde\pi_{h_2}\longrightarrow
b_0=\pi_h\frac{n(\lambda-\alpha)}{\lambda+n}>0.
\]

Thus the internal-edge entropy contribution

\[
(a(m)-b(m))\log\frac{a(m)}{b(m)}
\]

diverges to positive infinity. Every other unoriented-edge entropy term is nonnegative. More precisely, fixing any reference rate `m_ref>0` in the same units,

\[
\sigma(\widetilde Q(m))
=b_0\log\frac{m_{\rm ref}}m+O(1)
\quad\text{as }m\downarrow0.
\]

All other existing-edge rates and stationary probabilities approach strictly positive finite limits, so their entropy contributions remain finite; this justifies the displayed leading coefficient. Choosing `0<m<=m_ref` keeps every off-diagonal rate bounded by the maximum of the original rates, `n`, and `m_ref`. The upper-unbounded entropy does not require rates tending to infinity.

There is also a direct boundary irreducibility check. At `m=0` the internal clone edge is one-way, but either clone can reach the other through an old neighbor: `h_1 -> i -> h_2` and `h_2 -> i -> h_1` both have positive rates. The rest of the graph remains connected through the old paths. The boundary generator is therefore irreducible even when the original hidden state has degree one. The boundary need not itself satisfy bidirected support; every approximating `m>0` model does.

## 4. Exception: all microscopic states are observed endpoints

Suppose a compatible irreducible model has state set exactly `V`, so it has no fully hidden state. Under known observed incidence and reversal closure, the full generator is recoverable from the first two kernel coefficients.

For any observed mark `J=(a_J,b_J)`,

\[
q_J=\psi_{\bar J,J}(0).
\]

For every `v,w in V`, select an observed mark `I` ending at `v` and an observed mark `J` starting at `w`. Such choices exist by the definition of `V` and reversal closure. Then

\[
T_{vw}=\frac{\psi'_{I,J}(0)}{q_J}.
\]

Thus the data determine the entire visible block `Q_VV=T_VV+E_VV`, including its diagonal and all unobserved edges between visible endpoints.

In any larger compatible model, the same calculation gives the same block `Q_VV`. Define its data-determined row deficits

\[
d_v=-\sum_{w\in V}(Q_{VV})_{vw}.
\]

Generator normalization implies

\[
d_v=\sum_{h\notin V}q_{vh}\ge0.
\]

The originally fully visible model has `d_v=0` for every `v`. Hence every putative larger compatible model has no transitions from `V` into its additional states. Since `V` is nonempty, such a larger chain cannot be irreducible. Additional fully hidden states are therefore excluded, and the recovered generator is globally unique within the unrestricted finite-state class with this known incidence.

This reasoning does not require treating unobserved edges between observed endpoints as hidden states. Such edges are reconstructed in `Q_VV`. It would fail if observed marks could blur multiple microscopic transitions or their endpoint incidence could change.

## 5. Unrestricted finite cardinality: a complete upper-range dichotomy

Assume the given kernel has at least one finite admissible realization and observed incidence is fixed. The short-time construction above determines `Q_VV` and its deficits independently of the realization.

- If all deficits vanish, irreducibility permits no hidden states. The full generator and its finite entropy are unique.
- If any deficit is positive, every compatible realization has at least one fully hidden state. Applying the splitting construction to any one finite realization gives a finite enlarged family with unbounded entropy.

Therefore unrestricted finite cardinality gives **unique generator/entropy or unbounded entropy**, with the alternative determined by the visible row deficits. This is an upper-range conclusion conditional on model feasibility. It neither solves a realization-existence problem for arbitrary input functions nor identifies the entropy infimum in the unbounded case. It also does not say that every nonzero-deficit kernel is compatible with equilibrium.

## 6. Exact implications and limits for the `N<=6` program

For a class allowing arbitrary bidirected topology and all state counts up to `N_max`, a compatible model with a fully hidden state and at most `N_max-1` states immediately implies an unbounded entropy range **within that cap**. The enlarged family uses its source model's state count plus one, which does not exceed the cap.

For the usual single observed pair `x<->y`, this gives:

| Available compatible model | Guaranteed unbounded class |
| --- | --- |
| 3 states, including one fully hidden state | all models with at most 4 states |
| 4 states, including a fully hidden state | all models with at most 5 states |
| 5 states, including a fully hidden state | all models with at most 6 states |
| 6 states, including a fully hidden state | all models with at most 7 states; this construction alone says nothing decisive about the cap of 6 |

Consequently, even the globally unique **fixed-four-state minimal** cases in [unknown-topology-audit.md](unknown-topology-audit.md) become unbounded when a fifth state is allowed without a minimality restriction. The two theorems concern different admissible classes and are consistent.

For general observed mark sets, replace the “single observed pair” wording by the condition that at least one original state lies outside the known endpoint set `V`. The same one-state increment applies. Any fully visible compatible model, of whatever cardinality within the cap, remains globally unique even if the cardinality restriction is removed, by Section 4.

The splitting argument does **not** classify all kernels feasible under a six-state cap. In particular, it leaves open kernels for which every admissible realization within the chosen class already needs six states, and it does not justify identifying minimum positive-CTMC realization size with minimal linear realization dimension. Likewise, a restriction to minimal models removes these constructed nonminimal enlargements and requires separate analysis.

## Audit outcome

The proposed construction is valid for general resolved marked observations under its stated hidden-state condition. Killed-generator lumpability, stationary positivity and the degree-one hidden-state case all check analytically. The exact stationary formula makes the logarithmic divergence explicit. The no-hidden-state exception holds across all larger finite irreducible models when observed incidence is fixed, and strengthens the unrestricted-cardinality conclusion to a short-time-testable upper-range dichotomy. No publication novelty is asserted.
