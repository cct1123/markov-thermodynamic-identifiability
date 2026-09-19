# Independent mathematical referee report

Reviewed baseline: `c7ff789b2e9db090935b5bf16eb9a8d775f833c2`.
Checkpoint: 2026-09-19 04:53 UTC. Line locators below refer to that baseline.

This is a bounded mathematical review of the actual manuscript and proofs, not a reproduction of earlier referee verdicts. I read `manuscript/main.tex`, the observation-graph, two-Laplace, compact-prior and rare-event sections, and the realization, invariant-triangle, hidden-pair and splitting proofs. I did not independently repeat the entire endpoint interval certificate or perform a new literature-wide priority search. Claims of priority require the separate literature audit.

## Assessment

The strongest difficult result is the five-state support exhaustion, especially its global cone geometry and endpoint equality propagation. The genuinely general result is the distinction between exact identification and a local upper entropy ceiling. The manuscript handles that distinction carefully: an exact singleton can sit arbitrarily close to observations with unbounded compatible entropy. These are different assertions, and the five-state supercritical family makes their difference mathematically consequential.

The current presentation leaves substantial generality unused. Its one-pair criterion is organized by state count, although the mechanism is actually controlled by how many vertices the detector leaves uncovered. The acknowledged one-uncovered-vertex gap in `supplementary/observation-graph.tex:65–72` can be closed by the same scalar Schur-complement reconstruction already used for three states. More strongly, every complete-support source with at least two uncovered vertices has an *exact* entropy-divergent compatible path, without linear minimality. This goes beyond merely finding divergent models in every data neighborhood.

I found no concrete contradiction to an existing theorem in the inspected arguments. That is a bounded audit conclusion, not a full correctness certificate. The new structural statements below have explicit conventional proofs and exact example checks. They should still receive independent verification before promotion into the manuscript.

## Correctness and interpretation points requiring care

1. **Exact image versus local ceiling.** `main.tex:211–240` proves a local upper-ceiling criterion. `main.tex:403–447` does not determine the complete subcritical entropy image; its attainable half-line is not an infimum calculation. The stronger complete-source result below supplies an exact half-line and must not be silently extended to arbitrary sparse sources. The endpoint's two values and the supercritical singleton coexist with absence of a local ceiling, so an exact-image theorem and a local-ceiling theorem need separate statements.

2. **Fixed trace has a graph-dependent exceptional case.** At full vertex coverage, fixing all observed rates and the source trace can prohibit opening any missing edge. For the unit tree on three vertices, observe both tree edges and fix all four rates and trace −4. Every unobserved rate must remain zero; the class is a singleton despite sparse support. The baseline already flags the need for unobserved slack at `supplementary/observation-graph.tex:55–63`. A generalized fixed-trace theorem must preserve that qualification. This is a counterexample to an incautious extension, not an error in the stated one-pair theorem.

3. **First boundary, not an arbitrarily chosen boundary.** In `supplementary/proofs.tex:542–573`, the hidden shear must stop at the first zero of its internal rate polynomial or an external exit. Following the external ratio all the way when the internal polynomial vanishes earlier leaves the physical class. The baseline handles this correctly. The independent check below deliberately reaches an internal zero first and verifies the opposing flux remains positive.

4. **Nonminimal complete models need their own branch.** The reachability observation at `supplementary/proofs.tex:575–576` excludes equal external exit rows only under minimality. It cannot establish an exact unbounded fiber for *every* complete source. Equal-row strong lumping closes precisely that gap, with no appeal to minimality and no change in trace.

5. **The rare-rate exponent is tied to its chosen path.** `supplementary/rare-event.tex:1–28` is correct as a specified testing problem. The number 9 and the square of entropy come from choosing `k=exp(−1/e²)`. They are not a universal entropy-dependent sample-complexity law. Reparameterizing rare-rate paths changes the relation between entropy and the testing lower bound. A broader statistical contribution needs a declared parameter class and a matching upper result or an invariant modulus, not a stronger adjective around this example.

6. **Global support exhaustion remains the most fragile proof obligation.** `supplementary/proofs.tex:206–474` must cover the negative bottom-abscissa branch, both sides of the hyperbola pole, noncompact triangles, and every equality relaxation. The printed proof explicitly addresses those branches. Exact checks of its final discriminant or endpoint matrix alone do not independently establish the intervening geometric reduction. I found the chain logically consistent on direct inspection but did not replace it with an independent global proof. Preserve the current conservative proof status.

