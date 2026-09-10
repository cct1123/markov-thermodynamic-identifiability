# Compatibility orbits and the four-state diamond

Date: 2026-09-10 (UTC). Contribution type: analytic derivation. This note gives exact arguments under the [working formulation](formulation.md), extending the [small-network audit](small-network-audit.md). Representative cases are checked by [check_small_networks.py](check_small_networks.py). No novelty or exhaustive graph classification is asserted.

## Assumptions and conclusion

Use finite irreducible, time-homogeneous CTMCs with a simple bidirected graph and row generator `Q`. Observed marks resolve directed edges with known incidence, and the observed set is nonempty and closed under reversal. Data are the full joint next-mark/time kernel, including its absolute time scale and normalization. Let `V` contain every endpoint of an observed edge and place these visible states before the hidden states. Minimality refers to the linear realization of the entire matrix-valued kernel, not to the number of distinct poles in an individual entry.

For two minimal realizations of the same data, the compatibility transformation is exactly

\[
Q'=S^{-1}QS,\qquad S=\operatorname{diag}(I_V,U),\qquad U\mathbf1=\mathbf1,
\]

where `U` is invertible. Its entries may be signed. The transformed generator must satisfy the chosen topology, positivity, and irreducibility constraints. For four states and one observed bidirectional edge, this leaves two real similarity parameters before those physical constraints are imposed.

For the known full four-state diamond topology, the reduction and a direct resolvent calculation give a sharper result: distinct hidden escape rates imply a unique generator up to exchanging the hidden labels; equal hidden escape rates give an unbounded entropy fiber, whether or not the realization is minimal. These escape-rate strata are distinguishable from the data within this topology. Thus there is no bounded-but-nonunique fiber on this full diamond topology under the unrestricted positive-rate convention. This is a topology-specific result; other four-state topologies remain open here.

## 1. Short proof of minimal-realization similarity

Write the two kernel realizations as

\[
\Psi(t)=R e^{Tt}B=R' e^{T't}B'.
\]

Equality implies equality of all Markov parameters:

\[
R T^k B=R'T'^kB',\qquad k=0,1,\ldots.
\]

A realization is controllable if the columns of all `T^k B` span its state space, and observable if `R T^k z=0` for all `k` implies `z=0`. Here a minimal realization has both properties. They also directly certify minimal dimension: a sufficiently large block Hankel matrix of the Markov parameters factors as an observability matrix times a controllability matrix of full state-space rank; any competing realization factors the same matrix through its own state space.

Define `S` on the primed reachable vectors by

\[
S\left(\sum_k T'^k B' z_k\right)=\sum_k T^k B z_k,
\]

where each sum is finite. This is well-defined. If a primed sum vanishes, applying `R T^ell` to the proposed unprimed image gives the corresponding primed Markov-parameter sum, which vanishes for every `ell`; unprimed observability makes the image zero. Reversing the argument gives an inverse map. Controllability on both sides makes the domain and range the entire spaces, so the minimal dimensions agree and `S` is invertible.

Applying this definition on a spanning collection of reachable vectors gives

\[
S B'=B,\qquad S T'=T S,\qquad R S=R'.
\]

Hence

\[
T'=S^{-1}TS,\qquad B'=S^{-1}B,\qquad R'=RS.
\]

The mapping is unique for a fixed pair of labeled controllable realizations. This proof uses the shared matrix-valued kernel; fitting separate scalar waiting densities would not justify it.

## 2. Resolved reverse marks pin the visible coordinates

For any observed mark `J=(a_J,b_J)`, its reverse `bar(J)` ends at `a_J`. Thus

\[
\psi_{\bar J,J}(0)=q_{a_J b_J}.
\]

All observed rates are therefore determined from the data. Known incidence and those rates give the same `R` and `B` in any compatible model, after fixing the visible labels. The rows of `R` include the coordinate row for every visible endpoint, and the columns of `B` include a positive multiple of its coordinate column; reversal closure ensures neither side misses an endpoint.

Because `R'=R` and `B'=B`, the similarity satisfies `RS=R` and `SB=B`. The first identity fixes every visible row of `S` to its identity row, and the second fixes every visible column. Consequently

\[
S=\begin{pmatrix}I_V&0\\0&U\end{pmatrix}.
\]

