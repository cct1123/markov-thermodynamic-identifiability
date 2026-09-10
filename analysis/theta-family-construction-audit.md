# Constructive regions for the two-parameter theta family

Date: 2026-09-10 UTC. Contribution: analytic derivation and independent audit of the coordinating agent's spectral construction, with numerical spot checks explicitly separated below. No novelty claim. Only five physical states are used.

## Result and remaining region

Write
\[
Q(a,b)=\begin{pmatrix}
-11&1&2&0&8\\
2&-20&0&7&11\\
3&0&-7&4&0\\
0&6&5&-11&0\\
a&b&0&0&-a-b
\end{pmatrix},\qquad a,b>0,
\]
in state order \((x,y,h,k,l)\), and observe only the resolved pair \(x\leftrightarrow y\). Set
\[
s=a+b,\quad \alpha=9-2\sqrt6,\quad \beta=9+2\sqrt6.
\]

The exact marked-kernel entropy fiber is unbounded at the five-state cap throughout the union
\[
\boxed{\quad s\le\alpha\quad\text{or}\quad
\left(s\le\beta,\ a>\frac{35\sqrt6}{88},\
b>\frac{\sqrt6}{4}\right)
\quad\text{or}\quad
\left(s\ge\beta,\
\frac ab>\frac{11(s-11)^2}{1120}\ \text{or}\
\frac ba>\frac{14(s-7)^2}{55}\right).\quad}              \tag{1}
\]

