"""Exact representative checks of the observable four-state criterion.

Run: python analysis/check_observable_criterion.py
This is a rational-input audit, not a general fitting or feasibility solver.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import platform

import numpy as np
import scipy

from check_small_networks import derivatives, eye, matrix
from check_four_state_classification import physical, ranks


def det(a):
    return a[0, 0]*a[1, 1]-a[0, 1]*a[1, 0]


def inverse(a):
    return matrix([[a[1, 1], -a[0, 1]], [-a[1, 0], a[0, 0]]])/det(a)


def extract(joint):
    r, s = joint[0][1, 0], joint[0][0, 1]
    scale = matrix([[1/r, 0], [0, 1/s]])
    k = [value[[1, 0], :] @ scale for value in joint]
    assert np.array_equal(k[0], eye(2))
    d = k[1]
    a = d+matrix([[0, r], [s, 0]])
    m = k[2]-d @ d
    ell = k[3]-d @ d @ d-d @ m-m @ d
    return a, m, ell


def reconstruct(a, m, ell):
    entrance = -np.sum(a, axis=1)
    if all(v > 0 for v in entrance) and m[0, 1] == m[1, 0] == 0:
        x = matrix([[entrance[0], 0], [0, entrance[1]]])
        y = matrix([[m[0, 0]/entrance[0], 0], [0, m[1, 1]/entrance[1]]])
        h = inverse(x) @ ell @ inverse(y)
        return "A", np.block([[a, x], [y, h]])
    if det(m) == 0:
        return "unbounded", None
    j = ell @ inverse(m)
    trace = j[0, 0]+j[1, 1]
    discriminant = trace*trace-4*det(j)
    if discriminant <= 0:
        return "unbounded", None
    # These selected inputs have rational hidden eigenvalues. Reject other
    # inputs rather than silently replacing an exact sign test by a tolerance.
    p, q = isqrt(discriminant.numerator), isqrt(discriminant.denominator)
    assert p*p == discriminant.numerator and q*q == discriminant.denominator
    root = F(p, q)
    fast, slow = (-trace+root)/2, (-trace-root)/2
    assert fast > slow > 0
    z_fast = -(ell+slow*m)/(fast-slow)
    z_slow = (ell+fast*m)/(fast-slow)
    singleton = any(z_slow[i, i] > 0 and all(
        z_slow[r, c] == 0 for r in range(2) for c in range(2) if (r, c) != (i, i)
    ) for i in range(2))
    if not (det(z_fast) == 0 and all(v > 0 for v in z_fast.flat) and singleton):
        return "unbounded", None
    columns, rows = [], []
    for residue, rate in [(z_fast, fast), (z_slow, slow)]:
        column = np.sum(residue, axis=1)/rate
        index = next(i for i in range(2) if column[i] > 0)
        row = residue[index, :]/column[index]
        assert np.array_equal(np.outer(column, row), residue)
        assert sum(row) == rate
        columns.append(column)
        rows.append(row)
    x, y = np.column_stack(columns), np.vstack(rows)
    h = matrix([[-fast, 0], [0, -slow]])
    return "B", np.block([[a, x], [y, h]])


def main():
    fast_shared = matrix([[-3, 1, 2, 0], [1, -9, 3, 5],
                          [1, 1, -2, 0], [0, 1, 0, -1]])
    reverse_order = fast_shared.copy()
    reverse_order[3, 1], reverse_order[3, 3] = F(4), F(-4)
    equal_order = fast_shared.copy()
    equal_order[3, 1], equal_order[3, 3] = F(2), F(-2)
    swapped = [1, 0, 2, 3]
    cases = [
        ("opposite_singletons_cycle", "A", matrix([[-3, 1, 2, 0], [1, -4, 0, 3],
                                                  [4, 0, -5, 1], [0, 5, 2, -7]])),
        ("opposite_singletons_equal_pole", "A", matrix([[-3, 1, 2, 0], [1, -4, 0, 3],
                                                       [4, 0, -4, 0], [0, 4, 0, -4]])),
        ("shared_fast", "B", fast_shared),
        ("shared_fast_swapped_visible", "B", fast_shared[np.ix_(swapped, swapped)]),
        ("shared_slow_negative_control", "unbounded", reverse_order),
        ("equal_escapes_negative_control", "unbounded", equal_order),
        ("full_diamond_distinct", "unbounded", matrix([[-4, 1, 2, 1], [1, -4, 1, 2],
                                                       [2, 1, -3, 0], [1, 3, 0, -4]])),
        ("minimal_singular_M", "unbounded", matrix([[-1, 1, 0, 0], [1, -3, 2, 0],
                                                    [0, 3, -7, 4], [0, 0, 5, -5]])),
        ("nonminimal_singular_M", "unbounded", matrix([[-4, 1, 2, 1], [1, -4, 1, 2],
                                                       [1, 2, -7, 4], [1, 2, 5, -8]])),
    ]
    outputs = []
    for name, expected, source in cases:
        assert physical(source)
        a, m, ell = extract(derivatives(source, 4))
        assert np.array_equal(m, source[:2, 2:] @ source[2:, :2])
        assert np.array_equal(ell, source[:2, 2:] @ source[2:, 2:] @ source[2:, :2])
        label, recovered = reconstruct(a, m, ell)
        assert label == expected
        if recovered is not None:
            assert physical(recovered)
            assert np.array_equal(source, recovered)
            assert all(np.array_equal(v, w) for v, w in
                       zip(derivatives(source, 8), derivatives(recovered, 8)))
        outputs.append({"case": name, "classification": label, "ranks": ranks(source),
                        "det_M": str(det(m)), "generator": [[str(v) for v in row] for row in source]})
    assert outputs[-2]["ranks"] == (4, 4)  # Singular M does not imply nonminimality.
    paths = [Path(__file__), Path(__file__).with_name("check_small_networks.py"),
             Path(__file__).with_name("check_four_state_classification.py")]
    result = {"executed_at": datetime.now(timezone.utc).isoformat(),
              "environment": {"python": platform.python_version(), "numpy": np.__version__,
                              "scipy": scipy.__version__, "platform": platform.platform()},
              "script_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              "inputs": "Embedded rational generators; no randomness or external data.",
              "cases": outputs,
              "limitation": "Representative algebraic checks; general coverage uses the analytic classification, not enumeration."}
    Path(__file__).with_name("observable-criterion-checks.json").write_text(
        json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"cases": len(outputs), "reconstructed": 4,
                      "executed_at": result["executed_at"], "all_checks_passed": True}, indent=2))


if __name__ == "__main__":
    main()
