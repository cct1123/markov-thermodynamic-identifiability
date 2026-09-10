# Positive realization frontier for the theta family

Inspected 2026-09-10 UTC. Bounded primary-source follow-up under D007, targeting complete three-hidden-state realizations at fixed minimal order. Earlier scalar PH and marked-realization sources remain in [realization-frontier.md](realization-frontier.md); the isolated/distant example is already proved in [theta-global-audit.md](../analysis/theta-global-audit.md). No source files were saved locally and no additional numerical search was run.

**Outcome — inference.** The retrieved continuous-time primary theorem supplies exact invariant-cone machinery. It does not prove the required cone can have exactly three independent rays or satisfy strict inequalities. A task-specific deduction removes two distractions: a single trace-based uniformization shift covers the entire minimal theta fiber, and stochastic normalization is automatic once a strict order-three matrix realization exists. The remaining question is therefore an exact strict simplicial-cone feasibility problem. Details and limits are in [positive-realization-obstructions.md](../analysis/positive-realization-obstructions.md).

## Primary theorem actually read

J. M. van den Hof, *Realization of continuous-time positive linear systems*, Systems & Control Letters 31, 243–253 (1997); received 7 December 1995, revised 2 July 1996; [DOI](https://doi.org/10.1016/S0167-6911(97)00049-2), [full CWI journal PDF](https://ir.cwi.nl/pub/127/0127D.pdf). Definitions, proofs and examples in sections 2–4 were inspected.

**Primary result.** Definition 3.1 and Theorem 3.1, pp. 246–247, characterize existence of a continuous-time positive realization using a shift that makes every Markov parameter nonnegative, together with a backward-shift-invariant polyhedral cone containing the shifted Hankel columns. “Positive” here includes zeros. Theorem 4.2, pp. 247–248, relates minimum positive continuous-time order to minimum positive discrete-time order for every admissible shift. Example 4.1, pp. 248–249, shows why one arbitrary shift is insufficient in general. The construction permits the state count required by a cone's generators; it does not give a strict order-three guarantee.

**Scope.** This is a matrix-valued input/output theorem, relevant to the shared kernel. Neither spectral dominance alone nor separate scalar realization of each entry replaces its cone condition. The fixed-trace specialization in the linked analytic note is an agent deduction, not attributed to the paper.

## Closest strict-positivity source: exact hypotheses remain inaccessible

K.-H. Förster and B. Nagy, *Nonnegative realizations of matrix transfer functions*, Linear Algebra and its Applications 311(1–3), 107–129 (15 May 2000); [DOI](https://doi.org/10.1016/S0024-3795(00)00076-8), [publisher record](https://www.sciencedirect.com/science/article/pii/S0024379500000768).

**Abstract-only primary claim.** The abstract explicitly treats finite-dimensional discrete-time matrix transfer functions and conditions for realizations whose main matrix is irreducible, strictly positive, or primitive. It does not state the exact conditions or promise dimension equal to the McMillan degree. It also does not clarify in the abstract whether input/output matrices can both be strictly positive.

The [author bibliography](https://math.bme.hu/~bnagy/publ2011.html), entry 62, confirms the publication but supplied no full-text link. Publisher HTML opening and both PDF routes failed. This was a new targeted route, not a repetition of the Larget access attempts. The precise theorem, proof, and dimension restrictions remain an explicit gap.

L. Benvenuti and L. Farina's *A Tutorial on the Positive Realization Problem*, [full author-hosted preprint](https://sites.math.rutgers.edu/~sussmann/papers/res-farina-tutorial-positive-realization.pdf), introduction p. 1 and reference [103], supplied this citation path. Its statement about the strict/primitive extension is secondary and is not substituted for the inaccessible theorem.

## Dimension caution checked against another primary construction

Máté Matolcsi and Béla Nagy, *Estimates for the dimensions of nonnegative realizations*, Acta Scientiarum Mathematicarum (Szeged) 70, 511–524 (2004); received 11 November 2003, revised 10 June 2004; [full journal PDF](https://www.acta.hu/download.phtml?id=2798).

**Primary result.** Theorem 2.2, p. 515, constructs a finite nonnegative realization and an explicit dimension upper bound for a scalar primitive transfer function with simple dominant pole, nonnegative impulse response, and the stated normalization. The bound depends on additional spectral and coordinate quantities and is not simply the McMillan degree. The introductory cone definitions, pp. 512–513, distinguish realization order from the number of generators of a cone in a chosen realization.

**Inference.** A scalar dominance/existence theorem, even one with an explicit finite bound, does not resolve the shared matrix kernel at precisely three hidden states. This source was checked to prevent that inference, rather than as a proposed solution of the theta problem.

## Consequential remaining test

At minimal points off `a+b=9−2√6`, the theta transfer passes the elementary positive-pole, positive-Markov-parameter and simple positive-Perron-residue tests. A three-ray cone satisfying all strict inequalities still has to be constructed or excluded. At the repeated dominant line, Perron theory excludes a similar irreducible hidden block, but does not bound entropy on other supports; nonminimal exceptions require separate treatment. The current source evidence does not settle this remaining feasibility problem or establish novelty of a prospective classification.
