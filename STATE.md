# Current research state

Agent-maintained checkpoint, not a live process indicator.

- **Research status:** finished at the current verified frontier; further broad work in the completed directions has low expected value. The general five/six-state program and publication novelty remain unresolved. [Report](outputs/REPORT.md), [stopping decision D020](evidence/RECORDS.md#d020)
- **Last research checkpoint:** 2026-09-11 00:04 UTC (2026-09-10 America/Chicago). Completed prior-art comparison, the general robustness theorem, the smallest fixed-trace counterexample and the one-hidden-state stability classification; independently verified and saved E054–E058. Final link/provenance checks and temporary-file cleanup passed.
- **Publication review:** 2026-09-11 00:48 UTC. The user's subsequent “commit and push” authorizes publication to the configured `origin/main`, superseding the research run's no-publication instruction. Both new checkers reproduced their accepted outputs without changing them. This is maintenance; research remains finished. [D021](evidence/RECORDS.md#d021)
- **Scope:** preserve PROJECT.md, historical proofs and the saved scientific next action. Publication status is recorded by Git history and the upstream reference; no new investigation is authorized by the maintenance request.

## Accepted answer

Under the [formulation](analysis/formulation.md)—irreducible simple bidirected row CTMCs, even states, one channel per ordered pair, known visible endpoints, only resolved x↔y observed, exact joint next-mark/time kernels, and at most five states—let z_* be the unique positive root

**352z⁴−3168z³−4644z²−11340z−7623=0**, with z_*≈10.5571496686650.

| Balanced theta(z,z) parameter | Entire entropy fiber |
| --- | --- |
| 0<z<z_* | Unbounded above |
| z=z_* | Exactly two distinct finite values |
| z>z_* | Singleton; generator globally unique |

At z_*, exactly two generators exist up to hidden labels: the source and one connected hidden path. Their entropy rates lie in the certified intervals **[0.062946400236, 0.062946400237]** and **[0.065579685966, 0.065579685967]** in the displayed inverse-time units, k_B=1. This establishes existence of a minimal-five-state bounded-nonunique example. [Main proof](analysis/theta-balanced-boundary.md), [E051](evidence/RECORDS.md#e051), [E052](evidence/RECORDS.md#e052)

Confidence rests on global analytic support exhaustion, an independently derived matching quartic, an exact algebraic endpoint with ten marked derivatives, rigorous rational entropy bounds, and independent proof/code review. This is conventionally proved and computationally checked, **not formally verified**. Publication novelty is unestablished; prior source-access gaps remain.

**New robustness theorem:** at any source with two fully hidden states, every positive joint-kernel TV neighborhood contains arbitrarily high finite entropy at the same state count, observed rates and exact trace. All rates share a finite cap. Under stationary finite-horizon sampling, any modelwise uniformly valid upper confidence limit must be infinite with probability at least its coverage at the source. This includes exactly identifiable and finite-fiber sources. [General proof](analysis/entropy-neighborhood-audit.md), [explicit checked witness](analysis/finite-precision-instability.md), [E055](evidence/RECORDS.md#e055), [E056](evidence/RECORDS.md#e056)

**Smallest counterexample:** a minimal-three-state equilibrium tree is approached by uniquely identified triangles with exact trace −4, all rates at most one and entropy asymptotic to `1/(3e)`. This preserves source order. In contrast, strictly positive three-state triangles have locally continuous entropy under a common rate cap. The sparse failure is entropy discontinuity, even though the generator inverse remains continuous. [Fixed-trace proof](analysis/three-state-fixed-trace-audit.md), [local classification](analysis/one-hidden-robustness-audit.md), [E057](evidence/RECORDS.md#e057), [E058](evidence/RECORDS.md#e058)

Assumptions: unknown competitor topology, no positive reverse-rate floor, fully resolved marks, and uniform finite-sample coverage for the statistical statement. Local continuity does not imply a globally honest almost-surely finite confidence limit. Exact identities, independent stationary solves, coupling and compactness supply the evidence; numerical convergence alone does not prove the results.

## Evidence and rejected shortcut

The initial hypothesis that the first-order threshold z_c≈10.54524979109513 was sharp was falsified by an exact rational complete witness on [10.545,10.5455]. A second-order opening explains the failure. [E050](evidence/RECORDS.md#e050)

The global cone envelope proves exclusion above z_* and uniquely forces the endpoint path. Exact interval margins and small strict vertex perturbations prove complete realizations throughout [10.5,z_*), overlapping the prior unbounded interval. The 26-run seeded search was discovery only; its failures are not nonexistence evidence. [Cone proof](analysis/balanced-cone-bound.md), [analysis index](analysis/README.md)

Prior results remain accepted: four-state singleton/unbounded classification, state splitting, theta unbounded regions and the open two-parameter uniqueness region. A sixth state makes this endpoint's entropy unbounded by splitting. The subcritical entropy classification does not assert connected hidden support on the exceptional slow-pole line. Local isolation, finite Hankel positivity and bounded rate closure remain insufficient shortcuts. [D007](evidence/RECORDS.md#d007), [D009](evidence/RECORDS.md#d009), [E028](evidence/RECORDS.md#e028), [E046](evidence/RECORDS.md#e046)

## Current uncertainty and next action

The primary-source comparison is complete within its bounded scope. Finite positive-realization fibers and general confidence-set impossibility are known antecedents. Only the specific physical entropy statements remain potential contributions. Missing originals and the lack of a matching located theorem do not establish novelty. [E054](evidence/RECORDS.md#e054), [positioning](evidence/two-point-entropy-positioning.md)

**Single best next action:** obtain Larget's original canonical-equivalence theorem through a genuinely new accessible route, starting from the exact preprint leads in the [finite-fiber audit](evidence/finite-fiber-prior-art.md#outstanding-original-source-gap-larget), and compare its physical positivity, order, observation and exceptional-fiber assumptions directly against E051. A matching full physical-fiber result would alter the publication claim. Do not equate canonical uniqueness with physical uniqueness or treat failed retrieval as absence. [D020](evidence/RECORDS.md#d020)

**Main risk:** publication novelty; general realization finiteness and confidence-set impossibility are already known, and the three-state sparse entropy discontinuity is not specific to hidden observation. Only the precise physical theorem combination is a candidate contribution. Broader exact classification needs new global insight; repeated threshold searches and additional unmotivated examples are not the next action.

All bounded assignments are complete and incorporated. Two new root checkers and separate embedded replays passed; source hashes, links, historical evidence and the human brief were checked. Failed algebra/extraction/retrieval attempts remain in the linked notes. No research work is running. D016 and the no-publication outcome in D020 describe earlier requests; D021 records the subsequent publication authorization.
