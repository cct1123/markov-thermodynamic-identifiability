# Observation coverage and physical regularization audit

2026-09-14 UTC. Contribution labels: **inference / conventionally proved** for the arguments below; **reproduced calculation** only for the exact checks in the final section. No priority claim. This extends the observation-graph formulation already present in manuscript Lemma `lem:neighborhood` and preserves the existing hidden-shear proof.

## Observation graph and a positive coverage result

Let the declared microscopic vertex set V be fixed and finite. Let O be a nonempty reverse-closed set of individually resolved directed transitions, all with positive rates and known endpoints. A vertex is *covered* when incident to a transition in O; by reverse closure it then has both an incoming and outgoing observed transition. A fully hidden vertex is uncovered. Set E=sum over observed rank-one jump matrices, T=Q-E, R_I=e_destination(I)^T and B_J=q_J e_origin(J). The complete next-event kernel is R exp(Tt) B. Individual entries retain joint probabilities and absolute time.

**Proposition (full vertex coverage).** If every vertex is covered, two distinct positive Laplace arguments determine Q uniquely on this fixed vertex set. The inverse on admissible data is rational and locally Lipschitz, hence locally Lipschitz in maximum row TV and continuous in the product weak topology of the row laws. No common rate bound is needed.

**Proof.** For each i choose an observed mark I_i ending at i and an observed mark J_i beginning at i. Their rates a_i=q_{J_i} are positive. The selected N by N kernel matrix is

    F(lambda)_{ij}=Psi_hat_{I_i,J_j}(lambda)
                 = [(lambda I-T)^(-1) D]_{ij}, D=diag(a_i).

The killed resolvent is invertible for lambda>0. For M_k=F(lambda_k)^(-1),

    M_2-M_1=(lambda_2-lambda_1)D^(-1),
    D=(lambda_2-lambda_1)(M_2-M_1)^(-1),
    T=lambda_1 I-D M_1.

For any remaining observed mark J let f_J be its measured column restricted to the chosen rows I_i. Then

    (lambda_1 I-T) f_J=q_J e_origin(J).

This recovers every observed rate, so Q=T+E is recovered. Every matrix inverse has a nonzero denominator at each admissible source and remains well defined in a sufficiently small neighborhood. These rational formulas extend smoothly to a neighborhood in ambient measurement space (even though off-model data need not yield a diagonal D or physical Q). Each Laplace measurement is a bounded continuous test of the row laws and is TV-Lipschitz. This proves the assertions. There are no hidden-label ambiguities because all vertices have named observed incidence. □

This proves more than recovering rates by psi_reverse,forward(0), because evaluation of a density at zero is not continuous in TV. Two positive Laplace points give the required bounded measurement functions. It also shows that fixed positive event rates are not a necessary external calibration.

**Entropy consequence.** At a complete source, all recovered reverse rates stay positive in a sufficiently small data neighborhood, so the entropy inverse is locally Lipschitz and there is a finite local upper ceiling. At an irreducible sparse source the same conclusion holds if competitors have the same known support (or cannot add edges and remain near that source). Full coverage therefore does not require observing every physical edge. In a complete three-state graph, observing 1<->2 and 2<->3 covers all vertices, while the reciprocal pair 1<->3 remains hidden and causes no failure of identification or local boundedness.

**Sparse-boundary qualification.** If the class permits newly opening unobserved pairs, vertex coverage alone does not ensure an entropy ceiling at a sparse source. In the unit tree 1<->2<->3 observe both old pairs, and open q_13=e and q_31=exp(-1/e^2), preserving the four old rates. The generators approach the tree, the row laws converge in TV by finite-state killing-time coupling, pi_1 approaches 1/3, and the new edge contributes asymptotically 1/(3e). Q is still reconstructed uniquely from each exact observed kernel. Here the trace changes by the vanishing quantity -(e+exp(-1/e^2)); this example does **not** retain a fixed trace while fixing every existing rate. A fixed trace equal to the sum of all fixed observed rates would forbid any extra edge in this special source.

## What the negative results do and do not classify

The manuscript's existing multiple-mark hidden-pair lemma proves: with at least two uncovered vertices, unknown reciprocal support and fixed N, every positive row-TV neighborhood has unbounded entropy; observed rates and trace can also be preserved. The perturbation to a complete graph uses unobserved rate slack, which is available with uncovered vertices. Then a normalized similarity on two uncovered coordinates fixes every marked jump map, reset row and input column. This requires no assumption that all other states are observed.

For an **exact** fiber at fixed support, two uncovered states alone are insufficient as a general conclusion. The existing hidden-pair audit provides sufficient conditions: adjacent external twins, or equal-escape unjoined external twins with distinct exit rows; adjacent external twins with equal exit rows are covered by strong lumping. A known connected tree has sigma=0 for all rates, so can have many uncovered vertices without entropy divergence. Incomparable pair neighborhoods obstruct that pair-only shear but do not classify the full similarity orbit.