## New result: exact dichotomy at complete sources

**Statement.** Fix a known finite vertex set, a nonempty reverse-closed collection of individually resolved observed edges, and the same CTMC/time-reversal assumptions as the manuscript. Let `u` denote the number of vertices incident to no observed edge. If a source generator `Q₀` has complete reciprocal support, then:

- for `u≤1`, its full marked waiting kernel determines its generator on that vertex set;
- for `u≥2`, its exact entropy image contains `[σ(Q₀),∞)`, even when all observed rates, the source trace, and complete support are retained.

The upper interval is an attainable subset, not a claim that no smaller entropy is compatible. No minimality is required. Each prelimit model is irreducible, has positive rates in both directions, and has finite entropy. All rates are bounded by `τ=−tr Q₀`.

The `u≤1` proof appears in the following section. Here is the full `u≥2` argument, audited independently against the baseline shear formulas.

### Unequal full external exit rows

Choose two uncovered states `h,k`. Let `J=V\{h,k}` and let their external exit rows be `Y_h=(q_hi)_{i∈J}`, `Y_k=(q_ki)_{i∈J}`. All entries are positive because the source is complete. Suppose these rows differ. After interchanging `h,k` if necessary,

`r* = min_{i∈J} Y_hi/Y_ki` lies strictly between zero and one.

Write `m=q_hk>0`, `n=q_kh>0`, `λ_h=m+ΣY_hi`, `λ_k=n+ΣY_ki`. Embed

`U_e = [[1−e,e],[0,1]]`

on the `h,k` coordinates of `S_e`, with identity elsewhere, and set `Q_e=S_e⁻¹Q₀S_e`. Its determinant is `1−e`; also `S_e 1=1`. The outside entrances and exits are

`q_ih(e)=(1−e)q_ih`, `q_ik(e)=q_ik+e q_ih`,

`q_hi(e)=(Y_hi−eY_ki)/(1−e)`, `q_ki(e)=Y_ki`.

The internal pair is

`q_kh(e)=n(1−e)`, `q_hk(e)=f(e)/(1−e)`,

where `f(e)=m+e(λ_k−λ_h)−n e²`. This concave quadratic has exactly one positive root

`e_f = [(λ_k−λ_h)+sqrt((λ_k−λ_h)²+4nm)]/(2n)`.

Set `e*=min(r*,e_f)`. Then `0<e*<1`. For `0≤e<e*` every displayed off-diagonal is strictly positive; all other off-diagonals are unchanged. Row normalization follows from `S_e1=1`; the trace follows from similarity. Thus the whole prelimit path stays inside complete reciprocal support.

Because no mark touches `h,k`, every observed jump matrix commutes with `S_e`, `R S_e=R`, and `S_e B=B`. Consequently the killed generators are similar and

`R exp(T_e t) B = R exp(T₀t) B`

for every nonnegative time, with every observed rate fixed. This is exact equality of the whole marked kernel, not equality of finitely sampled transform values.

If `π` is the source stationary row vector, the unique stationary row vector is `π(e)=π S_e`. Explicitly,

`π_h(e)=(1−e)π_h`, `π_k(e)=π_k+eπ_h`, and `π_i(e)=π_i` outside the pair.

Every limiting stationary mass is strictly positive because `e*<1`. All rates have finite limits for the same reason.

If `e*=e_f`, then `q_hk(e)→0` while the opposing flux tends to

`(π_k+e*π_h)n(1−e*)>0`.

If `e*=r*`, choose an external minimizer `i`. Its exit `q_hi(e)→0` while the opposite flux tends to

`π_i(1−r*)q_ih>0`.

At a simultaneous boundary either argument works. The corresponding pair contribution `(F−G)log(F/G)` tends to positive infinity. Every other pair contribution is nonnegative, so cancellation is impossible. This proves `σ(Q_e)→∞`.

### Equal full external exit rows

Suppose instead that `Y_h=Y_k=y`, and put `λ=Σ_i y_i>0`, `m₀=q_hk`, `n₀=q_kh`, `c=m₀+n₀>0`. Leave every outside rate and every external entrance/exit unchanged. Vary

`m=q_hk` in `(0,m₀]`, and set `n=q_kh=c−m`.

For all these parameters, both internal rates are strictly positive, every external rate is strictly positive, and the total internal rate `m+n=c` preserves the trace. The source occurs at `m=m₀`.

