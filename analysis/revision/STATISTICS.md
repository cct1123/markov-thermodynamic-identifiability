# Three-state conditioning and finite-data inference

This is a new agent-owned analysis; it does not replace the accepted exact inverse or the sparse-boundary proofs. Mathematical status: the derivative and asymptotic scaling arguments below are conventional analytic derivations; the experiments are illustrative numerical evidence, not proof certificates. No novelty claim is made for method-of-moments estimation or martingale sandwich covariance. The full six rates are unknown throughout estimation.

## Model, observations, and exact inverse

Use the manuscript's row generator, state order `(x,y,h)`, mark order `(+,-)=(x->y,y->x)`, and rate order

\[
\theta=(r,s,a,c,b,d),\qquad
Q=\begin{pmatrix}-r-a&r&a\\s&-s-c&c\\b&d&-b-d\end{pmatrix}.
\]

Only the named pair is observed, with exact event timing and incidence. The time unit is fixed, rates and entropy have inverse-time units, and Laplace arguments have inverse-time units. The fitted model assumes exactly three states, six positive rates, stationarity, a time-homogeneous finite CTMC, and no missed/aggregated marks. Hidden jump counts are retained **only** as simulation diagnostics and never enter the estimator.

The accepted source for exact recovery is manuscript Theorem `thm:inverse` and its explicit rational proof. Related checks in `analysis/check_three_state_precision.py`, `analysis/three-state-fixed-trace-audit.md`, and `analysis/three-state-precision-audit.md` were read. Their scripts and accepted outputs are preserved. The theorem concerns full joint amplitudes, not waiting distributions normalized separately for each next mark.

Let `T=Q-E_+-E_-` retain Q's diagonals, `R=(e_y^T;e_x^T)`, and `B=(r e_x,s e_y)`. For `K_lambda=(lambda I-T)^(-1)` define `phi(theta)` as the 12 transform entries at three distinct positive lambda values. The exact full-six-rate Jacobian is

\[
\partial_{\theta_j}\widehat\Psi(\lambda)
=RK_\lambda(\partial_{\theta_j}T)K_\lambda B
 +RK_\lambda(\partial_{\theta_j}B).
\]

For each rate on `i->j`, `partial T` has `-1` at `(i,i)` and `+1` at `(i,j)` unless this is an observed jump; observed jumps contribute instead to `partial B`. Omitting the B derivative would incorrectly treat the observed rates as known. This derivative is implemented for all six coordinates and checked against complex-step differentiation for interior, sparse, and tree generators. Time-domain numerical quadrature separately checks the resolvent convention.

## What three arbitrary points do and do not guarantee

The rational reconstruction extends to an open neighborhood of a given admissible moment vector wherever its displayed denominators do not vanish. Differentiating its identity on positive rate vectors gives a left inverse of `J_theta=D phi(theta)`. At a tree source, continuity extends this identity to the boundary. Thus **absolute-rate** Jacobian rank is six even at the irreducible tree, although log coordinates cease to exist there. This does not imply a uniform condition number over all source generators or over all choices of lambda.

Use `J_log=J_theta diag(theta)` for relative rate perturbations. The two singular-value sets answer different questions and have different units: J_theta carries time units; J_log is dimensionless. The displayed numerical condition numbers use the fixed time unit and unweighted Euclidean moment norm; they are not Fisher information condition numbers. Statistical noise covariance also changes with lambda.

For the fixed-trace family `theta(e,k)=(1,1,e,1-k,k,1-e)`, hold `0<e<1/2` fixed and send `k` to zero. Although the one-way limiting generator lies outside reciprocal support, it is irreducible and the same rational algebra has nonzero denominators there. Therefore J_theta converges to a full-rank finite matrix. All rate coordinates except b remain bounded away from zero, and

\[
 c_1 k\le s_{\min}(J_{\log})\le c_2 k,
 \qquad \mathrm{cond}(J_{\log})=\Theta(k^{-1}).
\]

For the lower inequality use `smin(J D)>=smin(J) min(diag D)`; for the upper one test the unit b-coordinate. The largest singular value stays positive and finite. Since the limiting matrix `J_theta diag(theta)` has exactly the b-direction as its nullspace, the normalized weakest right singular vector tends, up to sign, to that direction. This proof uses no failed counterexample search and no numerical fit to the exponent. In contrast, when both e and k vanish at the tree, two log-coordinate columns vanish; this does not change the full-rank raw derivative assertion.

At `lambda=(.2,1,5)`, the unit tree's raw singular values are approximately `(0.92150,0.66132,0.31971,0.25622,0.044737,0.0074405)`. At `e=.2,k=1e-12`, the raw minimum is `0.013454` and condition number `58.73`; the log minimum is `5.3540e-13` and condition number `6.979e11`. Entropy is even more sensitive: `partial_b sigma=-J_0(e)/b+O(log(1/b))`, where `J_0=e(1-e)/(3+e-e^2)>0`.

