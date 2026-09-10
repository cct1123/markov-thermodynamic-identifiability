# Hidden-pair mixing in an arbitrary finite network

Date: 2026-09-10 UTC. Contribution: analytic derivation, adversarial scope audit and selected exact checks below; no novelty claim. This generalizes the constructive lemma in [unknown-topology-audit.md](unknown-topology-audit.md) using the observation conventions and hidden similarities of [formulation.md](formulation.md) and [compatibility-orbit.md](compatibility-orbit.md). No state is added.

## Conclusions for the five-state search

The two-state mixing argument embeds in an arbitrary `N`-state network provided its incidence conditions include **every other state**, including other hidden states. Two fully hidden vertices are called *external twins* here when they have the same neighbors outside the pair. The pair itself may be joined or unjoined.

For a minimal kernel realization of dimension `N`:

- An adjacent pair of external twins forces unbounded entropy already at the **same dimension and fixed topology**.
- A nonadjacent twin pair does the same when its two total escape rates agree.
- Nonadjacent twins with unequal escape rates cannot be mixed nontrivially in isolation while retaining the absent pair edge. If topology is unknown, a small similarity opens that edge and gives an unbounded fiber at the same dimension.
- More generally, adjacent hidden vertices whose external neighborhoods are comparable by inclusion also force unboundedness when topology may change. For a nonadjacent strictly nested pair, write `h` for the vertex with the larger external neighborhood. The same conclusion holds if `lambda_h <= lambda_k`.

Incomparability of the neighborhoods, or the reverse escape ordering for an unjoined nested pair, obstructs **this isolated-pair method**. Neither is a uniqueness theorem for the entire hidden-similarity orbit. Mixing three or more hidden coordinates can escape constraints imposed when all other coordinates are fixed.

Thus a proposed bounded-but-nonunique minimal five-state example with one observed pair must survive these tests on each of its three hidden pairs. These are sufficient exclusion tests; they are not a complete five-state classification.

## 1. Embedded block and compatibility

Take two fully hidden states `h,k`, neither an endpoint of any observed mark, and let `W` contain all remaining `N-2` states. Order the generator as `(W,h,k)`:

\[
Q=\begin{pmatrix}A&X\\Y&H\end{pmatrix},\qquad
H=\begin{pmatrix}-\lambda_h&m\\n&-\lambda_k\end{pmatrix}.
\]

Here `X` is `(N-2) x 2`, `Y` is `2 x (N-2)`, and

\[
m=q_{hk},\quad n=q_{kh},\quad
\lambda_h=m+\sum_{i\in W}Y_{hi},\quad
\lambda_k=n+\sum_{i\in W}Y_{ki}.
\]

Bidirectionality means either `m,n>0` or `m=n=0`, and `X_ih>0` iff `Y_hi>0`, with the analogous condition for `k`. Define

\[
N_h=\{i\in W:X_{ih}>0\},\qquad
N_k=\{i\in W:X_{ik}>0\}.
\]

External twins satisfy `N_h=N_k=J`. Their common neighborhood is nonempty by irreducibility and the presence of observed states outside the pair.

For any invertible row-normalized pair matrix

\[
U=\begin{pmatrix}u&1-u\\v&1-v\end{pmatrix},\qquad
\delta=u-v\ne0,
\]

put `S=diag(I_W,U)` and `Q'=S^{-1}QS`. Then

\[
A'=A,\quad X'=XU,\quad Y'=U^{-1}Y,\quad H'=U^{-1}HU.
\]

All observed edges lie in `A`, so their rates and incidence stay unchanged. If `T=Q-E` is the killed generator, `S` commutes with `E`; moreover `RS=RS^{-1}=R` and `SB=S^{-1}B=B`. Hence

\[
T'=S^{-1}TS,\qquad Re^{T't}B=Re^{Tt}B.
\]

Every physically admissible transformed generator preserves the complete marked waiting kernel. This direction requires no minimality theorem. If the original realization is minimal, each transformed realization is minimal because controllability and observability are invariant under invertible similarity. The stationary law is `pi'=pi S` whenever the transformed graph is irreducible.

