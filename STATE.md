# Current research state

Agent-maintained checkpoint, not a live process indicator.

- **Status:** finished — initial frontier-assessment run. The general classification and publication novelty remain unresolved.
- **Last checkpoint:** 2026-09-10 04:38:00 UTC.
- **Last completed action:** reviewed and pruned the research artifacts; exact and numerical checks passed again.
- **Current scope:** maintenance only, following the user's request to prune, commit and push. Preserve [PROJECT.md](PROJECT.md); do not restart research or broad N≤6 enumeration.

## Current answer

The [formulation](analysis/formulation.md) fixes joint waiting kernels for individually resolved, reverse-closed edges with known incidence, finite irreducible simple bidirected CTMCs, and single-channel state-level entropy. Cardinality, topology, minimality and rate restrictions define different compatibility classes. [D001](evidence/RECORDS.md#d001)

**Exact findings; novelty unestablished:**

- At most three states: one observed bidirectional edge identifies every rate. [E017](evidence/RECORDS.md#e017)
- Minimal four-state examples preserve every observed kernel while entropy covers [0,infinity), even on a fixed complete graph or diamond. [E019](evidence/RECORDS.md#e019), [E021](evidence/RECORDS.md#e021)
- Full-positive fixed diamond: distinct hidden escape rates identify the generator; equal escapes give an unbounded entropy fiber, including nonminimal cases. The data distinguish these strata. [E021](evidence/RECORDS.md#e021)
- [Reproducible checks](analysis/README.md) confirm the representative calculations. [E020](evidence/RECORDS.md#e020)

## Prior constraints and unresolved risk

Compatible-model optimization, hidden similarities and equilibrium/nonequilibrium ambiguity are established prior art. Closest constraints include Ehrich, Wagner–Timmer, Wu–Jia, Siekmann and marked-realization theory. [E004](evidence/RECORDS.md#e004), [E008–E012](evidence/RECORDS.md#e008)

Exact entropy-range classification is a plausible gap, not a certified open problem. Full theorem hypotheses remain unverified for Larget and the original Xiang reconstruction paper. [E007](evidence/RECORDS.md#e007), [E022](evidence/RECORDS.md#e022)

Minimality and topology alone do not classify entropy. Do not infer a universal unique/unbounded dichotomy from the examples. [D002](evidence/RECORDS.md#d002), [D003](evidence/RECORDS.md#d003)

## Next research action

Determine whether any **minimal four-state fixed-graph fiber has a finite non-singleton entropy range without a common positive lower rate cutoff**. Use the two-parameter hidden-similarity reduction in [compatibility-orbit.md](analysis/compatibility-orbit.md), impose generator positivity/support, and analyze boundary stationary fluxes.

The full diamond is already classified; begin with other topologies or other complete-graph fibers. An exact bounded example falsifies a proposed dichotomy; a rigorous divergent-boundary criterion could establish a classification. Numerical failure to find an example proves neither. Compare any prospective theorem with the closest prior art before claiming novelty.

## Resumption

The [report](outputs/REPORT.md) closes the initial frontier assessment with exact exploratory results and a discriminating next question. All bounded assignments are integrated; no worker remains active and no external blocker is pending. Resume at the action above, without repeating completed examples or assuming exhaustive coverage.