The graph classification now has two firm sufficient extremes: full coverage gives generator recovery and complete-source ceilings; two or more uncovered vertices give local unboundedness in the unknown-support class. The case of exactly one uncovered vertex in arbitrary N is not exhausted by these statements. The one-pair N=3 theorem settles its special case. Observing more edges may also determine entropy without determining every rate; no necessity claim for full coverage is made.

If the dimension is unknown, a compatible model containing a fully hidden vertex can be split into two strongly lumpable clones. The existing Appendix `app:split` proves exact all-time observation preservation and unbounded entropy with one extra state. This needs a fully hidden vertex: splitting a named endpoint while claiming to preserve an individually resolved microscopic jump changes the observation model. Linear minimal order, minimum positive order and minimum order in a chosen canonical topology are different notions. For the balanced family, the source is already physical and linearly minimal of order five, so its minimum physical order equals five; this special coincidence does not hold for arbitrary positive-realization problems.

State lumping differs from resolved-edge observation. A macrostate jump usually leaves an unknown distribution of microscopic reset states, so adjacent waiting-time laws need not compose into all higher-order observed laws. Strong lumpability is a sufficient property of selected constructions, not an assumption that arbitrary coarse data are Markovian. Under lumping, even an observed graph covering every macrostate does not meet the full microscopic vertex-coverage hypothesis.

## Bounds and continuity under physical priors

Write K=sum_i pi_i sum_{j!=i}q_ij for stationary jump activity (inverse time), and A_max=max_supported |log(q_ij/q_ji)| for the dimensionless maximum edge rate affinity. Stationarity cancels log pi terms, giving

    0 <= sigma = sum_{i!=j} pi_i q_ij log(q_ij/q_ji) <= K A_max.

Nishiyama and Hasegawa's stronger established result is

    sigma <= K A_max tanh(A_max/2),

with the value 0 at A_max=0. Their original [PRE 108, 044139 (2023)](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevE.108.044139/fulltext), Eqs. (5)--(8), was re-read on 2026-09-14. This is a bound using a *microscopic* rate-ratio constraint and microscopic activity, not an upper bound derived from arbitrary partially observed waiting laws. A bound on observed event activity is not automatically a bound on K.

| Prior | Entropy ceiling | Continuity and conditioning | Physical content |
| --- | --- | --- | --- |
| q_ij <= M alone | No; the existing fixed-trace tree example has M=1 | Does not control logarithmic reverse-rate singularity | Kinetic timescale bound |
| q_ij >= m on supported edges alone | No; rates can grow without limit | Removes small rates on declared support, but not every inverse degeneracy | Kinetic lower bound; cannot be added as numerical pseudocount |
| m <= q_ij <= M on a fixed connected support | sigma <= (N-1) M log(M/m), with the sharper tanh factor available | Q->sigma is uniformly Lipschitz on this compact class; generator identifiability is still a separate condition | Rate floor and ceiling jointly bound rate affinities |
| A_max <= A alone | No; a biased cycle can be sped up arbitrarily | Controls edge asymmetry, but leaves activity and observation degeneracies | Thermodynamic rate-affinity prior under local detailed balance |
| A_max <= A and K <= K_0 | sigma <= K_0 A tanh(A/2) | Entropy continuous under Q convergence to an irreducible limit, even when pairs vanish together; no automatic inverse identification | Bounds activity and allowed entropy change per jump |
| Known connected tree support | sigma=0 | Entropy known even if rates are not | Topology rules out cycle currents |

For the continuity assertion, split the finitely many pairs into those with positive limiting rates and those absent at the limit. The first are smooth since stationary probabilities converge and stay positive at an irreducible limit. For the second, the directed representation bounds the magnitude of each contribution by A pi_i q_ij, which vanishes. In fact entropy is locally Lipschitz on the bounded-ratio cone near an irreducible source: the gradient of x log(x/y) is bounded when x/y lies in a fixed compact positive interval, including after continuous extension to the paired zero. The stationary law is locally smooth in Q. None of this proves a locally Lipschitz inverse observation map when exact equivalences remain.

**Additional counterexample (floor plus activity is insufficient).** Set q_12=c>=1 and every other off-diagonal rate of a complete three-state generator to 1. Then

    pi=(1/(c+2), (2c+1)/(3(c+2)), 1/3),
    K=3(c+1)/(c+2)<3,
    sigma=(c-1)/(3(c+2)) log c -> infinity.

Thus even a fixed floor and activity ceiling need not bound entropy without control of rate ratios or upper rates. The fast state has small occupancy; activity control alone does not bound every microscopic rate. This is a generator-level counterexample, not an exact observation-preserving family.

## Thermodynamic terminology and detector limitations

