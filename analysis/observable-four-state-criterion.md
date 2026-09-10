# An observable uniqueness criterion at exactly four states

Date: 2026-09-10 UTC. Contribution: analytic derivation and independent audit, not a publication-novelty claim. No numerical computation is reported here. The admissible model and entropy conventions are those of [formulation.md](formulation.md). The necessity and unbounded-complement statements below use the complete support classification in [unknown-topology-audit.md](unknown-topology-audit.md) and its [nonminimal extension](nonminimal-four-state-audit.md). The sufficient conditions and explicit reconstructions are also proved directly here.

## Scope and result

Assume the data admit an irreducible simple bidirected CTMC on **exactly four microscopic states**, with known observed incidence consisting of the individually resolved pair `x<->y`. The other two states are hidden. All joint next-mark/time kernels are known exactly, including their absolute time scale. Allow every connected bidirected topology on these four states, with no common positive lower bound on present rates. Minimality is not assumed.

The classification has a finite operational test. Recover the two observed rates `r,s` and the visible killed-semigroup block `K(t)` from the kernels as in Section 1, then compute

\[
D=K'(0),\qquad A=D+\begin{pmatrix}0&r\\s&0\end{pmatrix},\qquad a=-A\mathbf1,
\]

\[
M=K''(0)-D^2,\qquad L=K'''(0)-D^3-DM-MD.
\]

Only derivatives through order three are needed. All matrices in these tests are two by two, in the fixed visible order `(x,y)`.

The compatible generator is unique up to hidden-state permutation, and hence has unique entropy production, **if and only if at least one of these two observable conditions holds**:

**A. Disjoint hidden incidence.**

\[
a_x>0,\qquad a_y>0,\qquad M_{xy}=M_{yx}=0.
\]

**B. A shared fast pole and a single-endpoint slow pole.** The matrix `M` is invertible, `J=LM^{-1}` has distinct eigenvalues `-lambda_f,-lambda_s` with `lambda_f>lambda_s>0`, and the matrices

\[
Z_f=-\frac{L+\lambda_sM}{\lambda_f-\lambda_s},\qquad
Z_s=\frac{L+\lambda_fM}{\lambda_f-\lambda_s}
\]

satisfy, for some endpoint `j in {x,y}`,

\[
\operatorname{rank}Z_f=1,\quad Z_f>0\ \text{entrywise},\quad
Z_s=c\,e_j e_j^T,\quad c>0.
\]

Equivalently, the observable hidden transfer matrix in Section 1 has the exact decomposition

\[
F(z)=\frac{Z_f}{z+\lambda_f}+\frac{Z_s}{z+\lambda_s}
\]

with these pole and residue conditions. Section 5 proves why the finite derivative test determines this whole rational matrix under exactly-four-state admissibility. The poles are not fitted poles of an individual waiting density.

If neither condition holds, the compatible entropy-production rates are unbounded above. This last conclusion is a statement about the supremum; it does not specify the infimum or assert an equilibrium compatible model.

The assumption that an admissible exactly-four-state realization exists is essential. These conditions are not presented as a general feasibility test for arbitrary functions, a test for arbitrary state counts, or a finite-sample inference procedure.

## 1. Extracting the observable matrices

Write the observed marks as `+=x->y` and `-=y->x`, and their rates as `r=q_xy` and `s=q_yx`. The complete joint kernels give

\[
r=\psi_{-,+}(0)>0,\qquad s=\psi_{+,-}(0)>0.
\]

For the killed generator `T`, with only the two observed off-diagonal rates removed, its visible semigroup block is determined by

\[
K(t)=[e^{Tt}]_{VV}=
\begin{pmatrix}
\psi_{-,+}(t)/r&\psi_{-,-}(t)/s\\
\psi_{+,+}(t)/r&\psi_{+,-}(t)/s
\end{pmatrix}.
\]

In particular `K(0)=I_2`. Let

\[
D=K'(0),\qquad
A=D+\begin{pmatrix}0&r\\s&0\end{pmatrix},\qquad
a=-A\mathbf1.
\]

Here `D` is diagonal because the only edge between the two visible states is observed. The values `a_i` are the total rates from visible endpoint `i` into the hidden states, not the total visible escape rates.

For any compatible generator, write

\[
Q=\begin{pmatrix}A&X\\Y&H\end{pmatrix},\qquad
T=\begin{pmatrix}D&X\\Y&H\end{pmatrix}.
\]

The hidden block `H` is transient: in a finite irreducible chain, a path out of the hidden set exists from every hidden state. Consequently `H` is invertible and its eigenvalues have negative real parts. The Schur complement gives

\[
\widehat K(z)=\left[zI-D-X(zI-H)^{-1}Y\right]^{-1},
\]

so the data determine

\[
F(z)=zI-D-\widehat K(z)^{-1}=X(zI-H)^{-1}Y.
\]

The identities initially hold for sufficiently large positive `z` and extend as rational identities. The inverse at `z=0` is also legitimate under these admissibility assumptions. Generator normalization gives

\[
X\mathbf1=a,\qquad H\mathbf1=-Y\mathbf1,
\qquad F(0)\mathbf1=X(-H)^{-1}Y\mathbf1=X\mathbf1=a.
\]

This last identity supplies the normalization needed in the residue reconstruction; it must not be assumed for arbitrary unverified data.

Define a second Laurent coefficient `L` by

\[
F(z)=\frac{M}{z}+\frac{L}{z^2}+O(z^{-3}),\qquad M=XY,\qquad L=XHY.
\]

Both coefficients can be extracted directly from derivatives, without a Laplace transform:

\[
M=K''(0)-D^2,\qquad
L=K'''(0)-D^3-DM-MD.
\]

