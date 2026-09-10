# Four states with unknown topology: adversarial audit

Date: 2026-09-10 UTC. Contribution: analytic derivation and audit, not a novelty claim. No numerical computation was required. This note uses the [formulation](formulation.md) and the minimal-realization orbit theorem in [compatibility-orbit.md](compatibility-orbit.md). It does not depend on an unproved general boundary-geometry assertion for a two-dimensional positivity domain.

## Result and precise scope

Assume four states `(x,y,h,k)`, an irreducible simple bidirected CTMC, exactly the observed pair `x<->y`, known observed incidence, full joint waiting kernels, and minimal kernel realization dimension four. Individual positive rates have no common positive lower cutoff. Allow **all bidirected supports on these same four states**.

Then the compatibility class has either:

1. a unique generator up to exchanging `h,k`, hence unique entropy production; or
2. entropy production unbounded above.

In particular, allowing unknown topology cannot produce a bounded non-singleton entropy set by joining finitely many individually identifiable fixed-topology realizations. The proof below gives explicit paths to an unbounded family whenever global uniqueness is not forced.

The globally unique cases, read from any representative generator, are:

- each visible endpoint has exactly one hidden neighbor, and these neighbors differ; the hidden-hidden edge may be present or absent;
- the hidden-hidden edge is absent, one visible endpoint has exactly one hidden neighbor `h`, the other has both hidden neighbors, and `lambda_h > lambda_k`, where the lambdas are hidden escape rates.

All other connected supports/parameters permitted by minimality have an unbounded compatibility class. The second criterion is unchanged by relabeling visible endpoints or hidden states in the indicated way.

This is a statement about **fixed dimension four and a minimal observed kernel**. It does not cover dimension at most four when the kernel has lower minimal dimension, extra hidden states, unknown mark incidence, multiple channels, detector errors, or restricted rate intervals. Literature novelty has not been assessed for this theorem.

## 1. Orbit and notation

Write

\[
Q=\begin{pmatrix}A&X\\Y&H\end{pmatrix},\qquad
H=\begin{pmatrix}-\lambda_h&m\\n&-\lambda_k\end{pmatrix}.
\]

Here rows of `X` index `(x,y)` and columns index `(h,k)`; `Y` reverses those roles. Bidirectionality means `X_ih>0` exactly when `Y_hi>0`, and likewise for `k`; either `m,n>0`, or `m=n=0`. Generator normalization gives `lambda_h=m+sum_i Y_hi` and `lambda_k=n+sum_i Y_ki`; these are total hidden escape rates, including the hidden-hidden edge when present. The observed edge is always positive in both directions. A visible endpoint's hidden-neighbor set may be empty, a singleton, or `{h,k}`.

Every compatible four-state realization is minimal because the data have minimal dimension four. By the orbit theorem, it has

\[
Q'=S^{-1}QS,\quad S=\operatorname{diag}(I_2,U),\quad
U=\begin{pmatrix}u&1-u\\v&1-v\end{pmatrix},\quad \delta=u-v\ne0.
\]

The blocks transform as

\[
X'=XU,\qquad Y'=U^{-1}Y,\qquad H'=U^{-1}HU,
\qquad
U^{-1}=\frac1\delta\begin{pmatrix}1-v&u-1\\-v&u\end{pmatrix}.
\]

The visible block is unchanged, and the stationary law is `pi'=pi S`. A permutation of the target hidden labels changes the sign of `det U`. Hence every target has a representative with `delta>0`; proving uniqueness in that chamber proves uniqueness up to hidden permutation.

## 2. A singleton imposes a global constraint

Suppose endpoint `i` has only hidden neighbor `h`. Then its row of `X` and column of `Y` are `(a,0)` and `(b,0)^T`, with `a,b>0`. Their transformed entries are

\[
(X'_{ih},X'_{ik})=(au,a(1-u)),\qquad
(Y'_{hi},Y'_{ki})=\frac b\delta(1-v,-v).
\]

Nonnegativity in the positive-determinant chamber requires `0<=u<=1` and `v<=0`. Bidirected support strengthens this substantially:

- `u=0` is impossible, since the reverse rate at `i<->h` is positive;
- `u=1` requires `v=0`, since the forward rate at `i<->k` is zero;
- `v=0` requires `u=1`, since its reverse rate is zero.

Thus every admissible target satisfies **either `U=I`, or `0<u<1` and `v<0`**. In the latter case `i` acquires both hidden neighbors. This is a global restriction, not a first-order perturbation statement.

