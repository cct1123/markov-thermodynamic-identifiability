# Revision notes

14 September 2026. This revision makes scientific and repository changes; it is a draft for expert human review, not a submitted or human-approved paper. Start with the [revised manuscript](manuscript/main.pdf), [theorem/assumption audit](analysis/revision/AUDIT.md) and [single reproduction command](reproduce_all.py). The [baseline](outputs/revision/baseline/) preserves the previous article and reports.

## Major scientific changes

The paper now leads with exact generator identification versus entropy identification, exact boundedness, local upper ceilings, continuity, conditioning and finite-sample estimation. The general fixed-count ceiling theorem organizes the article. The constructed five-state fiber follows the three-state, statistical and physical results rather than dominating the abstract and opening.

The original six main theorem statements and all original proof appendices are preserved. A new appendix proves a nontrivial local five-state perturbation result. Four new figures cover conditioning, finite-data performance, realization geometry and continuation; the original two figures remain. The bibliography grows from 15 to 31 cited entries with actual source/version/access comparisons, including 2025 finite-statistics work and a September 2026 adjacent development. [Literature audit](analysis/revision/LITERATURE.md).

## New results

- **Conditioning:** the full six-rate resolvent Jacobian is explicit, including the derivative of the observed-rate matrix. Absolute-rate rank remains full at a three-state tree. At fixed positive entrance rate and reverse rate k tending to zero, the smallest log-rate singular value scales as k and its condition number as 1/k. This is a sensitivity result, not an optimal sample-complexity claim. A 165-triple Laplace design comparison illustrates why noise covariance and the target functional matter as well as singular values.
- **Finite inference:** actual marked CTMC trajectory → empirical joint Laplace moments → constrained six-rate fitting → stationary entropy → martingale-sandwich delta interval. A deterministic 900-trajectory experiment reports every point estimate, missing/boundary interval, bias, variance and coverage. At the interior example, 5,000 records yield 8.8% relative entropy RMSE and 20,000 yield 4.6%. At k=exp(-25), small fitted residuals coexist with severe undercoverage; an explicit heuristic rare-mark warning suppresses suggested intervals. Pointwise asymptotics are not uniform finite-sample guarantees.
- **Exponential testing cost:** for Q(e,k) versus Q(e,k^p), with k=exp(-1/e²) and independently variable reverse rate, sum of test errors at most gamma requires H ≥ (1-gamma)/(k-k^p)-1, even with the full microscopic trajectory. The logarithm of this lower bound divided by the smaller entropy squared tends to 9. The hard alternatives retain trace and the upper rate cap. [Proof and checks](analysis/revision/RARE-EVENT.md).
- **Transverse persistence:** the exit-asymmetry perturbation z±delta has an explicit discriminant polynomial and z*'(0)≈0.4650042. Exact rational signs certify a local geometric rectangle. The unbounded/two-value/singleton entropy transition persists in a sufficiently small neighborhood. A wider 41-node continuation is expressly numerical. [Proof, normal form and diagnostics](analysis/revision/CONTINUATION.md).
- **Observation graph:** if resolved reciprocal edges cover every microscopic vertex, two distinct positive Laplace points identify the full generator with unknown observed rates; one suffices when rates are known. Two fully hidden vertices instead suffice for the existing no-local-ceiling construction under unknown support. Graphs with one uncovered vertex are not completely classified.
- **Regularization:** the published sharp microscopic activity–affinity bound is incorporated. An exact example shows that even a positive rate floor plus bounded activity can leave entropy unbounded. Rate caps, floors, affinity constraints and known support have distinct consequences for entropy regularity and inverse identification.

The new mathematical statements are conventionally proved with exact checks where appropriate. Neither the 900 simulations nor high-precision continuation is presented as formal verification.

## Claims weakened or clarified

No correct original theorem was weakened. Broader interpretations were restricted:

- Three arbitrary **distinct** positive Laplace points give exact recovery, not uniform numerical or statistical conditioning.
- The relation log(1/k)/sigma²→9 does not imply the multiplicative asymptote k~exp(-9 sigma²). A prescribed one-parameter prior tying k to e also excludes the hard testing alternative.
- The five-state transition is a fold of active boundary equations. It is not a saddle-node of two isolated full realizations; a continuum exists below the boundary. The local perturbation does not establish genericity under arbitrary rate/topology changes.
- Exact local geometry is certified for |delta|≤.005 within the stated z rectangle. Distinct critical entropies are proved in a possibly smaller neighborhood by continuity, without claiming an explicit certified radius.
- A finite five-state fiber becomes unbounded with a sixth hidden state. Minimum positive and linear order coincide for this family; they are not interchangeable assumptions in general.
- Network entropy becomes physical dissipation only with appropriate state/channel resolution and local detailed balance. An abstract CTMC does not specify unique physical heat currents.
- Finite timing bins, missed events, detector memory and blurred labels are different observation models. A correctly resolved recorded microscopic jump still resets its endpoint.
- Lower bounds, finite-statistics inference, hidden entropy, positive realization equivalence and general confidence-set impossibility are established antecedents. Literature-wide novelty remains unproved.

## Reproducibility and validation

Use the scientific environment described in [manuscript/README.md](manuscript/README.md):

```text
python -B reproduce_all.py
python -B reproduce_all.py --build --tectonic /path/to/tectonic --offline
```

The workflow replays 15 historical scientific scripts while protecting 22 accepted JSON outputs, checks printed exact interval bounds and the independent manuscript algebra, runs new exact rare-rate/graph/unfolding checks, regenerates conditioning and 900 trajectories, and runs 21 unit/independent checks (9 existing, 7 inference, 5 continuation). The build option compiles and validates the paper. Exact proofs, numerical experiments and historical explorations are clearly separated. The [reproduction manifest](outputs/revision/reproduction.json) records actual commands, timings, versions and results; the [inventory](outputs/revision/repository-audit.json) records scope and preservation checks. Historical mathematical artifacts are not silently overwritten.

## Remaining open questions

The full classification of observation graphs with one uncovered state, arbitrary five/six-state fibers, generic perturbations of all model rates, optimal statistical design and estimation near rare-event boundaries, unknown-dimension inference under useful physical priors, and detector-noise/missed-event likelihoods remain open. Cap-free positive continuity from one fixed stationary window remains distinct from the proved joint-kernel inverse. A quantitative off-balanced entropy-gap interval could strengthen the local perturbation radius. The numerical rate floor is not experimental evidence for such a floor.

Expert review should concentrate on the invariant-triangle support exhaustion, its exact endpoint certificate and the transferred strict margins in the new appendix. Source access gaps in older realization literature remain an attribution risk. Author identities, affiliations, funding, final disclosure and scientific approval still require the human authors; none has been invented.

## Suggested journal positioning

**PRE or JSTAT is the most defensible current target.** This is an assessment of fit, not predicted acceptance. PRE's statistical-physics scope fits the ceiling theorem, concrete CTMC mechanisms and finite-data consequences; its full-article format can accommodate the proof burden. JSTAT is a credible alternative if the authors favor a more mathematical statistical-mechanics presentation. [PRE scope](https://journals.aps.org/pre/about), [JSTAT information](https://publishingsupport.iopscience.iop.org/journals/journal-of-statistical-mechanics-theory-and-experiment/about-journal-statistical-mechanics-theory-experiment/) (checked 14 September 2026).

**PRL would require a separate short paper**, centered on the broad upper-inference obstruction and an especially compelling physical implication. The present detailed proof and numerical package is not a Letter. PRL emphasizes impact, innovation and broad interest and specifies a 3,750-word Letter core; no claim that the present work meets that editorial threshold is made. [PRL author criteria](https://journals.aps.org/prl/authors).

A mathematical/stochastic-process journal is plausible if the positive-realization theorem becomes the primary contribution and the conventional proof is independently vetted. The current paper's strength is the combination of physical interpretation, exact upper-envelope results and honest finite-data diagnostics. Journal choice should follow expert assessment of novelty and proof correctness, not the special threshold alone.
