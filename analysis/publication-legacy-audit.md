# Publication audit of the earlier theorem inventory

Date: 2026-09-11 UTC. Contribution: independent analytic and implementation audit of existing results, plus a second challenge of the new stability criteria. This note is a dependency and scope audit, not a new topology search or novelty claim. No accepted calculation was overwritten or replayed. Fresh execution in this assignment was limited to reading saved JSON and checking source hashes.

## Audit conditions and outcome

The falsification condition was any admissible boundary case omitted by a stated theorem, any use of minimal similarity for a nonminimal model, any jump from a support-opening failure to global uniqueness, or any finite or numerical calculation being used as proof of a continuum or all-time statement without the needed algebra. For the stability claims the target was a source in the claimed class with a finite local ceiling despite the proposed divergence mechanism, or a purported missing-edge perturbation that violates fixed trace, a rate cap, frozen observed rates, or irreducibility.

The earlier classifications survive this audit with their stated hypotheses. They do not constitute an exhaustive classification of all networks through six states. Several historical final paragraphs are superseded by later theta proofs; retain them as dated limitations and use the later records in the theorem inventory. The fixed-state-count local-ceiling criterion survives without an additional arbitrary prescribed rate cap. The explicit tight-cap counterexample below prevents that stronger claim. Generator-level missing-edge instability needs a positive compensating rate that is allowed to change when trace and selected rates are both fixed.

All entropy statements use the working convention: finite irreducible simple bidirected row CTMCs, even microscopic states, one rate per ordered pair, positive rates on present edges, physical time fixed, and the stationary Markov entropy-production functional with Boltzmann's constant one. Exact observation statements use the full joint next-mark/time kernel and known resolved mark incidence, not marginal waiting densities. No positive lower rate floor is imposed. Most small-state results observe exactly the pair `x<->y`; the orbit and splitting theorems permit general nonempty reverse-closed resolved marks.

## Precise inventory and dependency limits

### Minimal compatibility and small state counts

The [compatibility-orbit proof](compatibility-orbit.md) states that two minimal realizations of the same full marked kernel are related by

\[
Q'=S^{-1}QS,\qquad S=\operatorname{diag}(I_V,U),\qquad U\mathbf1=\mathbf1,
\]

where `V` is the known observed endpoint set and `U` is any real invertible matrix for which the resulting generator is physical. Signed entries must be allowed. The converse holds without demanding positivity of `S`. The proof pins both visible rows and columns using reversal closure, then obtains normalization from invertibility of the killed generator. Irreducibility and a nonempty mark set give finite expected time to the next observed event, including when the killed support itself is reducible. This is a fixed minimal-dimension characterization; arbitrary larger nonminimal realizations need not be in this orbit.

The [small-network audit](small-network-audit.md) supplies the exact two-/three-state reconstruction underlying E017. The more recent [publication stability audit](publication-stability-audit.md) strengthens its topological continuity conclusion by an explicit three-positive-Laplace-value inverse, including both leaf orientations. Neither scalar pole counting nor a nonsingular particular coordinate chart is the definition of minimality.

### Exactly four states, prescribed support

The [minimal fixed-topology proof](four-state-classification-audit.md), together with the [nonminimal extension](nonminimal-four-state-audit.md), establishes **singleton entropy or upper-unbounded entropy** for every connected prescribed bidirected support on exactly four states with only `x<->y` observed. The final theorem does not require minimality. Its complete cases are:

| Support condition | Fixed-support conclusion |
| --- | --- |
| Either visible endpoint has exactly one hidden neighbor | Generator unique up to hidden labels; this incidence automatically forces full minimal dimension four. |
| No hidden edge; both visible endpoints have both hidden neighbors | Full diamond: distinct total hidden escapes give a unique generator; equal escapes give unbounded entropy. |
| No hidden edge; only one visible endpoint touches the hidden states | Tree; every stationary edge current vanishes, hence entropy is zero. Generator uniqueness is not asserted. |
| Hidden edge present; no visible singleton incidence | Unbounded entropy, whether the visible pair is pendant to a triangle or the graph is complete. |

