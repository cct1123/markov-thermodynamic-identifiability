# Entropy is unbounded in every observational neighborhood

Date: 2026-09-10 UTC. Contribution: independent analytic audit of the coordinator's proposed neighborhood theorem, strengthened below to an exactly fixed generator trace. Mathematical status: conventionally proved by the displayed argument; not formally verified. No numerical experiment was required or performed. No novelty claim is made.

Sources inspected: the repository's [formulation](formulation.md), [compatibility audit](compatibility-orbit.md), and [hidden-pair boundary theorem, Sections 1–3](hidden-pair-boundary-audit.md#3-explicit-fixed-topology-boundary-theorem), recorded as [E032](../evidence/RECORDS.md#e032). These are shared mathematical dependencies, not independent primary literature. The independent contribution here is the perturbation/continuity argument, its exact-trace strengthening, and the audit of the statistical consequence proposed by the coordinator.

## 1. Precise strongest statement

Fix a finite irreducible row CTMC generator \(Q\) on \(N\) states, with simple bidirected support. Let \(\mathcal O\) be a nonempty reverse-closed set of resolved observed directed edges, all having positive rates, with known endpoints. Assume there exist **two distinct fully hidden states** \(h,k\): neither is an endpoint of any edge in \(\mathcal O\). Topology is otherwise unknown and all bidirected edges between existing states are admissible. Rates use the same fixed time unit.

For two such models with the same marks, define the observable-law distance

\[
d(Q,P)=\max_{I\in\mathcal O}\frac12\sum_{J\in\mathcal O}
\int_0^\infty |\psi^Q_{IJ}(t)-\psi^P_{IJ}(t)|\,dt.
\]

This is the maximum row total-variation distance between the **joint** next-mark/time probability laws. It is a pseudometric on generators, since different generators can have equal observed kernels.

