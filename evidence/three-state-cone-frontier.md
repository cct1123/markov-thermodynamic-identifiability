# Three-state cone frontier: static factorization versus invariant realization

Inspected 2026-09-10 UTC, after maintenance commit `c4df036`, for the renewed exact global theta(100,100) question. Contribution: bounded primary-source review and a separate analytic deduction. This note uses the existing [positive-realization frontier](positive-realization-frontier.md), [strict cone reduction](../analysis/positive-realization-obstructions.md), and [fast-case coordinates](../analysis/theta-fast-case-audit.md). No source files were saved and no new optimization or framework was introduced.

**Outcome — inference.** Rank-three stochastic-factorization topology and infinitesimal rigidity are established prior art. Neither inspected theorem imposes the extra invariant-cone condition needed for a CTMC realization. Every finite block Hankel truncation of theta(100,100)'s uniformized hidden response admits strictly positive factors of inner dimension three, even though the source generator is locally isolated. This is the three-mode hidden response; the full marked kernel has minimal dimension five. Ordinary static factorization uniqueness or boundary tests therefore cannot certify the desired CTMC uniqueness. This source check supplies prior-art constraints, not the global classification.

The separate [spectral-cone proof](../analysis/theta-fast-spectral-audit.md) now establishes global CTMC uniqueness. The finite-Hankel construction below therefore also shows that strict finite factorizations can coexist with global dynamical identifiability.

## 1. Primary rigidity theorem and its scope

