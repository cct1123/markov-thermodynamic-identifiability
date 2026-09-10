# Sharp balanced-ray invariant-triangle bound

Date: 2026-09-10 UTC. Contribution: analytic exclusion, equality classification and subcritical existence, with exact algebraic checks. Mathematical status: conventionally proved by the argument below, independently reviewed by the coordinator and boundary auditor; not formally verified. No novelty claim. This note uses the modal/cone reduction already proved in [the global spectral audit](theta-fast-spectral-audit.md), and does not repeat its realization-minimality proof.

## Statement and scope

Write the balanced source as `Q(z,z)` in the existing audit, and retain its admissible class: finite irreducible simple bidirected CTMCs, one resolved observed reverse pair, exact all-time joint next-mark/time kernels, and at most five physical states. Put

\[
\rho=\sqrt6,\quad r_y=4(\rho-1)/5,\quad m=(7+2\rho)/5,
\quad L=(3-\rho/2)/8,\quad R=35\rho/88,
\]
\[
A=z,\quad B=z/r_y,\quad k=(2z-9+2\rho)/(4\rho),
\quad a=k-1,\quad J=am+k.
\]

Let \(z_*\) be the unique positive real root of

\[
\mathcal P(z)=352z^4-3168z^3-4644z^2-11340z-7623.
\tag{1}
\]

Numerically \(z_*=10.5571496686650\). Every compatible model with connected hidden support is impossible for \(z>z_*\). At \(z=z_*\), there is **at most one** compatible connected-hidden generator up to hidden labels. The latter conclusion is an equality classification, not by itself an existence assertion. Its only possible support is a hidden path with the center attached only to \(x\), one endpoint only to \(y\), and the other endpoint attached to both visible states.

The argument derives a necessary quadratic feasibility condition for every \(z\ge21/2\). Section 6 additionally proves **complete compatible generators for every \(21/2\le z<z_*\)**, and hence unbounded entropy throughout this interval. This overlaps the previously proved unbounded interval and closes the saved balanced-ray gap. Disconnected-hidden rigidity from the previous audit implies global generator uniqueness for every \(z>z_*\), without any optimizer-based premise. Existence and entropy at the equality parameter remain separate boundary-witness checks.

## Falsification condition and tools

For a counterexample to the bound, it suffices to exhibit a finite nondegenerate triangle with origin in its interior, containing \((1,A),(-m,B)\), contained in
\(v\ge L(-m-u),\ v\ge R(u-1)\), and invariant under the flow
\((u,v)\mapsto(e^{-t}u,e^{-kt}v)\), at some \(z>z_*\). Any physical connected-hidden counterexample necessarily produces such a triangle; reciprocal support is retained in the final equality analysis, and is not needed for exclusion. All dimensions and zero-rate strata therefore remain covered by the inherited cone reduction. A numerical approximate marked-kernel match is not this exact falsification condition.

The weakest sufficient route was planar inequalities plus exact polynomial algebra. No parameter search, graph enumeration, or optimizer is used to certify nonexistence. The former local-opening threshold is not assumed globally sharp: it emerges below as the limiting case of a cone vertex approaching infinity. The coordinating agent independently derived the same quartic from a physical hidden-path exit-coordinate calculation; agreement shares the original theta inputs but uses a different formulation.

## 1. Exhaust the bottom-vertex signs

The previous audit proves that the triangle's vertices can be labelled

\[
(-\ell,P),\quad(c,Q),\quad(d,-W),
\qquad \ell\ge m,\ c\ge1,\ -m<d<1,\ P,Q,W>0.
\]

Its necessary inequalities include

\[
P\ge L(\ell-m),\quad W\le\min\{L(m+d),R(1-d)\}<1,
\tag{2}
\]
\[
(a\ell+kd)P\le\ell W,\qquad(ac-kd)Q\le cW,
\tag{3}
\]
\[
B\le H(\ell,P,c,Q):=
\frac{(c+m)P+(\ell-m)Q}{\ell+c},
\qquad
Q\le\frac{A+W}{1-d}(c-d)-W.
\tag{4}
\]

If \(d<0\), equation (14) of the existing spectral audit gives

\[
z<\frac{25/8+(25/18)(z+1)}{z-7}.
\]

