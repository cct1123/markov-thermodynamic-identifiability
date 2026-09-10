# Removing minimality at exactly four states

Date: 2026-09-10 (UTC). Contribution type: analytic audit. This note extends the [fixed-topology audit](four-state-classification-audit.md) and [unknown-topology audit](unknown-topology-audit.md) under the [working formulation](formulation.md). It makes no novelty claim.

## Outcome and scope

The linear-minimality assumption can be removed when there are **exactly four microscopic states**, one resolved observed bidirectional edge `x<->y`, a connected simple bidirected graph, and complete exact joint waiting kernels. Positive rates have no common positive lower cutoff.

- For each fixed topology, the entropy fiber is either a singleton or unbounded above.
- Allowing all connected bidirected topologies on those same four states also gives only a singleton or an unbounded entropy fiber.
- In the unknown-topology class, the only globally unique cases are the two classes already identified in the minimal audit. Both are automatically minimal. Every compatible model with a nonminimal four-state realization has an unbounded unknown-topology entropy fiber.

The proof does **not** assert that all equal-kernel nonminimal realizations are similar. It uses the minimal orbit theorem only after proving minimality where needed; elsewhere it constructs exact compatible families by a sufficient similarity transformation or by strong lumpability. Cardinality remains exactly four throughout each family.

## 1. A visible singleton forces minimal dimension four

Order the states `(x,y,h,k)`. After deleting the observed off-diagonal entries, write

\[
T=\begin{pmatrix}D&X\\Y&H\end{pmatrix},\qquad
H=\begin{pmatrix}-\ell_h&m\\n&-\ell_k\end{pmatrix}.
\]

Here `m=q_hk`, `n=q_kh`; either both are positive or both vanish. The quantities `ell_h=m+sum_i Y_hi` and `ell_k=n+sum_i Y_ki` are total hidden escape rates. For rank arguments, rescaling the two nonzero observed-rate columns of `B` and permuting the rows of `R` lets us use `B=(I_2,0)^T` and `R=(I_2,0)` without changing controllability or observability.

The relevant block powers are

\[
TB=\begin{pmatrix}D\\Y\end{pmatrix},\qquad
T^2B=\begin{pmatrix}D^2+XY\\YD+HY\end{pmatrix},
\]

and

\[
RT=(D,X),\qquad RT^2=(D^2+XY,DX+XH).
\]

Suppose some visible vertex has exactly one hidden neighbor, relabeled `h`. There are four possibilities for the other visible vertex's hidden-neighbor set.

**Opposite singleton `{k}`.** Both `X` and `Y` are diagonal up to permutation, with positive diagonal entries. They are invertible, so `[B,TB]` and `[R;RT]` have rank four.

**Full set `{h,k}`.** Both `X` and `Y` are triangular up to permutations, again with nonzero diagonal entries. The same rank-four argument applies.

**The same singleton `{h}` or the empty set.** The matrices have the forms `X=(x,0)` and `Y=(y^T,0)^T`, with `x,y` nonzero nonnegative two-vectors. Connectivity forces `m,n>0`, since hidden state `k` has no visible neighbors.

Choose a column `j` with `Y_hj=b>0`. The hidden projections of columns `j` of `TB` and `T^2B` are respectively

\[
\begin{pmatrix}b\\0\end{pmatrix},\qquad
\begin{pmatrix}*\\nb\end{pmatrix}.
\]

Their determinant is `n b^2>0`. Since the columns of `B` already span the visible coordinates, controllability has rank four. Similarly choose a row `i` with `X_ih=a>0`. The hidden restrictions of rows `i` of `RT` and `RT^2` are `(a,0)` and `(*,ma)`, with determinant `m a^2>0`. Together with the visible coordinate rows of `R`, this gives observability rank four.

Thus every connected four-state graph with a visible singleton is automatically a minimal realization of its full kernel. This is stronger than irreducibility alone and follows from the support-specific rank calculations above. All existing minimal fixed-topology and unknown-topology arguments therefore remain applicable to these models without adding an assumption.

Consequently a potentially nonminimal model has only zero or two hidden neighbors at each visible vertex. At least one visible vertex has two, by connectivity.

## 2. No hidden-hidden edge