If the other visible endpoint has only neighbor `k`, nonnegativity of its transformed row/column requires `v>=0` and `u>=1`. Combining the constraints forces `U=I`. This proves the first global-uniqueness case, regardless of the hidden-hidden edge.

## 3. A direct unboundedness lemma for dense visible incidence

Suppose every **nonempty** visible hidden-neighbor set equals `{h,k}`, and `m,n>0`. Empty visible-neighbor sets remain allowed. At least one set is nonempty because the full graph is connected.

Minimality implies that the two rows of `Y` are different. Indeed, if `Y_h=Y_k=y`, then `Y=1 y`. Generator normalization gives `H1=-(y1)1`. The three-dimensional subspace

\[
\{(z_x,z_y,z_h,z_h)^T:z_x,z_y,z_h\in\mathbb R\}
\]

is invariant under the killed generator `T` and contains the input columns `B`, which live in visible coordinates. The four-state kernel would therefore fail controllability. This contradiction proves `Y_h!=Y_k`.

Let `J` be the set of visible endpoints having hidden neighbors. Every `Y_hi,Y_ki` for `i in J` is strictly positive. After exchanging the source hidden labels if necessary, arrange

\[
r=\min_{i\in J}\frac{Y_{hi}}{Y_{ki}}<1.
\]

Such an ordering is possible because the two rows differ; also `r>0`. Consider the explicit triangular similarities

\[
U_e=\begin{pmatrix}1-e&e\\0&1\end{pmatrix},\qquad 0\le e<r.
\]

For all nonempty rows, the transformed visible-hidden rates are

\[
X'_{ih}=(1-e)X_{ih},\quad X'_{ik}=X_{ik}+eX_{ih},
\qquad
Y'_{hi}=\frac{Y_{hi}-eY_{ki}}{1-e},\quad Y'_{ki}=Y_{ki}.
\]

They remain strictly positive for `e<r`; empty rows/columns stay zero. The hidden rates are

\[
H'_{kh}=n(1-e)>0,\qquad
H'_{hk}=\frac{f(e)}{1-e},\qquad
f(e)=m+e(\lambda_k-\lambda_h)-ne^2.
\]

Since `f(0)=m>0`, let `e_*` be the first zero of `f` in `(0,r]`, if one exists, and otherwise let `e_*=r`. Then `0<e_*<=r<1`. For every `0<=e<e_*`, all required edges are positive and all original missing visible edges remain absent. The graph stays connected, so these are admissible generators. Every rate is bounded along this path because `1-e>=1-r>0`.

The stationary law is explicitly

\[
\pi'_x=\pi_x,\quad\pi'_y=\pi_y,\quad
\pi'_h=(1-e)\pi_h,\quad\pi'_k=\pi_k+e\pi_h.
\]

All stationary probabilities have strictly positive limits at `e_*`.

If `f(e_*)=0`, one hidden rate tends to zero while its reverse tends to `n(1-e_*)>0`. Their stationary fluxes therefore have respective limits zero and strictly positive. If `e_*=r`, at least one `Y'_{hi}` tends to zero while `X'_{ih}` tends to `(1-r)X_ih>0`, again giving a one-way stationary-flux limit. The conclusions remain valid if both events occur simultaneously.

An unoriented-edge entropy term `(a-b) log(a/b)` diverges whenever one flux tends to zero and the other to a strictly positive finite limit. All other edge terms are nonnegative. Therefore total entropy tends to infinity along the admissible path.

**Scalar-block variant.** The same proof works when `m=n=0` and `lambda_h=lambda_k=lambda`, because `H=-lambda I` remains unchanged. There is then no hidden-edge positivity condition: simply take `e->r`. Minimality again excludes identical rows of `Y`. This independently establishes the needed full-positive equal-escape diamond unboundedness in the minimal case.

**Fixed-topology corollary.** Every member of the triangular path before its endpoint has exactly the original support. Thus the dense-incidence positive-hidden-edge class is unbounded already with its topology fixed. This includes the complete graph and the graph consisting of an observed leaf attached to a hidden triangle. The scalar-block variant likewise preserves the full diamond topology. The paths change no observation kernel and do not rely on allowing topology changes at the limiting, inadmissible one-way edge.

The argument uses no compactness of a positivity domain, no assumed existence of a generic boundary, and no cancellation-prone entropy formula. It gives the divergent edge, limiting stationary probabilities, bounded rates and exact compatible path explicitly.

## 4. Opening a singleton when the hidden edge is present