This is impossible already for \(z\ge10\), because the reversed strict difference has positive numerator
\(72z^2-604z-325=72(z-10)^2+836(z-10)+835\).
Hence throughout the range of this note \(d\ge0\).

Now \(a>7/10\), so (2)-(3) give \(P\le W/a<10/7<2\). Also \(B>5z/6>2\), and \(A>B\). Upper containment of \((1,A)\) therefore forces \(Q\ge A\); upper containment of \((-m,B)\) forces \(\ell>m\).

## 2. The bottom lies to the right of the wedge apex

Set \(\epsilon=1-d\in(0,1]\). From the second inequality (3), \(c\ge1\), \(Q\ge A\), and \(aQ-W>0\),

\[
\epsilon\le\frac{A+W}{kA}
\le\frac{A+R\epsilon}{kA},\qquad
\epsilon\le\frac1{k-R/A}.
\tag{5}
\]

The wedge apex has coordinate

\[
d_0=\frac{R-Lm}{L+R},\qquad
\epsilon_0=1-d_0=\frac{L(m+1)}{L+R}.
\]

The exact inequality
\(1/(k(21/2)-R/(21/2))<\epsilon_0\) is checked in the accompanying script. For \(z\ge21/2\), \(k-R/z\) is strictly increasing. Thus (5) implies \(d>d_0>0\), and consequently the tighter bottom bound is always

\[
W\le R\epsilon.
\tag{6}
\]

All signs used to divide in (5) are strict: \(kA-R>0\), \(aQ-W>0\), and \(A>0\).

## 3. Maximize the upper containment bound exactly

Fix an admissible \(d,W\). First maximize over the left vertex. The function

\[
g(\ell)=\frac{\ell W}{a\ell+kd}
\]

is strictly increasing and concave because \(d>0\). Equations (2)-(3) imply \(L(\ell-m)\le g(\ell)\). This holds precisely up to the unique intersection \(\ell_* =m+t\), \(t>0\), where

\[
P_*=Lt=g(m+t),\qquad
Lt[a(m+t)+kd]=(m+t)W.
\tag{7}
\]

Uniqueness also follows directly because the equation for \(t\) is a quadratic with positive leading coefficient and negative constant. Thus \(\ell\le\ell_*\), \(P\le P_*<2\). For fixed \(c,Q\), both partial derivatives of \(H\) with respect to \(P\) and \(\ell\) are strictly positive when \(Q>P\):

\[
H_P=\frac{c+m}{\ell+c}>0,\qquad
H_\ell=\frac{(c+m)(Q-P)}{(\ell+c)^2}>0.
\]

We may therefore replace the left vertex by \((\ell_*,P_*)\) to obtain an upper bound. This relaxation is valid even if the enlarged triangle violates some condition not used here.

For the right vertex put \(q=(A+W)/\epsilon\). Equations (3)-(4) give an increasing linear bound \(Q\le q(c-d)-W\) and, when \(ac-kd>0\), a decreasing bound \(Q\le cW/(ac-kd)\). They meet at exactly

\[
c_* =\frac{k}{a}\left[d+\frac{W\epsilon}{A+W}\right],
\qquad
Q_* =\frac{Ad+W}{a\epsilon}.
\tag{8}
\]

The meeting point is strictly to the right of the pole \(kd/a\). If \(c_*<1\), the decreasing bound is already below \(A\) at \(c=1\), contradicting \(Q\ge A\). Thus \(c_*\ge1\).

Along the linear bound, \(H\) increases strictly with \(c\), since its derivative has positive numerator
\((\ell_*-m)[q(\ell_*+d)+W+P_*]\).
Along the decreasing bound, \(H\) decreases strictly whenever \(Q>P_*\): both its direct decrease with \(c\) and its positive dependence on \(Q\) have that sign. A point with \(Q\le P_*\) cannot attain \(B>2>P_*\). Therefore the largest possible upper bound in (4) is attained uniquely at (8).

It remains to maximize over \(W\). Write \(r=c_*/Q_*=k\epsilon/(A+W)\). The resulting envelope is

\[
H_* =\frac{t[Lm+(1+Lr)Q_*]}{m+t+rQ_*}.
\tag{9}
\]