When `m=n=0` and neither visible vertex is a singleton, there are only two possible supports.

**Both visible vertices have both hidden neighbors.** This is the full-positive diamond. The [existing diamond proof](compatibility-orbit.md) already treats minimal and nonminimal models: distinct hidden escape rates identify all rates up to hidden permutation; equal escapes give an unbounded fixed-topology entropy fiber. Its equal-escape construction uses the visible resolvent and remains valid when `X` or `Y` is singular.

**One visible vertex has no hidden neighbors and the other has both.** This is a tree, so entropy is identically zero on the fixed topology. Distinct hidden escape rates give minimal dimension four, by the same `[Y,HY]` and `[X;XH]` argument used for the diamond. Equal hidden escape rates are the potentially nonminimal case: both hidden states have their sole outgoing visible rate equal to the same number `a>0`, so their rows of `Y` coincide. Section 4 below shows that adding a positive hidden-hidden link preserves the full kernels and provides an unbounded family when topology is unknown.

## 3. Positive hidden-hidden edge with unequal visible exit rows

Now suppose `m,n>0`, every nonempty visible hidden-neighbor set is `{h,k}`, and `Y_h != Y_k`. No minimality assumption is needed.

Let `J` be the nonempty set of visible vertices with hidden neighbors. All `Y_hi,Y_ki` for `i in J` are positive. After exchanging hidden labels if necessary,

\[
0<r=\min_{i\in J}\frac{Y_{hi}}{Y_{ki}}<1.
\]

The ordering is possible because the two exit rows differ; inactive visible columns are zero on both rows and are omitted from the ratio.

Use the explicit hidden transformation

\[
U_e=\begin{pmatrix}1-e&e\\0&1\end{pmatrix},\qquad
S_e=\operatorname{diag}(I_2,U_e).
\]

For `0<=e<r`, transformed visible-hidden rates are

\[
X'_{ih}=(1-e)X_{ih},\quad X'_{ik}=X_{ik}+eX_{ih},\qquad
Y'_{hi}=\frac{Y_{hi}-eY_{ki}}{1-e},\quad Y'_{ki}=Y_{ki}.
\]

The hidden off-diagonal rates are

\[
H'_{kh}=n(1-e),\qquad
H'_{hk}=\frac{f(e)}{1-e},\qquad
f(e)=m+e(\ell_k-\ell_h)-ne^2.
\]

Starting with `f(0)=m>0`, stop at the first root `e_*` in `(0,r]`, if present, and otherwise at `e_*=r`. Every point before the endpoint has all required rates positive on the original support. The normalized hidden similarity preserves the full kernels whether or not the original realization is minimal: sufficiency follows directly from `T'=S_e^{-1}TS_e`, `RS_e^{-1}=R`, and `S_e B=B`.

The stationary law is

\[
\pi'_x=\pi_x,\quad\pi'_y=\pi_y,\quad
\pi'_h=(1-e)\pi_h,\quad\pi'_k=\pi_k+e\pi_h.
\]

All four components have strictly positive limits because `e_*<=r<1`. If `f(e_*)=0`, one hidden rate vanishes while its reverse stays positive. If `e_*=r`, at least one hidden-to-visible rate vanishes while its reverse remains positive. The corresponding entropy term diverges; all other edge terms are nonnegative. Rates remain bounded because the denominator is at least `1-r>0`.

Thus the triangular lemma in the earlier audit requires minimality only to deduce unequal exit rows. Once inequality of those rows is stated directly, this exact fixed-topology divergent family applies to nonminimal models too.

## 4. Equal visible exit rows: lumping gives a divergent family

Suppose instead

\[
Y_h=Y_k=y,\qquad a=y\mathbf1>0.
\]

All active visible-hidden legs are positive in both directions. The hidden block is

\[
H=\begin{pmatrix}-(a+m)&m\\n&-(a+n)\end{pmatrix}.
\]

The partition with singleton visible states and hidden block `{h,k}` is strongly lumpable. Its aggregate generator is

\[
\overline Q=\begin{pmatrix}A&X\mathbf1\\y&-a\end{pmatrix},
\]

which is independent of `m,n`. The observed edge remains between singleton blocks. For its membership matrix `L`, `TL=L Tbar`, `B=L Bbar`, and `RL=Rbar`, so the usual exponential intertwining gives equality of **all** joint observed kernels, including their normalization and time scale.

