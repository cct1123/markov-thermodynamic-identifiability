# A complete realization across the balanced local-opening boundary

Date: 2026-09-10 UTC. Bounded independent contribution to the saved balanced-theta feasibility action. No literature or novelty claim. This note does not assign evidence IDs or alter the project state.

**Result:** the endpoint of the previously proved strict first-order opening region is not a global connected-hidden feasibility boundary. A fixed rational normalized hidden similarity produces a complete five-state generator for every

\[
\frac{2109}{200}\le z\le\frac{21091}{2000},
\qquad\text{i.e.}\qquad 10.545\le z\le10.5455.
\]

This interval contains

\[
z_c=\frac{11+\sqrt{1120/11}}2
=\frac{11}{2}+\frac{2\sqrt{770}}{11}
\simeq10.54524979109513.
\]

The realizations preserve the entire marked waiting kernel exactly. They have all 20 off-diagonal rates strictly positive, so every hidden graph is a triangle. The accepted adjacent-pair boundary theorem therefore gives unbounded entropy at these parameters. This contribution proves existence on this small interval; it does not locate the sharp upper feasibility threshold.

Mathematical status: **counterexample** to treating the strict first-order threshold as a global exclusion; **conventionally proved existence interval**, supported by executed exact arithmetic. Neither solver certification nor formal verification is claimed.

## Assumptions and falsification condition

The source is the displayed theta family in [the construction audit](theta-family-construction-audit.md), state order \((x,y,h,k,l)\):

\[
Q(z)=\begin{pmatrix}
-11&1&2&0&8\\2&-20&0&7&11\\3&0&-7&4&0\\
0&6&5&-11&0\\z&z&0&0&-2z
\end{pmatrix}.
\]

The admissible class is finite, irreducible, simple bidirected CTMCs on at most five states, with known visible endpoints and only the resolved reverse pair \(x\leftrightarrow y\) observed. The observations are the complete joint next-mark/time kernels, not selected moments or sampled times. Rates use the same arbitrary inverse-time unit as the source. Similarity matrices may have signed entries; physical rates may not.

The bounded falsification target was: **does there exist a compatible five-state generator with connected bidirected hidden graph at \(z=z_c\), or just above it?** A successful witness must have exact zero row sums, exact fixed observed rates/visible block, exact all-time kernel equality, an invertible normalized hidden similarity, and positive reciprocal rates on its claimed support. For the stronger complete-support target, the objective gap is the minimum over all 20 off-diagonal rates; it must be proved strictly positive, not merely exceed a floating-point tolerance. No approximate-data witness is promoted to exact evidence.

The tools are small matrix algebra, Fraction arithmetic and a separate SymPy polynomial identity. No global optimizer, graph enumerator, SMT query or formal prover is needed for this witness.

## Exact rational witness and interval proof

Set

\[
U=\begin{pmatrix}
31297248897/31250000000&-176804231/50000000000&506029979/250000000000\\
220129579/62500000000&7792751537/7812500000&-99427/100000000\\
-70035349/31250000000&176854731/200000000000&1001356857513/1000000000000
\end{pmatrix}.
\]

Every row sums to one and

\[
\det U=\frac{62522105533100116406027}{62500000000000000000000}>0.
\]

For \(T=\operatorname{diag}(I_2,U)\), define

\[
Q'(z)=T^{-1}Q(z)T.
\]

The [executed exact checker](check_balanced_boundary_witness.py) verifies both inverse identities, every row sum, the unchanged visible block, and strict positivity of every off-diagonal at both rational endpoints. The [complete output](../outputs/balanced-boundary-witness.json) stores the two full rational generators and stationary laws. The minimum off-diagonal rate is approximately \(1.73341440\times10^{-6}\) at the lower endpoint and \(1.16080342\times10^{-6}\) at the upper endpoint; these are display approximations to checked strictly positive rationals, not feasibility tolerances. At the upper endpoint the exact minimum is

\[
Q'_{kl}=\frac{18143968551777818701787225691597}
{15630526383275029101506750000000000000}>0.
\]

Because \(T\) is fixed and \(Q(z)\) is affine in \(z\), every rate of \(Q'(z)\) is affine in \(z\). Strict positivity at the two endpoints proves strict positivity on the whole closed interval, with no sampling gap. The exact squared comparison

\[
0<2(2109/200)-11,
\qquad
\big(2(2109/200)-11\big)^2
<1120/11<
\big(2(21091/2000)-11\big)^2
\]

places \(z_c\) strictly inside it. Normalization and invertibility hold throughout since \(U\) does not vary.

Partition the source into \((A,X;Y,H)\). Then

\[
A'=A,\quad X'=XU,\quad Y'=U^{-1}Y,\quad H'=U^{-1}HU,
\]

so the full rational hidden transfer is identical:

\[
X'(\lambda I-H')^{-1}Y'=X(\lambda I-H)^{-1}Y.
\]

