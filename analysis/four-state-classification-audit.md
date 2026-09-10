# Audit of the minimal four-state fixed-topology dichotomy

Date: 2026-09-10 (UTC). Contribution type: analytic audit. This note checks the theorem against the [formulation](formulation.md) and the proved [compatibility orbit](compatibility-orbit.md). It contains no numerical enumeration and makes no novelty claim.

## Verdict and precise scope

Fix a connected simple bidirected graph on exactly four states, with one resolved observed bidirectional edge `x<->y`, known incidence, and strictly positive rates on every present directed edge. Assume the full matrix-valued observed kernel has minimal linear realization dimension four. Among all generators on that fixed topology producing exactly the same full kernel, the stationary entropy-production rate is either unique or unbounded above. The argument below excludes a bounded-but-nonunique entropy fiber under these assumptions.

The result uses freedom to approach zero rates; it does not impose a common positive rate cutoff. It does not cover nonminimal four-state data in general, unknown topology, extra states, parallel channels, blurred marks, or finite-precision observations. Boundary generators used in the proof can contain one-way edges, but they are limits of admissible bidirected generators, not members asserted to have finite entropy.

The delicate points in the proposed argument hold with the following clarifications:

- The nonnegative boundary remains minimal because the similarity matrices and their inverses are uniformly bounded; this must be established before using minimality to infer boundary irreducibility.
- A row with no hidden neighbors supplies permanent zeros, which must be omitted from the finite set of newly paired edge zeros.
- Two paired visible-hidden zero equations have determinant `-(ac+bd)<0`, so their intersections are finite even when the coefficients produce an excluded singular similarity.
- A normalized diagonalizer of the irreducible two-state hidden block need not exist, but there are at most two; equal hidden row sums can make the set empty rather than continuous.

## 1. Coordinates and elementary topology reduction

Order states `(x,y,h,k)` and write

\[
Q=\begin{pmatrix}A&X\\Y&H\end{pmatrix}.
\]

All compatible four-state realizations are minimal because their common kernel has minimal dimension four. By the orbit proof they have

\[
Q_U=S_U^{-1}QS_U,\qquad
S_U=\operatorname{diag}(I_2,U),\qquad
U=\begin{pmatrix}u&1-u\\v&1-v\end{pmatrix},\quad
\Delta=u-v\ne0.
\]

In particular `X_U=XU`, `Y_U=U^{-1}Y`, and `H_U=U^{-1}HU`. Signed entries of `U` are allowed; only the transformed generator must have the required positive rates and zeros.

If a visible vertex, say `x`, has exactly one hidden neighbor, label it `h`. Its row of `X` and column of `Y` have the forms `(a,0)` and `(b,0)^T`, with `a,b>0`. Preserving the absent `x->k` edge gives `a(1-u)=0`, hence `u=1`. Preserving `k->x=0` gives `-vb/Delta=0`, hence `v=0`. Thus `U=I`. Rates are unique after aligning the hidden labels, so entropy is unique. This handles every topology in which either visible vertex has exactly one hidden neighbor.

Otherwise each visible vertex has either zero or two hidden neighbors. They cannot both have zero, since the graph is connected. The remaining possibilities are:

| Hidden link `h<->k` | Visible hidden-neighbor counts | Conclusion |
| --- | --- | --- |
| Absent | `(2,2)` | Full diamond: distinct hidden escape rates give uniqueness; equal escapes give unbounded entropy, by the existing diamond proof. |
| Absent | `(0,2)` or `(2,0)` | Tree: every stationary edge current is zero, so entropy is identically zero. |
| Present | `(2,2)` | Complete graph: the open-region argument below gives unbounded entropy. |
| Present | `(0,2)` or `(2,0)` | A triangle with the observed edge as a pendant edge: the same open-region argument gives unbounded entropy. |

The tree conclusion follows by summing stationarity over either component left by deleting an edge: that sole connecting edge has zero net stationary current. These cases exhaust the possibilities without graph enumeration.

## 2. The remaining physical similarity region is open

