# Five-state sparse audit: distinct diagonal hidden poles

Date: 2026-09-10 UTC. Contribution: analytic proof and exact representative calculations, with verification status recorded below. This bounded audit studies one sparse class under [D005](../evidence/RECORDS.md#d005); it is not a five-state topology enumeration or a novelty claim.

## Scope and result

Assume the [working formulation](formulation.md), exactly one resolved observed pair `x<->y`, and a five-state representative with three hidden states, **no hidden-hidden edges**, and three pairwise distinct hidden escape rates. Every hidden state has at least one visible neighbor, as required by connectivity. Its visible-neighbor set is therefore `{x}`, `{y}`, or `{x,y}`. Competing models may use any simple bidirected topology on at most five states.

**Proved for this class:** the kernel has minimal linear dimension five. Its unknown-topology compatibility fiber has one of the following two outcomes:

1. If the three hidden neighbor sets are all different, and the shared state's escape rate exceeds both exclusive states' escape rates, the entire generator is unique up to hidden permutation.
2. Otherwise the entropy-production rate is unbounded above.

Thus this distinct-diagonal class supplies no bounded non-singleton entropy fiber. The uniqueness statement excludes arbitrary three-state hidden mixing, not merely pairwise perturbations. It uses a spectral obstruction from the positive dominant-pole residue of every hidden component connecting the two visible ports.

A second checked deduction, in Section 6, shows why a proposed finite ambiguity between two hidden-path representations can leave entropy identical. Its full unknown-topology fiber is not classified here.

## 1. Formulation and automatic minimality

Write

\[
Q=\begin{pmatrix}A&X\\Y&H\end{pmatrix},\qquad
H=-\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3),
\]

where the positive `lambda_i` are distinct. Each column of `X` and corresponding row of `Y` is nonzero, and their positive entries share the same visible incidence by bidirectionality. Since there are no hidden-hidden edges, `Y_i 1=lambda_i`.

Let `T` remove the observed off-diagonal pair, leaving visible block `D`. The observed data determine the visible block `K(t)=[exp(Tt)]_VV`, its derivative `D=K'(0)`, and the hidden response

\[
F(z)=zI-D-\widehat K(z)^{-1}
=X(zI-H)^{-1}Y
=\sum_{i=1}^3\frac{Z_i}{z+\lambda_i},\qquad Z_i=X_{:i}Y_{i:}.
\]

Every residue is nonzero, nonnegative, and rank one.

For completeness, automatic minimality follows without equating the number of scalar poles with realization dimension. An unobservable full vector must have zero visible part and hidden part `w` satisfying `XH^j w=0` for all `j`. For each visible row, the first three such equations form a nonsingular Vandermonde system in the three distinct `lambda_i`, implying `X_vi w_i=0` for every `v,i`. Every hidden column has a positive entry, so `w=0`. The transposed argument with `H^jY` proves controllability. The corresponding full-space implications follow because the unobservable subspace is `T` invariant, and a vector `(0,w)` with `Xw=0` is sent to `(0,Hw)`; the controllability argument is its dual.

The kernel therefore has minimal dimension five. Every competing model under a five-state cap must also have exactly five states and be minimal. The [orbit theorem](compatibility-orbit.md) applies:

\[
Q'=S^{-1}QS,\qquad S=\operatorname{diag}(I_2,U),\qquad U1=1,
\]

with arbitrary real invertible `3 x 3` `U`, subject to physical generator constraints. In particular `H'=U^{-1}HU` has the same three distinct eigenvalues. No positivity constraint is imposed on `U` itself.

## 2. Repeated visible-neighbor sets give unbounded entropy

Suppose two hidden states share the same visible-neighbor set. Mix only these two states, leaving the third hidden coordinate unchanged. This keeps every hidden edge between the selected pair and the third state zero. On each active visible port both selected forward and reverse legs are strictly positive; on an inactive port both are zero.

Order the selected pair so `lambda_1<lambda_2`. For sufficiently small `e,eta>0`, use