The outside block may have arbitrary internal topology and rates. Treating all its coordinates as fixed does not assume they are visible.

## 2. Equal external exit rows imply nonminimality

Suppose the **full external exit vectors** agree: `Y_h=Y_k=y`. Then `H1=-(y1)1`. The subspace

\[
\mathcal L=\{z\in\mathbb R^N:z_h=z_k\}
\]

has dimension `N-1` and is invariant under `Q`: equal pair coordinates give equal output pair coordinates, since their common outside contributions are `y z_W` and internal pair jumps cancel in the difference. It is also invariant under `T`, because observed edges touch neither `h` nor `k`. Every column of `B` has zero pair coordinates and lies in this subspace. Thus all reachable vectors `T^jBz` lie in `L`; the kernel realization is uncontrollable and nonminimal.

Consequently minimality guarantees `Y_h!=Y_k` for every pair of fully hidden states. This statement is about equality of the full external vectors, not just equality of their sums or rates into observed endpoints. Equal exit rates `lambda_h=lambda_k` do not by themselves cause nonminimality. Equal rates into the visible endpoints also do not suffice when rates into other hidden states differ.

## 3. Explicit fixed-topology boundary theorem

Assume external twins, unequal external exit vectors `Y_h!=Y_k`, and either:

1. `m,n>0`; or
2. `m=n=0` and `lambda_h=lambda_k`.

No minimality assumption is needed once the unequal-vector condition is explicit. Every entry `Y_hi,Y_ki` with `i in J` is positive. Exchange the pair labels if necessary so that

\[
r=\min_{i\in J}\frac{Y_{hi}}{Y_{ki}}\in(0,1).
\]

This choice is possible because the vectors differ. Consider

\[
U_e=\begin{pmatrix}1-e&e\\0&1\end{pmatrix},\qquad 0\le e<r.
\]

For every outside state `i`,

\[
X'_{ih}=(1-e)X_{ih},\quad
X'_{ik}=X_{ik}+eX_{ih},
\]

\[
Y'_{hi}=\frac{Y_{hi}-eY_{ki}}{1-e},\quad
Y'_{ki}=Y_{ki}.
\]

Both directions of every external pair edge remain positive for `e<r`; all common missing edges stay zero. Rates within `W` stay unchanged. If the pair is adjacent,

\[
H'_{kh}=n(1-e)>0,\qquad
H'_{hk}=\frac{f(e)}{1-e},\qquad
f(e)=m+e(\lambda_k-\lambda_h)-ne^2.
\]

Let `e_*` be the first zero of `f` in `(0,r]`, if there is one, and otherwise set `e_*=r`. Then `0<e_*<=r<1`, and all generators with `0<=e<e_*` retain the original support and irreducibility. If the pair is unjoined with equal escape rates, `H=-lambda I` stays unchanged; take `e_*=r` without a polynomial constraint.

The stationary law is explicit on the whole path:

\[
\pi'_i=\pi_i\quad(i\in W),\qquad
\pi'_h=(1-e)\pi_h,\qquad
\pi'_k=\pi_k+e\pi_h.
\]

Since `e_*<1`, **every stationary probability has a strictly positive finite limit**. Every transformed rate remains bounded, since `1-e>=1-r>0`.

At an internal-edge boundary `f(e_*)=0`, the flux on `h->k` tends to zero while that on `k->h` tends to

\[
(\pi_k+e_*\pi_h)n(1-e_*)>0.
\]

At an external boundary `e_*=r`, choose `i` attaining the minimum ratio. The flux on `h->i` tends to zero while that on `i->h` tends to

\[
\pi_i(1-r)X_{ih}>0.
\]

These conclusions also hold if several rates vanish simultaneously. Each edge's entropy contribution is nonnegative, and an edge with one vanishing and one positive limiting flux contributes an amount tending to infinity. Therefore `sup sigma(Q_e)=infinity`.