These formulas retain matrix multiplication order. They follow by multiplying the displayed blocks of `T` twice and three times.

## 2. Condition A: direct support identification and reconstruction

For a visible endpoint `i`, let `N_i` be its hidden-neighbor set. Bidirectionality means `X_ih>0` exactly when `Y_hi>0`. Therefore

\[
M_{xy}=\sum_{h}X_{xh}Y_{hy}=0
\]

holds exactly when no hidden state is adjacent to both visible endpoints. All summands are nonnegative; cancellation is impossible. The same support statement is equivalent to `M_yx=0` for admissible bidirected data. Keeping both zero tests makes the criterion symmetric.

The positive entrance totals make `N_x,N_y` nonempty. Since there are exactly two hidden states, disjointness forces `N_x={h}` and `N_y={k}` after hidden relabeling. Thus `X,Y` are positive diagonal matrices. In particular `M_xx,M_yy>0` follow from admissibility and need not be added as independent assumptions.

All rates can now be reconstructed from observable quantities:

\[
X=\operatorname{diag}(a_x,a_y),\qquad
Y=\operatorname{diag}\left(\frac{M_{xx}}{a_x},\frac{M_{yy}}{a_y}\right),
\qquad H=X^{-1}LY^{-1}.
\]

Together with the known block `A`, these fix `Q`. The existence assumption ensures the reconstructed hidden rates and row sums are admissible. More strongly, every admissible candidate must have the displayed blocks, so no competing topology or disconnected branch of a similarity parameterization can evade the argument.

The hidden-hidden edge can be present or absent. If it is absent and both hidden escape rates coincide, `F` has only one pole with a rank-two residue. Condition A still applies: counting distinct poles alone would incorrectly discard this unique minimal four-state case.

## 3. Condition B: normalized reconstruction

For each pole label `ell in {f,s}`, define the corresponding column of `X` by

\[
x_\ell=\frac{Z_\ell\mathbf1}{\lambda_\ell}.
\]

Choose any row index `i` with `(x_ell)_i>0` and set

\[
y_\ell=\frac{(Z_\ell)_{i,:}}{(x_\ell)_i}.
\]

The rank-one condition makes this independent of the chosen nonzero row and gives `x_ell y_ell=Z_ell` and `y_ell 1=lambda_ell`. In the slow case, explicitly,

\[
x_s=(c/\lambda_s)e_j,\qquad y_s=\lambda_s e_j^T.
\]

Use `X=(x_f,x_s)`, `Y=(y_f;y_s)`, and

\[
H=\operatorname{diag}(-\lambda_f,-\lambda_s).
\]

The fast column and row are strictly positive; the slow state is adjacent only to endpoint `j`. All visible-hidden links are therefore bidirected. The graph is connected because the observed pair is positive in both directions and the fast hidden state is shared. All present rates are finite and positive. Normalization follows from

\[
X\mathbf1=\frac{Z_f\mathbf1}{\lambda_f}+
\frac{Z_s\mathbf1}{\lambda_s}=F(0)\mathbf1=-A\mathbf1,
\qquad Y\mathbf1=-H\mathbf1.
\]

Thus the reconstructed blocks form an admissible generator. Their Schur complement equals the observed `F` with the observed `D`, so they reproduce `K`, and hence all original joint kernels.

### Direct exclusion of competing hidden edges

