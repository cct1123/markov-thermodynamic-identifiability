# Exact strata of the theta(a,b) family

Date: 2026-09-10 UTC. Contribution: bounded analytic audit and exact checks. Scope is the parameter family below, with `a,b>0`, full joint kernels of the resolved observed pair `x<->y`, and the repository's simple bidirected CTMC convention. This note does not enumerate topologies or classify all globally compatible models. No novelty claim is made.

## Result

The full marked realization is observable of dimension five for every positive parameter pair. It is controllable of dimension five except at the single point

\[
a_*=2\sqrt6-3,\qquad b_*=12-4\sqrt6,
\]

where controllability and the minimal linear realization dimension are four.

The exit-coordinate chart matrix `C=[Y,1]` is singular on the entire line `2a+b=6`. Except at the point above, that singularity is only a chart failure, not linear nonminimality. The hidden-eigenvalue coincidence lines are `a+b=9+-2sqrt(6)`. The fast coincidence never destroys minimality in the positive quadrant; the slow coincidence does so only at `(a_*,b_*)`.

There is also a global support obstruction: on the slow coincidence line, away from `(a_*,b_*)`, the dominant hidden-response residue has rank two. Hence no compatible representation can have an irreducible hidden block, including any complete positive representation. At the exceptional point the residue has rank one, and an explicit compatible complete four-state generator exists. Splitting one of its hidden states gives a complete five-state generator and unbounded entropy under the five-state cap at that point.

## 1. Blocks and the relevant rank tests

In order `(x,y,h,k,l)`, the generator is

\[
Q(a,b)=\begin{pmatrix}
-11&1&2&0&8\\
2&-20&0&7&11\\
3&0&-7&4&0\\
0&6&5&-11&0\\
a&b&0&0&-a-b
\end{pmatrix}.
\]

Put `t=a+b`. After the observed pair is killed, the visible block is `D=diag(-11,-20)` and

\[
X=\begin{pmatrix}2&0&8\\0&7&11\end{pmatrix},\qquad
Y=\begin{pmatrix}3&0\\0&6\\a&b\end{pmatrix},\qquad
H=\begin{pmatrix}-7&4&0\\5&-11&0\\0&0&-t\end{pmatrix}.
\]

Because the reset rows and absorption columns span both visible coordinates, full controllability is equivalent to controllability of `(H,Y)`, and full observability to observability of `(X,H)`. For example a left uncontrollable eigenvector of the full killed generator has zero visible part and a hidden part `w` with `wY=0` and `wH=lambda w`; the observability statement is dual. Equivalently the full reachable space consists of the visible plane plus the hidden span of `Y,HY,H^2Y,...`.

The two eigenvalues of the coupled hidden block correspond to the positive decay rates

\[
\lambda_-=9-2\sqrt6,\qquad\lambda_+=9+2\sqrt6.
\]

The third hidden eigenvalue is `-t`. These hidden-block coincidences must not be confused with repeated poles or rank loss of the complete marked realization.

## 2. Observability never fails

The two rows of `X` and the second row of `XH` give the minor

\[
\det\begin{pmatrix}
2&0&8\\0&7&11\\35&-77&-11t
\end{pmatrix}
=-14(11t+19)<0.
\]

Thus `(X,H)` is observable of hidden dimension three for every `t>0`; the full realization is observable of dimension five. This includes both hidden-eigenvalue coincidence lines and the whole exit-chart singular line.

## 3. Controllability fails at exactly one positive point

The matrix `Y` has rank two, and its left null space is spanned by

\[
w=(-2a,-b,6).
\]

The hidden reachable dimension is two exactly when this null line is left invariant under `H`; otherwise `HY` immediately adds a third independent direction. Since the last component of `w` is nonzero, invariance forces the eigenvalue to be `-t`. Direct multiplication gives the two conditions

\[
2a(t-7)+5b=0,\qquad 8a+b(t-11)=0.
\]

