# Independent mathematical review for the manuscript core

Reviewed 2026-09-11 UTC. Scope: the entire balanced-theta entropy fiber at a five-state cap, and the sharp fixed-count local entropy-ceiling theorem. This is a skeptical conventional proof review, with a fresh exact calculation, not formal verification or an originality assessment. Historical scientific files and accepted outputs were preserved. The coordinator owns manuscript synthesis, state, and evidence IDs.

**Finding:** the two proposed central theorems are supported under their declared assumptions. I found no substantive mathematical gap in the global endpoint count or the all-N ceiling criterion. One legacy summary uses an incorrect description of the escape-rate symbol; the underlying proof is correct, and the correction is specified below. The manuscript must contain the actual global support argument and the finite collection of exact sign certificates. Merely referring to previously accepted theorem labels would not make the proof self-contained.

## 1. Exact assumptions and limits retained

The class consists of finite irreducible row CTMC generators, one kinetic rate per ordered pair, nonnegative offdiagonals, reciprocal support, and two named visible states x,y with q_xy,q_yx>0. Exactly those two directed jumps are resolved marks. The observation is the complete matrix of joint next-mark/time densities, in fixed physical time, with the killed generator retaining the full-generator diagonals. The entropy is the stationary Markov entropy-production functional, using natural logarithms and k_B=1. An interpretation as total physical dissipation requires adequately resolved channels; the mathematical theorem does not add such physical information.

For the balanced theorem the class has at most five states, with arbitrary competing bidirected support and hidden labels quotiented out. For the ceiling criterion it has exactly N states; there is no common rate ceiling or positive reverse-rate floor unless explicitly stated. Fixed observed rates and fixed source trace are permitted restrictions. An arbitrary additional tight individual-rate cap is not.

The exact balanced source has minimal linear order five at every z>0. This is sufficient to put all cap-five competitors in its normalized similarity orbit. It does not by itself prove that five is the smallest cap at which any bounded nonuniqueness can occur. The manuscript can omit the latter global claim and thereby avoid importing the separate complete four-state classification.

## 2. Global balanced endpoint count: support audit

The checked source is the displayed Q(z) with hidden blocks

\[
X=\begin{pmatrix}2&0&8\\0&7&11\end{pmatrix},\quad
Y=\begin{pmatrix}3&0\\0&6\\z&z\end{pmatrix},\quad
H=\begin{pmatrix}-7&4&0\\5&-11&0\\0&0&-2z\end{pmatrix}.
\]

The direct exact minors are -9z(4z-9), -18z(2z-3), and -14(22z+19). The first two never vanish simultaneously for z>0, and the third is strictly negative. The visible reset and exit maps select the entire visible plane, so these hidden ranks imply full marked order five. This addresses the chart failure at z=2 and both repeated hidden poles without extrapolation from generic rank.

The realization-basis proof is valid: equality of all Markov parameters defines an invertible map on reachable vectors, observability establishes that it is well-defined, and the resolved reverse pair pins both visible rows and columns. Transience and T1=-B1 then force S1=1, giving S=diag(I_2,U), U1=1. Signed U must be allowed. Under the cap, smaller or nonminimal competitors cannot reproduce the rank-five Hankel matrix. Conversely an admissible normalized hidden similarity preserves the entire kernel directly.

At and above z_* the hidden spectrum is three distinct real modes, -alpha, -beta, -2z, where alpha=9-2sqrt(6), beta=9+2sqrt(6), and 2z>beta. I checked all hidden support partitions:

* Three singleton components are impossible because the beta transfer residue has negative offdiagonal entries, whereas singleton residues are nonnegative outer products.
* A connected pair and a singleton at beta are impossible for the same reason.
* A singleton at alpha would leave the pair with dominant pole -beta. Its Perron transfer residue is nonnegative, again contradicting the beta residue.
* A singleton at 2z leaves the pair's zeroth hidden response diag(6,42). Reciprocal visible incidence forces its two states to attach separately to x and y. Zeroth and first moments and row sums give x_1 y_1=6, x_2 y_2=42, y_1+h=7, y_2+k=11, x_1 h y_2=48, x_2 k y_1=105. Thus hk=20, 19h-hk=56, and all six pair rates are uniquely the source rates. The singleton residue and its escape sum then fix its rates too.
* Every connected hidden graph, including paths and triangles with arbitrary visible paired zeros, produces an irreducible Metzler H'. The positive left/right Perron eigenvectors force all modal cone rays to have strictly positive first coordinate. Sectioning at that coordinate equal to one produces a finite nondegenerate triangle, with origin strictly inside. Therefore neither signed similarities, unbounded similarity coordinates, nor rays at infinity escape the connected-case proof. Reducible cases were separately handled above.

