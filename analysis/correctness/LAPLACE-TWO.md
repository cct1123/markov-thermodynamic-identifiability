# Two Laplace points, leaf exceptions, and finite-record topology

Checkpoint: 2026-09-15 UTC. This is an independent exact audit of the requested two-versus-three refinement. It preserves all preceding proofs, programs, and outputs. Mathematical status: conventional algebraic/measure-theoretic proofs with executed exact symbolic regression checks; not formal verification. No priority claim is made.

## 1. Conventions and result

Here, and **only in this new module**, every tuple uses the user's order

\[
(r,s,a,b,c,d),\qquad
Q=\begin{pmatrix}-r-a&r&a\\s&-s-c&c\\b&d&-b-d\end{pmatrix}.
\]

The existing `analysis/revision/inference.py` and conditioning text instead list `(r,s,a,c,b,d)`; their code and data are unchanged. The generator equation itself is identical. State order is `(x,y,h)`, mark order is `(+,-)=(x->y,y->x)`, `r,s>0`, support is reciprocal and connected, and time units and observed endpoints are fixed. The full joint transforms retain their absolute amplitudes:

\[
\widehat\Psi_Q(\lambda)=R(\lambda I-T)^{-1}B,\quad
R=\begin{pmatrix}0&1&0\\1&0&0\end{pmatrix},\quad
B=\begin{pmatrix}r&0\\0&s\\0&0\end{pmatrix},
\]

where T removes only the two observed off-diagonal entries and **retains Q's diagonals**.

**Exact result.** Any two distinct positive full transform matrices identify every complete three-state triangle, with all six rates initially unknown, uniquely among the reciprocal models with at most three states. The inverse is rational and locally Lipschitz at each such source. Three distinct positive matrices remain sufficient for generator recovery throughout the original class, and three are necessary for that task in the worst case when an observed-endpoint rate is uncalibrated: at a hidden leaf, every pair of distinct positive arguments leaves a positive one-parameter generator ambiguity. One full matrix is insufficient for generator recovery in general even on complete triangles; the displayed equilibrium example does not establish one-point entropy nonidentification.

This is a finite-summary statement. Equal transforms at two prescribed arguments do not mean equal full waiting laws. It is also a generator statement: the displayed leaf counterexample has zero entropy in both models.

**Entropy corollary, 18 September supplied review.** Two distinct positive full transform matrices identify entropy throughout the reciprocal class with at most three states, even with unknown observed rates. If an off-diagonal of `M=(P Psi_hat)^(-1)` is nonzero, support is complete and the two-point inverse recovers the unique generator. Otherwise every compatible model is a hidden-leaf tree or two-state chain; stationarity across each edge cut gives detailed balance and entropy zero. The zero pattern concerns M or F=P Psi_hat, not the off-diagonals of the original Psi_hat. This conventional support argument does not imply entropy continuity at a tree or prove that two arguments are necessary for entropy. [Supplied evidence and scope](../../outputs/laplace-review-2026-09-18/REVIEW.md), [three independent exact stratum tests](test_laplace_entropy.py).

## 2. Proof that two points suffice for complete triangles

Use the original proof's `P=((0,1),(1,0))`, `M(lambda)=(P Psi_hat(lambda))^{-1}`, and `h=b+d`. Direct Schur elimination gives

\[
M(\lambda)=\operatorname{diag}(r^{-1},s^{-1})
\left[\operatorname{diag}(\lambda+r+a,\lambda+s+c)
-\frac1{\lambda+h}\binom a c(b,d)\right].
\]

Invertibility follows from the positive-argument killed resolvent and its strictly row diagonally dominant Schur complement. In particular,

\[
M_{xy}(\lambda)=-\frac{ad}{r(\lambda+h)},\qquad
M_{yx}(\lambda)=-\frac{cb}{s(\lambda+h)}.
\]

For a complete triangle both are nonzero. With `0<lambda_1<lambda_2`, set

\[
\rho=\frac{M_{xy}(\lambda_1)}{M_{xy}(\lambda_2)}
=\frac{\lambda_2+h}{\lambda_1+h}>1,
\qquad
h=\frac{\lambda_2-\rho\lambda_1}{\rho-1}.
\]

The other off-diagonal can be used instead. Once h is known, define for each visible row

\[
G_i(\lambda)=\frac{(M(\lambda)\mathbf1)_i-1}{\lambda}
=u_i+\frac{v_i}{\lambda+h},
\]

\[
v_i=\frac{G_i(\lambda_1)-G_i(\lambda_2)}{\lambda_2-\lambda_1}
(\lambda_1+h)(\lambda_2+h),\qquad
u_i=G_i(\lambda_1)-\frac{v_i}{\lambda_1+h}.
\]

