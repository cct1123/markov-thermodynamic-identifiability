"""One targeted global probe beyond the analytic residue-construction region.

Run from the repository root: python -B analysis/probe_theta_fast_case.py
This is a discovery diagnostic, never an infeasibility certificate.
"""
from datetime import datetime, timezone
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import platform

import numpy as np
import scipy
from scipy.optimize import linprog
from check_five_state_extensions import theta, tangent
from check_small_networks import exact_rank
from probe_theta_compatibility import search_complete


def main():
    exact_q = theta(100, 100)
    _, _, exact_a = tangent(exact_q)
    # Exact certificate chosen from the two-dimensional left null space.
    dual = np.array([F(3), F(1), F(1), F(53200, 109371), F(7, 3),
                     F(133900, 109371), F(1983, 36457), F(4577, 36457)], dtype=object)
    assert all(v > 0 for v in dual)
    assert all(v == 0 for v in dual @ exact_a)
    assert exact_rank(exact_a) == 6
    a = np.asarray(exact_a, dtype=float)
    local = linprog(np.zeros(6), A_ub=-a, b_ub=-np.ones(len(a)),
                    bounds=[(None, None)]*6, method="highs")
    results, messages = search_complete(exact_q, np.random.default_rng(20260911))
    paths = [Path(__file__), Path(__file__).with_name("check_five_state_extensions.py"),
             Path(__file__).with_name("check_small_networks.py"),
             Path(__file__).with_name("check_four_state_classification.py"),
             Path(__file__).with_name("probe_theta_compatibility.py")]
    output = {"executed_at": datetime.now(timezone.utc).isoformat(),
              "input": {"a": 100, "b": 100}, "seed": 20260911,
              "environment": {"python": platform.python_version(), "numpy": np.__version__,
                              "scipy": scipy.__version__},
              "script_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              "local_lp": {"success": bool(local.success), "status": int(local.status),
                           "message": str(local.message)},
              "exact_local_isolation": {"tangent_rank": 6,
                                        "positive_left_null_vector": [str(v) for v in dual],
                                        "annihilation_verified": True,
                                        "exit_chart_determinant": -882},
              "search_bounds": [-3, 3], "determinant_floor": 1e-4,
              "max_iterations": 400, "results": results,
              "warnings": messages,
              "limitation": "Bounded numerical probe; failure does not prove global impossibility, uniqueness or bounded entropy."}
    Path(__file__).with_name("theta-fast-probe.json").write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    best = max(results, key=lambda r: r["minimum_offdiagonal"] if r["minimum_offdiagonal"] is not None else -1e100)
    print(json.dumps({"executed_at": output["executed_at"], "local_lp": output["local_lp"],
                      "best": best, "warnings": output["warnings"]}, indent=2))


if __name__ == "__main__":
    main()
