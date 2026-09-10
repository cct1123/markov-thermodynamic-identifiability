# A sharp balanced-theta boundary with a finite two-model endpoint

Date: 2026-09-10 UTC. This is the scoped continuation of D012's balanced-parameter question, under the unchanged [formulation](formulation.md). Contribution: conventional analytic deductions, exact algebraic calculations and explicitly separate numerical discovery. No publication-novelty or formal-verification claim.

## Exact endpoint result

Let

\[
Q(z)=\begin{pmatrix}
-11&1&2&0&8\\2&-20&0&7&11\\3&0&-7&4&0\\
0&6&5&-11&0\\z&z&0&0&-2z
\end{pmatrix},\qquad z>0,
\]

in order \((x,y,h,k,l)\), with only the resolved pair \(x\leftrightarrow y\) observed. Competitors are irreducible simple bidirected CTMCs, with known visible endpoints and **at most five states**, and the same full joint next-mark/time kernels at every time. All rates are finite, states even under time reversal, and there is no imposed positive rate cutoff. Hidden relabelings are identified.

Define \(z_*\) as the unique positive real root of

\[
\boxed{352z^4-3168z^3-4644z^2-11340z-7623=0.}
\tag{1}
\]

Its value is \(z_*=10.5571496686650\ldots\). At \(z=z_*\), the entire compatible generator set consists of **exactly two models up to hidden labels**: the disconnected-hidden source and one connected-hidden path realization. Their entropy rates differ. Exact rational enclosures give

\[
0.062946400236\le\sigma(Q(z_*))\le0.062946400237,
\]
\[
0.065579685966\le\sigma(Q_*(z_*))\le0.065579685967.
\tag{2}
\]

Thus the entropy fiber at this five-state cap is bounded and non-singleton, in fact a two-point set. This answers the previously unresolved **existence** question for minimal five-state kernels, without classifying arbitrary five-state kernels. The values are inverse-time rates with \(k_B=1\) and natural logarithms. Allowing a sixth hidden-capable state invokes the accepted splitting construction and makes the entropy unbounded again.

