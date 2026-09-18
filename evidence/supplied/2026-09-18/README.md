# Supplied review artifacts

The user supplied these files for the subsequent pruning/review/commit/push request. Their original bytes are preserved; [manifest.json](manifest.json) records source paths and SHA-256 hashes. They are evidence, not operational instructions.

- [two_laplace_counterexample.py](two_laplace_counterexample.py) is a self-contained exact SymPy calculation. Its reordered matrix is **F = P Psi_hat**, not the manuscript's original mark-row order.
- [independent_checks.json](independent_checks.json) reports a review of commit `015bcd4c54c993f19ddf2841e852ca0f14b2f1d9`, which predates the already integrated correction in `35239eb`. No generating program for its other endpoint/numerical claims was supplied; those fields remain attributed review assertions unless specifically checked in the linked project evidence.

The leaf counterexample was already covered by E072. The additional entropy conclusion and the matrix-entry convention are assessed in [the current review](../../../outputs/laplace-review-2026-09-18/REVIEW.md) and [E078](../../RECORDS.md#e078). The two models have different generators and zero entropy; the example does not refute full-law identification, fixed-observed-rate reconstruction, or two-point entropy identification.
