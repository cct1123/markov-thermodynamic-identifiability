# Independent global five-state proof audit — 2026-09-15

## Verdict and scope

The balanced five-state endpoint and supercritical whole-fiber conclusions survive this audit in the declared class: finite irreducible CTMCs, reciprocal support with strictly positive rates on each present direction, exactly one resolved microscopic reverse pair with fixed visible endpoints, complete all-time joint next-event kernels, and at most five total states. Hidden permutations do not count as distinct generators. No theorem-level counterexample or unclosed logical gap was found. This conclusion rests on the expanded arguments below, not on preceding favorable reviews or a failure of numerical search.

The existing manuscript compresses several essential proof steps enough that they should be repaired before publication. The fixes are explicit derivations, not weaker theorem statements. A replacement for Appendices A and B, with compatible section/equation labels, is [global-proof.tex](global-proof.tex). The coordinator owns manuscript integration.

The most consequential repairs are:

1. Prove full minimality from hidden reachability/observability and the directly resolved visible plane. Also justify invertibility of the killed generator before using it to pin normalization.
2. Make the Perron-to-triangle step explicit, including strictly positive barycentric coordinates of the origin and why neither degenerate triangles nor rays at infinity represent a connected admissible competitor.
3. Include the omitted but necessary right-output inequality `Q_v >= R_w(c-1)` in the list of inequalities. Derive the entire reflected `d<0` chain rather than referring to it.
4. Treat the region `ac-kd<=0` separately before dividing by the right invariance coefficient. Identify both algebraic intersections and prove which bound is active on each interval.
5. Track strictness through each relaxation, especially the final increase of `W`, so that equality at the threshold fixes the original triangle rather than merely a relaxed one.
6. Derive the unique positive column scaling from row normalization. A unique cone alone is not generator uniqueness; endpoint existence and entropy separation still require the separate certificate.

## What was actually inspected and executed

Inspected the current full `manuscript/supplementary/proofs.tex` and, in particular, its observation-equivalence, global-cone, endpoint, hidden-pair and subcritical sections; `analysis/balanced-cone-bound.md`; the explicit reflected derivation in `analysis/theta-fast-spectral-audit.md`; and the three accepted bound, sufficiency and endpoint checkers. Their inputs and current hashes are recorded in the new output.

Executed from the repository root:

```powershell
.\.venv\Scripts\python.exe -B analysis/correctness/global_independent.py
```

The run completed with all assertions passing. It wrote only [global-independent.json](../../outputs/correctness-2026-09-15/global-independent.json). It independently checked derivative/factor identities, exact sign bounds, all eight low-pole opening velocities, all eight fast-opening velocities, a two-mode similarity and its repeated-pole limit, and the finite reciprocal hidden-support partition. It also freshly re-executed `check_balanced_cone_bound.py`, `check_balanced_cone_sufficiency.py`, and `check_balanced_fold.py` with JSON writes intercepted; all assertions passed and every historical JSON hash remained unchanged.

The independent calculation and historical re-executions are separated in the output. Re-running an accepted checker is not independence from its encoding. New exact calculations use SymPy and rational interval arithmetic; no approximate sign, optimizer result, feasibility solver or formal verification is used. The universal conclusions require the conventional arguments below and in the replacement text.

## A. Normalization and all competing dimensions

For any admissible finite irreducible competitor, the observed pair is eventually hit almost surely. A direct uniform proof is available: choose for every state a finite path leading to an observed jump and a sufficiently large common time; each has positive probability. The minimum over finitely many starting states is positive. The strong Markov property bounds survival geometrically over successive time blocks. Therefore the killed generator is Hurwitz and invertible. This closes the premise of `TS1=T1 => S1=1`.

The visible columns of `B` span the visible coordinate plane. This plane is in the full reachable space. Applying `T` and subtracting that plane supplies the hidden columns of `Y`; repetition supplies `H^jY`. The displayed nonvanishing minors then give full reachability. For observability, `Rv=0` first sets the visible part to zero, and the subsequent equations recursively imply `XH^j v_H=0`; hidden observability sets the hidden part to zero. Thus the source's five-dimensional full realization is minimal for **every** `z>0`, including `z=2` and the coincident hidden poles. This is not a pole-count argument.

The common block Hankel rank is five. A realization of dimension below five cannot produce it. A five-state competitor must also be minimal, because a lower-dimensional minimal realization of that competitor would factor the same rank-five Hankel matrix through a smaller space. Thus all cap-admissible competitors fall under the unique realization similarity theorem. The reset and event maps pin both visible rows and columns; positivity is required of the resulting generator, not of the hidden similarity matrix.

