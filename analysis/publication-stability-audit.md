# Publication audit: sharp assumptions for entropy stability

Date: 2026-09-11 UTC. Contribution: independent proof audit, exact algebraic checks, and two structural extensions. Mathematical status: conventional proofs with executed exact checks; not formal verification. No literature search or novelty claim is part of this bounded assignment. Existing accepted scripts and outputs are preserved.

## 1. Main conclusions

The fixed-trace three-state divergence and E055's two-hidden-state theorem survive audit. The earlier sufficient rate cap in the positive-three-state continuity result is unnecessary for the joint-kernel metric. A finite rational inverse using **three positive Laplace arguments** recovers every irreducible three-state source locally, including a hidden-leaf tree, with neither a prior rate cap nor previously fixed observed rates. It is locally Lipschitz in row total variation and continuous under weak convergence of the joint row laws. Entropy inherits local Lipschitz continuity at a strictly positive triangle, while paired-zero edges permit unbounded entropy despite continuous generator recovery.

With exactly one known resolved observed pair and unknown competitor topology, this yields a complete criterion for a finite local entropy upper bound at **fixed state count**:

\[
\boxed{\quad N=2\quad\text{or}\quad N=3\text{ with a complete triangle}.\quad}
\tag{1}
\]

The criterion remains exact if competitors must also retain the source's observed rates and trace. It does **not** remain true after adding an arbitrary tighter prescribed rate cap; Section 5 gives an explicit counterexample to that overstatement. For stationary-window TV the saved bounded-rate continuity proof remains the established positive result; the new cap-free inverse uses joint waiting-kernel data and must not silently be transferred to that different experiment.

## 2. Exact audit of the existing divergence mechanisms

### Three-state fixed-trace example