Robert Krone and Kaie Kubjas, *Uniqueness of nonnegative matrix factorizations by rigidity theory*, SIAM Journal on Matrix Analysis and Applications 42(1), 134–164 (2021), [DOI](https://doi.org/10.1137/19M1279472). The full [arXiv v3 preprint](https://arxiv.org/pdf/1902.02868v3), dated 2 September 2020, was inspected. Locators use preprint pages.

**Primary results.** For finite matrices with rank = nonnegative rank = r, Section 3, pp. 8–10, characterizes infinitesimal motions using active `AD,−DB` inequalities. Proposition 4.2, p. 12, gives infinitesimal ⇒ local rigidity, not global uniqueness. Proposition 5.3, pp. 19–20, characterizes the relative boundary for positive rank-r matrices: every size-r nonnegative factorization must contain a zero.

**Task mapping — inference.** The repository adds generator inequalities to this tangent-cone principle. One sparse factorization does not satisfy the boundary criterion's universal quantifier.

## 2. Primary rank-three topology theorem

David Mond, Jim Smith and Duco van Straten, *Stochastic factorizations, sandwiched simplices and the topology of the space of explanations*, Proceedings of the Royal Society A 459, 2821–2845 (2003); [DOI](https://doi.org/10.1098/rspa.2003.1150), [full author-hosted journal PDF](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/30.Stochastic%20factorizations,%20sandwiched%20simplices%20and%20the%20topology%20of%20the%20space%20of%20explanations%20-%202003.pdf). Sections 2, 4–5 were inspected; locators use printed pages.

**Primary results.** Theorem 2.4/Corollary 2.5, p. 2827, identify rank-size stochastic factorizations with nested simplices modulo permutations. For rank-three n×m stochastic matrices, Theorem 1.2, pp. 2822–2823, gives empty fibers, circle homotopy type, or at most n+m contractible components. Theorem 4.9, p. 2842, bounds components by the polygons' total edge count; two triangles give a connected space. Section 5, pp. 2842–2843, constructs squares with eight isolated intermediate triangles.

**Task mapping — inference.** Disconnectedness is established prior art. Dynamics additionally requires operator invariance, so unrestricted triangle-space topology does not classify CTMC fibers or their entropy.

## 3. Exact finite-Hankel obstruction to a proposed shortcut

**Analytic deduction for this task.** For theta(100,100), write

\[
X=\begin{pmatrix}2&0&8\\0&7&11\end{pmatrix},\qquad
Y=\begin{pmatrix}3&0\\0&6\\100&100\end{pmatrix},\qquad
H=\begin{pmatrix}-7&4&0\\5&-11&0\\0&0&-200\end{pmatrix}.
\]

The fixed-trace uniformization uses γ=218. Put `P=I+H/218` and `B=Y/218`. Then

\[
P=\frac1{218}
\begin{pmatrix}211&4&0\\5&207&0\\0&0&18\end{pmatrix}.
\]

For finite nonnegative integers m,n define

\[
O_m=\begin{pmatrix}X\\XP\\\vdots\\XP^m\end{pmatrix},\qquad
C_n=\begin{pmatrix}B&PB&\cdots&P^nB\end{pmatrix}.
\]

Their product is the block Hankel matrix with blocks `XP^(i+j)B`. For all k≥1, both `XP^k` and `P^kY` are entrywise positive: the upper two-state block of P is strictly positive, while its third diagonal entry is positive. At k=0, only the four indicated entries of X and Y vanish.

Choose

\[
U_\varepsilon=
\begin{pmatrix}1&\varepsilon&-\varepsilon\\
\varepsilon&1&-\varepsilon\\0&0&1\end{pmatrix},
\qquad \det U_\varepsilon=1-\varepsilon^2,
\qquad U_\varepsilon\mathbf1=\mathbf1.
\]

For small ε>0,

\[
XU_\varepsilon=
\begin{pmatrix}2&2\varepsilon&8-2\varepsilon\\
7\varepsilon&7&11-7\varepsilon\end{pmatrix}>0.
\]

The new formerly zero entries of `Uε⁻¹Y` are

\[
(U_\varepsilon^{-1}Y)_{hy}
=\frac{\varepsilon(94-100\varepsilon)}{1-\varepsilon^2},\qquad
(U_\varepsilon^{-1}Y)_{kx}
=\frac{\varepsilon(97-100\varepsilon)}{1-\varepsilon^2}.
\]

They are positive, for example whenever `0<ε<94/100`; all the other entries are positive there as well. Every remaining row or column in the chosen finite truncation was already strictly positive. By continuity there is an ε>0, depending on m,n, for which

\[
O_mU_\varepsilon>0,\qquad U_\varepsilon^{-1}C_n>0,
\qquad O_mC_n=(O_mU_\varepsilon)(U_\varepsilon^{-1}C_n).
\]

Thus **each finite block Hankel truncation of the uniformized hidden response has strictly positive factors of inner dimension three**. When the truncation has ordinary rank three, as every sufficiently large truncation does by minimality, these are size-equals-rank factorizations. Small truncations may have smaller ordinary rank; the inner-dimension-three assertion still holds.

The factors have an open neighborhood of alternative positive factors, so their ordinary NMF is not globally rigid. Applying Krone–Kubjas Proposition 5.3 to a rank-three truncation places it in the relative interior of the nonnegative-rank-three set. Neither positivity of finitely many moments nor uniqueness of their static factorization captures the missing generator constraint.

Indeed this particular similarity is explicitly nonphysical:

\[
(U_\varepsilon^{-1}HU_\varepsilon)_{hl}
=\frac{\varepsilon(-197+194\varepsilon)}{1-\varepsilon^2}<0
\quad(0<\varepsilon<1).
\]

There is no contradiction with the source's local isolation as a CTMC generator. The product factorization remains exact, but the inferred dynamics contains a negative off-diagonal rate.

Nor can one hold this ε fixed and pass from the finite factorizations to an infinite Hankel factorization. The third column of `XP^kUε` is the original third column minus ε times the sum of its first two columns. The singleton decays with eigenvalue `18/218`, faster than the two-state Perron mode `1−(9−2√6)/218`; this transformed column eventually becomes negative. Finite truncation and infinite-time positivity are different constraints.

**Executed algebra check.** At ε=1/100, Python `Fraction` arithmetic with the existing helpers verified strict X/Y positivity and all three displayed transformed-entry formulas; the hidden h→l rate was `−6502/3333`. This checks the algebra at one rational value, while the displayed formulas and continuity argument prove the finite-truncation statement. Run on 2026-09-10 before the 13:48 UTC checkpoint, with Python 3.9.12 and NumPy 2.0.1. Helper SHA-256 values were `1eb96cad1462049f19cbf32e301cb62e812a6ca663743577b0e5028579b48ab6` for [check_small_networks.py](../analysis/check_small_networks.py) and `4f5ba7179e1af63f2115fbfb6bf98d672d6e8105a4730e8ef58c873c2ab0368d` for [check_five_state_extensions.py](../analysis/check_five_state_extensions.py). Reproduce from the repository root:

```powershell
python -B -c "import sys; sys.path.insert(0,'analysis'); from fractions import Fraction as F; from check_small_networks import matrix; from check_five_state_extensions import theta,inverse; e=F(1,100); q=theta(100,100); u=matrix([[1,e,-e],[e,1,-e],[0,0,1]]); x=q[:2,2:]@u; y=inverse(u)@q[2:,:2]; h=inverse(u)@q[2:,2:]@u; assert all(t>0 for t in x.flat) and all(t>0 for t in y.flat); assert y[0,1]==e*(94-100*e)/(1-e*e); assert y[1,0]==e*(97-100*e)/(1-e*e); assert h[0,2]==e*(-197+194*e)/(1-e*e); print(h[0,2])"
```

## 4. Search and access limits

The two useful citation paths were exact-rank NMF rigidity → Mond–Smith–van Straten's triangle topology, and the existing positive-realization bibliography → results specifically mentioning third order. The latter again led to scalar realization conditions rather than a verified strict matrix theorem. Benvenuti–Farina–Anderson–De Bruyne, *Minimal Positive Realizations of Transfer Functions with Positive Real Poles*, [DOI](https://doi.org/10.1109/81.883332), explicitly restricts its formulation to SISO discrete time; its full introduction was readable in the [primary-paper text](https://www.researchgate.net/publication/2367933_Minimal_Positive_Realizations_of_Transfer_Functions_with_Positive_Real_Poles). Its detailed theorem and proof were not audited here, and no scalar-to-matrix extension is inferred.

No new concrete full-text route emerged for Förster–Nagy (2000); the earlier exact-hypothesis/order gap remains. Failed publisher routes were not repeated. The Mainz PDF was readable as full extracted text; several screenshot requests failed, so the numeric component bound was cross-checked against the explicit prose of Theorem 4.9 rather than uncertain OCR inequality signs. The arXiv rigidity preprint was fully accessible; journal version differences were not compared.

The source check therefore strengthens the prior-art constraint on local rigidity and disconnectedness, and eliminates an insufficient finite-Hankel shortcut. It does not certify novelty, prove existence of a strict order-three matrix realization, exclude connected hidden paths or triangles, or bound the theta(100,100) entropy range. A global proof must retain dynamical invariance, not only static triangle nesting.

## 5. Focused check against the proposed global cone exclusion

After the coordinator supplied a proposed global exclusion using Perron-normalized triangles, the flow `(−u,−κv)`, and two output-wedge inequalities, a further bounded search targeted irreducible third-order and matrix-valued positive realizations. The existing invariant-cone machinery supports the reduction. None of the inspected source results supplies the quantitative inequalities excluding this particular triangle; that claim requires its separate analytic proof. This is a scope distinction, not a novelty determination.

A potentially misleading title led to a limited new source check. Rafael Cantó, Beatriz Ricarte and Ana M. Urbano, *On Positive Realizations of Irreducible Transfer Matrices*, LNCIS 341, 41–48 (2006), [DOI](https://doi.org/10.1007/11757344_6), was available only through its [primary abstract](https://www.researchgate.net/publication/266718971_On_positive_realization_of_irreducible_transfer_matrices); the chapter route failed. It describes algebraic normality of a transfer matrix and a construction with A in Jordan form. The authors' [MAT-TRIAD 2007 abstract, pp. 60–61](https://homepages.tuni.fi/simo.puntanen/AbstractBook-MatTriad-2007-Bedlewo.pdf), inspected directly, confirms that their term “irreducible transfer matrix” concerns the polynomial numerator at denominator roots. It is not the hidden-graph irreducibility condition used here.

Their *Positive Realizations of Transfer Matrices With Real Poles*, IEEE Transactions on Circuits and Systems II 54(6), 517–521 (2007), [DOI](https://doi.org/10.1109/TCSII.2007.894408), has an accessible [primary abstract](https://www.researchgate.net/publication/3452697_Positive_Realizations_of_Transfer_Matrices_With_Real_Poles): it asserts minimal positive realization for second-order normal discrete-time transfer matrices with nonnegative impulse response and simple real poles, and extensions to some higher-order cases. The full theorem was not obtained. No general fixed-order-three, strict-matrix, connected-hidden exclusion, or uniqueness conclusion is inferred from either abstract.

These new access-limited leads are retained to prevent repeating the terminology mistake or overstating the completeness of the frontier review. They do not replace a full primary theorem comparison before publication.
