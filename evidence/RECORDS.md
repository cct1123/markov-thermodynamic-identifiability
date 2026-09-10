# Evidence and decision records

Recorded and retrieved **2026-09-10 UTC**, unless stated otherwise. Primary findings below are source-reported, not independently replicated. Agent deductions and executed calculations are separately labeled. The two [thermodynamic](hidden-entropy-frontier.md) and [realization](realization-frontier.md) memos preserve additional locators, citation trails, and access limitations. No downloaded source archive is claimed.

Execution dates and hashes identify the runs described in each record. [E044](#e044) records the maintenance replays and validation fix; the linked JSON outputs contain the current source hashes. Earlier research decisions about leaving changes uncommitted are historical; [D010](#d010) records the user's subsequent commit/push authorization.

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
- Artifacts: [run instructions](../analysis/README.md), [script](../analysis/check_small_networks.py), [recorded JSON](../analysis/small-network-checks.json). Research run: 2026-09-10T04:36:46.881935+00:00. Maintenance replay and the added irreducibility guard are recorded in E044.
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
- Follow-up: the limitation to this topology is the scope of the original note. E023–E027 subsequently classify every four-state support, including unknown topology and nonminimal models; E030 gives the observable criterion.

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
- Outcome: the proposed four-state question is resolved negatively by E023–E027. D005 replaces this historical next action with the five-state question and records the state-budget restriction.

## D004

**Resume the saved research question under renewed authorization**

- Date: 2026-09-10 UTC.
- Decision: the new research brief reopens investigation after maintenance commit 113b76e; no further commit or push is authorized in this run.
- Basis: the user repeats the autonomous frontier/exploration request. The initial formulation and literature map already exist, so resume D003's bounded-but-nonunique four-state question rather than repeating broad searches.
- Consequence: audit a candidate fixed-topology dichotomy and the nearby unknown-topology case; pursue focused prior-art verification. Candidate arguments remain provisional until checked. Preserve PROJECT.md and existing evidence history.

## E023

**Minimal four-state fixed-topology entropy dichotomy**

- Kind: analytic inference, independently audited; no publication-novelty claim.
- Date: 2026-09-10 UTC. Artifact: [fixed-topology proof](../analysis/four-state-classification-audit.md), sections 1–6; underlying orbit reduction in E021.
- Result: with one resolved observed pair, known incidence, a connected simple bidirected four-state graph, positive present rates and minimal kernel dimension four, each fixed-topology entropy fiber is a singleton or unbounded above. There is no bounded non-singleton case.
- Mechanism: a visible endpoint with one hidden neighbor pins the hidden similarity. Without such a singleton, the remaining supports are a tree, a full diamond, a complete graph, or a hidden triangle with an observed pendant edge. The first two are already classified. For the last two, fixed trace bounds rates; full controllability/observability bounds the similarity and its inverse, retaining irreducibility and positive stationary probabilities at the boundary. Paired-zero boundaries occupy only finitely many points of the two-dimensional admissible similarity domain, forcing a one-way boundary and divergent entropy.
- Audit corrections: permanent absent edges must not be counted as newly paired zeros; normalized hidden diagonalizers can fail to exist but form at most two points; boundary minimality must precede the irreducibility argument. E024 supplies an independent constructive route for the remaining dense-incidence cases.
- Limits: this proof assumes minimality and fixed topology. E027 removes minimality, and E024 treats unknown topology. Closed realization orbits are prior theory, not a novel ingredient (E025).

## E024

**Unknown topology at minimal dimension four: two globally unique cases, all others unbounded**

- Kind: analytic inference, independently audited; selected reproduced checks in E026.
- Date: 2026-09-10 UTC. Artifact: [unknown-topology proof](../analysis/unknown-topology-audit.md), sections 2–7.
- Result: allow all connected bidirected topologies on exactly four states while observing the resolved pair x↔y. For minimal four-state kernels, global generator/entropy uniqueness occurs exactly when (1) x and y each have one hidden neighbor and these neighbors differ, with the hidden-hidden edge either present or absent; or (2) there is no hidden-hidden edge, one visible endpoint touches only hidden h, the other touches both h,k, and the shared state's escape rate satisfies λh>λk. All other fibers have unbounded entropy. Hidden relabeling is immaterial.
- Global argument: with positive similarity determinant, a visible singleton forces either U=I or 0<u<1,v<0. Opposite singletons force identity. For a singleton/full incidence and diagonal hidden block, both transformed hidden off-diagonal signs are those of λk−λh. This excludes every competing topology in case (2), not only nearby perturbations. All other supports can reach a dense-incidence class or scalar hidden block through explicit signed similarities.
- Constructive divergence: for unequal hidden visible-exit rows choose r=min_i(Yhi/Yki) in (0,1) after hidden relabeling, over active visible endpoints. Use Ue=[[1−e,e],[0,1]], stopping at the first zero of m+e(λk−λh)−ne² or at e=r. Before that endpoint support and kernels are preserved; at it one forward flux vanishes while its reverse stays positive. The stationary law transforms to (πx,πy,(1−e)πh,πk+eπh), retaining positive limits.
- Limit: no entropy infimum or equilibrium compatibility is asserted. E027 extends the theorem to every four-state realization; E030 converts the result to an observable criterion.

## E025

**Focused prior-art check: unboundedness mechanisms and closed orbits have antecedents**

- Kind: primary results plus separately identified inference. Retrieval: 2026-09-10 UTC. Precise sources, versions, locators and access gaps are in [the follow-up memo](entropy-range-followup.md).
- Primary result: Ehrich (2021), *Tightest bound on hidden entropy production from partially observed dynamics*, [full preprint](https://arxiv.org/html/2105.08803v2), section 4 pp. 13–14 Eqs. (39)–(47), exactly parameterizes four-state discrete-time aggregate equivalence with two hidden states and unknown topology, assuming invertible hidden coupling blocks. Section 4.1 reports growing sampled entropy as grids refine, with a near-one-way edge mechanism. This is numerical evidence, not a universal upper-range theorem; section 5 anticipates continuous-time extensions.
- Primary result: Siekmann (2026), *Modelling ion channels with a view towards identifiability*, [DOI](https://doi.org/10.1007/s11538-025-01558-3), section 3.4.3 Eq. (62), explicitly constructs one-way boundary generators inside aggregate-equivalence parameterizations. Wagner–Timmer (2000), [DOI](https://doi.org/10.1016/S0006-3495(00)76529-5), pp. 2919–2920, provides exact equilibrium ambiguity and structural-zero-preserving local similarities. Both use aggregate observations, and neither inspected result is an entropy-range classification for our resolved pair.
- Primary theorem: Helmke–Moore, *Optimization and Dynamical Systems*, author-hosted second edition March 1996, [full text](https://users.cecs.anu.edu.au/~john/papers/BOOK/B04.PDF), section 7.4 Lemma 4.1, printed p. 212 (PDF index 222), proves that controllable/observable complex triples have closed similarity orbits of dimension n²; the real closed orbit is used on printed p. 288. The complete extracted lemma/proof was inspected. The originating Helmke (1993) article, [DOI](https://doi.org/10.1137/0331001), remains abstract-only here.
- Inference: fixed trace and nonnegative generator rates restrict the closed minimal orbit to a bounded closed set. This compactness specialization does not establish boundary irreducibility or positive opposing flux by itself. Do not claim orbit closedness, hidden ambiguity, or a one-way-edge mechanism as new.
- Search outcome/limits: no matching complete four-state resolved-edge dichotomy was located in this bounded primary-source and citation check. That is not proof of novelty. Larget's full theorem and the original Xiang reconstruction proof remain access gaps (E007, E022). The 2025 Seifert review was used only as a forward citation map, not as independent primary evidence.

## E026

**Executed exact witnesses for the four-state classification**

- Kind: reproduced calculation. Artifacts: [script](../analysis/check_four_state_classification.py), [JSON](../analysis/four-state-classification-checks.json). Command: `python analysis/check_four_state_classification.py` from the repository root.
- Run: 2026-09-10T04:51:46.386765+00:00; Python 3.9.12, NumPy 2.0.1, SciPy 1.13.1, Windows. Script SHA-256: `cbcc7efb6b46623574758af2706de3249419eca99112203fdc1c50ecb34d3d2c`; imported helper hash is recorded in JSON. Embedded rational inputs; no randomness or external dataset.
- Checks: three explicit paths (pendant triangle, complete graph with hidden-edge boundary first, and sparse support opening) have exact stationary laws, rank-four realizations, eight matching Markov parameters, bidirected positive interiors and irreducible one-way boundaries with positive opposing flux. Their entropy log coefficients are 536/1631, 2139/3344 and 4/75. Numerical kernel residual is at most 2.498001805406602e-16 over six times and three boundary gaps per path; final log slopes agree with the exact coefficients.
- Additional checks: five exact support-opening examples cover distinct/equal hidden escapes, same singleton and one-port structures. Signed rational grids in two globally unique examples admit only identity and hidden permutation. An equal-exit-row model has controllability/observability ranks (3,4), guarding against importing a minimal theorem without checking its premise.
- Limits: the grid is a negative-control search, not proof of uniqueness or exhaustiveness. General coverage comes from E023–E024's analytic arguments.

## E027

**Exactly four states with one observed pair have no bounded nonunique entropy fiber**

- Kind: analytic inference, independently audited; representative executed checks in E029.
- Date: 2026-09-10 UTC. Artifact: [nonminimal extension](../analysis/nonminimal-four-state-audit.md), sections 1–5.
- Result: E023's fixed-topology dichotomy and E024's unknown-topology classification hold without assuming minimality. Every nonminimal four-state realization gives unbounded entropy when topology is unknown. The two unknown-topology uniqueness cases are automatically minimal and identify the generator.
- Proof: a visible singleton forces controllability and observability rank four by triangular coupling blocks or two-step access along the hidden edge. Potentially nonminimal cases therefore have only zero/full hidden incidence at each visible endpoint. A no-hidden-edge full diamond is covered by E021; a one-port tree has fixed-topology entropy zero. With a hidden edge, unequal exit rows admit E024's sufficient similarity construction even without minimality. Equal exit rows strongly lump, so varying one internal rate to zero with the opposite rate fixed preserves the complete kernel and keeps positive opposing stationary flux. The nonminimal tree can add that invisible hidden edge when topology is unknown.
- Consequence: finite nonunique entropy does not appear merely by union over unknown supports or by admitting redundant four-state realizations. Fixed-topology entropy uniqueness can still coexist with rate ambiguity, as in the nonminimal tree.
- Limits: no assertion that all nonminimal equivalents are similar. Exactly four states and the specified resolved observation remain essential; cardinality enlargement is handled separately in E028.

## E028

**One additional fully hidden state gives unbounded entropy; unrestricted cardinality has a visible test**

- Kind: analytic inference, independently audited; strong-lumping provenance in E001/E018; selected reproduced calculation in E029. Date: 2026-09-10 UTC.
- Artifact: [state-splitting proof](../analysis/state-splitting-audit.md), sections 1–6. Scope: any finite irreducible simple bidirected CTMC and any nonempty reverse-closed set of individually resolved observed edges with known incidence.
- Construction: split any state outside the observed endpoint set V into two clones. Split each old incoming rate in fixed positive fractions; duplicate each old outgoing rate; connect clones with rates m>0 and fixed n>0. The aggregation matrix C satisfies Qtilde C=CQ and Ttilde C=CT, with the required observed input/output identities, so all joint kernels remain exactly unchanged.
- Entropy: for original hidden escape λ, original stationary mass πh, and assigned incoming flux divided by πh equal to α in (0,λ), clone stationary masses are πh(α+n)/(λ+m+n) and πh(λ+m−α)/(λ+m+n). As m tends to zero, entropy is b0 log(m_ref/m)+O(1), where b0=πh n(λ−α)/(λ+n)>0. All rates remain bounded above; the limiting chain remains irreducible even if the original hidden state was a leaf.
- Observable exception: zeroth and first kernel coefficients recover the entire Q_VV block. Its row deficits dv=−Σw∈V Qvw equal total rates into fully hidden states. If all deficits vanish, irreducibility excludes every larger compatible model, so the full generator is globally unique. If any deficit is positive and a finite realization exists, the splitting construction makes entropy unbounded in the unrestricted finite-state class.
- State-cap consequence: a compatible hidden-state model of size at most Nmax−1 guarantees unbounded entropy within the cap Nmax. For one observed pair, a five-state realization therefore makes the class N≤6 unbounded. Cases requiring the full cap, and fixed-dimension minimal classes, remain substantive. Minimum admissible CTMC size is not automatically the minimum linear realization dimension.
- Limits: the clone family is nonminimal and changes cardinality/topology. This is not a fixed-topology or fixed-minimal-order theorem, not a general realization-feasibility test, and not a statement about entropy minima or physical channel decompositions. Novelty remains unverified.

## E029

**Executed cloning and nonminimal-family checks**

- Kind: reproduced calculation. Artifacts: [script](../analysis/check_state_splitting.py), [JSON](../analysis/state-splitting-checks.json). Command: `python analysis/check_state_splitting.py`.
- Run: 2026-09-10T04:59:11.675261+00:00; same environment as E026. Script SHA-256: `9d925a943330513022a690111761336ff9cb2835916a026405a373a96653bc27`; both helper hashes are in JSON. Inputs are exact embedded generators; no randomness.
- Result: a generator in E024's globally unique four-state case was expanded to five states with split fraction 1/3, reverse clone rate 2 and forward rates 10^-3, 10^-6 and 10^-9. Exact intertwining, stationary equations, aggregation of stationary mass and derivative orders 0–8 certify equality of the full four-versus-five-state kernels. The entropy divergence coefficient is 11/60; the final numerical log slope agrees within relative tolerance 10^-5.
- Nonminimal controls: full hidden incidence and a one-port tree with equal exits both preserve their three-state quotient kernels after adding internal rates. Exact seven-parameter certificates and positive boundary stationary fluxes agree with the predicted divergence. The script checks representative formulas; E027–E028 supply the general proofs.

## E030

**An exact observable four-state uniqueness criterion uses only three derivatives**

- Kind: analytic inference, independently audited; representative reproduction in E031. Date: 2026-09-10 UTC.
- Artifact: [observable criterion and reconstruction](../analysis/observable-four-state-criterion.md), operational theorem and sections 1–5. Assume the data admit an exactly-four-state baseline CTMC with only the resolved pair x↔y observed; topology is unknown and minimality is not imposed.
- Extraction: recover observed rates r,s and visible killed block K(t) from the joint kernels. Then D=K′(0), A=D+observed visible off-diagonals, a=−A1, M=K″(0)−D² and L=K‴(0)−D³−DM−MD. In every candidate M=XY and L=XHY.
- Unique case A: ax,ay>0 and both off-diagonal entries of M vanish. Positivity forces disjoint hidden incidence. Reconstruct X=diag(a), Y=diag(Mxx/ax,Myy/ay), H=X^-1 L Y^-1.
- Unique case B: M is invertible, J=LM^-1 has distinct eigenvalues −λf,−λs with λf>λs>0, and residues Zf=−(L+λs M)/(λf−λs), Zs=(L+λf M)/(λf−λs) satisfy rank(Zf)=1, Zf strictly entrywise positive, Zs=c e_j e_j^T for c>0. Reconstruct each hidden entrance column as Zℓ1/λℓ, normalize its exit row from the residue product, and set H=diag(−λf,−λs).
- Independent sufficiency: in B an irreducible two-state hidden block would have a strictly positive slow-mode residue at both active endpoints, contradicting the singleton slow residue. Thus all candidates have no hidden edge, and the residues plus row sums uniquely fix their rates. Both A/B have det M>0 and are automatically minimal. Necessity and the unbounded complement follow from E024/E027.
- Limits: singular M need not mean nonminimality. A repeated hidden pole with rank-two residue can still satisfy A. Exact rank/zero/order tests are conditional on four-state feasibility; no noisy-data thresholding or arbitrary-function feasibility claim is made. The complement is unbounded above, with infimum undetermined in general.

## E031

**Executed observable-criterion reconstruction and falsification checks**

- Kind: reproduced calculation. Artifacts: [script](../analysis/check_observable_criterion.py), [JSON](../analysis/observable-criterion-checks.json). Command: `python analysis/check_observable_criterion.py`.
- Run: 2026-09-10T05:06:52.278728+00:00; Python 3.9.12, NumPy 2.0.1, SciPy 1.13.1, Windows. Script SHA-256: `40af86e70e5f3a522d8f2a92196a13e59879b706694a5b84a965c625012af51b`; imported helper hashes are in JSON. Nine embedded rational inputs; no external data or randomness.
- Checks: extraction uses only the four matrix coefficients of the actual joint kernels, then reconstructs four unique generators exactly, including opposite singletons with one rank-two hidden pole and both visible orientations of B. Recovered generators also pass eight-parameter all-time certificates.
- Negative controls: reversing the shared/singleton escape ordering, equal escapes, a distinct-escape full diamond with unknown topology, a minimal rank-four model with singular M, and a nonminimal model all fail the uniqueness criterion as required. The singular-M minimal example explicitly guards against conflating coupling rank and realization rank.
- Limit: the small audit uses rational hidden eigenvalues in its selected B/complement examples and asserts exact rational discriminants. It is not a general eigensolver, feasibility algorithm or finite-sample inference implementation. General coverage rests on E030's proof.

## D005

**Close the four-state question and isolate the effect of the state budget**

- Date: 2026-09-10 UTC. Basis: E023–E031 and the prior-art limitations in E025.
- Decision: D003's proposed bounded-but-nonunique four-state search is resolved negatively, for fixed and unknown topology, including nonminimal realizations. Retain its earlier text as history, but do not repeat that search. The complete finite observable test is a stronger candidate contribution than another ambiguous model pair; publication novelty remains unestablished.
- Interpretation: unrestricted finite cardinality has an elementary unique/unbounded upper-range dichotomy by state splitting and visible deficits. Under a cap, a hidden-state realization with one spare state already suffices for unboundedness. Broad N≤6 enumeration would mostly revisit this construction.
- Next action: attack the first remaining dimension, a minimal five-state kernel under a five-state cap with unknown bidirected topology. Use the three-hidden-state similarity domain to seek an exact bounded non-singleton entropy fiber or a proof that every entropy-varying fiber has a divergent boundary. Begin with sparse support constraints; do not infer a five-state theorem from a numerical failure or the four-state planar argument.
- Falsification and resumption: one certified bounded nonunique fiber refutes extension of the dichotomy. A valid general boundary argument would extend it; a matching prior theorem would redirect the project. Minimum linear dimension five ensures that the cloning construction has no spare state under this cap, without assuming equality of linear and positive realization orders in general.
- Stopping rationale: this run reaches a defensible exact four-state answer, an independently reconstructed observable criterion, and a cardinality impossibility result. A five-state support/boundary proof is a distinct research step beyond these accepted results; further broad source collection or enumeration is not needed to support the present synthesis. General classification through six states and publication novelty remain unresolved.

## D006

**Resume at five states and test whether pairwise boundary arguments suffice**

- Date: 2026-09-10 UTC. The new user research brief reopens the completed run and retains the scientific objective; existing uncommitted results remain the starting evidence. Preserve PROJECT.md and leave changes for review.
- Decision: pursue D005's minimal five-state question with bounded independent audits of sparse support, embedded hidden-pair transformations, and close realization/entropy prior art. The coordinator examines possible higher-dimensional obstructions and performs only targeted calculations justified by those arguments.
- Success criteria: obtain an exact bounded nonunique example, a proved extension covering a meaningful class, or a specific obstruction that materially narrows the remaining question. Distinguish each from a full five-state classification; no broad graph enumeration and no novelty claim from search absence.

## E032

**Hidden-pair boundary constructions extend to arbitrary fixed dimension**

- Kind: analytic inference, independently audited; representative exact checks. Date: 2026-09-10 UTC. Artifact: [hidden-pair audit](../analysis/hidden-pair-boundary-audit.md), sections 1–6.
- Result: two fully hidden states with identical neighbors among all other states, including other hidden states, give an unbounded fixed-topology entropy fiber if their mutual edge is present and their full external exit rows differ. The same holds without their mutual edge when their total escape rates agree. The normalized triangular similarity and positive limiting stationary masses from E024 extend verbatim with all other coordinates fixed.
- Minimality: identical full external exit rows imply an invariant codimension-one reachable subspace and hence nonminimality. Thus minimality supplies the unequal-row premise. Adjacent identical-exit pairs outside the minimal subclass are still unbounded by varying an existing invisible internal rate under strong lumping; no new state is needed. Two unjoined identical-exit leaves sharing one neighbor are a necessary exception to fixed-topology pair divergence.
- Unknown-topology extension: hidden twins with distinct escapes can open their missing mutual edge. Strictly nested external neighborhoods can become twins if the pair is adjacent, or if unjoined and the larger-neighborhood state's escape is no greater than the other's. These yield unboundedness at the same state count.
- Limit: incomparable neighborhoods, or the opposite escape order for an unjoined nested pair, pin only transformations of that pair. They do not establish global uniqueness. E035 supplies an exact counterexample requiring simultaneous three-hidden-state mixing. The audit includes independent exact checks and embedded reproducibility commands.

## E033

**A complete five-state sparse subclass: three distinct diagonal hidden modes**

- Kind: analytic inference with independent audit and reproduced examples. Date: 2026-09-10 UTC. Artifact: [sparse five-state proof](../analysis/five-state-sparse-audit.md), sections 1–5 and embedded executable check.
- Scope: one resolved observed pair, a representative with three hidden states, no hidden-hidden links, and three distinct hidden escape rates; competing topologies and counts up to five are allowed. Distinct modes and nonzero incidence imply minimum linear dimension five by Vandermonde controllability/observability, not scalar pole counting alone.
- Classification: global uniqueness occurs exactly when the three hidden visible-neighbor sets are {x}, {y}, {x,y}, with the shared state's escape larger than both exclusive escapes. Every other fiber in this subclass is unbounded. Repeated incidence or the reverse rate ordering admits embedded pair opening and divergence.
- Global proof of the unique case: cross-port hidden responses have only the shared state's pole. Every hidden connected component touching both ports has a positive dominant-pole residue. The shared pole is faster than both others, so a bridging component cannot contain either other eigenvalue. It must be a singleton; the remaining two exclusive poles force separate singletons. Residues and row sums then identify all rates against arbitrary three-coordinate mixing.
- Executed examples: the unique rational matrix has stationary law (8,10,8,5,6)/37 and entropy 2 log(2)/37. Raising one exclusive escape from 1 to 4 yields an exact signed-similarity family with entropy divergence coefficient 8/93. Both have rank (5,5); ten Markov parameters, stationary equations and six parameter points pass. The full code, inputs, values, runtime and helper checksum are embedded in the note; root independently reran it successfully.
- Limit: no classification of repeated hidden modes, general coupled hidden blocks or every five-state fiber. Novelty unestablished.

## E034

**Maximal observed path delay forces global rate uniqueness under a state cap**

- Kind: analytic inference, independently audited; reproduced checks. Date: 2026-09-10 UTC. Artifact: [path-cap proof](../analysis/path-cap-uniqueness-audit.md); script/output in E036.
- Theorem: for feasible baseline data with one observed pair and cap N≥3, if the first nonzero derivative of the visible killed-semigroup entry Kxy occurs at order N−1, every compatible model has exactly N states and its killed graph is the simple x-to-y path through all vertices. The full generator is that path plus the observed edge and is globally unique up to hidden labels.
- Proof: the first nonzero derivative is a positive sum of shortest unobserved path weights; negative diagonals cannot contribute at that order. A path of length N−1 saturates the cap. Bidirectionality makes every extra edge a forward shortcut, so none is allowed. Endpoint resolvent continued fractions recover ordered diagonals di and adjacent products pi. Known observed rate r and row sums recover f0=−d0−r, b0=p0/f0, then fi=−di−b(i−1), bi=pi/fi. The last row checks the observed reverse rate. Endpoint Krylov triangularity proves minimal dimension N.
- Primary attribution: endpoint Jacobi recovery is established theory; Gesztesy–Simon (1997), [author text](https://math.caltech.edu/papers/bsimon/p261.pdf), Theorem 3.5 printed p. 12, Theorem 3.1 p. 8 and reconstruction pp. 11–12. Bidirected paths are diagonally symmetrizable, preserving endpoint resolvents. The cap and CTMC row-sum deductions are made here; no novelty is asserted.
- Checks/limits: exact three-, five- and six-state examples recover all rates; endpoint derivatives through 2N−1 suffice for the reconstruction. The five/six-state added-chord controls shorten the derivative delay as predicted. The test is sufficient, assumes exact zeros and feasibility, and fails to force the path when a larger state budget is allowed.

## E035

**An isolated minimal five-state realization shares its kernel with an unbounded component**

- Kind: analytic inference and reproduced exact calculation, independently audited. Date: 2026-09-10 UTC. Artifact: [theta global audit](../analysis/theta-global-audit.md), with exact witnesses in [the check output](../analysis/five-state-extension-checks.json).
- Source: in order (x,y,h,k,l), Q has rows (-11,1,2,0,8), (2,-20,0,7,11), (3,0,-7,4,0), (0,6,5,-11,0), (3,3,0,0,-6). Its unobserved paths are x-h-k-y and x-l-y. Every isolated hidden-pair transformation is pinned by incomparable external neighborhoods. The full marked kernel is minimal of dimension five.
- Local isolation certificate: parameterize normalized hidden similarities near identity by six off-diagonal perturbations. The eight missing directed rates have first-order matrix A of rank six. In row-major missing-edge order, c=(3,1,1,10/3,7/3,19/15,151/15,79/15)>0 satisfies cA=0 exactly. Any nearby feasible sequence would yield a nonzero direction v with Av≥0, forcing Av=0 and then v=0, a contradiction. Continuity of U=C(C′)^-1 with C=[Y,1] nonsingular transfers isolation to generator space.
- Distant compatible generator: U=(1/1000)[[871,-390,519],[623,790,-413],[-183,133,1050]], det U=34813/31250, yields Q*=diag(I2,U)^-1 Q diag(I2,U). Every off-diagonal rate is positive; their minimum is 139/500. Exact ranks (5,5), stationarity and Markov parameters 0–9 verify membership of the same fiber. Its entropy is approximately 0.4376183787 versus 0.0428244846 at the isolated source.
- Explicit unbounded component: mix indices 3,4 of Q* with [[1−e,e],[0,1]]. For 0≤e<e*=104489/1158489 the graph remains complete. The hidden-rate positivity polynomial at e* is 6376107122347/1342096763121>0. At e*, rate 3→x vanishes with positive opposing flux c*=53132140/1141883991; entropy is c* log(1/(e*−e))+O(1). All rates remain bounded above and stationary masses have positive limits.
- Conclusion: the full minimal five-state compatibility set is disconnected, even modulo hidden permutations: an isolated point coexists with a continuous unbounded-entropy family. Local identifiability, pairwise rigidity and continuation from one physical model cannot establish global entropy uniqueness. This does not imply that the entropy image itself is disconnected.
- Limit: an exact example, not a universal five-state classification or a publication-novelty claim. The same support with last row (9,10,0,0,-19) also admits an exact infinitesimal three-state opening despite pairwise rigidity; E036 checks both cases.
- Further inference: for this source, the nonsingular exit-coordinate matrix C=[Y,1] converts the entire normalized hidden-similarity class to noncollinear triangles of exit rates. The audit gives exact entrance barycenters, the quadratic inward vector field and the reciprocal-support constraints. This is a global coordinate reduction, not a convexity or completeness-of-search theorem.

## E036

**Executed five-state extensions and discovery of the distant component**

- Kind: reproduced calculation; search proposals separated from exact certificates. Artifacts: [exact script](../analysis/check_five_state_extensions.py), [exact output](../analysis/five-state-extension-checks.json), [bounded probe](../analysis/probe_theta_compatibility.py), [probe output](../analysis/theta-compatibility-probe.json).
- Commands from the root: `python analysis/check_five_state_extensions.py` and `python analysis/probe_theta_compatibility.py`. Research exact run: 2026-09-10T06:21:18.094203+00:00, SHA-256 `4f5ba7179e1af63f2115fbfb6bf98d672d6e8105a4730e8ef58c873c2ab0368d`. Discovery probe: 2026-09-10T06:21:18.791381+00:00, SHA-256 `1ce97dd30b38dca248df9bfb05bf2e9045e0c76bb50cca5d73dde8653d5c33ae`. E044 records subsequent maintenance replays; current JSONs contain their source/helper hashes. Environment: Python 3.9.12, NumPy 2.0.1, SciPy 1.13.1, Windows.
- Exact checks: generator signs and row sums, stationary laws, rank-five controllability/observability, ten all-time Markov-parameter identities, positive dual and rank-six local-isolation certificate, distant complete-graph membership, boundary coefficient and logarithmic entropy slope. The measured final slope 0.046530293323088445 agrees with the exact coefficient 53132140/1141883991 within relative tolerance 10^-5. Five/six-state path reconstructions and chord controls also pass. All exact inputs are embedded; those checks use no randomness.
- Discovery probe: SLSQP maximized a common positive off-diagonal lower margin over six hidden coordinates, with bounds [-3,3], positive determinant floor 10^-4, thirteen starts per model, seed 20260910 and at most 400 iterations per start. All thirteen opening-control starts found positive solutions. For the locally isolated target, only two starts found a positive complete solution; twelve of thirteen runs reported optimizer success. Rounded rational coordinates were then independently verified in the exact script, so the proof does not depend on numerical success flags or tolerances.
- Search limitations/failures: one target run did not report success; SLSQP emitted its standard bound-clipping warning. Neither is used as evidence of impossibility. The initial diagnostic probe used a symmetric eigenvalue routine on a nonsymmetric hidden block; it was corrected to `eigvals`, with exact tangent matrices and LP results unaffected. The corrected saved output is authoritative.
- Scope: this is a targeted two-model search and exact validation, not topology enumeration, exhaustive component discovery or a generic inference package.

## E037

**Finite realization alternatives and entropy upper bounds have restrictive prior hypotheses**

- Kind: primary results with separately labeled inference. Retrieval: 2026-09-10 UTC. Full details, exact locators and access outcomes: [five-state frontier follow-up](five-state-frontier-followup.md).
- Primary result: Rizk, Burke and Walsh, *On the Non-uniqueness of Representations of Coxian Phase-Type Distributions*, [arXiv:1901.03849v2](https://arxiv.org/pdf/1901.03849v2), Theorem 2 pp. 12–13 and Algorithm 1 pp. 13–14, gives finitely many global Coxian alternatives through diagonal permutations under nonredundancy. The forward marked-absorption extension is Lindqvist (2023), [DOI](https://doi.org/10.1007/s10985-022-09547-7), Theorems 4–5 and Example 5, journal-PDF pp. 12–13. Full primary texts inspected; their shared theorem is not counted twice as independent evidence.
- Inference: these models have one-way transient structure and a fixed entrance, so neither their finite enumeration nor resolved absorption causes establish a finite stationary entropy fiber for our bidirected two-reset observation. They do establish that local uniqueness cannot generally be substituted for global uniqueness in realization problems.
- Primary bound: Nishiyama–Hasegawa (2023), *Upper bound for entropy production in Markov processes*, [DOI](https://doi.org/10.1103/PhysRevE.108.044139), [full preprint](https://arxiv.org/pdf/2306.15251v2), Eq. (8), bounds stationary entropy by activity times log R times (R−1)/(R+1), where R is the maximum microscopic forward/reverse rate ratio. Section IV notes that partial observation does not supply R.
- Inference: fixed trace bounds activity but not R, so this theorem does not convert our compact rate closure into a finite entropy bound. The precise inverse-Jacobi theorem supporting E034 is attributed there. No matching full five-state entropy classification was obtained; absence from this bounded check does not establish novelty.

## E038

**A proposed finite representation ambiguity does not vary entropy**

- Kind: analytic inference, independently audited. Date: 2026-09-10 UTC. Artifact: [sparse audit](../analysis/five-state-sparse-audit.md), section 6.
- Candidate: assign three rank-one hidden-response residues between a two-state hidden path and a singleton parallel path. If either of two positive residues can pair with a signed residue to produce the two-state component, their off-diagonal entries in the proposed construction are respectively (c,d), (c,d), and (−c,−d).
- Negative finding: both unobserved paths then have the same rate-product ratio R=c/d. Orienting all paths x→y gives currents J0+J1+J2=0, so entropy equals J0 log[(r/s)/R], where r,s and observed current J0 are fixed by the full kernels. Thus distinct path representations obtained this way have identical entropy.
- Limit: no claim that these two representations exhaust the full fiber or that constant cross-response ratio excludes hidden dissipation. This rejects the candidate as a bounded-nonunique entropy example; it does not prove a general impossibility result.

## D007

**Reject local continuation as a global search method; focus on exact component geometry**

- Date: 2026-09-10 UTC. Basis: E032–E038.
- Decision: retain the complete four-state result, but do not extrapolate its low-dimensional geometry to five states. The new example proves that even exact local isolation can coexist with a distant unbounded component. Pair tests remain useful sufficient exclusions, and the distinct-diagonal subclass and cap-saturating path class are now settled.
- Consequence: a prospective bounded five-state fiber requires control of all compatible components. Counting parameters, preserving one topology, enumerating a canonical subclass, or starting continuation at one realization cannot supply that control. The finite residue-reassignment candidate is also rejected because it does not vary entropy (E038).
- Next action: use the exact exit-triangle parameterization in the theta audit to classify global feasibility across the two-parameter family obtained by replacing Q's final row with (a,b,0,0,−a−b), a,b>0. First determine when a distant complete realization exists; this certifies unboundedness via E032. Treat singular coordinate charts and nonminimal parameter strata separately. Absence of such a realization would require examining other supports before claiming uniqueness or boundedness.
- Stopping rationale: this run supplies a checked disconnected-fiber counterexample, exact divergence, substantial five-state and arbitrary-N special cases, and a bounded prior-art reassessment. A global two-parameter component classification is the next distinct theorem-level task. The full minimal five-state bounded/nonunique question and publication novelty remain unresolved; no commit or push is performed.

## D008

**Resume the two-parameter family with spectral and minimality strata explicit**

- Date: 2026-09-10 UTC. The renewed research brief reopens D007's global theta-family question; preserve prior uncommitted findings and PROJECT.md.
- Decision: independently analyze exact minimality/coordinate singularities, constructive fixed-dimension divergence, and positive-realization spectral constraints. Use only targeted parameter calculations, not topology enumeration. Distinguish absence of a complete representative from absence of all divergent compatible families.
- Success criteria: a parameter-dependent constructive theorem, a verified exceptional bounded/unique class, or an exact obstruction narrowing global feasibility. Save exact certificates and access limits before promoting conclusions.

## E039

**Exact theta-family rank strata and a global obstruction to connected hidden realizations**

- Kind: analytic inference and reproduced calculation, distinguished here. Date: 2026-09-10 UTC. Artifact: [parameter-strata audit](../analysis/theta-parameter-strata-audit.md).
- Family: Q(a,b) has rows (-11,1,2,0,8), (2,-20,0,7,11), (3,0,-7,4,0), (0,6,5,-11,0), (a,b,0,0,-a-b), with a,b>0 and only x↔y observed. Define alpha=9−2sqrt(6), beta=9+2sqrt(6), s=a+b.
- Exact inference: observability has rank five everywhere; a hidden minor is −14(11s+19). Controllability loses one dimension only at (a,b)=(2sqrt(6)−3,12−4sqrt(6)); the minimal linear dimension there is four. The chart determinant 3(6−2a−b) vanishes along an entire line, but that line is otherwise minimal. The fast coincidence s=beta is fully minimal; the slow coincidence s=alpha is minimal except at the stated point.
- Global obstruction: on s=alpha the dominant hidden-response residue determinant is (135−41sqrt(6)/2)(a−(2sqrt(6)−3)). At every minimal point it has rank two. An irreducible Metzler hidden block exposes a nonzero rank-one Perron residue, so no connected hidden representation is possible, even at larger order. This does not bound entropy on disconnected hidden supports; E041 settles this entire line as unbounded.
- Exceptional point: an explicit stochastic intertwining to a four-state algebraic realization, followed by a rational hidden similarity, yields a complete bidirected four-state CTMC with the same kernels. This proves admissible order four constructively. E028 then supplies a complete five-state cloning family with unbounded entropy under the cap.
- Reproduced calculation: the embedded coefficient-pair arithmetic over Q(sqrt(6)) checks five representative strata, ranks (4,4) of the complete four-state model, exact intertwining and strict positivity. It was executed by the auditor and rerun by the coordinator at approximately 06:55 UTC. Python 3.9.12, NumPy 2.0.1; the note contains the exact command and helper hash. SymPy was unavailable; no symbolic-package result is claimed.
- Limit: chart failure and hidden-pole coincidence are not by themselves nonminimality; absence of a connected hidden realization is not a finite-entropy certificate. No publication novelty claim.

## E040

**Primary positive-realization theory and the exact fixed-order reduction**

- Kind: primary results with separately labeled deductions. Retrieval: 2026-09-10 UTC. Sources/access and exact locators: [positive-realization frontier](positive-realization-frontier.md). Deduction: [fixed-order obstruction note](../analysis/positive-realization-obstructions.md), sections 1–5.
- Primary result: J. M. van den Hof, *Realization of continuous-time positive linear systems*, Systems & Control Letters 31 (1997), 243–253, [DOI](https://doi.org/10.1016/S0167-6911(97)00049-2), [full CWI PDF](https://ir.cwi.nl/pub/127/0127D.pdf). Definition 3.1 and Theorem 3.1, pp. 246–247, require shifted nonnegative Markov parameters and an invariant polyhedral cone containing the Hankel columns. Theorem 4.2, pp. 247–248, compares minimal positive orders across all admissible shifts; Example 4.1 explains why an arbitrary single shift is insufficient. Full theorem text was inspected by the source auditor and coordinator.
- Deductions specific to the minimal theta fiber: every compatible three-state hidden block has trace −(18+s). Consequently gamma=18+s makes P=I+H/gamma nonnegative with positive diagonals for every candidate. Complete five-state feasibility is equivalent to a three-dimensional realization of G(z)=F(gamma(z−1)) whose state, input and output matrices are all strictly positive. Diagonal scaling by r=(I−P)^−1B1 restores CTMC row sums; the visible entrance totals are G(1)1=(10,18). This is a strict three-ray invariant-cone question. The common shift is justified by fixed trace, not imported as a general theorem.
- Limits: the cone theorem gives no strict three-ray guarantee. Förster–Nagy (2000), [DOI](https://doi.org/10.1016/S0024-3795(00)00076-8), explicitly treats irreducible/strict/primitive main matrices in its abstract, but its full hypotheses, input/output strictness and dimension restrictions remain inaccessible. Matolcsi–Nagy (2004), Theorem 2.2 p. 515, [full journal PDF](https://www.acta.hu/download.phtml?id=2798), gives a scalar finite-dimension bound under its stated spectral assumptions; it does not imply a shared matrix realization at McMillan order. Source-level overlap remains a novelty risk.

## E041

**Constructive unbounded regions of the theta family, including both repeated-pole lines**

- Kind: analytic inference with independent algebraic audit. Date: 2026-09-10 UTC. Artifacts: [construction audit](../analysis/theta-family-construction-audit.md) and [full slow-line proof](../analysis/positive-realization-obstructions.md), section 6. Not a whole-plane classification.
- In E039 notation, unbounded entropy under the five-state cap is proved whenever: (i) s≤alpha; (ii) s≤beta, a>35sqrt(6)/88 and b>sqrt(6)/4; or (iii) s≥beta and either a/b>11(s−11)^2/1120 or b/a>14(s−7)^2/55. The union also covers every positive point on s=beta, including the single ratio where the two strict first-order tests fail.
- Construction for (ii): decompose F(z)=Zalpha/(z+alpha)+Zbeta/(z+beta)+Zs/(z+s). Zalpha and Zs are positive rank one; Zbeta has positive diagonal and negative off-diagonal entries. Reassign Zalpha to a singleton, then realize the other modes in a two-ray cone. Strictly positive entrance/exit matrices exist precisely at the two displayed coordinate thresholds for this construction. Diagonal scaling normalizes row sums. The pair is connected for s<beta, or unjoined with equal escapes for s=beta; E032 proves divergence in both cases.
- For s<alpha, a normalized three-coordinate perturbation built from the Perron vectors of the original two-state hidden block opens every missing rate strictly. For s≥beta, eliminating the six first-order variables yields exactly the two strict ratio inequalities in (iii). These are necessary and sufficient for strict first-order complete opening, not for existence of a distant complete model.
- Entire slow line: factor Zalpha=pr and Zs=vw with all factors positive. For sufficiently small epsilon>0, replace the repeated-alpha residue by (p+epsilon v)r+v(w−epsilon r). Both remain positive rank one, while the first plus Zbeta has strictly positive off-diagonal entries. The same two-mode construction yields adjacent external twins, hence divergence. No minimality is assumed. At minimal points the constructed hidden block must remain disconnected, consistently with E039.
- Entire fast line: its two strict ratio thresholds coincide, covering every ratio except one. The remaining point satisfies the strict coordinate thresholds of (ii); exact inequalities are given in the construction note.
- Limit: outside this union no conclusion follows from failure of these constructions. Their kernel identities and sign arguments are analytic. Numerical and exact representative verification are recorded separately; agreement between auditors is not counted as an independent empirical origin.

## E042

**Fast-region support exclusion and a precisely narrowed unresolved kernel**

Later resolution: [E048](#e048) proves global uniqueness at theta(100,100) and in a larger parameter region. The local and numerical findings below are retained as historical evidence; their original limitations remain valid.

- Kind: analytic inference plus an explicitly inconclusive numerical probe. Date: 2026-09-10 UTC. Artifacts: [construction audit](../analysis/theta-family-construction-audit.md), sections 5 and following; [fast-case audit](../analysis/theta-fast-case-audit.md); [script](../analysis/probe_theta_fast_case.py), [JSON](../analysis/theta-fast-probe.json).
- Global exclusion for s>beta: every compatible generator with a reducible bidirected hidden block is Q(a,b) up to hidden labels. Three singleton components cannot supply the signed beta residue. In a 2+1 split, only singleton s is possible: singleton beta has a signed residue, and singleton alpha would leave beta as the pair's dominant pole, also impossible. The residual alpha/beta pair has zero off-diagonal transfer at time zero, forcing opposite singleton visible incidence. Its first two Markov matrices and row sums pin all six rates. The singleton residue fixes its remaining rates.
- Extension: the same reducible-hidden rigidity holds for alpha<s<beta when a≤35sqrt(6)/88 or b≤sqrt(6)/4. The alternative pair would have zero-time transfer Zs+Zbeta with a negative entry, or one zero off-diagonal and the other positive at a threshold. Both are impossible for reciprocal visible incidence; simultaneous threshold equalities lie below alpha. No connected-hidden exclusion is implied.
- Rejected local-coverage shortcut: every theta source in alpha<s≤7 is exactly locally isolated. With L=s−7, M=s−11, D=LM−20<0, the positive dual (3,3/7,1,(Mb−5a)/D,1,(La−4b)/D,(33M/7−96)/D,(24L−165/7)/D) annihilates the rank-six tangent matrix. Minimal realization coordinates give the necessary continuity even where the exit chart is singular. This is an analytic certificate; it is not a newly executed parameter sweep or a global uniqueness proof.
- Further inference: any minimal five-state representative whose three hidden states form a triangle has unbounded entropy. Among three subsets of the two visible endpoints, two visible-neighbor sets are comparable. In the hidden triangle, their remaining hidden neighbor is shared, so E032's adjacent equal/nested-neighborhood construction applies. A potentially bounded distinct component in this region must therefore have a hidden path; a triangle alternative would already certify unboundedness.
- Target (a,b)=(100,100): the missing-rate derivative matrix has rank six and strictly positive left annihilator (3,1,1,53200/109371,7/3,133900/109371,1983/36457,4577/36457). The chart determinant is −882. Exact rational checks plus the normalized-sequence argument prove local isolation in generator space. Global uniqueness is not established, as E035 already shows why this reasoning would fail.
- Executed diagnostic: `python -B analysis/probe_theta_fast_case.py`, research run 2026-09-10T06:55:19.969603+00:00, Python 3.9.12, NumPy 2.0.1, SciPy 1.13.1. Thirteen starts, seed 20260911, six coordinates bounded by [-3,3], positive determinant floor 10^-4, margin in [0,2], maximum 400 SLSQP iterations per start. No positive complete witness was found; best returned margin is zero at the source. The local LP was infeasible, consistent with the exact certificate. Bound-clipping warnings and every status are retained. E044 records an unchanged replay after code consolidation; JSON records current source/helper hashes.
- Limit: optimizer success with zero margin and failed starts do not prove absence, entropy boundedness or uniqueness. The fast-case note supplies exact rational exit-triangle coordinates for a global feasibility proof, including sparse connected hidden supports. This is one targeted kernel, not an exhaustive graph or parameter search.

## E043

**Exact quadratic-field verification of the theta residue constructions**

- Kind: reproduced calculation. Artifacts: [standalone exact script](../analysis/check_theta_residue_construction.py), [complete JSON output](../outputs/theta-residue-checks.json). Command: `python -B analysis/check_theta_residue_construction.py` from the repository root.
- Latest successful execution: 2026-09-10T07:00:06.758392+00:00; Python 3.9.12, Windows, standard library only. Script SHA-256: `df7d9a893580d489ae94902b42e15337560d6926c6a50f681ec2fda9b4347b34`. The JSON records its environment and hash; all inputs are embedded and deterministic.
- Method: exact arithmetic in Q(sqrt(6)), with rational coefficient pairs and exact sign comparisons; exact Gaussian elimination, stationary laws and ten marked-kernel parameters. Five cases: (3,3); a=1 on the slow coincidence; the nonminimal exceptional point; a=3 on the fast coincidence; and a=1/10 on the slow line outside the direct coordinate thresholds. The last uses repeated-residue redistribution.
- Result: every candidate has zero row sums, nonnegative rates, reciprocal support, irreducible full graph, positive stationary law, and exactly equal Markov parameters at orders 0–9. This certifies all-time joint-kernel equality. Source and candidate ranks are (5,5), except (4,5) at the unique nonminimal point. Exact cone interval and normalization signs pass.
- Numerical illustration only: at (3,3), entropy changes from approximately 0.0428244845594 to 0.372313157659 in this new algebraic representative. It differs from the earlier complete Q* in E035; both are compatible. General unboundedness is proved by the subsequent pair construction in E041, not by these five finite entropy values.
- Limit: representative validation supports the algebraic construction; it is not a parameter enumeration or a proof of the unclassified complement. No new symbolic dependency, general inference framework or novelty claim.

## D009

**Keep the global gap; replace broad parameter search with one exact connected-support test**

- Date: 2026-09-10 UTC. Basis: E039–E043, preserving D007's warning against local-to-global inference.
- Outcome: the theta family now has exact minimality strata, broad constructive unbounded regions and complete coverage of both repeated-pole lines. The slow line proves that absence of a complete representative can coexist with unbounded entropy even when every compatible hidden graph is disconnected. Primary positive-realization theory reduces complete feasibility to a strict three-ray cone question but does not supply the missing fixed-order theorem.
- Rejected shortcut: local opening cannot cover the remaining low-exit coordinates automatically. Every source in alpha<s≤7 is locally isolated by a positive dual certificate; the construction memo records this obstruction. This is consistent with both the distant unbounded example and the still-unclassified complement.
- Single next action: settle exact connected-hidden feasibility for theta(100,100), using the rational global coordinates in the fast-case audit. Its reducible-hidden class is already unique, its source is exactly isolated, and a bounded thirteen-start probe found no complete witness. A global exclusion gives generator uniqueness; a hidden-triangle witness gives unboundedness; a hidden-path witness needs full boundary/component analysis before any entropy classification.
- Stopping rationale for this scoped investigation: the frontier check, exact exceptional-line analysis, constructive parameter theorems, failed-idea audit and reproducible checks are complete. The unresolved question now requires an exact global cone/support proof; repeating local tests, residue reassignment or bounded optimizer starts cannot decide it. The general bounded-nonunique five-state question and publication novelty remain unresolved. Leave the report and checkpoint ready for that distinct proof task; no commit or push.

## E044

**Maintenance review strengthens validation without changing the scientific results**

- Kind: reproduced calculations and bounded analytic review, 2026-09-10 UTC. Current reproducibility index: [analysis/README.md](../analysis/README.md).
- Correctness fix: [check_small_networks.py](../analysis/check_small_networks.py) previously accepted disconnected generators with a positive stationary law. Two disjoint bidirected pairs with uniform stationary mass are a counterexample. The validator now checks reachability and rejects this case in a focused negative control. Final script SHA-256: `1eb96cad1462049f19cbf32e301cb62e812a6ca663743577b0e5028579b48ab6`.
- Verification: all six `check_*.py` scripts passed before and after the fix in an isolated temporary copy, using Python 3.9.12, NumPy 2.0.1 and SciPy 1.13.1 as applicable. Scientific JSON contents matched the previous saved outputs after excluding execution metadata and the added negative-control flag. The five affected outputs were regenerated at 13:31:41–13:31:44 UTC; the standalone quadratic-field output was preserved because its source and dependencies were unchanged. Independent Decimal sign/arithmetic checks and matrix-exponential comparisons also passed during review.
- Pruned code: the two probes now share `search_complete` in [probe_theta_compatibility.py](../analysis/probe_theta_compatibility.py), preserving seeds, bounds, starts and solver settings. Both were replayed at 13:32:53 UTC with `python -B analysis/probe_theta_compatibility.py` and `python -B analysis/probe_theta_fast_case.py`. All 39 optimization results match their original values and statuses exactly, accounting for the standardized `hidden_determinant` field name. Warnings are recorded by both probes.
- Reproducibility fix: [.gitattributes](../.gitattributes) pins Python sources to LF on checkout so raw-byte checksums remain stable when Git's platform newline conversion is enabled. All current Python sources already used LF.
- Analytic review: no substantive algebraic error was found in the bounded review of the accumulated four-state, hidden-pair, splitting, sparse-five, path and theta proofs. The synthesis now states the one-observed-pair hypothesis where required and the fully-hidden-state condition for cloning. The next-step wording explicitly requires excluding hidden paths as well as triangles before claiming uniqueness. These are scope/clarity corrections, not new classifications. E023's proof locator now includes its decisive Section 6.
- Limits: successful checks and a bounded proof review do not establish publication novelty or resolve the remaining global five-state problem. Existing failed-search outcomes remain inconclusive.

## D010

**Review, prune and publish the accumulated research artifacts**

- Date: 2026-09-10 UTC. The user explicitly requests review, fixes, pruning, commit and push. This supersedes earlier research-run instructions to leave changes uncommitted; it does not authorize beginning a new scientific investigation.
- Scope: review the accumulated uncommitted artifacts, fix concrete validation and presentation issues, remove duplicate probe code and stale research bookkeeping, and preserve the human-owned brief and evidence IDs.
- Outcome: E044 records the irreducibility fix, exact replays, shared probe implementation, checkout-stable checksums and corrected assumptions. STATE.md and the report are shortened while detailed proofs and historical provenance remain available.
- Publication action: commit the reviewed state on the existing main branch and push normally to origin after validation. Do not rewrite remote history. The research handoff remains D009's global connected-hidden feasibility question.

## D011

**Resume the global fast-kernel question after the reviewed checkpoint**

- Date: 2026-09-10 UTC. The renewed autonomous-research brief reopens D009's unresolved question. The clean starting checkpoint is commit c4df036, already pushed under D010.
- Decision: retain the established formulation, frontier map and prior exact findings. Focus new work on global connected-hidden feasibility at theta(100,100), using independent hidden-path, spectral and invariant-cone approaches with a focused primary-literature check.
- Success criteria: a global exclusion, a certified distinct realization, or a rigorous reduction that removes an entire class of competing supports. Preserve failed approaches and distinguish finite numerical diagnostics from global certificates. Do not repeat the same bounded optimizer search or begin broad graph enumeration.
- Assignments: hidden paths in analysis/theta-fast-hidden-paths.md; spectral constraints in analysis/theta-fast-spectral-audit.md; fixed-order cone/NMF prior art in evidence/three-state-cone-frontier.md. Root owns global geometry, evidence IDs, checkpoint and synthesis.

## E045

**Primary rank-three factorization topology and rigidity constrain the frontier**

- Kind: primary results with separately identified interpretation. Retrieved 2026-09-10 UTC. Precise source locators, access limits and task mapping: [three-state cone frontier](three-state-cone-frontier.md), sections 1–2 and 4–5.
- Robert Krone and Kaie Kubjas, *Uniqueness of nonnegative matrix factorizations by rigidity theory*, SIAM J. Matrix Anal. Appl. 42(1), 134–164 (2021), [DOI](https://doi.org/10.1137/19M1279472), [full preprint v3](https://arxiv.org/pdf/1902.02868v3), dated 2 September 2020. Proposition 4.2, preprint p. 12, gives infinitesimal implies local rigidity. Proposition 5.3, pp. 19–20, puts a positive rank-r matrix on the relative nonnegative-rank-r boundary exactly when every size-r factorization contains a zero. Both propositions were inspected by the source auditor and coordinator.
- David Mond, Jim Smith and Duco van Straten, *Stochastic factorizations, sandwiched simplices and the topology of the space of explanations*, Proc. R. Soc. A 459, 2821–2845 (2003), [DOI](https://doi.org/10.1098/rspa.2003.1150); full author-hosted PDF linked in the memo. Theorem 2.4/Corollary 2.5, p. 2827, identifies factorizations with nested simplices modulo permutations. Theorem 4.9, p. 2842, bounds connected components by total polygon edges; section 5 exhibits eight isolated triangles between squares. Relevant full text was inspected by both auditors.
- Inference: neither disconnected factorization spaces nor the infinitesimal/local distinction is novel here. Static nesting does not enforce CTMC generator invariance. No inspected theorem supplies E048's quantitative global exclusion; that is not a novelty certification.
- Access limits: Cantó–Ricarte–Urbano (2006/2007) full realization hypotheses remain unverified beyond primary abstracts. Their algebraic “irreducible transfer matrix” is not hidden-graph irreducibility. The earlier Förster–Nagy strict-order gap remains. Do not infer a general three-state strict matrix theorem from these sources.

## E046

**Finite Hankel positivity cannot replace dynamical invariance**

- Kind: analytic inference and reproduced exact calculation, separated here. Artifact: [three-state cone frontier](three-state-cone-frontier.md), section 3, including the exact reproducer.
- For theta(100,100), uniformize the hidden block with gamma=218. Every finite block Hankel truncation O_m C_n of this hidden response admits strictly positive factors of inner dimension three. This does not concern the full marked kernel, whose minimal dimension is five. The explicit normalized signed similarity is U_epsilon=((1,epsilon,−epsilon),(epsilon,1,−epsilon),(0,0,1)). It opens the four zero entrance/exit entries; all higher shifted moments were already strictly positive, so sufficiently small epsilon works by continuity for each finite truncation.
- Every sufficiently large truncation has ordinary rank three, and E045 then places it in the relative interior of the nonnegative-rank-three set. Its static factorization is nonunique, despite global CTMC uniqueness from E048. No fixed positive epsilon in this construction works for all times: the transformed output's third column eventually becomes negative because the singleton mode decays faster.
- The hidden rate (U_epsilon^−1 H U_epsilon)_{hl}=epsilon(−197+194epsilon)/(1−epsilon²) is negative for 0<epsilon<1. Thus the positive finite factors do not define a physical CTMC.
- Exact check: the embedded Fraction calculation was executed by the source auditor and rerun by the coordinator at approximately 13:58 UTC, Python 3.9.12 and NumPy 2.0.1. At epsilon=1/100, all entrance/exit entries are positive and the offending hidden rate is −6502/3333. The formulas, rather than this one value, establish the general claim. Helper hashes are retained in the memo.
- Limit: this rejects static finite-Hankel positivity or rigidity as a substitute for generator constraints. It does not rule out finite derivative methods that explicitly retain the dynamics.

## E047

**Independent hidden-path support and polynomial exclusion at theta(100,100)**

- Kind: analytic inference with reproduced exact elimination. Artifact and embedded standard-library checker: [hidden-path audit](../analysis/theta-fast-hidden-paths.md).
- Among all 64 visible-incidence assignments on a three-hidden-state path, removing E032's immediately unbounded patterns and using the positive cross moment leaves four patterns up to path reflection. Two have an invisible middle and fail exact first-moment identities. The remaining two reduce to one endpoint exit rate in the nonsingular global exit chart.
- Exact reverse-edge numerators factor as u(u−3)P_x(u) and u(u−6)P_y(u), with degree-six residuals listed in the note. Descartes' rule excludes roots of P_x on the physical u>1 domain; all seven Bernstein coefficients exclude roots of P_y on 5<u<7. Denominators cannot vanish in a physical candidate. The surviving u=3 and u=6 reconstruct the disconnected source, not a hidden path.
- Inference: any connected hidden-path alternative would therefore trigger unbounded entropy. Together with the earlier triangle and disconnected-block results, this independently rules out bounded nonuniqueness at this kernel, but does not alone exclude every connected alternative. E048 supplies the stronger exclusion.
- Reproduction: the embedded checker regenerated the rational elimination, primitive coefficient lists, sign certificates, incidence reduction and source reconstruction. It passed for the auditor and coordinator; coordinator replay 2026-09-10 approximately 13:56:22 UTC, Python 3.9.12, standard library only. Direct rational matrix conjugation at two diagnostic points checks the missing-edge identities. No random or rate-grid input; approximate roots used during derivation were replaced by exact certificates.

## E048

**Global generator uniqueness for fast balanced theta kernels and an open region**

- Kind: analytic inference with focused reproduced exact arithmetic. Full proof: [spectral-cone audit](../analysis/theta-fast-spectral-audit.md), sections 1–8. Calculation: [check_theta_fast_spectral.py](../analysis/check_theta_fast_spectral.py), [JSON](../outputs/check_theta_fast_spectral.json).
- Result: with only resolved x↔y observed, exact joint kernels, simple bidirected irreducible CTMCs and at most five states, Q(100,100) is globally unique up to hidden labels. The same holds for every Q(z,z), z≥40, and the explicit open two-parameter sufficient region in equation (1). The generator and entropy are both identified. The numerical entropy at (100,100) is approximately 0.0755509024393 in the displayed inverse-time units, with k_B=1.
- Proof: for s>beta, the hidden transfer has three distinct nonzero rank-one modes and the full kernel has minimal dimension five. Any irreducible three-state hidden realization yields, by strict Perron eigenvectors, a finite invariant triangle in the normalized modal plane. It contains two specified input points, lies in a fixed output wedge, and contains the origin in its interior. Its vertices must have two positive heights and one negative height. Lower-edge invariance and input containment give mutually incompatible upper bounds, according to the sign of the negative vertex's horizontal coordinate. These inequalities exclude all connected hidden graphs, including paths and triangles, even allowing arbitrary nonnegative entrance/exit patterns.
- E042's disconnected-hidden rigidity then exhausts the admissible class. No local certificate, positive similarity assumption, optimizer failure, or finite sampling is used to prove nonexistence. The five-state cap is essential: one additional hidden state permits E028's unbounded cloning family.
- Generality: writing r_y=4(sqrt(6)−1)/5, A=a, B=b/r_y, m=(7+2sqrt(6))/5, k_L=(3−sqrt(6)/2)/8, k_R=35sqrt(6)/88 and kappa=(a+b−alpha)/(4sqrt(6)), sufficient conditions are s>beta and both (kappa−1)B>k_R[1+(A+1)/k_L] and (kappa−1)A>k_L[m+(B+1)/k_R]. The balanced z≥40 corollary follows from positive shifted quadratic coefficients, not a parameter sweep. Neither the region nor the constant 40 is asserted sharp.
- Reproduction: `python -B analysis/check_theta_fast_spectral.py`; coordinator execution 2026-09-10T13:56:22.080058+00:00, Python 3.9.12, standard library only. Script SHA-256 `192c0c5a37bdd40bf665f6346b639e02ad92cdd424010658d54afde5067c6c9b`; the output also records the unchanged quadratic-field helper hash. Modal identities, residues, source constraints/ranks, wedge bounds, strict margins at 100/40 and balanced-ray polynomial coefficients all pass.
- Entropy cross-check: section 8 of the proof records the exact stationary law and the formula [−11000 log(32/35)+19900 log(16/11)]/111741. At 14:04 UTC, direct Fraction substitution verified normalization, stationarity and both route currents. An independent NumPy 2.0.1 stationary linear solve and edge-flux sum agreed with the cycle-affinity expression to below 10^−13. This verifies the numerical illustration, not the universal uniqueness argument.
- Quality and limits: the coordinator checked the Perron orientation, exhaustive sign pattern, all lower/upper edge inequalities and the reducible completion. Agreement on this analytic method is not an independent empirical origin. E047 is a separate support-elimination check with a weaker conclusion. The result is an exact special-case theorem; the general five-state entropy classification, sharp theta boundary and publication novelty remain unresolved.

## D012

**Close the fast-kernel feasibility question and move to the remaining parameter boundary**

- Date: 2026-09-10 UTC. Basis: E045–E048. D011's exact target is settled globally; D009's proposed theta(100,100) test must not be repeated as an unresolved problem.
- Outcome: fast theta kernels supply an open region of global generator uniqueness, beyond the earlier diagonal-hidden and cap-saturating-path cases. Together with E041's unbounded regions this makes a sharper one-parameter classification a concrete next research problem. Static finite-Hankel factorization is an insufficient shortcut because it omits the generator constraint.
- Single next action: classify connected-hidden feasibility along Q(z,z) between the already proved unbounded interval and the sufficient uniqueness region. Retain the normalized Perron triangle and exact reciprocal-support conditions; eliminate its geometric variables or obtain an exact boundary witness. Any bounded-nonunique claim must still show different entropy values and control the entire compatible set.
- Stopping rationale: the renewed frontier assessment, exact global target, analytic extension and independent certificates are complete. Closing the remaining parameter gap requires a distinct global parameter-elimination or boundary-construction argument; repeating the completed searches, local tests or static NMF calculations cannot provide it. The full five/six-state program is not claimed complete. All bounded assignments returned artifacts and were incorporated. Preserve the new research locally for review; the earlier maintenance commit/push was already completed.
- Final consistency review: the new exact checker, embedded path certificate and finite-Hankel algebra passed. Local Markdown links, record anchors, stable IDs and saved source hashes resolve; the human-owned brief and operating instructions are unchanged. The report and state replace the now-settled target with the parameter-boundary action.

## E049

**Maintenance review clarifies the hidden-response scope and preserves the global proof**

- Kind: bounded analytic review and reproduced calculations, 2026-09-10 approximately 21:47–21:50 UTC. Reviewed E045–E048, their proofs, the new checker, report and current handoff; no new scientific investigation.
- Scope correction: the strict inner-dimension-three factorization result concerns finite block Hankel truncations of the **uniformized hidden response**, not the full marked kernel, whose minimal dimension is five. The report, frontier summary, E046 and STATE now state this explicitly. The detailed O_m C_n calculation was already correct; no mathematical conclusion changed.
- Analytic review: an independent reviewer checked Perron normalization, the exhaustive triangle vertex pattern, inequalities (9)–(14), the open region, balanced z≥40 bounds and reducible-hidden completion. No additional actionable proof error was found. Stationarity, route currents and edge-flux entropy independently give 0.07555090243930729. This is a bounded review, not a novelty assessment.
- Reproduction: `python -B analysis/check_theta_fast_spectral.py` was run in an isolated temporary copy of the Python sources. Its JSON is identical to the saved output except execution time; source hashes and scientific values match. The embedded hidden-path certificate and E046's Fraction calculation also passed with their documented commands. Python 3.9.12, NumPy 2.0.1 where used. Existing saved execution metadata was preserved.
- Pruning: removed three generated bytecode files and their analysis/__pycache__ directory after verifying its resolved path lies inside this repository. Preserved the ignored human prompt history and all reproducibility artifacts. Updated the stale README research target and shortened STATE. Human-owned PROJECT.md and framework instructions are unchanged.
- Repository checks: 375 local Markdown links, 117 anchors, 62 unique consecutive evidence/decision IDs and 24 saved source hashes pass. All Python sources parse and retain LF bytes; `git diff --check` reports no whitespace errors.

## D013

**Commit and push the reviewed global-uniqueness artifacts**

- Date: 2026-09-10 UTC. The user explicitly requests review, pruning, report cleanup, commit and push. This supersedes D012's instruction to leave the research changes local; the completed research remains finished.
- Scope: publish E045–E049, the global spectral proof and exact checker/output, independent hidden-path certificate, frontier assessment and updated synthesis. Retain provenance and historical limitations; exclude disposable caches and the human prompt log.
- Validation: focused replays, bounded proof review and repository consistency checks passed. Verify staged Python bytes before committing. Fetch/prune of origin succeeded, with main and origin/main initially identical at c4df036.
- Publication action: commit the reviewed artifacts on existing main and push normally to origin without rewriting history. The next scientific action remains D012's parameter-boundary question.

## D014

**Resume only the balanced-theta connected-hidden boundary**

- Date: 2026-09-10 UTC. The user's explicit next-loop instruction reopens D012's single next action after the infrastructure upgrade. PROJECT.md is unchanged; prior global theta(100,100) results are not reopened.
- Scope and success: classify connected-hidden feasibility for theta(z,z) in the gap between E041's constructive interval and E048's sufficient uniqueness region. Seek a sharp exclusion or exact boundary witness; otherwise preserve a rigorously improved parameter reduction with its unresolved interval. No general five-state bounded-nonunique assertion follows without controlling the entire fiber.
- Initial hypothesis, not a result: the local-opening threshold z_c=(11+sqrt(1120/11))/2 might be the global connected-hidden boundary. Falsification condition: some z>=z_c admits a five-state generator with the same full marked kernel, nonnegative paired off-diagonal support, irreducible full generator and connected hidden block. Numerical residual agreement supplies only a candidate; hidden similarity/exact derivative certificates and physical constraints must be checked exactly. A failed search cannot establish exclusion.
- Method: use the already derived finite Perron triangle and parameter algebra before heavyweight elimination. Root conducts focused global-coordinate exploration; bounded independent workers derive cone inequalities and analyze the endpoint. Record bounds, settings, failed attempts and exact checks separately. Preserve existing scientific outputs and the prior uncommitted infrastructure changes; no commit or push is requested.

## E050

**An exact complete realization crosses the balanced first-order threshold**

- Contribution labels: inference (analytic existence interval), reproduced calculation (exact witness and independent transfer identity). Mathematical status: conventionally proved interval and counterexample to D014's initial threshold hypothesis. Date: 2026-09-10 UTC.
- Statement: under the existing five-state-cap, resolved x↔y, exact joint-kernel and simple bidirected irreducible CTMC conventions, theta(z,z) has a complete compatible realization for every 2109/200≤z≤21091/2000. This interval contains z_c=(11+sqrt(1120/11))/2. Thus the strict first-order opening threshold is not the global connected-hidden feasibility boundary.
- Artifact: [boundary witness and proof](../analysis/balanced-boundary-witness.md); [exact checker](../analysis/check_balanced_boundary_witness.py); [output](../outputs/balanced-boundary-witness.json). A fixed rational row-normalized hidden similarity has positive determinant; every transformed off-diagonal is a strictly positive rational at both interval endpoints. Each rate is affine in z, proving the full interval. A separate SymPy determinant/adjugate calculation proves equality of all four hidden-transfer rational functions. Exact stationary laws and similarity are also checked.
- Mechanism: at z_c two missing rates open at first order, while six first-order-zero rates open at second order with an explicit correction. Three larger finite perturbation attempts produced negative rates and are preserved as unsuccessful attempts, not nonexistence evidence. The initial symbolic-expression comparison failure was corrected without changing the witness.
- Entropy implication: the complete triangle supplies an adjacent hidden-pair construction under E032, so the entropy fiber is unbounded on this interval. Mere generator nonuniqueness is not used for this implication.
- Verification: independent worker and coordinating-agent replay both passed using Python 3.9.12 and SymPy 1.14.0; command, environment and input/script hashes are in the output. No stochastic inputs, solver certification or formal verification. This small interval alone does not locate the global transition.

## E051

**Sharp upper boundary and a two-point entropy fiber at a minimal five-state kernel**

- Contribution labels: inference (global analytic exclusion and equality classification); reproduced calculation (independent exact path construction, kernel equality and entropy bounds). Mathematical status: conventionally proved within the stated model class, with independently reviewed argument and executed exact checks; not formally verified. Date: 2026-09-10 UTC.
- Result: let z_* be the unique positive root of P(z)=352z^4−3168z^3−4644z²−11340z−7623, approximately 10.5571496686650. For z>z_* the balanced theta generator is globally unique under the five-state cap. At z=z_* there are exactly two compatible generators up to hidden labels: the source and one connected-hidden path. The full kernel remains minimal of dimension five. Consequently its entropy fiber is a bounded two-point set, resolving the previously open existence question for a minimal five-state bounded-nonunique example, without classifying general five-state kernels.
- Global proof: [cone envelope and equality argument](../analysis/balanced-cone-bound.md), Sections 1–5; [main synthesis and endpoint construction](../analysis/theta-balanced-boundary.md). For z≥10.5, all finite Perron triangles satisfy a quadratic necessary inequality in t>0. Its discriminant is a negative positive-factor multiple of P(z). Above z_* it is strictly negative everywhere; at z_* its sole zero and strict envelope monotonicity uniquely force the triangle and all reciprocal zeros. The resulting possible support is a hidden path whose center sees x, one endpoint y, and the other x,y. The accepted disconnected-hidden rigidity (E041/E048) leaves only the source in that class. Thus all hidden supports, zero strata and models under the cap are controlled, not just a local component.
- Independent algebra: [path derivation](../analysis/derive_balanced_path.py), [full factorization](../analysis/balanced-path-polynomial.json), derived from the earlier exit chart with parameter z. Its physical quadratic in the y-only endpoint exit has discriminant −567(z−2)²(2z−3)²P(z), independently yielding the same quartic. Other factors and denominator exclusions are retained; this elimination is not used by itself to exclude other supports.
- Exact endpoint: [check_balanced_fold.py](../analysis/check_balanced_fold.py), [accepted output](../outputs/balanced-fold-checks.json). A normalized hidden similarity over Q(z_*) reconstructs the path with exactly seven reciprocal undirected edges. Exact row sums, physical signs, stationary laws and marked derivatives 0–9 pass. Number-field signs are checked by rational isolation of the selected positive root, not a coefficient-sign shortcut.
- Entropy separation: exact rational log-series remainder bounds give source entropy between 0.062946400236 and 0.062946400237, path entropy between 0.065579685966 and 0.065579685967, and a gap between 0.002633285729 and 0.002633285730. Units are inverse time with k_B=1. Therefore differing entropy is certified independently of the approximate matrix display. The log enclosure uses 24 positive atanh-series terms after powers-of-two reduction and an explicit geometric tail bound; 60/100-digit evaluations agree.
- Verification: coordinator audited the whole envelope chain; the independent boundary worker checked every geometric monotonicity/equality case and separately replayed the polynomial identities and full endpoint certificate. [Independent cone review](../outputs/balanced-boundary-cone-review.txt), [independent endpoint replay](../outputs/balanced-fold-independent-replay.json). Independent NumPy stationary/inverse and SciPy exponential checks agree; these numerical checks do not supply the universal exclusion. Both routes share the source formulation, not independent empirical data.
- Discovery and limits: [26-run bounded probe](../analysis/probe_balanced_boundary.py), [output](../analysis/balanced-boundary-probe.json), seed 20260910, retained 5 candidates meeting its positivity filter, best z≈10.557134405 with rate floor 1e−7. Failed starts and warnings remain recorded. That search does not prove the transition. At this checkpoint, sufficiency throughout the short interval immediately below z_* is still being completed. No novelty assessment was added; prior source-access limitations persist. A sixth state permits E028's unbounded splitting family.

## E052

**Subcritical complete realizations close the whole balanced entropy classification**

- Contribution labels: inference (analytic continuum construction and entropy deduction), reproduced calculation (exact rational interval bounds). Mathematical status: conventionally proved, independently audited and checked; no solver/formal certification. Date: 2026-09-10 UTC. This completes the subcritical step explicitly left pending in E051.
- Result: every 10.5≤z<z_* has a complete compatible five-state generator. Combined with E041's unbounded range 0<z<z_c, which overlaps this interval, and E051, the balanced entropy fiber under a five-state cap is unbounded for 0<z<z_*, exactly two finite values at z_*, and a singleton for z>z_*. Connected hidden support is not asserted everywhere below 10.5; the prior slow-pole obstruction remains intact.
- Proof: [cone note, Section 6](../analysis/balanced-cone-bound.md#6-sufficiency-below-the-fold-complete-compatible-generators). At t=−f1/(2f2), the exact positive discriminant gives strict upper-input slack below the quartic root. Rational outward interval arithmetic certifies the other geometric margins on the whole enclosing interval [10.5,10.55714966867]. Three sufficiently small changes open the bottom output, left output/tangency, and right tangency/input, preserving every other strict condition by continuity at each fixed z. No uniform perturbation size near z_* is assumed. The resulting strict invariant cone gives all-positive modal input/output and Metzler rates; the unique positive row normalization preserves the entire marked kernel.
- Entropy: the complete generator has adjacent hidden external twins; equality of their full external exit rows would imply a four-state lumping, contradicting minimality. E032's boundary theorem therefore supplies a valid divergent-entropy family. Feasibility alone is not used as an entropy-divergence certificate.
- Verification: [check_balanced_cone_sufficiency.py](../analysis/check_balanced_cone_sufficiency.py), [accepted interval output](../analysis/balanced-cone-sufficiency-checks.json). All 12 strict geometric checks and exact tangency identities passed with Python 3.9.12/SymPy 1.14.0. Coordinator and independent boundary auditor checked the perturbation directions, completeness of all face conditions, row normalization and entropy hypotheses. [Independent replay](../outputs/balanced-cone-sufficiency-independent-replay.json) agrees on all mathematical outputs. Independent replay files retain their execution-time source hashes; accepted cone outputs were refreshed after final explanatory edits to the note.
- Scope and limitations: this closes the saved balanced-parameter gap and proves a concrete bounded-nonunique minimal-five-state example. It does not classify general five-state networks or the full two-parameter theta family. Novelty remains unestablished. No scientific conclusion comes from absent numerical counterexamples, finite parameter sampling or a proof sketch alone.

## D015

**Finish the balanced boundary action with an exact two-point endpoint**

- Date: 2026-09-10 UTC. Basis: E050–E052 and D014's explicitly scoped resumption.
- Outcome: the initial local-threshold hypothesis was falsified, replaced by an exact quartic global threshold, with full connected-hidden exclusion above, a globally exhausted two-model endpoint with rigorously different entropy, and complete realizations/unbounded entropy below. The saved action has a defensible complete answer; further numerical searches in this interval cannot change the proved classification without exposing an error in its assumptions or proof.
- Stopping rationale: all support coverage, endpoint feasibility, entropy separation and interval sufficiency obligations are discharged and independently reviewed. The research brief and historical proofs remain preserved; no commit or push is requested. All bounded assignments are complete. The general five/six-state program is not marked solved.
- Reopening condition and next useful action: theorem-level prior-art comparison and further independent review of the finite two-point entropy theorem would address publication novelty and proof risk. New evidence, a concrete proof objection or a changed admissible class can reopen the boundary; do not repeat the already completed threshold search. Two-parameter classification and finite-data robustness are distinct future scopes.

## E053

**Publication review of the balanced-boundary result**

- Contribution labels: reproduced calculation (certificate replays), observation (repository review), inference (scope consistency). Date: 2026-09-10 UTC. This is maintenance verification of E050–E052, not a new research action or novelty assessment.
- Exact replay: copied the visible repository files to a disposable isolated workspace and ran `.venv/Scripts/python.exe -B` with `analysis/check_balanced_boundary_witness.py`, `analysis/check_balanced_cone_bound.py`, `analysis/check_balanced_cone_sufficiency.py`, `analysis/check_balanced_fold.py` and `analysis/derive_balanced_path.py`. All five passed. Their mathematical outputs exactly match the accepted JSON; differences are execution timestamps and the fold checker's absolute source-path key in the relocated workspace. Source bytes were identical. Python 3.9.12, SymPy 1.14.0, mpmath 1.3.0, NumPy 2.0.1 and SciPy 1.13.1.
- Independent review: the endpoint, exclusion, subcritical perturbations, entropy hypotheses and stated model scope revealed no new proof defect. A separate checker review found no certificate error and checked six rational log enclosures against 120-digit evaluations; those numerical spot checks supplement the rigorous remainder bound. Replaying the same certificates confirms reproducibility rather than providing an independent proof. The prior independent derivations and conventional arguments remain the proof basis.
- Corrections: clarified that the historical fast spectral checker covers the balanced tail z≥40, and that only the full two-parameter complement remains unclassified after the balanced slice was resolved. No theorem or entropy value changed. The infrastructure validation correction and its reproduced pre-fix failures are retained in the [capability audit](../docs/capability-audit.md#subsequent-publication-review-2026-09-10); capability tests are not scientific evidence.
- Provenance: accepted scientific outputs and earlier failed attempts remain unchanged. The older independent sufficiency replay retains its execution-time hash of the proof note, whose final explanatory edits postdate that replay as already recorded in E052. No failed numerical search or successful replay is treated as a proof of nonexistence. The research remains finished within D015's scope; formal verification and publication novelty remain unestablished.
- Repository validation and pruning: 522 local Markdown link paths, 145 anchors, all 53 evidence and 16 decision IDs, and Python syntax checks passed. All 22 staged Python files retain their exact working bytes; 59 recorded source/artifact hash references match staged checkout bytes, with only the documented historical note hash above differing. PROJECT.md, historical scripts and the prior evidence-record prefix remain unchanged. Removed the 110 disposable isolated-replay files after comparison; the ignored environment and human prompt history remain local. `git diff --cached --check` passed.

## D016

**Commit and push the reviewed boundary result and research stack**

- Date: 2026-09-10 UTC. The user's explicit “review prune commit push” instruction supersedes the earlier leave-local requests in D015 and the infrastructure audit. It authorizes maintenance and publication, without reopening the scientific investigation or changing PROJECT.md.
- Scope: publish the reviewed E050–E053 boundary proofs, certificates, preserved discovery failures and synthesis together with the lightweight scientific stack and optional uncompiled formal scaffold. Preserve prior evidence and human prompt history; remove only disposable replay files and caches.
- Basis: focused exact replays and independent review passed, with report wording and complex-input validation corrected. Fetch/prune of origin succeeded; existing main and origin/main both initially pointed to 621a309d04be125a86aea67a5eca2ebe391afd95.
- Publication action: verify links, provenance and staged bytes, commit on existing main and push normally to origin without rewriting history. The next scientific action remains D015's theorem-level prior-art comparison and independent review; publication does not expand the theorem's scope or proof status.
- Publication outcome: the reviewed changes were committed locally as `e7a1af4a80e80196885767d9da976f3330bffc5e`. Automatic approval review rejected `git push origin main`, citing possible disclosure of private research to an unverified external destination and requiring explicit authorization of the payload and destination. No push occurred. Read-only checks confirmed the configured/upstream destination is `git@github.com:cct1123/markov-thermodynamic-identifiability.git`, branch `main`; GitHub CLI/connector metadata were unavailable, and public API retrieval failed, so ownership/visibility could not be independently established. Required input: explicit confirmation to upload the reviewed research and infrastructure commits to that repository's `main`. After confirmation, retry the normal push and verify remote equality; do not reopen research or bypass the rejection.
