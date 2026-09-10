# Current research state

Agent-maintained checkpoint, not a live process indicator.

- **Research status:** finished for the scoped investigation; the general five-state question remains unresolved. [D009](evidence/RECORDS.md#d009)
- **Last checkpoint:** 2026-09-10 13:36 UTC.
- **Maintenance:** user authorized review, fixes, pruning, commit and push. Six deterministic checks and both seeded probes passed; scientific results are unchanged. The shared validator now rejects disconnected generators. [E044](evidence/RECORDS.md#e044), [D010](evidence/RECORDS.md#d010)
- **Scope:** preserve PROJECT.md and prior evidence. Maintenance does not reopen the research investigation.

## Accepted answer

The [formulation](analysis/formulation.md) assumes finite irreducible simple bidirected CTMCs, even states, one channel per ordered pair, known resolved reverse-closed marks, and exact joint next-mark/time kernels. State count, topology and rate restrictions define different admissible classes.

- With **one observed pair**, at most three states identify all rates; exactly four states have only singleton or unbounded entropy fibers, including nonminimal realizations. A third-derivative criterion decides four-state uniqueness. [E030](evidence/RECORDS.md#e030)
- One spare fully hidden state guarantees unbounded entropy. The unrestricted-cardinality class has an observable unique/unbounded dichotomy. Hidden-pair, distinct-diagonal and cap-saturating-path results cover additional fixed-cap cases. [E028](evidence/RECORDS.md#e028), [report](outputs/REPORT.md)
- Five states admit a locally isolated generator with a distant unbounded component. The theta family has broad proved unbounded regions, including both repeated-pole lines; minimal points on the slow line have no connected hidden representation despite unbounded entropy. [E035](evidence/RECORDS.md#e035), [E039–E043](evidence/RECORDS.md#e039)

Proofs and exact representative checks are indexed in [analysis/README.md](analysis/README.md). Publication novelty is unestablished. Positive-realization and aggregate-equivalence theory are close prior art; the strict order-three cone question is not settled by the inspected theorem. Förster–Nagy's full strict-realization hypotheses, Larget and original Xiang results remain access gaps. [E040](evidence/RECORDS.md#e040)

## Single next research action

Decide exact connected-hidden feasibility at theta(100,100), using the rational global coordinates in the [fast-case audit](analysis/theta-fast-case-audit.md). Its disconnected-hidden alternatives are globally excluded and its source is exactly locally isolated. A thirteen-start search found no complete witness, which supplies no global bound.

Excluding **both hidden paths and hidden triangles** proves uniqueness. A hidden-triangle witness proves unboundedness; a hidden-path witness needs further boundary/component analysis. A bounded-nonunique claim must exhibit different entropy values and control the entire compatible set. [E042](evidence/RECORDS.md#e042)

## Handoff

Local isolation, pairwise rigidity and absence of a complete representative are not finite-entropy certificates. Do not assume a connected generator fiber or equate linear with positive realization order. [D007](evidence/RECORDS.md#d007), [D009](evidence/RECORDS.md#d009)

All bounded reviews are complete. No active research assignments or external blockers. Reopen research for new evidence, a global proof approach or renewed user instruction; repeating the same local tests or bounded searches cannot decide the remaining question.
