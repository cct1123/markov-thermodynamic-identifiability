# Independent audit of the supplied Laplace claims

Audit date: 19 September 2026 (UTC). **Judgment:** the supplied two-point leaf ambiguity and the two-point entropy-identification corollary are correct under the manuscript's stated model class. The existing manuscript already restricts the conclusion appropriately. An additional exact one-point entropy counterexample is recorded below; it does not require changing the manuscript for this bounded review.

Mathematical status: conventional derivation and executed exact symbolic/rational checks, not formal verification. No literature or novelty claim is made. This audit treats statements in supplied files as claims to check, not operating instructions.

## Scope and independent check

Sources read: [model and observation definitions](../../manuscript/main.tex), [two-point supplement](../../manuscript/supplementary/laplace-two.tex), [detailed prior proof](../../analysis/correctness/LAPLACE-TWO.md), [existing entropy tests](../../analysis/correctness/test_laplace_entropy.py), the supplied `two_laplace_counterexample (1).py`, and the Laplace sections of supplied `independent_checks (1).json`. The coordinating agent separately replays the supplied files and audits the JSON's other calculations.

The supplied source hashes are respectively `abfcf6c6a9b6bf80e7c34b78189b31d005b45bc383f27a2aa9a933b10ac260ed` and `ee63f11fb2f5103a8d367c1c7e7437b7fdd518e6ee7af84c87f867092f3ef97e`.

The independent [check script](laplace_scope_checks.py) imports no repository modules. It solves the backward first-step equations and stationary-flux equations, checks generic reconstruction, both symbolic leaf strata and the two-state stratum, and verifies two exact scope witnesses. [Executed output](laplace-scope-checks.json) records the command, source hash, versions and exact results. Python 3.9.12 and SymPy 1.14.0; no randomness, numerical tolerances or optimization. The independent implementation shares SymPy and the same mathematical first-step identities with prior checks, so agreement is not independent engine verification.

## Why the two-point inverse works

Use fixed endpoints `(x,y,h)`, physical time, one kinetic channel per ordered pair, connected reciprocal support, and observed rates `r,s>0`. Write

\[
Q=\begin{pmatrix}-r-a&r&a\\s&-s-c&c\\b&d&-b-d\end{pmatrix},\qquad h=b+d.
\]

The tuple order here is `(r,s,a,b,c,d)`. Remove the marked off-diagonals while retaining the generator diagonals. The first-step equations for the two next-mark tests give

\[
F=P\widehat\Psi=K\operatorname{diag}(r,s),\quad
K^{-1}=\operatorname{diag}(\lambda+r+a,\lambda+s+c)
-\frac{(a,c)^T(b,d)}{\lambda+h}.
\]

Here `P` swaps previous-mark rows into starting-state order. Thus the supplied diagonal matrices are **F**, whereas the manuscript's mark-ordered \(\widehat\Psi=PF\) is off-diagonal for a tree. The factors `r,s` are essential absolute joint amplitudes, not separately imposed calibrations.

The Schur matrix has nonpositive off-diagonals and row sums
\(\lambda+r+a\lambda/(\lambda+h)>0\) and
\(\lambda+s+c\lambda/(\lambda+h)>0\).
It is therefore strictly diagonally dominant and nonsingular for positive arguments. With \(M=F^{-1}\),

\[
M_{12}=-\frac{ad}{r(\lambda+h)},\quad
M_{21}=-\frac{cb}{s(\lambda+h)},\qquad
G=\frac{M\mathbf1-\mathbf1}{\lambda}
=\begin{pmatrix}1/r+a/[r(\lambda+h)]\\1/s+c/[s(\lambda+h)]\end{pmatrix}.
\]

For a complete triangle all six rates are positive. Clearing denominators between two arguments yields the independent equivalent inverse

\[
h=\frac{\lambda_2M_{12}(\lambda_2)-\lambda_1M_{12}(\lambda_1)}
{M_{12}(\lambda_1)-M_{12}(\lambda_2)}.
\]

Its denominator is nonzero because \(ad/r>0\) and \(\lambda_2>\lambda_1>0\). The two values of each `G` row then solve linearly for `u_i,v_i` in \(G_i=u_i+v_i/(\lambda+h)\), giving \(u=(1/r,1/s)\) and \(v=(a/r,c/s)\). Finally \(d=-M_{12}(\lambda_1)(\lambda_1+h)/v_x\), and \(b=h-d\). The script verifies these identities with generic positive symbols.

There is no equilibrium, equal-rate or repeated-eigenvalue exception: no step divides by current, affinity or an eigenvalue gap. All denominators are nonzero at each positive complete source; this establishes a rational, locally Lipschitz inverse on admissible nearby data. It gives no uniform conditioning guarantee as arguments merge, rates diverge or a hidden edge pair approaches zero.

