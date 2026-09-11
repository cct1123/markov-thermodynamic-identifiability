# Finite invariant-realization fibers: focused prior-art audit

Checkpoint: 2026-09-10 UTC; updated after the coordinator's PDF rendering check. Bounded independent literature assignment, following the [balanced endpoint theorem](../analysis/theta-balanced-boundary.md) and [earlier cone frontier](three-state-cone-frontier.md). No scientific scripts, accepted outputs, evidence IDs, state or report were changed. Online sources below were retrieved on 2026-09-10; this worker saved no source copies. The coordinator later downloaded and rendered the Mond source to resolve an OCR ambiguity.

**Conclusion — inference.** Finite disconnected rank-minimal nonnegative factorization spaces are established precedent. A simple exact lift also gives finite disconnected minimal continuous-time positive-realization fibers, so **mere finiteness of a positive-realization fiber is not a defensible novelty claim**. The inspected sources neither contradict nor subsume the repository's narrower result: exactly two irreducible simple bidirected CTMC generators under an unknown-topology five-state cap, one resolved observed pair, three hidden modes, and rigorously different finite entropy rates.

The strongest apparently matching CTMC statement found was Siekmann's reference to a finite number of equivalent models. Reading its actual example shows that its two reduced identifiable topologies sit inside a continuous equivalence class. It is not a proof that the unrestricted same-order fiber is finite. Publication novelty remains unestablished.

## 1. The most direct finite-fiber precedent

