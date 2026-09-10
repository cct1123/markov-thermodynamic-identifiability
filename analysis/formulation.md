# Mathematical formulation

Working formulation, 2026-09-10. Definitions and the elementary deductions below are agent-maintained scope choices, not claims of novelty. The human brief remains [PROJECT.md](../PROJECT.md). Literature and validation records are maintained in [evidence/RECORDS.md](../evidence/RECORDS.md).

## Model and thermodynamic convention

Start with an irreducible, time-homogeneous CTMC on a finite set V of N states. Use the row-generator convention: q_ij >= 0 for i != j, q_ii = -sum_{j != i} q_ij, and p'(t) = p(t) Q. The unique stationary probability row vector satisfies pi Q = 0 and pi 1 = 1. Time is measured in a fixed physical unit.

The initial admissible class consists of simple bidirected graphs: q_ij > 0 iff q_ji > 0, with one kinetic channel for each ordered state pair. All individual rates are finite. Missing links have both rates zero. Treat states as even under time reversal. These restrictions isolate the conventional finite-state jump-process entropy production; irreversible edges, odd variables, parallel reservoir channels, external protocols, and detector errors require separate formulations.

In units with k_B = 1, define the steady-state entropy-production rate

$$
\sigma(Q)=\sum_{i<j:\,q_{ij}>0}
(\pi_i q_{ij}-\pi_j q_{ji})
\log\frac{\pi_i q_{ij}}{\pi_j q_{ji}}.
$$

Equivalently, stationarity cancels the system-entropy contribution, giving the directed sum sum_{i != j} pi_i q_ij log(q_ij/q_ji). The first expression makes nonnegativity and zero at detailed balance explicit. Interpreting this as the full physical dissipation assumes the elementary states and thermodynamic channels are sufficiently resolved and local detailed balance applies. Generator-level entropy need not equal reservoir-resolved entropy when parallel channels are silently aggregated.

## Observation object

An observable mark I identifies one directed edge (a_I,b_I), not a collection of edges. Observing I resets the conditional microscopic state to b_I. The nonempty observable set O is initially closed under reversal, with bar(I)=(b_I,a_I). The detector records every passage along these edges, with direction and exact timestamps. All other jumps are unobserved.

For consecutive observed event times tau_n and marks I_n, the data are the joint next-mark/time densities

$$
\psi_{IJ}(t)\,dt
=\Pr\{I_{n+1}=J,\;\tau_{n+1}-\tau_n\in[t,t+dt)\mid I_n=I\}.
$$

