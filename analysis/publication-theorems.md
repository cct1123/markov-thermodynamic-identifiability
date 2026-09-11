# Mathematical specification for the publication audit

2026-09-11 UTC. This replaces informal readings of the results, not the historical evidence. All theorems below have conventional proofs; none has been formally verified. The exact-check artifacts support specified identities and examples. Literature originality is assessed separately in the [realization comparison](../evidence/publication-realization-novelty.md) and [thermodynamic comparison](../evidence/publication-thermodynamics-novelty.md). The [legacy audit](publication-legacy-audit.md) states the remaining consequential classifications and counterexamples precisely.

## 1. Common definitions and quantifiers

Fix a time unit and two distinct named states x,y. For N>=2 let C_N be the class of real N-by-N row generators Q on {x,y,h_1,...,h_(N-2)} satisfying: q_ij>=0 for i!=j; q_ii=-sum_(j!=i)q_ij; connected reciprocal support q_ij>0 iff q_ji>0; and r=q_xy>0,s=q_yx>0. Every rate is finite, but there is no common upper bound or positive lower bound. Competitor topology is unknown. C_<=m is the disjoint union of C_N for 2<=N<=m. C_N(Q0;r,s,tau) additionally fixes q_xy=r0,q_yx=s0 and -tr Q=tau0=-tr Q0. A separate bound q_ij<=M is denoted C_N^M; it is never implicit. A prescribed support G or positive floor m is another restriction, explicitly named when used.

Models have one kinetic channel per ordered pair and states even under time reversal. For a mathematical generator the functional below is defined without a reservoir model. Interpreting it as total physical dissipation further requires sufficiently resolved thermodynamic channels and local detailed balance. Parallel channels, odd states, driven generators, unresolved marks and uncertain endpoint incidence are different models.

Observe exactly two marks +=(x,y), -=(y,x). Put E_+=r e_x e_y^T, E_-=s e_y e_x^T, T=Q-E_+-E_-, R=(e_y^T;e_x^T), B=(r e_x,s e_y). **T keeps Q's diagonals.** It is transient because Q is finite irreducible and the observed set is nonempty. Define the observation map

\[
\mathcal O(Q)=\Psi_Q(t)=R e^{Tt}B,\quad t\ge0,
\qquad \widehat\Psi_Q(\lambda)=R(\lambda I-T)^{-1}B,\quad\lambda>0.
\]

Row I is the probability measure mu_I^Q(dt,J)=psi_IJ(t)dt on X=[0,infinity) times {+,-}: the joint waiting time and next mark after mark I. Its total mass is one; an individual entry need not integrate to one. Absolute time and joint amplitudes are retained. The two exact row measures determine the continuous densities everywhere, all reset-conditioned event sequences, and the stationary time-origin observed process by renewal stationarity. The latter has finite mean interevent time. No claim is made that approximate moments determine approximate stationary event frequencies.

Q~obs Q' means equal row measures, equivalently equal Psi for every t>=0. Q~lab Q' means permutation similarity fixing x,y. Lab equivalence implies observational equivalence but is a much narrower relation. The physical fiber and its entropy image in a declared class C are

\[
\mathcal F_C(D)=\{[Q]_{lab}:Q\in C,\mathcal O(Q)=D\},\quad
\mathcal S_C(D)=\{\sigma(Q):[Q]_{lab}\in\mathcal F_C(D)\}.
\]

For the unique positive stationary row pi Q=0, pi1=1, set F_ij=pi_i q_ij and

\[
\sigma(Q)=\sum_{i<j:q_{ij}>0}(F_{ij}-F_{ji})\log(F_{ij}/F_{ji})
=\sum_{i\ne j:q_{ij}>0}\pi_iq_{ij}\log(q_{ij}/q_{ji}).
\]

Natural logs, k_B=1; sigma has inverse-time units. A paired absent edge contributes zero. Every admitted model has finite sigma>=0; sigma=0 iff detailed balance holds. A one-way edge is outside C_N. With stationary fully observed path law P_Q^H on [0,H], time reversal theta, the jump likelihood gives D_KL(P_Q^H || P_Q^H composed with theta^-1)=H sigma(Q). The waiting-rate terms cancel, and stationarity cancels the expected endpoint log-pi term. Observed-law KL is generally smaller and is not the functional classified here.

