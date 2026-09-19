# Literature audit for the next theorem

2026-09-19 UTC. Bounded independent literature assignment. Labels below distinguish original-source results from reviewer inferences. This file neither certifies priority nor assigns shared evidence IDs. The review read `PROJECT.md`, the saved state, `manuscript/supplementary/observation-graph.tex`, and `analysis/revision/GRAPH-REGULARIZATION.md` before searching.

The strongest target is a sharp local entropy-ceiling classification for arbitrary reverse-closed resolved-edge observation sets, supported by an explicit inverse using a small number of positive Laplace evaluations. **Bare generator identifiability with one hidden vertex has close and consequential prior art.** The distinction between an exact inverse and a stable inverse from bounded measurements must carry the mathematical contribution.

## Closest original sources

### Burgarth: zero forcing for Markov generators

**Primary result.** Daniel K. Burgarth, *Identifying combinatorially symmetric Hidden Markov Models*, Electronic Journal of Linear Algebra **34**, 393–398 (2018), [journal landing page and DOI](https://journals.uwyo.edu/index.php/ela/article/view/1899), DOI 10.13001/1081-3810.3651; [directly read preprint](https://arxiv.org/pdf/1709.02932), arXiv:1709.02932v1. Retrieved 2026-09-19. Precise locators: Sec. 2 Definitions 1–3; Sec. 3 Lemma 2; Sec. 5 Eq. (18) and Theorem 2, preprint pp. 6–7. Theorem 2 states CTMC identification when observed vertices form a zero-forcing set. Its data are the restricted ordinary semigroup at all times; derivatives supply generator powers. The proof uses normalization to recover the transition to a uniquely hidden neighbor and then propagates matrix entries. No statistical-efficiency claim accompanies the theorem.

**Access/version limitation.** The full preprint was read. The journal PDF returned cache/fetch errors, so the final theorem text was not verified against the journal version. Journal metadata reports 2018; the arXiv record has one 2017 submission, while the delivered PDF has a 2021 generated date. The preprint's CTMC sign sentence is inconsistent with its displayed semigroup; use the repository's standard generator convention when adapting the argument.

### van Waarde–Tesi–Camlibel: graph-constrained linear system identification

**Primary result.** H. J. van Waarde, P. Tesi and M. K. Camlibel, *Identifiability of Undirected Dynamical Networks: A Graph-Theoretic Approach*, IEEE Control Systems Letters **2**(4), 683–688 (2018), [DOI](https://doi.org/10.1109/LCSYS.2018.2846630); [directly read university-hosted publisher PDF](https://pure.rug.nl/ws/portalfiles/portal/64490085/08382192_1_.pdf). Retrieved 2026-09-19. Locators: Sec. II.A definitions of Q(G), Qp(G); Sec. II.C–D transfer matrix and identifiability; Sec. IV Theorems 1–2 and Remark 4, pp. 685–687. Known undirected graph, symmetric state matrix and positive supported off-diagonals are explicit assumptions. A zero-forcing intersection of input/output vertices suffices for identification. Remark 4 constructs a hidden diagonal-scaling ambiguity after relaxing symmetry. The source also distinguishes identifiability from a reconstruction algorithm and says the zero-forcing condition is sufficient, not necessary.

**Inference.** This is adjacent foundational work, but symmetry of the numerical weights is stronger than reciprocal support. Its hidden-scaling counterexample need not preserve generator row sums. Neither its positive nor negative theorem should be copied into this manuscript without those constraints being checked. No source copy was redistributed.

### Maier–Seifert–van der Meer: the same resolved-transition experiment

**Primary result.** A. M. Maier, U. Seifert and J. van der Meer, *From observed transitions to hidden paths in Markov networks*, Physical Review Research **7**, 033067 (2025), [DOI](https://doi.org/10.1103/p4k1-1dvb); [directly read preprint v1](https://arxiv.org/html/2504.16015v1), 22 April 2025. Retrieved 2026-09-19. Locators: Sec. III Eq. (4), Sec. VI introductory definition and VI.1–VI.4, Sec. VII, Appendix B. The paper extracts path entropy and shortest/second-shortest path information from transition waiting laws. Its minimal graph consists of what these tools can reconstruct; the algorithm can branch into several graph candidates. Sec. VI explicitly permits certain hidden additions without contradicting the extracted topological information. A worked example recovers a six-state graph from two observed reverse pairs.

**Inference.** “Network reconstruction from few visible edges” would be an inadequate novelty claim. The proposed result should instead specify physical-generator recovery from finitely many absolute transform matrices, its state/support class, and the local entropy-ceiling consequence. Matching extracted path lengths is weaker than matching all-time waiting matrices. Only v1 was represented as read.

### Ehrich: compatible entropy sets and growing maxima

**Primary result.** J. Ehrich, *Tightest bound on hidden entropy production from partially observed dynamics*, J. Stat. Mech. **2021**, 083214, [DOI](https://doi.org/10.1088/1742-5468/ac150e); [directly read original preprint](https://arxiv.org/pdf/2105.08803). Retrieved 2026-09-19. Locators: Sec. 4 Eqs. (39)–(48), Sec. 4.1 and Fig. 8, discussion pp. 17–18 in the delivered 22-page PDF. For a masked discrete-time chain with two visible and two hidden states, fixed count and unknown zero pattern, the paper parameterizes compatible models using invertible jump-probability matrices. The full observed jump law follows from the first nontrivial matrices under those invertibility conditions. It reports that progressively finer parameter grids produce apparently unbounded entropy maxima and identifies the nearly irreversible-edge mechanism. The discussion anticipates analogous continuous-time results.

**Inference.** Compatible-model fitting, entropy nonuniqueness and the suggested divergence mechanism are established antecedents. A universal all-source local classification and an exact divergent family have a stronger mathematical status than the numerical upper-range observation; cite the observation rather than presenting the mechanism as newly discovered. No source calculation was rerun in this assignment.

### Nishiyama–Hasegawa: upper bounds require microscopic controls

**Primary result.** T. Nishiyama and Y. Hasegawa, *Upper bound for entropy production in Markov processes*, Physical Review E **108**, 044139 (2023), [directly read publisher full text](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevE.108.044139/fulltext), [DOI](https://doi.org/10.1103/PhysRevE.108.044139). Retrieved 2026-09-19. Locators: Sec. II Eqs. (5)–(8) and Appendix A. With microscopic stationary activity K and maximum supported rate ratio R, the upper bound is sigma <= K log(R)(R-1)/(R+1). The paper gives a driven-cycle equality example. Its inputs constrain microscopic activity and rate asymmetry.

**Inference.** This is an essential complementary upper-bound result. A local ceiling inferred solely from the resolved waiting laws and a dimension restriction has different premises. Observed-event activity must not be substituted for all microscopic jump activity.

### Finite-frequency realization: an unresolved detailed comparison

**Primary abstract only.** A. J. Mayo and A. C. Antoulas, *A framework for the solution of the generalized realization problem*, Linear Algebra and its Applications **425**, 634–662 (2007), [DOI](https://doi.org/10.1016/j.laa.2007.03.008). Publisher search metadata/abstract describes constructing generalized state-space realizations of tangential interpolation data using Loewner and shifted Loewner matrices. The full publisher page returned 403. A 2006 primary conference precursor, [*New Results on Interpolation and Model Reduction*](https://mathweb.ucsd.edu/~helton/MTNSHISTORY/CONTENTS/2006KYOTO/CONFERENCEWEBSITE/papers/0402.pdf), was found but its full-text fetch timed out. Retrieved/attempted 2026-09-19.

**Inference / access limit.** Finite transform-data realization is a mature adjacent framework. This abstract-level access cannot establish a precise overlap with a two-/three-point physical CTMC inverse. Keep the detailed priority comparison open; do not label a finite-sample-count theorem new merely because this bounded search did not locate it.

## Exact observation-model comparison

The following is reviewer algebra, not an attributed theorem or an executed numerical check. It explains why the Burgarth source materially changes the novelty assessment.

Let C be the covered vertices. Choose one incoming and one outgoing mark at each i in C, and write the selected time kernel as F(t)=(exp(Tt))_CC D, with D the selected positive outgoing-rate diagonal. Complete exact waiting laws determine the analytic density and thus F(0)=D; all other observed rates are likewise determined at their origin rows. This zero-time operation is an exact-data statement and **is not continuous in TV**.

Set U(lambda)=Fhat(lambda)D^-1=((lambda I-T)^-1)_CC. Every observed edge is inside C, so E is supported on C x C. The resolvent identity for Q=T+E gives

    Z(lambda)=((lambda I-Q)^-1)_CC
             = (U(lambda)^-1-E_CC)^-1.

Thus complete waiting laws determine the restricted ordinary semigroup. If C=V\{h}, write A=Q_CC and x=Q_Ch. Row normalization yields x=-A 1. Irreducibility supplies i with x_i>0. The second generator-power block gives

    Q_hC = ((Q^2)_iC-(A^2)_iC)/x_i,
    q_hh = -Q_hC 1.

Consequently one-hidden-state exact recovery is elementary once restricted semigroup data are available. Also, C is automatically zero forcing on any connected support, so this case lies at the heart of Burgarth's mechanism. This argument does not rely on a complete source and does not provide the bounded positive-Laplace inverse, its conditioning, or entropy continuity across changing supports.

## Recommended target and research-loop exit criteria

**Theorem target, not established by this literature assignment:** on a fixed labeled microscopic vertex set and an arbitrary nonempty reverse-closed resolved-edge observation set, classify the existence of a finite local upper entropy ceiling in the unknown reciprocal-support class. The candidate criterion to challenge is: the source is complete and at most one vertex is uncovered. The root investigator is deriving and checking that statement independently; this file does not promote it to a proved result.

The useful chain of work is:

1. Prove a rational inverse from a fixed small number of positive Laplace matrices when exactly one vertex is uncovered. State whether arguments are arbitrary distinct positives or adaptively selected, whether rates are calibrated, and whether the full matrix is required. Show denominator exclusions on every admissible support, including a hidden leaf.
2. Turn that inverse into local generator continuity in weak row-law and TV topologies without a common rate cap. A proof using only density derivatives at zero misses this requirement.
3. Use positive complete support to obtain an entropy ceiling. Attack every sparse source by opening a missing unobserved reverse pair asymmetrically and retaining irreducibility; distinguish fixed trace and free trace. For two or more uncovered vertices, reuse the accepted hidden-shear construction with the multi-mark hypothesis checked.
4. Test exceptional strata before adopting the statement: hidden degree one, disconnected observed graph, many marks sharing origins/destinations, redundant marks, paired-zero boundaries, and a rate sequence escaping to infinity. Use exact all-time checks for any candidate nonidentifiability example.
5. Present the sharp local classification as the main advance, and the small finite-data inverse as the mechanism. Credit zero forcing and compatible entropy-set analysis. Retain the five-state exact fiber as a separate phenomenon rather than claiming the graph result classifies exact fibers in higher hidden dimension.

An independent proof route should exploit generator normalization or Schur complements, not merely rerun the same reconstruction implementation. The most valuable attempted falsification is a sequence with matching/convergent bounded Laplace data and either nonconvergent rates or divergent entropy at a proposed positive source. A failed search is inconclusive; proof must close noncompact escape directions and all denominator strata.

## Search coverage and remaining uncertainty

Queries covered Markov zero forcing and inverse generators, boundary/partial-state recovery, transition-based waiting-law graph reconstruction, compatible entropy ranges, upper entropy bounds, and finite Laplace/Loewner realization. Primary originals were read for the five principal comparisons above. The audit found a concrete omitted predecessor that narrows the reconstruction novelty claim; it did not establish literature-wide priority for the proposed ceiling classification. A close fixed-frequency theorem or an existing sharp local classification could still change the assessment. No external contacts, uploads, source-code reruns or mathematical proof certifications were performed.

## Follow-up: complete-source exact-fiber dichotomy

The coordinating investigator requested a targeted second comparison for the stronger candidate: **at every complete source, at most one uncovered vertex gives generator uniqueness; at least two uncovered vertices give an unbounded exact entropy fiber at the same state count, even without minimality, preserving every observed rate and the trace.** This statement concerns the source's complete support; individual competitors need only satisfy the declared reciprocal-support class unless the proof establishes completeness throughout the finite-parameter family. The source distinction must stay visible.

### Additional primary reads

**Primary result.** M. Wagner and J. Timmer, *The Effects of Non-Identifiability on Testing for Detailed Balance in Aggregated Markov Models for Ion-Channel Gating*, Biophysical Journal **79**, 2918–2924 (2000), [DOI](https://doi.org/10.1016/S0006-3495(00)76529-5); [directly read author-hosted journal PDF](https://jeti.uni-freiburg.de/papers/detailed_balance_printed.pdf). Retrieved 2026-09-19. Locators: pp. 2919–2920, “Criterion for non-identifiability,” Eqs. (1)–(2), and “Testing for detailed balance.” The paper uses normalized block similarities preserving the aggregate open/closed process. Equal dwell times in its four-state loop allow continuous indistinguishable families, including an equilibrium model and models violating detailed balance. Supported zeros impose additional constraints on those transformations.

**Inference.** Exact hidden thermodynamic ambiguity is established decades earlier. The observed variable is binary state aggregation, not the present known microscopic reset marks. The source's local nonidentifiability argument neither proves a universal complete-source statement nor proves unbounded stationary entropy within every such source's exact fixed-dimensional fiber.

**Primary result.** B. Vanluyten, J. C. Willems and B. De Moor, *Equivalence of state representations for hidden Markov models*, Systems & Control Letters **57**, 410–419 (2008), [DOI](https://doi.org/10.1016/j.sysconle.2007.10.004); [directly read author-hosted publisher PDF](https://homes.esat.kuleuven.be/~sistawww/smc/jwillems/Articles/JournalArticles/2008.3.pdf). Retrieved 2026-09-19. Locators: Proposition 2, Theorem 2 and Proposition 3, pp. 414–415. Proposition 2 characterizes equivalent positive Mealy representations of the same order using a nonsingular normalization-preserving simultaneous similarity, assuming quasi-Mealy minimality. Theorem 2 gives semialgebraicity. Proposition 3 treats the more general relation between positive-minimal and quasi-minimal representations. Stationarity preservation is explicitly discussed.

**Inference.** The algebraic equivalence mechanism is prior art. The source does not give an entropy functional, an irreversible limiting family, or the observation-coverage threshold. A proof not requiring minimality avoids a consequential limitation of directly applying Proposition 2.

**Primary result.** S. Zeraati, F. H. Jafarpour and H. Hinrichsen, *Entropy production of nonequilibrium steady states with irreversible transitions*, J. Stat. Mech. **2012**, L12001, [DOI](https://doi.org/10.1088/1742-5468/2012/12/L12001); [directly read preprint with supplemental material](https://arxiv.org/pdf/1211.4701). Retrieved 2026-09-19. Locators: opening discussion and supplement “The problem of infinite entropy production,” printed supplemental pp. 6–7 (PDF pp. 15–16), Eqs. (17)–(18). The source explains the logarithmic entropy singularity when a positive forward rate has a vanishing reverse rate and discusses finite observation time and small positive microscopic reverse rates.

**Inference.** The divergence mechanism itself is established. The difficult extra requirement here is preserving exactly the entire observed law and a fixed state count while reaching that singular boundary. This source does not supply that construction.

### Assessment of the stronger target

**Inference from these inspected sources:** the sharpened complete-source dichotomy is the better potential headline than another isolated example of hidden dissipation. Its value lies in simultaneous universal quantification over source rates and observation sets, exact-law preservation, fixed microscopic count, and inclusion of nonminimal sources. No matching theorem was found in these directly read close sources. That is a bounded comparison, not a priority certificate.

The two-hidden-vertex proof must cover two distinct strata. Unequal external exit rows may use the accepted normalized shear; its continuation must reach a one-way boundary with a nonvanishing limiting opposing flux while keeping other rates physical. Equal external exit rows permit collapsing the pair. Varying their internal rates at fixed sum leaves the collapsed generator fixed; to conclude exact marked-law preservation, all resolved marks must lie outside the pair and the collapsing map must intertwine the killed generator and each reset/output map. Positivity of limiting occupancy follows if the remaining external connections keep the limiting generator irreducible. Merely noting that “lumping is possible” is insufficient without these observation identities.

This follow-up added three targeted original reads and a bounded search for exact hidden-dissipation/unboundedness antecedents. General state-extension examples do not settle the stated fixed-N theorem. Burgarth remains the closest precursor to the positive half; Ehrich remains the closest upper-entropy-range comparison to the negative half. A final manuscript should give those specific comparisons alongside the new theorem rather than use first-of-its-kind language.