Keep all visible-hidden rates fixed and set `n>0` fixed, while taking `m->0+`. For every positive `m`, the original positive-hidden-edge topology is preserved. The aggregate stationary visible probabilities `pi_V` are fixed. Put

\[
I_h=\pi_V X_{:h}>0,\qquad
I_k=\pi_V X_{:k}>0,\qquad P=(I_h+I_k)/a.
\]

These influxes are strictly positive because at least one visible vertex is active, its stationary probability is positive, and both of its hidden entrance rates are positive. Solving the two hidden stationary balance equations gives

\[
\pi_h=\frac{I_h+nP}{a+m+n},\qquad
\pi_k=\frac{I_k+mP}{a+m+n}.
\]

Therefore

\[
\pi_h m\longrightarrow0,\qquad
\pi_k n\longrightarrow\frac{nI_k}{a+n}>0.
\]

The entropy contribution of `h<->k` diverges. This also follows from irreducibility of the limiting generator: each hidden state still communicates through an active visible vertex even when `h->k` vanishes. The explicit stationary formula makes the required nonzero opposing flux transparent. Every rate stays bounded along the path.

This proves fixed-topology unboundedness for equal exit rows whenever the hidden-hidden edge is present. It does not use a minimal-realization orbit; the varying models may have different hidden-mode spectra, while their aggregate observed kernels remain identical.

If the initial one-port tree in Section 2 has equal escape rates, its exit rows are identical and `m=n=0`. Adding arbitrary positive `m,n`, with the corresponding diagonal changes, leaves `Qbar` and all observed kernels unchanged. It creates the positive-hidden-edge graph just treated. Hence that tree's unknown-topology fiber is unbounded despite its fixed-topology entropy being identically zero.

## 5. Classification at exactly four states

The arguments cover every possible support and rate choice.

For a **fixed topology**:

| Case | Entropy fiber |
| --- | --- |
| A visible vertex has exactly one hidden neighbor | Singleton: automatic minimality and the previous absent-edge constraints identify the generator up to hidden labels. |
| No singleton, no hidden-hidden edge, one visible vertex inactive | Singleton `{0}`: the graph is a tree. |
| No singleton, no hidden-hidden edge, both visible vertices active | Full diamond: singleton for distinct hidden escapes, unbounded for equal escapes. |
| No singleton, hidden-hidden edge present | Unbounded: triangular similarity for unequal exit rows; strong lumping for equal exit rows. |

For **unknown topology on exactly these four states**, the [previous global proof](unknown-topology-audit.md) handles every automatically minimal singleton case, and the extensions above handle all potentially nonminimal cases. The only globally unique generators, up to hidden permutation, are:

1. Both visible endpoints have exactly one hidden neighbor, and those neighbors differ. The hidden-hidden edge may be present or absent.
2. The hidden-hidden edge is absent; one visible endpoint has only hidden neighbor `h`, the other has both; and the hidden escape rates satisfy `lambda_h>lambda_k`.

The second comparison uses total hidden escape rates, which here are simply the visible exit-rate sums because the hidden-hidden link is absent. Both classes are automatically minimal by Section 1. All other connected four-state cases have unbounded entropy fibers when topology is unknown.

In particular there is no overlooked finite non-singleton entropy set obtained from nonminimal realizations. The only new fixed-topology exception encountered in removing minimality is a thermodynamically unique tree, and allowing the hidden-hidden edge immediately provides its compatible divergent family.

## Limits of this extension

The result concerns exactly four microscopic states and one resolved observed pair, under simple bidirected support and complete exact kernels. It does not classify unions allowing additional states, impose a finite-sample inference procedure, determine the infimum of every unbounded fiber, or treat extra thermodynamic channels. The global theorem still depends on the previously audited global constraints for minimal singleton models; those arguments should be retained in a consolidated proof.

The audit found no mathematical gap in this extension. Its contribution is the support-specific automatic-minimality proof and the separation of two nonminimal mechanisms: an explicit sufficient similarity when exit rows differ, and strong lumpability when they coincide. Independent computation may verify representative formulas; publication novelty remains unestablished.