This proof neither requires an irreducible boundary generator nor assumes continuity of its stationary law. The displayed stationary vectors give the limits directly. The family before the endpoint is irreducible on exactly the original topology. In particular, an adjacent hidden twin pair or an equal-escape unjoined twin pair in a minimal five-state kernel eliminates bounded entropy at the five-state cap without cloning.

## 4. Why the support hypotheses matter at fixed topology

Suppose an outside state `i` is adjacent to `h` but not to `k`. Its coupling row and reverse column are `(a,0)` and `(b,0)^T`, with `a,b>0`. Under a general pair similarity,

\[
(X'_{ih},X'_{ik})=(au,a(1-u)),\qquad
(Y'_{hi},Y'_{ki})=\frac b\delta(1-v,-v).
\]

Retaining the original missing pair `i<->k` forces `u=1` and `v=0`, so `U=I`. The argument is symmetric for a neighbor exclusive to `k`. Therefore equal external neighborhoods are **necessary** for a nontrivial isolated pair similarity to preserve the same labeled bidirected support. Trivial hidden relabelings are ignored.

For external twins without a pair edge, retaining that absence requires `H'=U^{-1}HU` diagonal. If `lambda_h!=lambda_k`, the columns of `U` must be coordinate eigenvectors of the diagonal `H`, so row normalization forces a permutation matrix. Thus this fixed-topology pair method is rigid in the unequal-escape case. If the escapes agree, the scalar hidden block imposes no additional condition, and Section 3 applies in the minimal setting.

An apparent pair of twins based only on visible incidence can fail this test. For example, suppose both states connect to the same visible endpoints but only `h` connects to a third hidden state `l`. The triangular transformation immediately makes `q'_{lk}=e q_{lh}>0` while `q'_{kl}=0`, violating bidirectionality. State `l` must be included in `W` and the external-neighborhood test.

This necessity statement concerns transformations supported on this two-coordinate block. It does not exclude a larger hidden similarity that changes other hidden coordinates simultaneously.

## 5. Unknown topology: twins and nested neighborhoods

For unknown topology, a fixed small similarity may first create a suitable twin pair, after which Section 3 supplies an unbounded path. These steps preserve dimension and, for a minimal source, preserve minimality.

### Equal external neighborhoods

The joined and equal-escape unjoined cases are already handled at fixed topology. For unjoined twins with unequal escape rates, orient the labels so `lambda_h<lambda_k`. Put

\[
U_t=\begin{pmatrix}1-t&t\\-t&1+t\end{pmatrix},\qquad t>0
\]

with `t` sufficiently small. Existing external rates stay positive by continuity. Direct calculation, with `Delta=lambda_k-lambda_h>0`, gives

\[
H'_{hk}=t(1+t)\Delta>0,\qquad
H'_{kh}=t(1-t)\Delta>0.
\]

The now-adjacent twin pair satisfies Section 3. Hence any hidden external-twin pair in a minimal realization forces unboundedness with unknown topology at the same state count, regardless of escape ordering.

### Strictly nested neighborhoods

Suppose `N_k` is a proper subset of `N_h`. Every exclusive outside neighbor belongs only to `h`. The same `U_t` opens both directions between each such neighbor and `k`: for the singleton data above the transformed rates are `(a(1-t),at)` and `(b(1+t),bt)^T`. Existing common edges remain positive for sufficiently small `t`. The transformed pair therefore has common neighborhood `N_h`.

If the pair edge was present, it stays positive by continuity, so Section 3 applies. If it was absent and `lambda_h<lambda_k`, the displayed hidden-rate formulas open it. If it was absent and `lambda_h=lambda_k`, its block remains scalar and Section 3's unjoined variant applies. The external exit rows remain different: in general

\[
Y'_h-Y'_k=\frac{Y_h-Y_k}{u-v}.
\]

For strictly nested source supports they cannot have been equal.

### Precise pair-method obstructions

Choose the target pair labels so `delta=u-v>0`. An outside neighbor exclusive to `h` imposes nonnegativity `0<=u<=1`, `v<=0`. Bidirectionality rules out the one-sided support boundaries: every admissible target has either `U=I`, or `0<u<1` and `v<0`.