The planar boundary proof is sound only after proving both similarities and their inverses bounded, so a boundary remains a minimal realization. It then proves boundary irreducibility before invoking positive limiting stationary masses. Permanent absent rows are excluded from the finite newly paired-zero set. Two visible paired-zero equations have nonzero determinant; normalized two-state hidden diagonalizers form a finite set or an empty set, including equal-row-sum exceptions. An open bounded planar region cannot have only finitely many boundary points, so a one-way boundary exists. This dimension-specific argument is not an arbitrary-hidden-dimension theorem.

For nonminimal cases the extension does not assume equivalence implies similarity. With equal hidden exit rows it uses strong lumping and varies an internal hidden rate: the two limiting hidden masses stay positive because both receive strictly positive stationary influx. With unequal rows the explicit triangular family works without minimality. The distinction between unique entropy and unique generator in a tree must remain visible.

### Exactly four states, unknown support

The [unknown-topology proof](unknown-topology-audit.md) plus its nonminimal extension gives a stronger exact dichotomy: **generator unique up to hidden labels, or entropy unbounded**. The only unique cases are:

1. Both visible endpoints have a single hidden neighbor and those neighbors differ; the hidden edge may be present or absent.
2. There is no hidden edge, one hidden state is shared by both visible endpoints, the other touches only one endpoint, and the shared state's total escape rate is strictly larger.

Every nonminimal exactly-four-state fiber is unbounded when topology is unknown. Equality of the escapes in case 2 belongs to the unbounded complement. The support proof uses signed normalized similarities and examines the whole determinant chamber after hidden relabeling; the stored signed grid is merely a falsification control. The full-diamond result with distinct escapes is unique only when that support is prescribed; it is unbounded when hidden-edge additions are allowed. These are compatible conclusions about different classes.

The [observable criterion](observable-four-state-criterion.md) translates these two unique cases into a necessary and sufficient finite test, **conditional on existence of an admissible exactly-four-state realization**. Recover `r,s`, the visible killed semigroup `K`, and