\[
U_{e,\eta}=\begin{pmatrix}1-e&e\\-\eta&1+\eta\end{pmatrix}
\]

on that pair. All existing visible-hidden legs remain positive by continuity, and their missing whole rows/columns remain zero. Its two new hidden rates are

\[
H'_{12}=\frac{e(1+\eta)(\lambda_2-\lambda_1)}{1-e+\eta}>0,
\qquad
H'_{21}=\frac{(1-e)\eta(\lambda_2-\lambda_1)}{1-e+\eta}>0.
\]

This opens a bidirectional hidden edge with exactly unchanged kernels. The two selected rows of `Y` were unequal because their sums were distinct. They stay unequal under a normalized invertible hidden transformation: `U^{-1}Y=1y` would imply `Y=U1y=1y`.

The triangular divergent family in Section 3 of the [unknown-topology audit](unknown-topology-audit.md) now applies to the selected pair. Its proof uses only their positive internal link, positive active visible incidence, and unequal exit rows; it remains valid when an untouched third hidden state is present. The third state has no hidden links to the pair, so its blocks are unchanged. The second transformation gives a vanishing edge rate with a strictly positive reverse stationary flux, while the pair's stationary probabilities remain positive. Thus entropy is unbounded at exactly five states.

This is an unknown-topology argument: the first transformation adds a hidden link. Distinct diagonal hidden escape rates still identify rates when the original no-hidden-edge topology is held fixed.

## 3. One exclusive state at each port and one shared state

Only one incidence pattern remains after Section 2. Label the hidden states `h,k,l` with neighbor sets `{x}`, `{y}`, and `{x,y}`. Write

\[
X=\begin{pmatrix}a&0&c\\0&b&d\end{pmatrix},\qquad
Y=\begin{pmatrix}A&0\\0&B\\\gamma&\delta\end{pmatrix},\qquad
C=\gamma+\delta,
\]

where all displayed parameters are positive and `A,B,C` are distinct. Then

\[
F(z)=\frac1{z+A}\begin{pmatrix}aA&0\\0&0\end{pmatrix}
+\frac1{z+B}\begin{pmatrix}0&0\\0&bB\end{pmatrix}
+\frac1{z+C}\begin{pmatrix}c\gamma&c\delta\\d\gamma&d\delta\end{pmatrix}.
\]

If `C<A`, mix the shared state `l` and exclusive state `h`, leaving `k` fixed. Within this pair one visible port has both neighbors, and the other port has the shared state as its singleton neighbor. Its escape rate `C` is smaller than the other escape `A`. The signed perturbation above, with pair order `(l,h)`, makes the missing visible leg positive in both directions and opens the hidden link in both directions. Existing positive legs remain positive. The pair then has dense active visible incidence and unequal exit rows, so the exact triangular family again gives unbounded entropy. The case `C<B` uses `(l,k)` instead.

Consequently unboundedness holds unless `C>max(A,B)`. This leaves the only case where all pairwise attempts are pinned. The next section excludes non-pairwise hidden mixing globally.

## 4. Global spectral obstruction when the shared state is fastest

Assume `C>A` and `C>B`. The off-diagonal hidden responses are

\[
F_{xy}(z)=\frac{c\delta}{z+C},\qquad
F_{yx}(z)=\frac{d\gamma}{z+C}.
\]

Consider any compatible bidirected five-state generator. Its hidden subgraph splits into connected components, because each hidden link is present in both directions. After permutation `H'` is block diagonal over those components, with every nontrivial block irreducible Metzler. A component is called bridging here if it has visible connections to both `x` and `y`.

**Dominant-pole lemma.** For an irreducible hidden component touching both ports, the spectral-bound eigenvalue of its hidden block produces a strictly positive residue in `F_xy` and `F_yx`. Indeed the Perron eigenvalue of a sufficiently shifted nonnegative irreducible block is simple, with positive right and left eigenvectors `v,w`. For the corresponding eigenvalue of the unshifted block, its resolvent residue is `v w^T/(w^T v)`. Multiplying by the nonzero nonnegative entrance vector from one port and exit vector to the other gives a strictly positive number. The singleton version is immediate.

