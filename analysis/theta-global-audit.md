# A locally isolated five-state generator with distant unbounded alternatives

Date: 2026-09-10 UTC; checkpoint 06:22 UTC. Contribution: analytic audit and executed exact calculations. Scope: one observed resolved pair x↔y, complete joint waiting kernels, bidirected irreducible CTMCs, and a five-state cap. Hidden labels are immaterial. This note establishes a counterexample to using local isolation as a global thermodynamic-identifiability test; it does not classify other five-state kernels or claim novelty.

## Outcome and input

For state order `(x,y,h,k,l)`, let

\[
Q=\begin{pmatrix}
-11&1&2&0&8\\
2&-20&0&7&11\\
3&0&-7&4&0\\
0&6&5&-11&0\\
3&3&0&0&-6
\end{pmatrix}.
\]

Its kernel has linear dimension five. This generator is isolated in the full compatible generator set, including against nearby topology changes. Nevertheless, its kernel admits a distant complete positive generator and an explicit family with entropy tending to infinity. Thus the compatible generator set is disconnected. No disconnectedness claim is made for its image under the entropy functional.

The root agent found the distant model using a bounded 13-start SLSQP diagnostic and proposed rational rounding. The audit below independently checked the resulting rational similarity and boundary using exact fractions. Discovery by numerical search is separate from the exact certificate.

## 1. The local certificate is valid, with a limited conclusion

Use the six row-normalized hidden similarity directions `(h,k),(h,l),(k,h),(k,l),(l,h),(l,k)`, whose corresponding diagonal entries are minus their offdiagonal entries. For `U=I+εK`, the generator velocity is `QK−KQ`, with K zero on visible coordinates.

Order the originally missing directed rates as

\[
(x,k),(y,h),(h,y),(h,l),(k,x),(k,l),(l,h),(l,k).
\]

Their first-order coefficient matrix is

\[
L=\begin{pmatrix}
2&0&0&0&0&8\\
0&0&7&0&11&0\\
-6&-3&0&0&0&0\\
0&-1&0&4&0&0\\
0&0&-3&-3&0&0\\
0&5&0&-5&0&0\\
0&0&0&0&1&-5\\
0&0&0&0&-4&5
\end{pmatrix}.
\]

Exact row reduction gives rank six. The strictly positive vector

\[
w=(3,1,1,10/3,7/3,19/15,151/15,79/15)
\]

satisfies `wL=0`. Hence `Lv≥0` forces `Lv=0`, and then `v=0`.

This does imply local isolation, rather than merely the failure of a particular direction search. If distinct feasible normalized similarities approached identity, normalize their six-coordinate differences and take a convergent subsequence on the unit sphere. Taylor expansion of the missing-rate inequalities would produce a nonzero vector with `Lv≥0`, a contradiction. Nearby original positive rates impose no additional first-order restriction.

Isolation also holds in generator space. Write Q in visible/hidden blocks `(A,X;Y,H)` and define

\[
C=[Y,1]=\begin{pmatrix}3&0&1\\0&6&1\\3&3&1\end{pmatrix}.
\]

For every compatible minimal realization, `C'=[Y',1]=U⁻¹C`, so `U=C(C')⁻¹`. Since C is nonsingular, convergence `Q'→Q` forces `U→I`. A distant similarity cannot secretly approach Q through an unbounded coordinate change.

The isolated generator is a relatively open and closed singleton of the labeled compatibility set. After quotienting by hidden labels, its finite permutation orbit still gives an isolated class. The distant complete model below lies outside that class. This argument says nothing about the entropy values of other components before they are analyzed.

## 2. A rational distant positive realization

Set

\[
U_*=\frac1{1000}\begin{pmatrix}
871&-390&519\\623&790&-413\\-183&133&1050
\end{pmatrix},\qquad S_*=\operatorname{diag}(I_2,U_*),
\qquad Q_*=S_*^{-1}QS_*.
\]

Rows of U* sum to one and `det U*=34813/31250`. All twenty offdiagonal entries of Q* are strictly positive; their minimum is `139/500`, attained at `x→h`. Its stationary vector is

\[
\pi_*=
\left(\frac{1065}{5914},\frac{333}{2957},
\frac{680723}{5914000},\frac{601833}{5914000},
\frac{725111}{1478500}\right).
\]

The original stationary vector is

