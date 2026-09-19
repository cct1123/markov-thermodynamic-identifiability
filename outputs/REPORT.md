# Research synthesis — observation coverage and entropy fibers

19 September 2026. **Observation coverage controls exact entropy identification at complete networks and finite local upper ceilings.** The completed research loop extends the previous one-pair criterion to arbitrary nonempty reverse-closed sets of resolved microscopic transitions. Competitors use the same known labeled vertex set, irreducible reciprocal dynamics and unknown unobserved support. Full joint next-mark/time laws retain absolute amplitudes. [Theorems and proofs](novelty-loop-2026-09-19/COVERAGE-THEOREM.md).

The results have conventional proofs, independent mathematical review and exact computational support. No outstanding mathematical finding remained in the bounded final audit; the entire earlier five-state cone proof was not recertified. Formal verification and publication priority remain unestablished. [Review](novelty-loop-2026-09-19/REFEREE.md), [E081](../evidence/RECORDS.md#e081).

## What the new theorem establishes

| Source and coverage | Exact identification | Finite local entropy ceiling |
| --- | --- | --- |
| Complete; at most one uncovered vertex | Generator unique; two positive full Laplace matrices suffice | Exists |
| Complete; at least two uncovered vertices | Exact entropy image contains [sigma(source), infinity), even at fixed observed rates and trace | Does not exist |
| Sparse; at most one uncovered vertex | Generator recovered from at most three positive full Laplace matrices | Does not exist with unrestricted unknown support |
| Sparse; at least two uncovered vertices | General exact fiber remains unclassified | Does not exist with unrestricted unknown support |

When observed rates and trace are fixed, **zero total unobserved rate is an exception**: the constrained class is a singleton. Otherwise the same criterion holds. At complete N-state networks, the sharp observation minimum is floor(N/2) reverse pairs arranged to cover at least N-1 vertices; a matching attains it. Fixed sparse support, extra hidden states, additional tight rate constraints and blurred marks require separate statements. [E083](../evidence/RECORDS.md#e083).

## Finite measurements and a sharp counterexample

With one uncovered vertex, a scalar hidden-pole identity gives a rational inverse from any three positive full Laplace matrices. Two suffice when an observed edge joins two neighbors of the hidden vertex, including every complete source. Nonzero source denominators give local Lipschitz dependence on bounded measurements and row TV, and continuity for weak row-law convergence, without a common rate cap. [Inverse](novelty-loop-2026-09-19/COVERAGE-THEOREM.md#2-finite-inverse-and-denominator-audit).

For every N>=4, any prescribed two positive arguments admit distinct entropy rates despite identical measured matrices. The four-state witness at arguments 1 and 2 has entropy rates log(2)/17 and 6log(2)/97; its matrices differ at 3. Symbolic interpolation and observed leaves prove the arbitrary-argument and larger-N extensions. This is finite-summary ambiguity, not full-law equality, and does not contradict the earlier at-most-three-state result. [E082](../evidence/RECORDS.md#e082).

## Mechanism, attempted falsification and independent checks

The exact divergent path uses a hidden shear for unequal external exit rows and fixed-sum internal rates in a lumped pair for equal rows. These cases exhaust complete sources, including nonminimal ones. All-time marked kernels, observed rates and trace stay fixed while a rate vanishes against a positive opposing stationary flux. Continuity gives the attainable entropy half-line. The reversible unit-rate four-state source has exact image [0,infinity), with trace -12 and rates below 2 throughout the exhibited path.

Two provisional extensions were rejected: full hidden incidence is insufficient when a covered-covered pair is missing, and the calibrated criterion needs the zero-budget exception. Independent checks cover twelve sparse/complete reconstructions at N=4,5,6, full-mark entropy witnesses, arbitrary-sample interpolation, equal-exit lumping, an internal-first shear boundary and all observation sets through N=6. Universal statements rest on the proofs, not the finite checks. [Independent analysis](novelty-loop-2026-09-19/ONE-HIDDEN-INDEPENDENT.md), [reproduction commands](../analysis/novelty_loop/README.md), [current verification](novelty-loop-2026-09-19/verification.json).

## Novelty assessment and improvement plan

Burgarth substantially anticipates bare all-time one-hidden recovery. Hidden thermodynamic ambiguity, normalized similarity and the one-way entropy singularity also have established antecedents. The stronger candidate contribution is the combined coverage classification, universal complete-source exact divergence, finite-measurement sharpness and observation-design consequence. The bounded primary audit found no matching full theorem; detailed finite-frequency/Loewner comparison remains incomplete. [Primary comparison](novelty-loop-2026-09-19/LITERATURE.md).

All three planned rounds are complete. [Executed plan](novelty-loop-2026-09-19/PLAN.md), [D035](../evidence/RECORDS.md#d035). Next priorities are:

1. Complete finite-frequency attribution and integrate the reviewed addendum into the article.
2. Quantify conditioning and select observation pairs and transform arguments among coverage-sufficient designs.
3. Investigate exact entropy lower ranges. The finite-union-of-intervals/points route remains a proposed next theorem.

A matching prior theorem or a counterexample under the stated assumptions would change the assessment. Additional generic examples would not resolve these remaining questions.

## Preserved earlier results and delivery status

The five-state threshold still has two distinct entropy values at its endpoint and a unique generator above it; below it only an attainable half-line is proved. Compact-prior maxima, sequential finite-n moment coverage and rare-rate examples retain their earlier scopes. [E071](../evidence/RECORDS.md#e071), [E073](../evidence/RECORDS.md#e073), [E074](../evidence/RECORDS.md#e074). The preceding synthesis remains in [commit c7ff789](https://github.com/cct1123/markov-thermodynamic-identifiability/blob/c7ff789b2e9db090935b5bf16eb9a8d775f833c2/outputs/REPORT.md).

The new result is a separate research addendum. The [56-page manuscript](../manuscript/main.pdf) and [reproduction archive](manuscript-package.zip) retain the preceding version. Their historical tests and 900-trajectory campaign were not rerun in this cycle. Human-owned inputs and accepted scientific outputs are preserved. All bounded assignments are complete; no journal submission or recurring automation was performed.
