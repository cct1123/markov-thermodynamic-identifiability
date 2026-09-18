# Five-state boundary unfolding and critical audit

Contribution: exact algebra and rational interval calculations, conventional local proof, and a separately labeled wider numerical continuation. This is not formal verification or a claim of genericity in arbitrary Markov networks. All historical proof scripts and outputs are preserved.

## Perturbation and falsification target

In the source matrix `Q(z)` replace only `q_lx=z` and `q_ly=z` by `z+delta` and `z-delta`, respectively. Their sum stays `2z`, so the generator diagonal, trace, hidden eigenvalues, observed rates, and all other rates remain unchanged. The residue of the fast hidden pole changes. This is an exit-asymmetry perturbation, not a uniform time rescaling or relabeling. Rates require `z>|delta|`.

The scientifically relevant falsifier of a local boundary theorem would be a connected-hidden positive realization above the predicted critical curve with **exact all-time equality**, or a negative rate/failed denominator/nonreciprocal edge in its predicted critical realization. The target class remains irreducible reciprocal generators, one resolved microscopic reverse pair, known visible endpoints, and at most five states. Realizations are counted modulo hidden permutations. Approximate kernel agreement alone would not falsify or certify the exact theorem.

The existing support-exhaustion proof is explicit about these assumptions. It first handles disconnected hidden supports and then represents all connected supports by invariant triangles. Its unique-equality argument is necessary until the separate endpoint construction is checked. The independent cone-to-path equality check is therefore substantive. No logical gap in those balanced arguments was identified by this audit. The sharp threshold is not inferred from a failed optimizer or the first-order opening threshold.

## Exact extension

Retain the manuscript's constants `rho=sqrt(6)`, `r_y=4(rho-1)/5`, `m=(7+2rho)/5`, `L=(3-rho/2)/8`, `R_w=35rho/88`, `k=(2z-9+2rho)/(4rho)`, `a=k-1`, and `J=am+k`. Set `A=z+delta` and `B0=(z-delta)/r_y`. The modal output wedge and contraction rates are unchanged. Only the heights of the two modal inputs change. The generic envelope formulas in Appendix B are already valid for independent `A,B0`.

With `F=f0+f1 t+f2 t^2`, the exact discriminant is

\[
\Delta=-\left(\frac{11}{1200}+\frac{11\sqrt6}{4200}\right)
\left(z+\frac{19}{22}\right)^2\frac{\mathcal P_\delta(z)}{352},
\]

\[
\mathcal P_\delta(z)=352z^4-3168z^3-4644z^2-11340z-7623
 -(20160z+14112)\delta-(352z^2-3168z+15768)\delta^2.
\]

These are exact symbolic identities, checked from the unchanged modal moments and independently against the generic triangle-height formula in the tests.

The script evaluates every strict sign needed to retain the global envelope reduction and its constructive sufficiency on the **whole rational rectangle**

\[
10.55\le z\le10.565,\qquad |\delta|\le0.005.
\]

The interval arithmetic uses exact rational endpoints, outward rounding to 45 decimal places after each operation, a rational enclosure of `sqrt(6)` with squared endpoints straddling six, and shifted polynomial evaluation to control dependency overestimation. All denominator intervals exclude zero. Representative certified bounds are `-f0>0.102`, `f1>5.267`, `-f2>14.445`, exclusion of a negative bottom vertex `>6.691`, apex separation `>0.0182`, and `dP_delta/dz>486081`. Endpoint polynomial signs hold uniformly in `delta`, hence every `|delta|<=.005` has precisely one root `z_*(delta)` in the rectangle. The saved JSON contains all exact interval endpoints; decimal values here only summarize those certificates.

Consequently, within the rectangle:

- Above this root, no connected hidden support is feasible. The disconnected-support argument leaves only the source.
- At the root, equality forces one normalized connected-hidden path generator, in addition to the disconnected source. All six missing directed rates are paired structural zeros. The strict input/output/invariance margins imply strict positivity of the remaining rates and a positive row-normalization vector.
- Below the root, the vertex `t=-f1/(2f2)` has strictly positive envelope slack. The same three successive vertex changes used in the original proof make every rate positive. The hidden-pair shear then yields an exact data-preserving entropy-divergent family. A complete realization has an open six-dimensional set of admissible normalized hidden similarities, so this side contains infinitely many generators.

