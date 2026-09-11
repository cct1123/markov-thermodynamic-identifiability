# Paper structure: exact entropy fibers and observational stability

2026-09-11 UTC. **Verdict 1: ready for manuscript preparation**, with narrowly stated candidate originality. This is a proof/figure plan, not a manuscript draft or an acceptance forecast. Definitions and theorem numbers refer to [publication-theorems.md](../analysis/publication-theorems.md). The [report](REPORT.md) gives the audit decision and remaining risks.

## Central claim and scope

Working title: **Exact entropy fibers and instability in partially observed Markov networks**.

The contribution has two linked parts: an explicit full entropy identified set with exactly two values under a five-state cap, and a sharp criterion for whether an entropy upper ceiling survives any positive observation tolerance at fixed state count. The physical model is a finite simple bidirected CTMC with one known resolved observed pair and stationary even-state entropy. Unknown topology, absolute joint waiting laws and the absence of a reverse-rate floor must appear before the headline results.

The three-state example is a minimal explanation of the distinction, not the sole novelty claim. It shows that entropy can diverge while the physical generator inverse is locally Lipschitz. At four or more states, the general hidden-pair construction defeats local upper ceilings even for a complete source. This separates a singular entropy functional at sparse microscopic boundaries from hidden observational ambiguity near full-support generators.

## Main text sequence

1. **Question and definitions.** Introduce the observation map and the physical entropy functional, then the generator fiber, entropy identified set and robust upper envelope. Explain what exact identifiability does and does not mean. Fix C_N versus C_<=N and the TV/weak row-law topologies. State the full theorem outcomes immediately. Limit motivation to entropy inference with unresolved jumps; no claims about a universal measurement impossibility.
2. **Observation equivalence as a constrained realization problem.** Prove or briefly derive T1 and the pinned hidden similarity. Credit the full positive-HMM and MAP precedents. Include one diagram of the reset geometry. Explicitly require transformed offdiagonals and reciprocal zeros; a canonical realization is not the entire physical fiber.
3. **A finite, nontrivial exact entropy fiber.** State T3 for the balanced family and the exact quartic. Show source and alternative supports, the certified entropy intervals and the unbounded/two-point/unique transition. Prove enough of the global logic in the main text to make the count credible: minimality, connected versus disconnected hidden support, the invariant triangle and its unique equality configuration. Put the longer inequality verification and algebraic coordinates in appendices. Say “smallest cap” only with the supporting four-state classification included.
4. **Stable rate recovery does not ensure stable entropy.** Present T2's three-Laplace reconstruction, with the source-fixed branch at leaf data. Give the unit triangle as the positive regime and the fixed-trace tree-to-triangle sequence as the negative regime. Establish the exact current/affinity formula and e sigma->1/3 analytically; distinguish the fixed-e reverse-rate limit from the diagonal convergence path. Attribute the general logarithmic/relative-entropy singularity to prior work.
5. **A general stability classification.** Prove T5 by complete perturbation at fixed trace, followed by exact hidden-pair mixing; show why the order of limits is valid. Then state and prove T6: finite local upper ceilings exactly for N=2 or complete N=3. This supplies general significance beyond the special quartic example. Include the tight-cap counterexample to delimit the theorem.
6. **Finite records and regularity assumptions.** State the stationary coupling consequence and T7 as an application of established confidence-impossibility theory. Keep the finite-window experiment distinct from the joint-kernel topology. State the positive-floor/activity-ratio sufficient bound, crediting stronger known bounds. The cap-free stationary-window positive result remains open; it is not needed by the paper.
7. **Discussion of what is established.** Explain implications for interpreting exact inverse fits and upper thermodynamic limits. Discuss known topology, spare states, rate-ratio information and resolved thermodynamic channels. End with concrete scope limits and the remaining off-balanced classification, without claiming a general five/six-state solution or a new theory of identifiability versus stability.

## Theorem dependency sequence

| Paper theorem/lemma | Existing exact content | Proof location and obligation |
| --- | --- | --- |
| Lemma 1: observation and minimal orbit | T1 | Standard basis proof and normalization; clearly credited. |
| Theorem 1: exact balanced entropy fiber | T3 | Assemble the global cone proof, disconnected-support exhaustion, endpoint existence and certified separation into one argument. |
| Proposition 2: minimum order for bounded nonuniqueness | Earlier <=4 dichotomy plus T3 | Include the complete nonminimal-aware four-state argument in an appendix; omit a minimal-order headline if that appendix is dropped. |
| Theorem 3: finite-Laplace inverse and positive-triangle regularity | T2/T2a | Short Schur complement and rational recovery proof; no differentiation-continuity shortcut. |
| Proposition 4: sparse generator entropy boundary | T4/T4a | General missing-edge proof followed by the simplest unit-tree example. |
| Theorem 5: two-hidden-state neighborhood unboundedness | T5 | Unequal-exit pair lemma, fixed-trace completion, exact-law preservation and two-limit selection. |
| Corollary 6: sharp fixed-N ceiling criterion | T6 | Exhaust N=2, three-state triangle/tree, and N>=4. |
| Corollary 7: uniform finite-record upper limits | T7 | State precise experiment/coverage, cite the general statistical antecedent, and apply the physical sequence. |

