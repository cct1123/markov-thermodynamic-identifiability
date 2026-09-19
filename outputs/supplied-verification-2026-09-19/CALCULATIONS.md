# Bounded verification of the supplied review calculations

The assigned non-Laplace algebra and endpoint decimals reproduce. No mathematical discrepancy was found in these fields. The new calculations do not establish global support exhaustion, endpoint uniqueness, literature priority, or a new rigorous entropy interval certificate.

The checked sources are the [supplied JSON](../../evidence/supplied/2026-09-18/independent_checks.json), [second academic review](../../evidence/supplied/2026-09-19/second-academic-review.txt), and the displayed definitions in [the manuscript](../../manuscript/main.tex), Appendix C ("Exact endpoint construction and entropy certificate") of [the proof supplement](../../manuscript/supplementary/proofs.tex), and the cited local audits. Their SHA-256 hashes, the executed command, environment, complete matrices, stationary laws, differences, and tolerances are recorded in [calculations.json](calculations.json).

## Field-by-field verdict

| Supplied field or review calculation | Result and evidential scope |
| --- | --- |
| `minors` | All three determinants reconstructed exactly from the displayed hidden blocks: `-9*z*(4*z-9)`, `-18*z*(2*z-3)`, `-14*(22*z+19)`. The first two have only `z=0` as a common root; the third is strictly negative for positive `z`. This checks the algebra underlying the minimality argument. |
| `cone_discriminant_identity` | Exact discriminant of the displayed envelope quadratic equals `-(11/1200+11*sqrt(6)/4200)*(z+19/22)^2*P(z)/352`. This identity alone does not prove the envelope is globally exhaustive. |
| `path_discriminant_identity` | Exact discriminant of the displayed physical-path quadratic equals `-567*(z-2)^2*(2*z-3)^2*P(z)`. This checks the stated polynomial identity, not a classification of every path or exceptional chart. |
| `three_state_weights` | All three weights reconstructed as principal cofactors of `-Q(eps,kap)` and matched exactly. |
| `three_state_stationarity_exact` | Normalization, `pi*Q=0`, zero row sums, and trace `-4` checked exactly. The domain is `0 < kap < eps < 1/2`. |
| Review's three-state current/entropy calculation | All three oriented stationary currents equal `(eps-kap)*(1-eps-kap)/Z`. Their flux-ratio product is exactly `eps*(1-eps)/(kap*(1-kap))`. Positivity on the stated domain makes this the asserted cycle-affinity/entropy identity. |
| `endpoint_high_precision.z_star` | Recomputed at 80 and 120 digits from the quartic. Exact real-root counting gives one negative and one positive root; a positive rational bracket selects the required embedding. Matches the supplied decimal to its displayed rounding precision. |
| `endpoint_high_precision.sigma_source`, `sigma_target`, `delta_sigma` | Both endpoint generators reconstructed from the exact definitions in `Q(z*)`; independent fresh stationary solves at each precision agree with cofactor calculations. Edge-flux entropy agrees with the stationary directed-rate formula. All three supplied values reproduce. |
| Review's relative entropy separation | Recomputed as `4.18337779453271936...%`, agreeing with the stated approximately `4.1834%`. |
| `endpoint_high_precision.precision_digits` | The original claim of a 90-digit computation cannot be audited without its generating script. This execution explicitly uses 80 and 120 digits. |
| `endpoint_high_precision.max_tested_resolvent_discrepancy` | The exact supplied value `2.454546733e-91` is not reproducible from the supplied files because its argument grid and generating script are missing. Fresh explicitly specified grids give the residuals below. This is a missing provenance detail, not evidence of unequal kernels. |
| Review's two scalar conditioning identities | Exact differentiation and rational simplification verify `dh/dR = -(lambda1+h)^2/(lambda3-lambda1)` after substituting `R=(lambda3+h)/(lambda1+h)`, and `G(lambda_i)-G(lambda_j) = v*(lambda_j-lambda_i)/((lambda_i+h)*(lambda_j+h))`. Positive arguments and hidden escape, distinct inverse arguments, and the corresponding nonzero denominators are retained. |
| `three_laplace_inverse_test_errors` | The original three floating residuals cannot be reproduced as stated: original example rates, argument triples, and numerical implementation were not supplied. Laplace formulas and the supplied two-point example are covered by the separate scope audit. |
| `two_laplace_counterexample`, `two_laplace_entropy_identification` | Outside this assignment; covered by the separate Laplace replay/scope audit. |
| `review_scope` and narrative scope disclaimers | Preserved as reviewer attribution. The new computation does not authenticate the reviewer identity, reconstruct the full original review procedure, or enlarge its stated scope. |