Consider any compatible four-state generator. Both its visible entrance totals are positive, as is already implied by the strictly positive fast residue and `F(0)1=a`. Its two rows of `X` and, by bidirectionality, its two columns of `Y` are consequently nonzero and nonnegative.

If its hidden-hidden edge were present, `H` would be an irreducible two-by-two Metzler matrix. Its slow eigenvalue is simple, with strictly positive right and left eigenvectors `v,w`. Its slow spectral projector is `v w^T/(w^T v)`. Since `F` has two distinct poles and `H` has dimension two, these poles must be precisely its two eigenvalues. The slow-pole residue would therefore be

\[
\frac{(Xv)(w^TY)}{w^Tv}>0\quad\text{entrywise}.
\]

This contradicts `Z_s=c e_j e_j^T`. In particular the slow mode cannot disappear by cancellation: its residue is strictly positive in this situation.

Bidirectionality now forces **both** hidden off-diagonal rates to be zero. With `H` diagonal and two distinct observed poles, its diagonal entries are fixed to `-lambda_f,-lambda_s` up to permutation. Each pole residue is exactly one column-row product. The hidden row-sum equations then force the normalized reconstruction above. Thus the compatible generator is unique without needing to assume minimality or appeal to a local similarity calculation.

The fast/slow ordering is essential. A shared slow pole and a singleton fast pole is not condition B. Likewise two strictly positive pole residues may identify a generator when the full diamond topology is prescribed, but they do not satisfy this unknown-topology uniqueness test.

## 4. Minimality, necessity, and the unbounded complement

Both sufficient cases automatically have nonsingular `M=XY`:

- In A, `M` is diagonal with strictly positive diagonal entries.
- In B, if `i` is the endpoint other than `j`, then `det M=c(Z_f)_{ii}>0`, using `det Z_f=0`.

Hence `X,Y` are invertible. With input and output rescaled to the visible coordinate inclusions, `[B,TB]` and `[R;RT]` have rank four. The full joint-kernel realization is therefore minimal of dimension four. This is a rank argument, not a count of poles of `F` or of the full waiting kernel.

The two global-uniqueness cases established in the linked support audits translate exactly into A and B. Opposite singleton hidden-neighbor sets give A by positivity. In the other case, there is no hidden-hidden edge, one hidden state is shared, the other touches one endpoint, and the shared state's escape rate is strictly larger. Its diagonal hidden block produces precisely B, with both residues nonzero and no pole cancellation. Thus every unique case in the complete exactly-four-state classification is detected.

The [nonminimal audit](nonminimal-four-state-audit.md) supplies the remaining step: every nonminimal exactly-four-state data fiber is unbounded when topology is unknown. Its construction does not assume equivalence implies similarity for nonminimal models. Together with the minimal global classification, this proves that failure of both A and B implies an unbounded entropy fiber, even if minimality was not known in advance.

## 5. Why third-order derivatives suffice

For admissible exactly-four-state data, A and B can be decided from `K^(n)(0)` for `n=0,1,2,3` and the two observed rates. Condition A already uses only `A` and `M`.

If `M` is singular, neither unique case is possible, so the entropy fiber is unbounded by the classification. If `M` is invertible, define

\[
J=LM^{-1}.
\]

Because both `X,Y` are then invertible in every candidate,

\[
J=XHX^{-1},\qquad F(z)=(zI-J)^{-1}M.
\]

If `J` has distinct eigenvalues `-lambda_f,-lambda_s`, with `lambda_f>lambda_s>0`, its exact residues are

\[
Z_f=-\frac{L+\lambda_sM}{\lambda_f-\lambda_s},\qquad
Z_s=\frac{L+\lambda_fM}{\lambda_f-\lambda_s}.
\]

Testing these matrices against B is equivalent to testing the rational function. No independently fitted exponential decomposition or numerical inverse Laplace transform is required. Repeated eigenvalues do not satisfy B; condition A must still be checked. A nonsingular `M` is sufficient for minimality here but is not necessary for minimality in general, so singular `M` should not itself be called a nonminimality test.

This finite criterion relies on exact four-state admissibility to identify the whole two-dimensional hidden realization from these coefficients. It does not assert that three derivatives determine unrestricted higher-dimensional kernels. Exact zeros, ranks, and pole ordering also cannot be replaced by arbitrary numerical thresholds without a separate statistical analysis.

Once a unique generator is reconstructed, its stationary law and entropy follow from the usual normalized stationary equations and the entropy formula in [formulation.md](formulation.md). No claim is made here about entropy minima in the unbounded cases, additional hidden states, unknown mark incidence, or publication novelty.
