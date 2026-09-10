# Thermodynamic literature: supplementary source notes

Inspected 2026-09-10 UTC. [RECORDS.md](RECORDS.md) holds the findings, publication metadata, and limitations; these notes retain additional equations, access details, and search leads. Source-reported calculations were not independently reproduced. PDF pages are one-based.

## Ehrich 2021 — E004

[Record](RECORDS.md#e004); [inspected v2 PDF](https://arxiv.org/pdf/2105.08803v2), sections 2–5, pp. 13–18, Eqs. (39)–(50), Fig. 8.

The stationary discrete-time model has bidirectional support, two individually visible states, and remaining states pooled into one hidden symbol. With two hidden states and nonsingular P(2), its complete jump kernel is P(n)=CH^(n−2)B. Two free entries of B parameterize C=P(2)B^−1 and H=BP(2)^−1P(3)B^−1; positivity selects physical models. Eq. (49) minimizes entropy over the family.

Section 4.1 reports maxima growing with grid refinement near nearly irreversible edges, rather than proving divergence. Section 5 leaves the effect of additional hidden states open. Section 3.4 proves unicyclic recovery under its topology assumptions.

## Skinner and Dunkel 2021 — E005

[Record](RECORDS.md#e005). For the [PNAS paper](https://math.mit.edu/~dunkel/Papers/2021SkDu_PNAS.pdf), inspected main-text pp. 2–3, Eqs. (2)–(3), “One-Step Estimator” and “Two-Step Estimator.” Supporting proofs were not separately inspected. The reported canonical reductions and finite hidden-state bound preserve selected macrostate transition counts; they do not establish a bound for arbitrary full waiting kernels.

For the [PRL paper](https://math.mit.edu/~dunkel/Papers/2021SkDu_PRL.pdf), inspected pp. 1–4, Eqs. (1)–(7). Eq. (3) uses full unconditional metastate dwell densities. The practical construction fixes two moments and reduces metastate B to one state under those constraints. The killed-subgenerator waiting density follows Eq. (5); its moment formula is Eq. (6).

## Nitzan, Ghosal and Bisker 2023 — E006

[Record](RECORDS.md#e006); [inspected v1 PDF](https://arxiv.org/pdf/2212.01783v1), sections II, III.A, III.B, III.D and IV; pp. 2–5, 10; Eqs. (7)–(19). Publisher metadata/references were accessible, but publisher PDF retrieval failed; locators refer to the preprint.

Variables are stationary masses and fluxes n_ij=pi_i w_ij, subject to conservation on the hypothesized topology. Eq. (16) fits coarse stationary probabilities, one-/two-step fluxes and full conditional dwell densities psi_IJK(t); Eqs. (17)–(19) replace functional equality with moments. Section IV leaves universality of the observed simpler-topology bounds open.

## Harunari and collaborators — E014

[Record](RECORDS.md#e014). The [2022 v2 PDF](https://arxiv.org/pdf/2203.07427v2), sections II–III, pp. 2–5, Eqs. (4)–(14), uses individually resolved edges and reverse-closed observations. Repeated and alternating event statistics carry different information; the entropy statement includes ring and fully observed cases.

The [2024 v3 PDF](https://arxiv.org/pdf/2402.00837v3), sections III.C and VI, pp. 6 and 11, Eqs. (24)–(27), treats pooled event labels. Its exact construction assumes finitely many equal-affinity cycle families, each unambiguously identified by a minimal observed sequence. Eq. (26) recovers family affinities; Eq. (27) combines all relevant affinities and cycle currents. An arbitrary partial sum need not be a lower bound.

## Time-reversal exchange — E013

[Record](RECORDS.md#e013) supplies all three titles and DOIs.

- Martínez et al. (2019): [inspected author PDF](https://sites.lsa.umich.edu/horowitz-lab-new/wp-content/uploads/sites/1181/2020/01/s41467-019-11051-w.pdf), pp. 2–4, Eqs. (1)–(9). Eqs. (2)–(4) split semi-Markov trajectory KL; Eqs. (5)–(6) address second-order observations.
- Hartich–Godec (2024): [inspected comment](https://d-nb.info/1352118998/34), pp. 1–2, “Counterexample,” Eqs. (1)–(4), “Crucial elements.” The last-observed-state description can produce spurious coarse irreversibility from equilibrium dynamics.
- Bisker et al. (2024): [inspected reply](https://d-nb.info/1352064391/34), pp. 1–2, Eqs. (1)–(4), Fig. 1. It distinguishes coarse-graining a reversed trajectory from reversing a coarse trajectory, with commuting maps sufficient for equality.

These are one exchange about the observation/reversal operation, not independent evidence against the resolved-edge formulation.

## Tian 2026 — E015

[Record](RECORDS.md#e015); [inspected v2 PDF](https://arxiv.org/pdf/2605.02650v2), introduction and sections II–V, especially pp. 4–5, propositions 2–3 and Eqs. (28)–(34). Some indexed results retain the earlier title *Thermodynamic Completeness in Markovian Dynamics*.

The state generator is fixed. Proposition 2 characterizes uniqueness of linear mean records D j when D annihilates the channel-redistribution kernel of P; proposition 3 uses convex hulls of channel increments. The physical transport constructions were not independently validated here. This preprint concerns channel allocation, a different hidden variable from the generator in this project.

## Citation tracing and deferred leads

Searches covered author/title citation trails, full-WTD optimization, hidden reconstruction, entropy non-identifiability/unboundedness, and 2024–2026 follow-ups. This was a bounded search, not novelty certification. The Maier papers and Wagner–Timmer lead were subsequently integrated into [E002](RECORDS.md#e002), [E003](RECORDS.md#e003), and [E008](RECORDS.md#e008).

The following received **abstract-only screening** and support no theorem claims here:

- *Entropy estimation for partially accessible Markov networks based on imperfect observations*, PRE 111, 044106 (2025), [DOI](https://doi.org/10.1103/PhysRevE.111.044106): finite-resolution/sample-error extension.
- *Compensating Random Transition-Detection Blackouts in Markov Networks*, PRL 136, 247101 (2026), [DOI](https://doi.org/10.1103/p8yf-12yz): missed detections and short-time inference.
- *Counterexamples to the conjectured ordering between the waiting-time bound and the thermodynamic uncertainty bound on entropy production*, [arXiv:2601.04039](https://arxiv.org/abs/2601.04039): relevant if comparing estimator orderings. No universal ordering is assumed here.

The current research question and next action are maintained in [STATE.md](../STATE.md), rather than duplicated in this source note.