If there is also an outside neighbor exclusive to `k`, its constraints force `u>=1`, `v>=0`. Therefore incomparable neighborhoods pin the isolated-pair transformation to identity, up to hidden permutation, even when topology changes are allowed.

For an unjoined strictly nested pair with `h` the larger-neighborhood vertex, every nonidentity admissible target must obey the preceding open-quadrant restriction, while

\[
H'_{hk}=\frac{(1-u)(1-v)(\lambda_k-\lambda_h)}{u-v},\qquad
H'_{kh}=\frac{uv(\lambda_h-\lambda_k)}{u-v}.
\]

Both have the sign of `lambda_k-lambda_h`. If `lambda_h>lambda_k`, they would be negative; the isolated-pair orbit is therefore rigid up to permutation. This is a global restriction on this pair-only orbit, not merely failure of a selected first-order perturbation.

The resulting unknown-topology pair test is:

| External neighborhood relation | Pair edge | Conclusion for a minimal source |
| --- | --- | --- |
| Equal | Present | Unbounded already at fixed topology |
| Equal | Absent, equal escape rates | Unbounded already at fixed topology |
| Equal | Absent, unequal escape rates | Unbounded after opening the pair edge |
| Strictly nested, with `N_h` larger | Present | Unbounded after completing the smaller neighborhood |
| Strictly nested, with `N_h` larger | Absent, `lambda_h<=lambda_k` | Unbounded after completing the smaller neighborhood |
| Strictly nested, with `N_h` larger | Absent, `lambda_h>lambda_k` | Isolated pair method is rigid; full orbit unresolved |
| Incomparable | Either | Isolated pair method is rigid; full orbit unresolved |

In particular, a fully hidden leaf attached to another fully hidden state gives a nested adjacent pair and is excluded from a bounded-entropy candidate under unknown topology. For a five-state cycle with the observed edge on the cycle, by contrast, the three hidden pairs have incomparable external neighborhoods. This method provides no conclusion for that graph; it must not be interpreted as evidence of bounded nonuniqueness.

## 6. Equal exit rows outside the minimal subclass

The target five-state problem excludes identical full external exit rows by Section 2. It is nevertheless useful to distinguish failure of the triangular proof's ratio condition from evidence of bounded entropy.

If adjacent external twins have `Y_h=Y_k=y`, merging them is strongly lumpable because their rates to every outside state agree. Keep all outside rates and the pair-to-outside vector fixed, hold `n>0` fixed, and vary their **existing** rate `m` toward zero. The lumped generator and all marked kernels remain unchanged. Both pair states still communicate bidirectionally with every common outside neighbor, so their stationary probabilities have positive limiting values. The existing internal edge then produces divergent entropy exactly as in [state-splitting-audit.md](state-splitting-audit.md), applied to an already-present pair. No additional state is needed, and positive `m` retains the same topology. Combined with Section 3, adjacent hidden external twins force unbounded fixed-topology entropy whether or not the realization is minimal.

For unjoined twins with the same external exit row, write `lambda=y1`. If their common neighborhood has at least two states, retain each outside state's total rate into the pair while varying its split. Make one incoming rate `q_ih` tend to zero and keep a positive incoming rate from another common neighbor `j` fixed. Strong lumping again fixes the observed kernels and outside stationary probabilities. The stationary mass at `h` remains positive because of the unchanged incoming flux from `j`; its outgoing flux to `i` tends to a positive value. Hence entropy diverges at fixed topology, while the pair remains unjoined.

If their common neighborhood has only one state, the two unjoined twins are leaves attached to that state. Equal escape rates then imply equal full exit rows and nonminimality. Their leaf edges carry zero stationary current, and varying only their incoming split under a fixed aggregate creates no divergence. This is a concrete warning against inferring an infinite entropy contribution merely from a vanishing rate when its stationary mass vanishes too. It is not a classification of the entire network's compatibility fiber. If topology is allowed to change, adding a positive internal pair edge preserves the strong lumping and makes the preceding internal-edge divergence available at the same state count.

