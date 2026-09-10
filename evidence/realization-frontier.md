# Realization literature: supplementary source notes

Inspected 2026-09-10 UTC. [RECORDS.md](RECORDS.md) holds the findings and publication metadata. These notes preserve additional theorem hypotheses, locators, and access gaps. No source PDFs were saved locally. The project's observation map and specialized similarity proof are maintained in [formulation.md](../analysis/formulation.md) and [compatibility-orbit.md](../analysis/compatibility-orbit.md).

## Buchholz and Telek — E012

[Record](RECORDS.md#e012); *On minimal representations of Rational Arrival Processes*, inspected the author-uploaded 2011-09-15 preprint via [ResearchGate](https://www.researchgate.net/publication/227072004_On_minimal_representations_of_Rational_Arrival_Processes). Locators refer to that preprint.

Section 3, pp. 2–3, uses simultaneous similarity C_i=B^-1 D_i B with B1=1. Section 7, pp. 15–16, defines equivalence through every joint marked interarrival density. Theorem 7 gives sufficient conditions D_k V=V C_k for each k=0,...,K, V1=1, and nu V=phi, where nu and phi are stationary event-epoch vectors. Theorem 8 gives the reverse-direction rectangular intertwining. Section 4, Theorem 5, p. 9, characterizes rational minimality by generalized observability/controllability ranks; section 7.1 extends to marks.

The paper assumes a unique stationary event-epoch vector. Rational minimality need not equal minimum Markovian order, and arbitrary marks need not have single-edge support. The resolved-edge specialization is derived separately in this repository, not attributed as a theorem of this paper.

## Phase-type and positive realization — E011

[Record](RECORDS.md#e011). Horváth–Telek, *A Constructive Proof of the Phase-Type Characterization Theorem*: inspected [arXiv:1502.00521v1](https://arxiv.org/pdf/1502.00521), pp. 1–4, definitions 1–5, theorems 1 and 3, and the algorithm outline.

Theorem 3 concerns a normalized scalar matrix-exponential density without an atom at zero. Strict positivity for t>0 and a unique eigenvalue with maximal real part in its minimal ME representation characterize finite PH representability; that eigenvalue may have multiplicity greater than one. The characterization is credited to O'Cinneide (1990). Theorem 1 uses alpha W=gamma, AW=WG and W1=1 for possibly different-dimensional equivalence.

Commault–Mocanu, *Phase-type distributions and representations: Some results and open problems for system theory*: inspected [full PDF](https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/CommaultMocanu_forAssignment.pdf), section 3.2, Theorem 4, pp. 570–571. Its same-order/same-graph normalization gives A1+B=0 and, at unit DC gain, C1=1. Here irreducibility means each state lies on an input-output path; it means neither strong connectivity nor linear minimality. Prescribed microscopic boundary vectors are not automatically retained.

## Fredkin and Rice — E007

[Record](RECORDS.md#e007); [inspected NIST PDF](https://nvlpubs.nist.gov/nistpubs/jres/090/jresv90n6p517_A1b.pdf), pp. 518–520. The stationary aggregate model assumes diagonalizable within-aggregate subgenerators.

Theorem A bounds the dwell-density coefficient matrix rank by the interaggregate block rank. Theorem B, p. 519, reduces higher joint dwell laws to pair densities under distinct within-aggregate spectra and nonzero univariate exponential coefficients. Theorem C uses these ranks to bound identifiable parameter count.

Results are stated without proofs, referring to underlying work including the authors' *On aggregated Markov processes* (1986), J. Appl. Probab. 23, 208–214, whose full text was not obtained. “Equilibrium” in the 1985 prose denotes stationary operation; detailed balance is discussed separately.

## Wagner and Timmer — E008

[Record](RECORDS.md#e008); [inspected full author PDF](https://jeti.uni-freiburg.de/papers/detailed_balance_printed.pdf), pp. 2919–2920. “Criterion for non-identifiability” constructs topology-preserving local similarity families using the implicit-function theorem. “Testing for detailed balance,” p. 2920, gives the exact four-state equilibrium/nonequilibrium ambiguity. This is distinct from the finite-data power studies elsewhere in the paper.

## Siekmann — E010

[Record](RECORDS.md#e010); inspected [publisher HTML](https://link.springer.com/article/10.1007/s11538-025-01558-3) and [author PDF](https://researchonline.ljmu.ac.uk/id/eprint/27780/1/Modelling%20ion%20channels%20with%20a%20view%20towards%20identifiability.pdf), sections 3.4.1–3.4.4.

In section 3.4.2, Eqs. (52)–(55) use two free rates and four observed invariants for the three-state binary aggregate model. Fig. 7, pp. 25–26, distinguishes classes containing a detailed-balance curve from those with no equilibrium member. Section 3.4.3, Eq. (62), includes a one-way-edge boundary; nonnegative-rate restrictions affect existence of simpler representatives.

## Wu and Jia — E009

[Record](RECORDS.md#e009); inspected complete [arXiv:2406.19586v2](https://arxiv.org/html/2406.19586v2), dated 2024-12-13, including End Matter. Published main text and separate supplement were subscription-only; version differences remain unchecked.

The Model section's eigenvector normalization requires nonzero row sums, and coefficient extraction requires visible modes. Distinct within-cluster eigenvalues alone do not guarantee these conditions. Eqs. (2), (4)–(9) develop sufficient statistics; Eq. (10) imposes compatible-rate equations, whose unique solvability still needs to be established. Eqs. (12)–(13) are necessary equilibrium conditions; End Matter Appendix A proves a converse for three states and two clusters. Approximating a degenerate model does not settle its exact identifiability.

## Xiang and Deng — E022

[Record](RECORDS.md#e022); inspected the complete [2025 author-review PDF](https://www.sciengine.com/doi/pdfView/44DD49AD8BDD4325A8C525255E5CA50C). This is a primary-author account, not the original 2024 proof.

Section 3.1, p. 1535, defers the distinguishability definition to references 66 and 71. Theorems 3.1–3.3, p. 1540, report stationary reconstruction from all leaves and two adjacent observable states per cycle; the single-cycle result includes an iff statement. Definition 3.3, p. 1543, defines D-Markov chains by diagonalizability of every principal submatrix obtained by deleting one state. Section 3.6, pp. 1543–1544, assumes known topology and distinguishes separately observed states from pooled open-state data. It flags mathematical verification of topology-preserving similarity ambiguity for further work.

Those observations do not automatically follow from resolved-edge timestamps: a visit to an endpoint may occur without a recorded edge crossing.

## Limited-access originals and citation trails

- **Kienker (1989):** [DOI](https://doi.org/10.1098/rspb.1989.0024), [PubMed](https://pubmed.ncbi.nlm.nih.gov/2471201/). Abstract only. It describes similarities mixing equal-conductance states; a necessary-and-sufficient theorem was not verified from full text.
- **Larget (1998):** [DOI](https://doi.org/10.1239/jap/1032192850), [publisher abstract/references/citing list](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/canonical-representation-for-aggregated-markov-processes/D21B644D94227A9591ADE4D32708960E). Full text unavailable; exact regularity hypotheses for its canonical representation remain a gap. Backward references include Blackwell–Koopmans (1957), Gilbert (1959), Kienker (1989), Ito–Amari–Kobayashi (1992), and Rydén's continuous-time hidden-Markov work. Forward leads include the recent reconstruction and equilibrium-feasibility sources above. Citation leads are not inspected theorem evidence.
- **Xiang, Zhou, Deng and Yang (2024):** [DOI](https://doi.org/10.1063/5.0156458), [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/38386908/), [first-page publisher preview](https://www.researchgate.net/publication/378399352_Identifying_the_generator_matrix_of_a_stationary_Markov_chain_using_partially_observable_data). Full publisher retrieval failed; the original proof and deferred distinguishability condition remain unverified despite the later review.
- **Telek and Horváth (2007):** *A minimal representation of Markov arrival processes and a moments matching method*, Performance Evaluation 64, 1153–1168, [DOI](https://doi.org/10.1016/j.peva.2007.06.001). Indexed preprint/abstract only; CiteSeer PDF retrieval failed. It is a backward reference behind Buchholz–Telek's similarity discussion. Generic rank/moment claims were not imported into degenerate cases.

Current conclusions and the next research action are in [STATE.md](../STATE.md) and [the report](../outputs/REPORT.md).
