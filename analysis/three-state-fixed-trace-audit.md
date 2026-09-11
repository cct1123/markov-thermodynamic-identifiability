# Three-state entropy instability at fixed trace and unit rate cap

Date: 2026-09-10 UTC. Contribution: independent analytic audit and executed exact symbolic verification of the coordinator's proposed construction. Mathematical status: conventionally proved and exactly checked as specified below; not formally verified. No novelty claim or literature comparison is made here.

## Result and admissible class

Use the repository's [formulation](formulation.md): simple finite bidirected row CTMCs, even states, one channel per ordered pair, known resolved reverse-closed marks, and natural-log entropy in units with Boltzmann's constant one. Observe only \(x\leftrightarrow y\), at fixed rates one in both directions, and impose the exact state cap three. Topology is unknown.

The symmetric tree source

\[
Q_0=\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{pmatrix}
\quad\text{in order }(x,y,h)
\]

has stationary law \((1,1,1)/3\), entropy zero, and minimal full marked-kernel realization dimension three. The already proved [three-state recovery theorem](small-network-audit.md#1-identification-for-at-most-three-states), [E017](../evidence/RECORDS.md#e017), identifies its entire generator within the at-most-three-state class.

Nevertheless, every positive total-variation neighborhood of its joint next-mark/time kernel contains **unbounded entropy**, even restricting to exactly three states, exactly the source trace \(-4\), and microscopic offdiagonal rates at most one. The same is true for every positive neighborhood of its stationary observed path law on any fixed finite physical observation horizon. Two states cannot have this property in the simple bidirected convention because every two-state CTMC satisfies detailed balance and has entropy zero. Thus three is the minimum possible state count for this particular instability.

## 1. Exact candidate and stationary law

For \(0<k<e<1/2\), define

\[
Q(e,k)=\begin{pmatrix}
-1-e&1&e\\
1&-2+k&1-k\\
k&1-e&-1+e-k
\end{pmatrix}.
\tag{1}
\]

Every row sums to zero. Every offdiagonal rate is strictly positive and at most one; the observed rates are unchanged. The graph is a complete triangle, hence irreducible and bidirected. Its trace is exactly \(-4\). The bound one concerns individual jump rates, not the state escape rates, which are \(1+e,2-k,1-e+k\).

The stationary tree weights are

\[
w_x=1-e+2k-k^2,\quad
w_y=1+k-e^2,\quad
w_h=1-k+2e-ek,
\]
\[
Z=w_x+w_y+w_h=3+e+2k-e^2-ek-k^2,
\qquad \pi=(w_x,w_y,w_h)/Z.
\tag{2}
\]

Each weight is a sum of positive directed-tree products. In particular
\(Z-3=e(1-e-k)+k(2-k)>0\).
The checker verifies both the three tree cofactors and the normalized stationary equation independently from (1).

With orientation \(x\to h\to y\to x\), all three steady edge currents equal

\[
J=\frac{(e-k)(1-e-k)}{Z}>0.
\]

The product of the three oriented stationary flux ratios is
\(e(1-e)/[k(1-k)]\); stationary probabilities cancel. Therefore

\[
\boxed{\quad \sigma(Q(e,k))=
\frac{(e-k)(1-e-k)}Z
\log\frac{e(1-e)}{k(1-k)}.\quad}
\tag{3}
\]

Every factor and logarithm has its asserted sign on the stated open domain, since \(s(1-s)\) is strictly increasing on \((0,1/2)\).

## 2. Minimal dimension and exact identifiability persist

Let \(E\) contain only the two observed offdiagonal entries and put \(T=Q-E\). In mark order \((x\to y,y\to x)\),

\[
B=(e_x,e_y),\qquad R=\begin{pmatrix}e_y^T\\e_x^T\end{pmatrix}.
\]

An explicit controllability minor and observability minor are

\[
\det(e_x,e_y,Te_y)=1-e>0,
\]
\[
\det\begin{pmatrix}e_x^T\\e_y^T\\e_y^TT\end{pmatrix}
=1-k>0.
\tag{4}
\]

Both equal one at the source \(e=k=0\). Thus the entire full marked-kernel realization has minimal order three throughout this construction and at its source. E017 also identifies every individual candidate (1) exactly within the three-state cap. The instability therefore occurs between arbitrarily close but distinct observable kernels; it is not an exact nonidentifiability example and uses neither spare states nor nonminimal representations.

## 3. Unbounded neighborhoods and a divergent convergent sequence

For each fixed \(e\in(0,1/2)\), send \(k\downarrow0\) through positive values. The current tends to

\[
J_0(e)=\frac{e(1-e)}{3+e-e^2}>0,
\]

while the logarithm in (3) equals \(\log(1/k)+O_e(1)\). Hence entropy diverges with positive logarithmic coefficient \(J_0(e)\). The one-way limit itself is outside the bidirected class; all models before that limit remain admissible and retain the rate cap and trace.

For a single sequence converging entrywise to the source, choose
\(k(e)=\exp(-1/e^2)\) and let \(e\downarrow0\). This lies in \(0<k<e\) for all sufficiently small positive \(e\). Then

\[
\frac{J(e,k(e))}{e}\longrightarrow\frac13,
\]
\[
e^2\log\frac{e(1-e)}{k(e)(1-k(e))}
=1+e^2\log e+e^2\log(1-e)-e^2\log(1-k(e))
\longrightarrow1.
\]

Consequently

\[
\boxed{\quad Q(e,k(e))\to Q_0,
\qquad \sigma(Q(e,k(e)))\sim\frac1{3e}\to\infty.\quad}
\tag{5}
\]

This limiting proof is analytic; it does not interpret floating-point underflow of \(k(e)\) as a positive admissible rate.

## 4. Quantitative observation-law bounds

For each state, the sum of absolute offdiagonal rate changes from \(Q_0\) is respectively \(e,k,e+k\). A common/excess-clock coupling therefore has separation hazard at most \(e+k\) while the two microscopic paths coincide. The observed rates and marks coincide up to separation.

The original mean times to the next observed edge from \((x,y,h)\) are exactly \((1,2,3)\), as follows from \((-T_0)u=\mathbf1\). The two observed reset states are \(x,y\). Therefore the maximum joint next-mark/time row distance obeys

\[
d(Q_0,Q(e,k))\le2(e+k)<4e.
\tag{6}
\]

This bound is also a direct specialization of the independent semigroup \(L^1\) bound in the [neighborhood audit](entropy-neighborhood-audit.md#3-independent-quantitative-continuity-of-the-observation-law). It treats the full joint row laws, including next-mark probabilities, and integrates over all waiting times.

The stationary initial-law difference has a particularly simple exact form. Direct factorization gives

\[
3w_x-Z=-(e-k)(4-e-2k),
\]
\[
3w_y-Z=-(e-k)(1+2e+k),
\]
\[
3w_h-Z=(e-k)(5+e-k).
\]

Thus the first two stationary probabilities decrease from \(1/3\), and the hidden probability increases. Consequently

\[
\operatorname{TV}(\pi(e,k),\pi_0)
=\frac{(e-k)(5+e-k)}{3Z}
<\frac{11e}{18}.
\tag{7}
\]

For a fixed physical observation horizon \(H<\infty\), start each model in its own stationary law. Initial maximal coupling and the same rate-clock argument give

\[
\operatorname{TV}(\mathbb P_{Q(e,k)}^{H},\mathbb P_{Q_0}^{H})
\le\frac{(e-k)(5+e-k)}{3Z}+(e+k)H
<e\left(\frac{11}{18}+2H\right).
\tag{8}
\]

Here \(\mathbb P^H\) denotes the observed marked-path law, including event times and both window-end censoring cases. Rates and \(H\) use the fixed units in which the displayed observed rates equal one. The data-processing step from coupled microscopic paths to their observed paths cannot increase total variation.

Equations (6) and (8) are uniform over \(0<k<e\). Choose a fixed sufficiently small \(e>0\) to enter any prescribed positive observational neighborhood, and then let \(k\downarrow0\) to obtain unbounded entropy inside it. Alternatively, sequence (5) has both kernel laws and stationary finite-window path laws converging to the source while entropy diverges. The [uniform-confidence argument](entropy-neighborhood-audit.md#6-finite-horizon-statistical-implication-audit-of-the-added-claim) therefore applies already in this fixed-three-state, fixed-trace, unit-rate-cap class.

## 5. Scope and falsification audit

The exact claim would be falsified by an error in stationary weights/current, a loss of positive bidirected support along the proposed domain, failure of minimal order three, a nonvanishing observation-law distance along (5), or an entropy limit that remained bounded. The exact checks below and the explicit sign/limit arguments address each of these conditions. No search failure is used as proof.

The source is a known tree only **as one generator**; the admissible class permits the triangle opening. If the topology were prescribed to remain that tree, every admissible generator would have zero entropy and this construction would be excluded. The unboundedness also disappears under a uniform positive reverse-rate floor. This audit makes no assertion about known hidden microscopic initial states or a horizon growing jointly with \(e^{-1}\).

The immediate mechanism is entropy's failure of upper semicontinuity at the sparse bidirected boundary: two reverse rates vanish on very different scales. Since the generators themselves converge entrywise, this example does not require an unstable or nonunique observable inverse. Its significance here is that exact source order, exact trace, a finite rate cap, and even pointwise exact identifiability of every model do not alone furnish a robust finite entropy upper bound.

## Exact reproduction

The embedded check uses SymPy exact rational/polynomial arithmetic. Its symbols retain the displayed domain through the analytic sign argument; it does not replace \(0<k<e<1/2\) by a numerical rate grid. Execute from the project root:

~~~powershell
@'
from pathlib import Path
audit = Path('analysis/three-state-fixed-trace-audit.md').read_text(encoding='utf-8')
check_source = audit.rsplit('<!-- THREE_STATE_FIXED_TRACE_CHECK -->', 1)[1].split('```python', 1)[1].split('```', 1)[0]
assert 'all_exact_checks_passed' in check_source
exec(compile(check_source, '<three-state-fixed-trace-check>', 'exec'))
'@ | .\.venv\Scripts\python.exe -B -
~~~

<!-- THREE_STATE_FIXED_TRACE_CHECK -->

```python
from datetime import datetime, timezone
import hashlib
import json
import platform
import sympy as s

e, k = s.symbols('e k', positive=True)
q = s.Matrix([[-1-e, 1, e], [1, -2+k, 1-k], [k, 1-e, -1+e-k]])
q0 = q.subs({e: 0, k: 0})
ones = s.ones(3, 1)
weights = s.Matrix([[1-e+2*k-k**2, 1+k-e**2, 1-k+2*e-e*k]])
z = 3+e+2*k-e**2-e*k-k**2
assert q*ones == s.zeros(3, 1)
assert s.trace(q) == -4
assert s.expand(sum(weights)-z) == 0
assert all(s.expand(v) == 0 for v in weights*q)
cofactors = [s.expand((-q).minor_submatrix(i, i).det()) for i in range(3)]
assert cofactors == list(weights)
assert s.expand(z-3-e*(1-e-k)-k*(2-k)) == 0
pi = weights/z
current = (e-k)*(1-e-k)/z
oriented = [(0, 2), (2, 1), (1, 0)]
for i, j in oriented:
    assert s.cancel(pi[i]*q[i,j]-pi[j]*q[j,i]-current) == 0
flux_ratio = s.prod(pi[i]*q[i,j]/(pi[j]*q[j,i]) for i,j in oriented)
assert s.cancel(flux_ratio-e*(1-e)/(k*(1-k))) == 0
observed = s.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
t = q-observed
b = s.Matrix([[1, 0], [0, 1], [0, 0]])
r = s.Matrix([[0, 1, 0], [1, 0, 0]])
control_minor = s.Matrix.hstack(b[:,0], b[:,1], (t*b)[:,1]).det()
observe_minor = s.Matrix.vstack(r[1,:], r[0,:], (r*t)[0,:]).det()
assert s.expand(control_minor-(1-e)) == 0
assert s.expand(observe_minor-(1-k)) == 0
t0 = q0-observed
source_mean_times = (-t0).inv()*ones
assert source_mean_times == s.Matrix([1, 2, 3])
source_control = s.Matrix.hstack(b, t0*b, t0**2*b).rank()
source_observe = s.Matrix.vstack(r, r*t0, r*t0**2).rank()
assert source_control == source_observe == 3
deviations = [-(e-k)*(4-e-2*k), -(e-k)*(1+2*e+k), (e-k)*(5+e-k)]
assert all(s.expand(3*weights[i]-z-deviations[i]) == 0 for i in range(3))
assert s.cancel(current.subs(k, 0)-e*(1-e)/(3+e-e**2)) == 0
result = {
    'executed_at': datetime.now(timezone.utc).isoformat(),
    'python': platform.python_version(), 'sympy': s.__version__,
    'embedded_source_sha256': hashlib.sha256(check_source.encode('utf-8')).hexdigest(),
    'inputs': 'Exact symbolic e,k; analytic domain 0<k<e<1/2; no stochastic inputs',
    'row_sums_zero_and_trace_minus_four': True,
    'stationary_tree_cofactors_and_stationary_equation': True,
    'all_three_oriented_currents_equal': str(s.factor(current)),
    'cycle_flux_ratio': str(s.factor(flux_ratio)),
    'full_order_minors': [str(control_minor), str(observe_minor)],
    'source_full_ranks': [source_control, source_observe],
    'source_next_mark_mean_times': [str(v) for v in source_mean_times],
    'stationary_TV_numerator_factorization': str(deviations[2]),
    'fixed_e_divergence_coefficient': str(s.factor(current.subs(k,0))),
    'all_exact_checks_passed': True,
}
print(json.dumps(result, indent=2))
```

Execution result is recorded below after the actual run. The entropy asymptotic and total-variation inequalities are the analytic arguments above; they are not described as solver-certified results.

Incomplete initial execution: the first extraction used the first marker occurrence, which was the literal in the reproduction command rather than the actual code marker. It evaluated only a harmless string expression and produced no check output; that run established no mathematical result. Extraction was corrected to the last marker occurrence, with a guard requiring the result key to occur in the extracted source.

The corrected execution completed successfully:

```json
{
  "executed_at": "2026-09-10T23:59:18.067990+00:00",
  "python": "3.9.12",
  "sympy": "1.14.0",
  "embedded_source_sha256": "1157e231716af670c1d2c009fab64d6bfc09a154a6118386483c8b219f1dd0fa",
  "inputs": "Exact symbolic e,k; analytic domain 0<k<e<1/2; no stochastic inputs",
  "row_sums_zero_and_trace_minus_four": true,
  "stationary_tree_cofactors_and_stationary_equation": true,
  "all_three_oriented_currents_equal": "(e - k)*(e + k - 1)/(e**2 + e*k - e + k**2 - 2*k - 3)",
  "cycle_flux_ratio": "e*(e - 1)/(k*(k - 1))",
  "full_order_minors": ["1 - e", "1 - k"],
  "source_full_ranks": [3, 3],
  "source_next_mark_mean_times": ["1", "2", "3"],
  "stationary_TV_numerator_factorization": "(e - k)*(e - k + 5)",
  "fixed_e_divergence_coefficient": "e*(e - 1)/(e**2 - e - 3)",
  "all_exact_checks_passed": true
}
```