Attempts to evade the cap through a nonminimal five-state realization, a different signed similarity, or a hidden-coordinate chart singularity therefore fail for explicit reasons. The six-state split is outside this cap and remains a valid unboundedness construction. The audit does not claim minimal linear and minimum positive orders coincide in general.

## B. Exhaustive disconnected support analysis

On three hidden states, reciprocal support has eight labeled undirected edge sets: one with component sizes `(1,1,1)`, three with sizes `(2,1)`, and four connected supports. This finite partition was checked independently. It would not be exhaustive in a class allowing arbitrary one-way hidden edges, but that is not the declared class.

At `z>=21/2`, the inherited hidden eigenvalues `-alpha,-beta,-2z` are distinct, with `-alpha` dominant. A hidden singleton must contribute its nonnegative outer-product residue at the eigenvalue assigned to it. Minimality prevents a source mode from disappearing in an unobservable singleton. Hence three singletons, or a singleton at `-beta`, contradict the mixed-sign residue. If a singleton were at `-alpha`, the irreducible remaining pair would have dominant eigenvalue `-beta`; its Perron residue is a nonnegative outer product after multiplication by nonnegative input/output blocks, giving the same contradiction.

Only the fast singleton remains. The pair's zeroth transfer is `diag(6,42)`. Every shared visible attachment would contribute a strictly positive off-diagonal product, because reciprocity equates entrance and exit supports. Nonnegative terms cannot cancel. To supply both positive diagonal moments with two states, one pair state must attach only to `x`, the other only to `y`. The possibility of a state with no visible attachment is excluded by these two diagonal moments, not merely by intuition about connectivity.

The remaining rate elimination is valid because every divided quantity is a positive present rate. Multiplying the two off-diagonal moments and dividing by the diagonal moments gives `h0*k0=20`. The first off-diagonal ratio gives `h0(11-k0)=8(7-h0)`, so `19h0-h0k0=56`. Thus the pair rates are uniquely the source rates. A possible scalar freedom in factoring the fast residue is removed by the singleton's exit sum `2z`. All disconnected possibilities have therefore been disposed of before the triangle argument begins.

## C. Finite triangles, labeling and excluded boundary strata

Let `b=V^{-1}e1` and `a_P^T=e1^T V`. For irreducible Metzler `H'`, these are nonzero Perron eigenvectors. Their signs are fixed: `X'b=p>0` with `X'>=0` makes `b>0`, and `a_P^T b=1` makes `a_P>0`. Thus every first coordinate `s_i` of a column of `V` is positive. The sectioned vertices are `V_i/s_i`, and

`e1 = sum_i (b_i s_i) (V_i/s_i)`, with all `b_i s_i>0` and sum one.

This explicitly proves that the origin is strictly interior. Invertibility of `V` proves affine independence. Every finite physical competitor produces a finite triangle, even if arbitrarily ill-conditioned; no common bound on triangle coordinates is needed. A sequence with a ray approaching the first-coordinate-zero plane is not an extra finite competitor. A ray exactly on that plane is incompatible with the strict left Perron vector in this branch.

The two-positive/one-negative vertex labeling is also exhaustive. Nonpositive-height wedge points have abscissae in `[-m,1]`. With only one positive-height vertex, obtaining the positive input at abscissa `1` forces that vertex's abscissa to be at least `1`; the positive input at `-m` forces it to be at most `-m`, an impossibility. The interior origin requires at least one negative-height vertex. There are only three vertices, so there is no zero-height vertex. The negative vertex has `-m<d<1`; the two others extend to the left and right and have `ell>=m,c>=1`.

The endpoint possibilities `ell=m,c=1,d=0` are initially retained. At high `z`, `P<2<B0<A` later excludes `ell=m`. The right invariance inequality and `aQ_v-W>0` exclude `d=0`. The value `c=1` is retained in the envelope domain; it is not silently discarded. No extra assumption that every microscopic rate is strictly positive on a complete graph is made in this necessity argument.

## D. The reflected inequality, fully derived

The manuscript's short list omitted `Q_v>=R_w(c-1)`, although it follows from the already stated wedge. It is essential in the reflected calculation and is now displayed explicitly in the replacement proof.

For `d<0`, right lower-face invariance gives `Q_v<W/a`. Upper input containment, right-output positivity and left-lower input containment then yield