The identity holds whenever the resolvents exist and hence as an identity of rational functions. The visible resolvent follows by the Schur complement. Subtracting the same observed-edge matrix from the unchanged \(A\) gives the same killed visible resolvent, proving equality of the complete next-mark/time kernels. This is the observation-preserving argument of [the construction audit, Section 1](theta-family-construction-audit.md#1-hidden-transfer-and-the-exact-residues).

As a separate algebraic check, SymPy constructs the two endpoint hidden resolvents through determinant and adjugate, compares their common cubic denominator and all four numerator polynomials exactly, and writes those polynomials to the output. This does not rely on the Fraction inverse implementation. Both checks share the source matrices and standard rational arithmetic, so they are complementary implementations, not independent empirical evidence.

Exact stationary solves additionally verify \(\pi' Q'=0\), normalization, positivity, and \(\pi'=\pi T\) at both endpoints. These are consistency checks; complete support already implies irreducibility and stationary uniqueness. No clipping, reverse-rate epsilon, altered observed data, or state splitting is used.

## Why the first-order threshold can be crossed

Put \(M=4\sqrt{770}/11\), \(a=z_c=(M+11)/2\). Specify the off-diagonal entries of a row-sum-zero hidden velocity \(K\), in order \((hk,hl,kh,kl,lh,lk)\), by

\[
K_{\mathrm{off}}=(-aM/30,\ M/5,\ a/3,\ -1,\ -7a/33,\ aM/120).
\]

Set each diagonal to minus its off-diagonal row sum. The two originally missing rates \(hl,lh\) have strictly positive first-order coefficients, approximately \(24.4360360\) and \(27.0850140\). The other six originally missing rates, in order \((xk,yh,hy,kx,kl,lk)\), have exactly zero first-order coefficients.

For those six rows the derivative matrix has rank five and a strictly positive left-null vector

\[
c=(\sqrt{770}/22,\ 4/11,\ \sqrt{770}/66,\ 28/33,
14/33+\sqrt{770}/60,\ 1)^T.
\]

Consequently no velocity makes these six first-order coefficients all strictly positive. That fact is only a first-order obstruction.

Choose a second-order correction \(L\), again normalized by zero row sums, with

\[
L_{\mathrm{off}}=(1081/100,\ 301/50,\ 699/100,\ 573/100,
-213/50,\ -49/20).
\]

Writing the hidden embeddings as \(\widehat K,\widehat L\), expansion of
\(T_\epsilon^{-1}QT_\epsilon\), where
\(U_\epsilon=I+\epsilon K+\epsilon^2L\), gives

\[
Q+\epsilon[Q,\widehat K]
+\epsilon^2\big([Q,\widehat L]-\widehat K[Q,\widehat K]\big)
+O(\epsilon^3).
\]

The six second-order coefficients are strictly positive; their approximate values are
\((2.02,2.07,2.05486510,2.00599097,2.02386133,2.03660933)\).
The output preserves each exact value in \(\mathbb Q(\sqrt{770})\), together with a strictly positive rational lower bound obtained from the verified enclosure

\[
27748873851023/10^{12}<\sqrt{770}
<27748873851024/10^{12}.
\]

For diagnostic interpretation, the positive weighted second-order contribution before adding \(L\) is

\[
c^T\big(-\widehat K[Q,\widehat K]\big)_{\mathrm{active}}
=2077\sqrt{770}/11979+8869/1815>0.
\]

Thus all eight originally missing rates open for sufficiently small positive \(\epsilon\): two at order \(\epsilon\), six at order \(\epsilon^2\). Existing rates remain positive and \(U_\epsilon\) remains invertible by continuity. This is an analytic local opening at the exact first-order boundary. The displayed rational \(U\) was obtained by rounding the off-diagonal entries of this curve at \(\epsilon=1/1000\) to denominator \(10^{12}\) and setting diagonals from normalization; **its subsequent exact checks, not the rounding, establish admissibility**.

## Entropy implication, failed attempts and limits

The complete hidden triangle contains adjacent hidden external twins. The boundary theorem in [hidden-pair-boundary-audit.md](hidden-pair-boundary-audit.md), also invoked in [the theta construction audit](theta-family-construction-audit.md), applies to these exact complete realizations and proves an unbounded entropy fiber. No entropy inference is made merely from generator nonuniqueness or a large numerical value.

Exploration of the unrounded local curve with \(\epsilon=1/100,1/50,1/20\) produced negative off-diagonal rates (approximately \(-0.00017895,-0.00243929,-0.05684530\)). These unsuccessful step choices show that the useful neighborhood is small; they are not evidence against another realization. The first checker run also failed because it compared unsimplified symbolic expression trees with zero. It was corrected to simplify each exact residual; the candidate and the mathematical statement did not change. The successful output retains these failures.

No rates or topologies beyond this construction were exhausted. In particular, reciprocal zero-rate boundary strata, hidden paths, distant components and the sharp upper parameter boundary remain outside this subtask. Failure of any attempted continuation would not prove exclusion. The parent investigation independently addresses the larger balanced-parameter interval.

## Reproduction

Run from the repository root:

```powershell
.\.venv\Scripts\python.exe -B analysis/check_balanced_boundary_witness.py
```

The run passed with Python 3.9.12 and SymPy 1.14.0. The JSON records execution time, dependency versions, exact command, source hashes, topology/observation assumptions, all exact matrices and check outcomes. There are no stochastic inputs, optimizer settings or feasibility tolerances. The resolved installed packages are retained in [balanced-boundary-environment.txt](../outputs/balanced-boundary-environment.txt). The source inputs are the existing construction audit and spectral audit; those artifacts are unchanged.

## Independent review of the subsequent sharp cone bound

After the witness above was complete, the coordinator requested an independent review of [balanced-cone-bound.md](balanced-cone-bound.md), Sections 1–5. This is a later bounded assignment; it does not change the witness or its accepted checker. The cone note and this review share the existing modal reduction and theta inputs.

The geometric inequality chain passes review. In particular:

- The inherited two-positive/one-negative vertex classification covers every connected three-hidden-state realization, including a path with paired missing edges. The old negative-bottom bound excludes `d<0` already for `z>=10`.
- The bottom-coordinate inequality follows from `c(aQ-W)<=kdQ`, `c>=1` and `aQ-W>0`; using `Q>=A` gives the stated upper bound on `epsilon=1-d`. Its application of the right wedge face is justified by the separately checked apex inequality.
- Maximizing the left vertex uses strict increases in both `P` and `ell`, with `Q>P`; the unique line/concave-curve intersection gives a genuine upper bound. It does not assume the relaxed triangle remains physical.
- The right linear bound and decreasing hyperbolic bound meet strictly beyond their pole. If `c*<1`, the hyperbolic bound at one is below `A`, contradicting necessary `Q>=A`. On the feasible branch the containment height increases before their meeting and decreases after it.
- Increasing `W` raises `t` and `Q*` and lowers `r=c*/Q*`. The height's derivative in `r` has the sign of `Lt-Q*<0`. During this increase `c*` also increases, so `c*>=1` and hence `Q*>=A` remain valid. This closes a potentially consequential monotonicity-domain concern.
- At the quartic root, equality of the full chain forces every stated face/tangency condition. The resulting triangle has at most one set of vertices, and the unique row-normalizing positive scaling eliminates apparent additional generators from cone-column scalings. Permuting hidden labels is the remaining equivalence. The equalities alone do not establish existence or positivity of all other rates; the parent must check its physical boundary witness separately.

Independent exact calculations reproduced the generic envelope identity, its theta-specialized constant coefficient, the discriminant factorization, and the signs isolating the positive quartic root. Each polynomial residual was exactly zero. The isolating endpoints were `10.55714966866` and `10.55714966867`, with negative and positive quartic values respectively. Values approximately `f1=5.49650870504`, `f2=-14.4989170901` were inspected only as a diagnostic; the contributor's dedicated interval checker supplies rigorous sign certification over the root interval.

An initial direct nested rational-function simplification was manually stopped without a result after it proved inefficient. Rewriting the rational expressions over explicit common denominators reduced the verification to a polynomial expansion that completed in about one second. The incomplete simplification is not contrary evidence and does not enter the conclusion. The contributor independently made the same algebraic simplification; this is implementation agreement, not independent scientific evidence.

The compact calculation below preserves the independently executed check. It uses only SymPy and exact algebra. Execute the fenced block directly in the same Python environment; there are no stochastic inputs or tolerances.

```python
import sympy as s
A,k,m,L,R,t=s.symbols('A k m L R t')
a=k-1; J=a*m+k
D=R*m+(k*L+R)*t; E=L*t*(J+a*t)
HN=t*(L*m*a*E*(A*D+R*E)+(A*D+(R+L*k)*E)*(A*D+(R-A)*E))
HD=E*(a*(m+t)*(A*D+R*E)+k*(A*D+(R-A)*E))
fL=A*R*m+(A*(R+L*k-L*a*m)+L**2*J**2+L*R*J)*t+a*(L**2*J+L*R-A*(L+L**2*k/R))*t*t
assert s.Poly(s.expand(R*(L*HN*(J+a*t)**2-HD*fL)),A,k,m,L,R,t).is_zero
z=s.symbols('z'); rho=s.sqrt(6)
L=(3-rho/2)/8; R=35*rho/88; m=(7+2*rho)/5
A=z; B=5*z/(4*(rho-1)); k=(2*z-9+2*rho)/(4*rho)
a=k-1; J=a*m+k
f0=A*R*m/L-B*J**2
f1=A*(R/L+k-a*m)+L*J**2+R*J-2*B*J*a
f2=a*(L*J+R-A*(1+L*k/R)-B*a)
P=352*z**4-3168*z**3-4644*z**2-11340*z-7623
assert s.simplify(f0+(19+9*rho)/100*z*(z*z-11*z+s.Rational(211,44))) == 0
assert s.simplify(s.expand(f1*f1-4*f0*f2)+(s.Rational(11,1200)+11*rho/4200)*(z+s.Rational(19,22))**2*P/352) == 0
assert P.subs(z,s.Rational(1055714966866,10**11)) < 0
assert P.subs(z,s.Rational(1055714966867,10**11)) > 0
print('PASS: independent envelope, theta coefficients, discriminant and root signs')
```

## Independent audit and replay of the physical fold certificate

The coordinator then requested review of [check_balanced_fold.py](check_balanced_fold.py) and its [accepted output](../outputs/balanced-fold-checks.json). The code was read in full and replayed successfully in the existing environment. To preserve the accepted output, the replay changed only the output destination literal from `outputs/balanced-fold-checks.json` to [outputs/balanced-fold-independent-replay.json](../outputs/balanced-fold-independent-replay.json) in memory before execution. No source file was edited. The source hashes, exact source/target/similarity matrices, stationary laws, support, entropy enclosures and numerical cross-checks agree with the original certificate. This replay is reproducibility evidence from the same algorithm; the independent contribution is the following mathematical/code audit.

- The polynomial has exactly one negative and one positive real root; the selected positive root is enclosed using rational isolation and exact polynomial signs. Field elements are evaluated as polynomials on that positive rational interval. Coefficient signs are handled by interval multiplication, so cancellation and the selected real embedding are respected. No incorrect `AlgebraicField.is_positive` convention enters this run.
- Every inversion and division occurs in the exact number field and therefore rejects a zero denominator. Every remaining rate has a rigorous interval sign, and all missing edges are exact paired zeros. The asserted support is connected with hidden path `2-3-4`. Normalization, stationarity, positive stationary masses and the visible block are checked exactly. The source remains minimal at this parameter because its three hidden poles are distinct with nonzero residues, as in the inherited spectral audit.
- The marked reset rows and exit columns match the ordered observed pair `x->y`, `y->x`. Exact equality of derivatives of orders zero through nine is consistent with the dimension-five realization certificate. More directly, the displayed normalized hidden similarity commutes with subtracting the observed-edge matrix; hence the killed generators are similar with the visible reset/output coordinates fixed. This proves all-time equality without depending on sampled times or a finite tolerance.
- The logarithm enclosure uses `log(x)=2*atanh((x-1)/(x+1))` after exact powers-of-two reduction to `[1,2]`. The omitted positive terms have denominators at least the first omitted odd denominator and a geometric ratio bounded by `1/9`, justifying the displayed rational tail bound. Negative powers of two are handled by full interval multiplication. Monotonic logarithm bounds for the flux ratio, interval multiplication by the signed current, and summation over unordered edges enclose the entropy with the correct convention and no missing factor of two.

The replay returned rigorous enclosures

\[
\sigma_{\rm source}\in[0.062946400236,0.062946400237],\qquad
\sigma_{\rm path}\in[0.065579685966,0.065579685967],
\]

and

\[
\sigma_{\rm path}-\sigma_{\rm source}
\in[0.002633285729,0.002633285730].
\]

The decimal endpoints are exact outward-rounded rationals in inverse-time units with Boltzmann's constant one. No issue was found in the sign, logarithm, support or observation checks. Combining this existence and entropy-separation certificate with the independently reviewed at-most-one connected equality classification and the accepted reducible-hidden rigidity yields exactly two generator classes and two entropy values at the fold, subject to those explicitly shared analytic dependencies. Publication novelty and the rest of the five-state classification are not assessed here.