Let `E` contain exactly the observed off-diagonal entries of `Q`, so `T=Q-E`. Since `E` acts only in the fixed visible coordinates, `S^{-1}ES=E` and

\[
Q'=T'+E=S^{-1}QS.
\]

The transient matrix obeys

\[
T\mathbf1=-B\mathbf1,\qquad T'\mathbf1=-B\mathbf1.
\]

The right-hand `1` has the observed-mark dimension. The matrix `T` is invertible: a finite irreducible CTMC with a nonempty observed edge set reaches a next observed edge almost surely with finite mean, so the survival semigroup tends to zero and `-T^{-1}` is its time integral. From `TS=ST'` and `SB=B`,

\[
T S\mathbf1=S T'\mathbf1=-S B\mathbf1=-B\mathbf1=T\mathbf1.
\]

Invertibility gives `S1=1`, or `U1=1`.

Conversely, any such invertible `S` for which `Q'=S^{-1}QS` is an admissible generator has the same observed rates, incidence, and full kernel. Indeed `T'=S^{-1}TS`, `RS^{-1}=R`, and `SB=B`. Minimality is also preserved. Its stationary law is `pi'=pi S`; this is normalized and stationary, and positivity then follows from uniqueness of the normalized stationary vector of an irreducible generator. Thus a separate positivity check on `pi S` is unnecessary once generator admissibility has been proved.

This characterizes the entire minimal compatibility fiber at its fixed dimension through physical inequalities on `U`. It does not characterize larger nonminimal models when additional hidden states are allowed.

## 3. Four states and one observed edge

With two hidden states, every real matrix satisfying the normalization condition has the form

\[
U=\begin{pmatrix}u&1-u\\v&1-v\end{pmatrix},\qquad u-v\ne0.
\]

No condition `0<=u,v<=1` is imposed by the observation equivalence itself. Restricting to stochastic `U` would discard potentially physical compatible generators. For a particular graph, the off-diagonal signs and required zeros of `S^{-1}QS` determine the admissible region of this two-parameter plane.

This is a finite-dimensional compatibility reduction, not yet an entropy-range classification. In particular, a sequence can approach a singular `U`, a generator boundary, or both; neither a formal pole in the transformation nor an individual vanishing rate alone establishes entropy divergence without examining stationary fluxes.

## 4. Known full diamond: distinct escapes imply uniqueness

The full diamond here has observed link `x<->y` and all four hidden-visible links `x<->h`, `x<->k`, `y<->h`, `y<->k`, each positive in both directions; there is no `h<->k` link. In block form,

\[
Q=\begin{pmatrix}A&X\\Y&H\end{pmatrix},\qquad
H=\operatorname{diag}(-\lambda_h,-\lambda_k),
\]

where `X,Y` are strictly positive `2 x 2` matrices and `lambda_i=(Y1)_i>0`. Removing the observed link changes only `A`, leaving the same `X,Y,H` in `T`. Write that killed visible block as `D`.

For distinct `lambda_h,lambda_k`, this full diamond is automatically minimal. To see observability, an unobservable vector first has zero visible components. Its hidden component `z` must then satisfy `Xz=0` and `XHz=0`, from the first and second derivatives. Any positive row `(x_h,x_k)` of `X` gives two equations with coefficient determinant `x_h x_k(lambda_h-lambda_k)`, which is nonzero. Hence `z=0`. The transposed argument, using a positive column of `Y` and `[Y,HY]`, gives controllability. Equivalently one can subtract the visible `D` contributions when comparing the first two powers of `T`.

Every compatible four-state generator is then also minimal, because the kernel has minimal dimension four. The orbit theorem applies, with

\[
X'=XU,\qquad Y'=U^{-1}Y,\qquad H'=U^{-1}HU.
\]

Known absence of the hidden-hidden edge forces `H'` diagonal. The columns of `U` must therefore be eigenvectors of the diagonal matrix `H`. With two distinct eigenvalues each eigenvector is a coordinate vector, so invertibility makes `U` a monomial matrix: a permutation times a nonsingular diagonal scaling. The normalization `U1=1` forces each nonzero row entry to be one. Thus `U` is exactly a hidden-label permutation.

All rates are unique up to this permutation; the entropy-production rate is unique. This result assumes the fixed diamond topology. If additional hidden-hidden edges or additional states are allowed, the requirement that `H'` stay diagonal no longer gives this conclusion.

