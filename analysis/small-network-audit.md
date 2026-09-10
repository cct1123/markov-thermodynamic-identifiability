# Exact small-network audit

Date: 2026-09-10 (UTC). Contribution type: analytic derivation and source-informed inference. This is a bounded mathematical audit, not an exhaustive topology search and not a claim of novelty. It uses the definitions in [formulation.md](formulation.md). Representative calculations are checked by [check_small_networks.py](check_small_networks.py); the general arguments below are analytic.

## Scope and conclusions

Assume a finite irreducible CTMC with a simple bidirected graph, one channel for each ordered state pair, known endpoints of one resolved observed bidirectional edge, exact joint next-mark/time densities including their absolute normalization and time scale, and the conventional state-level stationary entropy-production rate with natural logarithms and `k_B=1`. The generator acts on row probabilities. Every displayed numerical rate is in a single common inverse-time unit.

Under these assumptions:

1. In the class with at most three states, all rates and topology are identified by the zero-time value and first two derivatives of the full observed kernel. The two-state and three-state cases are distinguishable in that class, including a hidden leaf.
2. There are four-state families of a fixed topology whose full kernels are identical and whose entropy-production rates realize every finite nonnegative value. A lumpable diamond gives a simple example.
3. A second example has fixed complete four-state topology and minimal realization dimension four. It too realizes entropy range `[0,infinity)` with exactly fixed kernels. Excluding reducible or nonminimal kernel realizations therefore does not restore thermodynamic identifiability in general.

Consequently four is the minimum fixed cardinality at which such nonidentifiability can occur for this observation scheme and admissible class. This is an existence threshold, not a classification of every four-state model, graph, or observed kernel. Identification within `N<=3` does not exclude compatible larger models when cardinality is unrestricted.

## 1. Identification for at most three states

Call the visible endpoints `x,y`, with marks `+=(x,y)` and `-=(y,x)`. Let `r=q_xy>0` and `s=q_yx>0`. Order kernel rows and columns by `(+,-)`. Immediately after `+` the state is `y`, while immediately after `-` it is `x`. Therefore

\[
r=\psi_{-+}(0),\qquad s=\psi_{+-}(0).
\]

Let `K(t)` be the visible `x,y` principal submatrix of `exp(Tt)`, where `T` removes only the two observed off-diagonal entries from `Q`. The data determine all four entries:

\[
K(t)=
\begin{pmatrix}
\psi_{-+}(t)/r&\psi_{--}(t)/s\\
\psi_{++}(t)/r&\psi_{+-}(t)/s
\end{pmatrix}.
\]

For three states, write the hidden state as `h` and the remaining rates as

\[
a=q_{xh},\quad c=q_{yh},\quad b=q_{hx},\quad d=q_{hy}.
\]

Bidirectionality means `a>0 iff b>0` and `c>0 iff d>0`; irreducibility requires `a+c>0`. In state order `(x,y,h)`,

\[
T=\begin{pmatrix}
-(r+a)&0&a\\
0&-(s+c)&c\\
b&d&-(b+d)
\end{pmatrix}.
\]

First derivatives recover the visible-to-hidden rates:

\[
a=-K'_{xx}(0)-r,\qquad c=-K'_{yy}(0)-s.
\]

The second derivatives give

\[
\begin{aligned}
K''_{xx}(0)&=(r+a)^2+ab,&K''_{xy}(0)&=ad,\\
K''_{yx}(0)&=cb,&K''_{yy}(0)&=(s+c)^2+cd.
\end{aligned}
\]

If `a>0`, then

\[
b=\frac{K''_{xx}(0)-(r+a)^2}{a},\qquad
d=\frac{K''_{xy}(0)}{a}.
\]

If `a=0`, irreducibility forces `c>0`, and

\[
b=\frac{K''_{yx}(0)}{c}=0,\qquad
d=\frac{K''_{yy}(0)-(s+c)^2}{c}.
\]

Thus all rates, including the absent links, are determined. The symmetric formulas from the other row provide consistency checks when both `a,c` are positive. If just one is positive, the graph is a three-state tree with a hidden leaf; it is still identified, and its stationary entropy production is zero. If both are positive, the triangle generator and hence its stationary entropy production are identified.

For two states, `K(t)=diag(exp(-rt),exp(-st))`; the recovered `a,c` both vanish. No irreducible three-state model can have `a=c=0`. This distinguishes `N=2` from `N=3` within their union. An observed edge between distinct states excludes `N=1`. This proof uses exact derivatives, so it is a structural-identifiability statement; it makes no claim about estimation conditioning with finite temporal resolution or noise.

## 2. A lumpable four-state diamond

Use state labels `(1,3,2,4)`, with visible link `1<->3`. Fix positive `r,s,A,C,b,d` and choose `0<u<A`, `0<v<C`:

