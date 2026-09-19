# Observation coverage, exact entropy fibers and finite local ceilings

19 September 2026. Research-loop result, extending the arbitrary-observation appendix at commit `c7ff789`. **Status: conventional proofs with independent mathematical review and executed exact examples; not formally verified.** Novelty is assessed separately in [LITERATURE.md](LITERATURE.md). Bare all-time one-hidden-state recovery is closely anticipated by Burgarth's zero-forcing result. The proposed contribution is the combination of finite positive-transform recovery, the all-source complete-network entropy dichotomy, and the sharp local-ceiling/design criterion.

## 1. Experiment, model class and statement

Fix a labeled vertex set V of size N>=2 and a nonempty reverse-closed set O of individually resolved microscopic transitions with known endpoints. Every observed rate is strictly positive. Competitors are finite irreducible row generators Q on **this same vertex set**, with reciprocal support: q_ij>0 iff q_ji>0. Unobserved support is unknown; rates have no common floor or cap. There is one kinetic channel per ordered pair. Natural logarithms and k_B=1 are used.

Let C be the vertices incident to O, H=V\C, and E the matrix whose observed off-diagonal entries are q_ij and whose other entries vanish. Put T=Q-E, R_I=e_dest(I)^T and B_J=q_J e_orig(J). The data are the absolute joint row probability laws

    Psi_I(J,dt) = [R exp(Tt) B]_IJ dt,
    Psi_hat(lambda) = R (lambda I-T)^(-1) B, lambda>0.

They include the next-mark probabilities, not just separately normalized conditional waiting densities. All rows and mark endpoints are labeled. The next observation occurs almost surely by finite irreducibility and O nonempty. The entropy rate is

    sigma(Q) = sum_{i<j: q_ij>0} (pi_i q_ij-pi_j q_ji)
                                    log[(pi_i q_ij)/(pi_j q_ji)],

where pi is the unique stationary probability. A *finite local ceiling at Q0* means that some neighborhood of its data, restricted to the declared model class, has bounded sigma. We use maximum row total variation, or the product weak topology of joint row laws on the finite mark set times [0,infinity). The proof also gives a neighborhood defined by finitely many bounded Laplace tests.

**Theorem 1 (finite recovery with at most one uncovered vertex).**

1. If H is empty, any two distinct positive full Laplace matrices determine Q, without calibration of observed rates. One suffices when those rates are known.
2. If |H|=1, any three distinct positive full Laplace matrices determine Q. Two suffice whenever the hidden vertex is adjacent to both endpoints of some observed edge; in particular they suffice at every complete source. No realization minimality is assumed.
3. Each stated inverse has a rational branch with nonzero denominators in a neighborhood of each source to which it applies. It is locally Lipschitz in its finite measurements, hence in maximum row TV, and continuous for weak row-law convergence. These assertions require no common rate bound.

For every N>=4, any prescribed two distinct positive arguments admit an entropy ambiguity with one hidden vertex (Section 5). Thus three, rather than two, are required in the worst case across this class. This is a finite-summary ambiguity, not equality of the full waiting law.

**Theorem 2 (complete-source exact entropy dichotomy).** Let Q0 be complete, meaning q0_ij>0 for every i!=j.

- If |H|<=1, its full-data generator fiber is the singleton {Q0}, even among competitors of unknown reciprocal support on V, and it has a finite local entropy ceiling.
- If |H|>=2, its exact entropy fiber contains **[sigma(Q0),infinity)**. This remains true after fixing every observed rate and tr Q to their source values. The witnessing path starts at Q0, stays within complete support for every finite prelimit parameter, has uniformly bounded rates, and preserves the full joint waiting kernel exactly. Neither source minimality nor a generic-rate condition is required.

The half-line inclusion does not determine whether entropy values below sigma(Q0) also occur. At a reversible complete source, nonnegativity makes the exact image [0,infinity).