The whole hidden spectrum is exactly `{-A,-B,-C}`, with distinct eigenvalues, by the minimal orbit theorem. Each eigenvalue belongs to only one hidden component, so the positive dominant-pole residue of a bridging component cannot be canceled by another component. Since the observed off-diagonal responses have only pole `-C`, every bridging component must have spectral bound `-C`.

But `-C` is strictly smaller than both other hidden eigenvalues `-A,-B`. A component containing either of those eigenvalues would have spectral bound greater than `-C`. Therefore a bridging component can contain only the eigenvalue `-C`, and it consists of one hidden state. At least one bridge is required by the nonzero cross responses, and distinctness allows exactly one.

The remaining two hidden states cannot share a bridging component. The pole `-A` occurs only in `F_xx`, and `-B` only in `F_yy`, with positive residues. Thus the remaining states must be separate singleton components attached exclusively to `x` and `y`, respectively. A two-state component attached only to one port could not supply the other diagonal response pole. Hence every compatible topology is the original one, up to hidden labels.

Finally residues identify all rates. For each singleton hidden component with residue `Z_i` and escape `lambda_i`,

\[
X_{:i}=Z_i1/\lambda_i,
\]

and its exit row is recovered by dividing any nonzero row of `Z_i` by the corresponding entrance rate. The visible block is already determined by the observed rates and `K'(0)`. This proves global generator uniqueness, including against arbitrary signed, non-pairwise `3 x 3` hidden similarities.

The argument is limited to distinct hidden poles and this residue pattern. It does not assert that positive residues or pairwise rigidity alone force uniqueness in other five-state models.

## 5. Two exact examples

State order is `(x,y,h,k,l)`, and rates use one common inverse-time unit with `k_B=1`.

### Globally unique example

\[
Q_{\rm unique}=\begin{pmatrix}
-3&1&1&0&1\\
1&-3&0&1&1\\
1&0&-1&0&0\\
0&2&0&-2&0\\
1&2&0&0&-3
\end{pmatrix},\qquad
\pi=\frac1{37}(8,10,8,5,6).
\]

The three hidden escapes are `A=1`, `B=2`, `C=3`; the shared state is fastest. The residue obstruction proves uniqueness across all bidirected topologies under the five-state cap. Its entropy rate is

\[
\sigma=\frac2{37}\log2.
\]

The two leaf currents vanish, while the current along `x->l->y->x` is `2/37` and that cycle's rate-product ratio is two.

### Explicit unbounded example

Change the `h->x` rate to four, so the hidden escapes are `A=4`, `B=2`, `C=3`. A single signed hidden transformation suffices:

\[
U_t=\begin{pmatrix}1+t&0&-t\\0&1&0\\t&0&1-t\end{pmatrix},\qquad
\det U_t=1,\qquad 0\le t<1/3.
\]

The corresponding generators are

\[
Q_t=\begin{pmatrix}
-3&1&1+2t&0&1-2t\\
1&-3&t&1&1-t\\
4-3t&2t&-4+t^2&0&t(1-t)\\
0&2&0&-2&0\\
1-3t&2+2t&t(1+t)&0&-3-t^2
\end{pmatrix},\qquad
\pi_t=\frac1{31}(8,10,2+8t,5,6-8t).
\]

At `t=0` this is the diagonal-hidden representative. For `t>0`, the new `y<->h` and `h<->l` links are positive. Every point remains bidirected, irreducible and minimal of dimension five. Direct similarity gives the same complete kernels for every `t`.

As `t->1/3-`, the rate `l->x=1-3t` vanishes while the reverse rate `x->l=1-2t` tends to `1/3`. Its opposing stationary flux tends to `8/93`. All other required rates and stationary probabilities have positive limits. Therefore