Then `r=1/u_x`, `s=1/u_y`, `a=v_x/u_x`, `c=v_y/u_y`, and

\[
d=-\frac{rM_{xy}(\lambda_1)(\lambda_1+h)}a,
\qquad b=h-d.
\]

All source denominators are strictly nonzero (`lambda_2-lambda_1`, `rho-1`, `u_x,u_y`, `a`). The formulas are therefore rational and locally Lipschitz in the finite data near a complete source. A competitor with at most two states has no such nonzero inverse off-diagonal. A reciprocal three-state competitor with an equal full matrix must also have nonzero `ad` (or `cb`), forcing its complete support; it is consequently recovered by the same formulas. This proves uniqueness across the stated state cap, not just in a selected parameterization.

The algebraic nonzero-product condition also makes sense without reciprocity, but that larger class is not asserted here. With the observed x-y pair present, connected reciprocal three-state supports are precisely the triangle or one of the two hidden-leaf attachments. In this particular class, `ad>0` or `cb>0` is equivalent to a complete triangle. No assertion about arbitrary sparse larger networks follows.

There is no uniform two-point conditioning bound as arguments coalesce or as the needed product tends to zero. In particular this refinement does not replace the three-point raw-rate conditioning guarantee at a leaf. The exact script finds raw derivative ranks 6 at a triangle with two points, 5 at the proposed leaf with two points, and 6 at that leaf with three points. Its leaf null direction, in this module's tuple order, is `(1/6,0,1,1,0,0)`.

## 3. The user's leaf pair is a valid full-matrix counterexample

In the order **(r,s,a,b,c,d)**, the proposed pair is

\[
\theta_1=(1,1,1,1,0,0),\qquad
\theta_2=(6/5,1,12/5,2,0,0).
\]

Thus

\[
Q_1=\begin{pmatrix}-2&1&1\\1&-1&0\\1&0&-1\end{pmatrix},\qquad
Q_2=\begin{pmatrix}-18/5&6/5&12/5\\1&-1&0\\2&0&-2\end{pmatrix}.
\]

Both are irreducible reciprocal trees; the hidden state is attached to x. Their full transforms are

\[
\widehat\Psi_1(\lambda)=
\begin{pmatrix}0&(\lambda+1)^{-1}\\
\dfrac{\lambda+1}{\lambda^2+3\lambda+1}&0\end{pmatrix},
\]

\[
\widehat\Psi_2(\lambda)=
\begin{pmatrix}0&(\lambda+1)^{-1}\\
\dfrac{6(\lambda+2)}{5\lambda^2+28\lambda+12}&0\end{pmatrix}.
\]

These were computed independently from the full 3x3 resolvents, including B and the mark row order, and match the literal rational matrices

\[
\widehat\Psi_1(1)=\widehat\Psi_2(1)=
\begin{pmatrix}0&1/2\\2/5&0\end{pmatrix},\qquad
\widehat\Psi_1(2)=\widehat\Psi_2(2)=
\begin{pmatrix}0&1/3\\3/11&0\end{pmatrix}.
\]

The difference in the only differing entry is

\[
[\widehat\Psi_1-\widehat\Psi_2]_{-,+}(\lambda)
=-\frac{\lambda(\lambda-1)(\lambda-2)}
{(\lambda^2+3\lambda+1)(5\lambda^2+28\lambda+12)}.
\]

It is not identically zero. At the third positive argument 3 the entries are `4/19` and `10/47`, differing by `-2/893`. Even the zero-time density amplitudes differ: `psi_{-,+}(0)=r=1` versus `6/5`. Adding just `Psi_hat(0)` does not distinguish them: both integrated mark-transition matrices are `((0,1),(1,0))`. The extra information carried by the mean waiting time is a derivative at zero, not this already normalized zero-argument transform.

### Additional data or assumptions that distinguish the pair

- Calibrating r distinguishes them immediately; calibrating s alone does not, since s=1 in both. The pair is not a counterexample inside a class fixing both observed rates.
- The stationary laws are `(1/3,1/3,1/3)` and `(5/17,6/17,6/17)`. Each absolute stationary mark intensity is `1/3` in the first model and `6/17` in the second. Total event intensities are `2/3` and `12/17`. Thus a supplied infinite-statistics event rate in physical time distinguishes them.
- Normalized mark proportions are `(1/2,1/2)` in both, so normalized label frequencies do **not** supply that additional information.
- The traces are `-4` and `-33/5`; a common calibrated trace excludes this pair.
- Both generators satisfy detailed balance and have network entropy zero. This example demonstrates failure of two-point **generator** identification, not nonidentification of entropy, not equality of full laws, and not hidden irreversible currents.