There is a useful normalization shortcut. Since `H1=-Y1`, `wY=0` and `wH=-tw` imply `tw1=0`. With `t>0`, this forces `w1=6-2a-b=0`. Hence any loss of controllability lies on the chart line. There, `a=6-t`, `b=2t-6`; the eigenvector conditions reduce to

\[
t^2-18t+57=0.
\]

Positivity on the chart line requires `3<t<6`, which selects only `t=lambda_-`. It gives exactly `(a_*,b_*)` above. The alternative root `lambda_+` makes `a<0` and is outside the parameter domain.

At the exceptional point the hidden reachable dimension is exactly two because `Y` already has rank two. Thus full controllability has rank four. Since full observability remains five, its restriction to the four-dimensional reachable space is observable, and the minimal input-output realization dimension is exactly four. At every other positive pair both full ranks are five.

## 4. Exit chart and coincidence strata

The chart matrix is

\[
C=[Y,1]=\begin{pmatrix}3&0&1\\0&6&1\\a&b&1\end{pmatrix},\qquad
\det C=3(6-2a-b).
\]

On the positive part of its singular line, the third visible-exit row is a convex combination of the first two:

\[
(a,b)=p(3,0)+(1-p)(0,6),\qquad p=a/3\in(0,1).
\]

This affine relation does not ordinarily define an invariant hidden direction. Only at `(a_*,b_*)` does it also align with a left eigenvector of the coupled hidden block.

| Parameter stratum | Full controllability | Full observability | Minimal linear dimension |
| --- | --- | --- | --- |
| Generic positive pair | 5 | 5 | 5 |
| `2a+b=6`, excluding `(a_*,b_*)` | 5 | 5 | 5 |
| `a+b=lambda_-`, excluding `(a_*,b_*)` | 5 | 5 | 5 |
| `a+b=lambda_+` | 5 | 5 | 5 |
| `(a_*,b_*)` | 4 | 5 | 4 |

In particular an exit-chart inverse is invalid along a one-dimensional set of fully minimal models. Neither that chart failure nor a repeated hidden eigenvalue alone licenses a dimension reduction.

## 5. A global obstruction on the slow coincidence line

The data determine the hidden response

\[
F(z)=X(zI-H)^{-1}Y.
\]

At `t=lambda_-`, its dominant pole `-lambda_-` has residue

\[
R_-=Z_-+\begin{pmatrix}8\\11\end{pmatrix}(a,b),\qquad
Z_-=
\frac1{4\sqrt6}\begin{pmatrix}
6(2+2\sqrt6)&48\\105&42(-2+2\sqrt6)
\end{pmatrix}.
\]

The first matrix is the positive rank-one Perron residue of the coupled two-state hidden block. The second is the singleton contribution. All entries of their sum are positive. On the coincidence line,

\[
\det R_-=
\left(135-\frac{41}{2}\sqrt6\right)
\left(a-(2\sqrt6-3)\right).
\]

Thus the dominant residue has rank two except at `(a_*,b_*)`, where it has rank one.

For any irreducible Metzler hidden block, the spectral-bound eigenvalue is simple with positive left and right eigenvectors. Its resolvent residue is rank one. If the hidden block communicates with both visible ports, multiplication by nonnegative entrance and exit matrices gives a nonzero positive rank-one dominant residue in `F`. A complete positive representation necessarily has these properties. Its Perron pole cannot be canceled, because its visible entrance/exit projections are strictly positive.

Consequently the rank-two dominant residue above rules out every representation with an irreducible hidden block. This obstruction is stronger than absence of a local support-opening direction and does not depend on the exit chart or on a minimal-similarity parameterization. In particular it rules out complete positive representations on the punctured slow-coincidence line, even if additional hidden states were considered.

No corresponding Perron obstruction follows merely from the fast coincidence: its repeated eigenvalue is not the spectral bound. Complete-positive feasibility elsewhere in the parameter plane remains unclassified here.

## 6. The exceptional point has a complete four-state realization

At `(a_*,b_*)`, put