### The escape-rate strata are determined by the data

As in the prior audit, the observed rates and four waiting kernels determine the visible block `K(t)=[exp(Tt)]_VV`. Its first derivative determines `D=K'(0)`. A Schur complement gives, for sufficiently large real `z`,

\[
\widehat K(z)=\left[zI-D-X(zI-H)^{-1}Y\right]^{-1}.
\]

The data therefore determine the rational matrix

\[
F(z)=zI-D-\widehat K(z)^{-1}
=\sum_{i\in\{h,k\}}\frac{x_i y_i}{z+\lambda_i},
\]

where `x_i` is the corresponding column of `X` and `y_i` the row of `Y`. Each residue `x_i y_i` has strictly positive entries and is nonzero. If the escape rates differ, neither of the two distinct poles can cancel; if they agree, there is exactly one pole with residue `M=XY`. Thus a full-positive distinct-escape diamond and a full-positive equal-escape diamond cannot produce identical observed data. This argument does not assume minimality.

For distinct escapes there is also a direct rate reconstruction from these residues. If `Z_i=x_i y_i` is the residue at `-lambda_i`, then `y_i 1=lambda_i` gives `x_i=Z_i 1/lambda_i`. Dividing any row of `Z_i` by the corresponding positive component of `x_i` then recovers `y_i`. This supplies an independent algebraic way to see uniqueness up to exchanging the poles and hidden labels.

## 5. Equal escapes: minimality and unbounded entropy

When `lambda_h=lambda_k=lambda`, the hidden block is `H=-lambda I`. Every invertible hidden similarity preserves this scalar block, so the diagonal constraint imposes no further restriction on `U`.

In this case minimality holds exactly when both `X` and `Y` are invertible. Sufficiency follows from the full ranks of `[B,TB]` and `[R;RT]`. If `X` is singular, a nonzero `z` in its null space produces an unobservable eigenvector `(0,z)` of `T` with eigenvalue `-lambda`; if `Y` is singular, the transposed argument produces an uncontrollable direction. Repeated hidden escape rates therefore do not imply nonminimality.

### Every positive equal-escape diamond has an unbounded fiber

Put `a=(X1)_x>0`, `c=(X1)_y>0`, and `M=XY`. Since `Y1=lambda 1`, define

\[
\alpha=\frac{M_{xx}}{\lambda a},\qquad
\beta=\frac{M_{yx}}{\lambda c}.
\]

Strict positivity gives `0<alpha,beta<1`. If the realization is minimal they are different, because equality would make `M` singular; for a nonminimal model they may be equal. Either way, choose

\[
0<p<\min(\alpha,\beta),\qquad
\max(\alpha,\beta)<q<1,
\]

and define

\[
Y_{p,q}=\lambda\begin{pmatrix}p&1-p\\q&1-q\end{pmatrix},
\qquad
X_{p,q}=\begin{pmatrix}
a\dfrac{q-\alpha}{q-p}&a\dfrac{\alpha-p}{q-p}\\
c\dfrac{q-\beta}{q-p}&c\dfrac{\beta-p}{q-p}
\end{pmatrix}.
\]

These matrices are strictly positive, and `Y_pq` is invertible. The rank of `X_pq` is the rank of `M`, so no assumption that `X_pq` is invertible is needed. Direct multiplication gives `X_pq 1=X1`, `Y_pq 1=lambda 1`, and `X_pq Y_pq=M`. With the unchanged visible block `A` and hidden block `H`, they therefore define admissible full-diamond generators.

All of them give the same full kernels because the Schur complement above depends on the hidden part only through `F(z)=M/(z+lambda)`. In the minimal case they are also in the same hidden-similarity orbit: `U=X^{-1}X_pq` is invertible, obeys `U1=1`, and gives `U^{-1}Y=Y_pq`. For nonminimal models the direct resolvent argument is needed; a similarity between the original and constructed realization is not claimed.

Their stationary visible probabilities remain fixed, including in the nonminimal case. Eliminating the hidden stationary vector gives

\[
\pi_H=\pi_V X/\lambda,\qquad
\pi_V(A+M/\lambda)=0,\qquad
\pi_V\left[\mathbf1+X\mathbf1/\lambda\right]=1.
\]

Both equations determining `pi_V` are invariant. The effective two-state matrix `A+M/lambda` has zero row sums and positive off-diagonal entries, so its stationary ratio is unique; the displayed normalization fixes the scale. In particular `pi_x,pi_y` are fixed and strictly positive.