**Theorem 3 (sharp local-ceiling criterion).** In the unrestricted unknown-support class above, a finite local ceiling exists **if and only if Q0 is complete and |H|<=1**. The same equivalence holds for either declared data topology and for local boundedness on a sufficiently small neighborhood in finitely many bounded Laplace measurements.

For the subclass with all observed rates and trace fixed, put

    U0 = -tr Q0 - sum_{(i,j) in O} q0_ij.

This is the total rate on unobserved directed transitions. The corrected constrained criterion is **U0=0, or (Q0 complete and |H|<=1)**. If U0=0, the constrained class is a singleton. This exception matters at sparse sources whose every supported edge is observed; it was absent from the single-pair N>=3 case because irreducibility there forces positive unobserved rate slack.

**Corollary (observation design at complete networks).** The minimum number of observed reverse pairs for either exact entropy identification or a finite local ceiling is floor(N/2). More precisely, an observation set succeeds if and only if it covers at least N-1 vertices. A matching on all vertices for even N, or all but one for odd N, attains the bound. It is coverage, not merely the number of measured pairs, that decides a given design.

## 2. Finite inverse and denominator audit

For each i in C select one previous mark I_i ending at i; reverse closure guarantees one. Aggregate next marks by their origin:

    F(lambda)_ij = sum_{J: orig(J)=j} Psi_hat(lambda)_{I_i,J}, i,j in C.

Write k_i=sum_{J:orig(J)=i}q_J>0, D=diag(k_i). If H={h}, partition

    T = [ A     a  ],       a_i=q_ih,
        [ b^T  -d ],       b_i=q_hi, d=b^T 1>0,
    A 1 + a = -k.

The Schur complement gives

    F(lambda) = [lambda I-A-a b^T/(lambda+d)]^(-1) D,
    M(lambda)=F(lambda)^(-1),
    g_i(lambda)=[(M(lambda)1)_i-1]/lambda
               = u_i + v_i/(lambda+d),
    u_i=1/k_i>0, v_i=a_i/k_i>=0.                         (1)

Invertibility holds for every positive lambda: lambda I-T is a nonsingular M-matrix, and its Schur complement is nonsingular. Equivalently, elimination of the scalar block lambda+d>0 yields this directly. At least one a_i is positive by irreducibility; a hidden leaf is allowed.

Order the three arguments lambda1<lambda2<lambda3 and choose any p for which g_p(lambda1)!=g_p(lambda2). Equation (1) shows that this is equivalent to a_p>0. Then

    rho = [(g_p(lambda1)-g_p(lambda2))/(lambda2-lambda1)]
          /[(g_p(lambda2)-g_p(lambda3))/(lambda3-lambda2)]
        = (lambda3+d)/(lambda1+d) > 1,
    d = (lambda3-rho lambda1)/(rho-1).                    (2)

Once d is known, for every i, including v_i=0 rows,

    v_i = [g_i(lambda1)-g_i(lambda2)]
          (lambda1+d)(lambda2+d)/(lambda2-lambda1),
    u_i = g_i(lambda1)-v_i/(lambda1+d),
    k_i=1/u_i, a_i=v_i/u_i.                              (3)

Define L_j=lambda_j I-D M(lambda_j). Then

    W = (L_1-L_2)(lambda1+d)(lambda2+d)/(lambda2-lambda1)
      = a b^T,
    A = L_1-W/(lambda1+d),
    b_j = W_pj/a_p.                                     (4)

Finally recover each individual observed rate, rather than just their sum. If J originates at i, the corresponding full-data column satisfies

    q_J = k_i Psi_hat(lambda1)_{I_i,J}/F(lambda1)_ii.     (5)

The diagonal resolvent entry, and hence F_ii, is strictly positive: starting at i, remaining there for a positive time already gives a positive contribution. Thus every denominator in (2)-(5) is nonzero at the source; no denominator requires all a_i or b_i to be positive. The recovered A is T_CC, so inserting the observed rates from (5) yields Q.