\[
p=\frac{2\sqrt6-3}{3},\qquad q=1-p.
\]

The stochastic `5 x 4` link `L` fixes `x,y,h,k` and maps the last row to the mixture `(p,q)` of the two retained hidden coordinates. With

\[
H_0=\begin{pmatrix}-7&4\\5&-11\end{pmatrix},\qquad
Y_0=\begin{pmatrix}3&0\\0&6\end{pmatrix},\qquad
\overline X=\begin{pmatrix}2+8p&8q\\11p&7+11q\end{pmatrix},
\]

one has `(p,q)H_0=-lambda_-(p,q)` and `(p,q)Y_0=(a_*,b_*)`. Hence

\[
Q(a_*,b_*)L=L\overline Q,\qquad
\overline Q=\begin{pmatrix}A&\overline X\\Y_0&H_0\end{pmatrix},\quad
A=\begin{pmatrix}-11&1\\2&-20\end{pmatrix}.
\]

The observed endpoints are fixed by `L`, so the corresponding killed-generator intertwining proves equality of all observed kernels. This is a stochastic intertwining, not a deterministic state partition. The intermediate `Qbar` has one-way visible-hidden links; it is used only as an algebraic realization.

Now take

\[
V=\begin{pmatrix}9/10&1/10\\1/10&9/10\end{pmatrix},\qquad
S=\operatorname{diag}(I_2,V^{-1}).
\]

The generator `Q4=S^{-1} Qbar S` is

\[
Q_4=\begin{pmatrix}
-11&1&5/4+10p&35/4-10p\\
2&-20&(55p-9)/4&(81-55p)/4\\
27/10&3/5&-547/80&283/80\\
3/10&27/5&437/80&-893/80
\end{pmatrix}.
\]

All off-diagonal entries are strictly positive, its rows sum to zero, and it has the same full marked kernel. Its linear dimension is four, consistent with the exact rank loss above. This explicitly establishes a four-state **bidirected** compatible realization; the equality of linear and admissible realization order was not assumed.

The [state-splitting construction](state-splitting-audit.md) can now split either hidden state of this complete four-state model into two clones with positive entrance fractions and positive internal rates. All pairs remain positive, giving a complete five-state model. Taking one internal clone rate to zero with its reverse fixed yields unbounded entropy while preserving every observed kernel. Thus the exceptional point is feasible for a complete positive five-state representation and has unbounded entropy within the five-state cap.

## 7. Exact representative verification

The checks below use rational arithmetic in `Q(sqrt(6))`, represented by coefficient pairs, so no symbolic package is required. An initial import probe found SymPy unavailable; no SymPy computation was performed. The following compact coefficient calculation uses the existing rational matrix helpers and writes no files.

From the repository root:

~~~powershell
python -B -c "from pathlib import Path; exec(Path('analysis/theta-parameter-strata-audit.md').read_text(encoding='utf-8').split('# BEGIN STRATA CHECK' + chr(10),1)[1].split('# END STRATA CHECK',1)[0])"
~~~

~~~python
# BEGIN STRATA CHECK
import sys, json
from fractions import Fraction as F
sys.path.insert(0, 'analysis')
import numpy as np
from check_small_networks import matrix, eye, exact_rank

def pair(rows0, rows1=None):
    first = matrix(rows0)
    second = matrix(np.zeros(first.shape, dtype=int)) if rows1 is None else matrix(rows1)
    return first, second

def mul(a, b):
    return a[0]@b[0]+6*(a[1]@b[1]), a[0]@b[1]+a[1]@b[0]

def equal(a,b):
    return all(np.array_equal(x,y) for x,y in zip(a,b))

def field_rank(a):
    lift = np.block([[a[0],6*a[1]],[a[1],a[0]]])
    result = exact_rank(lift)
    assert result % 2 == 0
    return result//2

def theta(a,b):
    q = pair([[-11,1,2,0,8],[2,-20,0,7,11],[3,0,-7,4,0],
              [0,6,5,-11,0],[a[0],b[0],0,0,-a[0]-b[0]]])
    q[1][4,0], q[1][4,1], q[1][4,4] = a[1], b[1], -a[1]-b[1]
    return q