The sign pattern of this triangle is exhaustive: exactly two vertices have positive height and one negative height. A lone positive-height vertex could not span both input abscissae, since nonpositive wedge points lie between -m and 1. Interior origin excludes zero bottom height. Labeling the vertices (-ell,P),(c,Q),(d,-W) gives ell>=m,c>=1,-m<d<1 and P,Q,W>0.

I checked the complete envelope chain in [balanced-cone-bound.md](balanced-cone-bound.md). The d<0 branch is excluded for z>=10.5 by the strict polynomial 72(z-10)^2+836(z-10)+835. For d>=0 the source inequalities imply P<10/7, Q>=A>B>2, ell>m, and the apex bound forces d>d_0>0. Thus W<=R(1-d) is the relevant bottom face. All denominators used here have the stated strict signs.

At fixed d,W,c,Q the left containment height increases strictly with ell and P; their unique maximal simultaneous values occur at the output/invariance intersection. The right input line is increasing in c and the right invariance hyperbola is decreasing on the positive-denominator branch. Their unique relevant intersection lies beyond its pole. The algebraic second intersection c=d is outside c>=1. If the relevant crossover lies below 1, the invariance bound at 1 is already below A, so no physical triangle is lost. The resulting height increases strictly with W up to R(1-d). These strictness conditions, not just the final quadratic, are what make the endpoint count unique.

The resulting necessary numerator is f_0+f_1 t+f_2 t^2, with denominator (J+at)^2. Its discriminant is exactly

\[
-\left(\frac{11}{1200}+\frac{11\sqrt6}{4200}\right)
\left(z+\frac{19}{22}\right)^2
\frac{352z^4-3168z^3-4644z^2-11340z-7623}{352}.
\]

There is exactly one positive root z_* of the quartic. Above it the negative discriminant and f_0<0 exclude all connected hidden supports. At it f_0<0,f_1>0,f_2<0, so exactly one positive t=-f_1/(2f_2) can attain equality. Every strict maximization must then attain equality, forcing one triangle up to permutation. Positive ray rescaling contributes no new normalized generator: w=-Hbar^{-1}Ybar1 is unique.

Existence is separate. The equality triangle's normalization, or the rational path chart, supplies the second physical generator. I read the exact path-check implementation: it retains denominator exclusions, computes in the selected real algebraic field, tests signs by rational root intervals instead of coefficient order, checks the precise seven-edge support, and verifies stationary normalization and ten Markov parameters. The different six-edge source and seven-edge target cannot be hidden relabelings. The rational logarithm bounds are valid: powers-of-two reduction plus the positive atanh tail bound encloses each log, and signed-current interval multiplication handles either current orientation. Thus the disjoint certified entropy intervals establish two entropy values, not merely two kinetic models.

I did not rerun the historical endpoint entropy certificate in this assignment; its implementation and saved certificate were inspected. The new independent computation below verifies the cone algebra and signs from original formulas, without importing that checker or its output. The global count remains a conventional proof, not an output of a finite numerical search.

## 3. A shorter self-contained subcritical covering

The balanced ray does not need the full two-parameter residue-redistribution theorem or the historical first-order threshold z_c. The following four overlapping constructions suffice.

**0<z<alpha/2.** Put d=2(sqrt(6)-1). In the hidden order (h,k,l), take K_hl=-4, K_kl=-d, K_lh=5, K_lk=d, K_hk=K_kh=0 and fix each diagonal by K1=0. In Q'=diag(I,I+epsilon K)^{-1}Q diag(I,I+epsilon K), the four absent hidden rates have first derivatives (alpha-2z)(4,d,5,d)>0. The absent visible incidences have derivatives (8d,55,4z,dz)>0. Hence all missing edges open for small positive epsilon while present edges remain positive. This interval covers the singular path chart z=2.

**alpha/2<=z<=beta/2.** The two-mode construction in [theta-family-construction-audit.md](theta-family-construction-audit.md), Section 2, puts the alpha residue in a singleton and the 2z,beta modes in a pair. Its two interval conditions are z>35sqrt(6)/88 and z>sqrt(6)/4. Both hold already at alpha/2. Thus its positive entrance/exit factorization applies throughout this closed interval, including both repeated poles. For 2z<beta the pair is joined; at equality it is unjoined with equal escapes. Its exit matrix has rank two, hence unequal exit rows, so the pair divergence lemma applies in either case. No inversion of the z=2 exit chart is used.

**beta/2<=z<=21/2.** This can be made entirely explicit. Put M=2z-11, L=M+4, and

