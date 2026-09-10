"""Exact state-splitting and nonminimal four-state entropy witnesses.

Run: python analysis/check_state_splitting.py
Uses the same deterministic rational algebra and numerical dependencies as the
other checks. General claims are proved in the accompanying audit notes.
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

from check_small_networks import check_generator, derivatives, entropy, eye, matrix
from check_four_state_classification import stationary


def split_hidden(q, hidden, forward, backward, theta=F(1, 3)):
    assert hidden not in (0, 1)  # These are the endpoints of the observed marks.
    assert 0 < theta < 1
    size = len(q)
    expanded = matrix(np.zeros((size+1, size+1), dtype=int))
    expanded[:size, :size] = q
    for i in range(size):
        if i != hidden:
            expanded[i, hidden] = theta*q[i, hidden]
            expanded[i, size] = (1-theta)*q[i, hidden]
            expanded[size, i] = q[hidden, i]
    expanded[hidden, size], expanded[size, hidden] = forward, backward
    for i in range(size+1):
        expanded[i, i] = -sum(expanded[i, j] for j in range(size+1) if j != i)
    membership = matrix(np.zeros((size+1, size), dtype=int))
    membership[:size, :] = eye(size)
    membership[size, hidden] = F(1)
    return expanded, membership


def assert_kernel(q, reference):
    count = len(q)+len(reference)
    assert all(np.array_equal(a, b) for a, b in
               zip(derivatives(q, count), derivatives(reference, count)))


def main():
    # Globally unique among four-state models, but not when a fifth is allowed.
    original = matrix([[-3, 1, 2, 0], [1, -9, 3, 5],
                       [1, 1, -2, 0], [0, 1, 0, -1]])
    hidden, backward, theta = 2, F(2), F(1, 3)
    original_pi = stationary(original)
    lam = -original[hidden, hidden]
    alpha = theta*lam
    coefficient = backward*original_pi[hidden]*(lam-alpha)/(lam+backward)
    split_rows = []
    for forward in [F(1, 1000), F(1, 10**6), F(1, 10**9)]:
        q, membership = split_hidden(original, hidden, forward, backward, theta)
        assert np.array_equal(q @ membership, membership @ original)
        pi = matrix([list(original_pi)+[F(0)]])[0]
        pi[hidden] = original_pi[hidden]*(alpha+backward)/(lam+forward+backward)
        pi[-1] = original_pi[hidden]*(lam+forward-alpha)/(lam+forward+backward)
        check_generator(q, pi)
        assert np.array_equal(pi, stationary(q))
        assert np.array_equal(pi @ membership, original_pi)
        assert_kernel(q, original)
        sigma = entropy(q, pi)
        split_rows.append({"forward_rate": str(forward), "entropy": sigma,
                           "entropy_minus_leading_log": sigma-float(coefficient)*math.log(1/float(forward))})
    slope = (split_rows[-1]["entropy"]-split_rows[-2]["entropy"])/math.log(1000)
    assert math.isclose(slope, float(coefficient), rel_tol=1e-5)

    # With equal hidden exits, internal rates are invisible under strong lumping.
    # Check both full incidence and a tree whose observed edge is a leaf.
    nonminimal = []
    membership = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]])
    for name, base in [
        ("full_incidence", matrix([[-4, 1, 2, 1], [1, -4, 1, 2],
                                   [1, 2, -3, 0], [1, 2, 0, -3]])),
        ("one_port_tree", matrix([[-1, 1, 0, 0], [1, -4, 2, 1],
                                  [0, 3, -3, 0], [0, 3, 0, -3]])),
    ]:
        quotient = (base @ membership)[[0, 1, 2], :]
        assert np.array_equal(base @ membership, membership @ quotient)
        rows = []
        for forward in [F(1, 1000), F(1, 10**6), F(1, 10**9)]:
            q = base.copy()
            q[2, 3], q[3, 2] = forward, backward
            q[2, 2] -= forward
            q[3, 3] -= backward
            pi = stationary(q)
            check_generator(q, pi)
            assert np.array_equal(q @ membership, membership @ quotient)
            assert_kernel(q, quotient)
            rows.append({"forward_rate": str(forward), "entropy": entropy(q, pi)})
        boundary = base.copy()
        boundary[3, 2] = backward
        boundary[3, 3] -= backward
        boundary_pi = stationary(boundary)
        assert all(p > 0 for p in boundary_pi)
        edge_flux = backward*boundary_pi[3]
        slope = (rows[-1]["entropy"]-rows[-2]["entropy"])/math.log(1000)
        assert math.isclose(slope, float(edge_flux), rel_tol=1e-5)
        nonminimal.append({"name": name,
                           "base_generator": [[str(v) for v in row] for row in base],
                           "quotient_generator": [[str(v) for v in row] for row in quotient],
                           "log_divergence_coefficient": str(edge_flux), "samples": rows})

    paths = [Path(__file__), Path(__file__).with_name("check_small_networks.py"),
             Path(__file__).with_name("check_four_state_classification.py")]
    result = {
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__, "platform": platform.platform()},
        "script_sha256": {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
        "inputs": "Exact rational matrices embedded in the script; theta=1/3, backward clone rate=2; no randomness.",
        "state_split": {"original_generator": [[str(v) for v in row] for row in original],
                        "original_stationary": [str(p) for p in original_pi],
                        "cloned_state": hidden, "state_counts": [4, 5],
                        "derivative_orders": [0, 8],
                        "log_divergence_coefficient": str(coefficient), "samples": split_rows},
        "nonminimal_families": nonminimal,
        "limitation": "Exact representative intertwining and derivative certificates; general coverage and divergence use the proofs. Novelty unestablished.",
    }
    Path(__file__).with_name("state-splitting-checks.json").write_text(
        json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"executed_at": result["executed_at"],
                      "state_split_counts": [4, 5], "split_log_coefficient": str(coefficient),
                      "nonminimal_families": len(nonminimal), "all_checks_passed": True}, indent=2))


if __name__ == "__main__":
    main()
