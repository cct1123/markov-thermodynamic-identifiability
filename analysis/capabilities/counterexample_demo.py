"""Editable adversarial-search example, unrelated to the scientific objective.

Toy false conjecture: x*y <= 1/8 for positive x,y with x+y=1.
Numerical falsification: equality residual <= 1e-10, positivity and violation
> 1e-6. Then independently check a reconstructed rational candidate exactly.
Failure to find a counterexample is not a proof.
Run from root: python -m analysis.capabilities.counterexample_demo
"""

import argparse
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.optimize import differential_evolution, minimize

from analysis.research_tools.provenance import write_manifest


def run(seed=20260910):
    rng = np.random.default_rng(seed)
    # Log-uniform positive sampling, then enforce the equality by construction.
    rates = np.exp(rng.uniform(np.log(1e-6), np.log(1e6), size=(128, 2)))
    samples = rates / rates.sum(axis=1, keepdims=True)
    best = samples[np.argmax(np.prod(samples, axis=1))]
    # Eliminate y for a global heuristic; this parametrization has a stated domain.
    de = differential_evolution(lambda z: -(z[0] * (1-z[0]) - 1/8),
                                [(1e-6, 1-1e-6)], seed=rng, maxiter=80,
                                popsize=12, tol=1e-10, polish=False, workers=1)
    # Independent formulation: two variables and an explicit equality constraint.
    local = minimize(lambda z: -z[0]*z[1], best, method="SLSQP",
                     bounds=[(1e-6, 1-1e-6)]*2,
                     constraints={"type": "eq", "fun": lambda z: z.sum()-1},
                     options={"ftol": 1e-12, "maxiter": 100})
    candidates = [("log_uniform", best, None, "128 samples"),
                  ("differential_evolution", np.array([de.x[0], 1-de.x[0]]), bool(de.success), str(de.message)),
                  ("SLSQP", local.x, bool(local.success), str(local.message))]
    rows = []
    for method, z, success, message in candidates:
        residual, violation = abs(float(z.sum()-1)), float(np.prod(z)-1/8)
        rows.append({"method": method, "parameters": z.tolist(), "success": success,
                     "message": message, "equality_residual": residual, "violation": violation,
                     "numerical_candidate": bool(np.all(z > 0) and residual <= 1e-10 and violation > 1e-6)})
    # limit_denominator proposes a nearby input; this is NOT a proof about floats.
    x = Fraction(str(local.x[0])).limit_denominator(1000)
    y = 1-x
    exact_violation = x*y-Fraction(1, 8)
    exact_pass = x > 0 and y > 0 and x+y == 1 and exact_violation > 0
    ctx = mp.mp.clone()
    ctx.dps = 80
    mx, my = ctx.mpf(x.numerator)/x.denominator, ctx.mpf(y.numerator)/y.denominator
    checked = mx*my-ctx.mpf(1)/8
    if not exact_pass or checked <= 0 or not all(row["numerical_candidate"] for row in rows):
        raise AssertionError("toy falsification capability failed")
    return {"claim": "x*y <= 1/8 for x>0,y>0,x+y=1 (deliberately false toy)",
            "searches": rows, "rational_candidate": [str(x), str(y)],
            "exact_violation": str(exact_violation), "high_precision_violation": str(checked),
            "status": "exact toy counterexample checked; no project claim",
            "limitation": "Search and optimizer success do not certify absence, exact equality or global optima."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="analysis/capabilities/results/counterexample.json")
    args = parser.parse_args()
    results = run()
    write_manifest(args.output, sources=[Path(__file__), "analysis/research_tools/provenance.py",
                   "analysis/requirements-research.txt", "analysis/requirements.txt"],
                   settings={"command": "python -m analysis.capabilities.counterexample_demo",
                             "seed": 20260910, "dps": 80, "samples": 128,
                             "raw_rate_bounds": [1e-6, 1e6], "equality_tolerance": 1e-10,
                             "violation_threshold": 1e-6, "rational_max_denominator": 1000,
                             "DE": {"maxiter": 80, "popsize": 12, "tol": 1e-10, "polish": False, "workers": 1},
                             "SLSQP": {"maxiter": 100, "ftol": 1e-12}},
                   results=results, kind="capability-test")
    print(results["status"])


if __name__ == "__main__":
    main()