def ranks(q):
    n=len(q[0]); killed=(q[0].copy(),q[1].copy())
    killed[0][0,1]=killed[0][1,0]=F(0)
    r=pair(eye(n)[:2,:]); b=pair(eye(n)[:,:2]); power=pair(eye(n))
    obs=[]; con=[]
    for j in range(n):
        obs.append(mul(r,power)); con.append(mul(power,b)); power=mul(power,killed)
    return field_rank(tuple(np.hstack([c[i] for c in con]) for i in range(2))), field_rank(tuple(np.vstack([o[i] for o in obs]) for i in range(2)))

cases=[('generic',(1,0),(1,0)), ('singular_chart',(1,0),(4,0)),
       ('slow_coincidence',(1,0),(8,-2)), ('fast_coincidence',(1,0),(8,2)),
       ('rank_loss',(-3,2),(12,-4))]
results={name:ranks(theta(a,b)) for name,a,b in cases}
assert list(results.values())==[(5,5),(5,5),(5,5),(5,5),(4,5)]

l=pair([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,-1,2]],
       [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,F(2,3),F(-2,3)]])
bar=pair([[-11,1,-6,16],[2,-20,-11,29],[3,0,-7,4],[0,6,5,-11]],
         [[0,0,F(16,3),F(-16,3)],[0,0,F(22,3),F(-22,3)],[0,0,0,0],[0,0,0,0]])
q4=pair([[-11,1,F(-35,4),F(75,4)],[2,-20,-16,34],
         [F(27,10),F(3,5),F(-547,80),F(283,80)],
         [F(3,10),F(27,5),F(437,80),F(-893,80)]],
        [[0,0,F(20,3),F(-20,3)],[0,0,F(55,6),F(-55,6)],
         [0,0,0,0],[0,0,0,0]])
s=pair([[1,0,0,0],[0,1,0,0],[0,0,F(9,8),F(-1,8)],[0,0,F(-1,8),F(9,8)]])
assert equal(mul(theta((-3,2),(12,-4)),l),mul(l,bar))
assert equal(mul(bar,s),mul(s,q4))
assert all(sum(row)==0 for part in q4 for row in part)
for i in range(4):
    for j in range(4):
        if i!=j:
            # The strict rational bound 2<sqrt(6)<5/2 proves positivity.
            lower=q4[0][i,j]+q4[1][i,j]*(F(2) if q4[1][i,j]>=0 else F(5,2))
            assert lower>0
assert ranks(q4)==(4,4)
print(json.dumps({'theta_ranks_control_observe':results,'complete_q4_ranks':ranks(q4),
                  'exact_intertwining':True,'exact_complete_positivity':True},indent=2))
# END STRATA CHECK
~~~

Verification status: the embedded check executed successfully on 2026-09-10 at approximately 06:51 UTC, with Python 3.9.12 and NumPy 2.0.1. Exact control/observation ranks were `(5,5)` at the generic, chart-line, slow-coincidence and fast-coincidence representatives, `(4,5)` at the exceptional point, and `(4,4)` for the constructed complete four-state generator. Both intertwining identities and strict positivity of every four-state off-diagonal rate passed in exact arithmetic. The imported helper [check_small_networks.py](check_small_networks.py) had SHA-256 `9b1b1007d17fa3fa55e50cb94135067cfe02c31b3e63415e0ad7926b9d6e39c4`. The general strata and support obstruction are algebraic results above; these representative checks are not a parameter search.

## Limits

This audit identifies linear-rank and chart strata exactly and settles complete-positive impossibility on the punctured slow-coincidence line, with its constructive exceptional point. It does not determine complete-positive feasibility or entropy boundedness everywhere else in the `(a,b)` plane. In particular chart singularity, fast hidden-eigenvalue coincidence, and failure of a local opening test are not global infeasibility proofs.