\[
\begin{aligned}
A&\le Q_v+\frac{(c-1)P}{\ell+c}
 \le Q_v\left[1+\frac{P}{R_w(\ell+c)}\right]\\
 &<\frac{W}{a}\left[1+\frac{B_0+W}{R_w(m+d)}\right]\\
 &\le\frac{L}{a}\left[m+d+\frac{B_0+W}{R_w}\right]
 <\frac{L}{a}\left[m+\frac{B_0+1}{R_w}\right].
\end{aligned}
\]

Every denominator is positive, and the two strict steps use respectively `d<0` and `W<1`. The final scalar comparison to `z` is exact after clearing its positive denominator; the numerator is `72(z-10)^2+836(z-10)+835`. The new script verifies that identity. Thus the reflected branch is actually excluded; it is not suppressed by choosing a favorable orientation.

For `d>=0`, the bounds give `P<W/a<2`, `Q_v>=A`, and `aQ_v-W>0`. Rewriting right invariance as `c(aQ_v-W)<=kdQ_v` already forces `d>0`. Combining it with `c>=1` gives the apex inequality. Its exact margin at `z=10.5` exceeds `0.014259`, and `k-R_w/z` is strictly increasing. Hence every candidate lies on the specified side of the wedge apex. This is a uniform inequality over candidate triangles, not a margin observed only at the endpoint witness.

## E. Right-envelope pole and monotone relaxations

The left maximum has a unique positive intersection because its quadratic in `t=ell-m` has positive leading coefficient and negative constant. Since `g` increases, every feasible left vertex satisfies both `ell<=ell_*` and `P<=P_*`. While replacing these coordinates, `Q_v>=A>2>P_*` retains the required strict derivative signs. Unused constraints may fail after relaxation; this is harmless because the construction is an upper bound. It would be harmful only if the relaxed triangle were asserted to exist physically, which it is not.

For the right vertex, define

\[
\mathcal L(c)=\frac{A+W}{1-d}(c-d)-W,\qquad
\mathcal H(c)=\frac{cW}{ac-kd}.
\]

For `c<=kd/a`, invariance imposes no upper restriction on positive `Q_v`; division by `ac-kd` would be invalid. For `c>kd/a`, the exact identity is

\[
\mathcal L(c)-\mathcal H(c)
=\frac{a(A+W)(c-d)(c-c_*)}{(1-d)(ac-kd)},\qquad
c_*-\frac{kd}{a}=\frac{kW(1-d)}{a(A+W)}>0.
\]

Thus the line is active up to `c_*`, including any interval below the pole, and the hyperbola is active afterward. The other root `c=d<1` lies outside the physical domain. If `c_*<1`, the hyperbola at one is already below `A` and decreases afterward, so there is no feasible `c>=1`. This proves `c_*>=1` without assuming it.

Writing `H_c=P_*+t(Q_v-P_*)/(ell_*+c)` makes monotonicity transparent. Along the line its derivative is strictly positive. Along the hyperbola it is strictly negative on its **whole** domain beyond the pole because `mathcal H(c)>W/a>P_*`. This last inequality strengthens the manuscript's argument that only heights above `B0` matter and removes any concern about a distant second maximum.

For the last saturation, `dt/dW>0` follows by implicit differentiation with strictly positive denominator `L[a(m+t)+kdm/(m+t)]`. Also `Q_*^v` increases and `r_c` decreases. The three partial derivatives of the final envelope have numerator signs `+,+,sign(Lt-Q_*^v)`, and `Lt<2<A<=Q_*^v` persists throughout increasing `W` to `R_w(1-d)`. Every step is therefore strict unless its original variable already equals the maximizing value.

These identities were derived and checked independently in the new script. The proof allows unbounded candidate `c` or `ell`; the envelope inequalities apply to every finite candidate and do not appeal to compactness or a finite search box.

## F. Equality rigidity and physical existence

Let an original feasible triangle exist at the threshold. Its original upper input height is at least `B0`, while its final relaxed and saturated height is at most `B0`. Every intervening inequality must therefore be equality. Strictness of the last `W` step forces the original `W=R_w(1-d)`. The discriminant-zero numerator has the sole root `t=t_*`. The rational formula for `epsilon` then fixes `d,W` uniquely. Equality in the left and right relaxations fixes the other four vertex coordinates. This argument explicitly refers back to the original triangle; it does not infer its uniqueness merely from a unique relaxed optimum.

