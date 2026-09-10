# Fixed-order positive realization tests for the theta family

Date: 2026-09-10 UTC. Contribution: analytic deductions from the [compatibility theorem](compatibility-orbit.md) and primary positive-realization machinery reviewed in [the source note](../evidence/positive-realization-frontier.md). No new numerical search is reported. The point `(a,b)=(3,3)` remains settled by [the exact distant witness](theta-global-audit.md).

Write `s=a+b`, with `a,b>0`, and

\[
X=\begin{pmatrix}2&0&8\\0&7&11\end{pmatrix},\quad
Y=\begin{pmatrix}3&0\\0&6\\a&b\end{pmatrix},\quad
H=\begin{pmatrix}-7&4&0\\5&-11&0\\0&0&-s\end{pmatrix}.
\]

The hidden transfer is `F(z)=X(zI−H)⁻¹Y`. Put `α=9−2√6` and `β=9+2√6`; the hidden spectrum is `−α,−β,−s`. Sections 1–5 assume the hidden transfer has McMillan degree three, equivalently the full resolved-edge kernel has linear dimension five. Nonminimal strata require a separate argument; their larger realizations need not share this hidden spectrum. Section 6 supplies a construction that also covers the nonminimal slow-coincidence point.

## 1. One universal shift suffices at this fixed minimal dimension

