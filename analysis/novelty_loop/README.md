# Coverage theorem research cycle

The 19 September 2026 cycle starts at `c7ff789` and is scoped by the user's request for an independent mathematical review, a substantial novelty plan, and actual execution of the research loop. The original brief, earlier scientific outputs and compiled manuscript are preserved.

The [theorem and full proofs](../../outputs/novelty-loop-2026-09-19/COVERAGE-THEOREM.md), [independent review](../../outputs/novelty-loop-2026-09-19/REFEREE.md), [independent inverse/falsification note](../../outputs/novelty-loop-2026-09-19/ONE-HIDDEN-INDEPENDENT.md), and [primary-source comparison](../../outputs/novelty-loop-2026-09-19/LITERATURE.md) distinguish universal proof, finite exact checks, numerical illustrations and originality assessment.

Run from the repository root, with Python assertions enabled:

```text
.venv/Scripts/python.exe -B analysis/novelty_loop/one_hidden_independent.py
.venv/Scripts/python.exe -B outputs/novelty-loop-2026-09-19/referee_checks.py
.venv/Scripts/python.exe -B analysis/novelty_loop/coverage_crosscheck.py
```

Dependencies: Python 3.9.12, SymPy 1.14.0, mpmath 1.3.0 (the last for 100-digit sparse-sequence entropy diagnostics). These are already pinned in the repository's research environment. All inputs and observation masks are embedded exact constructions. There is no random seed, optimizer, approximate equality test or downloaded dataset. The scripts retain source SHA-256 and runtime versions and reject `-O` or `PYTHONOPTIMIZE` before doing work. Regression command: `python -B -m unittest analysis.correctness.test_entrypoints -v`.

- `one_hidden_independent.py`: twelve exact sparse/complete reconstruction cases at N=4,5,6; full-mark finite-summary entropy witnesses and calibrated variant; exact stationary solutions plus numerical entropy along a rational sparse sequence; a killed-generator split intertwining.
- `referee_checks.py`: an independently coded selected-column inverse, equal-exit lumping and an unequal-exit shear that reaches its internal boundary first.
- `coverage_crosscheck.py`: direct symbolic resolvent plus a rectangular lumping identity for the reversible complete four-state source, a generic two-sample entropy ambiguity, and exhaustive nonempty observation-pair sets at N=2,...,6. The finite enumeration checks the universal matching argument; it does not prove a theorem about all rates or dimensions.

The shared CTMC observation model and SymPy engine limit independence. The conventional proofs supply quantifiers and limiting arguments; no successful calculation is labeled formal verification. Accepted historical scripts/data and the 900-trajectory statistical campaign are not rerun by this bounded cycle. The new result is a research addendum; the older manuscript and reproduction archive retain their earlier scientific version until editorial integration.
