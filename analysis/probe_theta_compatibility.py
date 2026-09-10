"""Bounded numerical search for a distant complete realization of one kernel.

Run: python analysis/probe_theta_compatibility.py
A failed search proves no global uniqueness or entropy bound.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import warnings

import numpy as np
import scipy
from scipy.optimize import minimize

from check_five_state_extensions import theta


def search_complete(exact_q, rng):
    """Run the same bounded thirteen-start diagnostic for one theta kernel."""
    q = np.array(exact_q, dtype=float)
    outside_diagonal = ~np.eye(5, dtype=bool)

    def transform(z):
        u = np.eye(3)
        k = 0
        for i in range(3):
            for j in range(3):
                if i != j:
                    u[i, j] = z[k]
                    u[i, i] -= z[k]
                    k += 1
        s = np.eye(5)
        s[2:, 2:] = u
        try:
            transformed = np.linalg.solve(s, q @ s)
        except np.linalg.LinAlgError:
            return None, u
        return transformed, u

    def constraints(z):
        transformed, u = transform(z)
        if transformed is None:
            return np.full(21, -1e6)
        # Hidden permutations preserve existence of a complete representative.
        # Coordinate bounds still make this only a bounded search.
        return np.r_[transformed[outside_diagonal]-z[6], np.linalg.det(u)-1e-4]

    starts = [np.zeros(7)]
    for scale in [0.05, 0.25, 0.75]:
        for _ in range(4):
            starts.append(np.r_[rng.uniform(-scale, scale, 6), 0])
    rows = []
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        for start in starts:
            result = minimize(lambda z: -z[6], start, method="SLSQP",
                              bounds=[(-3, 3)]*6+[(0, 2)],
                              constraints={"type": "ineq", "fun": constraints},
                              options={"maxiter": 400, "ftol": 1e-10})
            transformed, u = transform(result.x)
            minimum = float(np.min(transformed[outside_diagonal])) if transformed is not None else None
            rows.append({"success": bool(result.success), "message": str(result.message),
                         "minimum_offdiagonal": minimum,
                         "hidden_determinant": float(np.linalg.det(u)),
                         "parameters": result.x.tolist()})
    return rows, sorted(set(str(w.message) for w in caught))


def main():
    rng = np.random.default_rng(20260910)
    inputs = [("opening_control", theta(9, 10)), ("isolated_target", theta(3, 3))]
    all_results, all_warnings = [], set()
    for name, exact_q in inputs:
        rows, messages = search_complete(exact_q, rng)
        all_warnings.update(messages)
        best = max(rows, key=lambda row: row["minimum_offdiagonal"] if row["minimum_offdiagonal"] is not None else -1e100)
        all_results.append({"case": name, "runs": rows, "best": best})
    paths = [Path(__file__), Path(__file__).with_name("check_five_state_extensions.py"),
             Path(__file__).with_name("check_small_networks.py"),
             Path(__file__).with_name("check_four_state_classification.py")]
    output = {"executed_at": datetime.now(timezone.utc).isoformat(), "seed": 20260910,
              "environment": {"python": platform.python_version(), "numpy": np.__version__,
                              "scipy": scipy.__version__, "platform": platform.platform()},
              "script_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              "parameter_bounds": [-3, 3], "max_iterations_per_start": 400,
              "results": all_results, "warnings": sorted(all_warnings),
              "limitation": "Only a bounded numerical search for complete support; no absence, global uniqueness, or entropy-bound certificate."}
    Path(__file__).with_name("theta-compatibility-probe.json").write_text(
        json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"executed_at": output["executed_at"],
                      "best": [{"case": row["case"], "result": row["best"]} for row in all_results]}, indent=2))


if __name__ == "__main__":
    main()