**Primary result.** David Mond, Jim Smith and Duco van Straten, *Stochastic factorizations, sandwiched simplices and the topology of the space of explanations*, Proceedings of the Royal Society A 459, 2821–2845 (2003), [DOI](https://doi.org/10.1098/rspa.2003.1150), [author-hosted journal PDF](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/30.Stochastic%20factorizations,%20sandwiched%20simplices%20and%20the%20topology%20of%20the%20space%20of%20explanations%20-%202003.pdf).

Theorem 2.4/Corollary 2.5 identify rank-size stochastic factorizations with intermediate simplices modulo component permutations. A consequential OCR ambiguity was resolved visually: Section 5, printed p. 2842, explicitly says the eight Figure 13 triangles are isolated in the **full space** `Delta(V,W)`, without a boundary symbol. Theorem 4.9 bounds components of the smaller **boundary-vertex space** `Delta(V,boundary W)` by `p+q`. Section 3 supplies a deformation retraction from the full space to that smaller space, so component counts agree. Thus eight isolated full-space points and at most eight components exhaust the full fiber; it is not merely eight contractible components of unspecified cardinality.

The squares have side ratio `sqrt(2)-1`; the associated matrix has rank three. The coordinator downloaded/rendered the PDF after web screenshots failed; this worker independently inspected the rendered p. 2842. **Inference:** finite alternatives and tangency mechanisms are prior art, while theta's dynamical invariance is additional. The published count is accepted source evidence, not an independently reconstructed geometric enumeration.

## 2. A precise static-to-continuous corollary

**Agent mathematical deduction; conventionally proved below, conditional only on the cited factorization count.** Let `M>=0` have ordinary rank `r`, admit size-`r` nonnegative factorizations, and satisfy `M 1=1`. Fix a finite `lambda>0`. Consider

\[
G(s)=\frac{M}{s+\lambda}.
\]

Its minimal continuous-time positive realizations of order `r`, counted modulo **positive diagonal state scalings and state permutations**, are in bijection with size-`r` nonnegative factorizations of `M` modulo the same scalings/permutations.

**Proof.** For `M=XY`, both factors have full rank `r`. The realization

\[
H=-\lambda I_r,\qquad C=X,\qquad B=Y
\]

is nonnegative in the usual positive-systems sense: `H` is Metzler and `C,B>=0`. Its controllability matrix has the same rank as `Y`, and its observability matrix has the same rank as `X`, so it is an ordinary minimal order-`r` realization. Every other order-`r` realization is related by an invertible real similarity. A scalar matrix is unchanged by any such similarity, so its state matrix must also be `-lambda I_r`. Equality of the transfer is then exactly `C B=M`; there are no extra dynamical degrees of freedom.

To remove positive diagonal scaling uniquely, put `d=Y1`. Every `d_i>0` because `Y` has no zero row. With `D=diag(d)`, the normalized factors `X D` and `D^{-1}Y` both have row sums one: the second by definition and the first since `M1=1`. This normalization is unique on each positive-diagonal orbit. The remaining quotient is permutation, exactly the stochastic-factorization quotient used by Mond–Smith–van Straten. Their eight-point rank-three example therefore supplies an eight-point **minimal continuous-time positive-realization** fiber under this quotient. Under the much coarser quotient by arbitrary real similarities, every minimal linear realization is equivalent and this counting statement would be meaningless.

**Consequential limits.** “Positive” here allows zeros and is not “all rates strictly positive.” This corollary alone is not an irreducible bidirected CTMC or an entropy example. A CTMC embedding must additionally enforce reciprocal visible incidence, row normalization within a full generator, the observation/reset geometry and finite distinct entropy. In particular, if the input/output transfer is `2 x 2`, then `rank M<=2`; the scalar-dynamics construction cannot have minimal hidden dimension three. It therefore cannot reproduce the theta endpoint's minimal five-state marked kernel. The cited rank-three example uses more ports. These are mathematical restrictions, not missing numerical searches.

## 3. Stronger general topology results do not supply the missing physical conditions

**Primary result.** Yaroslav Shitov, *A universality theorem for nonnegative matrix factorizations*, inspected [arXiv:1606.09068v2](https://arxiv.org/pdf/1606.09068v2), 5 April 2018, Section 2, PDF page 3. Its Universality Theorem constructs a matrix and factorization size whose factorization space is strongly equivalent to the zero locus of a polynomial intersected with the unit cube. The definition immediately preceding it uses unique rational lifts and coordinate permutations. Sections 3–4 give the construction.

**Inference and limitation.** Thus complicated, including finite, NMF topology is far from a new possibility. The inspected theorem does not promise `factorization size = ordinary rank`, fix that size to three, impose a prescribed semigroup, or enforce CTMC reciprocity. Its general statement must not be substituted for the rank-minimal hypothesis in Section 2. This is a new bounded citation angle through universality, not a new general classification attempted here. Journal-version differences were not compared.

**Primary result.** Robert Krone and Kaie Kubjas, *Uniqueness of nonnegative matrix factorizations by rigidity theory*, SIAM Journal on Matrix Analysis and Applications 42(1), 134–164 (2021), [DOI](https://doi.org/10.1137/19M1279472); inspected [arXiv v3](https://arxiv.org/pdf/1902.02868v3), 2 September 2020. Example 4.3, preprint page 11, explicitly connects rank-three boundary factorizations to isolated nested triangles. Proposition 4.2 gives infinitesimal implies local rigidity. Corollary 4.7, page 12, makes a locally rigid factorization globally rigid by adding up to `r` positive rows and columns.

**Inference.** The latter is not a theorem that the original observation fiber is unique: its construction adds constraints/ports. The repository keeps the two visible endpoints and their complete marked kernel fixed. Moreover, the earlier finite-Hankel counterexample already shows why static NMF rigidity need not decide theta's dynamical cone feasibility. No contradiction was found by applying the actual quantifiers.

## 4. The misleadingly close finite-CTMC statement

**Primary result.** Ivo Siekmann, *Modelling ion channels with a view towards identifiability*, Bulletin of Mathematical Biology 88, article 2 (2026), published online 9 December 2025, [DOI/full HTML](https://doi.org/10.1007/s11538-025-01558-3), [institutional author PDF](https://researchonline.ljmu.ac.uk/id/eprint/27780/1/Modelling%20ion%20channels%20with%20a%20view%20towards%20identifiability.pdf). The introduction, PDF page 4 of 37, refers to an equivalence class containing a finite number of models after restricting attention to parameter-identifiable reduced structures. Sections 3.4.2–3.4.4, PDF pages 22–25, instead describe the encompassing three-state class through two free rates: Eqs. (52)–(55) parameterize it continuously. COC and CCO are distinct reduced representatives. Eq. (62) additionally retains a continuous one-way-edge boundary.

**Inference.** This is serious precedent for topology ambiguity, but its “finite” introductory wording does not exhaust the unrestricted nonnegative or bidirected same-order fiber. Its observation is binary open/closed aggregation, not this repository's resolved-edge reset kernel. The two acyclic reduced models are not evidence of different entropy. This targeted reread rejects a possible overclaim of direct precedence without denying the established continuous ambiguity. The PMC route returned a browser check; publisher HTML and the institutional PDF supplied the underlying text.

## 5. Continuous-time cone theorem and remaining access limits

**Primary result.** J. M. van den Hof, *Realization of continuous-time positive linear systems*, Systems & Control Letters 31, 243–253 (1997), [DOI](https://doi.org/10.1016/S0167-6911(97)00049-2), [full CWI PDF](https://ir.cwi.nl/pub/127/0127D.pdf). Theorem 3.1, printed pp. 246–247, requires nonnegative shifted Markov parameters and a backward-shift-invariant polyhedral cone. Theorem 4.2, pp. 247–248, relates positive minimality to all admissible shifts. The proof allows the order dictated by the cone generators. Definition 2.3's discussion, p. 245, identifies monomial matrices as the orthant-preserving invertible maps with orthant-preserving inverses.

**Inference.** This supports the correct dynamical condition and the scaling/permutation quotient; it neither forces a continuum of cones nor prohibits a finite invariant-triangle fiber. It does not establish a strict three-ray cone merely from positive external response. The scalar lift in Section 2 makes all cones invariant automatically; theta's unequal hidden decay rates are the substantive extra restriction.

The full theorem of Förster–Nagy (2000) remains the [previously recorded access gap](positive-realization-frontier.md); failed retrieval routes were not repeated. A focused search also surfaced *Minimal positive continuous-time realizations of positive response maps* (2019), [publisher entry](https://www.sciencedirect.com/science/article/abs/pii/S0167691119300921). Its accessible snippet describes **nonlinear local analytic** response-map realizations. The page failed to open; no uniqueness theorem from it is treated as evidence. Original Larget/Kienker/Rydén hypothesis gaps remain as recorded in [realization-frontier.md](realization-frontier.md). No new claim about those inaccessible originals is made.

## Search boundary, stopping rationale and next implication

The new angles were finite/countable realization fibers, the exact “finite number of models” CTMC wording, NMF universality, and lifting finite **rank-minimal** static fibers to continuous dynamics. Searches combining “positive realization,” “finitely many,” “isolated,” and “invariant cone” produced mostly irrelevant material; no absence conclusion is drawn. Accessible primary sources listed above were read at the specified theorem/example passages. This was not an exhaustive literature review.

The useful consequence is already concrete: frame the potential contribution around the **small fixed physical class and entropy separation**, not finite positive realizations or isolated triangle alternatives in general. The unclosed question is whether an earlier theorem/exact example has the same combination of resolved observation, bidirected reciprocity, fixed minimal order and finite non-singleton entropy. More untargeted searches would add little; comparison to a specifically identified physical theorem is the discriminating next step. No inspected result contradicts the exact theta endpoint, and failure to locate one is not evidence of novelty.