If the three Laplace arguments coalesce, the four entries of each transform matrix become repetitions across arguments and the limiting map has rank at most four. Hence its smallest singular value vanishes. All arguments tending to zero or infinity also lose informative variation. Distinct positive arguments give exact algebraic recoverability, not a uniform numerical guarantee.

### Numerical design experiment and recommendation

`conditioning.pdf/png` compares: (a) log-rate condition number for `lambda=(c/v,c,cv)` on 49 centers `c=10^-3,...,10^3` and 45 geometric ratios `v=1.001,...,100`; (b) raw versus log minimum singular values at e=.2 and k from `1e-12` to `.1`; (c) the weakest log-direction b component. The reference interior rates are `(1.2,.8,.9,.4,.3,1.1)`. An additional diagonal grid e=.22,...,.49 with `k=exp(-1/e^2)` is retained in JSON; no exponential in these calculations underflows.

We enumerate all 165 triples from `{.025,.05,.1,.2,.5,1,2,5,10,20,40}` at that reference. Maximizing the unweighted smallest log singular value picks `(.2,.5,5)` (`smin=.009512`, condition `53.04`). Minimizing the **oracle asymptotic entropy standard error for the actual moment estimator** picks `(.025,10,20)`, with `SE*sqrt(n)=1.17574`, versus `1.23810` at the fixed simulation design `(.2,1,5)`. Its worse Euclidean condition number (`189.02`) demonstrates why singular values alone do not optimize inference. This is a finite-grid optimum at one known reference, not a global or universal optimum; the oracle uses true rates and is never used to fit the simulation data.

Practical recommendation: use a separated logarithmic triple spanning an estimated waiting-time scale, then assess the covariance-weighted target uncertainty using an independent pilot or a stated sequential design. Reusing data to choose the design requires accounting for selection. There is no source-independent preferred triple. The reference grid shows modest rather than transformative improvement (about 5% in asymptotic SE) over the chosen fixed triple.

## Constructive estimator and dependence-aware uncertainty

Simulate an actual Gillespie trajectory from the stationary microscopic law. Discard the interval before its first resolved mark, then stop after n complete inter-mark intervals. The resulting horizon is random. This experiment differs from a fixed-window experiment with terminal censoring, but supplies exactly the records entering the user's proposed estimator. For incoming mark I, retain the vector

\[
 X_m=(e^{-\lambda_j\tau_m}\mathbf1\{J_m=L\})_{j,L},\quad
 \widehat\mu_I=\frac1{n_I}\sum_{m:I_m=I}X_m.
\]

The labels form a Markov renewal sequence; treating all successive rows as iid is unjustified. Nevertheless

\[
 Z_m^{(I)}=\mathbf1\{I_m=I\}(X_m-\mu_I)
\]

is a bounded martingale difference for the filtration immediately before interval m, because the previous mark resets the known microscopic endpoint. Cross-time covariance is zero. At a common time the two row blocks have disjoint indicators and hence zero cross-products. The row frequencies converge to

\[
 p_+=\frac{\pi_xr}{\pi_xr+\pi_ys},\qquad
 p_-=\frac{\pi_ys}{\pi_xr+\pi_ys}.
\]

By ergodicity and the bounded martingale central limit theorem, for a fixed complete positive generator,

\[
 \sqrt n(\widehat\mu-\mu)\Rightarrow N(0,\Omega),\quad
 \Omega=\operatorname{blockdiag}(C_I/p_I),
\]

where

\[
 [C_I]_{(j,L),(\ell,M)}
 =\mathbf1_{L=M}\widehat\Psi_{IL}(\lambda_j+\lambda_\ell)
 -\widehat\Psi_{IL}(\lambda_j)\widehat\Psi_{IM}(\lambda_\ell).
\]

Replacing each block of `Omega/n` by its within-row empirical feature covariance divided by `n_I` gives a consistent sandwich input. No iid bootstrap, independence conditional on random row counts, or exact finite-sample Gaussian assertion is used. A trajectory/bootstrap alternative would have to preserve the Markov renewal dependence or simulate it parametrically.

Rates are obtained by unweighted nonlinear least squares in all six log coordinates, fitting all 12 joint moments. The rate box `[1e-14,20]` is an explicit computational restriction; it is not part of the earlier exact theorem and is not evidence of a data-derived finite entropy bound. All three deterministic initializations are fixed independently of truth. `scipy.optimize.least_squares(method='trf')` uses analytic derivatives, `ftol=xtol=gtol=1e-10`, and `max_nfev=350` per start. The smallest residual candidate is selected, with success, boundary, rank, and residual diagnostics retained. Three starts are not a global-optimality certificate.