For the two-point branch, take an observed edge i->j whose endpoints both neighbor h. As the observed jump was removed, A_ij=0, and

    M(lambda)_ij = -a_i b_j/[k_i(lambda+d)] != 0,
    rho2=M(lambda1)_ij/M(lambda2)_ij=(lambda2+d)/(lambda1+d),
    d=(lambda2-rho2 lambda1)/(rho2-1).                   (6)

Now use (3)-(5). Completeness guarantees the required edge. Any competing generator matching these two data matrices also has the same nonzero entry in (6), so it belongs to this branch and reconstructs to Q0; competitors need not themselves be assumed complete. This addresses identifiability against the full unknown-support class, not only a neighborhood of complete competitors.

If H is empty, F=(lambda I-T)^(-1)D, so M_2-M_1=(lambda2-lambda1)D^(-1). Recover D and T=lambda1 I-DM_1, and use (5) for individual observed rates. With calibrated rates D and E are known and one F suffices.

Each source branch is a rational map on an open neighborhood of its measured vector: determinants, a_p, u_i, F_ii and rho-1 remain separated from zero in a sufficiently small neighborhood. Constants depend on the source and chosen arguments; no uniform conditioning near a degeneracy is claimed. Laplace tests 1_{J}(mark) exp(-lambda t) are bounded and continuous, so convergence of row laws gives convergence of these finite matrices. Aggregation is a fixed finite linear map. This proves the continuity/Lipschitz statements, including exclusion of rate escape for arbitrary admissible competitors whose measured matrices converge to the source.

## 3. Complete sources with two hidden vertices: exhaustive construction

Pick distinct h,k in H and let W=V\{h,k}; W contains the endpoints of at least one observed edge. All rates involving W are positive. Every resolved mark has origin and destination in W. Put y_h=(q_hi)_{i in W}, y_k=(q_ki)_{i in W}. These two rows are either different or identical; the two cases exhaust sources, including nonminimal sources.

### 3.1 Different external exit rows

After swapping h,k if necessary,

    r = min_{i in W} q_hi/q_ki lies in (0,1).

Set m=q_hk>0, n=q_kh>0, ell_h=m+sum_i q_hi, ell_k=n+sum_i q_ki. On the pair use

    S_e = [1-e  e],        Q_e=S_e^(-1) Q0 S_e,
          [ 0   1]

and use the identity on W. S_e 1=1. Direct multiplication gives

    q_e,ih=(1-e)q_ih,        q_e,ik=q_ik+e q_ih,
    q_e,hi=(q_hi-e q_ki)/(1-e), q_e,ki=q_ki,
    q_e,kh=n(1-e),
    q_e,hk=f(e)/(1-e),
    f(e)=m+e(ell_k-ell_h)-n e^2.                         (7)

Other outside off-diagonal rates are unchanged. Let e* be the smaller of r and the first positive root of f (if no root precedes r, use r). Since f(0)=m>0, we have 0<e*<=r<1 and f(e)>0 on [0,e*). All off-diagonal rates in (7) remain positive there, so Q_e is complete and irreducible; row sums determine its negative diagonal. Similarity preserves trace. Rates are bounded because e*<1 and all expressions have finite limits.

Observed E, R and B obey S_e^(-1) E S_e=E, R S_e^(-1)=R and S_e B=B. Hence T_e=S_e^(-1)T0 S_e and

    R exp(T_e t) B = R exp(T0 t) B for every t>=0.       (8)

The stationary row vector is pi_e=pi0 S_e: outside masses are unchanged, pi_e,h=(1-e)pi0,h and pi_e,k=pi0,k+e pi0,h. Every limiting mass is positive. If f(e*)=0, q_e,hk tends to zero while q_e,kh has a positive limit. Otherwise an external q_e,hi tends to zero at e*=r while q_e,ih has a positive limit. In either case one unordered-pair entropy term diverges to +infinity; all other terms are nonnegative. Thus sigma(Q_e) tends to infinity. A simultaneous internal/external zero causes no difficulty. Equation (8), positivity and the limit justify the whole exact path; a large optimized value is not used.