\[
\begin{array}{llll}
q_{13}=r,&q_{31}=s,&q_{12}=u,&q_{14}=A-u,\\
q_{32}=v,&q_{34}=C-v,&q_{21}=q_{41}=b,&q_{23}=q_{43}=d.
\end{array}
\]

There is no link `2<->4`. The partition with singleton blocks `1`, `3`, and hidden block `H={2,4}` has aggregate generator

\[
\overline Q=
\begin{pmatrix}
-(r+A)&r&A\\
s&-(s+C)&C\\
b&d&-(b+d)
\end{pmatrix}.
\]

For the membership matrix

\[
L=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\\0&0&1\end{pmatrix},
\]

direct multiplication gives `QL=L Qbar`. Removing the visible off-diagonal entries on both sides gives `TL=L Tbar`, since the visible states are singleton blocks. The absorption matrix factors as `B=L Bbar`, and `RL=Rbar`. Consequently

\[
\Psi(t)=R e^{Tt}B=R L e^{\overline Tt}\overline B
=\overline R e^{\overline Tt}\overline B.
\]

This proves equality of all joint kernels for every time, including amplitudes and event probabilities, throughout the `u,v` family. It is stronger than checking constancy of an entropy estimator or of a ratio of selected densities.

Let `p_1,p_3,p_H` be the fixed stationary probabilities of the aggregate chain. The microscopic stationary probabilities satisfy

\[
\pi_1=p_1,\quad \pi_3=p_3,\quad
\pi_2=\frac{p_1u+p_3v}{b+d},\quad
\pi_4=\frac{p_1(A-u)+p_3(C-v)}{b+d}.
\]

Keep `v>0` fixed and take `u` to zero from above. On edge `1<->2`, the forward stationary flux `p_1 u` vanishes, while the backward stationary flux `b pi_2` tends to `b p_3 v/(b+d)>0`. The nonnegative edge contribution to entropy therefore diverges. The full entropy diverges because every other unoriented-edge contribution is also nonnegative. All individual rates stay bounded and positive at each admissible point; the limiting zero rate is not itself included.

For the concrete choice `r=s=b=d=1`, `A=C=2`, `v=1`, and `0<u<2`,

\[
(\pi_1,\pi_3,\pi_2,\pi_4)
=\left(\frac14,\frac14,\frac{u+1}{8},\frac{3-u}{8}\right),
\qquad
\sigma(u)=\frac{1-u}{8}\log\frac{2-u}{u}.
\]

The visible edge current is zero. In orientations `(1,2),(3,2),(1,4),(3,4)`, the four remaining currents are respectively `(u-1)/8`, `(1-u)/8`, `(1-u)/8`, `(u-1)/8`; substitution gives the displayed formula. It vanishes at `u=1`, diverges as `u->0+` or `u->2-`, and is continuous on `(0,2)`. By the intermediate value theorem its range is every finite nonnegative value. Thus the entropy set of this fixed-topology kernel fiber is exactly `[0,infinity)`; no larger entropy set is possible because admissible finite bidirected generators have finite nonnegative entropy.

This family has a three-state aggregate realization, so it does not address whether nonidentifiability persists when kernel realizations must be minimal.

### Relation to the inspected source