**Exact meanings.** Generator identifiability means |F_C(D)|=1; thermodynamic identifiability means |S_C(D)|=1. Bounded nonuniqueness means 1<|S_C(D)| and sup S_C(D)<infinity; it need not mean a finite set. Unbounded means for every L<infinity there exists an admitted model with entropy>L. Divergence of a displayed sequence means sigma(Q_n)->+infinity; no infinite-entropy model has to be admitted. Empty fibers are incompatibility, not identifiability.

**Data topologies.** Use d_TV(D,D')=max_I (1/2)sum_J integral_0^infinity |psi_IJ-psi'_IJ|dt, with TV=sup_A|mu(A)-nu(A)|. Also consider the product weak topology of the two row probability measures on X. Fixed-lambda Laplace entries are bounded continuous tests for that topology. The stationary experiment has a different metric d_H(Q,Q')=TV(P_obs,Q^H,P_obs,Q'^H), H>0, including empty records and censored ends. Conclusions for d_TV or weak convergence are not automatically conclusions for d_H.

Define B_C(D,eta)=sup{sigma(P):P in C,d_TV(O(P),D)<eta}. A **robust finite upper ceiling** means B_C(D,eta)<infinity for some eta>0. Its weak-topology version uses some open neighborhood of D. This is local boundedness of a set-valued identified entropy range, even where sigma is not a single-valued function of D. At identifiable data, **thermodynamic continuity** means every admitted Q_n with O(Q_n)->D has sigma(Q_n)->sigma(Q); it is stronger than a finite ceiling. Local Lipschitz continuity means a finite source-dependent constant bounds entropy difference by d_TV in a neighborhood. No uniform condition number is asserted.

## 2. Exact observation and realization lemmas (established machinery)

**T1. Finite certificate and minimal orbit.** Two models of dimensions n,n' have equal kernels iff R T^k B=R'T'^k B' for 0<=k<n+n'. This follows by Cayley–Hamilton on diag(T,T'). Define linear minimality by full reachability span{T^k Bv} and observability intersection ker(RT^k)={0}. Equivalent minimal realizations have the same dimension and are related by a unique invertible similarity. With the resolved pair fixed, the similarity is S=diag(I_2,U), U1=1, and

\[
Q'=S^{-1}QS,\qquad X'=XU,\ H'=U^{-1}HU,\ Y'=U^{-1}Y.
\]

U need not be nonnegative. Physical offdiagonal positivity and reciprocal support must still be checked. The hidden block partition is Q=((A,X),(Y,H)). Invertibility of T and T1=-B1 prove normalization. See [compatibility proof](compatibility-orbit.md). This lemma is prior realization theory specialized to the prescribed event maps; semialgebraicity or similarity alone does not count F_C(D).

## 3. Three-state identifiability and cap-free continuity

**T2. Exact finite-Laplace inverse.** For every Q0 in C_3 and any fixed 0<lambda1<lambda2<lambda3, the values of Psi-hat at these three arguments determine Q0 uniquely within C_<=3. On a neighborhood of those values, the inverse restricted to admissible data is rational with nonzero denominators and is locally Lipschitz. Consequently, for Q_n in C_<=3, weak convergence of their row laws to O(Q0) implies eventually N_n=3 and Q_n->Q0 entrywise. Under d_TV convergence the inverse is locally Lipschitz. Neither observed rates, trace, upper rate bounds nor strictly positive triangles are assumed beforehand.

To specify the inverse, write

\[
Q=\begin{pmatrix}-r-a&r&a\\s&-s-c&c\\b&d&-b-d\end{pmatrix},\quad h=b+d.
\]

Here r,s>0, a,b>=0 with a=0 iff b=0, c,d>=0 with c=0 iff d=0, and a+c>0. Let P swap mark rows, F(lambda)=P Psi-hat(lambda), H(lambda)=F(lambda)^-1. Schur complementation gives

\[
G_x=\{(H1)_x-1\}/\lambda=1/r+(a/r)/(\lambda+h),\quad
G_y=1/s+(c/s)/(\lambda+h).
\]

Choose a row G=u+v/(lambda+h) with v>0 at Q0. Its three differences give

\[
R_0=\frac{G_1-G_2}{G_2-G_3}\frac{\lambda_3-\lambda_2}{\lambda_2-\lambda_1},\quad
h=\frac{\lambda_3-R_0\lambda_1}{R_0-1}.
\]