Let `C` merge `h,k` into one aggregate state `H`. Since the full external exit rows coincide, `Q_m C=C Q̄`, where the aggregate generator `Q̄` does not depend on `m`. Every marked edge avoids `h,k`, so also

`T_m C=C T̄`, `B=C B̄`, and `R C=R̄`.

It follows directly from the exponential power series that

`R exp(T_m t) B = R̄ exp(T̄t) B̄`

for all times and all `m`. This establishes exact kernel preservation by strong lumping. It remains valid if some other outside vertices are also hidden and if the original realization is nonminimal. Strong lumping also preserves the stationary marked-record law, including censored ends, because the aggregate initial stationary distribution and every observed jump are unchanged.

Let `π̄_H` be the stationary aggregate mass, and let the fixed outside stationary masses be `π_i`. Define the positive incoming stationary fluxes

`A=Σ_{i∈J}π_i q_ih>0`, `B_in=Σ_{i∈J}π_i q_ik>0`.

Aggregate stationarity gives `A+B_in=λ π̄_H`. Solving the two hidden balance equations yields

`π_h(m)=(A+π̄_H n)/(λ+c)`,

`π_k(m)=(B_in+π̄_H m)/(λ+c)`.

Their sum is `π̄_H`. Both limits as `m↓0` are strictly positive. The forward internal flux `π_h(m)m` vanishes, whereas the reverse tends to

`B_in c/(λ+c)>0`.

Thus the internal entropy term diverges. The other rates are fixed and all stationary masses have positive limits, so all other entropy terms have finite limits. This is an exact data-preserving divergence within the original dimension, complete support and trace, and it does not rely on nonminimal states being added.

### From a divergent path to an attainable interval

Both constructions begin at `Q₀`, remain in the physical class, and give continuous finite entropy along every prelimit parameter interval. Since entropy diverges at the omitted boundary, the intermediate value theorem gives every value in `[σ(Q₀),∞)`. There is no assertion about values below `σ(Q₀)` or about an attained global minimum.

## Closing the one-uncovered-vertex gap

This derivation does not assume complete support; irreducibility and reciprocal support suffice. Let `C` be the `p=N−1` covered vertices and let `h` be the uncovered vertex. In this order write

`T = [[A,a],[bᵀ,−h]]`, with `h=bᵀ1>0`.

Here `a_i=q_ih≥0`, `b_i=q_hi≥0`, and `A=T_CC`. Select for each covered vertex `i` one observed mark ending at `i` and one observed mark beginning at `i`, with unknown positive rate `d_i`. Set `D=diag(d_i)`. The selected square transform submatrix is

`F(λ)=K_CC(λ)D`,

where `K=(λI−T)⁻¹`. Its inverse is

`M(λ)=D⁻¹[λI−A−abᵀ/(λ+h)]`.

This square inverse exists at each positive `λ`: its Schur complement is a nonsingular M-matrix. If `W(λ)` is the same selected row set with *all* observed columns, the measured vector

`c=M(λ)W(λ)1`

equals `D⁻¹ o`, where `o_i` is the total rate of observed marks leaving `i`. This step is essential when a covered vertex has more than one outgoing observed mark; simply subtracting the scalar one in the three-state formula would be wrong.

Because `A1+a=−o` and `bᵀ1=h`,

`G(λ)=[M(λ)1−c]/λ = D⁻¹1+D⁻¹a/(λ+h)`.

At least one `a_i` is positive. On that source-selected row, three distinct positive arguments recover `h` by exactly the divided-difference ratio in the manuscript's three-state proof. The two-term representation then recovers `u_i=1/d_i` and `v_i=a_i/d_i` for every row, including rows with `a_i=0`. Hence `D` and `a` are known.

For two of those arguments define

`Z=[D(M₂−M₁)−(λ₂−λ₁)I](λ₁+h)(λ₂+h)/(λ₂−λ₁)`.

Then `Z=abᵀ`. Divide any row having `a_i>0` by `a_i` to recover `bᵀ`, and recover

`A=λ₁I−D M₁−Z/(λ₁+h)`.

For every additional observed column `w_J`, the vector `M₁w_J` has its sole possible nonzero entry at the mark's source vertex, equal to `q_J/d_source`. Thus every observed rate is recovered and `Q=T+E` follows. All denominators are nonzero at the source and remain nonzero locally. The inverse is rational and locally Lipschitz in its finite measurements, hence locally Lipschitz in row total variation and continuous under weak row-law convergence, with no rate cap.

At a complete source, two positive arguments suffice. Choose any observed edge `i→j`; then `A_ij=0`, and