\[
\sigma(Q_t)=\frac8{93}\log\frac1{1/3-t}+O(1)\longrightarrow\infty.
\]

Every individual rate remains bounded. The original model has entropy `2 log(2)/31`; no zero-entropy compatible realization is asserted.

## 6. Checked addendum: equal path ratios hide rate ambiguity, not entropy ambiguity

Consider the topology consisting of the observed edge `x<->y` and two unobserved paths `x-h-k-y` and `x-l-y`. Orient all three paths from `x` to `y`, and call their stationary currents `J_0,J_1,J_2`. Internal degree-two vertices make each path current constant, and stationarity gives `J_0+J_1+J_2=0`.

Let `R_1,R_2` be the forward/backward elementary rate-product ratios of the two hidden paths; the observed edge has ratio `r/s`. Summing edge contributions, with stationary-probability terms canceling, gives

\[
\sigma=J_0\log(r/s)+J_1\log R_1+J_2\log R_2.
\]

If `R_1=R_2=R`, then

\[
\sigma=J_0\log\frac{r/s}{R}.
\]

Both `J_0=\pi_xr-\pi_ys` and the rates `r,s` are fixed by complete observed kernels. If two candidate representations have the same hidden-response cross ratio `R=c/d` and both hidden paths separately have that ratio, the two candidates necessarily have identical entropy, despite distinct microscopic rates.

This applies to the proposed residue reassignment in which two entrywise-positive rank-one residues have off-diagonal entries `(c,d)` and a third signed rank-one residue has off-diagonal entries `(-c,-d)`. Pairing either positive residue with the signed one gives the two-state hidden path; its cross-response ratio is `c/d`, while the unpaired singleton path has the same ratio. Thus the construction alone is not a bounded-nonunique entropy counterexample.

**Limit of the identity:** it does not classify all compatible topologies of that kernel. A different hidden realization could carry circulation not present in either proposed path representation. Constancy of an observed cross ratio alone does not exclude hidden entropy, as the earlier four-state examples demonstrate. The later [theta-family construction audit](theta-family-construction-audit.md) addresses support opening and residue reassignment on this topology under explicit parameter conditions.

## 7. Reproducible representative checks

The following embedded check writes no files. It uses the existing exact matrix helpers, whose dependency versions are recorded by the output. From the repository root run:

~~~powershell
python -B -c "from pathlib import Path; exec(Path('analysis/five-state-sparse-audit.md').read_text(encoding='utf-8').split('# BEGIN REPRO CHECK' + chr(10),1)[1].split('# END REPRO CHECK',1)[0])"
~~~

~~~python
# BEGIN REPRO CHECK
import sys, json, math, platform
from fractions import Fraction as F
sys.path.insert(0, 'analysis')
import numpy as np
import scipy
from check_small_networks import matrix, eye, marked_system, exact_rank
from check_small_networks import derivatives, check_generator, entropy

unique = matrix([[-3,1,1,0,1], [1,-3,0,1,1], [1,0,-1,0,0],
                 [0,2,0,-2,0], [1,2,0,0,-3]])
unique_pi = matrix([[F(i,37) for i in [8,10,8,5,6]]])[0]
check_generator(unique, unique_pi)
assert abs(entropy(unique, unique_pi) - 2*math.log(2)/37) < 1e-14

def family(t):
    return matrix([[-3,1,1+2*t,0,1-2*t], [1,-3,t,1,1-t],
        [4-3*t,2*t,-4+t*t,0,t*(1-t)], [0,2,0,-2,0],
        [1-3*t,2+2*t,t*(1+t),0,-3-t*t]])

def stationary(t):
    return matrix([[F(8,31), F(10,31), (2+8*t)/31,
                    F(5,31), (6-8*t)/31]])[0]