## 7. Independent three-coordinate checks supplied by the coordinator

**Reproduced calculation.** The following two rational examples were supplied by the coordinating agent and independently checked here using Python `Fraction` arithmetic. The check source is embedded below; it uses the repository's existing exact matrix helpers. These examples distinguish the failure of pair mixing from local isolation of the complete three-hidden-coordinate orbit.

For the first example, in order `(x,y,h,k,l)`,

\[
Q=\begin{pmatrix}
-11&1&2&0&8\\
2&-20&0&7&11\\
3&0&-7&4&0\\
0&6&5&-11&0\\
9&10&0&0&-19
\end{pmatrix}.
\]

Observe only `x<->y`. Every hidden pair has incomparable external neighborhoods, so the pair-only test is rigid. Nevertheless, put `U=I+epsilon K`, with `epsilon=1/1000`. In row-major off-diagonal order `(hk,hl,kh,kl,lh,lk)`, take the entries of `K` to be

\[
(-1,581/1000,958/1000,-340/1000,-593/1000,273/1000),
\]

and set each diagonal to minus its row's off-diagonal sum.

The exact transformed generator has all twenty off-diagonal rates positive and zero row sums. Both original and transformed killed-kernel realizations have controllability and observability ranks `(5,5)`. The law `pi'=pi S` is strictly positive and stationary. The ten Markov parameters at orders zero through nine agree exactly, giving an all-time equality certificate as well as the direct similarity identity. The complete target graph contains adjacent hidden external twins, so Section 3 proves that this original sparse kernel has unbounded entropy under unknown topology at the same five-state cap.

**Inference.** This example explicitly refutes any proposed extension from “all isolated-pair moves are obstructed” to “the full hidden orbit is rigid.”

For the second example, retain the first four rows of `Q` and replace the last row by `(3,3,0,0,-6)`. Parameterize every normalized hidden matrix near identity by its six off-diagonal increments in the same order, setting its diagonal increments to minus the row sums. For the eight missing ordered rates in order

\[
(xk,yh,hy,hl,kx,kl,lh,lk),
\]

the first-order map `g(z)=Az+O(||z||^2)` is