Jann van der Meer, Benjamin Ertel, and Udo Seifert, *Thermodynamic inference in partially accessible Markov networks: A unifying perspective from transition-based waiting time distributions*, arXiv:2203.12020v2, version dated 18 August 2022, Appendix E.5, Table 5 and Eqs. (E89)-(E92), inspected 10 September 2026: [primary text](https://arxiv.org/html/2203.12020v2).

The source supplies the diamond and its exact Markov lumping of states `2,4`. Its varying Table-5 parameter changes the aggregate rate `q_1H`; that table by itself is not a fixed-full-kernel family. Holding both aggregate entrance sums fixed, as above, supplies the exact-kernel family audited here. This is a straightforward source-informed adaptation of its mechanism. No novelty claim follows.

## 3. Hidden similarity preserves the observation law

The [compatibility-orbit proof](compatibility-orbit.md#2-resolved-reverse-marks-pin-the-visible-coordinates) establishes the transformation used below. With visible endpoints first, take S=diag(I_2,U), where U is invertible and U1=1. Then Q_S=S^-1 Q S has the same observed kernel whenever its rates satisfy generator positivity, bidirectionality, and the chosen topology. Its stationary law is pi S. These physical constraints must be checked; U is a realization-coordinate change, not a physical lumping operation.

## 4. A minimal four-state family with entropy range `[0,infinity)`

In order `(x,y,h,k)`, start with the symmetric complete-graph generator

\[
Q_0=\begin{pmatrix}
-6&1&2&3\\
1&-10&4&5\\
2&4&-7&1\\
3&5&1&-9
\end{pmatrix}.
\]

Only `x<->y` is observed. This generator has stationary law `(1,1,1,1)/4` and zero entropy production. For `0<=epsilon<2/3`, set

\[
U_\epsilon=\begin{pmatrix}1-\epsilon&\epsilon\\0&1\end{pmatrix},
\quad S_\epsilon=\operatorname{diag}(I_2,U_\epsilon),
\quad Q_\epsilon=S_\epsilon^{-1}Q_0S_\epsilon.
\]

Direct multiplication gives

\[
Q_\epsilon=\begin{pmatrix}
-6&1&2(1-\epsilon)&3+2\epsilon\\
1&-10&4(1-\epsilon)&5+4\epsilon\\
\dfrac{2-3\epsilon}{1-\epsilon}&\dfrac{4-5\epsilon}{1-\epsilon}&-7-\epsilon&\dfrac{1+2\epsilon-\epsilon^2}{1-\epsilon}\\
3&5&1-\epsilon&-9+\epsilon
\end{pmatrix}.
\]

Every off-diagonal entry is strictly positive on this half-open interval. Row sums are zero; every rate is bounded along the family because `1-epsilon>=1/3`. The stationary law is

\[
\pi_\epsilon=\frac14(1,1,1-\epsilon,1+\epsilon).
\]

The previous similarity argument gives exactly the same full observed kernel for all `epsilon`.

### Minimality

For checking rank, permuting the two rows of `R` into visible-state order does not matter, and `B` consists of the two visible coordinate vectors since the observed rates both equal one. The hidden rows of `T_0 B` form

\[
Q_{HV}=\begin{pmatrix}2&4\\3&5\end{pmatrix},\quad \det Q_{HV}=-2.
\]

Thus the four columns of `[B,T_0 B]` span the four-state space. Similarly the hidden columns of `R T_0` form

\[
Q_{VH}=\begin{pmatrix}2&3\\4&5\end{pmatrix},\quad \det Q_{VH}=-2,
\]

so the four rows of `[R;R T_0]` also have full rank. Equivalently, the data-determined block Hankel matrix `[R;R T_0][B,T_0 B]`, with blocks `RB`, `R T_0 B`, and `R T_0^2 B`, has rank four. Any realization of dimension `n` factors that same matrix through an `n`-dimensional space, so `n>=4`. This proves minimal dimension four directly. Under similarity these rank properties are unchanged. In particular, none of this family admits an observation-preserving state lumping to a smaller CTMC. No generic minimal-realization uniqueness claim beyond similarity is required for the argument.

### Entropy formula and divergence

With orientations `(x,h),(y,h),(x,k),(y,k),(h,k)`, stationary currents are respectively

\[
\frac{\epsilon}{4},\quad \frac{\epsilon}{4},\quad
-\frac{\epsilon}{4},\quad-\frac{\epsilon}{4},\quad
\frac{\epsilon}{2}.
\]

The visible edge current vanishes. Inserting the corresponding flux ratios into the entropy sum and canceling `(1-epsilon)^2(1+epsilon)^2=(1-epsilon^2)^2` yields

\[
\boxed{\displaystyle
\sigma(\epsilon)=\frac{\epsilon}{4}
\log\frac{120(1+2\epsilon-\epsilon^2)^2}
{(2-3\epsilon)(4-5\epsilon)(3+2\epsilon)(5+4\epsilon)}.}
\]

For example, at `epsilon=1/4`,

\[
Q_{1/4}=\begin{pmatrix}
-6&1&3/2&7/2\\
1&-10&3&6\\
5/3&11/3&-29/4&23/12\\
3&5&3/4&-35/4
\end{pmatrix},\quad
\pi_{1/4}=(1/4,1/4,3/16,5/16),\quad
\sigma(1/4)=\frac1{16}\log\frac{529}{154}>0.
\]

As `epsilon->2/3-`, the forward `x->h` stationary flux tends to `1/6`, and its reverse flux `(2-3epsilon)/4` vanishes. Thus

\[
\sigma(\epsilon)=\frac16\log\frac1{2/3-\epsilon}+O(1).
\]

The same divergence follows directly from the boxed formula. Every model before the endpoint remains irreducible, bidirected, finite-rate, and minimal. Since `sigma(0)=0` and the formula is continuous up to any point short of `2/3`, the family attains every finite nonnegative entropy value. For these observed data the entropy set is exactly `[0,infinity)` even when the admissible class is restricted to the known complete four-state topology and minimal realizations.

## Boundaries of the result

The examples establish exact compatibility families and an existence threshold. They do not enumerate all fibers for `N<=6`, establish generic nonidentifiability for every graph, characterize all positive similarities, or supply a bounded-but-nonunique fiber. They rely on freedom to let positive reverse rates approach zero; a common strictly positive lower rate bound would exclude the divergent endpoints. Mere upper bounds on the rates do not exclude either construction.

The [evidence records](../evidence/RECORDS.md) distinguish these analytic deductions from prior results and numerical checks. Publication novelty remains unestablished.