\[
\pi=\frac1{5914}(1065,666,820,722,2641),\qquad \pi_* = \pi S_*.
\]

Exact checks establish both controllability/observability ranks `(5,5)` and equality of all kernel derivatives of orders 0–9. The [minimal compatibility theorem](compatibility-orbit.md) gives all-time equality directly from the normalized hidden similarity; the finite derivative certificate independently confirms it. Five-state minimality excludes all smaller competing models under the cap.

The rational construction, rather than its rounded floating approximation, is the witness. Negative entries of U* are allowed: physical positivity constrains Q*, not the similarity matrix itself.

## 3. Explicit divergent entropy family in the distant component

In Q*, mix states `k,l` (zero-based indices 3,4), using a second hidden similarity whose corresponding 2×2 block is

\[
W_t=\begin{pmatrix}1-t&t\\0&1\end{pmatrix},
\qquad Q_t=W_t^{-1}Q_*W_t,
\]

with identity on the other coordinates. For every external state `i∉{k,l}`,

\[
(Q_t)_{ki}=\frac{(Q_*)_{ki}-t(Q_*)_{li}}{1-t},\quad
(Q_t)_{ik}=(1-t)(Q_*)_{ik},\quad
(Q_t)_{il}=(Q_*)_{il}+t(Q_*)_{ik},\quad
(Q_t)_{li}=(Q_*)_{li}.
\]

The minimum external rate ratio occurs uniquely at `i=x`:

\[
r=\min_{i\notin\{k,l\}}\frac{(Q_*)_{ki}}{(Q_*)_{li}}
=\frac{104489}{1158489}<1.
\]

The other ratios, at `y,h`, are `1351057/421057` and `313949889/313515889`. The internal `k→l` numerator is

\[
f(t)=(Q_*)_{kl}+t[(Q_*)_{kk}-(Q_*)_{ll}]-t^2(Q_*)_{lk}.
\]

It is concave, with `f(0)>0` and

\[
f(r)=\frac{6376107122347}{1342096763121}>0.
\]

Consequently all offdiagonal rates remain strictly positive for `0≤t<r`. At `t=r`, exactly `k→x` vanishes; all other offdiagonals and every stationary probability have positive limits. The limiting generator remains irreducible, though it is no longer bidirected and is not a member of the admissible class.

Stationarity transforms as `π_t=π_*W_t`. The reverse stationary flux at the disappearing edge tends to

\[
c=(\pi_*)_x(1-r)(Q_*)_{xk}
=\frac{53132140}{1141883991}>0.
\]

Only that edge contribution diverges, and the rate tending to zero is linear in `r−t`. Thus, with `k_B=1`,

\[
\sigma(Q_t)=c\log\frac1{r-t}+O(1)\longrightarrow\infty.
\]

All members of this family have the original exact kernels and linear dimension five. Therefore the entropy fiber of the locally isolated original model is unbounded under the same five-state cap.

## 4. Exact global coordinates for future inverse-realization work

Using the nonsingular exit chart \(C\) from Section 1, compute

\[
D=C^{-1}HC=\begin{pmatrix}-10&2&-1\\1&-14&-1\\9&18&0\end{pmatrix},
\qquad XC=\begin{pmatrix}30&24&10\\33&75&18\end{pmatrix}=:B.
\]

Every compatible realization corresponds to three noncollinear exit-rate points `p_i=(u_i,v_i)`, with rows of C' equal to `(u_i,v_i,1)`. Conversely, any such C' gives