Each row integrates to one after summing over J. An individual entry generally integrates to a transition probability P_IJ, not one. Knowing only separately normalized conditional densities f(t|I,J) omits P_IJ and defines a weaker inverse problem. Here complete infinite-statistics data mean all joint kernels for all t >= 0, including zero entries and their absolute time scale. This convention agrees with the resolved-transition kernel in van der Meer, Ertel and Seifert (2022), Eq. (3), and its factorization in Eq. (56): [primary text](https://arxiv.org/html/2203.12020v2).

Resolved marks are consequential: they make the observed process a Markov renewal process. Blurred marks generally do not reset to a unique microscopic state, and pairwise waiting distributions then need not determine its complete observed trajectory law.

## Forward map and event frequencies

Let E=sum_{J in O} q_(a_J b_J) e_(a_J) e_(b_J)^T and T=Q-E. Only observed off-diagonal entries are removed; the diagonal remains that of Q. Recomputing row-sum-zero diagonals would describe a different process. T is the transient generator before the next observed jump. Let R have row I equal to e_(b_I)^T, and let B have column J equal to q_(a_J b_J) e_(a_J). Then

$$
\Psi(t)=R e^{Tt}B,\qquad
\widehat\Psi(s)=R(sI-T)^{-1}B.
$$

This is a shared matrix-valued absorption representation, not a separate arbitrary phase-type fit for every kernel. The same Q, observed-edge incidence, and rate parameters constrain R, T, and B simultaneously. The absorbing construction is prior art; see van der Meer et al. (2022), Appendix A.3.

For a finite irreducible model with nonempty O, the next observed event occurs almost surely with finite mean. Define P=int_0^infty Psi(t)dt=R(-T)^(-1)B. Its stationary event-index distribution rho obeys rho P=rho, rho 1=1. If m_I=sum_J int_0^infty t psi_IJ(t)dt and m=sum_I rho_I m_I, then the event rate of mark I is nu_I=rho_I/m=pi_(a_I) q_(a_I b_I). Thus absolute event frequencies are determined by the full joint kernels in this stationary setting; they need not be independent extra input. This renewal calculation is included to make the data convention explicit.

## Compatibility and the question being classified

Choose an admissible class C before using the word identifiable. It must state the allowed N, graphs, rate domain, observed-edge incidence, and any physical restrictions. Initially take the observed endpoints and their incidence as known, with hidden-state relabelings regarded as equivalent descriptions. If only event labels and their reversals are known, take the union over admissible endpoint identifications instead; that larger problem must be labeled separately.

For data D=Psi, define

$$
\mathcal F_{\mathcal C}(D)=\{M\in\mathcal C:\Psi_M(t)=\Psi(t)\text{ for every }t\geq0\},
\qquad
\mathcal S_{\mathcal C}(D)=\{\sigma(M):M\in\mathcal F_{\mathcal C}(D)\}.
$$

Models in the same fiber F are observationally equivalent. With resolved marks, equality determines all event-indexed finite trajectory laws, and the stationary time-origin version follows from renewal stationarity. Model equivalence here requires equality of functions, not agreement on a grid, finitely many approximate moments, or one entropy estimator.

For a nonempty fiber:

- **Exact thermodynamic identifiability:** S is a singleton. Microscopic parameter uniqueness is sufficient but not necessary.
- **Bounded but non-unique:** S contains at least two values and sup S < infinity. Its infimum and supremum need not be attained.
- **Unbounded above:** sup S = infinity. Each admissible model can still have finite entropy production.

An empty fiber means the data and class are inconsistent, not a fourth physical entropy class. Non-identifiability includes both bounded non-uniqueness and unboundedness. A finite lower bound alone does not imply a bounded entropy range.

Keep separate: fixed labeled topology; fixed N with unknown topology; N <= N_max; unrestricted finite N; and minimal-realization subclasses. Identifiability in a smaller class need not survive enlargement. Generic identifiability also does not settle exceptional symmetric or nonminimal models. In particular, exact estimator recovery conditional on a hidden forest is not evidence that every observationally equivalent realization has a hidden forest.

## Exact finite certificates

The derivatives at zero satisfy Psi^(k)(0)=R T^k B. For two finite realizations of dimensions n and n', equality for k=0,...,n+n'-1 suffices for equality at every time. To see this, represent the difference by the block diagonal matrix diag(T,T'), input stack [B;B'], and output [R,-R']. Cayley-Hamilton gives a recurrence of order at most n+n' for every matrix entry of its Markov parameters. Vanishing of the first n+n' parameters forces all subsequent ones to vanish, and the convergent exponential series then vanishes identically. Equality for all times plainly implies these derivative equalities.

This elementary realization-theory deduction provides a possible exact checking method, not a new general identifiability theorem. When both dimensions are <= N_max, parameters k=0,...,2N_max-1 are sufficient for comparing a candidate pair. Positivity, sparsity, generator normalization, and the shared edge-incidence constraints must still be imposed; a real rational transfer function alone does not characterize admissible microscopic models.

## Immediate research target

The initial small-network tests are complete: [the audit](small-network-audit.md) gives at-most-three-state recovery and both lumpable and minimal four-state unbounded fibers. [The orbit proof](compatibility-orbit.md) classifies the full-positive fixed diamond and reduces every minimal four-state fiber to a two-parameter hidden similarity domain. The next question is whether other fixed-graph minimal four-state fibers can have bounded but nonunique entropy without a common positive lower rate cutoff. The boundary behavior of stationary fluxes matters: an upper bound on rates does not prevent logarithmic entropy divergence as a positive reverse rate approaches zero. Conversely, imposing a compact strictly positive rate domain would make finite bounds largely a compactness consequence rather than the intended unrestricted classification.