\[
v_{\max}=7z/33,\quad
q=\tfrac12\left(M/5+96v_{\max}/(zM)\right),\quad
v=\tfrac12\left(zqM/96+v_{\max}\right),
\]
\[
u=\tfrac12\left(zq/24+4v/M\right),\quad
p=\tfrac12(-4u-zq/6),\quad
r=\tfrac12(11v/7+z/3).
\]

Use hidden offdiagonals (K_hk,K_hl,K_kh,K_kl,K_lh,K_lk)=(p,q,r,-1,-v,u), and K1=0. Here M>0, LM>=20, and 11M^2<=1100<1120. Thus all the open intervals defining these midpoints are nonempty. They imply

\[
q>M/5,\quad v<7z/33,\quad zq/24<u<4v/M,
\quad -4u<p<-zq/6,\quad 11v/7<r<z/3.
\]

The eight missing-rate derivatives are

\[
(2p+8u,\;7r-11v,\;-6p-zq,\;Lq-4,\;-3r+z,
\;5q-M,\;Lv-5u,\;4v-Mu),
\]

all strictly positive. This opens a complete realization. All denominators in the displayed K are positive; no limiting equality is silently admitted.

**21/2<=z<z_*.** The cone discriminant is positive and f_2<0, so t=-f_1/(2f_2)>0 gives strict upper slack for input B. All other geometric margins have the explicit positive interval certificates below. Decrease W, then move the left vertex strictly between its output and invariance bounds, then decrease the right vertex height. These three sufficiently small changes make all input/output and inward-flow inequalities strict. They produce a complete stable Metzler realization with positive row-normalizing vector. Each complete realization has an adjacent fully hidden pair with unequal full external exits, because equal exit rows would force an uncontrollable direction. The exact pair family then proves divergent entropy.

This closes the whole positive ray without needing a generic claim at repeated eigenvalues or a finite time-grid match. Each constructed family preserves the full transfer exactly.

## 4. Sharp local-ceiling criterion

The positive three-state result has a cap-free proof. From the full killed resolvent, with rates r,s,a,c,b,d and h=b+d, let F(lambda) be the row-swapped marked transform and H(lambda)=F(lambda)^{-1}. Its Schur complement is nonsingular for positive lambda because it is strictly row diagonally dominant. Direct calculation gives

\[
\frac{(H1)_x-1}{\lambda}=1/r+(a/r)/(\lambda+h),\quad
\frac{(H1)_y-1}{\lambda}=1/s+(c/s)/(\lambda+h).
\]

Three distinct positive arguments recover h from differences in a row with positive source entrance, then recover r,s,a,c. The corresponding source-positive entrance recovers the exit rates from an offdiagonal entry of H. Every denominator is nonzero at the source, including at either tree orientation; the local branch must be fixed using that source entrance. Two-state candidates have constant rows and cannot approach the nonzero source differences. Finite Laplace tests are continuous under weak row-law convergence and Lipschitz in row TV. Thus the physical generator inverse is locally Lipschitz in TV and continuous for weak row laws without an assumed common rate cap. Entropy is smooth on the complete three-state support, giving its finite local ceiling.

At a missing pair i,j of any irreducible source, add q_ij=e and q_ji=exp(-1/e^2), compensating their sum by subtracting it from an existing positive unobserved ordered rate. For small e all old reciprocal edges remain present; exact trace, observed rates and the original maximum-rate bound are retained. Stationary probabilities converge to positive source values. The new unoriented edge contributes asymptotically pi_i^0/e, so the entropy diverges. Common/excess-clock coupling or the integrated Duhamel identity gives joint-row TV convergence. With exactly one observed pair and N>=3, a positive unobserved compensating edge exists. This covers both three-state trees.

For every N>=4 there are two states absent from the observed endpoints. Convexly complete all unobserved rates while preserving their total mass, and assign one selected hidden external exit a different weight to ensure unequal external exit rows. The completion is arbitrarily close in row TV and has exactly the source trace and observed rates. At each fixed completion size, the triangular hidden-pair similarity keeps that exact kernel while a directional flux vanishes against a positive limiting opposing flux. Choose the completion size first and the pair limit second. No uniform positive divergence coefficient across completion sizes is required.

The integrated Duhamel bound uses positivity and the identity integral exp(T_e t)B1 dt=1. Its row-TV upper bound is epsilon R(-T)^{-1}|G-Q|1/2. It therefore controls all waiting times, not just a bounded time interval. Similarity separately preserves stationary observed finite-window densities by cancellation of every S in the marked-path likelihood; ordinary coupling makes the completion's stationary window law converge. Thus the statistical corollary is also justified under its stated stationary-window experiment, but it must not be deduced from row-TV convergence alone.