Now hold `q` fixed in its admissible interval and let `p->0+`. The rate `q_hx=lambda p` tends to zero, whereas

\[
q_{xh}=a\frac{q-\alpha}{q-p}\longrightarrow a\frac{q-\alpha}{q}>0.
\]

The forward stationary flux on `x->h` therefore tends to a strictly positive value. The reverse stationary flux is at most `lambda p`, and hence tends to zero. Its unoriented-edge entropy contribution diverges, so the total entropy is unbounded. Every rate remains uniformly bounded: hidden exits are at most `lambda`, and hidden entrance rates are at most their fixed row totals `a,c`.

This establishes unboundedness for every full-positive equal-escape diamond fiber, including nonminimal realizations. Together with the distinct-escape reconstruction and noncancellation of poles, it exhausts the full-positive fixed four-state diamond into unique-entropy and unbounded-entropy classes. It does not give the infimum of the equal-escape fibers in general. In particular it does not claim that a kernel with observable irreversibility has an equilibrium compatible model.

### A compact example with the complete entropy range

Take

\[
Q_0=\begin{pmatrix}
-4&1&2&1\\
1&-4&1&2\\
2&1&-3&0\\
1&2&0&-3
\end{pmatrix}
\]

in order `(x,y,h,k)`, observing only `x<->y`. Here `X=Y=[[2,1],[1,2]]` have determinant three, `H=-3I`, and symmetry gives the equilibrium stationary law `(1,1,1,1)/4`.

Set `U_e=[[1-e,e],[0,1]]` for `0<=e<1/2`. Its transformed generator is

\[
Q_e=\begin{pmatrix}
-4&1&2(1-e)&1+2e\\
1&-4&1-e&2+e\\
\dfrac{2-e}{1-e}&\dfrac{1-2e}{1-e}&-3&0\\
1&2&0&-3
\end{pmatrix},\qquad
\pi_e=\tfrac14(1,1,1-e,1+e).
\]

All required edge rates are positive and bounded. Minimality and all joint kernels are invariant. The visible current is zero, and the currents on `(x,h),(y,h),(x,k),(y,k)` are `(-e,e,e,-e)/4`. Consequently

\[
\sigma(e)=\frac e4\log\frac{(1+2e)(2-e)}{(1-2e)(2+e)}.
\]

At `e=1/4`, this is `log(7/3)/16`; as `e->1/2-`,

\[
\sigma(e)=\frac18\log\frac1{1/2-e}+O(1).
\]

Continuity and `sigma(0)=0` show that this particular minimal fixed-diamond fiber has entropy range exactly `[0,infinity)`.

The scalar hidden block should not be described as a repeated pole of the full observed transfer function. In this example the four eigenvalues of the killed generator are `(-7+sqrt(37))/2`, `(-7-sqrt(37))/2`, `(-7+sqrt(5))/2`, and `(-7-sqrt(5))/2`, all distinct. The degeneracy is in the hidden escape block, while the full kernel remains of minimal dimension four.

## What remains unproved

The orbit theorem gives a complete parameterization only for minimal models at their fixed dimension, and the diamond classification assumes all five specified undirected links are present with positive rates. It does not classify other four-state topologies, larger cardinalities, unknown observed-edge incidence, nonminimal realizations with additional hidden states, or physically imposed rate bounds and channel constraints.

The next concrete question is whether any minimal four-state fiber with a fixed simple bidirected topology is bounded but nonunique in entropy when rates are merely positive, without an artificial common positive rate cutoff. The full diamond has been ruled out by the arguments above, while the complete-graph example in the prior audit supplies an unbounded fiber. Other topologies and other complete-graph fibers remain unclassified.

A general answer needs a criterion linking the admissible similarity region and its generator boundary to entropy. A boundary where one stationary edge flux vanishes and its reverse stays positive is sufficient for divergence. It remains unproved here whether every thermodynamically nonunique minimal four-state fiber necessarily has such a boundary (or another divergent sequence), or whether some can remain entropy-bounded despite nonunique generators. A topology label or minimality alone does not decide this.

Literature constraints and novelty limitations are recorded in [E012](../evidence/RECORDS.md#e012) and [E021](../evidence/RECORDS.md#e021).
