# Thermodynamic identifiability: frontier assessment

**Initial frontier assessment and exact small-network exploration completed 2026-09-10 UTC. The general classification and publication novelty remain unresolved.** This is an evidence-backed working report, not a paper draft. The human [research brief](../PROJECT.md) is preserved.

The problem is mathematically definite once the observation protocol and admissible microscopic models are fixed. It substantially overlaps established inference and realization theory. A plausible narrower contribution concerns the **entire entropy-production range of a resolved-edge compatibility class**, especially whether that range can be bounded but nonunique without prescribed positive lower rate bounds.

The preliminary mathematics already rules out two tempting shortcuts: minimal realizations need not identify entropy, and topology alone cannot classify it. Exact examples and proofs below support those conclusions; their novelty has not been established.

## Precise question

Let Q be a finite irreducible row generator on a simple bidirected graph, with finite positive rates on every included edge and one thermodynamic channel per ordered state pair. States are even under time reversal. A detector records every occurrence of selected individually resolved directed edges, with known incidence; the nonempty observed set is closed under reversal.

The data are the full joint densities

$$
\psi_{IJ}(t)\,dt
=\Pr\{I_{\mathrm{next}}=J,\ \tau_{\mathrm{next}}-\tau\in[t,t+dt)\mid I\},
$$

including their amplitudes, next-mark probabilities, and absolute time scale. They are not merely separately normalized dwell-time shapes. Resolved marks reset the microscopic state, so this matrix kernel determines the stationary observed process. With observed off-diagonal rates removed while original diagonals are retained,

$$
\Psi(t)=R e^{Tt}B,\qquad
\sigma(Q)=\sum_{i<j:q_{ij}>0}
(\pi_iq_{ij}-\pi_jq_{ji})
\log\frac{\pi_iq_{ij}}{\pi_jq_{ji}},
\quad \pi Q=0.
$$

Boltzmann's constant is one. Entropy production has inverse-time units.

For an explicitly specified class C, characterize

$$
\mathcal S_{\mathcal C}(\Psi)
=\{\sigma(Q): Q\in\mathcal C,\ R e^{Tt}B=\Psi(t)\ \text{for every }t\ge0\}.
$$

