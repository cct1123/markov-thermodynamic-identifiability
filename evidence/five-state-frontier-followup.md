# Five-state frontier: finite alternatives, entropy bounds, and path reconstruction

Inspected 2026-09-10 UTC; checkpoint 06:13 UTC. Bounded follow-up to [the earlier realization notes](realization-frontier.md) and [entropy-range review](entropy-range-followup.md), under renewed D005/D006. Target: linear realization order five, a five-state cap, unknown bidirected topology, and the complete joint waiting kernels of one individually resolved observed pair x↔y. This source check does not establish a five-state classification or certify novelty. No source PDFs were saved locally and no numerical calculations were performed.

**Conclusion — inference.** Finite, isolated, nontrivial global alternatives are established in a restricted positive-realization family, so absence of local free parameters is inadequate evidence of global uniqueness. Those examples do not establish bounded non-singleton stationary entropy fibers in this repository's class. The inspected upper-bound theorem requires microscopic information beyond the observed kernels. The proposed path reconstruction uses established inverse-Jacobi machinery; the cap-dependent step forcing a path is a separate claim.

## Finite global alternatives: Coxian distributions

Jean Rizk, Kevin Burke and Cathal Walsh, *On the Non-uniqueness of Representations of Coxian Phase-Type Distributions*, [arXiv:1901.03849v2](https://arxiv.org/pdf/1901.03849v2), submitted version 23 July 2019. Full 20-page primary preprint inspected; journal publication not verified. Locators below are PDF pages.

**Primary results.** Theorem 1, p. 9, gives normalized invertible similarity for equivalent nonredundant PH representations. Corollary 1, pp. 10–11, specializes the transformation to lower triangular form for Coxian generators with nonzero superdiagonals and initial distribution e₁. Theorem 2, pp. 12–13, makes distinct equivalent Coxians differ in diagonal ordering; a fixed ordering admits at most one. Section 4, Algorithm 1, pp. 13–14, enumerates at most n! orders and checks feasible superdiagonals. Example 4/Table 2, pp. 14–15, has all six three-phase orders; Example 5, p. 15, has two. These are global alternatives within the Coxian family, not merely a local sensitivity calculation.

**Scope/inference.** Preserve nonredundancy. Coxian models are transient one-way chains with absorption, outside our bidirected stationary class. Exhausting their permutations does not exhaust all positive realizations. Directed acyclicity differs from an undirected tree of reversible edge pairs. No entropy-range result follows here.

## Forward check: resolved absorption causes do not remove the issue

Bo Henry Lindqvist, *Phase-type models for competing risks, with emphasis on identifiability issues*, Lifetime Data Analysis 29, 318–341 (2023), first published 8 February 2022; [DOI](https://doi.org/10.1007/s10985-022-09547-7), [full 24-page journal PDF](https://d-nb.info/1257579983/34). PDF pages are used because this copy does not consistently expose printed page numbers in extraction.

**Primary results and explicit attribution.** Section 2.1, PDF p. 5, defines nonredundancy by the reduced scalar Laplace-denominator degree. Theorem 4, section 3.2, PDF p. 12, gives equivalent competing-risk models through B1=1 and the simultaneous transformations pᵀ→pᵀB, Q→B⁻¹QB, L→B⁻¹L. It assumes that the unmarked PH model itself is nonredundant. Theorem 5, PDF pp. 12–13, extends uniqueness at fixed Coxian diagonal ordering to all cause-specific distributions, building on Rizk et al. Example 5, PDF p. 13, Eqs. (20)–(23), reproduces Lindqvist–Kjølen's 2018 two-phase, two-cause example: two distinct Coxian generators give identical subdensities 5e⁻⁴ᵗ−3e⁻⁵ᵗ and 3e⁻⁴ᵗ−2e⁻⁵ᵗ.

**Inference.** Exit marks alone need not restore uniqueness. One fixed entrance plus cause-resolved absorption is weaker than our two-reset 2×2 excursion kernel. The one-way transient example supplies no stationary detailed-balance comparison. Its repeated Coxian theorem is not independent confirmation of Rizk et al.

## Exact upper entropy bound and its missing hypothesis

Tomohiro Nishiyama and Yoshihiko Hasegawa, *Upper bound for entropy production in Markov processes*, Physical Review E 108, 044139 (2023); [DOI](https://doi.org/10.1103/PhysRevE.108.044139), [full arXiv:2306.15251v2](https://arxiv.org/pdf/2306.15251v2), version 6 October 2023. Full seven-page primary preprint inspected; publication metadata checked, version differences not compared.

**Primary result.** For a stationary finite CTMC with bidirectional support, section II A, p. 2, Eq. (8), bounds the entropy-production rate by

\[
\sigma\le a\log R\,\frac{R-1}{R+1},
\]

where a is total dynamical activity and R is the largest forward/reverse rate ratio over present edges. Appendix A, p. 5, proves the inequality. Section IV, p. 5, explicitly says partial observation prevents calculating R and hence direct application.

**Inference for this task.** A fixed minimal similarity orbit fixes Λ=−tr Q. Nonnegative rates give a≤Λ, but provide no uniform R bound. If the entire compatible class satisfies R≤R*, the theorem supplies a finite upper bound using Λ and R*. This is sufficient, not necessary: vanishing flux can compensate a divergent log ratio. Compact rate closure alone therefore does not answer the entropy question. This source gives no exact observational-fiber classification.

## Requested addendum: endpoint reconstruction is inverse-Jacobi theory

Fritz Gesztesy and Barry Simon, *m-Functions and inverse spectral analysis for finite and semi-infinite Jacobi matrices*, Journal d'Analyse Mathématique 73, 267–297 (1997); [DOI](https://doi.org/10.1007/BF02788147), [full author preprint](https://math.caltech.edu/papers/bsimon/p261.pdf). Full 29-page primary preprint inspected; following locators use its printed pages.

**Primary result.** For a real symmetric tridiagonal matrix with strictly positive offdiagonals, Theorem 3.5, p. 12 (=Theorem A.6, p. 23), identifies a unique N×N Jacobi matrix from its N-point endpoint spectral measure. Equation (2.15), p. 6, and Theorem 3.1, Eq. (3.1), p. 8, yield recursive recovery from the endpoint m-function. The explicit reconstruction steps (i)–(iii) are on p. 11. This is a finite-dimensional theorem, not just a semi-infinite analogy.

**Mapping — inference.** A killed bidirected path is diagonally similar to a symmetric Jacobi matrix. Diagonal endpoint resolvents are preserved; Jacobi offdiagonals are square roots of opposing-rate products. The theorem consequently recovers diagonal entries and those products. Known endpoint escape rates and CTMC row sums are additional inputs needed to split products into directed rates. The source does not prove that a derivative delay and cardinality cap force an unknown graph to be a path, or classify its entropy range.

## Remaining discriminant and access limits

**Inference.** A finite set of irreducible bidirected generators would have finite entropy values, but it must exhaust the full compatible class modulo hidden relabeling; different generators may still have identical entropy. Conversely, a continuous equivalence component can have bounded entropy. Thus neither generic similarity freedom nor a finite list inside one prescribed canonical form settles the requested five-state case. The consequential next step remains an exact global positive-realization analysis, including topology-changing alternatives, followed by an entropy comparison or a verified divergent-boundary argument.

The existing Larget (1998) full-text gap remains; no new concrete retrieval route was found, and previously failed routes were not repeated. A readable Ball (2011) [conference paper](https://2011.isiproceedings.org/papers/450279.pdf), sections 3.2–3.3, was checked as a citation bridge; its secondary references to canonical aggregate equivalence and an outlined result attributed to work then in preparation were not promoted to primary theorems here. It supplied no decisive entropy-range claim. The Lindqvist PMC route returned a challenge page; the national-library PDF above supplied the full text. The non-www Caltech PDF supplied Gesztesy–Simon after the www route failed. These are access outcomes, not evidence that inaccessible work lacks relevant results.

The bounded follow-up stops after the closest concrete finite-alternative family, its marked extension, the applicable upper-bound hypothesis, and the directly relevant inverse theorem. No matching bounded non-singleton five-state entropy theorem or example was obtained. That negative retrieval outcome leaves novelty unestablished.

## Focused addendum after the disconnected-fiber witness

Inspected 2026-09-10, approximately 06:25 UTC. The [theta audit](../analysis/theta-global-audit.md) subsequently established an isolated minimal five-state generator sharing its complete kernels with a distant open set of positive generators and an unbounded entropy family. This is stronger than finite ambiguity inside a prescribed Coxian form. It establishes disconnectedness of the generator fiber, not necessarily its entropy image.

**Retrieval outcome, not a primary theorem.** Two narrow query families were checked: connectivity/disconnectedness of positive realization sets, and isolated equivalent Markov/PH realizations coexisting with continuous families. No matching full primary result was obtained. Mostly irrelevant results and the already identified PH canonical-form literature were returned; their snippets do not support a novelty conclusion.

The concrete citation bridge was Commault–Mocanu, *Phase-type distributions and representations: Some results and open problems for system theory* (2003), [full PDF](https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/CommaultMocanu_forAssignment.pdf), section 4, pp. 571–573. Its Theorem 5, attributed to Cumani (1982), concerns conversion of triangular PH representations to ordered Coxian form. The discussion does not supply the required coexistence theorem. This is a secondary attribution and was not substituted for a primary read. The cited O'Cinneide (1989, 1991) originals were not retrieved anew in this bounded check. Their exact scope remains unverified here. No additional decisive source was added, and no novelty conclusion is drawn.