base = family(F(0))
base_derivatives = derivatives(base, 10)
points = [F(0), F(1,8), F(1,4)] + [F(1,3)-F(1,10**k) for k in [3,6,9]]
samples = []
for t in points:
    q, pi = family(t), stationary(t)
    check_generator(q, pi)
    s = eye(5)
    s[2,2], s[2,4], s[4,2], s[4,4] = 1+t, -t, t, 1-t
    assert np.array_equal(base @ s, s @ q)
    assert np.array_equal(stationary(F(0)) @ s, pi)
    assert all(np.array_equal(a,b) for a,b in zip(base_derivatives, derivatives(q,10)))
    samples.append({'t': str(t), 'entropy': entropy(q, pi)})

ranks = []
for q in [unique, base]:
    r, killed, b = marked_system(q)
    power, obs, ctr = eye(5), [], []
    for j in range(5):
        obs.append(r @ power)
        ctr.append(power @ b)
        power = power @ killed
    ranks.append([exact_rank(np.vstack(obs)), exact_rank(np.hstack(ctr))])
assert ranks == [[5,5],[5,5]]
limit_pi = stationary(F(1,3))
limit_q = family(F(1,3))
assert all(p > 0 for p in limit_pi) and all(v == 0 for v in limit_pi @ limit_q)
assert limit_q[4,0] == 0 and limit_pi[0]*limit_q[0,4] == F(8,93)
slope = (samples[-1]['entropy']-samples[-2]['entropy']) / math.log(1000)
assert abs(slope-F(8,93)) < 1e-5
print(json.dumps({'python': platform.python_version(), 'numpy': np.__version__,
 'scipy': scipy.__version__, 'exact_ranks': ranks, 'derivative_orders': [0,9],
 'unique_entropy': entropy(unique,unique_pi), 'samples': samples,
 'last_logarithmic_slope': slope, 'predicted_slope': float(F(8,93))}, indent=2))
# END REPRO CHECK
~~~

Verification status: the embedded check executed successfully on 2026-09-10 at approximately 06:15 UTC, using Python 3.9.12, NumPy 2.0.1 and SciPy 1.13.1. Both examples have exact observability/controllability ranks `(5,5)`. Exact similarities, generator constraints, stationary laws, and derivatives of orders 0-9 passed at all six rational points. The unique example gives entropy `0.037467415165402446`.

| Parameter in the divergent family | Computed entropy |
| --- | --- |
| `0` | `0.0447191729393513` |
| `1/8` | `0.11498773267995128` |
| `1/4` | `0.18617427943003806` |
| `1/3 - 10^-3` | `0.5237168233503335` |
| `1/3 - 10^-6` | `1.1164106267491003` |
| `1/3 - 10^-9` | `1.710623272316673` |

The last logarithmic slope is `0.08602109101570987`, approaching the proved coefficient `8/93 = 0.08602150537634409`. Imported helper [check_small_networks.py](check_small_networks.py) had SHA-256 `9b1b1007d17fa3fa55e50cb94135067cfe02c31b3e63415e0ad7926b9d6e39c4`. Inputs and the complete check code are embedded above; no random sampling or external data were used. The general classification rests on Sections 1-4, not on these representative checks or a finite numerical search.

## Scope beyond diagonal hidden blocks

The class just classified starts with diagonal hidden `H` and distinct hidden escapes. It does not cover a hidden chain or triangle, nonminimal data, repeated hidden eigenvalues, or arbitrary three-state hidden mixing on other supports. In particular, an unobserved path `x-h-k-y` in parallel with `x-l-y` has a coupled two-state hidden block plus a singleton, so the diagonal-residue proof above does not apply automatically.

A bounded-nonunique entropy fiber there would require control of every physical five-state realization, not just two isolated parameterizations. The [theta audit](theta-global-audit.md) gives an exact locally isolated realization with a distant unbounded component. The later [parameter-dependent constructions](theta-family-construction-audit.md) cover further regions, while [connected-hidden feasibility in the fast case](theta-fast-case-audit.md) remains unresolved. The residue-reassignment identity in Section 6 establishes equal entropy of the two proposed models, not bounded nonuniqueness of their full compatibility fiber.