For compatible data this set is either a singleton, bounded but non-singleton, or unbounded above. Fixed topology, fixed cardinality, a cardinality cap, unrestricted finite order, and minimal realizations are different choices of C. A result in one does not silently extend to another. Full definitions and the finite exact kernel-equality certificate are in [the formulation](../analysis/formulation.md), [E016](../evidence/RECORDS.md#e016), and [D001](../evidence/RECORDS.md#d001).

This addresses structural identifiability with infinite statistics. Stability under noisy or temporally unresolved measurements remains a separate problem.

## Frontier map

| Category | What the inspected evidence establishes | Implication |
| --- | --- | --- |
| Already known | Resolved-edge waiting kernels, absorbing representations, boundary-rate recovery, affinity/path inference; compatible-model lower-bound optimization | These concepts are prior infrastructure. [E001–E006](../evidence/RECORDS.md#e001), [E014](../evidence/RECORDS.md#e014) |
| Known under restrictions | Exact entropy recovery in specified observed-cycle structures; aggregate equivalence under rank/spectral conditions; reconstruction with particular state observations and known topology | Preserve each theorem's data and model assumptions. [E001](../evidence/RECORDS.md#e001), [E007](../evidence/RECORDS.md#e007), [E009](../evidence/RECORDS.md#e009), [E022](../evidence/RECORDS.md#e022) |
| What bounds do not determine | A minimum or trajectory lower bound need not give an upper bound, uniqueness, or all compatible generators | Estimator saturation conditional on one topology is not uniqueness over larger classes. [E004–E006](../evidence/RECORDS.md#e004) |
| Known non-identifiability | Exact hidden similarities, equilibrium/nonequilibrium aggregate ambiguity, and numerically varying entropy in a masked four-state model | A new indistinguishable pair or formal optimization alone is a weak novelty claim. [E004](../evidence/RECORDS.md#e004), [E008](../evidence/RECORDS.md#e008), [E010](../evidence/RECORDS.md#e010) |
| Unresolved in this investigation | Full entropy images over the positive, edge-constrained compatibility domain; bounded non-singleton fibers beyond the classified diamond | This is a candidate gap, not proof that no prior theorem exists. [E019](../evidence/RECORDS.md#e019), [E021](../evidence/RECORDS.md#e021) |
| Small promising opening | Exact four-state classification using the two hidden-similarity parameters and their physical boundaries | Proceed with a falsifiable mathematical problem before broad enumeration. [D002](../evidence/RECORDS.md#d002), [D003](../evidence/RECORDS.md#d003) |

The closest novelty constraints are Ehrich's compatible-model entropy optimization, Wagner-Timmer's exact equilibrium ambiguity, Wu-Jia's compatibility/equilibrium framework, and Siekmann's small-network equivalence classes. Their assumptions and access limitations are recorded in [E004](../evidence/RECORDS.md#e004), [E008](../evidence/RECORDS.md#e008), [E009](../evidence/RECORDS.md#e009), and [E010](../evidence/RECORDS.md#e010).

Classical marked-arrival and phase-type theory supplies useful algebra, but scalar realization existence does not enforce a common generator with the required observed edges. Algebraic minimality also need not equal minimal positive-realization order. [E011–E012](../evidence/RECORDS.md#e011).

Backward and forward tracing is preserved in the two [literature](../evidence/hidden-entropy-frontier.md) [memos](../evidence/realization-frontier.md). The search includes recent 2024–2026 follow-ups and older ion-channel and realization terminology. Exact full-text hypotheses remain unavailable for some close sources, particularly Larget's canonical-representation theorem and the original Xiang et al. reconstruction proof. Those are material novelty-verification gaps.

## Checked small-network results

These are deductions made and checked in this workspace. They are not attributed as new published results.

| Admissible class and data | Result | Evidence |
| --- | --- | --- |
| At most three states, one resolved observed bidirectional edge | The full generator and topology are identified by zero-time values and the first two derivatives, including hidden leaves | [E017](../evidence/RECORDS.md#e017) |
| Fixed four-state diamond, lumpable hidden pair | One fixed kernel admits entropy range [0, infinity); the kernel has a smaller three-state realization | [E018](../evidence/RECORDS.md#e018) |
| Fixed complete four-state graph, minimal dimension four | One fixed kernel still admits the entire entropy range [0, infinity) | [E019](../evidence/RECORDS.md#e019) |
| Fixed full-positive four-state diamond, distinct hidden escape rates | Every rate is identified up to exchanging hidden labels | [E021](../evidence/RECORDS.md#e021) |
| Same full-positive diamond, equal hidden escape rates | Every such fiber is unbounded above, including nonminimal cases; its infimum is not generally determined here | [E021](../evidence/RECORDS.md#e021) |

Thus four states is the smallest fixed cardinality allowing thermodynamic non-identifiability under this particular observation scheme. This does not mean data fitted by three states exclude larger hidden models.

The full diamond has observed x↔y and all four hidden-visible links, with no hidden-hidden link. Its equal/distinct escape-rate cases can be distinguished from the data. This gives a complete classification for that specified topology, including its nongeneric equal-escape stratum. It is not a classification of every four-state graph.

## Why minimality does not rescue entropy inference

A particularly compact minimal diamond starts with

$$
Q_0=\begin{pmatrix}
-4&1&2&1\\
1&-4&1&2\\
2&1&-3&0\\
1&2&0&-3
\end{pmatrix},
$$

in order (x,y,h,k), observing only x↔y. Let

$$
S_e=\operatorname{diag}\left(I_2,
\begin{pmatrix}1-e&e\\0&1\end{pmatrix}\right),
\qquad Q_e=S_e^{-1}Q_0S_e,\qquad 0\le e<\tfrac12.
$$

Every required edge remains positive, all rates stay bounded, and all four joint waiting kernels remain exactly unchanged. Controllability and observability have rank four, so no smaller finite linear or CTMC realization can produce this kernel. The stationary distribution and entropy are

$$
\pi_e=\tfrac14(1,1,1-e,1+e),\qquad
\sigma(e)=\frac e4
\log\frac{(1+2e)(2-e)}{(1-2e)(2+e)}.
$$

At e=0 entropy is zero; at e=1/4 it is log(7/3)/16 ≈ 0.0529561163. As e approaches 1/2, one reverse flux vanishes while its opposing flux stays positive, and

$$
\sigma(e)=\tfrac18\log\frac1{1/2-e}+O(1)\longrightarrow\infty.
$$

Continuity proves the whole range [0,infinity), rather than merely two distinct entropy values. The complete-graph example supplies an independent topology with the same conclusion. The arguments appear in [the orbit note](../analysis/compatibility-orbit.md) and [the small-network audit](../analysis/small-network-audit.md).

For the general diamond, write the hidden block as H=diag(-λh,-λk), with entrance and exit matrices X,Y. The observed visible resolvent determines

$$
F(z)=X(zI-H)^{-1}Y.
$$

Distinct escape rates give two noncancelling positive residue matrices; their residues and row-sum normalization reconstruct the hidden rates. Equal escapes give F(z)=XY/(z+λ), permitting positive factorizations of XY that reach a divergent one-way boundary. This is why topology alone cannot decide the answer.

## Validation and limitations

The [verification script](../analysis/check_small_networks.py) checks exact rational identities, stationary laws, ranks and sufficient finite Markov-parameter equalities. Independent matrix exponentials and edge-flux sums agree to numerical precision; a changed physical rate and an incorrectly recomputed killed diagonal both fail the equality check as intended. The [recorded output](../analysis/small-network-checks.json) supplies versions, residuals and the script checksum; [E020](../evidence/RECORDS.md#e020) records provenance and run limitations.

Exact certificates establish all-time equality. The numerical grid alone does not. General parameter-domain conclusions rely on the analytic proofs, not enumeration. The examples reject minimality as a cure, topology alone as a classifier, and rate upper bounds as sufficient to bound entropy. A positive lower rate cutoff would exclude their divergent boundaries.

## Remaining gap, risk and next action

The most plausible small research target is:

> Does any minimal four-state fixed-graph resolved-edge compatibility class have a finite, non-singleton entropy range when rates are constrained only to be positive on the chosen bidirected topology?

For minimal realizations, the entire same-dimensional compatibility class is reduced to

$$
Q'=S^{-1}QS,\quad S=\operatorname{diag}(I_2,U),\quad
U=\begin{pmatrix}u&1-u\\v&1-v\end{pmatrix},\quad u\ne v,
$$

subject to physical signs and required zeros. U can contain signed entries; restricting it to stochastic matrices would omit candidates. This gives a concrete two-parameter problem. The full diamond is now ruled out as a source of bounded nonuniqueness, while other graphs and other complete-graph fibers remain unclassified here.

**The single next action is to settle that bounded-but-nonunique question using the admissible similarity domain and its boundary stationary fluxes.** An exact positive fiber with certified finite bounds would falsify a proposed unique/unbounded dichotomy. Alternatively, a proof that each entropy-varying fiber reaches a divergent boundary would support a precise classification theorem. Failure of a numerical search would establish neither.

The largest novelty risk is that a sufficiently close specialization is already contained in classical equivalence theory or compatible-model entropy work. The principal correctness risk is silently enlarging the model class or equating algebraic minimality with a different physical minimality convention. Both risks require theorem-level comparison and explicit assumptions; no publication claim is made.

This run closes the initial frontier assessment with substantial exact exploratory results and a discriminating next problem. Further broad searching or N≤6 enumeration is less informative than that targeted calculation and the remaining close-source comparison. The general research objective stays unresolved; [STATE.md](../STATE.md) records the resumption point.
