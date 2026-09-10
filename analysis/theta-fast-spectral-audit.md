# A global spectral-cone obstruction for fast balanced theta models

Date: 2026-09-10 UTC. Contribution: analytic proof, independently checked with the coordinating agent, and a focused exact calculation. This is a global fixed-cap result; neither the earlier bounded searches nor local isolation enter its proof. No novelty claim is made. The invariant-cone framework is established prior mathematics; the [primary-source review](../evidence/positive-realization-frontier.md) records that provenance. The finite-triangle reduction and inequalities needed here are derived below.

## 1. Result and admissible class

Let

\[
Q(a,b)=\begin{pmatrix}
-11&1&2&0&8\\
2&-20&0&7&11\\
3&0&-7&4&0\\
0&6&5&-11&0\\
a&b&0&0&-a-b
\end{pmatrix},\qquad a,b>0,
\]

with only the resolved pair \(x\leftrightarrow y\) observed. Use the [formulation](formulation.md): exact full joint next-mark/time kernels, known visible endpoints, simple bidirected irreducible CTMCs, and at most five states. Put

\[
\rho=\sqrt6,\quad \alpha=9-2\rho,\quad\beta=9+2\rho,
\quad \delta=\beta-\alpha=4\rho,\quad s=a+b.
\]

**Theorem.** The kernel of \(Q(100,100)\) identifies its entire generator up to hidden labels. In particular its entropy fiber is a singleton. The same conclusion holds for every balanced model \(Q(z,z)\) with \(z\ge40\).

More generally, define

\[
r_y=\frac{4(\rho-1)}5,\quad A=a,\quad B=\frac b{r_y},
\quad m=\frac{7+2\rho}5,
\]
\[
k_L=\frac{3-\rho/2}{8},\quad k_R=\frac{35\rho}{88},
\quad\kappa=\frac{s-\alpha}{\delta}.
\]

An explicit open sufficient region for global generator uniqueness is

\[
\boxed{\ s>\beta,\qquad
(\kappa-1)B>k_R\left[1+\frac{A+1}{k_L}\right],\qquad
(\kappa-1)A>k_L\left[m+\frac{B+1}{k_R}\right].\ }       \tag{1}
\]

This region is sufficient, not necessary. Its complement is not classified here. The numerical constants refer to the fixed rate units of the displayed theta family.

## 2. Modal realization and fixed-order completeness

The hidden blocks are

\[
X=\begin{pmatrix}2&0&8\\0&7&11\end{pmatrix},\quad
Y=\begin{pmatrix}3&0\\0&6\\a&b\end{pmatrix},\quad
H=\begin{pmatrix}-7&4&0\\5&-11&0\\0&0&-s\end{pmatrix}.
\]

Their transfer has the exact modal realization

\[
D=\operatorname{diag}(-\alpha,-\beta,-s),\quad
X_m=(p,q,v),\quad Y_m=\begin{pmatrix}r\\f\\w\end{pmatrix},
\]
\[
p=\binom{3+\rho/2}{35\rho/8},\quad
q=\binom{3-\rho/2}{-35\rho/8},\quad v=\binom8{11},
\]
\[
r=(1,r_y),\quad f=(1,-4(\rho+1)/5),\quad w=(a,b).
\]

Thus

\[
F(z)=X(zI-H)^{-1}Y
=\frac{pr}{z+\alpha}+\frac{qf}{z+\beta}+\frac{vw}{z+s}.
\tag{2}
\]

For \(s>\beta\), these are three distinct simple poles with nonzero rank-one residues. The hidden transfer has minimal dimension three. Because both visible states are directly selected as reset and mark coordinates, eliminating their two fixed coordinates leaves precisely this hidden controllability/observability problem; the full killed realization has dimension five. This block argument is also recorded in the [theta rank audit](theta-parameter-strata-audit.md). Hence no smaller model is compatible under the cap.

Every compatible five-state model has the same visible block and hidden transfer. Minimal realization similarity, proved by bases in the [compatibility audit](compatibility-orbit.md), gives an invertible real \(V\) such that

\[
H'=V^{-1}DV,\qquad X'=X_mV\ge0,\qquad Y'=V^{-1}Y_m\ge0.
\tag{3}
\]