**Theorem.** Put \(M=-\operatorname{tr}Q>0\). For every \(\eta>0\) and every finite \(K\), there exists a complete, irreducible, simple bidirected generator \(Q'\) on exactly the same \(N\) states such that

\[
d(Q,Q')<\eta,\qquad \sigma(Q')>K,
\]
\[
q'_{ij}=q_{ij}\quad ((i,j)\in\mathcal O),\qquad
\operatorname{tr}Q'=\operatorname{tr}Q,
\]
\[
0<q'_{ij}\le M\quad(i\ne j).
\tag{1}
\]

In fact, for each sufficiently small perturbation of the observable data constructed below, there is an **entire exact-kernel family** of such generators whose entropy tends to infinity. The upper rate bound \(M\) is independent of \(\eta\), \(K\), and the member of that family. There is no minimality assumption.

The theorem concerns arbitrarily small positive neighborhoods. It does not assert that the exact fiber of the original \(Q\) is unbounded, and it therefore does not contradict the repository's exact singleton or finite two-point fibers.

## 2. A complete perturbation with exactly the original trace

Let \(\mathcal U=\{(i,j):i\ne j,\ (i,j)\notin\mathcal O\}\), and set

\[
u=\sum_{(i,j)\in\mathcal U}q_{ij}>0.
\]

Strict positivity follows without minimality: every outgoing jump from the fully hidden state \(h\) is unobserved, and irreducibility gives it positive escape rate. Choose any visible state \(x\), which exists because the observed set is nonempty. Give every pair in \(\mathcal U\) weight one except \((h,x)\), which receives weight two. Write their total weight as \(w_\Sigma\). Define a row generator \(G\) by

\[
g_{ij}=\begin{cases}
q_{ij},&(i,j)\in\mathcal O,\\
u w_{ij}/w_\Sigma,&(i,j)\in\mathcal U,
\end{cases}
\qquad g_{ii}=-\sum_{j\ne i}g_{ij}.
\tag{2}
\]

All offdiagonal entries are positive, observed rates are unchanged, and
\(-\operatorname{tr}G=-\operatorname{tr}Q\). For \(0<\varepsilon<1\), put

\[
P_\varepsilon=(1-\varepsilon)Q+\varepsilon G.
\tag{3}
\]

This is a complete bidirected irreducible row generator with the same observed rates and exactly the same trace as \(Q\).

The external exit rows of \(h,k\), including exits to **every** state outside that pair, differ for all sufficiently small positive \(\varepsilon\). To verify this without assuming minimality, denote their difference in \(Q\) by \(v\), and their difference in \(G\) by \(w\). Construction (2) gives \(w=(u/w_\Sigma)e_x\ne0\). Their difference in (3) is \((1-\varepsilon)v+\varepsilon w\). If \(v=0\), this is nonzero for every positive \(\varepsilon\). If \(v\ne0\), continuity keeps it nonzero for all sufficiently small positive \(\varepsilon\). A possible isolated cancellation at a larger \(\varepsilon\) is irrelevant and is explicitly avoided.

Using a convex combination rather than only adding rates is the exact-trace strengthening. The coordinator's additive construction also works; it instead gives a uniform upper bound \(-\operatorname{tr}Q-\varepsilon_0\operatorname{tr}C\) for a fixed permitted \(\varepsilon_0\).

## 3. Independent quantitative continuity of the observation law

Use the formulation's fixed mark matrices \(E,R,B\), with \(R\) selecting each observed reset state and \(B\) containing the observed exit rates. Because (3) preserves observed rates and incidence, all three matrices are unchanged. Put

\[
T=Q-E,\quad T_\varepsilon=P_\varepsilon-E,
\quad \Delta=G-Q.
\]

Both killed matrices are transient Metzler matrices. The finite irreducible chains hit a next observed edge almost surely with finite mean. Consequently

\[
\int_0^\infty e^{T_\varepsilon t}B\mathbf1\,dt=\mathbf1,
\qquad \int_0^\infty e^{Tt}\,dt=(-T)^{-1}.
\tag{4}
\]

The first identity uses the complete joint row normalization. It would not follow from separately normalized conditional waiting densities.

Duhamel's identity and entrywise positivity give

\[
\left|R(e^{T_\varepsilon t}-e^{Tt})B\right|
\le\varepsilon\int_0^t Re^{Ts}|\Delta|e^{T_\varepsilon(t-s)}B\,ds.
\]

Integrate, sum over next marks, and use (4). The total-variation distance of row \(I\) obeys

\[
\operatorname{TV}_I(Q,P_\varepsilon)
\le\frac\varepsilon2\left[R(-T)^{-1}|\Delta|\mathbf1\right]_I.
\tag{5}
\]

Every matrix and integrand on the bounding side is nonnegative, so exchanging the two integrals is justified. Define
\(r_i=\sum_{j\ne i}|g_{ij}-q_{ij}|\).
Since \(\Delta\mathbf1=0\), the diagonal absolute difference is at most \(r_i\); hence \(|\Delta|\mathbf1\le2r\). Therefore

\[
d(Q,P_\varepsilon)
\le\varepsilon\max_I\left[R(-T)^{-1}r\right]_I
\le\varepsilon r_{\max}\max_I\mathbb E_{b_I}^Q[\tau].
\tag{6}
\]

The constant is finite and independent of \(\varepsilon\). Units are consistent: \(r\) has inverse-time units, expected waiting time has time units, and total variation and the mixing coefficient \(\varepsilon\) are dimensionless.

There is also a direct coupling verification. While both chains occupy the same state, use common jump clocks at the minimum of their corresponding rates and separate excess clocks. Their total separation hazard is \(\varepsilon r_i\). Observed jump clocks are common because their rates are unchanged. Before the first separating jump, both next-mark identities and event times agree. Bounding the separation probability by the integrated hazard up to the original next observed event yields (6). For the coordinator's purely additive perturbation, this reduces to the simpler extra-clock bound \(\varepsilon c_{\max}\mathbb E[\tau]\).

## 4. Exact-kernel entropy divergence and the uniform rate cap

Fix a sufficiently small positive \(\varepsilon\) for which the external exit rows differ. In the complete generator \(P_\varepsilon\), the chosen hidden pair is adjacent and has identical external neighborhoods. Thus the explicit unequal-row version of the [hidden-pair theorem](hidden-pair-boundary-audit.md#3-explicit-fixed-topology-boundary-theorem) applies. It does not need a minimal-realization hypothesis.

For clarity, that theorem uses an invertible normalized pair mixing matrix

\[
U_e=\begin{pmatrix}1-e&e\\0&1\end{pmatrix},
\quad S_e=\operatorname{diag}(I_{N-2},U_e),
\quad 0\le e<e_*(\varepsilon)<1.
\]

All generated models
\(Q_{\varepsilon,e}=S_e^{-1}P_\varepsilon S_e\)
retain the complete support and all observed rates. They have **exactly** the kernel of \(P_\varepsilon\) for every time, and

\[
\sigma(Q_{\varepsilon,e})\longrightarrow\infty
\quad\text{as }e\uparrow e_*(\varepsilon).
\tag{7}
\]

The source theorem justifies (7) through a vanishing one-way limiting flux with positive reverse limiting flux and strictly positive limiting stationary probabilities. It is not a large optimized value or a claim that one zero rate automatically causes divergence.

Every member is a row generator, and similarity preserves trace. Hence

\[
\sum_i\sum_{j\ne i}q_{\varepsilon,e;ij}
=-\operatorname{tr}Q_{\varepsilon,e}
=-\operatorname{tr}Q=M.
\tag{8}
\]

Nonnegativity bounds every individual rate by the same \(M\). This is a bound on the sum of state escape rates, not an identification of trace with stationary jump activity. Formula (8) also bounds the latter, since it is a stationary average of the state escape rates.

To prove the theorem's quantifiers, first choose a fixed positive \(\varepsilon\) small enough that (6) is below \(\eta\) and the unequal-row premise holds. Next let \(e\) approach its boundary until (7) exceeds \(K\). All these models have distance exactly \(d(Q,P_\varepsilon)\) from \(Q\), since their kernels are identical. Their common bound (8) is independent of both choices.

This order matters. As \(\varepsilon\downarrow0\), the divergence coefficient or positive limiting stationary masses may also approach zero. For each fixed positive \(\varepsilon\), the divergence remains unbounded; no uncontrolled simultaneous limit is needed. A diagonal sequence can be chosen afterwards with observable distance tending to zero and entropy tending to infinity.

## 5. Falsification audit and boundaries of the statement

The proposed theorem was challenged at the following consequential points.

- **Equal exit rows/nonminimal models:** the pair theorem's unequal-row hypothesis is created explicitly in (2)-(3). Minimality is never inferred or required.
- **Hidden versus merely unobserved pair edge:** both selected states must be absent from every mark endpoint. Only then does the mixing preserve reset coordinates, observed jump-rate columns, and observed-edge matrices.
- **All external neighbors:** the rows compared include every outside state, including other hidden states. The complete perturbation supplies true external twins.
- **Normalization and all times:** (4)-(6) use joint normalized next-mark/time rows. The mixing preserves the matrix exponential kernel exactly, rather than matching moments or a finite time grid.
- **Uniform finite rates:** rates remain bounded because they are nonnegative and have fixed trace. Entropy can nevertheless diverge because there is no uniform positive lower bound on reverse rates.
- **Exceptional cancellation in the perturbation:** a possible isolated positive mixing coefficient at which external rows coincide is avoided by restricting to the proven sufficiently small interval.
- **Topology restrictions:** the completion step adds previously absent edges. Therefore the theorem is not a general assertion for a prescribed sparse topology. If the initial topology is complete, some cases already have an unbounded exact fiber, but that is a separate stronger premise.
- **Necessity of some hidden freedom:** dropping the hidden-state assumptions entirely makes the universal claim false. For example, every irreducible simple bidirected two-state CTMC has zero entropy. This audit does not classify the one-hidden-state case.
- **Additional rate-domain restrictions:** a uniform positive lower bound on all supported reverse rates changes the conclusion. With both rates in \([m,M]\), \(m>0\), the stationary cancellation formula bounds entropy by total stationary jump rate times \(\log(M/m)\). The construction necessarily approaches a boundary that such a restriction would exclude.

No counterexample survived under the stated assumptions. This is not an inference from a failed computational search: the constructive proof specifies an admissible family and the divergent limit. The universal trace cap \(-\operatorname{tr}Q\) is sufficient; this audit does not claim it is the smallest possible common rate cap.

## 6. Finite-horizon statistical implication: audit of the added claim

The coordinator additionally asked whether a uniform-confidence consequence follows. **It does**, under precise sampling and coverage assumptions. This is a separate statistical corollary, not a consequence of row total variation alone for arbitrary observation protocols.

Suppose the data consist of the observed marked path on a fixed finite physical interval \([0,H]\), started in the model's stationary distribution. The normalized similarities above preserve its stationary law exactly: \(\pi'=\pi S_e\), \(T'=S_e^{-1}TS_e\), \(E_J S_e=S_e E_J\), and \(S_e\mathbf1=\mathbf1\). Substitution in each marked-path likelihood

\[
\pi e^{Tt_1}E_{J_1}e^{T(t_2-t_1)}\cdots
E_{J_n}e^{T(H-t_n)}\mathbf1
\]

cancels every similarity. The same formula for zero events covers censoring at both window ends.

Moreover, the stationary distributions of \(P_\varepsilon\) converge to that of \(Q\), since the normalized finite stationary linear system has a nonsingular reduced system at irreducible \(Q\). A maximal initial coupling and the common/excess-clock coupling yield the finite-window observation bound

\[
\operatorname{TV}(\mathbb P_Q^{H},\mathbb P_{P_\varepsilon}^{H})
\le\operatorname{TV}(\pi_Q,\pi_{P_\varepsilon})
+\varepsilon r_{\max}H\longrightarrow0.
\tag{9}
\]

Combining (7) with (9) gives a sequence within the exactly fixed-trace, uniformly bounded-rate class such that \(\sigma(Q_n)\to\infty\) and \(\mathbb P_{Q_n}^{H}\to\mathbb P_Q^{H}\) in total variation.

Let \(U\) be a measurable extended-real upper confidence bound satisfying the **uniform** coverage requirement

\[
\mathbb P_P^{H}\{U\ge\sigma(P)\}\ge1-\alpha
\quad\text{for every }P\text{ in the stated model class}.
\tag{10}
\]

For each finite threshold \(C\), eventually \(\sigma(Q_n)>C\), so total-variation transfer of (10) gives
\(\mathbb P_Q^{H}\{U>C\}\ge1-\alpha\).
Taking \(C\uparrow\infty\) and continuity from above proves

\[
\boxed{\ \mathbb P_Q^{H}\{U=+\infty\}\ge1-\alpha.\ }
\tag{11}
\]

This conclusion holds even at an exactly identifiable or finite-fiber source. Independent auxiliary randomization does not help: adjoining the same random seed preserves the total-variation convergence. It does not apply automatically to pointwise/asymptotic coverage promises, restricted parametric priors, a positive reverse-rate floor, an increasing horizon without controlling the joint limit, or sampling from a specified microscopic hidden state. If the observation begins immediately after a specified observed mark, a different simple route works: the TV distance for any fixed number \(n\) of next-mark/time transitions is at most \(n d\), by sequential coupling.

### Independent hand check of the coordinator's four-state illustration

In order \((x,y,h,k)\), the proposed source is

\[
Q_0=\begin{pmatrix}
-2&1&1&0\\1&-2&0&1\\1&0&-2&1\\0&1&1&-2
\end{pmatrix},
\]

with only \(x\leftrightarrow y\) observed. Add rate \(\varepsilon\) on both missing bidirected pairs \(x\leftrightarrow k\), \(y\leftrightarrow h\), subtracting \(\varepsilon\) from every diagonal. This symmetric complete \(Q_\varepsilon\) has uniform stationary law. For the hidden pair mixing \(U_t=\left(\begin{smallmatrix}1-t&t\\0&1\end{smallmatrix}\right)\), \(0\le t<\varepsilon<1/2\), direct substitution gives all rates at most \(1+\varepsilon<3/2\), stationary vector \((1,1,1-t,1+t)/4\), and

\[
\sigma(Q_{\varepsilon,t})=
\frac{t(1-\varepsilon)}4
\log\frac{(1-\varepsilon t)(\varepsilon+t)}
{(\varepsilon-t)(1+\varepsilon t)}.
\tag{12}
\]

This formula was checked independently by hand: the four visible-hidden edge currents have magnitude \(t(1-\varepsilon)/4\), while the observed edge and hidden pair carry zero current; multiplying their four oriented flux ratios gives precisely the logarithm argument in (12). The logarithmic divergence coefficient is \(\varepsilon(1-\varepsilon)/4>0\).

The original expected next-mark times from \(x,y\) equal two: by symmetry write \(u_x=u_y=u\), \(u_h=u_k=v\); the killed equations give \(2u-v=1\) and \(v-u=1\), hence \(u=2,v=3\). Each state acquires extra jump rate exactly \(\varepsilon\), so \(d(Q_0,Q_\varepsilon)\le2\varepsilon\). Both models start uniformly, and the stationary finite-horizon observation laws differ by at most \(1-e^{-\varepsilon H}\le\varepsilon H\). Exact stationary observed-path equivalence transfers this bound to \(Q_{\varepsilon,t}\).

Thus the coordinator's explicit rate cap \(3/2\), entropy expression, TV constants, and confidence-bound consequence are consistent. This illustration uses an additive perturbation and does **not** keep trace exactly fixed; the general construction (2)-(8) establishes that stronger property separately. The source's asserted exact global uniqueness is supplied by the existing path-delay result and the coordinator's separate certificate; it was not needed to prove (12), the TV bounds, or the confidence impossibility.

## Outcome and remaining limits

The neighborhood theorem is supported by an explicit construction and two independent continuity routes (semigroup integration and coupling), with the exact-trace strengthening proved above. The uniform-confidence corollary follows under stationary finite-window sampling and uniform coverage; its narrower sampling assumptions are essential to the stated proof. No computation, external experiment, new source retrieval, or exhaustive topology search was needed. Publication novelty and statistical-prior-art comparison remain separate tasks.