Increasing \(W\) strictly increases \(t\) in (7), strictly increases \(Q_*\), and strictly decreases \(r\). In (9), the partial derivatives with respect to \(t,Q_*\) are positive. The partial derivative with respect to \(r\) has sign \(Lt-Q_*\), which is negative since \(Lt<2<A\le Q_*\). These inequalities remain valid while \(W\) is increased up to its allowed maximum. Hence the envelope strictly increases with \(W\). Its maximum occurs at

\[
W=R\epsilon.
\tag{10}
\]

This completes the optimization without assuming that any extremal triangle is physically realizable.

## 4. A quadratic feasibility certificate

Using (10) in (7), solve for the bottom coordinate:

\[
\epsilon=\frac{Lt(J+at)}{Rm+(kL+R)t},\qquad t>0.
\tag{11}
\]

All factors in this fraction are positive. Substitute (11) into (8)-(9). Direct rational simplification gives

\[
H_*-B=\frac{f_0+f_1t+f_2t^2}{(J+at)^2},
\tag{12}
\]

where

\[
f_0=ARm/L-BJ^2,
\]
\[
f_1=A(R/L+k-am)+LJ^2+RJ-2BJa,
\]
\[
f_2=a[LJ+R-A(1+Lk/R)-Ba].
\tag{13}
\]

Consequently every feasible connected-hidden triangle for \(z\ge21/2\) necessarily has a strictly positive \(t\) with
\(f_0+f_1t+f_2t^2\ge0\). The script checks (12) first with independent symbolic parameters \(A,k,m,L,R,t\), before substituting theta constants.

The exact coefficients satisfy

\[
f_0=-\frac{19+9\sqrt6}{100}\,z
\left(z^2-11z+\frac{211}{44}\right),
\tag{14}
\]
\[
f_1^2-4f_0f_2=
-\left(\frac{11}{1200}+\frac{11\sqrt6}{4200}\right)
\left(z+\frac{19}{22}\right)^2\frac{\mathcal P(z)}{352}.
\tag{15}
\]

The quartic has exactly one positive root by Descartes' rule of signs and changes sign from negative to positive there. Exact rational evaluations isolate its root between `10.55714966866` and `10.55714966867`. The positive root of the quadratic in (14) is the old local-opening threshold, and is strictly smaller than this interval. Therefore for every \(z>z_*\), \(f_0<0\) and the discriminant (15) is negative. The entire real quadratic is then strictly negative. This contradicts necessary condition (12), and proves exclusion.

The limiting case \(t\downarrow0\) in (12) is precisely the old local-opening condition \(f_0\ge0\). A finite \(t\) can raise the envelope, so treating that local threshold as globally sharp was an invalid conjecture. The exact quartic quantifies the small remaining interval; it is not inferred from a failed search.

## 5. Equality classification at the quartic root

At \(z=z_*\), exact isolating-interval checks give \(f_1>0\), \(f_2<0\). The quadratic in (12) is nonpositive and has exactly one zero,

\[
t_*=-f_1/(2f_2)>0.
\tag{16}
\]

If a feasible connected-hidden triangle exists at this parameter, every inequality in the chain
\(B\le H\le H_*\le\max_W H_*\le B\) must be equality. The strict monotonicity established above forces, uniquely:

- \(\ell=m+t_*\), \(P=Lt_*\), and equality in the left invariance inequality;
- the unique \(\epsilon\) of (11), \(d=1-\epsilon\), and \(W=R\epsilon\);
- \(c=c_*\), \(Q=Q_*\), with equality in the right invariance inequality and in the lower containment bound for input \((1,A)\);
- input \((-m,B)\) on the upper segment between the two positive vertices.

Thus the modal triangle is unique, up to vertex permutation. Its active conditions have direct reciprocal-support meaning. The left vertex lies on the left output face, so its visible entrance from \(x\) is zero; input \((1,A)\) lies on the opposite edge, so its exit to \(x\) is zero. The bottom vertex lies on the right output face, so its entrance from \(y\) is zero; input \((-m,B)\) lies on the opposite upper edge, so its exit to \(y\) is zero. The two tangency equalities delete both directions of the edge between the upper vertices. The possible physical hidden support is therefore the path stated above.

