# Supplied counterexample review and pruning

The supplied counterexample is valid and was already incorporated in commit `35239eb`. It does not contradict the current triangle reconstruction, three-point generator recovery, or full-law results. Its two generators share two Laplace matrices but both have entropy zero.

The additional conclusion in the supplied JSON is correct under the manuscript's reciprocal, connected **at-most-three-state** class: two distinct positive full Laplace matrices identify entropy. A nonzero off-diagonal of `M=(P Psi_hat)^(-1)` forces complete support and unique two-point generator reconstruction. Otherwise every compatible model is a tree or two-state chain, and stationarity across each edge cut forces zero current and zero entropy. The manuscript now states this as a conventional corollary. The result assumes resolved microscopic reverse marks and absolute timing; it supplies no entropy continuity at tree boundaries.

The JSON's “cross entries” must mean the off-diagonals of **F=P Psi_hat**, equivalently M. The original mark-ordered Psi_hat has positive cross entries even for trees. This convention is explicit in the proof and tested directly.

## What was pruned

- Ambiguous wording that could make “three arguments are necessary” sound like an entropy-identification requirement. It now explicitly concerns generator recovery.
- The article's duplicate one-point numerical example and Jacobian details. They remain in [the exact audit](../../analysis/correctness/LAPLACE-TWO.md) and its code/tests. That example has entropy zero for both generators, so it does not show that two arguments are necessary for entropy.
- A duplicate README link. Preserved baseline files, accepted outputs and proof evidence were retained.

## Sources, checks and limits

[Original supplied files and hashes](../../evidence/supplied/2026-09-18/README.md) are preserved byte-for-byte. The supplied Python script was inspected and executed successfully; [the replay receipt](supplied-replay.json) records its output and row-convention comparison with repository transforms. The JSON identifies the older public commit `015bcd4`; its unrelated endpoint decimals and global-check booleans remain attributed user-supplied review results, not newly reproduced calculations or rigorous certificates.

[Three exact stratum tests](../../analysis/correctness/test_laplace_entropy.py) solve stationary fluxes and killed resolvents directly for generic leaves/two-state chains and rational complete examples. A complete equilibrium triangle is included: complete support does not itself imply positive entropy. These tests supplement the support proof; they do not establish universal claims by sampling.

The completed workflow and PDF/package checks are recorded in [verification.json](verification.json). No novelty claim, formal verification, or new theorem about the five-state global support exhaustion is made. The finished investigation was reopened only for this supplied-evidence comparison and authorized editorial/repository delivery.
