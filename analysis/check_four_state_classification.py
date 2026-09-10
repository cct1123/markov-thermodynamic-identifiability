"""Exact witnesses and falsification checks for the four-state classification.

Run: python analysis/check_four_state_classification.py
All rates and paths are deterministic rational inputs. No graph enumeration.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import expm

from check_small_networks import (
    check_generator, derivatives, entropy, equal_escape_diamond,
    exact_rank, eye, marked_system, matrix,
)


def stationary(q):
    """Solve stationarity and normalization by exact Gauss-Jordan elimination."""
    n = len(q)
    a = q.T.copy()
    a[-1, :] = F(1)
    rhs = matrix([[0] for _ in range(n)])
    rhs[-1, 0] = F(1)
    a = np.concatenate([a, rhs], axis=1)
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i, col])
        a[[col, pivot]] = a[[pivot, col]]
        a[col] = a[col] / a[col, col]
        for row in range(n):
            if row != col:
                a[row] = a[row] - a[row, col] * a[col]
    return a[:, -1]


def similarity(u, v):
    delta = u-v
    assert delta
    s, inverse = eye(4), eye(4)
    s[2:, 2:] = matrix([[u, 1-u], [v, 1-v]])
    inverse[2:, 2:] = matrix([[1-v, u-1], [-v, u]]) / delta
    assert np.array_equal(s @ inverse, eye(4))
    return s, inverse


def transform(q, u, v):
    s, inverse = similarity(u, v)
    return inverse @ q @ s, s


def ranks(q):
    r, t, b = marked_system(q)
    power = eye(4)
    controllability, observability = [], []
    for _ in range(4):
        controllability.append(power @ b)
        observability.append(r @ power)
        power = power @ t
    return (exact_rank(np.concatenate(controllability, axis=1)),
            exact_rank(np.concatenate(observability, axis=0)))


def strongly_connected(q):
    for source in range(4):
        seen, todo = {source}, [source]
        while todo:
            i = todo.pop()
            for j in range(4):
                if i != j and q[i, j] > 0 and j not in seen:
                    seen.add(j)
                    todo.append(j)
        if len(seen) != 4:
            return False
    return True


def physical(q):
    for i in range(4):
        if sum(q[i]) != 0:
            return False
        for j in range(i+1, 4):
            if q[i, j] < 0 or q[j, i] < 0:
                return False
            if (q[i, j] > 0) != (q[j, i] > 0):
                return False
    return strongly_connected(q)


def support(q):
    return [(i, j) for i in range(4) for j in range(i+1, 4)
            if q[i, j] > 0 and q[j, i] > 0]


def same_kernel(q, reference):
    assert all(np.array_equal(a, b) for a, b in
               zip(derivatives(q, 8), derivatives(reference, 8)))


def boundary_witness(name, base, endpoint, direction, disappearing):
    assert ranks(base) == (4, 4)
    pi = stationary(base)
    check_generator(base, pi)
    alpha, beta = direction
    limit, limit_s = transform(base, 1+alpha*endpoint, beta*endpoint)
    limit_pi = pi @ limit_s
    assert strongly_connected(limit)
    assert all(p > 0 for p in limit_pi)
    assert all(sum(row) == 0 for row in limit)
    assert all(limit[i, j] >= 0 for i in range(4) for j in range(4) if i != j)
    i, j = disappearing
    assert limit[i, j] == 0 and limit[j, i] > 0
    coefficient = limit_pi[j]*limit[j, i]
    r0, t0, b0 = (np.asarray(a, float) for a in marked_system(base))
    times = [0.0, 1e-6, 0.01, 0.1, 1.0, 10.0]
    reference = [r0 @ expm(t0*time) @ b0 for time in times]
    rows = []
    for gap in [F(1, 1000), F(1, 10**6), F(1, 10**9)]:
        e = endpoint-gap
        q, s = transform(base, 1+alpha*e, beta*e)
        candidate_pi = pi @ s
        assert physical(q)
        check_generator(q, candidate_pi)
        assert ranks(q) == (4, 4)
        assert sum(q.diagonal()) == sum(base.diagonal())
        same_kernel(q, base)
        r, t, b = (np.asarray(a, float) for a in marked_system(q))
        residual = max(float(np.max(np.abs(r @ expm(t*time) @ b-expected)))
                       for time, expected in zip(times, reference))
        assert residual < 1e-12
        sigma = entropy(q, candidate_pi)
        rows.append({"gap": str(gap), "entropy": sigma,
                     "entropy_minus_leading_log": sigma-float(coefficient)*math.log(1/float(gap)),
                     "kernel_residual": residual,
                     "vanishing_rate": str(q[i, j])})
    measured = (rows[-1]["entropy"]-rows[-2]["entropy"])/math.log(1000)
    assert math.isclose(measured, float(coefficient), rel_tol=2e-4, abs_tol=1e-7)
    return {"name": name, "base_generator": [[str(v) for v in row] for row in base],
            "base_support": support(base), "interior_support": support(q),
            "direction": list(direction), "endpoint": str(endpoint),
            "disappearing_edge": list(disappearing),
            "boundary_stationary": [str(p) for p in limit_pi],
            "log_divergence_coefficient": str(coefficient),
            "measured_log_coefficient": measured, "samples": rows}


def main():
    # A hidden triangle attached to the observed pendant edge: an exit vanishes.
    pendant_triangle = matrix([[-1, 1, 0, 0], [1, -8, 2, 5],
                               [0, 3, -7, 4], [0, 7, 6, -13]])
    # A complete graph where a hidden-hidden edge reaches zero first.
    hidden_edge_first = matrix([[-6, 1, 2, 3], [1, -10, 4, 5],
                                [1, F(13, 2), F(-17, 2), 1], [2, 1, 2, -5]])
    # The same sparse support changes global classification with escape order.
    ordered_slow_h = matrix([[-3, 1, 2, 0], [1, -9, 3, 5],
                             [1, 1, -2, 0], [0, 4, 0, -4]])
    ordered_fast_h = ordered_slow_h.copy()
    ordered_fast_h[3, 1], ordered_fast_h[3, 3] = F(1), F(-1)
    witnesses = [
        boundary_witness("pendant_triangle_exit", pendant_triangle, F(3, 7), (-1, 0), (2, 1)),
        boundary_witness("complete_hidden_edge", hidden_edge_first, F(1, 4), (-1, 0), (2, 3)),
        boundary_witness("unknown_topology_opening", ordered_slow_h, F(1, 3), (-1, -1), (2, 1)),
    ]

    # Named support-opening cases: each sparse model has a dense compatible one.
    same_neighbor = matrix([[-3, 1, 2, 0], [1, -4, 3, 0],
                             [1, 2, -7, 4], [0, 0, 5, -5]])
    one_port_chain = matrix([[-1, 1, 0, 0], [1, -3, 2, 0],
                             [0, 3, -7, 4], [0, 0, 5, -5]])
    full_diamond = matrix([[-4, 1, 2, 1], [1, -4, 1, 2],
                           [3, 1, -4, 0], [1, 2, 0, -3]])
    one_port_tree = matrix([[-1, 1, 0, 0], [1, -6, 2, 3],
                            [0, 4, -4, 0], [0, 2, 0, -2]])
    equal_escape_sparse = ordered_slow_h.copy()
    equal_escape_sparse[3, 1], equal_escape_sparse[3, 3] = F(2), F(-2)
    openings = []
    for name, base, alpha, beta in [
        ("same_hidden_neighbor", same_neighbor, -1, -1),
        ("one_port_chain", one_port_chain, -1, -1),
        ("full_diamond_distinct", full_diamond, 1, 1),
        ("one_port_tree", one_port_tree, 1, 1),
        ("sparse_equal_escapes", equal_escape_sparse, -1, -1),
    ]:
        q, _ = transform(base, 1+F(alpha, 100), F(beta, 100))
        assert ranks(base) == ranks(q) == (4, 4)
        assert physical(base) and physical(q)
        same_kernel(q, base)
        assert len(support(q)) > len(support(base))
        openings.append({"name": name, "base_support": support(base),
                         "compatible_support": support(q)})

    # Falsify an overbroad rule that every minimal four-state model is ambiguous.
    opposite_neighbors = matrix([[-3, 1, 2, 0], [1, -4, 0, 3],
                                  [4, 0, -5, 1], [0, 5, 2, -7]])
    grid_checks = []
    grid = [F(i, 4) for i in range(-8, 13)]
    for name, base in [("opposite_singletons", opposite_neighbors),
                       ("singleton_faster_escape", ordered_fast_h)]:
        assert physical(base) and ranks(base) == (4, 4)
        admissible = []
        for u in grid:
            for v in grid:
                if u == v:
                    continue
                q, _ = transform(base, u, v)
                if physical(q):
                    admissible.append((str(u), str(v)))
                    same_kernel(q, base)
        assert set(admissible) == {("1", "0"), ("0", "1")}
        grid_checks.append({"name": name, "admissible_grid_points": admissible,
                            "limitation": "Finite falsification check; uniqueness uses the analytic sign proof."})

    # Equal hidden exit rows violate the minimality needed by the new theorem.
    nonminimal = matrix([[-4, 1, 2, 1], [1, -4, 1, 2],
                         [1, 2, -7, 4], [1, 2, 5, -8]])
    assert physical(nonminimal)
    nonminimal_ranks = ranks(nonminimal)
    assert nonminimal_ranks[0] < 4
    assert ranks(equal_escape_diamond(F(0))) == (4, 4)

    result = {
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__, "platform": platform.platform()},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "helper_sha256": hashlib.sha256(Path(__file__).with_name("check_small_networks.py").read_bytes()).hexdigest(),
        "inputs": "Named exact rational matrices and similarities embedded in this script; no randomness.",
        "all_time_certificate_derivative_orders": [0, 7],
        "boundary_witnesses": witnesses, "support_openings": openings,
        "global_uniqueness_grid_checks": grid_checks,
        "nonminimal_equal_exit_row_ranks": list(nonminimal_ranks),
        "limitation": "Representative exact and numerical checks; theorem coverage comes from the proofs, not sampling. Novelty unestablished.",
    }
    Path(__file__).with_name("four-state-classification-checks.json").write_text(
        json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"executed_at": result["executed_at"],
                      "boundary_witnesses": len(witnesses), "support_openings": len(openings),
                      "unique_grid_models": len(grid_checks),
                      "maximum_kernel_residual": max(row["kernel_residual"] for w in witnesses for row in w["samples"]),
                      "nonminimal_ranks": nonminimal_ranks}, indent=2))


if __name__ == "__main__":
    main()