No entrywise positivity of \(V\) is assumed. The argument below excludes an irreducible Metzler \(H'\) even without reciprocal visible support; it therefore covers every connected bidirected hidden graph, both paths and triangles.

## 3. An irreducible hidden block would yield a finite invariant triangle

Suppose \(H'\) in (3) is irreducible. Its dominant eigenvalue is \(-\alpha\). Its right eigenvector \(V^{-1}e_1\) has a constant strict sign by Perron–Frobenius. Since

\[
X'V^{-1}e_1=X_me_1=p>0,
\]

and \(X'\ge0\), that sign is positive. The left eigenvector \(e_1^TV\) is likewise strictly positive: its product with this positive right eigenvector is one. Therefore every column of \(V\) has a strictly positive first coordinate.

The cone \(K=V\mathbb R_+^3\) has a section by first coordinate one that is a finite nondegenerate triangle \(\mathcal T\). Positive column rescaling gives its vertices as \((1,u_i,v_i)\). Also \(e_1\) lies in the interior of \(K\), so \((0,0)\) lies in the interior of \(\mathcal T\).

Metzler positivity gives \(e^{tH'}\ge0\) for \(t\ge0\). Consequently \(K\) is invariant under \(e^{t(D+\alpha I)}\), and \(\mathcal T\) is invariant under

\[
(u,v)\longmapsto(e^{-\delta t}u,e^{-\kappa\delta t}v).
\tag{4}
\]

The two columns of \(Y_m\), divided by their positive first coordinates, show that \(\mathcal T\) contains

\[
(1,A),\qquad (-m,B).
\tag{5}
\]

Finally \(X_mV\ge0\) requires every vertex, and hence the entire triangle, to lie in the output wedge

\[
v\ge k_L(-m-u),\qquad v\ge k_R(u-1).
\tag{6}
\]

This proves necessity of a bounded invariant triangle. A cone with a generator on the first-coordinate-zero plane is not covered by this section, but is impossible when \(H'\) is irreducible by the strict left Perron vector just proved. The original disconnected hidden realization has such a generator; it is not erroneously excluded.

## 4. Exhausting the triangle's sign pattern

In (6), any point with \(v\le0\) has \(-m\le u\le1\). If only one triangle vertex had positive second coordinate, containing \((1,A)\) would require that vertex's first coordinate to be at least one. Containing \((-m,B)\) would require the same coordinate to be at most \(-m\), a contradiction. There are thus at least two vertices with positive second coordinate. Since the origin is interior, at least one vertex has negative second coordinate. With exactly three vertices the sign pattern is therefore two positive and one negative.

The negative vertex has first coordinate strictly between \(-m\) and one, by (6). To contain both points in (5), the two remaining vertices must extend to both sides of that interval. Label the vertices

\[
L=(-\ell,V_L),\quad R=(c,V_R),\quad N=(d,-W),
\]
\[
\ell\ge m,\quad c\ge1,\quad -m<d<1,
\quad V_L,V_R,W>0.
\tag{7}
\]

Equalities \(\ell=m\) or \(c=1\) are allowed. The output wedge yields

\[
\ell-m\le V_L/k_L,\qquad c-1\le V_R/k_R,
\]
\[
W\le\min\{k_L(d+m),k_R(1-d)\}<1.                    \tag{8}
\]

The last strict bound follows from \(d<1\), \(k_L<1/4\), and \(m<5/2\), giving \(W<7/8\).

## 5. Four containment and two invariance inequalities

The upper segment \(LR\), evaluated at the two input abscissae, gives

\[
B\le V_L+\frac{\ell-m}{\ell+c}(V_R-V_L)
\le V_L+\frac{\ell-m}{\ell+c}V_R,                     \tag{9}
\]
\[
A\le V_R+\frac{c-1}{\ell+c}(V_L-V_R)
\le V_R+\frac{c-1}{\ell+c}V_L.                       \tag{10}
\]

The input \((1,A)\) lies above the lower segment \(NR\); the input \((-m,B)\) lies above \(LN\). These give the additional, consequential inequalities

\[
(V_R+W)(1-d)\le(A+W)(c-d),\qquad
(V_L+W)(d+m)\le(B+W)(\ell+d).                        \tag{11}
\]

Invariance of (4) requires its velocity to point into the triangle at each vertex. Evaluating the lower supporting-line derivatives at \(L,R\) gives

\[
[(\kappa-1)\ell+\kappa d]V_L\le\ell W,
\]
\[
[(\kappa-1)c-\kappa d]V_R\le cW.                    \tag{12}
\]

For example the lower-left line is
\(v=-W+(V_L+W)(d-u)/(\ell+d)\). Its inward derivative at \(L\) is
\(-\kappa\delta V_L+\delta\ell(V_L+W)/(\ell+d)\ge0\), exactly the first inequality. No condition at an unexamined point is asserted sufficient; these necessary conditions alone will contradict feasibility.

If \(d\ge0\), the first inequality of (12) gives \(V_L\le W/(\kappa-1)\). Equations (8), (9), and (11) then imply

\[
B\le V_L\left[1+\frac{V_R}{k_L(\ell+c)}\right]
\le\frac{W}{\kappa-1}\left[1+\frac{A+W}{k_L(1-d)}\right]
<\frac{k_R}{\kappa-1}\left[1+\frac{A+1}{k_L}\right].  \tag{13}
\]

Here \(c-d<\ell+c\), and \(W\le k_R(1-d)\le k_R\). If \(d<0\), the second inequality of (12) instead gives \(V_R\le W/(\kappa-1)\), and the reflected calculation gives

\[
A\le V_R\left[1+\frac{V_L}{k_R(\ell+c)}\right]
\le\frac{W}{\kappa-1}\left[1+\frac{B+W}{k_R(d+m)}\right]
<\frac{k_L}{\kappa-1}\left[m+\frac{B+1}{k_R}\right].  \tag{14}
\]

Here \(\ell+d<\ell+c\), \(W\le k_L(d+m)\), and \(d+m<m\). All denominators used are strictly positive by (7). Conditions (1) contradict both exhaustive sign cases, so no such triangle, and hence no irreducible hidden realization, exists.

## 6. Exact evaluation at theta(100,100)

The elementary bound \(12/5<\sqrt6<5/2\) gives

\[
2<m<5/2,\quad 1/5<k_L<1/4,\quad9/10<k_R<1,
\]
\[
A=100,\quad80<B=25(\rho+1)<90,\quad
\kappa-1=\frac{191-2\rho}{4\rho}>18.
\]

The right-hand side of (13) is strictly below

\[
\frac{1+5(100+1)}{18}=\frac{253}{9}<29<80<B.
\]

The right-hand side of (14) is strictly below

\[
\frac{(5/2)+(90+1)/(9/10)}{72}
=\frac{1865}{1296}<2<100=A.
\]

Both possible bottom-vertex signs are therefore excluded globally, including triangles with zero permitted rates or paired missing hidden edges.

## 7. Balanced-ray and open-region consequences

For \(a=b=z\ge40\), the wedge is unchanged, \(A=z\), and

\[
\frac56z<B<z,\qquad\kappa-1=\frac{2z-\beta}{4\rho}>
\frac{z-7}{5}>0.
\]

The right-hand side of (13) is less than \((25z+30)/(z-7)\), which is less than \(5z/6<B\), because

\[
z^2-37z-36=(z-40)^2+43(z-40)+84>0.
\]

The right-hand side of (14) is less than

\[
\frac{25/8+(25/18)(z+1)}{z-7}<z=A,
\]

because

\[
72z^2-604z-325=72(z-40)^2+5156(z-40)+90715>0.
\]

Thus every \(z\ge40\) satisfies the obstruction, with a uniform analytic argument and no parameter sampling. More generally, (13)–(14) prove the open two-parameter sufficient region (1).

## 8. From connected-hidden exclusion to global uniqueness

For completeness, the remaining reducible-hidden argument is the one previously proved in [the construction audit, Section 5](theta-family-construction-audit.md#5-reducible-hidden-blocks-in-two-residual-regions). With bidirected support on three hidden states, a reducible block is either three singletons or an irreducible pair and a singleton. Three singletons, or a singleton at \(\beta\), cannot produce the negative offdiagonal entries of \(qf\). A singleton at \(\alpha\) would leave a pair with dominant pole \(-\beta\), whose residue is nonnegative by Perron–Frobenius, also impossible. The singleton must therefore carry the \(s\) mode.

The remaining pair has zero-time transfer \(pr+qf=\operatorname{diag}(6,42)\). Reciprocal visible support forces its two hidden states to attach separately to \(x\) and \(y\). Write their entrances \(x_1,x_2\), exits \(y_1,y_2\), and internal rates \(h,k\). Zeroth and first moments identify

\[
x_1y_1=6,\quad x_2y_2=42,\quad
y_1+h=7,\quad y_2+k=11,
\]
\[
x_1hy_2=48,\quad x_2ky_1=105.
\]

The products give \(hk=20\), then \(19h-hk=56\), so \(h=4,k=5,y_1=3,y_2=6,x_1=2,x_2=7\). The singleton's pole \(s\), residue \(vw\), and row sum identify its exits as \((a,b)\) and entrances as \((8,11)^T\). Thus the only reducible model is the original generator up to hidden labels. Combining this with the global exclusion proves the theorem.

The five-state cap is consequential. Allowing a spare hidden state invokes the previously proved [state-splitting ambiguity](state-splitting-audit.md). This note does not settle the general five-state bounded-nonunique question or classify every theta parameter.

At theta(100,100), the exact stationary law is
\[
\pi=\frac{1}{335223}(106500,66600,82000,72200,7923).
\]
The x-to-y currents along the longer and shorter hidden routes are respectively
\(-11000/111741\) and \(19900/111741\). Closing each route with the reverse observed edge gives affinities \(\log(32/35)\) and \(\log(16/11)\), so the identified entropy is
\[
\sigma=\frac{-11000\log(32/35)+19900\log(16/11)}{111741}
\simeq0.0755509024393.
\]
These are inverse-time units with Boltzmann's constant one. The source is not at equilibrium.

## 9. Exact checks and falsification limits

Run from the repository root:

```powershell
python -B analysis/check_theta_fast_spectral.py
```

The focused standard-library script imports the existing exact quadratic-field helper and writes [outputs/check_theta_fast_spectral.json](../outputs/check_theta_fast_spectral.json). It checks the modal similarity and residues, source generator constraints and full ranks at \((100,100)\) and \((40,40)\), input/wedge identities, every constant bound used above, the sufficient-region margins at both points, and the positive shifted polynomial coefficients covering the balanced ray. It records exact values, runtime provenance and source hashes.

Those calculations catch orientation or arithmetic errors; the universal nonexistence conclusion comes from Sections 3–5, not from checking selected triangles, optimizer failures, or a finite parameter grid. The proof allows signed similarities and all reciprocal zero patterns. Its irreducible-hidden exclusion assumes exactly three hidden modes; larger positive realizations are not excluded.
