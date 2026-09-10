"""Targeted exact checks: path reconstruction and genuinely three-state mixing.

Run: python analysis/check_five_state_extensions.py
No graph enumeration. LP proposes directions; exact arithmetic certifies them.
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
from scipy.optimize import linprog

from check_small_networks import (check_generator, derivatives, entropy, exact_rank, eye,
                                  marked_system, matrix)
from check_four_state_classification import stationary


def inverse(a):
    n = len(a)
    work = np.concatenate([a.copy(), eye(n)], axis=1)
    for col in range(n):
        pivot = next(i for i in range(col, n) if work[i, col])
        work[[col, pivot]] = work[[pivot, col]]
        work[col] = work[col]/work[col, col]
        for i in range(n):
            if i != col:
                work[i] = work[i]-work[i, col]*work[col]
    return work[:, n:]


def ranks(q):
    r, t, b = marked_system(q)
    power = eye(len(q))
    con, obs = [], []
    for _ in range(len(q)):
        con.append(power @ b)
        obs.append(r @ power)
        power = power @ t
    return exact_rank(np.hstack(con)), exact_rank(np.vstack(obs))


def normalize(q):
    q = q.copy()
    for i in range(len(q)):
        q[i, i] = -sum(q[i, j] for j in range(len(q)) if i != j)
    return q


def theta(exit_x, exit_y):
    return normalize(matrix([[0, 1, 2, 0, 8], [2, 0, 0, 7, 11],
                             [3, 0, 0, 4, 0], [0, 6, 5, 0, 0],
                             [exit_x, exit_y, 0, 0, 0]]))


def tangent(q):
    missing = [(i, j) for i in range(5) for j in range(5)
               if i != j and q[i, j] == 0]
    bases, velocities = [], []
    for i in range(2, 5):
        for j in range(2, 5):
            if i != j:
                k = matrix(np.zeros((5, 5), dtype=int))
                k[i, j], k[i, i] = F(1), F(-1)
                bases.append(k)
                velocities.append(q @ k-k @ q)
    a = matrix([[v[i, j] for v in velocities] for i, j in missing])
    return missing, bases, a


def scalar_peel(moments):
    """Peel a tridiagonal endpoint resolvent using exact Laurent coefficients."""
    diagonal, products = [], []
    while moments:
        assert moments[0] == 1 and len(moments) >= 2
        diagonal.append(moments[1])
        if len(moments) == 2:
            break
        reciprocal = [F(1)]
        for k in range(1, len(moments)):
            reciprocal.append(-sum(moments[j]*reciprocal[k-j] for j in range(1, k+1)))
        product = -reciprocal[2]
        assert product > 0
        products.append(product)
        moments = [-v/product for v in reciprocal[2:]]
    return diagonal, products


def cycle_check(n):
    assert n >= 4  # The chord negative control needs a non-observed chord.
    path = [0]+list(range(2, n))+[1]
    q = matrix(np.zeros((n, n), dtype=int))
    q[0, 1], q[1, 0] = F(23), F(29)
    for i, (u, v) in enumerate(zip(path, path[1:])):
        q[u, v], q[v, u] = F(2*i+2), F(3*i+11)
    q = normalize(q)
    check_generator(q, stationary(q))
    joint = derivatives(q, 2*n)
    r, s = joint[0][1, 0], joint[0][0, 1]
    cross = [value[1, 1]/s for value in joint]
    assert next(i for i, value in enumerate(cross) if value != 0) == n-1
    moments = [value[1, 0]/r for value in joint]
    diagonal, products = scalar_peel(moments)
    recovered = matrix(np.zeros((n, n), dtype=int))
    recovered[0, 1], recovered[1, 0] = r, s
    backward = r
    for i, (u, v) in enumerate(zip(path, path[1:])):
        forward = -diagonal[i]-backward
        assert forward > 0
        backward = products[i]/forward
        recovered[u, v], recovered[v, u] = forward, backward
    assert -diagonal[-1] == backward+s
    recovered = normalize(recovered)
    assert np.array_equal(q, recovered)
    assert ranks(q) == (n, n)
    assert all(np.array_equal(v, w) for v, w in zip(joint, derivatives(recovered, 2*n)))
    # A new bidirected chord must shorten the observable first-passage route.
    chord = q.copy()
    chord[path[0], path[2]] += F(1)
    chord[path[2], path[0]] += F(1)
    chord = normalize(chord)
    cross_chord = [value[1, 1]/s for value in derivatives(chord, 2*n)]
    assert next(i for i, value in enumerate(cross_chord) if value != 0) == n-2
    return {"states": n, "generator": strings(q), "first_cross_derivative": n-1,
            "reconstruction_max_derivative": 2*n-1, "ranks": ranks(q),
            "chord_first_derivative": n-2}


def strings(a):
    return [[str(v) for v in row] for row in a]


def main():
    open_source = theta(9, 10)
    missing, bases, a = tangent(open_source)
    # Rounded rational direction from the LP diagnostic; certify it exactly.
    coefficients = [F(-1), F(581, 1000), F(958, 1000),
                    F(-340, 1000), F(-593, 1000), F(273, 1000)]
    velocity = a @ np.array(coefficients, dtype=object)
    assert all(value > 0 for value in velocity)
    perturbation = sum((c*b for c, b in zip(coefficients, bases)),
                       matrix(np.zeros((5, 5), dtype=int)))
    similarity = eye(5)+perturbation/F(1000)
    transformed = inverse(similarity) @ open_source @ similarity
    pi = stationary(open_source) @ similarity
    check_generator(transformed, pi, complete=True)
    assert ranks(open_source) == ranks(transformed) == (5, 5)
    assert all(np.array_equal(v, w) for v, w in
               zip(derivatives(open_source, 10), derivatives(transformed, 10)))
    # Every pair-only neighborhood is incomparable in the original graph.
    for h in range(2, 5):
        for k in range(h+1, 5):
            external = set(range(5))-{h, k}
            nh = {v for v in external if open_source[h, v] > 0}
            nk = {v for v in external if open_source[k, v] > 0}
            assert nh-nk and nk-nh

    isolated = theta(3, 3)
    missing2, _, a2 = tangent(isolated)
    assert missing == missing2 and exact_rank(a2) == 6
    dual = np.array([F(3), F(1), F(1), F(10, 3), F(7, 3),
                     F(19, 15), F(151, 15), F(79, 15)], dtype=object)
    assert all(v > 0 for v in dual) and all(v == 0 for v in dual @ a2)
    assert ranks(isolated) == (5, 5)
    check_generator(isolated, stationary(isolated))

    # A distant complete realization of the locally isolated same kernel.
    distant_s = eye(5)
    distant_s[2:, 2:] = matrix([[871, -390, 519], [623, 790, -413],
                               [-183, 133, 1050]])/1000
    distant = inverse(distant_s) @ isolated @ distant_s
    distant_pi = stationary(isolated) @ distant_s
    check_generator(distant, distant_pi, complete=True)
    assert ranks(distant) == (5, 5)
    original_derivatives = derivatives(isolated, 10)
    assert all(np.array_equal(v, w) for v, w in
               zip(original_derivatives, derivatives(distant, 10)))
    assert min(distant[i, j] for i in range(5) for j in range(5) if i != j) == F(139, 500)
    h, k, disappearing_target = 3, 4, 0
    endpoint = F(104489, 1158489)
    outside = [i for i in range(5) if i not in (h, k)]
    assert endpoint == min(distant[h, i]/distant[k, i] for i in outside)
    polynomial_at_endpoint = (distant[h, k]+endpoint*(distant[h, h]-distant[k, k])
                              -distant[k, h]*endpoint*endpoint)
    assert polynomial_at_endpoint == F(6376107122347, 1342096763121) > 0
    coefficient = distant_pi[0]*(1-endpoint)*distant[0, h]
    assert coefficient == F(53132140, 1141883991)
    boundary_samples = []
    for gap in [F(1, 10**4), F(1, 10**7), F(1, 10**10)]:
        e = endpoint-gap
        step = eye(5)
        step[h, h], step[h, k] = 1-e, e
        member, member_pi = inverse(step) @ distant @ step, distant_pi @ step
        check_generator(member, member_pi, complete=True)
        assert all(np.array_equal(v, w) for v, w in
                   zip(original_derivatives, derivatives(member, 10)))
        boundary_samples.append({"gap": str(gap), "entropy": entropy(member, member_pi)})
    slope = (boundary_samples[-1]["entropy"]-boundary_samples[-2]["entropy"])/math.log(1000)
    assert math.isclose(slope, float(coefficient), rel_tol=1e-5)
    boundary_step = eye(5)
    boundary_step[h, h], boundary_step[h, k] = 1-endpoint, endpoint
    boundary = inverse(boundary_step) @ distant @ boundary_step
    boundary_pi = distant_pi @ boundary_step
    assert boundary[h, disappearing_target] == 0
    assert all(v > 0 for v in boundary_pi)
    assert boundary_pi[0]*boundary[0, h] == coefficient

    diagnostics = []
    for values in [(9, 10), (1, 1), (3, 3), (5, 5), (8, 8)]:
        source = theta(*values)
        _, _, exact_a = tangent(source)
        aa = np.array(exact_a, dtype=float)
        lp = linprog([0]*6+[-1], A_ub=np.c_[-aa, np.ones(len(aa))],
                     b_ub=np.zeros(len(aa)), bounds=[(-1, 1)]*6+[(0, None)], method="highs")
        assert lp.success
        diagnostics.append({"exit_rates": values, "maximum_strict_opening": -float(lp.fun),
                            "hidden_eigenvalues": sorted(np.linalg.eigvals(np.array(source[2:, 2:], float)).real.tolist())})
    paths = [Path(__file__), Path(__file__).with_name("check_small_networks.py"),
             Path(__file__).with_name("check_four_state_classification.py")]
    result = {"executed_at": datetime.now(timezone.utc).isoformat(),
              "environment": {"python": platform.python_version(), "numpy": np.__version__,
                              "scipy": scipy.__version__, "platform": platform.platform()},
              "script_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              "inputs": "Embedded rational inputs and five deterministic LP diagnostics; no random or exhaustive search.",
              "three_state_mixing": {"source_generator": strings(open_source),
                                     "hidden_similarity": strings(similarity[2:, 2:]),
                                     "transformed_generator": strings(transformed),
                                     "minimum_missing_rate_derivative": str(min(velocity)),
                                     "derivative_orders": [0, 9]},
              "local_isolation": {"generator": strings(isolated), "missing_edges": missing,
                                  "tangent_matrix": strings(a2), "rank": 6,
                                  "positive_dual": [str(v) for v in dual], "ranks": ranks(isolated),
                                  "scope": "Local isolation; the distant complete realization below proves the full compatibility set is disconnected and entropy unbounded."},
              "distant_realization": {"hidden_similarity": strings(distant_s[2:, 2:]),
                                      "generator": strings(distant),
                                      "stationary": [str(v) for v in distant_pi],
                                      "minimum_offdiagonal": "139/500",
                                      "source_entropy": entropy(isolated, stationary(isolated)),
                                      "distant_entropy": entropy(distant, distant_pi),
                                      "boundary_pair": [h, k], "boundary_endpoint": str(endpoint),
                                      "disappearing_edge": [h, disappearing_target],
                                      "log_coefficient": str(coefficient),
                                      "measured_log_coefficient": slope, "samples": boundary_samples},
              "path_reconstructions": [cycle_check(5), cycle_check(6)],
              "lp_diagnostics": diagnostics,
              "correction": "The initial unsaved probe used eigvalsh on a nonsymmetric hidden block. This diagnostic was corrected to eigvals; exact tangent matrices and LP results were unaffected.",
              "limitation": "General results use the linked proofs; no full five-state classification or novelty claim."}
    Path(__file__).with_name("five-state-extension-checks.json").write_text(
        json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"executed_at": result["executed_at"], "all_checks_passed": True,
                      "cycle_state_counts": [5, 6], "isolated_tangent_rank": 6,
                      "exact_complete_graph_opening": True}, indent=2))


if __name__ == "__main__":
    main()