Set `γ=−tr H=18+s`. Every compatible three-state hidden generator H' has the same trace. Its diagonal escapes `d_i=−H'ii` are positive because each full generator state has an outgoing rate. Therefore `0<d_i<γ`, and

\[
P'=I+H'/\gamma
\]

has positive diagonal entries and nonnegative offdiagonals. Its spectral radius is less than one. Thus every compatible CTMC, including one whose escapes exceed the original maximum diagonal escape, is covered by this same shift.

The corresponding discrete-time transfer is

\[
G(z)=F\big(\gamma(z-1)\big)
=X(zI-P)^{-1}B,\qquad P=I+H/\gamma,\quad B=Y/\gamma.
\]

A complete hidden block is equivalent to an entrywise strictly positive P'. The remaining visible-hidden rates are complete exactly when its input and output factors are entrywise strictly positive.

This fixed-order specialization does not contradict van den Hof's need to consider all admissible shifts when comparing arbitrary positive realization orders. Here minimality fixes the spectrum and trace, and the generator row sums bound each diagonal escape by that trace. Those additional restrictions supply a common shift.

## 2. Stochastic normalization is automatic after a strict realization is found

Suppose G has a three-dimensional realization `(C₀,P₀,B₀)` in which all three matrices are entrywise strictly positive. Its order equals the McMillan degree, so P₀ has exactly the poles of G and is stable. Define

\[
r=(I-P_0)^{-1}B_0\mathbf1>0,\quad D_r=\operatorname{diag}(r),
\]

\[
\widetilde P=D_r^{-1}P_0D_r,\quad
\widetilde B=D_r^{-1}B_0,\quad
\widetilde X=C_0D_r.
\]

Then `P̃1+B̃1=1`, and every matrix remains strictly positive. The continuous-time blocks

\[
\widetilde H=\gamma(\widetilde P-I),\qquad
\widetilde Y=\gamma\widetilde B
\]

satisfy `H̃1+Ỹ1=0`. Moreover

\[
\widetilde X\mathbf1=G(1)\mathbf1=F(0)\mathbf1=(10,18)^T.
\]

These are exactly the known visible row deficits, so adjoining the observed visible block produces a complete five-state CTMC with the prescribed kernels. The converse follows from section 1. Hence the task is precisely existence of an order-three realization of G with **all entries of the state, input and output matrices strictly positive**. A theorem guaranteeing only a nonnegative input/output factor or allowing extra states is insufficient.

## 3. Exact simplicial-cone criterion

Use the original minimal realization `(X,P,B)`. There is such a strict order-three realization if and only if a simplicial cone `K=V R_+³`, with V real and invertible, satisfies

1. Each column of B lies in the interior of K.
2. Each row of X is strictly positive on every nonzero vector in K.
3. P maps every nonzero vector of K into the interior of K.

Indeed these are precisely `V⁻¹B>0`, `XV>0`, and `V⁻¹PV>0`. Conversely, a strict order-three realization is similar to the original minimal one, giving exactly such a V. Diagonal normalization from section 2 then restores the CTMC constraints. No positivity is required of V in the original coordinates.

This is a finite-dimensional specialization of invariant-cone realization theory, not a new abstract characterization. It sharpens the unresolved geometry: a polyhedral invariant cone with more than three extreme rays proves existence at a larger state count, which does not answer the cap-five question. In the nonsingular exit chart `2a+b≠6`, the triangle formulation in the theta audit expresses the same search with CTMC normalization already built in. Singularity of that chart is not evidence of nonminimality.

## 4. What the elementary spectral tests do and do not exclude

All eigenvalues of P are positive:

\[
1-\alpha/\gamma,\quad1-\beta/\gamma,\quad1-s/\gamma.
\]

Away from `s=α`, the dominant one is simple. A collision at `s=β` is subdominant and is not by itself forbidden by Perron–Frobenius theory. The original shifted Markov matrices `XP^kB` are entrywise positive for every `k≥0`: the isolated shared state alone contributes `8a,8b,11a,11b` times a positive scalar, and the remaining two-state block contributes nonnegative entries.

When `s<α`, the dominant residue is a positive multiple of `[8,11]^T[a,b]`. When `s>α`, it comes from the irreducible two-state block; both visible input and output couplings see its positive Perron vectors, so its residue is also entrywise positive and rank one. Thus simple dominance, nonnegative poles, positive Markov matrices, and a positive rank-one dominant residue do not furnish an obstruction off `s=α`. No sufficiency theorem for exactly three strict states is asserted from these tests.

At `s=α`, a minimal three-state hidden realization has a repeated dominant eigenvalue. It cannot be similar to an irreducible Metzler matrix, so no complete five-state representative can exist within that minimal fiber. This excludes a complete representative only. It neither establishes entropy boundedness nor classifies other compatible supports. At a nonminimal point, the minimal-orbit premise fails and this spectral exclusion cannot be applied to arbitrary five-state alternatives.

## 5. Limits of the strict realization criterion

The normalization and universal shift reduce the question exactly to a strict order-three discrete-time matrix realization. The accessed primary cone theorem is an existence theorem with a polyhedral-cone requirement; it does not eliminate the three-ray feasibility problem. The closest source explicitly treating strictly positive realization matrices was accessible only through its abstract, so its exact assumptions and order guarantee remain unverified. No new classification of the off-line theta family follows from this note alone.

## 6. Update: the entire slow-coincidence line has unbounded entropy

The following analytic construction was proposed by the root agent and independently audited here. It settles the entropy question on `a+b=α` for every `a,b>0`, including the parts outside the earlier sufficient residue region and the nonminimal exceptional point. It does not assert existence of a complete hidden block on the minimal part of that line.

### 6.1 Necessary component structure at minimal points

At minimal points the hidden spectrum is `−α,−α,−β`. A bidirected hidden graph has block-diagonal connected components, each with an irreducible Metzler subgenerator. The repeated dominant eigenvalue excludes a single connected three-state component. Three singleton components are also impossible: the residue at `−β` has negative offdiagonal entries, whereas every singleton's residue is the nonnegative outer product of its entrance column and exit row. Thus every compatible minimal model on this line has exactly a two-state hidden component with spectrum `−α,−β` and a singleton with eigenvalue `−α`, up to hidden permutation. This restriction does not identify their residues separately.

### 6.2 Redistribute the coincident residue

Put `d=√6` and define column vectors p,q,v and row vectors r,t,w by

\[
p=\begin{pmatrix}3+d/2\\35d/8\end{pmatrix},\quad
q=\begin{pmatrix}3-d/2\\-35d/8\end{pmatrix},\quad
v=\begin{pmatrix}8\\11\end{pmatrix},
\]

\[
r=(1,4(d-1)/5),\qquad t=(1,-4(d+1)/5),\qquad w=(a,b).
\]

The two residues of the original hidden path are `pr` at `−α` and `qt` at `−β`; in particular

\[
pr+qt=\operatorname{diag}(6,42).
\]

The shared singleton contributes `vw` at `−α`, so the full transfer is

\[
F(z)=\frac{pr+vw}{z+\alpha}+\frac{qt}{z+\beta}.
\]

Choose any

\[
0<\varepsilon<\min\{a,b/r_y\}.
\]

Then both terms in the exact decomposition

\[
pr+vw=(p+\varepsilon v)r+v(w-\varepsilon r)
\]

are strictly positive rank-one matrices. This transfers a small portion of the singleton residue to the two-state component without changing either pole. The new pair response is

\[
F_2(z)=\frac{(p+\varepsilon v)r}{z+\alpha}+\frac{qt}{z+\beta}.
\]

Its zeroth Markov matrix has strictly positive offdiagonal entries, since

\[
(p+\varepsilon v)r+qt
=\operatorname{diag}(6,42)+\varepsilon vr.
\]

The inequalities on ε are satisfiable for every positive a,b; the earlier lower thresholds on a and b are unnecessary on this repeated-pole line.

### 6.3 A strict two-state positive realization, with all signs explicit

Let `pε=p+εv`, `A₀=diag(−α,−β)`, `C₀=[pε,q]`, and let B₀ have rows r,t. Define

\[
u=\frac{p_x+4\varepsilon}{q_x}>0,\qquad
\eta=1+\frac{11\varepsilon}{2p_y}>1,\qquad
V=\begin{pmatrix}1&1\\-u&\eta\end{pmatrix}.
\]

The transformed pair is `H₂=V⁻¹A₀V`, `X₂=C₀V`, `Y₂=V⁻¹B₀`. Its two hidden rates are

\[
(H_2)_{12}=\frac{(\beta-\alpha)\eta}{u+\eta}>0,\qquad
(H_2)_{21}=\frac{(\beta-\alpha)u}{u+\eta}>0.
\]

The output columns are `pε−u q` and `pε+η q`. The potentially restrictive entries are exactly `4ε` and `11ε/2`, respectively; the other two are sums of positive quantities. Hence `X₂>0` entrywise.

The input rows are

\[
\frac{\eta r-t}{u+\eta},\qquad\frac{ur+t}{u+\eta}.
\]

Their potentially restrictive entries are `(η−1)/(u+η)>0` and

\[
\frac{ur_y+t_y}{u+\eta}
=\frac{4\varepsilon r_y}{q_x(u+\eta)}>0,
\]

using `−t_y/r_y=p_x/q_x`. Their other entries are positive. Thus `Y₂>0` entrywise, and H₂ is stable and irreducible. This is an exact realization of F₂; no numerical approximation is involved.

### 6.4 Normalize, adjoin the singleton, and obtain divergence

Let `z₂=(−H₂)⁻¹Y₂1>0` and `D₂=diag(z₂)`. Replace the pair by

\[
\widehat H_2=D_2^{-1}H_2D_2,\quad
\widehat Y_2=D_2^{-1}Y_2,\quad
\widehat X_2=X_2D_2.
\]

This preserves strict positivity and gives `Ĥ₂1+Ŷ₂1=0`. For the singleton put

\[
z_3=(w-\varepsilon r)\mathbf1/\alpha>0,\quad
H_3=-\alpha,\quad Y_3=(w-\varepsilon r)/z_3,\quad X_3=vz_3.
\]

The three-state hidden block is the direct sum of Ĥ₂ and H₃. All six visible-hidden pairs are positive, and the first two hidden states have a bidirectional link; the singleton has no hidden links. The visible entrance totals equal

\[
\widehat X_2\mathbf1+X_3
=F(0)\mathbf1=(10,18)^T,
\]

so adjoining the fixed visible block `A=[[-11,1],[2,−20]]` gives an irreducible bidirected five-state CTMC with the original complete kernels.

The pair exit matrix Ŷ₂ is invertible: r,t are linearly independent, and both transformations above are invertible. Thus its two exit rows are unequal. The two pair states have the same external neighborhood `{x,y}`, with positive rates to both ports, and no links to the untouched singleton. The [embedded hidden-pair construction](hidden-pair-boundary-audit.md) therefore supplies an exactly equivalent family reaching a one-way boundary with positive opposing stationary flux, and entropy tends to infinity. This argument stays within five states.

Nothing in the construction uses minimality. At `(a,b)=(2√6−3,12−4√6)` it still gives a valid nonminimal five-state realization and the same divergent pair family. At every other point on `a+b=α`, the realization remains minimal by equality of its full kernels, while its hidden block remains reducible as required by the spectral obstruction.

**Conclusion.** Every positive point on the slow-coincidence line has unbounded entropy under the five-state cap. There are no singleton or bounded-nonunique entropy fibers on that line. The minimal points illustrate why impossibility of a complete compatible generator is not a finite-entropy certificate. The original open question away from this line is not resolved by this construction.

Verification status: independently audited by the displayed exact factorization, similarity identities and sign inequalities. Representative exact checks, including a slow-line point outside the direct residue region, are preserved in [check_theta_residue_construction.py](check_theta_residue_construction.py) and [theta-residue-checks.json](../outputs/theta-residue-checks.json). The entire line is covered by the analytic proof, including the nonminimal exception; the representative checks are not a parameter search. No novelty claim is made.