These are conventional local proofs supported by exact sign calculations. The statement that the **two critical generators have distinct entropies** follows in some sufficiently small neighborhood of `delta=0` from the original certified positive entropy gap and continuity on their fixed reciprocal supports. No explicit interval of entropy separation is asserted merely from the geometric rectangle. The saved wider numerical grid has positive gaps throughout, but that numerical fact does not replace an interval entropy certificate.

The implicit-function derivative is exact:

\[
z_*'(0)=\frac{20160z_*+14112}{\mathcal P'(z_*)}
\simeq0.465004213540206945.
\]

Nondegeneracy does not rely on that decimal: writing `z=10+x` gives
`P'(10+x)=1408x^3+32736x^2+223032x+353380>0` for `x>=0`.

The exact reduced normal form is

\[
F=f_2(t-t_c)^2-\frac{\Delta}{4f_2},\qquad t_c=-\frac{f_1}{2f_2},\quad f_2<0.
\]

The active-boundary path solutions have two roots, one double root, or no root as `Delta` decreases through zero. At the original critical point, numerical derivatives are `F_z=-48.589112...` and `F_tt=-28.997834...`. Their nonzero signs follow independently from the exact polynomial and `f2<0`. Thus this is a nondegenerate fold of the **boundary equation**, with square-root splitting of its roots. It is a boundary of a positivity-constrained realization set, not a generic saddle-node of the entire set of positive realizations. The complete subcritical continuum and the ever-present source disprove the latter interpretation.

## Numerical continuation and verification

The executed deterministic grid contains 41 `delta` values in `[-0.5,0.5]` at spacing `.025`. At each value, the script locates the polynomial root and evaluates the boundary path there and at offsets `z-z_*(delta)=+/- .001`. It reports **active-boundary path candidate counts**, not the total number of realizations outside the proved local rectangle. Counts are `2,1,0` below/at/above at every grid node. A complete exact-law realization is separately constructed below each node by deterministic backtracking of the triangle strictification. Its numerical positivity is a diagnostic; all-time equality is supplied by the analytic modal similarity identity.

All physical rates are computed at 80 decimal digits. No rate is clipped and no reverse epsilon is added. Six prescribed absent rates are checked below `1e-65` and omitted from entropy because the boundary equations make them structurally zero, not because they are small. Every remaining rate and stationary mass is positive. Present critical rates are at least about `0.164588` on this grid. Four resolvent arguments `.1,1,10,100` agree below `1e-65`. At `delta=-.5,0,.5`, independent 120-digit recomputation agrees with 80-digit entropy below `1e-65`; direct float64 matrix-exponential kernels at times `0,.01,.1,1,10` agree below `1e-12`.

For the six row-normalized hidden-similarity directions, the full generator-orbit Jacobian has numerical rank six. The Jacobian of the six active zero-rate equations has rank six on both subcritical path branches and rank five at their merger (relative singular-value tolerance `1e-10`). At `delta=0` the smallest active singular value is about `1.8e-16`, while the next is `3.127`; this is consistent with the exact one-dimensional boundary normal form. These rank computations are numerical diagnostics, not solver or formal certificates.

Selected continuation values:

| delta | critical z | source entropy | path entropy |
|---:|---:|---:|---:|
| -0.5 | 10.3259827963 | 0.0947113591 | 0.0995866301 |
| 0 | 10.5571496687 | 0.0629464002 | 0.0655796860 |
| 0.5 | 10.7911106097 | 0.0385675247 | 0.0398135262 |

Numerical continuation is not support exhaustion outside the certified rectangle. It does not prove genericity under arbitrary perturbations of entrance rates, hidden eigenvalues, topology, observed labels, or hidden dimension.

## Dimension and thermodynamic scope

For this kernel the minimum linear dimension is five and there is already a positive five-state source, so the minimum **positive state count** is also five. The five-state cap can equivalently be replaced here by restricting to positive realizations of that minimum state count. This coincidence must not be used as a general theorem that positive-realization order always equals linear order. A six-state strongly lumpable split preserves the data and admits divergent entropy, so unrestricted-dimensional inference retains no finite upper ceiling for this example, including above or at its five-state threshold.