\[
A=\begin{pmatrix}
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

Exact elimination gives `rank A=6`. The strictly positive vector

\[
c=(3,1,1,10/3,7/3,19/15,151/15,79/15)^T
\]

satisfies `c^T A=0` exactly. Hence `Az>=0` implies `Az=0`, then `z=0`.

This linear fact proves **actual local isolation**, not merely infinitesimal rigidity. If nonzero feasible increments `z_j->0` existed, a subsequence of their normalized directions would tend to a unit vector `v`. Dividing the necessary inequalities `g(z_j)>=0` by `||z_j||` would give `Av>=0`. The positive dual vector and full column rank would force `v=0`, a contradiction. The rational similarity map is analytic near identity, so its Taylor remainder has the stated quadratic order.

The second source is also exactly minimal, with ranks `(5,5)`. This promotes isolation in similarity coordinates to local isolation of generators in the full fixed-five-state compatibility fiber: select a nonsingular controllability minor `M(Q)`. For a compatible nearby `Q'`, the uniquely normalized similarity obeys `S M(Q')=M(Q)`, so `S=M(Q)M(Q')^{-1}->I` as `Q'->Q`. A nearby compatible generator would therefore produce a forbidden nearby similarity.

**Limit of the local certificate.** Local isolation alone does not exclude distant compatible generators or an unbounded component. The subsequent [global audit of this same example](theta-global-audit.md) constructs a distant complete representative and an exact entropy-divergent family. Its compatibility set is therefore disconnected and its entropy range unbounded; the local certificate does not decide connectivity of the entropy image.

### Reproduce the independent exact checks

Run from the repository root:

~~~powershell
python -c "from pathlib import Path; t=Path('analysis/hidden-pair-boundary-audit.md').read_text(encoding='utf-8'); exec(t.rsplit('<!-- PAIR_AUDIT_CODE -->',1)[1].split(chr(96)*3+'python',1)[1].split(chr(96)*3,1)[0])"
~~~

The accepted output reports positive opening rates, zero row sums, ranks `[5,5]` for both opening realizations, exact stationarity, ten equal Markov parameters, `rank A=6`, positive `c`, and six exact zeros for `c^T A`. It also prints all eight rational opened rates, the first-order matrix, and runtime versions. There is no stochastic input or seed.

<!-- PAIR_AUDIT_CODE -->
```python
import sys
sys.path.insert(0, "analysis")
import numpy as np
from fractions import Fraction as F
from check_small_networks import matrix, eye, exact_rank, marked_system, derivatives
from check_four_state_classification import stationary

def inverse(a):
    n = len(a)
    aug = np.concatenate([a.copy(), eye(n)], axis=1)
    for col in range(n):
        pivot = next(i for i in range(col,n) if aug[i,col])
        aug[[col,pivot]] = aug[[pivot,col]]
        aug[col] = aug[col] / aug[col,col]
        for i in range(n):
            if i != col: aug[i] = aug[i] - aug[i,col]*aug[col]
    return aug[:,n:]

def ranks(q):
    r,t,b = marked_system(q)
    p = eye(len(q)); cs=[]; os=[]
    for _ in range(len(q)):
        cs.append(p@b); os.append(r@p); p=p@t
    return [exact_rank(np.concatenate(cs,axis=1)), exact_rank(np.concatenate(os,axis=0))]

q = matrix([[-11,1,2,0,8],[2,-20,0,7,11],[3,0,-7,4,0],[0,6,5,-11,0],[9,10,0,0,-19]])
off = [(i,j) for i in range(3) for j in range(3) if i != j]
k = matrix([[0,0,0],[0,0,0],[0,0,0]])
for (i,j),value in zip(off,["-1","581/1000","958/1000","-340/1000","-593/1000","273/1000"]):
    k[i,j]=F(value)
for i in range(3): k[i,i]=-sum(k[i])
s = eye(5); s[2:,2:] = eye(3)+F(1,1000)*k
qp = inverse(s)@q@s
missing=[(i,j) for i in range(5) for j in range(5) if i != j and q[i,j] == 0]
print("opening_missing_order",missing)
print("opening_missing_rates",[str(qp[i,j]) for i,j in missing])
print("opening_all_rates_positive",all(qp[i,j]>0 for i in range(5) for j in range(5) if i != j))
print("opening_row_sums_zero",all(sum(row)==0 for row in qp))
print("opening_ranks",ranks(q),ranks(qp))
pi=stationary(q); pip=pi@s
print("opening_stationary_positive",all(p>0 for p in pip),all(x==0 for x in pip@qp))
print("opening_first10_parameters_equal",all(np.array_equal(a,b) for a,b in zip(derivatives(q,10),derivatives(qp,10))))
q0=q.copy(); q0[4]=matrix([[3,3,0,0,-6]])[0]
cols=[]
for a,b in off:
    l=matrix([[0]*5 for _ in range(5)])
    l[a+2,b+2]=F(1); l[a+2,a+2]=F(-1)
    comm=q0@l-l@q0
    cols.append([comm[i,j] for i,j in missing])
A=matrix(cols).T
c=matrix([["3","1","1","10/3","7/3","19/15","151/15","79/15"]])[0]
print("isolation_A",[[str(x) for x in row] for row in A])
print("isolation_rankA",exact_rank(A))
print("isolation_c_positive",all(x>0 for x in c))
print("isolation_cA",[str(x) for x in c@A])
print("isolation_ranks",ranks(q0))

import platform
print("environment", platform.python_version(), np.__version__)
```

## Scope retained after the audit

The constructive theorem and neighborhood tests reduce the sparse five-state search without spending an extra state. Their crucial hypotheses are fully hidden pair coordinates, incidence checked against all outside states, and a path staying inside physical bidirected rates until a positive-stationary-flux boundary. The remaining cases require simultaneous mixing of at least three hidden coordinates or a different argument. No general five-state unique/unbounded dichotomy, bounded counterexample, entropy infimum, or publication novelty is established by this note.