N=2 has entropy identically zero. Complete N=3 has the positive inverse result; trees fail by the chord construction; every N>=4 fails by completion and pair mixing. This proves exactly the stated iff, also with trace and observed rates fixed, and in weak row topology. An arbitrary additional cap invalidates it: with N=4, trace -12 and all twelve offdiagonal rates <=1, the class consists only of the all-one complete generator. Fixed support and positive rate floors also change the admissible class.

## 5. Correction and recommended proof package

**Minor legacy correction.** The hidden-pair summary in [publication-legacy-audit.md](publication-legacy-audit.md) calls lambda_h,lambda_k the sums of the external exit rows and then writes f(e)=m+e(lambda_k-lambda_h)-n e^2. In that formula they must be the **total escapes**, lambda_h=m+sum Y_h and lambda_k=n+sum Y_k. Equivalently write

\[
f(e)=m+e\{n+\textstyle\sum Y_k-m-\sum Y_h\}-ne^2.
\]

The original [hidden-pair proof](hidden-pair-boundary-audit.md) correctly defines them this way. This is a summary notation defect, not contrary evidence to the theorem. The new checker verifies the expanded formula directly.

The manuscript should include: the observation/entropy conventions; the normalized minimal orbit proof; the three minimality minors; explicit modal factors; disconnected support exhaustion; the Perron-triangle reduction; all envelope inequalities with domains; equality-to-generator uniqueness; the exact endpoint algebraic definition and sign/log certificate algorithm; the four-part subcritical covering above; the pair divergence lemma with total escapes; the finite-Laplace inverse; the completion/Duhamel proof; and the missing-chord argument. The optional sixth-state caveat can use the explicit clone stationary probabilities and killed intertwining, which are fully proved in [state-splitting-audit.md](state-splitting-audit.md). No claim of smallest possible cap or the full general five/six-state classification is needed.

## 6. Fresh exact computation and provenance

Run from the repository root:

```powershell
.\.venv\Scripts\python.exe -B analysis/manuscript-math-independent-check.py
```

The [new script](manuscript-math-independent-check.py) imports no historical checker or accepted output. Its [executed output](../outputs/manuscript-math-independent-checks.json) records the input hashes, script hash, UTC time, Python 3.9.12 and SymPy 1.14.0. There is no RNG, optimizer, numerical grid, or tolerance-based existence test. Exact symbolic checks verify minimality minors, the discriminant, total-escape shear formula, and the three-Laplace inverse from the full resolvent. Fresh rational intervals with outward rounding at every arithmetic operation, using polynomials shifted about z=21/2, verify all geometric signs on the entire interval [10.5,10.55714966867].

For a compact manuscript certificate, the saved rational enclosures imply these deliberately rounded strict lower bounds over that whole interval:

| Quantity | Strict rational lower bound |
| --- | ---: |
| f_1 | 5 |
| -f_2 | 14 |
| t | 18/100 |
| epsilon | 5/100 |
| 1-epsilon | 9/10 |
| c-1 | 1 |
| bottom left-output margin | 6/10 |
| right right-output margin | 170 |
| B above left lower edge | 8 |
| A below upper edge | 100 |
| left origin margin | 3/100 |
| right origin margin | 120 |
| bottom left inward derivative | 7/100 |
| bottom right inward derivative | 120 |

At the isolated root, -0.520929<f_0<-0.520928, 5.496508<f_1<5.496509 and -14.498918<f_2<-14.498917, as outward rational enclosures. The apex comparison has positive margin greater than 0.014259. The upper-input-B slack uses the exact discriminant sign and is zero at the fold, so it is intentionally absent from the strict whole-interval table.

An initial check run stopped because a SymPy structural-expression equality compared an expanded polynomial with its identical factorization. A direct print established the identity; replacing the comparison by an exact expanded-zero check made the full script pass. This was a test-harness issue, not a mathematical counterexample; the failed attempt is retained in the output provenance.

Reviewed inputs were PROJECT.md, STATE.md, analysis/publication-theorems.md, publication-endpoint-audit.md, publication-stability-audit.md, publication-legacy-audit.md, compatibility-orbit.md, balanced-cone-bound.md, theta-fast-spectral-audit.md, theta-family-construction-audit.md, theta-parameter-strata-audit.md, theta-balanced-boundary.md, hidden-pair-boundary-audit.md, entropy-neighborhood-audit.md, and state-splitting-audit.md. I also inspected relevant proof sections of theta-fast-hidden-paths.md, three-state-fixed-trace-audit.md, and one-hidden-robustness-audit.md; the implementations check_balanced_fold.py and check_balanced_cone_sufficiency.py; and saved cone/fold certificates. The older four-state and general sparse-five classifications were reviewed through the legacy inventory for scope and counterexamples, not independently reproved here. The final main manuscript can be checked separately when assembled.