These zeros alone do not establish strict positivity of every remaining rate, origin interior, or existence. Those are separate checks for a boundary witness. If that witness exists, however, there cannot be another modal triangle at this parameter. Positive rescaling of columns does not create another normalized CTMC: for fixed \(\bar H=V^{-1}DV\), \(\bar Y=V^{-1}Y_m\), row normalization requires the unique scaling vector \(w=-\bar H^{-1}\bar Y\mathbf1\). The eigenvalues are nonzero, so this normalization is unique; physical irreducibility requires its coordinates positive. Thus the equality classification gives at most one connected-hidden generator, rather than just one cone shape.

## 6. Sufficiency below the fold: complete compatible generators

Fix any \(z\in[21/2,z_*)\). On the entire rational enclosure
\([10.5,10.55714966867]\), the separate exact interval checker establishes
\(f_1>0\) and \(f_2<0\). Since \(\mathcal P(z)<0\), (15) gives a strictly positive discriminant. Choose

\[
t=-f_1/(2f_2)>0.
\]

Then \(f_0+f_1t+f_2t^2=-(f_1^2-4f_0f_2)/(4f_2)>0\). Define \(\epsilon,d,W,\ell,P,c,Q\) by (7)-(11) with \(W=R\epsilon\). Equation (12) shows that input \((-m,B)\) is strictly below the upper edge. This is a strict feasibility margin for each fixed \(z<z_*\); it is not claimed uniform as \(z\uparrow z_*\).

The exact interval checker verifies the other necessary geometric conditions simultaneously on the entire larger closed rational enclosure. In particular, \(0<\epsilon<1\), \(c>1\), and all undesignated output and input margins are strictly positive. The conditions verified explicitly are:

\[
L(m+d)-W>0,\qquad Q-R(c-1)>0,
\]
\[
B+W-\frac{P+W}{\ell+d}(d+m)>0,
\]
\[
\frac{(c-1)P+(\ell+1)Q}{\ell+c}-A>0.
\tag{17}
\]

They say that the bottom vertex is strictly above the other output face, the right vertex is strictly above its nontrivial output face, input \((-m,B)\) is strictly above the left lower face, and input \((1,A)\) is strictly below the upper face. The remaining output/input inequalities have manifest positive signs: the left vertex's right-output margin is \(P+R(\ell+1)>0\), the right vertex's left-output margin is \(Q+L(m+c)>0\), input \((1,A)\) is above the left lower face since \(1>d\), and input \((-m,B)\) is above the right lower face since \(-m<d\).

There is no degeneracy of the triangle. Put \(p=(P+W)/(\ell+d)\), \(q=(Q+W)/(c-d)\). The two tangencies yield \(p\ell=kP\) and \(qc=kQ\). Therefore the lower-face margins of the origin are exactly

\[
W-pd=aP>0,\qquad W+qd=aQ>0.
\tag{18}
\]

The upper face is above the origin because both upper vertex heights are positive. Thus the origin is strictly inside a finite nondegenerate triangle. At its bottom vertex the two inward flow derivatives are

\[
kW-pd=a(W+P)>0,\qquad kW+qd=a(W+Q)>0.
\tag{19}
\]

The two upper-edge inward derivatives at the upper vertices are also strictly positive: up to the positive divisor \(\ell+c\), their negatives in the outward convention are
\([a\ell+kc]P+\ell Q\) and \([k\ell+ac]Q+cP\). At each upper vertex the remaining inward derivative is zero by tangency. These six vertex-face derivative conditions are sufficient for invariance of a convex triangle under this linear flow. The only output equalities are at the left and bottom vertices, and the only input equality is input \((1,A)\) on the right lower edge. The other input is strictly interior.

This intermediate triangle is a useful nonnegative realization, but need not obey reciprocal support: the bottom output to \(y\) is zero while input \((-m,B)\) has a positive bottom barycentric coordinate. We therefore do **not** treat this intermediate object as the requested physical model. The following explicit perturbation opens every entry, retaining exact transfer equality:

1. Keep \(d\) fixed and decrease \(W\) slightly below \(R\epsilon\). Recompute the unique left intersection (7) and right intersection (8). All strict inequalities above persist by continuity, including \(B<H_*\), while the bottom vertex becomes strictly interior to both output faces.
2. Decrease \(\ell\) slightly below its recomputed intersection value, retaining \(\ell>m\), and choose
   \[
   P=\tfrac12\left[L(\ell-m)+\frac{\ell W}{a\ell+kd}\right].
   \]
   The two bracketed quantities now obey a strict inequality. Consequently the left output and left lower-face invariance conditions both become strict. This choice converges continuously to the previous left vertex as the decrease tends to zero.