### 3.2 Identical external exit rows

Write q_hi=q_ki=y_i>0, lambda=sum_i y_i, and c=q0_hk+q0_kh>0. Hold every outside rate and every external entrance/exit rate fixed; vary

    q_hk=m, q_kh=c-m,          0<m<c,                   (9)

with diagonals set by row sums. The source is m=q0_hk. The pair {h,k} is strongly lumpable: its exits to each outside state are y_i, while outside entrance to the aggregate is q_ih+q_ik. The aggregate generator is independent of m. If P is the rectangular indicator matrix of singleton outside blocks and {h,k}, then

    Q_m P=P Qbar, T_m P=P Tbar, B=P Bbar, R P=Rbar.

Observed jumps have endpoints in W, so the same relation holds for the killed generator. Power series or resolvents give R exp(T_m t)B=Rbar exp(Tbar t)Bbar independently of m. This proves the required marked-law equality, not just equality of unmarked dwell times. The aggregate stationary law is fixed, giving fixed outside masses and fixed pi_H=pi_h+pi_k.

Let A=sum_{i in W} pi_i q_ih>0 and B0=sum_{i in W} pi_i q_ik>0. Aggregate stationarity gives A+B0=pi_H lambda. Individual balance yields

    pi_h(m)=[A+pi_H(c-m)]/(lambda+c),
    pi_k(m)=[B0+pi_H m]/(lambda+c).                     (10)

Both stationary limits as m down to zero are positive. The h->k flux tends to zero while the k->h flux tends to B0 c/(lambda+c)>0. All rates are bounded, trace is fixed since the two escape rates sum to 2lambda+c, and completeness holds for every 0<m<c. Entropy therefore diverges. This proof covers the equal-exit stratum regardless of minimality of the observed realization; a minimal-realization similarity theorem alone would not close this case.

In either construction the exact path begins at Q0 and sigma is continuous before the excluded limit. For any s>=sigma(Q0), choose a point with larger entropy and apply the intermediate value theorem along the connecting path. Monotonicity is unnecessary. This proves the entire attainable half-line. The outside stationary masses and observed rates remain fixed in both constructions, so stationary observed jump intensities are also unchanged.

## 4. Local ceilings, sparse sources and calibrated exceptions

At a complete source with |H|<=1, Section 2 gives a rational inverse from two positive matrices. In a small data neighborhood every admissible recovered generator lies in a bounded entrywise neighborhood of Q0 with all off-diagonal rates bounded below by a positive number. The unique stationary law is smooth there, and so is sigma. Hence a finite local ceiling exists and entropy is locally Lipschitz in these measurements. This is local and source dependent; it does not supply a global bound or a uniform condition number.

Every incomplete source has a missing reverse pair {u,v}. It cannot be observed because all observed rates are positive. Open it at

    q_uv(e)=e, q_vu(e)=exp(-1/e^2), e>0,

keeping the old rates fixed and restoring diagonals. For small e, Q_e is irreducible with reciprocal support and Q_e->Q0. Thus pi_e->pi0, with every pi0_i>0. The new pair contributes

    (pi_e,u e-pi_e,v exp(-1/e^2))
       [1/e^2+log(e)+log(pi_e,u/pi_e,v)] ~ pi0_u/e.

Other terms are nonnegative, so entropy diverges. This includes a missing pair between two covered vertices: adjacency of the sole hidden vertex to every covered vertex is **not** sufficient for a ceiling.

