# Theoretical research workflow

Tool choice follows the consequential uncertainty. A small hand derivation may settle a four-state calculation; a polynomial counterexample may need elimination; a graph classification may need systematic support enumeration; a stable theorem may justify Lean. The layers in the [stack guide](research-stack.md) are available routes, not mandatory stages.

## From structure to a defensible claim

Use inexpensive numerical exploration to expose structure when that is useful. Compress the phenomenon to its smallest informative example. Formulate a falsification condition, search deliberately for it, and preserve failures that constrain the theory. Exactify promising patterns with rational/algebraic reconstruction, polynomial identities, limits or a conventional argument. Seek a mechanism, invariant or structural condition rather than an unexplained fit. Increase size only to test a stated scientific question. Check adjacent mathematical literatures before claiming novelty.

Choose an independent verification route for a surprising or publication-critical result when practical: float to high precision from original inputs; a different optimizer/formulation/initialization; symbolic algebra to independent numerical spot checks; alternative derivation; independent graph generation/count; theorem candidate to targeted falsification; conventional proof to formalization if worthwhile. Two agents using the same script/source are not independent confirmation. Record disagreement, shared dependencies and untested alternatives.

## Falsification before promotion

For a consequential conjecture, state assumptions, quantifiers, admissible topology/dimension/rate class and a computational rejection condition before attempting proof, or explain why computation cannot usefully test it. Separate a numerical candidate from a verified counterexample. For an identifiability claim, the target is equal observable data with different entropy. Approximate kernel agreement on a time grid is only a lead; the final witness needs exact all-time data equality under the stated admissible class (see the existing [formulation](../analysis/formulation.md)). For unboundedness, bounded optimization cannot establish divergence: construct an admissible parameter family preserving the data and prove its entropy limit.

In a search, expose feasibility residual and objective gap separately; optimizer success is not feasibility. Vary bounds, seeds, tolerances and parameterizations when they bear on the result. Include support-changing boundaries, near-zero rates, repeated poles/eigenvalues, singular realizations and disconnected components of the compatible set where relevant. Positive-rate parametrization excludes boundary strata, so test those separately. After a candidate is found, refine at higher precision, reconstruct rational/algebraic inputs if plausible and check the original constraints exactly. Reconstruction changes the candidate, so revalidate everything.

The [toy adversarial script](../analysis/capabilities/counterexample_demo.py) demonstrates log-uniform random search, differential evolution, an independently constrained SLSQP formulation, rational reconstruction and high-precision/exact checking. Adapt its falsification condition to the question rather than treating its objective as a generic research solver.

**Failure to find a counterexample is not a proof.** A finite search box does not imply global boundedness; a complete topology list does not exhaust continuous parameters; a time sample does not establish transfer-function equality; an elimination polynomial does not guarantee an admissible real lift. Preserve unsuccessful/inconclusive attempts separately from evidence against the claim.

## Claim status and promotion

Keep important mathematical claims in the existing `evidence/RECORDS.md` entry or linked proof note, using stable evidence anchors. The provenance labels already in AGENTS.md describe the contribution's origin; the following **mathematical status** describes its verification. Do not retroactively relabel existing results merely because tools were installed.

| Status | Minimum meaning |
| --- | --- |
| observation | Directly inspected instance/data, with method and input |
| numerical pattern | Repeated approximate behavior; scope, tolerances and exceptions explicit |
| conjecture | Precise proposed statement with assumptions and a falsification target |
| counterexample | Admissible witness contradicting a stated claim; distinguish numerical candidate from exactly checked witness |
| proposition / theorem candidate | A precise assertion and proposed argument; these names alone confer no proof status |
| conventionally proved | A complete domain-aware mathematical argument, with reviewer/independent checks and limitations recorded |
| solver-certified | Definitive result for an audited encoding, trusting a named solver/version; stronger certificate-checking status only if a checker ran |
| formally verified | Actual Lean check succeeded for the stated theorem and accepted axioms in the pinned environment |
| falsified | A verified counterexample or valid contradiction defeats the statement under its own assumptions; retain the old statement and link the correction |

Use this compact block for a consequential claim; omit irrelevant fields rather than creating a second tracking system:

```text
Contribution label: inference / reproduced calculation / primary result / ...
Mathematical status: conjecture [explicit verification scope]
Statement and quantifiers:
Assumptions/domain/admissible class (including denominators and boundary strata):
Evidence and literature: stable E/D links and precise sources
Falsification condition and attempts: script, scope, seed/budget, output, outcome
Proof/check: argument or exact identity; solver encoding or Lean theorem if present
Independent route: method, result, shared dependencies, disagreements
Unresolved weaknesses and condition for promotion/reconsideration:
```

A numerical pattern never silently becomes a theorem. A symbolic identity is an exact result only on its justified domain; it does not prove an entire classification. A solver answer certifies its encoding under the engine's trust assumptions. Arbitrary precision remains numerical evidence without an error certificate. A proof sketch written by an LLM is not formally verified.

Normally promote a claim into formalization only when it is consequential, precise, supported by reproducible calculations or conventional proof, seriously challenged by counterexample search, and stable enough to justify the effort. Formal status requires successful build, statement review and axiom audit; see [formal/README.md](../formal/README.md). Proof status does not establish novelty.

## Numerical rigor checklist when relevant

Use row generators (`Q 1 = 0`, `pi Q = 0`, `sum(pi)=1`) consistently. Record time units, natural logs and the entropy convention. Check nonnegative off-diagonals, structural zero support, irreducibility and stationary uniqueness explicitly: a reducible chain can have a strictly positive stationary law. Do not add epsilons to reverse rates or clip small positive/negative rates to manufacture a valid model.

Rescale time for extreme rate magnitudes; inspect residuals and condition estimates, and distinguish forward error from residual error. Near-singular systems can have small residuals and inaccurate answers. Check probability normalization/positivity, flux conservation, logarithm domains and underflow/overflow. A missing reverse flux can yield infinite entropy; an absent pair contributes zero. Subtracting nearly equal fluxes or eigenvalues can lose significant digits. Repeated eigenvalues/poles require rank/multiplicity analysis instead of naïve root matching. Near-zero support and roundoff zeros are different.

For apparent equalities, zeros, invariants, divergences or sign changes, vary tolerance and recompute at increasing precision from exact/decimal source inputs, then seek exact algebra or rigorous bounds where the claim requires them. Inspect one-sided limits and joint limit order. Symbolic simplification must retain parameter assumptions, branch choices, poles and singular strata. Multiplying rational inequalities by a denominator requires its sign. Gröbner elimination over complex closures cannot itself decide positive real feasibility. See [exact constraints](optional-tools.md#exact-constraints-a-usable-path-and-its-limits).

## Infrastructure runs

Keep capability audits and smoke outputs under `docs/` and `analysis/capabilities/`; they are not scientific discoveries and receive no scientific evidence IDs. Preserve PROJECT.md, accepted research outputs and the research report. Change STATE.md only when a capability issue materially changes the next research action. An infrastructure run does not reopen a finished investigation or authorize the next scientific experiment.