Consider either remaining case with `h<->k` present. A visible vertex has both hidden connections or neither. Consequently all required absent visible-hidden entries are entire zero rows of `X` and zero columns of `Y`, which remain zero for every `U`. The observed visible block is fixed, and the hidden off-diagonal entries are required positive rather than zero.

Let `D` be the set of `(u,v)` for which `Delta!=0` and all directed edges present in the fixed graph have positive transformed rates. No further support equalities are needed in these two cases. Therefore `D` is an open subset of the full real plane. It contains `U=I`, namely `(u,v)=(1,0)`, because all original required rates are positive. Every point of `D` gives an irreducible generator on the same connected topology and the same full kernels.

## 3. Bounded generators imply bounded similarities and inverses

All generators in the orbit have the same trace. Define

\[
L=-\operatorname{tr}Q=\sum_{i\ne j}q_{ij}>0.
\]

For every physical `Q_U`, all terms in the corresponding off-diagonal sum are nonnegative, and the sum is still `L`. Thus every off-diagonal rate is at most `L`, and every diagonal entry lies in `[-L,0]`. All entries of the killed generator `T_U=Q_U-E` are uniformly bounded as well, since the observed rates in `E` are fixed.

Use the fixed finite observability and controllability matrices

\[
O=\begin{pmatrix}R\\RT\\RT^2\\RT^3\end{pmatrix},
\qquad
C=\begin{pmatrix}B&TB&T^2B&T^3B\end{pmatrix}.
\]

Minimality gives full column rank of `O` and full row rank of `C`. Choose constant left and right inverses `L_O O=I_4` and `C L_C=I_4`. For the transformed matrices,

\[
O_U=O S_U,\qquad C_U=S_U^{-1}C,
\]

so

\[
S_U=L_O O_U,\qquad S_U^{-1}=C_U L_C.
\]

Because `T_U`, `R`, and `B` are bounded, the finitely many powers defining `O_U,C_U` are uniformly bounded. Therefore both `S_U` and `S_U^{-1}` are uniformly bounded over `D`.

It follows that `D` is bounded and `|det U|=|Delta|` is uniformly bounded away from zero. For example an operator-norm bound on `U^{-1}` bounds both singular values of `U` away from zero, and hence their product away from zero. Thus the closure `Dbar` is compact and every matrix `U` on it remains invertible. This rules out singular-similarity boundaries before discussing entropy.

## 4. Every boundary generator remains irreducible

For `U_*` in `Dbar`, continuity gives a generator `Q_*` with nonnegative off-diagonal entries, zero row sums, unchanged positive observed rates, and all originally absent edges still absent. It remains similar to `Q`, since `U_*` is invertible. In particular `(R,T_*,B)` has minimal dimension four.

For a nonnegative off-diagonal matrix, a missing directed path gives a structural zero in every corresponding matrix power: this can also be seen by adding a large diagonal multiple of the identity to obtain a nonnegative matrix without changing path reachability. Applied to the killed generator, controllability requires that each microscopic state can reach some visible state; otherwise its row in every `T_*^j B` is zero. Observability requires that every state is reachable from some visible state; otherwise its column in every `R T_*^j` is zero.

The observed states `x,y` still communicate in both directions in `Q_*`, through their fixed observed edge. Combining these two reachability facts with that edge shows that any state can reach any other in `Q_*`. Thus every generator on the compact closure is irreducible, even if some formerly bidirectional links become one-way.

Its unique stationary vector is `pi_*=pi S_{U_*}`. This depends continuously on `U_*` and is strictly positive at every point of `Dbar`. Compactness therefore gives a common positive lower bound on every stationary probability throughout the closure. This prevents a vanishing rate from being hidden by a simultaneously vanishing stationary mass in the boundary argument.

## 5. Boundaries with only paired edge zeros form a finite set

Every boundary point of `D` has at least one newly zero rate: if all required rates remained positive, continuity and invertibility would place it in the open region. Call a boundary point paired if every newly zero rate has a zero reverse rate. Already absent edges are not counted.

### Visible-hidden edges