## Figure specifications

| Figure | Exact scientific purpose | Inputs and safeguards |
| --- | --- | --- |
| 1: two endpoint networks and common observation | Make the whole-fiber result tangible: source has six reciprocal edges, alternative seven; only x-y is observed. Show two disjoint entropy intervals. | Exact source/path from `balanced-fold-checks.json`; rounded rates labeled illustrative. Shared kernel equality is certified algebraically, not by overlaying sampled curves. |
| 2: balanced parameter classification and cone tangency | Display unbounded, two-point and unique regimes, with the unique equality triangle at z_*. | Quartic and exact cone coordinates. Use symbolic region annotations, not a sampled maximum curve. Any subcritical finite plotted branch is only an example inside an unbounded fiber. |
| 3: uniquely identified but divergent three-state family | Show paired-zero chord opening; plot e sigma against e tending to 1/3 and the analytic TV bounds tending to zero. | Exact fixed-trace formula, arbitrary precision where needed; each plotted model remains bidirected. Rate cap one and trace -4 printed. Numerical plot illustrates an already proved limit. |
| 4: stability classification by state count/support | Compare entrywise-generator continuity with observation-level upper boundedness; highlight complete N>=4 sources as different from positive triangles. | T4/T6 table and one concise construction diagram. Label fixed N and unknown topology; annotate that an arbitrary extra tight cap can change the answer. |

No additional Monte Carlo panels, graph sweeps or new empirical examples are needed for this theorem paper. All final exported figures should be generated by standard plotting/vector tools from the exact accepted artifacts.

## Appendices and reproducibility package

- **A: definitions and linear lemmas.** Full matrix-valued Markov renewal relation, finite derivative certificate, minimum-order argument and stationary marked-path likelihood identity.
- **B: complete four-state obstruction.** Fixed/unknown-support classification including nonminimal cases, used only to justify smallest-cap language. The observable third-derivative test can be placed here or in supplementary material.
- **C: global invariant triangle.** Modal/Perron normalization, exhaustive vertex signs, all denominator domains, both bottom-abscissa cases, monotone envelope and equality implications. State crossover uniqueness only on the physical domain.
- **D: independent endpoint and entropy certificate.** Path-coordinate elimination, retained extraneous factors and excluded denominators, root isolation, exact support, stationary vectors and logarithm-series error bounds. Include the independent cone-to-path equality check.
- **E: subcritical covering and exceptional parameters.** Show the overlapping intervals and separate repeated-pole constructions; do not silently infer completeness at the slow coincidence.
- **F: hidden-pair and perturbation lemmas.** General unequal external rows, first physical boundary, positive limiting stationary masses, fixed-trace completion and Duhamel/coupling bounds.
- **G: stability/statistical details.** Rational inverse branches, leaf boundary, confidence quantifiers, tight-cap and ratio-only counterexamples, and the support-stability condition for a compact inverse range.
- **Reproducibility supplement:** pinned environment, exact root-relative commands, script/output hashes and read-only replay commands. Clearly separate discovery probes from certificates. Preserve historical failed ideas in the repository; the paper needs only failures that clarify a mathematical distinction. No formal-verification claim: the Lean scaffold remains uncompiled.

## Prior-work positioning and journal scope

The main comparison must credit finite factorization alternatives (Mond et al.), full positive-model equivalence (Vanluyten et al., Horváth–Telek), invariant PH polytopes (He–Zhang), aggregated hidden nonequilibrium (Wagner–Timmer, Siekmann, Ehrich), resolved-transition inference, relative-entropy singularities (Zeraati, Sason–Verdú), rate-ratio upper bounds (Nishiyama–Hasegawa), and the statistical impossibility antecedent (Moss). The two [novelty memos](../evidence/publication-realization-novelty.md) and [thermodynamic comparisons](../evidence/publication-thermodynamics-novelty.md) give source versions, exact locators and the mathematical differences. Do not claim a first finite positive realization, a new KL singularity, or generic marked-process identifiability.

**Initial journal scope: a regular research article in Physical Review E, statistical physics/stochastic processes.** This is a scope judgment based on its [current journal description](https://journals.aps.org/pre/about) and [section-selection guidance](https://journals.aps.org/authors/guidelines-section-selection-physical-review-e), inspected 2026-09-11. The physical inference question and exact stochastic-network theorems fit that stated remit. Keep the rigorous global proof available through appendices; a short Letter would force removal of material essential to assessing the claim. Journal fit does not predict acceptance. A mathematics-first venue can be reconsidered after the proof core shows its length; no unverified journal metrics or acceptance estimates are used.

## Single next action

Assemble the **self-contained theorem-and-proof core for Theorem 1 and Corollary 6**, following the dependencies above, with a compact primary-work comparison attached. Its completion condition is that a reader can verify the two-point exhaustion and all-N ceiling criterion without reconstructing the research chronology. Include every exceptional case and explicit counterexample. This is the highest-value preparation for expert scrutiny; no unrelated generalization or polished introduction is required first. No external contact, commit or push has been authorized.