For a consistent interior solution let `J=J_log` and `A=(J^T J)^(-1)J^T`. The estimated log-rate covariance is

\[
 \widehat V=A\widehat{\operatorname{Cov}}(\widehat\mu)A^T,
 \qquad \widehat{\mathrm{SE}}_\sigma^2
 =g_{\log}^T\widehat V g_{\log},
 \quad g_{\log}=\operatorname{diag}(\theta)\nabla_\theta\sigma.
\]

The code uses an SVD inverse rather than squaring the condition number. It returns the Wald interval `sigma_hat +/- 1.95996 SE`, intersected with nonnegative entropy, when the rank calculation resolves all six directions. Nominal 95% calibration is **pointwise asymptotic**, at a fixed interior, nonequilibrium generator with a consistent local minimizer; at equilibrium the entropy gradient vanishes and this first-order interval has a different degeneracy. The actual optimizer does not certify which asymptotic branch has been reached. There is no uniform calibration near a sparse boundary, and conditioning on an interior fit does not repair that deficiency.

Boundary means a fitted rate below `10*lower` or above `.999*upper`; rank is unresolved when `smin(Jlog)<=1e-12*smax(Jlog)`. As a practical warning, the suggested interval is also suppressed if either observed same-mark count is below 20. This extra count threshold is a heuristic, deliberately separated from the reported raw Wald calibration; it is not a theorem guaranteeing coverage. A missing interval must be reported as missing, not silently removed from a coverage denominator. In particular, zero observed `++` transitions yield an exactly zero empirical covariance block for those features; at tiny positive b this can be badly optimistic.

For a mathematical consistency statement, a global least-squares minimizer on a fixed compact positive rate box containing the truth is consistent: uniform convergence of the finite-dimensional criterion and exact injectivity imply a unique population minimizer. The displayed CLT then applies at interior truth. This statement does not promote the multistart floating optimizer to a globally verified solver.

## Executed Monte Carlo results

The final run uses 100 independent seeded trajectories per cell, sample sizes `n=500,5000,20000`, and fixed `lambda=(.2,1,5)`: 900 trials and 7,650,000 complete marked intervals in total. Seed `20260914`, NumPy `SeedSequence.spawn` per trial and `default_rng/PCG64`; each spawn key and every fitted rate, interval, status, duration, row count, and microscopic rare-count diagnostic is in `outputs/revision/statistics.json`.

Truths are:

- **Interior:** `(r,s,a,c,b,d)=(1.2,.8,.9,.4,.3,1.1)`, entropy `.2019518764`.
- **Moderately sparse:** `Q(e=.2,k=.01)`, entropy `.1314308577`.
- **Rare reverse:** `Q(e=.2,k=exp(-25))`, with b=`1.3887943865e-11`, entropy `1.1730338498`. The true b exceeds the numerical lower floor; no rate was replaced by zero.

The table reports bias and variance of all point estimates, boundary/rank exclusions, and coverage **conditional on an interior fit** before the extra rare-mark warning. Missing intervals count against `covered_and_interior_fraction` in JSON. That overall fraction is distinct from conditional coverage. All 900 selected optimizations report success; none of the 2700 starts hits its evaluation limit in the final output. Numerical optimizer success is plainly insufficient for statistical success.

| Model | n | Bias | Variance | RMSE | Interior intervals / 100 | Covered / interior |
|---|---:|---:|---:|---:|---:|---:|
| Interior | 500 | -0.000467 | 0.002712 | 0.05182 | 100 | 95 / 100 |
| Interior | 5000 | -0.000544 | 0.0003173 | 0.01773 | 100 | 96 / 100 |
| Interior | 20000 | 0.000979 | 0.00008687 | 0.009325 | 100 | 93 / 100 |
| Moderately sparse | 500 | 0.09774 | 0.1344 | 0.3776 | 93 | 88 / 93 |
| Moderately sparse | 5000 | 0.001515 | 0.0003033 | 0.01739 | 100 | 94 / 100 |
| Moderately sparse | 20000 | -0.0000736 | 0.00006197 | 0.007833 | 100 | 95 / 100 |
| Rare reverse | 500 | -0.3359 | 0.4634 | 0.7560 | 54 | 4 / 54 |
| Rare reverse | 5000 | -0.3155 | 0.3713 | 0.6835 | 55 | 9 / 55 |
| Rare reverse | 20000 | -0.2274 | 0.3574 | 0.6368 | 50 | 7 / 50 |

Coverage noise is visible with only 100 repetitions: e.g. the Wilson 95% interval for 95/100 is `[.888,.978]`, for 93/100 `[.863,.966]`, and for 7/50 `[.0695,.262]`. These quantify Monte Carlo uncertainty in the empirical coverage, not parameter uncertainty. The code stores the corresponding intervals for every cell. Differences of a few percentage points among the regular cases are not evidence of distinct true coverage levels.