For the source and family in [three-state-fixed-trace-audit.md](three-state-fixed-trace-audit.md), the domain is \(0<k<e<1/2\). The row sums, trace \(-4\), offdiagonal rate cap one, positive bidirected support, stationary tree weights, normalization, common oriented current, and cycle affinity are correct. The explicit minimality minors are \(1-e\) and \(1-k\); there is no repeated-spectrum exception. The source is also minimal three, and [E017](../evidence/RECORDS.md#e017) identifies every individual exact kernel within the cap three.

The correct entropy identity is

\[
\sigma=\frac{(e-k)(1-e-k)}{3+e+2k-e^2-ek-k^2}
\log\frac{e(1-e)}{k(1-k)}.
\]

At fixed \(e>0\), \(k\downarrow0\) has positive divergence coefficient \(e(1-e)/(3+e-e^2)\). The diagonal path \(k=\exp(-1/e^2)\), \(e\downarrow0\), instead gives \(\sigma\sim1/(3e)\) while the generators converge to the source. The distinction between these limits is material: the first proves an unbounded supremum within a fixed positive observation tolerance; the second proves convergence of the observed laws with divergent entropy.

The all-time row-TV bound \(2(e+k)\), original mean next-mark vector \((1,2,3)\), and stationary initial TV \((e-k)(5+e-k)/(3Z)\) are correct. Thus stationary finite-window TV is at most that initial TV plus \((e+k)H\). No microscopic initial-state information is supplied by that stationary statement. Every reverse rate remains positive before the excluded one-way boundary; no floating-point underflow is an admissible substitute for it.

The saved root checker independently solves stationary linear systems at 100 digits and sums edgewise entropy. Its output reports 15 cases for three families, with exact symbolic identities checked first. The fixed-trace family's numerical endpoint \(e=1/2\) lies outside the convenient strict bound in the prose but remains admissible because its actual \(k<e\) and \(e+k<1\); it is not used to extend a theorem silently.

### E055, with no minimality assumption

The [general neighborhood proof](entropy-neighborhood-audit.md) correctly requires two states absent from **all** observed endpoints, not merely an unobserved edge between two states. Completing all unobserved edges while preserving total unobserved rate mass gives the same trace. The asymmetric completion makes the pair's full external exit rows unequal for all sufficiently small positive mixing coefficients, even when the original rows coincide. A possible isolated larger cancellation does not invalidate that small interval.

The explicit unequal-row version of [E032](../evidence/RECORDS.md#e032), inspected in [hidden-pair-boundary-audit.md, Sections 1–3](hidden-pair-boundary-audit.md), supplies a complete, fixed-kernel family with positive limiting stationary masses and one vanishing reverse flux. It needs no minimality. The perturbation size is chosen first, and its entropy-divergent pair-mixing limit second. This avoids relying on a coefficient remaining positive uniformly as the perturbation tends to zero.

The integrated Duhamel bound
\(\operatorname{TV}_I\le\varepsilon[R(-T)^{-1}|G-Q|\mathbf1]_I/2\)
is valid because the killed semigroups are positive and
\(\int e^{T_\varepsilon t}B\mathbf1\,dt=\mathbf1\).
The equivalent weaker common/excess-clock hazard bound is correct, including diagonal row normalization. Trace preservation and nonnegative rates give the common cap \(-\operatorname{tr}Q\); this is a sufficient cap constructed by the theorem, not every cap containing the source.

## 3. New exact finite-Laplace inverse: remove the prior rate cap

Use observed marks \(+=(x,y),-=(y,x)\), with rates \(r,s>0\), and write

\[
Q=\begin{pmatrix}
-r-a&r&a\\s&-s-c&c\\b&d&-b-d
\end{pmatrix},\qquad h=b+d>0.
\]

The source is irreducible and bidirected, so \(a+c>0\). One of \(a,c\) may be zero; its reverse rate is then zero as well. Neither \(r,s\) nor a global upper rate bound needs to be known in advance.

Let \(P\) swap the two mark rows and let
\(F(\lambda)=P\widehat\Psi(\lambda)\).
The visible principal resolvent \(K\) satisfies
\(F=K\operatorname{diag}(r,s)\).
Put \(H=F^{-1}\). The Schur complement gives

\[
K^{-1}=\begin{pmatrix}\lambda+r+a&0\\0&\lambda+s+c\end{pmatrix}
-\frac1{\lambda+h}\binom a c(b,d).
\tag{2}
\]

For \(\lambda>0\), its offdiagonal entries are nonpositive and its row sums are strictly positive; it is strictly row diagonally dominant and nonsingular. Thus inversion of \(F\) is legitimate at all arguments used below. In particular

\[
G_x(\lambda)=\frac{(H\mathbf1)_x-1}{\lambda}
=\frac1r+\frac{a/r}{\lambda+h},\qquad
G_y(\lambda)=\frac1s+\frac{c/s}{\lambda+h}.
\tag{3}
\]

Fix any three distinct positive arguments \(\lambda_1<\lambda_2<\lambda_3\). Select a row corresponding to a **positive source entrance**, and write its expression as \(G=u+v/(\lambda+h)\), \(v>0\). Then

\[
\mathcal R=\frac{G(\lambda_1)-G(\lambda_2)}{G(\lambda_2)-G(\lambda_3)}
\frac{\lambda_3-\lambda_2}{\lambda_2-\lambda_1}
=\frac{\lambda_3+h}{\lambda_1+h}>1,
\]
\[
h=\frac{\lambda_3-\mathcal R\lambda_1}{\mathcal R-1}.
\tag{4}
\]

For each row, including a possible zero-entrance row, recover

\[
v_i=[G_i(\lambda_1)-G_i(\lambda_2)]
\frac{(\lambda_1+h)(\lambda_2+h)}{\lambda_2-\lambda_1},
\qquad u_i=G_i(\lambda_1)-\frac{v_i}{\lambda_1+h}.
\]

Hence \(r=1/u_x\), \(s=1/u_y\), \(a=v_x/u_x\), and \(c=v_y/u_y\). If the selected positive entrance is \(a\),

\[
d=-rH_{xy}(\lambda_1)\frac{\lambda_1+h}{a},\qquad b=h-d;
\]

if it is \(c\), instead use
\(b=-sH_{yx}(\lambda_1)(\lambda_1+h)/c\), \(d=h-b\).
No division by a disappearing entrance is required.

All expressions are rational in the entries of \(\widehat\Psi\) at these three arguments. At the source their denominators are strictly nonzero: the three \(F\) matrices are invertible; the chosen row's differences are positive; \(\mathcal R-1>0\); \(u_x,u_y>0\); and the selected entrance is positive. They therefore define a locally Lipschitz inverse in a neighborhood of the source's finite transform data. Each transform entry is a bounded linear functional of a joint row law and is Lipschitz in its TV distance. Thus

\[
d(\Psi_n,\Psi_*)\to0\quad\Longrightarrow\quad Q_n\to Q_*;
\]

locally the generator error is bounded by a source-dependent finite constant times row TV. This does not assert a uniform condition number across nearly degenerate sources. It also holds with **weak row-law convergence**, since \(e^{-\lambda t}\mathbf1_{\{J\}}\) is bounded and continuous on the product of nonnegative times and the finite mark set.

Two-state candidates have both \(G_i\) constant and cannot approach the nonzero chosen source differences at the three fixed arguments. Thus the same local conclusion holds for candidates under a cap of three. A two-state **source** under cap three is a different boundary: the selected positive-entrance assumption fails, as it should, and the known rare-state example remains possible.

At a full triangle all rates recovered above are eventually bounded away from zero. Its stationary law is a smooth normalized solution of a nonsingular reduced linear system; the logarithmic entropy expression is smooth there. Entropy is consequently locally Lipschitz in row TV, with no prior trace or upper-rate restriction. At a tree only generator recovery is locally Lipschitz; entropy need not even be locally bounded.

As an independent check for positive triangles, a same-direction scalar entry has the form
\(\widehat\psi_{--}(\lambda)=s a d/\det(\lambda I-T)\).
Its reciprocal is a cubic. Four finite positive Laplace values determine its coefficients; the ratio of its quadratic to cubic coefficient equals \(-\operatorname{tr}Q\). Convergence to a positive triangle therefore forces bounded rates automatically, agreeing with the sharper three-argument inverse. The latter additionally covers a tree and avoids any assumption about recovering time derivatives under TV convergence.

## 4. A general missing-edge theorem and the exact criterion

**Generator-level theorem.** At an irreducible bidirected source with unknown topology and fixed state count, entropy is locally upper-bounded in the generator-entry topology if and only if its support is complete. This remains true under exactly fixed trace and the original maximum offdiagonal rate cap.

For a complete source this follows from continuity on its positive interior. For a noncomplete connected source choose a missing pair \(i,j\), set its rates to \(e\) and \(k(e)=\exp(-1/e^2)\), and subtract \(e+k(e)\) from one existing positive ordered rate. For sufficiently small \(e\), that old rate stays positive and all source edges remain present. Bidirectionality, irreducibility and trace are preserved; choosing the new rates below the source maximum preserves that cap. The perturbed generators converge entrywise to the irreducible source, so \(\pi(e)\to\pi^0>0\). The new edge contributes

\[
[\pi_i(e)e-\pi_j(e)k(e)]
\log\frac{\pi_i(e)e}{\pi_j(e)k(e)}
\sim\frac{\pi_i^0}{e}\to\infty.
\tag{5}
\]

All other edge contributions are nonnegative (and old supported-edge contributions remain finite), so the total entropy diverges. Full stationary microscopic finite-window path laws converge in TV by an initial maximal coupling and a common/excess-clock coupling. This sparse-boundary mechanism is therefore not specific to hidden observation.

To retain specified observed rates as well as trace, choose the compensating positive ordered edge **outside the observed set**. Such an edge always exists for a connected source with exactly one observed pair and \(N\ge3\). The missing pair is also unobserved. Then the same coupling up to the next source mark gives joint-kernel TV tending to zero. If every positive source edge were observed and its rate frozen, fixed trace could forbid adding a chord; full microscopic observation with approximately rather than exactly fixed rates must not be confused with that stronger restriction.

For clarity, a general three-state leaf \(x-y-h\) with source rates \(r,s,c,d>0\) admits the explicit fixed-trace version

\[
Q(e,k)=\begin{pmatrix}
-r-e&r&e\\
s&-s-c+e+k&c-e-k\\
k&d&-k-d
\end{pmatrix},\quad 0<e+k<c.
\tag{6}
\]

Its oriented current numerator is \(e d s-k r(c-e-k)\), and its affinity is
\(\log[e d s/(k r(c-e-k))]\).
Along \(k=\exp(-1/e^2)\), entropy is asymptotic to
\(s d/[e(s d+r d+r c)]\). The observed rates, original trace and original maximum rate cap are retained for small \(e\). The other leaf orientation follows by relabeling.

Now define a robust finite upper ceiling to mean that some positive row-TV neighborhood of the source has finite entropy supremum in the declared fixed-\(N\) class. For exactly one known observed pair:

- \(N=2\): all models have entropy zero.
- \(N=3\), complete source: Section 3 gives local entropy continuity even in the unrestricted rate class.
- \(N=3\), tree source: (6) gives unbounded entropy in every neighborhood, preserving observed rates and trace.
- \(N\ge4\): there are at least two fully hidden states, so E055 gives unbounded entropy in every neighborhood, preserving observed rates and trace.

This proves (1) both for unrestricted finite rates and for the exact-source-trace/observed-rate subclass. It covers arbitrary fixed \(N\), not only \(N\le6\). It does not claim a corresponding classification for more observed pairs, different known incidence, a prescribed sparse topology, or additional individual rate restrictions.

## 5. Necessary caveats and rejected generalizations

**A prescribed small cap can change the criterion.** Take \(N=4\) and all twelve offdiagonal rates equal to one. If competitors must have trace \(-12\) and every rate at most one, the sum of twelve bounded rates can equal twelve only when all twelve equal one. This restricted class is a singleton with entropy zero, despite two fully hidden states for one observed pair. E055's sufficient cap is \(-\operatorname{tr}Q=12\), not the arbitrarily tighter cap one. The classification above therefore must not be advertised as valid under every cap merely containing the source.

**Positive floors:** with supported rates between \(m>0\) and \(M<\infty\), stationary cancellation gives \(\sigma\le A\log(M/m)\), where \(A\) is total stationary jump activity and \(A\le(N-1)M\). Trace \(-\tau\) improves this to \(A\le\tau\). A floor removes the boundary mechanism and changes the problem.

**Fixed topology:** at an irreducible generator with fixed bidirected support, its positive supported rates have a neighborhood bounded away from zero, so generator-level entropy is continuous even on a tree. Global observation-level continuity in larger hidden models is a different question; exact hidden ambiguity can survive a fixed topology.

**Closure and weak convergence:** all proposed divergence sequences remain admissible before their limiting paired-zero/one-way edge boundary. Entropy is evaluated before that boundary. The three-argument inverse assumes a genuinely irreducible three-state source, proper joint row laws, fixed resolved incidence and state cap three. Weak row-law convergence is enough for its bounded Laplace tests; it is not a statement that numerical differentiation is weakly continuous.

**Stationary finite windows:** the saved common-rate-cap proof in [one-hidden-robustness-audit.md](one-hidden-robustness-audit.md) correctly uses compactness of \((Q_n,\pi_n)\), uniform integrability of observed counts, and the consecutive-mark Palm identity \((H-t)\nu_I\psi_{IJ}(t)\,dt\). A limiting closed generator need not initially be irreducible; E017 reconstructs it as the irreducible source. The new finite-Laplace inverse does not by itself extract infinite-time kernel transforms from one fixed window. Removing the window proof's cap is left unresolved here rather than claimed by analogy. A fixed \(H>0\) is required; at \(H=0\) there is no informative stationary-window experiment.

**Confidence claims:** uniform modelwise finite-sample coverage, stationary initialization, fixed finite horizon and a measurable extended-real upper limit are required for the saved impossibility statement. Pointwise/asymptotic coverage, known microscopic hidden initialization and a jointly diverging horizon are distinct claims. Local entropy continuity at positive three-state triangles does not imply the existence of a globally honest almost-surely finite confidence limit.

## 6. Inputs inspected and reproducible exact checks

Read during this audit or the immediately preceding bounded derivations: `AGENTS.md`, `PROJECT.md`, `STATE.md`, `docs/research-stack.md`, `analysis/formulation.md`, `analysis/compatibility-orbit.md`, `analysis/small-network-audit.md` (E017), `analysis/hidden-pair-boundary-audit.md` (E032), `evidence/RECORDS.md` (especially E017/E032/E055–E058), `analysis/entropy-neighborhood-audit.md`, `analysis/three-state-fixed-trace-audit.md`, `analysis/one-hidden-robustness-audit.md`, `analysis/three-state-precision-audit.md`, `analysis/check_three_state_precision.py`, `outputs/three-state-precision-checks.json`, `analysis/check_finite_precision_instability.py`, and `outputs/finite-precision-checks.json`.

The initially guessed filenames `analysis/check_three_state_robustness.py` and `outputs/three-state-robustness-checks.json` did not exist; `rg --files` located the correct precision filenames. This was a file-discovery miss, not failed scientific evidence.

The fresh checker below verifies the three-argument inverse against the direct resolvent, both tree orientations and a fast-hidden rational example; checks the independent reciprocal-cubic trace identity; verifies the generic compensated-tree current/trace; and checks accepted source hashes without rerunning or overwriting accepted numerical outputs. It is exact arithmetic and has no RNG, grid search, optimizer, or tolerance-based existence claim.

~~~powershell
@'
from pathlib import Path
note = Path('analysis/publication-stability-audit.md').read_text(encoding='utf-8')
check_source = note.rsplit('<!-- PUBLICATION_STABILITY_CHECK -->', 1)[1].split('```python', 1)[1].split('```', 1)[0]
assert 'all_exact_checks_passed' in check_source
exec(compile(check_source, '<publication-stability-check>', 'exec'))
'@ | .\.venv\Scripts\python.exe -B -
~~~

<!-- PUBLICATION_STABILITY_CHECK -->

```python
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, platform
import sympy as S

r,s,a,c,b,d,L = S.symbols('r s a c b d lambda', positive=True)
h = b+d
T = S.Matrix([[-r-a,0,a],[0,-s-c,c],[b,d,-h]])
K = (L*S.eye(3)-T).inv()[:2,:2]
F = K*S.diag(r,s)
M = S.diag(L+r+a,L+s+c)-S.Matrix([a,c])*S.Matrix([[b,d]])/(L+h)
H = S.diag(1/r,1/s)*M
assert (F*H-S.eye(2)).applyfunc(S.cancel) == S.zeros(2)
gx,gy = [S.cancel(((H*S.ones(2,1))[i]-1)/L) for i in range(2)]
assert S.cancel(gx-1/r-a/(r*(L+h))) == 0
assert S.cancel(gy-1/s-c/(s*(L+h))) == 0
D = (L*S.eye(3)-T).det()
assert S.cancel(F[0,1]-s*a*d/D) == 0
reciprocal = S.Poly(S.expand(D/(s*a*d)),L)
assert S.cancel(reciprocal.coeff_monomial(L**2)/reciprocal.coeff_monomial(L**3)+S.trace(T)) == 0

u,v,h0,l1,l2,l3 = S.symbols('u v h0 l1 l2 l3', positive=True)
g = lambda z: u+v/(z+h0)
ratio = S.cancel((g(l1)-g(l2))/(g(l2)-g(l3))*(l3-l2)/(l2-l1))
assert S.cancel(ratio-(l3+h0)/(l1+h0)) == 0
hrec = S.cancel((l3-ratio*l1)/(ratio-1))
vrec = S.cancel((g(l1)-g(l2))*(l1+hrec)*(l2+hrec)/(l2-l1))
urec = S.cancel(g(l1)-vrec/(l1+hrec))
assert hrec == h0 and vrec == v and urec == u

arguments = [S.Rational(1),S.Rational(2),S.Rational(4)]
cases = [(1,1,0,1,0,1),(2,3,4,0,5,0),(2,3,4,5,6,7),
         (1,1,1,1,1,1),(1,2,3,4,100000,200000)]
for values in cases:
    sub = dict(zip((r,s,a,c,b,d),map(S.Rational,values)))
    ff = [F.subs(sub).subs(L,z) for z in arguments]
    hh = [x.inv() for x in ff]
    gg = [[S.cancel(((hh[j]*S.ones(2,1))[i]-1)/arguments[j])
           for j in range(3)] for i in range(2)]
    branch = 0 if gg[0][0] != gg[0][1] else 1
    gr = gg[branch]
    rr = (gr[0]-gr[1])/(gr[1]-gr[2])*2
    recovered_h = S.cancel((4-rr)/(rr-1))
    vv = [S.cancel((q[0]-q[1])*(1+recovered_h)*(2+recovered_h)) for q in gg]
    uu = [S.cancel(gg[i][0]-vv[i]/(1+recovered_h)) for i in range(2)]
    ro,so = [S.cancel(1/x) for x in uu]
    ao,co = [S.cancel(vv[i]/uu[i]) for i in range(2)]
    if branch == 0:
        do = S.cancel(-ro*hh[0][0,1]*(1+recovered_h)/ao)
        bo = S.cancel(recovered_h-do)
    else:
        bo = S.cancel(-so*hh[0][1,0]*(1+recovered_h)/co)
        do = S.cancel(recovered_h-bo)
    assert tuple((ro,so,ao,co,bo,do)) == values

e,k = S.symbols('e k', positive=True)
qt = S.Matrix([[-r-e,r,e],[s,-s-c+e+k,c-e-k],[k,d,-k-d]])
assert qt*S.ones(3,1) == S.zeros(3,1)
assert S.trace(qt) == -r-s-c-d
weights = S.Matrix([[S.expand((-qt).minor_submatrix(i,i).det()) for i in range(3)]])
Z = sum(weights)
assert (weights*qt).applyfunc(S.expand) == S.zeros(1,3)
J = (e*d*s-k*r*(c-e-k))/Z
for i,j in ((0,2),(2,1),(1,0)):
    assert S.cancel(weights[i]*qt[i,j]/Z-weights[j]*qt[j,i]/Z-J) == 0
assert S.expand(Z.subs({e:0,k:0})-(s*d+r*d+r*c)) == 0

accepted = []
for script,output in [('analysis/check_three_state_precision.py','outputs/three-state-precision-checks.json'),
                      ('analysis/check_finite_precision_instability.py','outputs/finite-precision-checks.json')]:
    record = json.loads(Path(output).read_text(encoding='utf-8'))
    actual = hashlib.sha256(Path(script).read_bytes()).hexdigest()
    assert actual == record['script_sha256']
    accepted.append({'script':script,'sha256':actual,'output':output})
print(json.dumps({'executed_at':datetime.now(timezone.utc).isoformat(),
    'python':platform.python_version(),'sympy':S.__version__,
    'embedded_source_sha256':hashlib.sha256(check_source.encode()).hexdigest(),
    'direct_resolvent_three_laplace_inverse':True,
    'inverse_rational_cases':len(cases),'both_leaf_orientations_and_fast_hidden_case':True,
    'reciprocal_cubic_trace_identity':True,'compensated_tree_stationarity_current_trace':True,
    'accepted_script_hash_checks':accepted,'all_exact_checks_passed':True},indent=2))
```

Fresh execution results follow after the actual run. The conventional continuity, compactness qualifications, topology theorem and divergent limits are not solver-certified by these algebraic checks.

The fresh exact execution passed without an unsuccessful mathematical run:

```json
{
  "executed_at": "2026-09-11T01:03:45.200041+00:00",
  "python": "3.9.12",
  "sympy": "1.14.0",
  "embedded_source_sha256": "4916bee2f8528b1f1812aa6e72eaafda62eff256c3c3f7cf6281a5caf6690bee",
  "direct_resolvent_three_laplace_inverse": true,
  "inverse_rational_cases": 5,
  "both_leaf_orientations_and_fast_hidden_case": true,
  "reciprocal_cubic_trace_identity": true,
  "compensated_tree_stationarity_current_trace": true,
  "accepted_script_hash_checks": [
    {
      "script": "analysis/check_three_state_precision.py",
      "sha256": "026f0ea82f3df3e7ef3212bb705fb5ef6e04d128f64316404d416f46565529fd",
      "output": "outputs/three-state-precision-checks.json"
    },
    {
      "script": "analysis/check_finite_precision_instability.py",
      "sha256": "f4aaac3e9e4d6554250a8425c3f43c9cf6f1ec50f138400d1f9ebe92b4930747",
      "output": "outputs/finite-precision-checks.json"
    }
  ],
  "all_exact_checks_passed": true
}
```