## 4. A positive family, arbitrary two arguments, and rate calibration

For the explicit data above, all tuples

\[
\theta(\beta)=\left(\frac6{7-\beta},\ 1,\
\frac{(\beta+1)(\beta+2)}{7-\beta},\ \beta,\ 0,\ 0\right),
\qquad0<\beta<7,
\]

in the order `(r,s,a,b,c,d)` have exactly those same two full matrices. The proposed pair corresponds to beta=1,2. The stationary intensity of either mark is `3 beta/(8 beta+1)`, which is strictly increasing and therefore separates all members of this family if known exactly. No positivity or denominator exception is hidden: beta=0 loses the reciprocal leaf, and beta=7 is excluded because the denominator vanishes.

More generally, at any x-leaf `r,s,a,b>0,c=d=0`,

\[
G_x(\lambda)=u+\frac v{\lambda+b},\quad u=1/r>0,\ v=a/r>0,
\qquad G_y=1/s.
\]

For any two prescribed positive distinct arguments, let

\[
D=\frac{G_x(\lambda_1)-G_x(\lambda_2)}{\lambda_2-\lambda_1}>0,
\quad v_\beta=D(\lambda_1+\beta)(\lambda_2+\beta),
\quad u_\beta=G_x(\lambda_1)-D(\lambda_2+\beta).
\]

Every beta>0 with u_beta>0 gives the x-leaf `(1/u_beta,s,v_beta/u_beta,beta,0,0)` matching both complete matrices. An open interval around beta=b is admissible; `d u_beta/d beta=-D` ensures distinct generators. The y-leaf is symmetric. This establishes the worst-case necessity of three rather than relying on a dimension count or one fortuitous numerical pair. The original three-point proof supplies sufficiency.

If both r and s are independently known, subtract the known constant `1/r` or `1/s` from a row G with positive hidden entrance. The ratio of its two residual values is `(lambda_2+h)/(lambda_1+h)`, so two arguments determine h and the remaining rates even at leaves. In fact, only the observed exit rate at the hidden-leaf attachment is missing in the uncalibrated leaf ambiguity. A known absolute stationary mark intensity also identifies the leaf family: it determines `G_x(0)=1/nu-1/s`, and along the family

\[
G_{x,\beta}(0)=G_x(\lambda_1)+D\lambda_1+
\frac{D\lambda_1\lambda_2}{\beta},
\]

which is strictly decreasing in beta. These are additional exact summaries, not information contained in two transform matrices alone.

For completeness, one point does not generally identify a triangle. In tuple order `(r,s,a,b,c,d)`, the complete generators `(1,1,1,1,1,1)` and `(2,2,3,2/5,3,2/5)` share at lambda=1 the full matrix `((1/21,8/21),(8/21,1/21))` and differ at lambda=2. Scaling both generators by any prescribed positive lambda_0 gives the corresponding failure at that single argument lambda_0.

## 5. Empirical total variation is not the observation-error topology

For any nonempty finite observed row, define

\[
\widehat\mu_I=\frac1{n_I}\sum_{m:I_m=I}\delta_{(\tau_m,J_m)}.
\]

The true CTMC joint row law has a density `psi_{IJ}(t)dt` in time. Let A be the finite set of observed time/label atoms. Then `hat_mu_I(A)=1` and `mu_I(A)=0`, hence

\[
\operatorname{TV}(\widehat\mu_I,\mu_I)=1
\]

under the manuscript convention `TV=sup_A|P(A)-Q(A)|`. This holds for every finite nonempty row, not just with high probability; random realized atom locations do not alter the atomlessness of the true measure. Thus the raw empirical law cannot converge in TV, although its bounded Laplace tests and its weak law can converge. The true-law TV neighborhoods in the stability theorems must not be presented as shrinking TV balls around empirical atomic measures. A smoothing model would require its own bias/error analysis; no such smoothing is used here.

## 6. A finite-n moment confidence rectangle valid for sequential records

Fix K positive Laplace arguments **before observing the estimation record** (an independent pilot may choose them), `0<alpha<1`, and a deterministic number n of complete inter-mark intervals. There are `d=2*K*2=4K` joint moment coordinates. The initial mark can have any law; stationarity is not needed for this concentration argument because each resolved mark resets a known endpoint. Times and marks must satisfy the stated exact CTMC observation model.

Let `F_0` contain the first resolved mark. For `m>=1`, let `F_m` be the information generated by `F_0` and the first m complete marked intervals. The incoming mark I_m is `F_{m-1}`-measurable. For a fixed coordinate `(I,j,L)`, put

\[
Z_m=\mathbf1\{I_m=I\}
\left(e^{-\lambda_j\tau_m}\mathbf1\{J_m=L\}-\mu_{I,jL}\right).
\]