\[
D=K'(0),\quad A=D+\begin{pmatrix}0&r\\s&0\end{pmatrix},\quad a=-A\mathbf1,
\quad M=K''(0)-D^2,\quad L=K'''(0)-D^3-DM-MD.
\]

Case A is `a_x,a_y>0` and `M_xy=M_yx=0`. Case B has invertible `M`, distinct eigenvalues `-lambda_f,-lambda_s` of `LM^-1`, with `lambda_f>lambda_s>0`, a strictly positive rank-one fast residue and a positive single-coordinate diagonal slow residue. Then the note reconstructs every rate. Failure of both tests gives unbounded entropy by the complete classification. An equal hidden pole with rank-two residue can still satisfy A. Singular `M` does not imply nonminimality, even though it excludes these unique cases. The checker intentionally accepts only its selected rational-eigenvalue inputs; it is not a general exact eigenvalue solver or a feasibility/statistical procedure.

Explicitly those residues are `Z_f=-(L+lambda_s M)/(lambda_f-lambda_s)` and `Z_s=(L+lambda_f M)/(lambda_f-lambda_s)`. Case B requires rank `Z_f=1`, every entry of `Z_f` strictly positive, and `Z_s=c e_j e_j^T` for exactly one visible coordinate j and some c>0. These algebraic conditions, together with exactly-four-state feasibility, are the complete finite observable test.

### One additional hidden state and unrestricted finite order

The [hidden-pair boundary theorem](hidden-pair-boundary-audit.md) used throughout has this sufficient form. Let h,k be outside every observed endpoint and have identical sets of neighbors outside {h,k}. Write Y_h,Y_k for their full external exit rows and lambda_h,lambda_k for their sums. If Y_h!=Y_k and either the pair is joined or it is unjoined with lambda_h=lambda_k, its exact observed fiber contains a fixed-support divergent-entropy family with the same state count. After possibly swapping h,k, the normalized triangular mixing uses `U_e=((1-e,e),(0,1))`, `r=min_j Y_hj/Y_kj in (0,1)` over the common positive neighbors, internal rates m=q_hk,n=q_kh, and `f(e)=m+e(lambda_k-lambda_h)-n e^2`. Stop at the first of r and any positive root of f. All rates remain physical before that boundary; pi'_h=(1-e)pi_h and pi'_k=pi_k+e pi_h have positive limits there, and one opposing flux remains positive. For an unjoined equal-escape pair, f is identically zero and the external boundary at r applies. Equal full exit rows require the separate lumpable construction, not this strict-minimum argument. Nested-neighborhood variants retain their additional inequalities in the original note; no universal theorem for incomparable pairs is asserted.

The [splitting theorem](state-splitting-audit.md) applies to any finite admissible `N`-state source having a state outside **all** observed endpoints. Splitting that state into two clones with identical external exits and strictly positive entrance fractions yields exactly `N+1` states, identical full kernels, uniformly bounded rates, and entropy tending to infinity as one internal clone rate tends to zero with its reverse fixed. The killed intertwining is checked separately from ordinary lumping. The one-neighbor hidden-state boundary remains irreducible through that neighbor, and both clone masses have positive limits. The added realization is nonminimal. This theorem does not promise the source trace or an arbitrary prescribed cap.

For unrestricted finite cardinality there is a complete upper-range dichotomy under known incidence. The observable visible block `Q_VV` and row deficits are fixed by the first two kernel coefficients. If every deficit is zero, irreducibility excludes all additional hidden states and the generator is globally unique. If any deficit is positive, every realization has a hidden state and splitting gives unbounded entropy. This is conditional on realizability; it does not identify the smallest positive CTMC realization order from the linear order.

For a cap `N_max`, splitting proves unboundedness only if a compatible hidden-state source of size at most `N_max-1` is available. Thus unique four-state kernels become unbounded at cap five, and the minimal-five-state finite fiber becomes unbounded at cap six. It does not resolve every kernel whose minimum admissible size already equals the cap.

### Sparse five-state class and path-cap theorem

The [sparse-five theorem](five-state-sparse-audit.md) assumes a representative with exactly three hidden singleton components, no hidden edges, and three pairwise distinct positive hidden escapes. It classifies the full unknown-topology fiber at cap five. It is unique exactly when the hidden neighbor sets are `{x}`, `{y}`, `{x,y}` and the shared state is faster than both exclusive states; otherwise entropy is unbounded. Distinct poles and nonzero incidences give full minimal dimension five by a Vandermonde reachability/observability argument. Global uniqueness uses the positive dominant residue of every bridging hidden component and distinctness of the entire hidden spectrum to prevent cross-component cancellation. Repeated escapes and other starting supports are outside this theorem.

The equal-hidden-path-ratio identity in the same note says that certain two alternative microscopic path representations have the **same** entropy; it does not classify their full fiber. A hidden response cross ratio alone cannot exclude hidden entropy or prove bounded nonuniqueness.

The [path-cap theorem](path-cap-uniqueness-audit.md) holds for every `N>=3`, conditional on an admissible realization at cap `N`: if the first nonzero `K_xy` derivative has order `N-1`, every candidate has exactly `N` states and killed support equal to the spanning path from `x` to `y`. Bidirectionality rules out a shortcut chord. The endpoint resolvent determines the diagonal entries and adjacent rate products by continued-fraction peeling; CTMC row sums and known `r` split them into all directed rates. Full minimal dimension `N` follows from endpoint Krylov triangularity. Derivatives through order `2N-1` suffice. The cap, exact derivative zeros, and single-channel convention are essential. The `N=3` theorem is valid; only the implementation's chord negative control requires `N>=4`, since the proposed three-state chord is the observed edge itself. Inverse-Jacobi machinery is established prior art; the source attribution in that note was not independently reopened in this assignment.

### Theta strata and constructive regions

For the explicit `Q(a,b)` defined in [theta-parameter-strata-audit.md](theta-parameter-strata-audit.md), `a,b>0`, the full observation rank is five everywhere and the control rank is five except at

\[
(a,b)=(2\sqrt6-3,12-4\sqrt6),
\]

where it is four and the minimal order is exactly four. The chart line `2a+b=6` is not a nonminimality locus; only the stated point loses rank. With `s=a+b`, `alpha=9-2sqrt(6)`, `beta=9+2sqrt(6)`, the hidden eigenvalue-coincidence lines are `s=alpha,beta`. Fast coincidence does not lose minimality. On the punctured slow line the dominant visible-response residue has rank two and excludes **every irreducible hidden block**, even at higher order, by the simple positive Perron residue. This does not exclude entropy divergence with reducible hidden support. The exceptional point has an explicit complete four-state physical realization; the intermediate stochastic intertwining model is one-way and is used only algebraically. Splitting the physical four-state realization yields the permitted complete five-state family.

The [construction note](theta-family-construction-audit.md) and [slow-line redistribution proof](positive-realization-obstructions.md#6-update-the-entire-slow-coincidence-line-has-unbounded-entropy) prove upper-unbounded entropy at cap five throughout

\[
s\le\alpha\quad\text{or}\quad
\left[s\le\beta,\ a>35\sqrt6/88,\ b>\sqrt6/4\right]\quad\text{or}\quad
\left[s\ge\beta,\ a/b>11(s-11)^2/1120\ \text{or}\ b/a>14(s-7)^2/55\right].
\]

All points on both coincidence lines are covered. Complete nearby models are proved for `s<alpha` and in the strict fast-opening regions, while minimal slow-line models necessarily retain reducible hidden support. The cone normalizer is positive by a stable Metzler inverse; the required exit-row inequality is preserved rather than assumed after normalization. Strict coordinate thresholds are sufficient construction bounds, not universal feasibility boundaries.

For `s>beta`, or for `alpha<s<beta` with `a<=35sqrt(6)/88` or `b<=sqrt(6)/4`, every compatible **reducible** hidden realization is the original source. The equality coordinate strata are excluded from residue reassignment by reciprocal support: the two offdiagonal entries of `XY` must vanish together. A distinct bounded-fiber candidate must therefore have a hidden path; a hidden triangle has a comparable adjacent external-neighborhood pair and hence supplies unboundedness. This is a support reduction, not a complete classification of the two-parameter plane.

The [local-isolation counterexample](theta-global-audit.md) at `(3,3)` has full order five, a positive exact dual proving actual isolation in generator space, and a distant rational complete realization with an exact divergent family. Local isolation therefore does not decide global thermodynamic identifiability. The tangent dual is promoted to actual isolation through a normalized sequence and a nonsingular similarity chart, not merely a failed linear program.

The [positive-realization note](positive-realization-obstructions.md) gives an exact strict three-dimensional cone criterion and a universal shift `gamma=-tr H` under the fixed minimal dimension. It is a reformulation in established realization machinery, not a solution of the three-ray cone feasibility problem. Nonnegative realization or extra rays do not prove strictly positive order-three realization. The [fast spectral proof](theta-fast-spectral-audit.md) later supplies a genuine open two-parameter uniqueness region and the sufficient balanced range `z>=40`; the subsequent sharp balanced theorem supersedes that sufficient bound. It remains legitimate to retain the off-balanced open-region theorem as a distinct inventory item.

The precise open sufficient region uses `r_y=4(sqrt(6)-1)/5`, `A=a`, `B=b/r_y`, `m=(7+2sqrt(6))/5`, `k_L=(3-sqrt(6)/2)/8`, `k_R=35sqrt(6)/88`, `kappa=(a+b-alpha)/(4sqrt(6))`. Require `s>beta`, `(kappa-1)B>k_R[1+(A+1)/k_L]`, and `(kappa-1)A>k_L[m+(B+1)/k_R]`. Then the full cap-five generator fiber is unique. These are sufficient, not sharp off the balanced ray.

One further exact obstruction, [E046](../evidence/RECORDS.md#e046), distinguishes static factorization from realizability: at theta(100,100), for every finite block Hankel truncation of the hidden response uniformized at gamma=218, strictly positive factors of inner dimension three exist; for sufficiently large truncations the ordinary rank is three. Nevertheless the physical cap-five CTMC is globally unique. The proposed finite-factor similarity has hidden rate `e(-197+194e)/(1-e^2)<0` for 0<e<1 and is not a generator. The quantifier is each finite truncation with a sufficiently small e depending on it, not one common e for all times. This is an explicit exact counterexample to replacing dynamical invariance by finite-Hankel positivity, not a new general factorization theorem.

## Second challenge of the stability criteria

The central statement in [publication-stability-audit.md](publication-stability-audit.md) uses exactly `N`, one known resolved pair, and unknown competitor bidirected support. A finite local upper ceiling in joint-row TV exists exactly for `N=2`, or `N=3` with a complete triangle. The same criterion holds when observed rates and source trace are fixed. This is a neighborhood result; it does not contradict exact singleton or two-point fibers at larger `N`.

The positive result for a three-state triangle needs no prior rate cap: the finite rational Laplace inverse is locally regular there, so nearby generators and their entropy remain near the source. At a three-state tree the same generator inverse is regular but entropy is not: adding the missing chord at rates `e,exp(-1/e^2)` and reducing an existing positive unobserved rate keeps the observed pair and trace fixed. Every connected three-state tree containing the observed pair has such a positive unobserved rate. For `N>=4` there are at least two fully hidden states, and E055 applies even at nonminimal or complete sources. In particular completeness of the original microscopic generator does not restore local observable entropy boundedness for two hidden states.

An extra **arbitrary prescribed** rate cap changes the class. For four states with all twelve directed rates equal to one, fixing trace `-12` and also imposing cap one forces every rate to remain one: the whole class is a singleton with zero entropy. Thus E055's constructed finite cap, for example `-tr Q`, cannot be replaced by every cap containing the source. The fixed-trace criterion should be stated without this additional constraint, or under a separately proved sufficient cap. A positive rate floor together with a common upper cap globally bounds entropy and likewise removes the construction.

At the generator-entry level, unknown-support local entropy boundedness is instead equivalent to completeness for any fixed finite `N`. At a noncomplete irreducible bidirected source, choose a missing pair and add rates `e` and `k=exp(-1/e^2)`. Subtract `e+k` from an existing positive directed rate and renormalize the diagonals. For sufficiently small `e`, old support stays positive, the source's maximum rate cap is retained, trace is fixed, and the stationary law converges to its positive source law. The added edge contributes asymptotically `pi_i/e`, while all old supported-edge contributions remain finite. Completeness gives ordinary smooth entropy continuity in an entrywise neighborhood.

If selected rates are frozen, the compensating directed rate must be among those allowed to vary. With exactly one observed pair and `N>=3` this always exists. If **all** originally positive rates are both individually frozen and trace is fixed, no positive missing edge can be added; that overgeneralization is false. Full microscopic observation with approximate equality does not freeze each rate and is compatible with the generator-limit counterexample. A known support restriction also disallows adding the chord. Irreducibility of the source is essential for the stated positive limiting stationary coefficient; reducible sources require a separate theorem. No statement here covers odd-variable time reversal or unresolved parallel channels.

These joint-row-TV conclusions also hold as instability under any weaker topology, since their divergent sequences already converge in TV. The positive three-state inverse is continuous for weak joint-row convergence because it uses finitely many bounded continuous Laplace test functions. Neither fact by itself transfers the cap-free positive result to a fixed stationary physical-time window: extraction of the full waiting law from that different experiment needs a separate argument. The previously saved finite-window positive proof uses a common rate cap. The divergent stationary-window constructions and their uniform-confidence impossibility implication have their own coupling and stationary-law arguments in the prior audit.

## Inspected evidence, fresh execution, and unresolved limitations

Read in this bounded inventory pass: `AGENTS.md`, `PROJECT.md`, `STATE.md`, `docs/research-stack.md`, `analysis/README.md`; the full mathematical notes `four-state-classification-audit.md`, `unknown-topology-audit.md`, `nonminimal-four-state-audit.md`, `observable-four-state-criterion.md`, `state-splitting-audit.md`, `five-state-sparse-audit.md`, `path-cap-uniqueness-audit.md`, `theta-parameter-strata-audit.md`, `theta-family-construction-audit.md`, `theta-global-audit.md`, and `positive-realization-obstructions.md`; the relevant statement/normalization sections of `compatibility-orbit.md`, the open-region/conclusion sections of `theta-fast-spectral-audit.md`, and the supersession note in `theta-fast-case-audit.md`. The small-network, E032, and robustness dependencies had already been read in the preceding audit and are referenced through `publication-stability-audit.md`; they were not freshly rerun here. This assignment did not independently retrieve the cited literature or claim any source-access improvement.

Implementation inspection covered all of `check_four_state_classification.py`, `check_state_splitting.py`, `check_observable_criterion.py`, and `check_five_state_extensions.py`, and the exact scalar arithmetic, construction, rank/stationary checks and caller in `check_theta_residue_construction.py`. Embedded checks in the sparse-five, path-cap and theta-strata notes were inspected. Saved JSON was parsed for the five listed checkers; all current script hashes match their output manifests. Hash agreement authenticates which inspected code produced the recorded claim; it is not an independent scientific replay.

| Saved output, relative to project root | Recorded scope | Last recorded run UTC |
| --- | --- | --- |
| `analysis/four-state-classification-checks.json` | Three exact boundary witnesses, five support openings, two finite signed-grid controls; no exhaustive grid theorem. | 2026-09-10 13:31:42 |
| `analysis/state-splitting-checks.json` | One 4-to-5 split, two lumpable nonminimal families, exact stationary/aggregation/finite-jet identities and numerical logarithmic slopes. | 2026-09-10 13:31:42 |
| `analysis/observable-criterion-checks.json` | Nine rational examples; four reconstructions and five unbounded controls, including minimal singular `M`. | 2026-09-10 13:31:43 |
| `analysis/five-state-extension-checks.json` | Exact local/distant five-state certificates and 5-/6-state path reconstructions; five LP diagnostics are separately numerical. | 2026-09-10 13:31:44 |
| `outputs/theta-residue-checks.json` | Five exact `Q(sqrt(6))` constructions including both coincidence lines, a low-coordinate slow-line point, and the rank-four exception. | 2026-09-10 07:00:06 |

Fresh metadata-only verification can be reproduced without importing or running any scientific checker:

```powershell
@'
import hashlib, json
from pathlib import Path
for script, output in [
 ('analysis/check_four_state_classification.py','analysis/four-state-classification-checks.json'),
 ('analysis/check_state_splitting.py','analysis/state-splitting-checks.json'),
 ('analysis/check_observable_criterion.py','analysis/observable-criterion-checks.json'),
 ('analysis/check_five_state_extensions.py','analysis/five-state-extension-checks.json'),
 ('analysis/check_theta_residue_construction.py','outputs/theta-residue-checks.json')]:
    p = Path(script)
    saved = json.loads(Path(output).read_text(encoding='utf-8'))['script_sha256']
    expected = saved[p.name] if isinstance(saved, dict) else saved
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    assert actual == expected, script
    print(script, actual)
'@ | .\.venv\Scripts\python.exe -B -
```

The source hashes checked in this pass are, in the table order:

```text
cbcc7efb6b46623574758af2706de3249419eca99112203fdc1c50ecb34d3d2c
9d925a943330513022a690111761336ff9cb2835916a026405a373a96653bc27
40af86e70e5f3a522d8f2a92196a13e59879b706694a5b84a965c625012af51b
4f5ba7179e1af63f2115fbfb6bf98d672d6e8105a4730e8ef58c873c2ab0368d
df7d9a893580d489ae94902b42e15337560d6926c6a50f681ec2fda9b4347b34
```

The old exact finite-jet certificates use orders `0,...,n+n'-1` for compared `n`- and `n'`-state realizations; Cayley-Hamilton on their block-diagonal difference realization makes that sufficient for all-time equality. More fundamentally the displayed similarities/intertwinings prove equality directly. Floating exponentials and logarithmic slope checks are corroboration; their numeric entropy values are not rigorous enclosures. The later algebraic endpoint's certified entropy intervals come from separate checkers and were audited in the dedicated endpoint assignment.

Retain the recorded failed or superseded attempts: finite grids do not prove global uniqueness; the initial nonsymmetric `eigvalsh` diagnostic was corrected to `eigvals` without changing the exact tangent proof; a failed complete search at `(100,100)` was inconclusive and later replaced by spectral exclusion; first-order threshold sharpness was falsified by the later second-order/boundary constructions. Historical missing-SymPy statements describe the old environment, not the currently installed stack. No unsuccessful new scientific search occurred in this assignment.

Remaining limits are substantive: a full two-parameter theta classification, a general five-/six-state exact-fiber classification, unknown/blurred incidence, and alternate microscopic reversal/channel conventions are not settled by this inventory. Primary-source novelty and any formalization remain separate audits. Failure to find a counterexample is not the justification for the accepted statements; the explicit global arguments above are.