The active constraints have paired physical meanings. The left vertex's zero `x` output pairs with the zero `x` input barycentric coordinate because `(1,A)` lies on the opposite edge. The bottom vertex's zero `y` output pairs with the zero `y` input coordinate because `(-m,B0)` lies on the upper edge. The two tangent constraints force both directions between the two upper vertices to vanish. Zero rates are allowed only in these reciprocal pairs in the endpoint model. Strict positivity of the remaining rates, positive stationary masses, and a nonzero entropy gap do not follow from these zeros alone; they are supplied by the separate exact endpoint certificate.

For a sectioned vertex matrix `V`, all remaining positive column scalings form a vector `w`. Row normalization requires `Hbar*w+Ybar*1=0`. The eigenvalues of `Hbar` are fixed nonzero negative values, so `w=-Hbar^{-1}Ybar*1` is unique. In an existing physical competitor it is positive; the certificate proves this positivity for the actual candidate. A permutation of vertices produces only the corresponding hidden permutation of the normalized generator. This closes the cone-to-generator uniqueness step.

The endpoint checker independently verifies the physical path in the exact real algebraic field, all prescribed zeros, positivity of every present rate, stationary normalization, ten exact kernel derivatives, and disjoint rational entropy intervals. Re-execution passed. The proof never uses the displayed rounded matrix as an equality certificate.

## G. Subcritical coverage and repeated poles

The four intervals still cover every `0<z<z_*`:

- `0<z<alpha/2`: the eight originally missing directed rates have strictly positive first derivatives under the displayed normalized hidden direction. The new script re-derived all eight exactly, including the coefficients proportional to `alpha-2z`. Therefore a sufficiently small positive step opens a complete generator without altering the kernel. `z=2` belongs to this interval, so its exit-chart singularity causes no gap.
- `alpha/2<=z<=beta/2`: the two-mode construction uses a similarity of a two-dimensional modal block and a separate positive singleton. The new script rechecked the block formula, rank-two input matrix, and exact scalar limit `Hbar=-beta I` at the upper endpoint. The positivity intervals are strict at both endpoints. Coincident residues add; distinct poles are not needed for this construction. Rank two makes the pair's full external exits unequal after positive row scaling. At the upper endpoint the unjoined pair has equal total escapes, exactly the alternative hypothesis of the hidden-pair lemma.
- `beta/2<=z<=10.5`: all eight fast-opening derivative formulas were independently re-derived. The manuscript's midpoint inequalities ensure strict positivity; notably `L_s M_s>=20` together with `q>M_s/5` gives the apparently borderline derivative `L_s q-4>0`. The equality endpoint does not leave a zero derivative.
- `10.5<=z<z_*`: positive discriminant gives positive upper-input slack at the quadratic maximum. The nonactive margins are certified on the whole stated rational interval. Successive sufficiently small changes of `W`, the left vertex, and the right height make all input, output and inward face constraints strict. The finitely many already strict margins persist at each fixed `z`; no uniform perturbation size near the threshold is claimed. The initial possibly one-way realization is not admitted as physical before these changes. The positive Hurwitz Metzler inverse gives positive normalization, and transfer equality at zero fixes the visible row sums.

The complete resulting model is linearly minimal. Equal full external exit rows for two fully hidden states would make the subspace `v_h=v_k` invariant under `T` and contain all columns of `B`, violating reachability. Thus a complete realization has the unequal pair required by the entropy-divergent shear. Every model before the shear endpoint retains positive reverse rates; the limiting one-way model itself is not asserted admissible. No bounded optimization value is being used as evidence of divergence.

## Limits and stopping rationale

The audit targeted adversarial escapes through nonminimal competitors, disconnected components, zero-height vertices, zero first-coordinate rays, reflected bottom positions, division across the right-envelope pole, nonmonotone relaxed regions, and equality lost during relaxation. Each is excluded or retained by an explicit argument above. No numerical search was necessary or sufficient to establish this exhaustion, and none was used as a surrogate.

The main remaining verification dependence is conventional human review of the mathematical statements and their exact-script encoding; the result is not formally verified. The audit does not extend the theorem to unknown state count, one-way support, unknown event endpoints, unresolved parallel channels, arbitrary observation graphs, or physical dissipation without the appropriate local-detailed-balance/channel assumptions. The local asymmetry extension still inherits these global arguments and additionally needs its own domain/sign certificate; its wider plotted continuation remains numerical.

The assigned audit is complete because its consequential proof omissions now have explicit analytic replacements and their exact algebraic dependencies were executed successfully. More generic searches would not strengthen universal support exhaustion. Integration should use the replacement text or equivalent lemmas, retain the separate endpoint existence/entropy certificate, and then run the coordinator's assembled manuscript checks.