The entropy used here is the stationary network entropy-production functional. The algebra does not require local detailed balance. Interpreting it as all physical dissipation requires the physical assumptions and resolved channel accounting stated in the main paper. Positive reverse rates are required for each admitted model; the divergent limiting model itself may lose a reverse edge and need not be admitted.

## Reproduction and artifacts

From the repository root:

```powershell
.\.venv\Scripts\python.exe -B analysis/revision/continuation.py
.\.venv\Scripts\python.exe -B -m unittest analysis.revision.test_continuation
```

The standalone script creates `outputs/revision/continuation.json`, `manuscript/figures/continuation.{pdf,svg,png}`, and `manuscript/figures/realization-geometry.{pdf,svg,png}`. The JSON records source hashes, dependency versions, domain, precision, numerical tolerances, all rates, stationary vectors, entropy values, discriminants, ranks and candidate counts. `--figures-only` redraws the figures from saved data. The geometry figure uses an invertible vertical rescaling to show both inputs and the highly elongated triangle. Both generated PNG figures were visually inspected for layout.

The tests additionally reconstruct the balanced critical generator from the independently preserved algebraic path-witness coefficient file and compare it with the modal triangle realization at 90 digits after the specified hidden permutation. This shares the source family and mpmath engine but uses distinct coordinate constructions and the historical exact field coefficients. Test assertions establish only the identities and finite cases stated here; the attached conventional proof is required for global support exhaustion.

An initial test implementation sent a large seven-variable rational expression directly to symbolic cancellation. That test run was interrupted before a result, then replaced by explicit clearing of the known nonzero denominators and polynomial expansion. The completed test below checks the same mathematical identity. The interrupted attempt is not evidence for or against it.

Final executed test command reported five tests passed in approximately 2.2 seconds. The standalone continuation script completed with all assertions passed and all 41 numerical nodes recorded.

## Independent rare-event review

The coordinating agent requested an independent review of `analysis/revision/rare-event-section.tex`, including testing quantifiers, stationary initial-law error and the exponential conclusion. The reviewer read that complete source. No objection was found to the stated proposition under its declared simple-hypothesis, fixed-duration and stationary-record assumptions.

For the three stationary weights `w=(1-e+2k-k^2,1+k-e^2,1-k+2e-ek)`, the derivatives are `(2-2k,1,-1-e)` and `Z'=2-e-2k>0` on `0<=k<=e<1/2`. The quotient rule and triangle inequality give

\[
\|\partial_k\pi\|_{TV}\le\frac{\|w'\|_1+|Z'|}{2Z}
=\frac{3-2k}{Z}\le1.
\]

Thus the two stationary initial laws differ in TV by at most `k-k^p`. Changing `k` to `k^p` alters only `y->h` and `h->x`. Although those changes have opposite signs, they occur in different source rows. A common/excess-clock coupling therefore has instantaneous separation hazard at most `k-k^p`, not twice this quantity. Combining initial maximal coupling and the path coupling gives full-path TV at most `(1+H)(k-k^p)`. Every fixed-duration simple-hypothesis test has sum of its two error probabilities at least one minus that TV, and the marked-record experiment cannot increase TV. These facts justify the proposed necessary duration bound.

The scaling `sigma(Q_p)/sigma(Q_1)->p` follows because the leading affinity changes from `1/e^2` to `p/e^2` while the cycle current remains asymptotic to `e/3`. Therefore the logarithmic duration lower bound normalized by `sigma(Q_1)^2` tends to 9 (or `9/p^2` for `sigma(Q_p)^2`). An exact multiplicative equivalence `k~exp(-9 sigma^2)` does not follow and is correctly disclaimed in the proposed text.

The simple alternative must be permitted to vary the small reverse rate independently of the common rate `e`; otherwise the relation `k=exp(-1/e^2)` as a known constraint would exclude `Q_p`. The proposed paragraph makes this distinction. The direct rare-jump count is a separate necessary-detection bound from its stationary expectation, not a Poisson assumption or a sufficient observation strategy. The statement about expected observed-event count converts fixed duration through stationary event intensity; it does not claim a lower bound for arbitrary stopping-time experiments based on a prescribed random number of events.