These laws converge in row TV, not merely in finitely many transforms. One justification: Q_e stays in a bounded neighborhood of an irreducible Q0 whose observed rates remain positive. For each starting state choose a finite path to a fixed observed jump. Along these paths old supported rates have a common positive lower bound and total rates a common finite upper bound. In a fixed time interval the probability of observing a jump is uniformly bounded below. Iterating intervals gives a uniform exponential tail for the first observed time. On each compact time interval, finite-matrix exponentials and B converge uniformly. Their densities therefore converge in L1 on the full half-line after controlling the common tail. This proves maximum row TV convergence.

For fixed observed rates and trace, if U0>0 choose any existing positive **unobserved** directed rate q_ab and reduce it by e+exp(-1/e^2). It stays positive for sufficiently small e; its reverse stays positive, all observed rates remain fixed, and the increase from opening {u,v} is exactly compensated in -tr Q. The previous divergence and convergence arguments still apply. If U0=0, every unobserved rate must vanish in every admissible constrained competitor, and all observed rates are fixed; thus Q is fixed. No compensation is available or needed.

At a complete source with |H|>=2, Section 3 already provides unbounded entropy in the exact fiber, inside every data neighborhood, even with the same trace and observed rates. Combining these exhaustive alternatives proves Theorem 3 and its constrained version.

For the observation-design corollary, m observed reverse pairs cover at most 2m vertices. Necessity of at least N-1 covered vertices gives m>=ceil((N-1)/2)=floor(N/2). A matching attains the bound. Exhaustive counts for N=2,...,6 check this finite combinatorics, but the counting argument proves it for every N.

## 5. Exact witnesses and executed independent checks

**Four-state finite-summary entropy witness.** Observe all six directed edges of the triangle on vertices 0,1,2; vertex 3 is hidden. Use

    Q1 = [-3  1  1  1]       Q2 = [-24/5  6/5  6/5  12/5]
         [ 2 -3  1  0]            [    2   -3    1     0]
         [ 1  1 -2  0]            [    1    1   -2     0]
         [ 1  0  0 -1],           [    2    0    0    -2].

For the origin-0 aggregate, F1(s)=(s+1)/(s^2/2+2s+1) and F2(s)=(12/5)(s+2)/[s^2+(34/5)s+24/5]; both take values 4/7 at s=1 and 3/7 at s=2. (The first expression is equivalently 2(s+1)/(s^2+4s+2).) The two outgoing mark fractions are 1/2; origin-1 and origin-2 waiting laws are unchanged because their next jump is observed. Thus the **full six-by-six matrices**, including duplicate reset rows, agree at 1 and 2. They differ at 3. Exact stationary currents give

    sigma(Q1)=log(2)/17,
    sigma(Q2)=6 log(2)/97,
    sigma(Q2)-sigma(Q1)=5 log(2)/1649>0.

The independently executed script verifies the full matrices, stationary normalization, reciprocal connected support, third-point disagreement and reconstruction. The ambiguity works for **any prescribed pair** s1!=s2>0: start from y(s)=a0+b0/(s+v0), with a0,b0,v0>0, and put

    C0=(s1+v0)(s2+v0),
    a(w)=a0+b0(v0-w)/C0,
    b(w)=b0(s1+w)(s2+w)/C0,
    k(w)=1/a(w), u(w)=b(w)/a(w), v(w)=w.

For w>0 near v0 with a(w)>0, the leaf transform is k/[s+k+s u/(s+v)] and its two measured values stay fixed. The visible triangle keeps outgoing fractions 1/2 at vertex 0 and the other rows displayed above. Stationary unnormalized weights are (10/k,3,4,10u/(kv)), and entropy is log(2)/Z(w), where

    Z(w)=7+10a(w)+10b(w)/w,
    Z'(w)=-10 b0 s1 s2/[C0 w^2]<0.

Thus distinct nearby w have different entropy despite equal two-point data. Adding observed unit-rate leaves at vertex 1 adds 3 per leaf to Z and preserves both the observation agreement and this strict derivative. This proves worst-case necessity for every N>=4. For the two displayed generators the cycle-current coefficients become 1/[17+3(N-4)] and 6/[97+18(N-4)], still distinct. Exact code checks N=5,6 and independently verifies the symbolic interpolation and derivative. These examples do not refute two-point recovery at complete sources and do not assert equal observed intensities or full-record equivalence.