3. Keep \(c=c_*\) and decrease \(Q\) slightly below \(Q_*\). At this crossover \(ac-kd>0\), so decreasing \(Q\) makes the right invariance inequality strict. It also makes input \((1,A)\) strictly above the right lower edge. The already strict upper containment, other input/output conditions, and remaining invariance conditions persist by continuity.

At each step, a sufficiently small positive change exists because only finitely many strict continuous inequalities must be preserved, with positive margins at the fixed parameter. No uniform perturbation size in \(z\) is needed. After these steps, all three vertices lie strictly inside the output wedge, both inputs lie strictly inside the triangle, and every inward vertex-face derivative is strictly positive.

Let \(V\) have the resulting modal vertex columns \((1,u_i,v_i)^T\). Then \(\bar X=X_mV>0\), \(\bar Y=V^{-1}Y_m>0\), and \(\bar H=V^{-1}DV\) has all six offdiagonal entries strictly positive. Invertibility follows from nondegeneracy. Its eigenvalues are the three fixed negative modal eigenvalues, so \(\bar H\) is Hurwitz. Since it is irreducible Metzler, \(-\bar H^{-1}>0\); hence the normalization vector \(w=-\bar H^{-1}\bar Y\mathbf1\) is strictly positive. With \(S=\operatorname{diag}(w)\), the physical hidden blocks

\[
H'=S^{-1}\bar H S,\quad X'=\bar X S,\quad Y'=S^{-1}\bar Y
\]

are strictly positive on every allowed offdiagonal/visible-hidden incidence and obey \(H'\mathbf1+Y'\mathbf1=0\). The visible row sums follow from the unchanged transfer at zero, as in the construction audit. Modal similarity preserves the entire rational hidden transfer exactly, and therefore preserves the full all-time marked waiting kernel. Together with the fixed positive observed pair, this is a complete five-state bidirected irreducible CTMC.

The three distinct nonzero rank-one modal residues give the inherited minimal full dimension five. Every pair of hidden vertices in the complete generator is adjacent and has the same external neighborhood; its full external exit vectors cannot be equal because that would contradict minimality. Thus the hypotheses of the already proved [hidden-pair boundary theorem, Section 3](hidden-pair-boundary-audit.md#3-explicit-fixed-topology-boundary-theorem) hold. That theorem supplies a valid data-preserving family with divergent entropy. The entropy fiber is therefore unbounded for **every** \(21/2\le z<z_*\). This conclusion uses the existing divergence theorem, not merely a large entropy value or the existence of multiple realizations. It overlaps the old near-identity unbounded interval, so their union reaches the new boundary without a parameter gap.

## Verification and limitations

Run from the project root:

```powershell
.\.venv\Scripts\python.exe -B analysis/check_balanced_cone_bound.py
```

The checker saves exact polynomial identities, rational interval sign checks, the constant/apex checks, source hashes, dependency versions, and execution time in [balanced-cone-bound-checks.json](balanced-cone-bound-checks.json). The root approximation is explicitly numerical; its isolating interval and signs use rational arithmetic. It independently checks the generic envelope identity before the theta specialization. The exclusion proof is the continuum argument above, not those finitely many arithmetic checks. The existing modal reduction and previous negative-bottom inequality are shared dependencies. No claim of formal verification, novelty, or a completed full five-state classification is made.

The sufficiency extension preserves the exclusion checker's implementation. After the note was finalized, its accepted output was refreshed to record the final source hashes. Run the separate sufficiency checker:

```powershell
.\.venv\Scripts\python.exe -B analysis/check_balanced_cone_sufficiency.py
```

It saves [balanced-cone-sufficiency-checks.json](balanced-cone-sufficiency-checks.json). All 12 strict geometric interval checks passed on the entire rational enclosure \([10.5,10.55714966867]\), along with exact tangency identities. The input-B upper slack uses the analytic discriminant sign and is positive only below the fold. The construction is an existence proof by strict inequalities and continuity; no floating-point candidate is promoted to exact kernel equality.