`M_ij(λ)=−a_i b_j/[d_i(λ+h)]≠0`.

Its ratio at the two arguments recovers `h`, after which the above formulas apply. With no uncovered vertex, the baseline full-coverage proposition already gives the same two-argument statement. Three is a worst-case universal upper bound for one uncovered vertex; the original three-state leaf example proves that two cannot suffice uniformly across every such graph/support class. It does not prove a separate three-point necessity theorem for each larger observation graph.

This proof works when the observation graph on covered vertices is disconnected. For example, two disjoint observed pairs cover four of five vertices and suffice for complete-source identification; two pairs sharing one vertex cover only three of five vertices and leave an exact unbounded entropy fiber. Coverage, rather than connectedness of the observation graph, is the key combinatorial quantity.

## Resulting local-ceiling classification

In the unrestricted fixed-vertex-set class with unknown reciprocal support, the preceding inversion and the baseline missing-pair/hidden-pair constructions give:

**A finite local upper ceiling exists exactly when the source is complete and at most one vertex is uncovered.**

For a noncomplete source, a missing pair is necessarily unobserved. Open it with rates `e` and `exp(−1/e²)`. Generator convergence gives waiting-law convergence, while positive limiting stationary mass yields divergent entropy. With two or more uncovered vertices, completion followed by the exact divergent path gives the baseline neighborhood obstruction. At a complete source with at most one uncovered vertex, the local rational inverse keeps rates inside a compact positive neighborhood and entropy is smooth there.

If every observed rate and the source trace are also fixed, let `U₀` be the sum of source rates on all unobserved ordered pairs. The classification has an extra finite case: `U₀=0`, which forces the constrained class to be a singleton. Otherwise, the noncomplete-source construction can subtract the newly added rates from an existing positive unobserved rate; this preserves the trace and observation-rate calibration. Irreducibility forces `U₀>0` whenever any vertex is uncovered. The complete-source exact divergent paths already preserve the trace.

## Independent exact checks

Run from the project root:

```powershell
.\.venv\Scripts\python.exe -B outputs/novelty-loop-2026-09-19/referee_checks.py
```

Inputs are exact integer generators and declared observation pairs embedded in [referee_checks.py](referee_checks.py). Output: [referee_checks.json](referee_checks.json). The output records Python 3.9.12, SymPy 1.14.0, and the script SHA-256. Arithmetic is exact rational/symbolic; no seed, optimizer or tolerance is used.

Executed results:

- three-argument reconstruction exactly recovers a four-state complete source, a five-state complete source with disconnected observed graph, and a six-state source whose sole hidden vertex is a leaf;
- an equal-exit four-state family has a symbolically constant full two-by-two Laplace matrix, trace −52, positive limiting stationary masses `(5/12,1/4,29/132,5/44)`, and reverse internal limiting flux `45/44`;
- an unequal-exit four-state shear reaches its internal boundary `sqrt(2402)−49` before its external boundary `1/2`; exact intertwining identities, normalization, stationarity, trace and positive opposing flux are verified.

An initial extension of the check harness used structural equality on an unsimplified symbolic row-sum expression and failed that assertion. Replacing it with exact rational cancellation made the identity explicit; the final run passes. This was a check-expression issue, not a failed scientific identity. The examples audit different exceptional mechanisms; they do not prove the general theorem by finite enumeration.

## Plan for substantially stronger research

1. **Complete the graph theorem and exact complete-source dichotomy now.** Promote only after independent proof and adversarial example checks, including disconnected observation graphs, hidden leaves, equal exit rows, a first internal shear boundary, and the zero-unobserved-mass trace exception. This changes the contribution from a special one-pair state-count criterion into a detector-placement theorem, while retaining exact versus local distinctions. At complete sources it yields a sharp observation-count consequence: at least `ceil((N−1)/2)` observed reverse pairs are needed to cover all but one vertex, and such a placement is sufficient. Counting alone does not certify a poor placement.

2. **Classify the topology of exact entropy images before further special families.** A promising general statement is that a fixed-cap exact entropy image is a finite union of intervals and points. On each reciprocal support, the finite Markov-parameter equality certificate makes the compatible rate set semialgebraic. It has finitely many connected components, and stationary entropy is continuous on each fixed-support component, so each image is an interval. A finite union over supports and dimensions completes the argument; support boundaries and open interval ends must remain explicit. This is a consequence of established semialgebraic topology rather than new topology in itself. Its scientific value is to delimit possible entropy fibers and organize the unresolved subcritical lower-range question. Do not claim an attained infimum or all-image equality without further work.