**Reversible complete source with exact entropy image [0,infinity).** Start with all off-diagonal rates equal to 1 on four states, observe 0<->1, and replace q_23=m, q_32=2-m, 0<m<2. All other off-diagonal rates stay 1. Then

    pi(m)=(1/4,1/4,(3-m)/8,(1+m)/8), tr Q=-12,
    sigma(Q_m)=(1/4)log(1/m)+O(1), m down to zero.

The source m=1 is reversible, every observed rate stays 1, and all rates remain below 2. The complete killed-generator intertwining and an independently formed symbolic resolvent both prove the same full two-mark transform for every m. Nonnegativity, continuity and the divergent limit give the entire entropy image [0,infinity). The example illustrates the nonminimal equal-exit branch, rather than leaving it implicit.

Reproduction from the repository root (assertions enabled):

```text
.venv/Scripts/python.exe -B analysis/novelty_loop/one_hidden_independent.py
.venv/Scripts/python.exe -B outputs/novelty-loop-2026-09-19/referee_checks.py
.venv/Scripts/python.exe -B analysis/novelty_loop/coverage_crosscheck.py
```

Outputs: [one-hidden-independent.json](one-hidden-independent.json), [referee_checks.json](referee_checks.json), [coverage-crosscheck.json](coverage-crosscheck.json). Embedded exact rational inputs, source hashes, versions, parameter domains and arithmetic are recorded. The sparse rate sequence uses a rational reverse rate 2^(-n^2) and 100-digit entropy evaluation; its diverging limit follows from the displayed analytical construction, not from finitely many numerical values.

The independent implementations check different aggregation choices, complete and sparse strata through N=6, disconnected observation graphs, an internal shear boundary before the external boundary, equal-exit lumping, and the finite-summary entropy witness. They share the CTMC observation model and standard symbolic library; they are not independent experimental evidence or formal proofs. Universal claims rest on Sections 2-4, with the independent referee's scope review in [REFEREE.md](REFEREE.md) and the falsification note in [ONE-HIDDEN-INDEPENDENT.md](ONE-HIDDEN-INDEPENDENT.md).

## 6. Novelty and remaining scope

Burgarth's CTMC zero-forcing theorem uses all-time observed-state semigroups and already covers all but one observed state. Exact resolved waiting laws can recover those restricted semigroups by a resolvent identity; hence all-time one-hidden recovery by itself should not be promoted as the main new result. The finite positive-transform branch proves the stronger bounded-measurement continuity used here. Wagner--Timmer supplies exact hidden thermodynamic ambiguity for aggregated CTMCs; Vanluyten--Willems--De Moor supplies normalized-similarity equivalence under minimality hypotheses; Ehrich reports a compatible discrete-time example with apparently unbounded grid maxima. The present target adds universal complete-source quantifiers, exact fixed-dimensional divergence, preserved marks/trace, and the nonminimal equal-exit case. [Primary sources and precise comparisons](LITERATURE.md).

The bounded primary-source audit found no matching full theorem. It does not establish priority, and the detailed comparison with finite-frequency/Loewner realization remains an access gap. Known support, additional nonminimal states, unresolved channels, blurred marks, macrostate resets and different observation models require separate statements. The exact entropy images at sparse sources with multiple hidden vertices and the full lower part of the special five-state subcritical image remain open. Local ceiling existence does not by itself certify finite-trajectory coverage or provide a practical tight optimization algorithm.

The next useful cycle is to audit finite-frequency prior work and optimize the conditioning/design tradeoff among coverage-sufficient observation sets. A separate structural route could classify exact entropy images as finite unions of intervals/points under a fixed state cap using finite polynomial compatibility and fixed-support continuity; this is a proposed next result, not established by the present cycle.
