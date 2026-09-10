# Evidence and decision records

Recorded and retrieved **2026-09-10 UTC**, unless stated otherwise. Primary findings below are source-reported, not independently replicated. Agent deductions and executed calculations are separately labeled. The two [thermodynamic](hidden-entropy-frontier.md) and [realization](realization-frontier.md) memos preserve additional locators, citation trails, and access limitations. No downloaded source archive is claimed.

## E001

**Resolved-edge waiting kernels, entropy bounds, and hidden lumping**

- Kind: primary result; inference separately identified.
- Source: J. van der Meer, B. Ertel and U. Seifert, *Thermodynamic Inference in Partially Accessible Markov Networks: A Unifying Perspective from Transition-Based Waiting Time Distributions*, Physical Review X 12, 031025 (2022), [DOI](https://doi.org/10.1103/PhysRevX.12.031025); [inspected arXiv HTML v2](https://arxiv.org/html/2203.12020v2).
- Locators/access: full relevant text, Eq. (3), sections III, IV.3, V.2, VI, appendices A.3, D and E.5.
- Finding: the joint next-transition/time kernel has an absorbing-process representation; its entropy estimator lower-bounds microscopic production and is exact in specified structures, including sufficiently observed unicycles. Constant waiting-time ratios alone do not exclude hidden nonequilibrium. Appendix E.5 gives a hidden-state lumping example.
- Inference/limits: saturation under a true-network assumption is not uniqueness across a larger compatibility class. The appendix motivates E018, but its displayed changing entrance rate also changes aggregate dynamics; it is not itself our fixed-kernel parameter family.

## E002

**Boundary kinetics are already recoverable**

- Kind: primary result.
- Source: A. M. Maier, J. Degünther, J. van der Meer and U. Seifert, *Inferring Kinetics and Entropy Production from Observable Transitions in Partially Accessible, Periodically Driven Markov Networks*, Journal of Statistical Physics 191, 104 (2024), [DOI/full text](https://doi.org/10.1007/s10955-024-03315-7).
- Locators/access: section 3, Eqs. (11)–(14), inspected publisher text.
- Finding: short-time transition-conditioned densities identify observed rates; event frequencies and rates yield stationary probabilities at observed endpoints. The paper treats periodic stationary driving and, as a special case, time-independent steady states; it does not require detailed balance for these identities.
- Bearing/limit: taking the zero-time limit to recover observed rates is infrastructure, not a novelty claim. E017 separately derives recovery of the entire generator for the specific one-edge, at-most-three-state class.

## E003

**Path and minimal-network reconstruction is substantial prior art**

- Kind: primary result; inference.
- Source: A. M. Maier, U. Seifert and J. van der Meer, *From observed transitions to hidden paths in Markov networks*, Physical Review Research 7, 033067 (2025), [DOI](https://doi.org/10.1103/p4k1-1dvb); [inspected preprint v1](https://arxiv.org/html/2504.16015v1).
- Locators/access: sections III–VI, VII.2–VII.4 and VIII; full relevant HTML.
- Finding: waiting-time information constrains path entropy and hidden path lengths under specified conditions; their reconstruction procedure produces candidate minimal networks and can branch.
- Limit: a reconstruction based on selected inferred properties is not an exhaustive characterization of every generator sharing the full matrix-valued kernel. Their graph-minimality criterion differs from controllable/observable linear-realization minimality.
- Bearing: hidden topology or path inference in general is already occupied territory.

## E004

**Compatible-model entropy optimization and four-state ambiguity predate this project**

- Kind: primary result; inference.
- Source: J. Ehrich, *Tightest bound on hidden entropy production from partially observed dynamics*, Journal of Statistical Mechanics (2021), 083214; [inspected full arXiv v2](https://arxiv.org/html/2105.08803v2).
- Locators: section 4, Eqs. (39)–(49), Fig. 8; section 5.
- Finding: for a discrete-time masked Markov chain with two visible and two hidden states of known count, matrix factorization reconstructs families compatible with all masked jump probabilities. Entropy is optimized over physical rates. Fig. 8 numerically displays broad entropy variation and apparently unbounded maxima near one-way boundaries.
- Limits: this is a different observation/time model; the numerical appearance of divergence is not a general rigorous upper-range theorem. Section 5 explicitly discusses unresolved effects of extra hidden states.
- Inference: “optimize entropy over compatible hidden models” and four-state ambiguity are not new project concepts. A resolved-edge CTMC result needs additional exact scope and conclusions.

## E005

**Optimal lower bounds already quantify over compatible microscopic models**

- Kind: primary result.
- Sources: D. J. Skinner and J. Dunkel, *Improved bounds on entropy production in living systems*, PNAS 118, e2024300118 (2021), [full author PDF](https://math.mit.edu/~dunkel/Papers/2021SkDu_PNAS.pdf); *Estimating Entropy Production from Waiting Time Distributions*, Physical Review Letters 127, 198101 (2021), [DOI](https://doi.org/10.1103/PhysRevLett.127.198101), [full author PDF](https://math.mit.edu/~dunkel/Papers/2021SkDu_PRL.pdf).
- Locators/access: PNAS Eq. (2) and canonical reductions; PRL Eqs. (3)–(4), inspected main texts.
- Finding: the formal minimum ranges over models reproducing selected data. Practical results use one-/two-step counts or dwell-time moments. The PRL full-distribution formulation uses binary-metastate dwell densities.
- Limit: selected counts, moments and unconditional metastate dwells are not the full resolved next-edge/time kernel. Minimum entropy does not determine its supremum or whether the full compatibility fiber is a singleton in entropy.

## E006

**Waiting-time fitting to assumed hidden topologies is established**

- Kind: primary result.
- Source: E. Nitzan, A. Ghosal and G. Bisker, *Universal bounds on entropy production inferred from observed statistics*, Physical Review Research 5, 043251 (2023), [DOI](https://doi.org/10.1103/PhysRevResearch.5.043251); [inspected preprint v1](https://arxiv.org/pdf/2212.01783v1).
- Locators/access: Eq. (16), Eqs. (17)–(19), section IV and examples; full relevant PDF.
- Finding: optimization fits conditional dwell information together with stationary probabilities and fluxes on assumed network structures; moments furnish a practical implementation.
- Limit: numerical optimization does not certify a global entropy range for every topology or state count. The paper discusses the role of topological assumptions. Its results should not be characterized as failing to answer a different data model.
- Bearing: distinguish fixed-topology inference from an unrestricted compatible-model class.

## E007

**Classical aggregated-Markov equivalence is an essential novelty constraint**

- Kind: primary-author account; abstract-only statements as labeled.
- Sources: D. R. Fredkin and J. A. Rice, *Aggregated Markov processes and channel gating kinetics*, J. Res. NBS 90 (1985), 517–520, [full PDF](https://nvlpubs.nist.gov/nistpubs/jres/090/jresv90n6p517_A1b.pdf); P. Kienker, *Equivalence of aggregated Markov models of ion-channel gating* (1989), [DOI](https://doi.org/10.1098/rspb.1989.0024); B. Larget, *A canonical representation for aggregated Markov processes* (1998), [DOI](https://doi.org/10.1239/jap/1032192850).
- Locators/access: Fredkin–Rice pp. 518–520, especially Theorem B: pair dwell densities determine higher joint densities under distinct within-aggregate spectra and nonzero exponential coefficients. The article states results without proofs and refers to underlying work. Kienker's abstract and Larget's publisher abstract/references/citing list were read; their full proofs were not obtained.
- Finding: observation-preserving transformations and canonical aggregate representations are longstanding subjects. Larget's abstract claims equivalence conditions and minimal parameterizations under regularity assumptions.
- Limit: exact Larget hypotheses remain unverified; binary aggregate observations are not resolved edges. The realization memo records backward links to Blackwell–Koopmans, Gilbert, Ito–Amari–Kobayashi, Rydén, and forward reconstruction work. These citation links are search leads, not inspected theorem evidence.

## E008

**Exact equilibrium/nonequilibrium observational ambiguity is known**

- Kind: primary result; inference.
- Source: M. Wagner and J. Timmer, *The Effects of Non-Identifiability on Testing for Detailed Balance in Aggregated Markov Models for Ion-Channel Gating*, Biophysical Journal 79 (2000), 2918–2924, [DOI](https://doi.org/10.1016/S0006-3495(00)76529-5); [inspected full author PDF](https://jeti.uni-freiburg.de/papers/detailed_balance_printed.pdf).
- Locators: pp. 2919–2920, “Criterion for non-identifiability” and “Testing for detailed balance.”
- Finding: topology-preserving local similarity families can leave aggregate observations invariant; the four-state loop with equal open dwell times admits indistinguishable equilibrium and nonequilibrium dynamics.
- Inference: since standard state-level entropy is zero precisely at detailed balance, this already obstructs generic thermodynamic-identifiability claims for aggregate observations.
- Limit: no full entropy upper-range theorem or direct preservation of one specified resolved microscopic edge follows automatically.

## E009

**Recent coarse-grained compatibility and equilibrium-feasibility conditions**

- Kind: primary result; inference.
- Source: B. Wu and C. Jia, *Parameter Inference and Nonequilibrium Identification for Markov Networks Based on Coarse-Grained Observations*, Physical Review Letters 134, 087103 (2025), [DOI](https://doi.org/10.1103/PhysRevLett.134.087103); [inspected full arXiv v2](https://arxiv.org/html/2406.19586v2), 2024-12-13.
- Locators: Model section; Eqs. (2), (4)–(10), (12)–(13); End Matter Appendix A.
- Finding: with known topology and stated spectral/visibility conditions, equal sufficient statistics characterize compatible rates. Necessary equilibrium conditions detect nonequilibrium when violated; Appendix A proves an equilibrium-feasibility converse for three states and two clusters.
- Limits: parameter counting is not unique solvability. Distinct spectra do not alone ensure visible modes or valid eigenvector normalization. Aggregate-state data differ from resolved-edge marks. Published main/supplement differences were not checked because full publisher access was unavailable.
- Bearing: compatibility equations and equilibrium feasibility are close prior art; full entropy magnitude/range remains a separate question in the inspected version.

## E010

**Recent small-network equivalence classes include physical boundaries**

- Kind: primary result.
- Source: I. Siekmann, *Modelling ion channels with a view towards identifiability*, Bulletin of Mathematical Biology 88:2 (2026), online 2025, [DOI/full text](https://doi.org/10.1007/s11538-025-01558-3); [inspected author PDF](https://researchonline.ljmu.ac.uk/id/eprint/27780/1/Modelling%20ion%20channels%20with%20a%20view%20towards%20identifiability.pdf).
- Locators: sections 3.4.1–3.4.4, Eqs. (52)–(55), Fig. 7, Eq. (62).
- Finding: a fully connected three-state binary aggregate model has explicitly parameterized equivalent rates; classes can contain a detailed-balance curve or have no detailed-balance member, and one-way boundaries matter.
- Limit: the observations pool microstates; the full entropy range is not calculated. This is direct prior art for low-state compatibility geometry and equilibrium feasibility, so dimensionality alone cannot motivate a novelty claim.

## E011

**Phase-type existence and positive realization supply machinery, not the full answer**

- Kind: primary result.
- Sources: I. Horváth and M. Telek, *A Constructive Proof of the Phase-Type Characterization Theorem*, Stochastic Models 31 (2015), 316–350, [DOI](https://doi.org/10.1080/15326349.2015.1012912), [full preprint](https://arxiv.org/pdf/1502.00521); C. Commault and S. Mocanu, *Phase-type distributions and representations: Some results and open problems for system theory*, Int. J. Control 76 (2003), 566–580, [DOI](https://doi.org/10.1080/0020717031000114986).
- Locators/access: Horváth–Telek definitions 1–5 and Theorem 3, pp. 1–4; Commault–Mocanu section 3.2, Theorem 4, pp. 570–571, full relevant texts.
- Finding: scalar PH representability has a characterization and constructive proof; a suitable positive stable SISO realization can be normalized to PH form at the same order and graph.
- Limits: scalar existence does not impose a state-count cap or a common realization for every kernel entry. The normalization does not automatically preserve prescribed edge boundary vectors. Historical open problems in the 2003 paper are not current open-problem evidence.

## E012

**Normalized similarity and marked-realization minimality are established tools**

- Kind: primary result; inference.
- Source: P. Buchholz and M. Telek, *On minimal representations of Rational Arrival Processes*, Annals of Operations Research 202 (2013), 35–58, [DOI](https://doi.org/10.1007/s10479-011-1001-5); inspected author-uploaded 2011 preprint via [ResearchGate](https://www.researchgate.net/publication/227072004_On_minimal_representations_of_Rational_Arrival_Processes).
- Locators: section 3 pp. 2–3, section 4 Theorem 5 p. 9, section 7 Theorems 7–8 pp. 15–16.
- Finding: simultaneous normalized similarity/intertwining preserves marked arrival laws; generalized observability and controllability characterize rational-realization minimality, under the stated stationary-vector assumptions.
- Limits: rational minimality can differ from minimal positive/Markovian order. A general mark can pool microscopic edges; the rank-one resolved-edge constraints here require a specialization.
- Inference: the proof in E021 specializes classical realization machinery; it is not asserted to be a new general realization theorem.

## E013

**Time reversal must match the observation operation**

- Kind: primary results/comment and reply.
- Sources: I. A. Martínez, G. Bisker, J. M. Horowitz and J. M. R. Parrondo, *Inferring broken detailed balance in the absence of observable currents*, Nature Communications 10, 3542 (2019), [DOI](https://doi.org/10.1038/s41467-019-11051-w); D. Hartich and A. Godec, comment, Nature Communications 15, 8678 (2024), [DOI](https://doi.org/10.1038/s41467-024-52602-0); original authors' reply, 15, 8679 (2024), [DOI](https://doi.org/10.1038/s41467-024-52603-z).
- Access/locators: waiting-time irreversibility construction and the full 2024 comment/reply discussion, detailed in the thermodynamic memo.
- Finding: waiting-time asymmetry can supply information beyond observed currents, but coarse-graining and physical time reversal need not commute for all protocols.
- Limit: this issue does not invalidate the correctly reversed resolved-edge construction of E001. It motivates fixing even microscopic states and a reverse-closed mark set, rather than transferring an estimator to arbitrary blurred observations.

## E014

**Few visible transitions and unresolved events require different data models**

- Kind: primary result.
- Sources: P. E. Harunari, A. Dutta, M. Polettini and É. Roldán, *What to Learn from a Few Visible Transitions' Statistics?*, Physical Review X 12, 041026 (2022), [DOI](https://doi.org/10.1103/PhysRevX.12.041026), [full preprint](https://arxiv.org/pdf/2203.07427v2); P. E. Harunari, *Uncovering nonequilibrium from unresolved events*, Physical Review E 110, 024122 (2024), [DOI](https://doi.org/10.1103/PhysRevE.110.024122), [full preprint](https://arxiv.org/pdf/2402.00837v3).
- Locators/access: 2022 sections II–III, Eqs. (4)–(14); 2024 section III.C, Eqs. (24)–(27), section VI; full relevant PDFs.
- Finding: visible-transition statistics constrain currents, affinities and entropy in specified networks. Unresolved event labels require additional handling; known cycle families can enable stronger reconstruction.
- Limit: pooled marks do not generally reset the hidden state, so their history need not be captured by a one-step next-mark/time kernel. No general resolved-edge entropy-fiber classification is imported from these results.

## E015

**Channel ambiguity is a separate thermodynamic inverse problem**

- Kind: primary preprint result.
- Source: Y. Tian, *Thermodynamic incompleteness of state dynamics in Markovian transport*, arXiv:2605.02650v2 (2026-05-14), [inspected PDF](https://arxiv.org/pdf/2605.02650v2).
- Locators: propositions 2–3, record-kernel criterion and convex-hull channel allocation.
- Finding: identical state dynamics can admit different unresolved channel assignments and transport thermodynamics.
- Limit: this recent preprint is not peer-reviewed evidence of a full solution to our problem. Its hidden variables can remain ambiguous even when the state generator is fixed.
- Bearing: the baseline deliberately fixes one thermodynamic channel per state pair. Extending it requires a separately stated entropy observable.

## E016

**Precise compatible-model question and a finite exact equality certificate**

- Kind: assumption and analytic inference, derived in this workspace.
- Artifact: [formulation](../analysis/formulation.md), especially data, admissible classes and finite certificates.
- Adopted model: finite irreducible simple bidirected row-generator CTMC; even states; nonempty reverse-closed individually resolved edge marks with known incidence; joint densities including next-mark probabilities and time units; single-channel state-level entropy with Boltzmann constant one.
- Deduction: retaining original diagonals in the killed matrix gives the shared realization Ψ(t)=R exp(Tt)B. Observational equivalence compares this whole matrix function. Within a specified model class, the entropy image is a singleton, finite but non-singleton, or unbounded above; an empty fiber is inconsistent data.
- Exact certificate: for realization dimensions n and n', equality of RT^kB for k=0,...,n+n'-1 implies equality for all times, by Cayley–Hamilton on the block-diagonal difference realization. Finite floating-point samples are not this certificate.
- Limit: this is infinite-statistics structural identifiability, not a stable finite-data reconstruction theorem.

## E017

**At most three states: one observed bidirectional edge identifies all rates**

- Kind: analytic inference; reproduced calculation for selected examples.
- Artifacts: [small-network audit](../analysis/small-network-audit.md), section 1; [executed checks](../analysis/small-network-checks.json).
- Result: in the baseline class with at most three states, zero-time kernel values identify the observed rates, first derivatives identify hidden entrance rates, and second derivatives identify both hidden exit rates. The argument includes a hidden leaf and the two-state limit.
- Checks: exact rational recovery of two triangles, both hidden-leaf placements, and a two-state model.
- Limit: uniqueness is over the at-most-three-state class. A larger nonminimal model can share some of these kernels. The derivation is checked here, but no novelty is asserted; E002 and E007–E012 are relevant prior machinery.

## E018

**A lumpable four-state diamond has entropy range [0, infinity)**

- Kind: analytic inference; reproduced calculation.
- Artifacts: [small-network audit](../analysis/small-network-audit.md), lumpability section; [script](../analysis/check_small_networks.py) and [results](../analysis/small-network-checks.json).
- Construction: in order (x,y,h,k), observed x↔y, let rows of Q(u) be (-3,1,u,2-u), (1,-3,1,1), (1,1,-2,0), (1,1,0,-2), with 0<u<2.
- Proof/result: strong lumping h,k to one state preserves all observed kernels. Entropy equals (1-u)log((2-u)/u)/8, extends to zero at u=1, and diverges at both ends. Continuity gives the whole range [0,infinity).
- Provenance: inspired by the inspected mechanism in E001; this fixed-aggregate-entrance family was derived here. Exact intertwining and seven derivative equalities against the three-state quotient were checked.
- Limit: this realization is nonminimal, so it cannot alone refute identifiability under an imposed minimality condition.

## E019

**Minimal four-state ambiguity survives removal of redundant states**

- Kind: analytic inference; reproduced calculation.
- Artifacts: [small-network audit](../analysis/small-network-audit.md), minimal complete-graph family; [script](../analysis/check_small_networks.py), [results](../analysis/small-network-checks.json).
- Construction: Q0 has rows (-6,1,2,3), (1,-10,4,5), (2,4,-7,1), (3,5,1,-9), observing the first edge in both directions. Set S=diag(I2,[[1-e,e],[0,1]]) and Qe=S^-1 Q0 S for 0≤e<2/3.
- Result: each Qe has the same complete graph, full kernel and minimal realization dimension four. Its entropy is e/4 times log[120(1+2e-e²)²/((2-3e)(4-5e)(3+2e)(5+4e))]. This equals zero at e=0 and diverges at 2/3, so this fixed fiber has range [0,infinity).
- Checks: exact generator/stationarity/similarity identities, rank-four controllability and observability, eight Markov parameters, and independent matrix-exponential and entropy evaluations.
- Limit: a rigorous example, not an exhaustive complete-graph classification or certified novel discovery. All rates stay bounded above; one reverse rate tends to zero.

## E020

**Executed reproducibility and falsification checks**

- Kind: reproduced calculation.
- Artifacts: [run instructions](../analysis/README.md), [script](../analysis/check_small_networks.py), [recorded JSON](../analysis/small-network-checks.json). Latest recorded run: 2026-09-10T04:36:46.881935+00:00, repeated successfully during maintenance review.
- Environment: Python 3.9.12, NumPy 2.0.1, SciPy 1.13.1, Windows. Exact rational inputs are embedded; no random sampling.
- Method: Fraction algebra verifies identities and finite all-time certificates; SciPy matrix exponentials independently check 66 times from zero through 100. Stationarity, normalization, event frequencies, minimality and closed entropy formulas are checked.
- Output: maximum complete-graph kernel residual 4.0245584642661925e-16; entropy formula residual at most 8.881784197001252e-16. Both negative controls are detected: changing a physical rate changes the kernel, and recomputing killed diagonals produces a wrong kernel.
- Additional result: E021's representative distinct-escape diamond has π=(29,26,21,27)/103 and entropy 5 log(3/2)/103. Equal-escape example/factorization checks also pass.
- Correction: an initial run failed because NumPy fixed-width integers entered Fraction arithmetic; converting them to Python integers fixed that implementation issue. Only subsequent successful runs support the findings. The JSON records the script SHA-256.

## E021

**Complete compatibility reduction and a fixed-diamond classification**

- Kind: analytic inference; selected reproduced calculations.
- Artifact: [compatibility orbit proof](../analysis/compatibility-orbit.md), sections 1–5; E020 for examples.
- General result: at the minimal linear-realization dimension, two compatible models differ by S=diag(I_visible,U), with U invertible and U1=1. Entries of U may be signed; physical generator signs and the chosen topology select the admissible region. Reverse-closed resolved marks pin visible rows and columns. The proof specializes the prior machinery in E012.
- Topology-specific result: a full four-state diamond has observed x↔y, all four positive hidden-visible links, and no hidden-hidden link. Distinct hidden escape rates give two noncancelling poles in the observable hidden response; their residues recover all rates up to hidden permutation. Equal escape rates give an unbounded entropy fiber, including nonminimal cases, by an explicit positive factorization approaching a one-way boundary at nonzero opposing flux. The data distinguish these strata.
- Example: the equal-escape minimal family has entropy e log[(1+2e)(2-e)/((1-2e)(2+e))]/4, 0≤e<1/2, and full range [0,infinity).
- Limits: equality of hidden escape rates does not mean repeated poles of the full transfer function. General equal-escape fibers are proved unbounded; their entropy infima are not all proved zero. This class has no bounded-but-nonunique case, but other topologies remain unclassified here. Novelty requires further comparison.

## E022

**Partial-state reconstruction has additional hypotheses and a different observation protocol**

- Kind: abstract-only primary statement and primary-author review account, distinguished below.
- Sources: Xiang, Zhou, Deng and Yang, *Identifying the generator matrix of a stationary Markov chain using partially observable data*, Chaos 34, 023132 (2024), [DOI](https://doi.org/10.1063/5.0156458), [abstract](https://pubmed.ncbi.nlm.nih.gov/38386908/); X. Xiang and Y. Deng, *Parameter estimation for stationary Markovian systems based on partially observable information*, Scientia Sinica Mathematica 55 (2025), 1527–1548, [DOI](https://doi.org/10.1360/SSM-2024-0260), [full author-review PDF](https://www.sciengine.com/doi/pdfView/44DD49AD8BDD4325A8C525255E5CA50C).
- Access/locators: 2024 abstract/first-page preview only; 2025 full text, section 3.1 p. 1535, theorems 3.1–3.3 p. 1540, definition 3.3 p. 1543 and section 3.6.
- Finding: the authors report reconstruction using separately observed states at leaves and adjacent states on cycles, with distinguishability and diagonalizability restrictions. The later review clarifies known-topology assumptions and the irreversible subclass.
- Limit: the original proof and deferred distinguishability definition remain unverified. Edge timestamps do not automatically reveal every visit to a visible endpoint, so these theorems are not imported as a solution. Author review and original abstract constitute one evidential origin.

## D001

**Fix the data and model class before discussing identifiability**

- Date: 2026-09-10 UTC.
- Decision: adopt E016 as the derived working formulation; preserve human-owned PROJECT.md.
- Basis: E001, E007, E011–E015 show that resolved edges, pooled observations, fixed order, algebraic minimality and channel assignments lead to different inverse problems.
- Consequence: report every conclusion with its cardinality/topology assumptions. Do not treat normalized conditional dwell shapes alone as the full data or equate estimator saturation with global uniqueness. Reconsider if the human chooses a different physical observation protocol.

## D002

**Focus prospective novelty on the exact entropy range, not generic hidden-model ambiguity**

- Date: 2026-09-10 UTC.
- Decision: do not present compatible-model minimization, hidden similarities, or indistinguishable equilibrium/nonequilibrium models as new. Investigate exact entropy images under resolved-edge constraints and specified positive-rate classes.
- Basis: E004–E012 and E014. Recent compatibility/equilibrium work narrows the gap further.
- Consequence: broad N≤6 enumeration is deferred. A publication claim remains conditional on theorem-level comparison with closest prior work, including access gaps. Absence of a located full classification is not proof of novelty.

## D003

**Reject minimality as a cure; replace a graph-only criterion with a rate-sensitive question**

- Date: 2026-09-10 UTC.
- Decision: reject the hypothesis that excluding redundant states restores entropy identifiability, and reject a universal classification by topology alone.
- Basis: E019 is minimal and unbounded. E021 gives both unique and unbounded fibers on the same fixed diamond, distinguished by hidden escape rates. E018 alone would not establish either conclusion.
- Next action: use the two-parameter hidden-similarity domain to determine whether any other minimal four-state fixed-graph fiber has a finite non-singleton entropy range without imposing a common positive rate cutoff. Seek an exact bounded example or a rigorous boundary criterion; do not assume a universal unique/unbounded dichotomy.
- Reconsider when: a matching prior theorem settles this question, or a carefully checked bounded-but-nonunique fiber changes the boundary hypothesis.