For a visible vertex with both hidden neighbors, write its original row of `X` as `(a,b)` and its corresponding column of `Y` as `(c,d)^T`, all four numbers strictly positive. The transformed rates involving `h` are

\[
q_{ih}(U)=au+bv,\qquad
q_{hi}(U)=\frac{c-d+du-cv}{\Delta}.
\]

Their simultaneous vanishing is equivalent to

\[
au+bv=0,\qquad du-cv=d-c.
\]

The coefficient determinant is `-(ac+bd)<0`, so this pair has exactly one solution in the full plane, and at most one with `Delta!=0`. In particular when `c=d` the unique solution is `(u,v)=(0,0)`, which is singular and excluded.

For the edge involving `k`, simultaneous vanishing gives

\[
au+bv=a+b,\qquad du-cv=0,
\]

with the same nonzero determinant. Again there is at most one nonsingular solution. There are at most four present visible-hidden undirected edges, so all their paired-zero candidates form a finite set. A visible vertex with no hidden neighbors contributes no new candidate.

### The hidden-hidden edge

Simultaneously setting the two hidden off-diagonal rates to zero makes `U^{-1}HU` diagonal. The original hidden block has positive off-diagonal entries because `h<->k` is present. Its two eigenvalues are real and distinct, since the discriminant is

\[
(H_{11}-H_{22})^2+4H_{12}H_{21}>0.
\]

For each of the two orderings of its eigenlines, the columns of `U` must be those eigenvectors times arbitrary nonzero scales. The normalization `U1=1` uniquely determines those two scales, by expressing the vector `1` in that eigenbasis. If one coefficient is zero, that ordering supplies no invertible normalized matrix; otherwise it supplies exactly one. Thus there are at most two normalized diagonalizers, including signed possibilities. This is a finite set, not a family. For example equal hidden row sums can make `1` an eigenvector, forcing one coefficient to vanish and leaving no such diagonalizer.

Every paired boundary point must belong to the finite union just described, since it has at least one newly zero undirected edge. Additional simultaneous zeros can only reduce that set.

## 6. A one-way boundary exists and forces divergence

A nonempty bounded open subset of the plane cannot have finite boundary. One direct proof is to start from an interior point and follow each ray until its first exit: boundedness supplies an exit, openness makes the first exit a boundary point, and distinct rays give distinct points.

The physical region `D` is nonempty, open, and bounded. Its paired boundary points form a finite set. Therefore some boundary point has a newly zero rate with a strictly positive reverse rate.

Choose a sequence `U_n` in `D` tending to such a point, with `q_ij(U_n)->0` and `q_ji(U_n)->b>0`. The uniform positive stationary bound gives

\[
\pi_i(U_n)q_{ij}(U_n)\longrightarrow0,\qquad
\pi_j(U_n)q_{ji}(U_n)\longrightarrow c>0.
\]

The corresponding nonnegative unoriented-edge contribution

\[
\left(\pi_iq_{ij}-\pi_jq_{ji}\right)
\log\frac{\pi_iq_{ij}}{\pi_jq_{ji}}
\]

diverges to positive infinity. Every other edge contribution is nonnegative, so total entropy diverges. Each member of the sequence remains a finite-rate irreducible bidirected generator on the original topology and has exactly the same complete observed kernels.

This proves unboundedness for both open-region graph classes. Combining it with the degree-one, tree, and diamond cases proves the stated dichotomy.

## Scope of the argument

This analytic argument builds on the earlier orbit and diamond proofs. The [nonminimal extension](nonminimal-four-state-audit.md) and [unknown-topology audit](unknown-topology-audit.md) establish their broader four-state statements separately. This planar argument does not identify the entropy infimum in unbounded fibers or extend to three or more hidden states: in higher hidden dimension the paired-zero sets can have larger dimensions.

The proof is structural and uses exact equality of all kernels. It makes no claims about numerical conditioning or the ability to distinguish nearby models from finite data. Independent computational examples can audit formulas and boundary behavior but cannot replace the argument covering all parameter values. Prior-art assessment remains necessary before describing the theorem as new.