The strict subregion \(s<\alpha\) and the third region have complete realizations arbitrarily near the source. The full slow-coincidence line \(s=\alpha\) is covered by the independently audited residue-redistribution proof in [positive-realization-obstructions.md, Section 6](positive-realization-obstructions.md#6-update-the-entire-slow-coincidence-line-has-unbounded-entropy). The second region has the explicit spectral realization below: two hidden states with the same visible neighbors, plus a third hidden state. It includes the locally isolated example \((3,3)\) and does not require minimality or an invertible exit-coordinate chart. Together the second and third regions cover **every** positive point on \(s=\beta\); see Section 3a.

For \(s>\beta\), and also for \(\alpha<s<\beta\) outside the strict coordinate thresholds of the second region, a separate result narrows the search: every compatible realization with **reducible bidirected hidden block** is the original theta generator, up to hidden labels. Thus any different compatible generator there must have an irreducible hidden block. This is an obstruction to a class of constructions, not global uniqueness.

The remaining parameters are not classified here. Failure of a complete-representation search, the inequalities of this particular construction, or local isolation is not an entropy bound.

## 1. Hidden transfer and the exact residues

Partition \(Q=(A,X;Y,H)\) into the two visible and three hidden states. Its hidden transfer is
\[
F(z)=X(zI-H)^{-1}Y
=\frac{Z_\alpha}{z+\alpha}
+\frac{Z_\beta}{z+\beta}
+\frac{Z_s}{z+s}.                                      \tag{2}
\]
When poles coincide, the corresponding terms are simply added; (2) remains an identity.

Put
\[
d=7-\alpha=2(\sqrt6-1),\qquad
\Delta=\beta-\alpha=4\sqrt6.
\]
The two-state block \(\begin{pmatrix}-7&4\\5&-11\end{pmatrix}\) has spectral projectors
\[
P_\alpha=\Delta^{-1}
 \begin{pmatrix}d+4&4\\5&d\end{pmatrix},\qquad
P_\beta=\Delta^{-1}
 \begin{pmatrix}d&-4\\-5&d+4\end{pmatrix}.
\]
Since its visible entrance and exit matrices are \(\operatorname{diag}(2,7)\) and \(\operatorname{diag}(3,6)\),
\[
Z_\alpha=\Delta^{-1}
 \begin{pmatrix}6(d+4)&48\\105&42d\end{pmatrix},\qquad
Z_\beta=\Delta^{-1}
 \begin{pmatrix}6d&-48\\-105&42(d+4)\end{pmatrix},
\]
and
\[
Z_s=\begin{pmatrix}8\\11\end{pmatrix}(a,b).
\]

In particular \(Z_\alpha,Z_s\) are strictly positive rank-one matrices, whereas \(Z_\beta\) has positive diagonal and negative off-diagonal entries. Also
\[
Z_\alpha+Z_\beta=\operatorname{diag}(6,42).              \tag{3}
\]

Preserving \(F(z)\) and the visible block \(A\) preserves the visible resolvent by the Schur complement
\[
[(zI-Q)^{-1}]_{VV}=[zI-A-F(z)]^{-1}.
\]
The same statement holds after subtracting the observed-edge matrix from \(A\), hence preserves the full marked waiting kernel. This implication requires no minimality assumption. Moreover
\[
F(0)\mathbf1=-XH^{-1}Y\mathbf1=X\mathbf1,
\]
so a realization with normalized hidden row sums automatically preserves the two visible hidden-entry totals \(10,18\).

## 2. An explicit two-mode cone realization

The coordinating agent proposed moving the entire positive \(\alpha\)-residue into a singleton hidden state and realizing the \(s,\beta\) residues in a coupled pair. The following gives explicit formulas and verifies every physical constraint.

Factor
\[
Z_s=p\,r,\quad p=(8,11)^T,\quad r=(a,b),
\]
\[
Z_\beta=q\,f,\quad
q=(2d,-35)^T,\quad
f=\Delta^{-1}(3,-24/d).
\]
These products agree with (2), using \(d(d+4)=20\). In eigenmode coordinates let
\[
X_m=(p,q),\qquad Y_m=\begin{pmatrix}r\\f\end{pmatrix},
\qquad D_m=\operatorname{diag}(-s,-\beta).
\]
Choose
\[
\frac{24}{d\Delta b}<t<\frac4d,\qquad
\frac3{\Delta a}<u<\frac{11}{35},                       \tag{4}
\]
and put
\[
P=\begin{pmatrix}1&1\\-t&u\end{pmatrix}.
\]
For a completely explicit selection, use the midpoint of each interval in (4).

The intervals exist exactly when
\[
b>\frac6\Delta=\frac{\sqrt6}{4},\qquad
a>\frac{105}{11\Delta}=\frac{35\sqrt6}{88}.              \tag{5}
\]
Define
\[
\bar X=X_mP=
\begin{pmatrix}
8-2dt&8+2du\\
11+35t&11-35u
\end{pmatrix},
\]
\[
\bar Y=P^{-1}Y_m
=\frac1{t+u}\begin{pmatrix}
ua-3/\Delta&ub+24/(d\Delta)\\
ta+3/\Delta&tb-24/(d\Delta)
\end{pmatrix},
\]
\[
\bar H=P^{-1}D_mP
=\frac1{t+u}\begin{pmatrix}
-su-\beta t&u(\beta-s)\\
t(\beta-s)&-st-\beta u
\end{pmatrix}.                                        \tag{6}
\]
Equations (4) make every entry of \(\bar X,\bar Y\) strictly positive. For \(s<\beta\), both internal off-diagonal rates in \(\bar H\) are positive; for \(s=\beta\), \(\bar H=-\beta I\). Its eigenvalues are negative in both cases.

Normalize hidden row sums by
\[
w=-\bar H^{-1}\bar Y\mathbf1,\qquad W=\operatorname{diag}(w),
\]
\[
X_p=\bar XW,\qquad Y_p=W^{-1}\bar Y,\qquad H_p=W^{-1}\bar HW. \tag{7}
\]
Because \(\bar H\) is a stable Metzler matrix and \(\bar Y\mathbf1>0\), \(w>0\). This can also be checked without a matrix inverse:
\[
\zeta=\frac{3-24/d}{\Delta\beta},\qquad
w=\frac1{t+u}\begin{pmatrix}u-\zeta\\t+\zeta\end{pmatrix}. \tag{8}
\]
The first coordinate is positive since \(\zeta<0\). For \(s\le\beta\), \(b\le\beta\), and the lower bound for \(t\) in (4) implies \(t>-\zeta\). Thus the second coordinate is positive as well.

The pair has
\[
H_p\mathbf1+Y_p\mathbf1=0,\qquad
X_p(zI-H_p)^{-1}Y_p
=\frac{Z_s}{z+s}+\frac{Z_\beta}{z+\beta}.               \tag{9}
\]

For the singleton \(\alpha\)-mode factor
\[
Z_\alpha=c\,g,\qquad
c=(2(d+4),35)^T,\quad g=\Delta^{-1}(3,24/(d+4)).
\]
Use entrance vector and exit row
\[
x_\alpha=\frac{g\mathbf1}{\alpha}c,\qquad
y_\alpha=\frac{\alpha}{g\mathbf1}g.
\]
Then \(y_\alpha\mathbf1=\alpha\), and \(x_\alpha y_\alpha=Z_\alpha\).

The final hidden realization is
\[
\widetilde X=(X_p,x_\alpha),\qquad
\widetilde Y=\begin{pmatrix}Y_p\\y_\alpha\end{pmatrix},\qquad
\widetilde H=\operatorname{diag}(H_p,-\alpha),
\]
with the original \(A=\begin{pmatrix}-11&1\\2&-20\end{pmatrix}\).
All visible-to-hidden and hidden-to-visible rates are strictly positive. The pair edge is bidirected when \(s<\beta\) and absent when \(s=\beta\); the singleton has no hidden edges. Row sums vanish by (7), (9), and \(F(0)\mathbf1=(10,18)^T\). All five states communicate via the visible states, so the generator is irreducible.

This construction is an exact positive realization of (2), not an approximate match. At repeated poles it remains valid by the same displayed identities.

### Entropy consequence

The two pair states have exactly the same external neighborhood \(\{x,y\}\), and their full external exit rows differ. Indeed \(Y_m\), hence \(Y_p\), has rank two: one original row is strictly positive and the other has opposite signs. If \(s<\beta\), they are adjacent twins. If \(s=\beta\), they are unjoined twins with equal escape rate \(\beta\).

The explicit triangular boundary theorem in [hidden-pair-boundary-audit.md](hidden-pair-boundary-audit.md) therefore applies in both cases, without requiring minimality. Orient the pair so
\[
r_*=\min_{i=x,y}\frac{(Y_p)_{1i}}{(Y_p)_{2i}}<1,
\]
and mix it by \(\begin{pmatrix}1-e&e\\0&1\end{pmatrix}\). Stop before the first external-exit zero or internal-rate zero. All pre-boundary generators retain the constructed support and the exact kernel. Their stationary law transforms as
\[
(\pi_1,\pi_2)\mapsto((1-e)\pi_1,\pi_2+e\pi_1).
\]
The endpoint lies below \(e=1\), so all stationary masses have positive limits and all rates stay bounded. One rate vanishes while its reverse stationary flux remains positive. The nonnegative entropy term on that edge diverges. This proves the second region of (1).

The strict thresholds (5) describe this cone construction. Equality makes an interval collapse and does not itself give a physical bidirected endpoint. No impossibility conclusion for other realizations follows from failing (5).

## 3. Near-identity opening below the slow pole

The coordinating agent independently supplied the following local construction; the signs below were checked analytically here. Let
\[
v=(4,d)^T,\qquad \ell=(5,d),\qquad
H_2v=-\alpha v,\quad \ell H_2=-\alpha\ell.
\]
Use a normalized hidden perturbation \(U_\epsilon=I+\epsilon K\) with
\[
K_{hl}=-4,\quad K_{kl}=-d,\quad K_{lh}=5,\quad K_{lk}=d,
\quad K_{hk}=K_{kh}=0,
\]
and each diagonal set to minus its row's off-diagonal sum.

The derivative of the transformed generator is \(QK-KQ\), with \(K\) embedded in the hidden coordinates. The four originally missing hidden rates have positive derivatives
\[
(h\to l,k\to l)=(\alpha-s)(4,d),\qquad
(l\to h,l\to k)=(\alpha-s)(5,d).
\]
The four missing visible-incidence rates have derivatives
\[
(x\to k,y\to h,h\to y,k\to x)=(8d,55,4b,da)>0.
\]
Thus for every \(s<\alpha\), all missing rates become strictly positive for sufficiently small \(\epsilon>0\); all existing positive rates stay positive by continuity, and \(U_\epsilon\) is invertible near identity. Normalization preserves row sums, and hidden similarity preserves the exact kernel.

The complete target contains adjacent hidden external twins, so the same boundary theorem gives unbounded entropy for the strict subregion \(s<\alpha\) of (1). At \(s=\alpha\) these hidden opening velocities vanish; the separate residue-redistribution argument cited in Section 4 covers that boundary.

## 3a. Exact strict first-order opening test at and above the fast pole

This extends the first-order idea to \(s\ge\beta\), verifying the coordinating agent's constants and their necessity for strict opening of every missing rate. Write
\[
L=s-7,\qquad M=s-11,\qquad LM\ge20,
\]
and parameterize a normalized hidden velocity by
\[
p=K_{hk},\ q=K_{hl},\ r=K_{kh},\
z=K_{kl},\ t=K_{lh},\ u=K_{lk}.
\]
In missing-rate order \((xk,yh,hy,hl,kx,kl,lh,lk)\), the raw derivative vector used by the dual certificates below is
\[
\mathcal A(p,q,r,z,t,u)^T=
(2p+8u,\ 7r+11t,\ -6p-bq,\ Lq+4z,\
-3r-az,\ 5q+Mz,\ -Lt-5u,\ -4t-Mu)^T.
\]
The missing visible-rate derivatives impose
\[
p>-4u,\quad p<-bq/6,\qquad
r>-11t/7,\quad r<-az/3.
\]
Thus \(p,r\) can be chosen exactly when
\[
bq<24u,\qquad 7az<33t.                                \tag{10}
\]
The missing hidden-rate derivatives impose
\[
Lq+4z>0,\quad 5q+Mz>0,\qquad
-Lt-5u>0,\quad -4t-Mu>0.                              \tag{11}
\]

Any solution must have either \(q>0,z<0,t<0,u>0\) or \(q<0,z>0,t>0,u<0\). Indeed \(q,z\le0\) is incompatible with (11), while \(q,z\ge0\), through (10), would force \(t,u>0\), again contradicting (11). The zero-coordinate boundary cases likewise force incompatible signs. Equation (10) then fixes the signs of \(t,u\).

For the first branch scale \(z=-1\) and write \(t=-v\), \(v>0\). Because \(LM\ge20\), the exact restrictions simplify to
\[
q>M/5,\qquad v<7a/33,\qquad
bq/24<u<4v/M.
\]
There is a solution if and only if
\[
\boxed{\quad a/b>11M^2/1120.\quad}                     \tag{12}
\]
For example choose \(q\) just above \(M/5\), \(v\) just below \(7a/33\), then choose \(u\) strictly between its displayed bounds, and choose \(p,r\) in their nonempty intervals above. These are explicit open-interval choices; midpoint choices after taking sufficiently small endpoint offsets give a concrete normalized \(K\).

For the second branch scale \(q=-1\), write \(u=-v\), and use
\[
z>L/4,\qquad v<b/24,\qquad
7az/33<t<5v/L.
\]
This is possible if and only if
\[
\boxed{\quad b/a>14L^2/55.\quad}                       \tag{13}
\]
These necessity and sufficiency statements include \(s=\beta\), where the paired bounds coincide but remain strict. Once such a \(K\) exists, \(U=I+\epsilon K\) opens a complete physical generator for sufficiently small \(\epsilon>0\). The twin boundary theorem proves unboundedness.

At \(s=\beta\), the two thresholds for \(a/b\) in (12) and (13) are equal:
\[
k=\frac{11(\beta-11)^2}{1120}
=\frac{55}{14(\beta-7)^2}.
\]
Thus all ratios except \(a/b=k\) have a strict opening. The remaining point is
\[
a_*=\frac{429-44\sqrt6}{357-22\sqrt6},\qquad
b_*=\beta-a_*.
\]
It satisfies the strict spectral thresholds (5), so Section 2 covers it. For the first inequality, clearing positive denominators gives
\(42372>16367\sqrt6\), which follows already from \(\sqrt6<5/2\).
The second inequality follows directly from
\(1120\beta>\sqrt6(357-22\sqrt6)\).
Numerically \(a_*\simeq1.05975109,\ b_*\simeq12.83922840\), whereas the thresholds are approximately \(0.97422887,0.61237244\).

Consequently **the entire fast-coincidence line \(s=\beta\) has unbounded entropy** at the five-state cap. For \(s>\beta\), (12)–(13) leave a closed ratio interval with no *strict first-order complete opening*. That fact alone neither proves actual local isolation nor rules out a distant compatible component.

## 3b. Local isolation at \((100,100)\)

The coordinating agent's [exact certificate and targeted probe](theta-fast-probe.json), produced by [probe_theta_fast_case.py](probe_theta_fast_case.py) at 2026-09-10 06:55:19 UTC, records the positive left null vector
\[
c=\left(3,1,1,\frac{53200}{109371},\frac73,
\frac{133900}{109371},\frac{1983}{36457},
\frac{4577}{36457}\right)^T
\]
for the derivative matrix in missing-rate order \((xk,yh,hy,hl,kx,kl,lh,lk)\). This audit independently executed its annihilation and strict positivity using Python Fraction arithmetic.

The derivative matrix has rank six analytically: a vector in its null space must have \(q=z=0\), since the hidden opening rows have determinant
\((s-7)(s-11)-20=193\cdot189-20=36457\ne0\).
The remaining rows then force \(p=r=t=u=0\). The positive dual and full rank imply actual local isolation by the normalized-sequence proof in [theta-global-audit.md](theta-global-audit.md), not merely failure of a strict opening direction. The original exit chart has determinant \(-882\), so similarity coordinates vary continuously near the original generator and this isolation holds in generator space.

The same source artifact records a thirteen-start bounded search without a positive complete witness. That search is not an absence certificate. Together with Section 5, the exact result is only that this point is locally isolated and has no different reducible-hidden representative; distant irreducible-hidden alternatives remain unresolved.

## 3c. Rejected shortcut: the locally isolated strip above the slow pole

The conjectured shortcut that local opening covers every point outside the direct residue region with \(\alpha<s<\beta\) is false. In fact **every source with \(\alpha<s\le7\) is locally isolated**, regardless of its positive coordinate ratio.

Set \(L=s-7\le0\), \(M=s-11<0\), and
\[
D=LM-20=(s-\alpha)(s-\beta)<0.
\]
If the two hidden outgoing opening derivatives in (11) are strictly positive, their coefficient matrix
\[
B=\begin{pmatrix}L&4\\5&M\end{pmatrix},\qquad
B^{-1}=\frac1D\begin{pmatrix}M&-4\\-5&L\end{pmatrix}
\]
forces \(q,z>0\). The incoming opening inequalities similarly force
\((t,u)^T=-B^{-T}h<0\) for a strictly positive vector \(h\). This contradicts \(bq<24u\). Thus no strict first-order complete opening exists anywhere in this strip.

There is a stronger exact certificate. In missing-rate order
\((xk,yh,hy,hl,kx,kl,lh,lk)\), define
\[
c=\left(
3,\frac37,1,\frac{Mb-5a}{D},1,\frac{La-4b}{D},
\frac{33M/7-96}{D},\frac{24L-165/7}{D}
\right)^T.                                            \tag{14}
\]
Each coordinate is strictly positive: both \(D\) and the numerator of every term with denominator \(D\) are negative. Direct substitution in the six columns of the derivative matrix from (10)–(11) gives \(c^T\mathcal A=0\). The matrix has rank six. Indeed its two hidden outgoing rows force \(q=z=0\) when \(\mathcal A v=0\), since their determinant is \(D\ne0\); its remaining rows then force \(p=r=t=u=0\).

The positive-dual normalized-sequence argument therefore proves actual local isolation, not merely the failure of strict first-order opening. The three distinct poles with nonzero rank-one residues give a minimal hidden transfer of dimension three, hence a minimal full realization of dimension five. Continuity of the uniquely normalized similarity through a nonsingular controllability minor promotes the isolation to generator space, including when the particular exit-coordinate chart is singular.

For example \((a,b)=(1/2,9/2)\) lies in the strip and fails the lower \(a\) threshold in (5). It is locally isolated, so a local construction cannot fill this gap in (1). This does not show that its entropy is bounded: the source \((3,3)\) lies in the same locally isolated strip yet has distant unbounded alternatives. The residual low-\(a\) and low-\(b\) regions require a global argument. No parameter grid or additional numerical search was used for this rejection.

## 4. A repeated dominant pole obstructs complete hidden support

At \(s=\alpha\), the original hidden eigenvalues are \(-\alpha,-\alpha,-\beta\). For a **minimal five-state source**, normalized hidden similarity exhausts compatible five-state generators and fixes these eigenvalues. An irreducible Metzler hidden block has a simple dominant eigenvalue by Perron-Frobenius theory. Therefore no compatible hidden block can be irreducible on this line, in particular none can be complete.

This conditional spectral obstruction must not be applied to a nonminimal source through the minimal similarity theorem. It also does not obstruct unbounded entropy: Section 2 has a reducible hidden block and proves divergence on the part of this line satisfying (5). The independently audited [residue-redistribution proof in positive-realization-obstructions.md, Section 6](positive-realization-obstructions.md#6-update-the-entire-slow-coincidence-line-has-unbounded-entropy) covers **every** positive point on this line, including the nonminimal exception.

## 5. Reducible hidden blocks in two residual regions

Assume \(s>\beta\). The three poles in (2) are distinct and all three rank-one residues are nonzero. The hidden transfer has minimal dimension three: each residue contributes rank one at a distinct pole. With both visible coordinates serving as input/output coordinates, the full killed realization has dimension five. Thus every admissible realization under the five-state cap is minimal and lies in the normalized hidden similarity class; in particular the hidden eigenvalues are \(-\alpha,-\beta,-s\).

A reducible bidirected three-state hidden block is, after relabeling, either three singleton blocks or a connected two-state block plus a singleton.

- Three singletons are impossible. A singleton's transfer residue is an outer product of nonnegative entrance and exit rates, whereas \(Z_\beta\) has negative off-diagonal entries.
- A singleton at \(\beta\) is impossible for the same reason.
- A singleton at \(\alpha\) leaves a connected pair with eigenvalues \(-\beta,-s\). Its dominant pole is \(-\beta\). The spectral projector at the dominant eigenvalue is a positive outer product; multiplication by nonnegative entrance and exit matrices gives a nonnegative residue. It cannot equal \(Z_\beta\).
- Therefore the singleton must be at \(s\), leaving the original \(\alpha,\beta\) transfer in the pair.

For this remaining assignment the pair is globally pinned. Its zero-time transfer (3) has both off-diagonal entries zero and positive diagonal entries. In a bidirected physical realization, every hidden state adjacent to both visible states would make both off-diagonal sums positive. Consequently, the two hidden states must attach separately to \(x\) and \(y\), one each. Write their entrance and exit rates as \(x_1,x_2,y_1,y_2>0\), and their connected hidden block as
\[
H_p=\begin{pmatrix}-\lambda_1&m\\n&-\lambda_2\end{pmatrix}.
\]
The zero-time and first derivative matrices identify
\[
x_1y_1=6,\quad x_2y_2=42,\quad
\lambda_1=7,\quad\lambda_2=11,
\]
\[
x_1my_2=48,\qquad x_2ny_1=105.
\]
Hence \(mn=20\). Row sums give \(y_1=7-m,\ y_2=11-n\). Substituting in the first cross moment gives
\[
6m(11-n)/(7-m)=48,\quad
19m-mn=56,
\]
so \(m=4,n=5\), followed by \(y_1=3,y_2=6,x_1=2,x_2=7\).

The singleton residue \(Z_s\), together with its total escape rate \(s\), fixes its exits to \((a,b)\) and entrances to \((8,11)^T\). Thus the whole generator is exactly the source, up to hidden labels.

This proves uniqueness **among reducible hidden blocks** for \(s>\beta\).

The same conclusion extends to
\[
\alpha<s<\beta,\qquad
a\le\frac{35\sqrt6}{88}\quad\text{or}\quad
b\le\frac{\sqrt6}{4}.                                  \tag{15}
\]
The poles are again distinct, with nonzero rank-one residues, so the same minimality and component enumeration apply. A singleton at \(\beta\), or three singletons, remains impossible because \(Z_\beta\) has negative off-diagonal entries. If the singleton is instead at \(\alpha\), the two-state component must have zero-time impulse response
\[
X_pY_p=Z_s+Z_\beta.
\]
This is the zeroth time-domain Markov matrix, not the Laplace value \(F_p(z=0)\). Its off-diagonal entries are
\[
(X_pY_p)_{xy}=8b-2\sqrt6,\qquad
(X_pY_p)_{yx}=11a-\frac{35\sqrt6}{8}.                  \tag{16}
\]
Below either threshold in (15), one of these entries is negative, contradicting \(X_p,Y_p\ge0\).

Equality at one threshold cannot restore a physical bidirected realization in this strip. For any nonnegative entrance/exit pair obeying reciprocal visible-hidden support,
\[
(X_pY_p)_{xy}>0\quad\Longleftrightarrow\quad
(X_pY_p)_{yx}>0.
\]
Both conditions mean that at least one hidden state is adjacent to both visible endpoints; if no such state exists, both entries are zero. In (16), equality at just one threshold makes one entry zero and the other strictly positive, which violates this symmetric zero pattern. Simultaneous equality at both thresholds is impossible in \(\alpha<s<\beta\), since their sum is
\[
\frac{57\sqrt6}{88}<\alpha.
\]
If the other coordinate lies below its threshold, negativity already gives the contradiction.

Thus a singleton at \(\alpha\) is excluded throughout (15). The only remaining singleton assignment is \(s\), and the preceding exact-moment argument pins the two-state component and singleton to the original source. This establishes the reducible-hidden uniqueness extension, including equality at either coordinate threshold. It does not exclude a distant connected hidden realization.

Connected hidden alternatives remain a separate question in both residual regions. In particular, these results do not establish a finite entropy upper bound.

There is one further useful support reduction for connected alternatives. If the three hidden states form a triangle, their three visible-neighborhood subsets of \(\{x,y\}\) necessarily contain a comparable pair: this subset poset has width two. For that pair, the third hidden state belongs to both external neighborhoods, and the pair is adjacent. The complete external neighborhoods are therefore comparable, so the fixed-dimension adjacent-pair theorem gives unbounded entropy. This argument allows topology changes when the inclusion is strict.

Consequently a hidden-triangle alternative is already an unboundedness certificate. In either residual region, a distinct compatible generator in a bounded entropy fiber would therefore have to have a hidden **path**, the only remaining connected bidirected graph on three hidden states. Neither existence nor global exclusion of such path alternatives is proved here.

## 6. Numerical checks and reproducibility

The formulas in Section 2 were independently executed at \((1,1),(3,3),(1,10),(6,7),(\alpha/2,\alpha/2),(\beta/2,\beta/2)\). All target rates were nonnegative, every visible incidence rate was strictly positive, and the zero rates were permitted missing hidden edges. The largest absolute row-sum error was \(3.56\times10^{-15}\); the largest entrywise difference between old and new hidden transfers at \(z=0,0.1,1,5,30\) was \(3.56\times10^{-15}\).

These are floating-point spot checks, not exact verification of a continuum or a substitute for the algebra above. Their role was to catch factorization, orientation and normalization errors. The repeated-pole cases were included deliberately. Runtime: Python 3.9.12, NumPy 2.0.1, SciPy 1.13.1; no stochastic input. Additional exact representative checks of residue reassignment and slow-pole redistribution are preserved in [check_theta_residue_construction.py](check_theta_residue_construction.py) and [theta-residue-checks.json](../outputs/theta-residue-checks.json).

Run the following embedded source from the repository root:

~~~powershell
python -B -c "from pathlib import Path; t=Path('analysis/theta-family-construction-audit.md').read_text(encoding='utf-8'); exec(t.rsplit('<!-- THETA_CONSTRUCTION_CHECK -->',1)[1].split(chr(96)*3+'python',1)[1].split(chr(96)*3,1)[0])"
~~~

<!-- THETA_CONSTRUCTION_CHECK -->

```python
import numpy as np
from scipy.linalg import block_diag
alpha=9-2*np.sqrt(6.0); beta=9+2*np.sqrt(6.0)
delta=beta-alpha; d=7-alpha
def construction(a,b):
    s=a+b
    t=(24/(d*delta*b)+4/d)/2
    u=(3/(delta*a)+11/35)/2
    P=np.array([[1.,1.],[-t,u]])
    Xm=np.array([[8.,2*d],[11.,-35.]])
    Ym=np.array([[a,b],[3/delta,-24/(d*delta)]])
    Hb=np.linalg.solve(P,np.diag([-s,-beta])@P)
    if s == beta: Hb=-beta*np.eye(2)
    Xb=Xm@P; Yb=np.linalg.solve(P,Ym)
    w=np.linalg.solve(-Hb,Yb@np.ones(2))
    Hn=(Hb*w[None,:])/w[:,None]
    Xn=Xb*w[None,:]; Yn=Yb/w[:,None]
    c=np.array([2*(d+4),35.])
    g=np.array([3.,24/(d+4)])/delta
    Xa=c*g.sum()/alpha; Ya=alpha*g/g.sum()
    X=np.column_stack([Xn,Xa])
    Y=np.vstack([Yn,Ya])
    H=block_diag(Hn,-alpha)
    A=np.array([[-11.,1.],[2.,-20.]])
    Q=np.block([[A,X],[Y,H]])
    return Q
for a,b in [(1.,1.),(3.,3.),(1.,10.),(6.,7.),(alpha/2,alpha/2),(beta/2,beta/2)]:
    Q=np.array([[-11,1,2,0,8],[2,-20,0,7,11],[3,0,-7,4,0],[0,6,5,-11,0],[a,b,0,0,-a-b]],dtype=float)
    Qn=construction(a,b)
    rates=Qn[~np.eye(5,dtype=bool)]
    errors=[]
    for z in [0.,.1,1.,5.,30.]:
        old=Q[:2,2:]@np.linalg.solve(z*np.eye(3)-Q[2:,2:],Q[2:,:2])
        new=Qn[:2,2:]@np.linalg.solve(z*np.eye(3)-Qn[2:,2:],Qn[2:,:2])
        errors.append(np.max(np.abs(old-new)))
    print((a,b),'min_rate',rates.min(),'min_visible_incidence',min(Qn[:2,2:].min(),Qn[2:,:2].min()),'row_error',np.max(np.abs(Qn.sum(axis=1))),'transfer_error',max(errors))
    assert rates.min()>-1e-12
    assert min(Qn[:2,2:].min(),Qn[2:,:2].min())>0
    assert np.max(np.abs(Qn.sum(axis=1)))<1e-12
    assert max(errors)<1e-12
import platform, scipy
print('environment',platform.python_version(),np.__version__,scipy.__version__)
```