3. **Seek a class-wide quantitative estimation theorem only after the structure is settled.** Fix physically defensible rate/dimension restrictions and an observation graph, define a modulus of entropy over finite Laplace-measurement neighborhoods, and seek matching testing and reconstruction bounds. This would distinguish detector-conditioning losses from a rare reverse-rate singularity. Additional Monte Carlo runs or another chosen exponential path would add little novelty without a theorem specifying what is optimal and over which class.

The first direction is ready for a bounded proof-and-verification loop. The second is a plausible next structural loop. The third is a longer project and should not delay a coherent paper around the first two exact mechanisms and the existing support-exhaustive five-state example.

## Final-draft audit of the consolidated theorem

At 2026-09-19 05:01 UTC I independently checked [COVERAGE-THEOREM.md](COVERAGE-THEOREM.md), including the new arbitrary-two-arguments witness. The inspected version has SHA-256 `5cbbea286800a33a8917b671b897850bfadc14ce76a5ddc2f6c0392cea58d5a6`. This follow-up checks mathematical consolidation, not literature priority.

**Outcome: no outstanding mathematical finding in the inspected draft.** The audit explicitly covered the following potential failure points:

- Aggregating next marks by their origin gives `D=diag(total observed outgoing rates)`, so subtracting `1` in its equation (1) is correct. Equation (5) recovers each individual rate from a positive diagonal resolvent entry; no hidden calibration assumption remains.
- The two-point branch has `A_ij=0` for its chosen observed edge under every admissible competitor, not merely at the source. The same nonzero inverse entry therefore forces every matching competitor into the reconstruction branch. This proves unknown-support uniqueness on the fixed vertex set.
- The rational denominators are nonzero at the source; shrinking the finite-measurement neighborhood consequently confines every admissible competitor to a bounded positive-rate neighborhood. This establishes the finite-Laplace-test local ceiling at complete sources. The negative constructions either preserve all-time data exactly or converge in row TV, and therefore also defeat every fixed finite set of bounded Laplace measurements. No passage from finite tests to all-time equality is being inferred in the wrong direction.
- The equal-exit branch supplies killed-generator intertwining and positive limiting stationary fluxes, so it preserves the full joint marked waiting law and works without minimality. The half-line follows by continuity and divergence; it does not assert an infimum below the source value.
- The fixed-observed-rate/trace zero-slack exception and the coverage lower bound `ceil((N−1)/2)=floor(N/2)` have the right quantifiers. The design criterion is stated at complete sources on a known vertex set.
- Section 5's displayed four-state matrices have stationary distributions `(5,3,4,5)/17` and `(25,18,24,30)/97`. Their entropy rates and positive gap are correct. Independent direct construction of the full six-by-six matrices confirms equality at arguments 1 and 2 and inequality at 3. The same check passes at dimensions five and six after adding observed leaves to vertex 1.
- The arbitrary-two-arguments interpolation has exact stationary unnormalized weights `(10/k,3,4,10u/(kv))`, normalizer `Z=7+10a+10b/w`, and derivative `Z'=-10 b0 s1 s2/(C0 w²)<0`. It therefore establishes actual entropy ambiguity for any prescribed distinct positive pair, not just for the example arguments 1 and 2. Exact symbolic cancellation and stationary-balance checks independently confirm these identities.
- The complete reversible example has the displayed stationary masses, trace −12 and divergent internal-flux coefficient `1/4`; its attainable half-line and entropy nonnegativity give the exact image `[0,∞)`.

The one presentation clarification raised during this audit was to specify the leaf attachment and rates in the dimension extension. The inspected final version now says observed unit-rate leaves at vertex 1, which resolves it. A further wording improvement, optional rather than a mathematical correction, would replace “a sufficiently small finite collection” with “a sufficiently small neighborhood in a finite collection of Laplace measurements,” to distinguish the number of tests from the neighborhood radius.

The same reproduction command above now includes the final-draft witness checks. The script SHA-256 at this research-review checkpoint was `db17c280294256a60e56b235dee8c23265fb9d35538b012fa9a5c4607c65810a`. The later delivery adds only an early disabled-assertion guard; [verification.json](verification.json) records the new hash and the unchanged scientific replay payload. The checked examples and symbolic identities supplement the conventional proofs; they neither certify literature priority nor formally verify the universal theorem.
