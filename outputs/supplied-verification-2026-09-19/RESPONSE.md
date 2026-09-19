# Response to the second academic review

19 September 2026 (UTC). **The review's mathematical checks reproduce, and its standalone reproduction-driver defect was still present in the starting checkout. That defect is now fixed.** The remaining requested presentation changes have been made; several larger changes were already incorporated after the review's target commit. [Evidence and decisions](../../evidence/RECORDS.md#e079).

The supplied review names `015bcd4`. This pass began with a clean checkout at `a171f32`, after revisions `35239eb` and `a171f32`. Both `(1)` attachments are byte-identical to the previously preserved files. The [pasted review and original-file manifest](../../evidence/supplied/2026-09-19/manifest.json) preserve the new provenance. The review is supplied evidence and a user-requested checklist, not independent authority for its claims.

## Response by requested revision

| Review item | Current outcome |
| --- | --- |
| A. Scientific mismatch must fail reproduction | **Fixed in this pass.** The downstream validator already rejected mismatches, but the standalone driver still returned success. The [baseline demonstration](defect-demonstration.json) reproduces exit 0 and `all_checks_passed=true` with a changed `/entropy`. The [driver](../../manuscript/scripts/reproduce.py) now rejects mismatches before subsequent computations, figure writes or a new success receipt. [Regression tests](../../analysis/correctness/test_validation.py) exercise changed scientific and provenance-only payloads through the real driver in isolated temporary copies. No arbitrary numeric tolerance was introduced. |
| B. Full entropy image wording | Already corrected. The abstract, main theorem discussion and limitations distinguish the two-point endpoint set and unique supercritical generator from an attainable subcritical half-line. Neither its lower endpoint nor gaps below that half-line are claimed to be characterized. See Eq. (66), pp. 27–29 of the revised PDF. |
| C. Equality case auditability | The earlier revision already expanded the representation, reflected inequality, both sides of the envelope pole, strict monotonicity and normalization arguments. This pass adds the displayed chain `B0 <= Hc <= H* <= H*sat <= B0` and Table V, assigning each equality its forced parameter and the reason. The separate saturated height makes the last relaxation explicit. See Appendix B.5, pp. 44–45. Existence and entropy separation remain separate in Appendix C. |
| D. Closest prior work | Ehrich's compatible-model and upper-range antecedent, Nitzan's tolerance-constrained fitting, and the complementary Nishiyama–Hasegawa activity/rate-ratio bound were already explicit. A new paragraph on p. 3 distinguishes Maier–Seifert–van der Meer's path entropy and minimal-graph reconstruction from the stationary entropy image and minimal linear order. The primary source was inspected at [arXiv v1, Secs. III, VI–VII](https://arxiv.org/html/2504.16015v1). No exhaustive priority certification is asserted. |
| E. Source-dependent conditioning | Existing raw/log-rate Jacobian analysis and conditioning figures are retained. Eq. (26), p. 11, now gives the review's explicit scalar derivative and informative-difference formulas, explaining amplification at fast hidden escape or weak entrance. Both identities were checked exactly. |
| Two versus three Laplace arguments | Already incorporated; independently checked again. Two identify complete-triangle generators and entropy across the reciprocal at-most-three-state class. Three are required for worst-case uncalibrated generator recovery. The supplied leaf pair has entropy zero in both models and different transforms at a third argument. Its matrix is `F=P Psi_hat`, with previous-mark rows permuted. |
| Finite-record and physical qualifications | Preserved: uniform coverage at fixed finite horizon is distinct from pointwise/increasing-horizon inference; stationary records have a separate convergence proof; one microscopic reverse pair, reciprocal support, state-count constraints and resolved channels remain explicit. Bounded rates do not bound affinities without additional microscopic information. |

## Mathematical verification and limits

The [field-by-field calculation audit](CALCULATIONS.md), [executed calculations](calculations.json), and [independent Laplace derivation](laplace-scope-audit.md) document inputs, exact domains, methods and limitations. Exact checks reproduce all three minors, both discriminant identities, stationary weights/current/affinity, and the scalar conditioning formulas. Fresh endpoint reconstruction at 80 and 120 digits gives, in the manuscript's inverse-time units,

| Quantity | Rounded value |
| --- | --- |
| Threshold | 10.55714966866497 |
| Source entropy | 0.06294640023687435 |
| Alternative entropy | 0.06557968596684145 |
| Separation | 0.00263328572996709 (4.18338% of source) |

Exact similarity identities verify the endpoint candidate's all-time marked-kernel equality. Numerical stationary solves are checked against cofactors, and two entropy formulas agree. These calculations share the displayed generator construction and symbolic engine with existing work; they do not newly prove global exhaustion or certify the endpoint intervals. The existing conventional proofs and interval certificates retain those roles.

The original JSON omits the grids/inputs needed to reproduce its precise resolvent discrepancy and its three inverse-test error values. Their exact decimal residuals therefore remain attributed, unreproduced results. A newly specified resolvent grid and exact inverse checks pass. Missing provenance does not constitute evidence of unequal laws.

A bounded falsification check also found an exact one-point entropy ambiguity between complete triangles, with gap `log(2)/660`; [the witness and exact execution](laplace-scope-audit.md#additional-exact-result-one-argument-can-miss-entropy) are preserved separately. It supports a possible future minimality statement, but was not needed for or added to this focused manuscript revision. A four-state witness in the same audit confirms that the zero-pattern entropy argument cannot be extended beyond its stated cap.

## Validation and disposition

The [bounded verification](verification.json) passes all **41 tests**, the supplied standalone script, all **15 historical scientific-payload comparisons**, the manuscript build and source/receipt validation. The full 900-trajectory campaign remains the previously executed result; it was not rerun for this code gate and exposition change. [Preservation checks](preservation.json) retain the original six theorem statements, baseline artifacts, accepted historical outputs and human-owned brief/instructions. The three source attachments are byte-identical to their preserved copies.

The PDF now has 56 pages. All pages were rendered and inspected in contact sheets, with the new comparison, conditioning formulas, equality chain and table inspected at full page size. The [visual receipt](visual-check.json) records the final PDF hash; the build reports no unresolved citations/references or overfull boxes. [Current manuscript](../../manuscript/main.pdf); [reproduction archive](../manuscript-package.zip).

The checklist is resolved. No newly demonstrated mathematical contradiction requires reopening the broader investigation. The full lower portion of the subcritical entropy image, larger arbitrary graphs, detector changes and exhaustive literature priority remain outside this review. No submission-readiness guarantee or formal verification is inferred from these checks.