## Endpoint values and independent checks

| Quantity | Fresh value, rounded for display |
| --- | --- |
| Positive root | `10.55714966866497068801877270373327982` |
| Source entropy | `0.062946400236874352911686953764819217` |
| Alternative entropy | `0.065579685966841445651891885296354030` |
| Entropy separation | `0.002633285729967092740204931531534813` |
| Relative separation | `4.183377794532719360526339137520615%` |

Entropy uses natural logarithms and the manuscript's `k_B=1` convention, so rates and entropy share the fixed inverse-time units. The exact field calculation establishes the six absent directed edges as zero and the seven reciprocal support pairs as nonzero. Positivity of supported rates and stationary masses is checked numerically at both precisions. No tiny negative rate is clipped and no reverse-rate epsilon is added. Algebraic row normalization and marked-matrix commutation, together with reset/exit invariance, establish the candidate's all-time kernel identity; a finite grid is not being used to establish that identity.

The fresh resolvent grid is `lambda = (1/10, 1, 2, 3, 10, 100)`, with the maximum absolute matrix-entry discrepancy:

| Precision | Fresh maximum resolvent discrepancy | Largest source/target stationary cofactor versus LU discrepancy |
| --- | --- | --- |
| 80 digits | `3.74249e-80` (upper rounded) | `3.42622e-81` (upper rounded) |
| 120 digits | `1.85885e-119` (upper rounded) | `9.43945e-121` (upper rounded) |

The 80/120-digit root values differ by about `4.54e-79`; the entropy values and their separation differ by less than `5e-80`. Comparisons against the supplied decimal strings have differences below `3.23e-69` for the root and `4.07e-72` for the entropies. The complete unrounded numbers and acceptance thresholds are saved in JSON. These are arbitrary-precision numerical results, not rigorously enclosing intervals.

## Reproduction and independence

Run from the repository root:

```powershell
.venv/Scripts/python.exe -B analysis/correctness/verify_review_calculations.py
```

The completed run used Python 3.9.12, SymPy 1.14.0 and mpmath 1.3.0 on Windows. There is no RNG, optimizer, or topology enumeration. The [new script](../../analysis/correctness/verify_review_calculations.py) imports no historical checker and reads no historical accepted numerical output. Supplied numbers enter only the comparison after fresh calculations. The exact coefficients and generator construction are transcribed from the displayed definitions, and the exact endpoint implementation shares the historical `Q(z*)` field/conjugation formulation; its agreement is not an independent derivation of those definitions. The new stationary linear solves versus cofactors, entropy formulas, and numerical conjugation checks provide independent checks of those downstream steps.

The assertion guard precedes imports/calculations and rejects both `-O` and `PYTHONOPTIMIZE=1`. Both modes were executed in child processes: each returned status 1 with the assertion-enabled message, emitted no calculation progress, and left the JSON output unchanged. The normal command was rerun after the guard and scalar identities were added, so the saved script hash matches the executed version. Final generated JSON SHA-256 after these guard checks: `70247f8cc533a72cf99483765707c4374414d12bdb53a1f9dfc1aa5792dd15dd`.

Only the assigned new checker and this output directory's calculation artifacts were written. Accepted historical outputs and the supplied originals were not overwritten.