The proved functional is stationary Schnakenberg/network entropy production for a finite CTMC with even states and one channel per pair. Algebraic results require positivity, reciprocity and stationarity; they do not require a chosen reservoir interpretation. Physical entropy production requires a thermodynamically consistent microscopic/mesoscopic state description and channel-resolved local detailed balance. With intrinsic state entropies s_i, a channel can obey log(q_ij^alpha/q_ji^alpha)=Delta s_res^alpha+s_j-s_i. The mean state-entropy increment vanishes at stationarity; total and medium/environment entropy-production rates then agree under the usual sign convention, although trajectory quantities differ by a boundary term. An abstract generator by itself does not specify a unique heat current, reservoir temperature or chemical-work decomposition.

For the exp(-1/e^2) reverse-rate example, a bounded forward rate combines with unbounded log(q_ij/q_ji), representing an unbounded per-transition thermodynamic bias under local detailed balance. It is excluded by a fixed edge-affinity prior. A cycle affinity is a sum of edge rate affinities; the two should not be interchanged. Correct reservoir-channel identification matters: aggregating parallel channels can hide dissipation even if every state transition is observed. See Esposito (2012), Sec. II.A, Eqs. (3)--(4), (8), (14)--(17), and Sec. IV; these passages were directly read in [arXiv:1112.5410](https://arxiv.org/pdf/1112.5410).

Finite bandwidth, timestamp binning, missed events and blurred labels alter the likelihood. Known random processing applied equally to both microscopic experiments contracts total variation, so it cannot remove an existing indistinguishability obstruction. It can also destroy the microscopic reset property used in the constructive inverse. In particular, finite timing bins with all events retained are not detector dead time with missed events. Stationarity, complete event capture, known event incidence and a correctly specified detector must be stated before interpreting the proposed finite-data intervals.

## Executed exact checks

The following code is retained here as a transparent exact check. Run from project root with `@' ... '@ | .\.venv\Scripts\python.exe -B -` in PowerShell. No random seed or numerical tolerance is used; all data and Laplace arguments are rational. The check source was executed on 2026-09-14 with Python 3.9.12 and SymPy 1.14.0. It checks a sparse covered graph with an unobserved edge and extra redundant observed marks, so it can catch row/column, killing-diagonal and unselected-mark mistakes. It also checks the activity counterexample symbolically. These examples support the displayed proof; they do not establish its universal quantifiers.

```python
import sys
import sympy as s
n=4
Q=s.Matrix([[-6,1,2,3],[4,-10,0,6],[7,0,-16,9],[10,11,12,-33]])
marks=[(0,1),(1,0),(2,3),(3,2),(0,2),(2,0)]
E=s.zeros(n)
for i,j in marks: E[i,j]=Q[i,j]
T=Q-E
incoming=[(1,0),(0,1),(3,2),(2,3)]
outgoing=[(0,1),(1,0),(2,3),(3,2)]
D=s.diag(*[Q[i,j] for i,j in outgoing])
R=s.Matrix([list(s.eye(n)[j,:]) for i,j in incoming])
B=s.zeros(n,len(marks))
for k,(i,j) in enumerate(marks): B[i,k]=Q[i,j]
la,lb=s.Rational(2,3),s.Rational(7,2)
Ya=R*(la*s.eye(n)-T).inv()*B
Yb=R*(lb*s.eye(n)-T).inv()*B
cols=[marks.index(j) for j in outgoing]
Fa=Ya[:,cols]; Fb=Yb[:,cols]
Dr=(lb-la)*(Fb.inv()-Fa.inv()).inv()
Tr=la*s.eye(n)-Dr*Fa.inv()
Er=s.zeros(n)
for k,(i,j) in enumerate(marks):
    z=(la*s.eye(n)-Tr)*Ya[:,k]
    assert z==Q[i,j]*s.eye(n)[:,i]
    Er[i,j]=z[i]
assert Dr==D and Tr==T and Tr+Er==Q
c=s.symbols('c', positive=True)
C=s.Matrix([[-c-1,c,1],[1,-2,1],[1,1,-2]])
pi=s.Matrix([[1/(c+2),(2*c+1)/(3*(c+2)),s.Rational(1,3)]])
assert s.simplify(sum(pi)-1)==0 and (pi*C).applyfunc(s.simplify)==s.zeros(1,3)
K=sum(-pi[i]*C[i,i] for i in range(3))
J=pi[0]*C[0,1]-pi[1]*C[1,0]
assert s.simplify(K-3*(c+1)/(c+2))==0
assert s.simplify(J-(c-1)/(3*(c+2)))==0
print(sys.version.split()[0], s.__version__)
print('covered-graph exact inverse: PASS; floor/activity counterexample: PASS')
```

Output:

```text
3.9.12 1.14.0
covered-graph exact inverse: PASS; floor/activity counterexample: PASS
```
