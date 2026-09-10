# Current research state

Agent-maintained checkpoint, not a live process indicator.

- **Research status:** finished for the saved balanced-theta boundary action. The general five/six-state program is not finished. [Report](outputs/REPORT.md), [D015](evidence/RECORDS.md#d015)
- **Last checkpoint:** 2026-09-10 23:29:31 UTC. Review, exact replays, repository checks and pruning completed; changes committed locally as e7a1af4. Automatic approval review rejected the push. [E053](evidence/RECORDS.md#e053), [D016](evidence/RECORDS.md#d016)
- **Scope:** D014 completed only D012's balanced parameter gap. The current action reviews and publishes that result and the research stack; it does not reopen research. PROJECT.md is preserved.

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

## Evidence and rejected shortcut

The initial hypothesis that the first-order threshold z_c≈10.54524979109513 was sharp was falsified by an exact rational complete witness on [10.545,10.5455]. A second-order opening explains the failure. [E050](evidence/RECORDS.md#e050)

The global cone envelope proves exclusion above z_* and uniquely forces the endpoint path. Exact interval margins and small strict vertex perturbations prove complete realizations throughout [10.5,z_*), overlapping the prior unbounded interval. The 26-run seeded search was discovery only; its failures are not nonexistence evidence. [Cone proof](analysis/balanced-cone-bound.md), [analysis index](analysis/README.md)

Prior results remain accepted: four-state singleton/unbounded classification, state splitting, theta unbounded regions and the open two-parameter uniqueness region. A sixth state makes this endpoint's entropy unbounded by splitting. The subcritical entropy classification does not assert connected hidden support on the exceptional slow-pole line. Local isolation, finite Hankel positivity and bounded rate closure remain insufficient shortcuts. [D007](evidence/RECORDS.md#d007), [D009](evidence/RECORDS.md#d009), [E028](evidence/RECORDS.md#e028), [E046](evidence/RECORDS.md#e046)

## Handoff and resumption condition

All review assignments are complete. Five exact boundary scripts replayed with matching mathematical outputs; historical scientific artifacts and failed attempts were preserved. Publication alone is blocked: automatic approval review requires explicit confirmation to upload the reviewed research and infrastructure commits to `git@github.com:cct1123/markov-thermodynamic-identifiability.git` on `main`. After confirmation, push normally and verify the remote; do not repeat research. [Publication decision](evidence/RECORDS.md#d016)

The saved boundary question is settled; do not repeat its search. If a new research run is authorized, the single most useful next action is **theorem-level prior-art comparison and further independent review of the exact two-point entropy theorem**, particularly finite positive-realization and aggregate-equivalence results. No new literature search occurred in this scoped continuation. General two-parameter classification and finite-data robustness are separate future scopes. Reopen this boundary only for a concrete proof objection, new contrary evidence or changed model assumptions. [D015](evidence/RECORDS.md#d015)