\[
U=C(C')^{-1},\quad Y'=C'_{:,1:2},\quad
H'=C'D(C')^{-1},\quad X'=B(C')^{-1}.
\]

These formulas exhaust the normalized hidden similarity class; U is automatically invertible and row-normalized. Physical feasibility remains essential.

The entrance inequalities `X'≥0` mean that the triangle with vertices p_i contains the two fixed points

\[
b_x=(3,12/5),\qquad b_y=(11/6,25/6),
\]

because rows of X' have totals 10 and 18. Exit positivity means the vertices lie in the nonnegative quadrant. For internal rates define

\[
g(u,v)=\big(u^2+uv-10u+v+9,\ uv+v^2+2u-14v+18\big).
\]

The generator identities yield, at each vertex,

\[
g(p_i)=\sum_{j\ne i}H'_{ij}(p_j-p_i).
\]

The two edge directions from a vertex are linearly independent, so the internal nonnegativity inequalities are exactly the requirement that g(p_i) lie in their nonnegative cone. One must also impose reciprocal support: `X'_{xi}>0` iff `u_i>0`, `X'_{yi}>0` iff `v_i>0`, and `H'_{ij}>0` iff `H'_{ji}>0`; zeros occur in pairs. Full graph connectivity is a separate requirement. Subject to these conditions the displayed formulas give precisely the admissible fiber.

The original triangle has vertices `(3,0),(0,6),(3,3)`. The positive witness triangle has vertices

\[
\left(\frac{1906467}{1114016},\frac{1062171}{557008}\right),\quad
\left(\frac{313467}{1114016},\frac{4053171}{557008}\right),\quad
\left(\frac{3475467}{1114016},\frac{1263171}{557008}\right).
\]

Both anchor points are strictly interior to the latter triangle and all internal generator coefficients are positive. The coordinate description does not assert that straight interpolation between feasible triangles remains feasible. The coexistence of an isolated feasible triangle and a distant open feasible set is established by the exact certificates above.

## 5. Verification and provenance

The audit independently executed exact fraction calculations through the existing helpers, importing modules with bytecode writes disabled. It checked L and its positive dual, both realization ranks, the normalized similarity, all rate signs, stationary vectors, derivative orders 0–9, the three external ratios, f(r), the unique boundary zero, and the positive coefficient c. The consolidated reproducible witness is in [check_five_state_extensions.py](check_five_state_extensions.py) and [five-state-extension-checks.json](five-state-extension-checks.json).

The executed commands used Python 3.9.12, NumPy 2.0.1 and SciPy 1.13.1. The initial audit's `check_five_state_extensions.py` SHA-256 was `241cbf4ed18a0950de1cf000172bda0c1d84681db39c3a8b75396c1da6448d9b`; later checks extended that script. Current source and helper hashes are in [five-state-extension-checks.json](five-state-extension-checks.json), with maintenance changes recorded in [E044](../evidence/RECORDS.md#e044). An optional SymPy import was unavailable; the accepted audit calculations use fractions and the existing helpers.

For a standalone reproduction of the decisive construction and endpoint, from the repository root:

~~~powershell
$env:PYTHONDONTWRITEBYTECODE = '1'
@'
import sys
sys.path.insert(0, 'analysis')
import numpy as np
from fractions import Fraction as F
from check_five_state_extensions import inverse, matrix, theta, eye, ranks, derivatives
from check_four_state_classification import stationary
q = theta(3, 3)
u = matrix([[871,-390,519],[623,790,-413],[-183,133,1050]]) / F(1000)
s = eye(5); s[2:,2:] = u
qs = inverse(s) @ q @ s
pi = stationary(q) @ s
assert all(qs[i,j] > 0 for i in range(5) for j in range(5) if i != j)
assert min(qs[i,j] for i in range(5) for j in range(5) if i != j) == F(139,500)
assert ranks(q) == ranks(qs) == (5,5)
assert all(np.array_equal(a,b) for a,b in zip(derivatives(q,10), derivatives(qs,10)))
assert all(v > 0 for v in pi) and all(v == 0 for v in pi @ qs)
a,b = 3,4
r,j = min((qs[a,j]/qs[b,j],j) for j in range(5) if j not in (a,b))
assert (r,j) == (F(104489,1158489),0)
f = qs[a,b] + r*(qs[a,a]-qs[b,b]) - r*r*qs[b,a]
assert f == F(6376107122347,1342096763121)
w = eye(5); w[a,a] = 1-r; w[a,b] = r
qb = inverse(w) @ qs @ w
assert [(i,j) for i in range(5) for j in range(5) if i != j and qb[i,j] == 0] == [(3,0)]
assert all(qb[i,j] >= 0 for i in range(5) for j in range(5) if i != j)
assert all(v > 0 for v in pi @ w)
assert pi[0]*(1-r)*qs[0,3] == F(53132140,1141883991)
print('Exact distant realization and divergent endpoint certified.')
'@ | python -B -
~~~

The displayed command combines the independently executed checks without changing their inputs or formulas. The underlying all-time and divergence conclusions come from the analytic arguments, not approximate matching on a time grid. Publication novelty and a general five-state classification remain unestablished.