For every \(z>z_*\), the generator is globally unique. For every \(0<z<z_*\), the entropy fiber is unbounded. The [cone note, Section 6](balanced-cone-bound.md#6-sufficiency-below-the-fold-complete-compatible-generators) proves complete realizations for all \(10.5\le z<z_*\); this overlaps the previously proved unbounded interval \(0<z<z_c\). Thus the entire balanced entropy classification is

| Balanced parameter, five-state cap | Entropy fiber |
| --- | --- |
| \(0<z<z_*\) | Unbounded above |
| \(z=z_*\) | Exactly two distinct finite values |
| \(z>z_*\) | Singleton; generator globally unique |

This is an entropy classification for the whole ray, not an assertion of connected hidden support at every subcritical parameter. The slow-coincidence line retains the earlier disconnected-hidden obstruction. In the saved fast-parameter gap, connected-hidden feasibility is completely classified: complete graphs exist below the fold, exactly one path exists at it, and none exists above it.

## Why the whole endpoint fiber is exhausted

At these parameters \(2z>\beta=9+2\sqrt6\), the three hidden modes \(-\alpha,-\beta,-2z\) are distinct with nonzero rank-one residues, where \(\alpha=9-2\sqrt6\). The full marked kernel has minimal dimension five. Hence every competitor under the cap has five states and belongs to the normalized hidden-similarity class, by the prior [spectral audit, Sections 2–3](theta-fast-spectral-audit.md).

The new [global cone proof](balanced-cone-bound.md) considers every connected hidden support through a finite Perron-normalized invariant triangle. It proves nonexistence above (1). At equality, its sequence of strict envelope optimizations forces a unique triangle: the left and bottom vertices lie on specified output faces, one input lies on a lower edge, the other on the upper edge, and both upper-vertex vector fields are tangent to the lower edges. These are paired zero constraints; they leave a hidden path with center attached only to \(x\), one endpoint only to \(y\), and the other attached to both visible states. Positive column rescaling of a cone supplies no extra normalized CTMC, since the row-normalizing vector is uniquely \(-H^{-1}Y\mathbf1\).

This proves **at most one** connected-hidden generator, not just local isolation or the absence of a complete graph. The exact construction below proves its existence. For disconnected hidden graphs, the previous [construction audit, Section 5](theta-family-construction-audit.md#5-reducible-hidden-blocks-in-two-residual-regions) exhausts singleton/pair spectral assignments and identifies only the original generator for \(2z>\beta\). Combining these two global arguments gives exactly two generators. No connected component, sparse support, boundary-zero stratum, smaller model, or positive similarity assumption is omitted within the stated class.

## Independent path-coordinate construction

The endpoint candidate was derived independently from the physical hidden path using the exit chart in [the earlier path audit, Section 4](theta-fast-hidden-paths.md#4-one-variable-reduction-for-the-two-remaining-patterns). Its algebra does not use the cone envelope. Write

\[
C=\begin{pmatrix}3&0&1\\0&6&1\\z&z&1\end{pmatrix},\quad
H=\begin{pmatrix}-7&4&0\\5&-11&0\\0&0&-2z\end{pmatrix},\quad D=C^{-1}HC.
\]

Let the new hidden order be (y-only endpoint, x-only center, shared endpoint), with exit chart

\[
C'=\begin{pmatrix}0&u&1\\v&0&1\\B&A&1\end{pmatrix}.
\]

To state the rational formulas without long expanded coefficients, exchange the visible coordinates of the vector field and set

\[
(a_1,a_2,b_1,b_2,c_1,c_2)
=(D_{22},D_{21},D_{12},D_{11},D_{32},D_{31}),
\]

using one-based matrix indices. Set

\[
p_x=(42+11z)/18,\quad p_y=11z/18,\quad
q_x=8z/10,\quad q_y=(6+8z)/10.
\]

The endpoint tangency and visible-incidence equations give

\[
v=-\frac{u(a_2u+c_2)}{u^2+a_1u+c_1},\quad
c=\frac{p_x-u}{p_y},\quad d=\frac{q_y-v}{q_x},
\]
\[
A=\frac{u+cv}{1-cd},\qquad B=\frac{v+du}{1-cd}.
\tag{3}
\]

The remaining missing reverse hidden edge is a scalar polynomial condition. After preserving all original denominator exclusions, its numerator factors into \(u(u-6)z\) and three quadratics in \(u\). The relevant quadratic is

\[
a(z)u^2+b(z)u+c(z)=0,
\]
\[
\begin{aligned}
a(z)&=100z^4-840z^3+3741z^2-6867z+3978,\\
b(z)&=-408z^4-2916z^3+8766z^2+3105z-12474,\\
c(z)&=2412z^4-5724z^3+891z^2+3402z.
\end{aligned}
\tag{4}
\]

Its discriminant is exactly

\[
b(z)^2-4a(z)c(z)=-567(z-2)^2(2z-3)^2\mathcal P(z),
\tag{5}
\]

where \(\mathcal P\) is (1). The same quartic therefore emerges from two formulations. The other factors are retained in the [full symbolic output](balanced-path-polynomial.json); ignoring their physical branches is not used to prove global exclusion.

At \(z=z_*\), choose \(u=-b(z_*)/[2a(z_*)]\), then (3) defines \(v,A,B\). Let

\[
U=C(C')^{-1},\qquad S=\operatorname{diag}(I_2,U),\qquad
Q_*=S^{-1}Q(z_*)S.
\tag{6}
\]

These are exact definitions over the real number field \(\mathbb Q(z_*)\). The [exact certificate](check_balanced_fold.py) verifies that every displayed denominator and determinant is nonzero, \(U\mathbf1=\mathbf1\), all row sums vanish, every positive edge is reciprocated, and the support is precisely the claimed path. No rounding or rate clipping is used. For orientation only, its generator is approximately

\[
Q_*\simeq\begin{pmatrix}
-11&1&0&1.86553087&8.13446913\\
2&-20&6.92248992&0&11.07751008\\
0&6.22824145&-11.27299011&5.04474866&0\\
2.77737298&0&3.73491843&-6.73129745&0.21900604\\
10.48328058&10.38263173&0&0.24409946&-21.11001177
\end{pmatrix}.
\]

Use (3)–(6) or the exact coefficient representation in [balanced-fold-checks.json](../outputs/balanced-fold-checks.json), not the rounded matrix, for reproduction. Its seven undirected edges make the full graph irreducible. The source has six edges, so these cannot be hidden relabelings of one generator.

Normalized hidden similarity preserves all-time kernels directly. A separate exact check verifies marked-kernel derivatives of orders 0 through 9; the accepted Cayley–Hamilton certificate then independently confirms equality for every time. Exact normalized stationary laws and their similarity relation are checked too. Full minimality is inherited from the source kernel, not guessed from numerical ranks.

## Entropy separation is rigorously bounded

The checker performs number-field operations using SymPy's algebraic field, but **does not use its `is_positive` method to order the chosen real root**. In the installed version that method tests the leading coefficient, which is insufficient for the real embedding. Instead the quartic's positive root is isolated in an exact rational interval of width below \(10^{-35}\); each reduced field element is a degree-at-most-three polynomial, evaluated with exact rational interval bounds. This establishes all physical signs and provides enclosing intervals for stationary currents and flux ratios.

For each positive rational endpoint of a logarithm interval, powers-of-two range reduction brings the argument to \([1,2]\). For \(t=(x-1)/(x+1)\in[0,1/3]\), the checker uses

\[
\log x=2\sum_{j=0}^{n-1}\frac{t^{2j+1}}{2j+1}+R_n,\qquad
0\le R_n\le\frac{2t^{2n+1}}{(2n+1)(1-t^2)},\quad n=24.
\]

All interval operations, including negative currents and negative powers-of-two log shifts, use outward exact rational bounds. These yield (2) and

\[
0.002633285729\le\sigma(Q_*)-\sigma(Q(z_*))\le0.002633285730.
\]

Thus the sign is not inferred from limited precision. Independent 60/100-digit evaluations agree, and NumPy stationary solves plus independent matrix-exponential comparisons at five times check orientation and numerical consistency. Those latter computations are diagnostic; the exact equalities and rational remainder bounds certify the claims.

## Falsification history, reproducibility and limits

The initial conjecture that the known first-order threshold \(z_c=(11+\sqrt{1120/11})/2\) was globally sharp was false. The [independent rational witness](balanced-boundary-witness.md) proves complete realizations throughout \([10.545,10.5455]\), crossing that threshold. A second-order local expansion explains why the first-order obstruction fails. Unsuccessful larger perturbation steps are preserved there.

The new [bounded SLSQP probe](probe_balanced_boundary.py), with seed 20260910, ran 26 starts/settings combinations and maximized z for complete-support candidates. Five returned candidates meeting the explicit positivity filter; the best was approximately 10.557134405 with minimum rate near \(10^{-7}\), close to but below (1). The output retains failures, warnings, matrices, condition numbers and bounds. This suggests the limiting support; it proves neither nonexistence nor the boundary value. The exact path factorization and global envelope supersede that numerical lead.

From repository root:

```powershell
.\.venv\Scripts\python.exe -B analysis/probe_balanced_boundary.py
.\.venv\Scripts\python.exe -B analysis/derive_balanced_path.py
.\.venv\Scripts\python.exe -B analysis/check_balanced_boundary_witness.py
.\.venv\Scripts\python.exe -B analysis/check_balanced_cone_bound.py
.\.venv\Scripts\python.exe -B analysis/check_balanced_cone_sufficiency.py
.\.venv\Scripts\python.exe -B analysis/check_balanced_fold.py
```

Scripts preserve inputs, versions, exact commands, source hashes and corresponding outputs. The discovery run is optional for rechecking the proof; deterministic certificates suffice. There is no external dataset. Existing scientific scripts and their outputs were not overwritten. The general five/six-state classification, finite-data robustness, two-parameter boundary and literature novelty are not resolved here. No Lean check or general quantifier-elimination result is claimed.