For each row i set v_i=(G_i1-G_i2)(lambda1+h)(lambda2+h)/(lambda2-lambda1), u_i=G_i1-v_i/(lambda1+h). Then r=1/u_x,s=1/u_y,a=v_x/u_x,c=v_y/u_y. Fix the branch using the **source** entrance: if a0>0 use d=-r H_xy(lambda1)(lambda1+h)/a,b=h-d throughout its neighborhood; otherwise c0>0, and use b=-s H_yx(lambda1)(lambda1+h)/c,d=h-b throughout. Both leaves are covered without dividing by a newly opened entrance tending to zero. Two-state candidates have constant G rows and cannot approach the nonzero source differences. Full proof, including nonsingularity and weak-topology justification: [stability audit, Section 3](publication-stability-audit.md#3-new-exact-finite-laplace-inverse-remove-the-prior-rate-cap).

**Corollary T2a.** At every complete Q0 in C_3, thermodynamic entropy is locally Lipschitz in d_TV and continuous under weak row-law convergence among C_<=3. At a tree, the generator inverse has the same regularity but entropy need not be locally bounded. The previous common-rate-cap proof of E058 is valid but its cap is unnecessary for joint-kernel data. For stationary d_H the saved sufficient common cap remains part of the proved positive result; its removal is open.

Small examples: all six rates one gives a stable equilibrium triangle. The unit tree x-y-h has r=s=c=d=1,a=b=0; its inverse is locally Lipschitz but T4 below defeats every entropy ceiling. C_2 itself has sigma identically zero. A C_2 source under the enlarged cap three is a different boundary; the rare-hidden-state example in [E058](../evidence/RECORDS.md#e058) is unstable. Enlarging the cap above three invalidates T2a by hidden-state splitting. No claim of minimality of the number **three Laplace arguments** is made.

## 4. The exhaustive finite entropy fiber

**T3. Balanced-theta theorem.** In C_<=5 consider, in order (x,y,h,k,l),

\[
Q(z)=\begin{pmatrix}-11&1&2&0&8\\2&-20&0&7&11\\3&0&-7&4&0\\0&6&5&-11&0\\z&z&0&0&-2z\end{pmatrix},\quad z>0.
\]

Let z_* be the unique positive root of 352z^4-3168z^3-4644z^2-11340z-7623. Every source has linear minimal order five. For 0<z<z_* the entropy fiber is unbounded. For z>z_* the generator fiber is a singleton. At z=z_* the generator fiber has exactly two elements modulo hidden labels, Q(z_*) and Q_*, and its entropy image has exactly two distinct finite points with certified enclosures

\[
\sigma(Q(z_*))\in[.062946400236,.062946400237],\qquad
\sigma(Q_*)\in[.065579685966,.065579685967].
\]

Q_* is defined exactly, without rounded entries, by the rational exit-chart formulas (3)–(6) of [the endpoint specification](theta-balanced-boundary.md#independent-path-coordinate-construction). Equivalently the equality-cone construction in [publication endpoint audit, Section 5](publication-endpoint-audit.md#5-exact-cone-construction-independently-matches-the-path-witness) defines it over Q(z_*,sqrt(6)) and all sqrt(6) coefficients cancel. Its seven reciprocal edges differ from the source's six. Thus the two generators cannot be relabelings. This referenced exact algebraic definition is part of the statement.

Proof obligations and status: minimality forces all cap-five competitors into T1's orbit; Perron normalization exhausts every connected hidden support by a nondegenerate finite triangle; a global envelope quadratic has discriminant a negative positive-factor multiple of the stated quartic; its equality case forces one triangle; separate residue/reciprocity arguments exhaust disconnected hidden supports as the source. Exact feasibility and rigorous logarithm remainders supply existence and entropy separation. A strict-cone construction below the fold overlaps the earlier subcritical theorem, including separately handled repeated poles. [Fresh independent audit](publication-endpoint-audit.md) verifies all of these, including an independent coefficientwise equality between the cone and path constructions.

The unique positive quartic root is approximately 10.5571496686650; the numerical value is illustrative. z=0 is excluded because the source ceases to be irreducible. Hidden pole coincidences at 2z=9+-2sqrt(6), the chart zero z=2 and the earlier first-order threshold are not missing cases: the separate constructive covering handles them. The endpoint is away from these degeneracies. The cone proof's right crossover is unique on its physical domain c>=1 beyond its pole; an algebraic root outside that domain does not represent another model.

Minimal assumptions: exact derivatives 0 through 9 can replace all-time equality under the cap; no external rate cap is needed since trace is fixed by similarity. Full-chain irreducibility may be replaced by nonnegative row normalization plus exact data and the cap: minimality gives reachability and return to the visible pair, hence irreducibility. The cap may be replaced by requiring all competitors to be linearly minimal. Removing it while admitting nonminimal models allows a sixth state and unbounded entropy. Reciprocal support, resolved known event incidence and the entropy convention have not been removed. Fixed source topology leaves only the source; fixed path topology leaves only Q_*. The theorem does not classify the general five-state class or prove novelty. The smallest possible cap for bounded nonuniqueness is five by the separate C_<=4 classification in the [legacy audit](publication-legacy-audit.md).

## 5. Sparse boundaries, hidden ambiguity and sharp local ceilings

**T4. Generator-topology boundary theorem.** On C_N with its entrywise topology, sigma is locally upper-bounded at Q0 iff Q0 has complete support. The same iff holds after fixing source trace and imposing its original maximum offdiagonal rate M0. If Q0 has a missing pair i,j, add rates e,k(e)=exp(-1/e^2) and subtract e+k from one existing positive ordered rate. For small e>0 all source edges remain reciprocal and connected, trace and M0 are retained, and pi(e)->pi0>0. The new edge contributes asymptotically pi_i^0/e; all other edge terms are nonnegative. Full stationary microscopic finite-window laws converge in TV by coupling. If the compensating edge is unobserved, specified observed rates also remain fixed. Under one observed pair and N>=3 such an edge always exists. At complete sources all supported rates have a positive local floor and entropy is smooth. This proves both directions, without a numerical-search premise.

**T4a. Smallest explicit fixed-trace example.** For 0<k<e<1/2 set

\[
Q(e,k)=\begin{pmatrix}-1-e&1&e\\1&-2+k&1-k\\k&1-e&-1+e-k\end{pmatrix}.
\]

All rates are <=1, -tr Q=4, and the source Q(0,0) is the unit tree x-y-h. Every kernel is minimal three and uniquely identifies the generator in C_<=3. With Z=3+e+2k-e^2-ek-k^2,

\[
\sigma=\frac{(e-k)(1-e-k)}{Z}\log\frac{e(1-e)}{k(1-k)},\quad
d_{TV}<4e,\quad d_H\le11e/18+2eH.
\]

For k=exp(-1/e^2) and e->0, e sigma->1/3. For fixed e>0, k->0 has positive logarithmic divergence coefficient, so every positive neighborhood of the tree has infinite entropy supremum under the same count, trace and cap. Three is minimal because every two-state bidirected generator has sigma=0. Proof and boundary checks: [E057](../evidence/RECORDS.md#e057), [fresh audit](publication-stability-audit.md). The exclusions k=e (zero cycle affinity), k=0 (inadmissible one-way triangle) and e=k=0 (valid tree with paired zero) are distinct. The displayed open domain is sufficient; it is not claimed to be the maximal positivity domain.

**T5. General two-hidden-state neighborhood theorem.** More generally allow any nonempty reverse-closed set of individually resolved edges on a fixed finite state set. If Q0 has at least two states absent from every observed endpoint, then for every eta>0 and L<infinity there exists a complete bidirected Q with the same N, every observed rate and exact trace, with d_TV(O(Q),O(Q0))<eta and sigma(Q)>L. All its rates are <=tau0. There also exists such a divergent sequence with d_H->0 for each fixed finite H under stationary initialization. No minimality or source sparsity is needed.

Proof: first convexly complete the unobserved edges with the same total rate mass and unequal external exit rows for a chosen hidden pair. Integrated Duhamel gives TV->0; then, at each fixed completion size, the exact hidden-pair similarity family reaches an excluded one-way boundary with positive limiting opposing flux. The same stationary observed law is preserved along that family. Take the completion limit after selecting sufficient entropy. This is the two-limit construction in [E055](../evidence/RECORDS.md#e055), independently audited in [Section 2](publication-stability-audit.md#2-exact-audit-of-the-existing-divergence-mechanisms). It does not say the original exact fiber is unbounded or that the high-entropy generators approach Q0 entrywise.

**T6. Sharp fixed-count criterion.** For one resolved pair, N>=2 and Q0 in C_N, a robust finite upper ceiling in C_N exists iff N=2 or (N=3 and Q0 is complete). The identical criterion holds in C_N(Q0;r,s,tau) and for product weak row topology. Positive cases follow from T2a and sigma=0 for N=2; T4 excludes all three-state trees; T5 excludes every N>=4 source. This is an all-N theorem, not a five-state conjecture. It also shows the distinction between thermodynamic identifiability and local upper stability: exact singleton and two-point fibers can have an infinite local upper envelope.

Targeted falsification limits: the theorem does not survive every additional tight cap. For N=4, tau=12 and q_ij<=1, all twelve rates must be one, so the entire restricted class is a singleton despite two hidden states. A positive floor or known tree topology also excludes the sparse construction. Complete generator support suffices for entrywise entropy continuity (T4) but not observational upper stability for N>=4 (T5). N and a cap on N are different assumptions. These are explicit counterexamples to stronger statements, not merely cautions.

## 6. Statistical consequence and sufficient regularity conditions

**T7. Uniform upper-confidence obstruction.** Let U be a measurable extended-real statistic of a stationary observed record on fixed H>0, possibly with independent randomization, and 0<alpha<1. Suppose P_Q^H{sigma(Q)<=U}>=1-alpha for every Q in a class containing a sequence with sigma(Q_n)->infinity and TV(P_Qn^H,P_Q0^H)->0. Then P_Q0^H{U=+infinity}>=1-alpha. For every finite L, the coverage bound transfers to P_Q0{U>L}; let L increase to infinity. This elementary statistical mechanism has established Gleser–Hwang-type precedents. T4a/T5 supply the physical sequences, including their fixed-trace restrictions. Uniform modelwise finite-sample coverage is essential; the statement does not address pointwise asymptotic coverage, priors or a growing horizon. Positive-triangle local continuity does not imply a globally almost-surely finite honest bound; the separate domination result in E058 proves a weaker positive probability of infinity there.

**T8. Sufficient regularity and the exact mechanism.** Fix a reciprocal graph G and a compact set K of irreducible generators with support exactly G. Suppose every admitted sequence with O(Q_n)->D0 has hidden relabelings with dist(Q_n,K)->0 and support(Q_n)=G eventually. Then continuity of pi and sigma on this support stratum gives a finite local upper ceiling: otherwise choose sigma(Q_n)>n at data distance <1/n and extract a limit in K, contradicting continuity. If sigma is constant on K, entropy converges to that value. The positive minimum of the G-rates over K supplies a uniform floor; eventual equality of the competitors' support forbids newly opening edges that vanish in the limit. This is a sufficient condition, not asserted necessary or novel. T2 verifies it locally for a triangle. T4a falsifies the provisional weaker formulation requiring only a compact irreducible limiting set: its limit is the unit tree with positive present rates, while vanishing new chords carry divergent entropy. T5 shows bounded trace alone does not supply this support-controlled inverse property.

An explicit uniform bound is simpler: if all supported rates lie in [m,M], m>0, then sigma<=A log(M/m), where A=sum_i pi_i sum_(j!=i)q_ij is stationary activity. A<=(N-1)M and also A<=tau when trace is fixed. This follows from the directed entropy identity; no stationary probability floor is required. A uniform ratio bound q_ij/q_ji<=R **together with A<=Amax** suffices instead, with sigma<=Amax log R. A lower individual-rate floor is therefore stronger than necessary when trace or activity is controlled. Ratios alone do not bound entropy: a three-cycle with clockwise rates 2c and reverse rates c has pi=(1/3,1/3,1/3), sigma=c log2 and A=3c, diverging as c increases while R=2. This is a coarse established-type bound, not a novel sharp thermodynamic inequality. Trace tau is not activity A.

## 7. Evidence status and open statements

T1–T8 are conventional results with the above scopes, not numerical conjectures. New T2/T4/T6 are proved in the [stability audit](publication-stability-audit.md); root [independent checks](check_publication_audit.py) and [output](../outputs/publication-audit-checks.json) use direct 160-digit resolvents, an alternative exact four-point reciprocal-cubic trace interpolation, and independent stationary solves. The six inversion cases, three exact interpolation cases and twelve chord diagnostics all passed. These do not replace the rational inverse or continuum proof. The endpoint has exact algebraic witnesses, rational log bounds and independent whole-support proof audits.

Numerical only: optimizer locations, best positive margins, entropy decimal illustrations outside certified intervals, time-grid/exponential agreement and sampled condition numbers. Rejected claims: first-order threshold sharpness, local isolation implying global uniqueness, static Hankel positivity implying dynamical feasibility, and arbitrary tight-cap versions of T6. Historical failed attempts remain in their original artifacts and the fresh audit notes.

Open: a full two-parameter theta or arbitrary five/six-state exact-fiber classification; cap-free continuity from one stationary finite window; observations with unknown/blurred incidence or parallel thermodynamic channels; optimal transform sample count; and an exhaustive novelty certification (which no finite search supplies). None is needed to state or prove T3 or T6. Originality and publishability are reasoned assessments, not theorem labels.