Suppose some visible endpoint has only neighbor `h`, and no endpoint has only neighbor `k`. Thus the other endpoint's neighbor set is empty, `{h}`, or `{h,k}`. If `m,n>0`, use

\[
U_{e,\eta}=\begin{pmatrix}1-e&e\\-\eta&1+\eta\end{pmatrix},
\qquad e,\eta>0
\]

with both parameters sufficiently small. For every singleton at `h`, transformed forward rates are `(a(1-e),ae)` and reverse rates are

\[
\frac b{1-e+\eta}(1+\eta,\eta),
\]

all positive. Existing full rows and corresponding reverse columns stay positive by continuity. Empty rows/columns remain zero. The positive hidden edge also stays positive by continuity. Thus the transformed generator has dense incidence at every nonempty visible row and a positive hidden edge. It is minimal, being similar to the original. Section 3 applies and supplies unbounded entropy in the **same observed-data fiber**.

When the other endpoint has no hidden neighbors or only neighbor `h`, connectivity forces `m,n>0`, because otherwise hidden state `k` would be disconnected. Hence those cases are all covered here.

## 5. One singleton and one full row, without the hidden edge

The remaining singleton case has, after relabeling, `x` adjacent only to `h`, `y` adjacent to both, and `m=n=0`. Then `H=diag(-lambda_h,-lambda_k)`, and direct multiplication gives

\[
H'_{hk}=\frac{(1-u)(1-v)(\lambda_k-\lambda_h)}{u-v},
\qquad
H'_{kh}=\frac{uv(\lambda_h-\lambda_k)}{u-v}.
\]

By Section 2, every nonidentity admissible target in the positive-determinant chamber must have `0<u<1` and `v<0`. Both displayed rates consequently have the sign of `lambda_k-lambda_h`.

- If `lambda_h>lambda_k`, both would be negative. No nonidentity admissible target exists. This proves the second global-uniqueness case, even though competing supports are allowed.
- If `lambda_h<lambda_k`, the small perturbation `U_{e,eta}` from Section 4 makes both hidden rates positive and opens the singleton's missing visible edge. The other full row remains positive by continuity. Section 3 then proves unboundedness.
- If `lambda_h=lambda_k`, the same perturbation leaves `H` scalar and opens the singleton's missing visible edge, yielding a full-positive diamond. The scalar-block variant in Section 3 proves unboundedness.

The sign argument is global and handles all admissible target supports. Merely checking an infinitesimal direction would not suffice to establish the unique case; Section 2 supplies the required global constraint.

## 6. No singletons and no hidden edge

Now every nonempty visible-neighbor set is `{h,k}`, and `m=n=0`.

If hidden escape rates are equal, Section 3's scalar-block variant applies. If only one visible row is nonempty in this scalar-block case, the two rows of `Y` necessarily coincide, contradicting minimality; this exceptional support/parameter combination is therefore excluded by the theorem's hypotheses.

If `lambda_k>lambda_h`, choose small `e,eta>0` with `u=1-e`, `v=-eta`. Both formulas in Section 5 are strictly positive. If `lambda_k<lambda_h`, choose instead `u=1+e`, `v=eta`; for sufficiently small parameters `u-v>0`, and both formulas are again strictly positive. All visible-hidden edges remain positive by continuity, and empty visible rows remain zero. We have reached the dense-incidence positive-hidden-edge class in Section 3, so the original fiber is unbounded.

## 7. Exhaustion and audit outcome

There must be at least one nonempty visible-neighbor set. The two sets have sizes in `{0,1,2}`. If both are singletons with different hidden neighbors, Section 2 proves uniqueness. If there is a singleton but not an opposite singleton, the other set is empty, the same singleton, or full. Connectivity handles the first two possibilities through Section 4; the full case is handled by Sections 4–5 according to the hidden edge. If there are no singletons, every nonempty set is full, covered by Sections 3 or 6. These alternatives exhaust connected supports.

The exhaustive case split proves the stated unknown-topology dichotomy. The explicit triangular path in Section 3 establishes unboundedness with a nonvanishing opposing stationary flux. Bidirectionality at the singleton boundaries and minimality when excluding equal rows of `Y` are essential hypotheses.

Follow-up verification is recorded in [E026](../evidence/RECORDS.md#e026); the [nonminimal extension](nonminimal-four-state-audit.md) removes the minimality assumption and the [observable criterion](observable-four-state-criterion.md) independently reconstructs the unique cases. The focused [prior-art check](../evidence/entropy-range-followup.md) constrains prospective novelty without establishing it. This note supplies the minimal four-state analytic argument; larger state counts require separate analysis.