The strong Markov/reset property implies `E[Z_m|F_{m-1}]=0`. Conditionally, Z_m lies either in the singleton {0} or in `[-mu_{I,jL},1-mu_{I,jL}]`, an interval of length one. Conditional Hoeffding's lemma therefore gives, for every real eta,

\[
E[e^{\eta Z_m}\mid F_{m-1}]\le e^{\eta^2/8}.
\]

Iteration and Chernoff's bound (optimized at eta=`4t/n`) give

\[
P\left(\left|\sum_{m=1}^n Z_m\right|>t\right)
\le2\exp(-2t^2/n).
\]

No independence of successive rows or conditioning on random row counts has been assumed. Union over the d coordinates with

\[
t_{n,\alpha}=\sqrt{\frac n2\log\frac{2d}{\alpha}}
\]

gives the finite-sample simultaneous statement

\[
P\left\{\forall(I,j,L)\text{ with }n_I>0:
|\widehat\mu_{I,jL}-\mu_{I,jL}|
\le\frac{t_{n,\alpha}}{n_I}\right\}\ge1-\alpha.
\]

For n_I=0 impose no constraint on that row (equivalently use radius infinity); do not divide by zero or fill an unobserved row with pseudo-data. Coordinate intervals can be intersected with `[0,1]` without losing coverage. The confidence rectangle is conservative and does not establish efficiency. The displayed bound does not automatically apply to adaptively chosen n, same-record design selection, terminal censoring at a fixed physical horizon, or missed marks.

Intersecting this rectangle with a declared microscopic model class gives an honest confidence set for Q. Taking the entire entropy image, or a **certified** enclosing interval, transfers that coverage to entropy. Its upper endpoint may be infinite. An optimizer merely finding a large feasible entropy value gives a lower bound on that supremum; it does not certify a finite upper confidence limit. No optimization or numerical coverage experiment is claimed to prove this concentration statement. The mathematical proof is sufficient and the earlier exact all-time obstruction explains why unbounded answers must be retained.

## 7. What the existing estimator already supplies

The existing `analysis/revision/inference.py` meets the operational trajectory and pointwise-analysis requirements: it simulates actual stationary CTMC records, discards the initial censored interval, collects a fixed n complete intervals, computes per-incoming-mark joint Laplace means, fits all six rates under a disclosed numerical box, and accounts for row dependence with a martingale sandwich. It uses finite bounded moments rather than raw empirical-TV convergence, so the atomic-measure correction does not invalidate its implementation.

Its 900 seeded Monte Carlo trials already report bias, variance, optimizer/boundary/rank failures, interval availability, and conditional/overall coverage. Their results remain unchanged. The Wald intervals only have pointwise asymptotic justification at a regular nonequilibrium interior truth, and the low-count warning is a heuristic. Neither the warning, multistart optimizer success, nor observed Monte Carlo coverage is a uniform finite-sample coverage theorem. The rectangle above is a rigorous optional confidence-set construction, not a retroactive guarantee for those Wald intervals. Existing experiments use a random physical horizon induced by fixed n; they are not a fixed-window censored-likelihood experiment.

## 8. Reproducibility, falsification, and checks

Run from the repository root:

```powershell
.\.venv\Scripts\python.exe -B -m analysis.correctness.laplace_two
.\.venv\Scripts\python.exe -B -m unittest analysis.correctness.test_laplace_two -v
```

The script performs a generic positive-symbol full-resolvent/Schur check and exactly recovers all six symbolic rates from two points. It checks the explicit and arbitrary-two-point leaf families, literal full matrices at 1,2,3, exact stationary intensities, the one-point complete counterexample, and the boundary Jacobian ranks. `outputs/correctness-2026-09-15/laplace-two.json` contains commands, version, UTC execution time, script hash, domain exclusions, input tuples, full matrices, and exact results. The seven unit tests separately check literal rational data, time-zero amplitudes, calibration information, both leaf orientations, and nonsymmetric/rational complete triangles at noninteger Laplace arguments.

The candidate would fail if the direct full matrices differed at either proposed argument, if reciprocity/irreducibility failed, if B omitted r or s, or if full-law equality had been inferred from two evaluations. Those checks passed. Generic recovery would fail if any positive-domain denominator vanished or a complete competitor escaped the off-diagonal recovery; the sign conditions above address those exceptions. The initial script run stopped at a structural SymPy-expression comparison (`6/(7-beta)` versus an equivalent sign-normalized rational representation); the assertion was corrected to exact cancellation of the difference and then all checks passed. This was not a failed mathematical candidate. No floating-point approximation, optimization tolerance, search failure, or rare-rate clipping supports the exact claims.