## Support and entropy: the indispensable assumptions

In connected reciprocal three-state support with `x--y` present, the hidden state is attached either to both endpoints (complete triangle), only `x`, or only `y`. Reciprocity means `a>0 iff b>0` and `c>0 iff d>0`; consequently either inverse cross entry is nonzero exactly for the complete triangle. A two-state competitor has both cross entries zero. Equal complete-triangle data therefore force every competitor in the state cap into the same invertible class.

If both cross entries vanish, every compatible model in the cap is a tree or two-state chain. Remove any supported tree edge and sum stationarity over one resulting component. That edge is the sole crossing, so its stationary current vanishes. Every supported edge is balanced and network entropy is zero. The script independently checks both symbolic leaf orientations and the two-state model by solving stationarity. This covers the exceptional strata rather than extrapolating the positive-rate inverse through a zero denominator.

Reciprocity, irreducibility, the state cap, and exact joint amplitudes are consequential. Nonreciprocal competitors are outside the entropy convention and invalidate this support classification. A disconnected hidden component is outside the connected class. Normalizing each individual time density would remove information used by the inverse. Exact zeros here are not a rule for thresholding noisy data.

The cap cannot be dropped from the zero-pattern argument. For example,

\[
Q_4=\begin{pmatrix}-4&1&2&1\\1&-1&0&0\\1&0&-3&2\\2&0&1&-3\end{pmatrix}
\]

has connected reciprocal support, a marked bridge `x--y`, diagonal `F` at every positive argument, uniform stationary law and entropy \(3\log(2)/4>0\). Its unobserved three-edge cycle carries current. This is an exact counterexample to extending “zero cross entries imply zero entropy” beyond the cap, not a claim that this four-state model shares a three-state full law.

## The supplied leaf example and calibration

The supplied pair has `r=1` versus `6/5` and common `s=1`. Its two diagonal `F` values at arguments 1 and 2 translate to the manuscript's two off-diagonal \(\widehat\Psi\) values. Its distinct values at argument 3 preclude all-time observable equality. Every member is a reciprocal tree and has entropy zero, so it refutes two-point **generator** recovery without refuting two-point entropy identification.

The general positive leaf family is valid locally: `G_x=u+v/(lambda+b)` has three positive unknowns, and the two equations leave `b` variable with `u,v` positive on an open interval around the source. The other row is fixed by `s`. Fixing `r` at the attachment removes this freedom; fixing `s` alone does not. A known attachment rate permits recovery of `b` from the ratio of the two residuals `G_x-1/r`. Both observed rates known therefore cover either leaf orientation. A supplied absolute stationary event intensity or common trace also excludes this particular pair; normalized mark proportions do not. These are extra observations or constraints, not information silently present in the two matrices.

## Additional exact result: one argument can miss entropy

The prior one-point example uses equilibrium generators and correctly makes no entropy-necessity claim. A separate nonequilibrium witness is

\[
Q_A=\begin{pmatrix}-2&1&1\\1&-3&2\\1&1&-2\end{pmatrix},\qquad
Q_B=\begin{pmatrix}-14/11&9/11&5/11\\1&-13/3&10/3\\1&3&-4\end{pmatrix}.
\]

Both are complete reciprocal triangles, and the exact first-step solve gives

\[
F_A(1)=F_B(1)=\begin{pmatrix}5/13&1/26\\1/13&4/13\end{pmatrix}.
\]

Their stationary laws are
\(\pi_A=(1/3,1/4,5/12)\) and
\(\pi_B=(11/25,153/550,31/110)\).
Both cycles `x->y->h->x` have affinity `log(2)`, while their stationary currents are `1/12` and `9/110`. Direct edge-flux entropy and the cycle-current formula agree:

\[
\sigma_A=\frac{\log2}{12},\qquad
\sigma_B=\frac{9\log2}{110},\qquad
\sigma_A-\sigma_B=\frac{\log2}{660}>0.
\]

The full matrices differ at argument 2. For any prescribed \(\lambda_0>0\), multiplying both generators by \(\lambda_0\) gives the same witness at \(\lambda_0\), because \(\widehat\Psi_{cQ}(\lambda)=\widehat\Psi_Q(\lambda/c)\), with entropy multiplied by `c`. Hence two arguments are necessary as well as sufficient for entropy in the uncalibrated worst case. This additional result has conventional exact support; it is not a priority claim and has not been inserted into the manuscript.

## Project implication

The supplied claims support the already incorporated distinction between three-point worst-case generator recovery and two-point entropy recovery. They neither contradict full-law three-state identifiability nor establish entropy stability at tree boundaries. No defect in the audited support proof or inverse was found. The additional one-point witness can support a future minimality statement if desired, without affecting existing accepted results.