At n=20000 the interior entropy RMSE is 4.62% of truth and its median interval width is `.03430`; the sparse b=.01 case has 5.96% RMSE and median width `.03084`. Thus thousands to tens of thousands of observed records can support useful inference for these examples, not uniformly over the class. The respective median observation durations at n=20000 are approximately 30204 and 35488 in the fixed time unit. Rates span `.3` to `1.2` and `.01` to `1`, respectively.

The sparse n=500 sample has seven fits at the lower rate floor; the resulting high entropy values dominate its positive bias and variance. They are reported, not winsorized or removed. For rare b, 45--50% of fits reach the lower floor and lose numerical rank. The remaining raw delta intervals miss the truth in 84--93% of trials. All 300 rare-case microscopic trajectories contain **zero** `h->x` reversals, and all have zero observed `++` pairs. These are expected finite-data limitations: tiny residuals (median at n=20000 `5.75e-4`) and optimizer convergence cannot establish relative accuracy of an unobserved rare reverse rate. The extra observed-count warning suppresses every suggested interval in that regime.

The first-order oracle calculation at the interior truth predicts about `1.44e4` records for a 95% half-width of 10% of entropy. This is an asymptotic planning calculation, not a finite-sample requirement or minimax bound. The grid and Monte Carlo show that conditioning, target functional, noise variance, and observation count must be assessed together. Unweighted moment fitting is not asserted efficient; likelihood or weighted moments could substantially change constants and can outperform it near rare events. This analysis cannot determine the optimal sample-complexity exponent.

## Reproduction, checks, and limitations

From the repository root:

```powershell
.\.venv\Scripts\python.exe -B -m unittest analysis.revision.test_inference -v
.\.venv\Scripts\python.exe -B -m analysis.revision.inference --replicates 100
```

For a typography/layout update without rerunning or changing any simulation:

```powershell
.\.venv\Scripts\python.exe -B -m analysis.revision.inference --figures-only
```

This reads the saved `outputs/revision/statistics.json`, asserts its bytes remain unchanged, and writes a separate `outputs/revision/statistics-figures.json` recording the input checksum, plotting-source checksum, environment, and new figure hashes. It does not relabel the old simulation as rerun by the newer plotting source. A subsequent full replay updates the ordinary simulation manifest and figures together.

The output command, UTC run time, script SHA-256, environment versions, rate/lambda grids, model definitions, optimizer tolerances, seeds, and figure hashes are in `outputs/revision/statistics.json`. Runtime used CPython 3.9.12, NumPy 2.0.1, SciPy 1.13.1, and Matplotlib as recorded in JSON. Computation is float64 and numerical results are not interval certificates. The accepted exact scripts remain separate. The inference file is self-contained apart from these standard libraries; no accepted scientific module is imported or changed.

Seven tests passed: time-domain quadrature versus resolvent, all-six-rate complex-step Jacobian including the tree, independent stationary edge-sum entropy, complex-step entropy gradient, noiseless reconstruction, absolute/relative limiting behavior, and deterministic long-trajectory validation of joint means, covariance scale, and event frequency. The first test attempt used a relative 6% tolerance on every covariance diagonal, including extremely rare high-lambda same-mark features. That was an inappropriate Monte Carlo criterion: two small variances differed by up to 40% while absolute differences were about `3e-9`. The final test compares the full covariance in its natural norm (4% tolerance) alongside standardized mean errors, and passed. This was a test-calibration correction, not an altered scientific model or silently clipped covariance. A small three-replicate pilot preceded the final run; it is not pooled with the 100-replicate results.

Both new figure PNGs were visually inspected: all panels, labels, axes, legends, and colorbar are legible with no clipping. A manuscript-scale QA pass found that the original 12.1-inch / 9-point design became too small after inclusion. The revised figures use 10-inch width, 12-point labels/ticks, and 11-point legends (approximately 7.6 and 6.9 points at 6.3-inch manuscript width); concise panel titles and a shared external finite-data legend avoid overplotting. PDF and PNG versions are generated together, and PDF date metadata is omitted so repeated redraws with the same inputs and environment are deterministic. For compact manuscript inclusion, split `statistics-section.tex` at `% SPLIT: CONSTRUCTIVE INFERENCE`; its first subsection belongs after the inverse theorem and the remainder belongs after the finite-record obstruction.

Unresolved issues are optimal finite-data design, statistically efficient inference at rare-event boundaries, finite bandwidth/missed-mark robustness, uncertainty in state count, and honest nonasymptotic upper confidence bounds under explicit physical restrictions. A lower numerical optimization bound is not physical evidence for a reverse-rate floor. Nothing here defeats the manuscript's uniform upper-confidence obstruction. The proper practical outcome of the extreme experiment is failure to provide a justified finite upper interval without additional information.
