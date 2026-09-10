"""Exact rational and independent numerical checks of small CTMC examples.

Run from the repository root: python analysis/check_small_networks.py
Requires numpy and scipy; no random sampling or external input files.
See small-network-audit.md for arguments and literature limitations.
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


def matrix(rows):
    # Convert NumPy scalars first: Fraction(np.int64) can retain fixed-width
    # numerators and overflow, defeating the intended exact arithmetic.
    return np.array([[F(x.item() if isinstance(x, np.generic) else x)
                      for x in row] for row in rows], dtype=object)


def eye(n):
    return matrix(np.eye(n, dtype=int))


def exact_rank(a):
    a = a.copy()
    row = 0
    for col in range(a.shape[1]):
        pivot = next((i for i in range(row, len(a)) if a[i, col]), None)
        if pivot is None:
            continue
        a[[row, pivot]] = a[[pivot, row]]
        a[row] = a[row] / a[row, col]
        for i in range(len(a)):
            if i != row:
                a[i] = a[i] - a[i, col] * a[row]
        row += 1
        if row == len(a):
            break
    return row


def marked_system(q):
    """Observe +=(0,1), -=(1,0); retain the original diagonals."""
    n = len(q)
    t = q.copy()
    t[0, 1] = t[1, 0] = F(0)
    r = eye(n)[[1, 0], :]
    b = matrix(np.zeros((n, 2), dtype=int))
    b[0, 0], b[1, 1] = q[0, 1], q[1, 0]
    return r, t, b


def derivatives(q, count):
    r, t, b = marked_system(q)
    power = eye(len(q))
    values = []
    for _ in range(count):
        values.append(r @ power @ b)
        power = power @ t
    return values


def check_generator(q, pi, complete=False):
    n = len(q)
    assert all(sum(row) == 0 for row in q)
    assert sum(pi) == 1 and all(p > 0 for p in pi)
    assert all(x == 0 for x in pi @ q)
    for i in range(n):
        for j in range(i + 1, n):
            assert q[i, j] >= 0 and q[j, i] >= 0
            assert (q[i, j] > 0) == (q[j, i] > 0)
            if complete:
                assert q[i, j] > 0


def entropy(q, pi):
    total = 0.0
    for i in range(len(q)):
        for j in range(i + 1, len(q)):
            if q[i, j]:
                forward, reverse = pi[i] * q[i, j], pi[j] * q[j, i]
                total += float(forward - reverse) * math.log(float(forward / reverse))
    return total


def three_state(a, b, c, d, e, f):
    return matrix([[-a-c, a, c], [b, -b-e, e], [d, f, -d-f]])


def reconstruct_three(q):
    z, first, second = derivatives(q, 3)
    a, b = z[1, 0], z[0, 1]
    c, e = -first[1, 0] / a - a, -first[0, 1] / b - b
    d = (second[1, 0] / a - (a+c)**2) / c if c else F(0)
    f = (second[0, 1] / b - (b+e)**2) / e if e else F(0)
    return three_state(a, b, c, d, e, f)


def minimal_family(t):
    return matrix([
        [-6, 1, 2*(1-t), 3+2*t],
        [1, -10, 4*(1-t), 5+4*t],
        [(2-3*t)/(1-t), (4-5*t)/(1-t), -7-t, (1+2*t-t*t)/(1-t)],
        [3, 5, 1-t, -9+t],
    ])


def minimal_entropy_formula(t):
    ratio = 120*(1+2*t-t*t)**2 / ((2-3*t)*(4-5*t)*(3+2*t)*(5+4*t))
    return float(t/4) * math.log(float(ratio))


def equal_escape_diamond(t):
    return matrix([
        [-4, 1, 2*(1-t), 1+2*t],
        [1, -4, 1-t, 2+t],
        [(2-t)/(1-t), (1-2*t)/(1-t), -3, 0],
        [1, 2, 0, -3],
    ])


def main():
    # Exact reconstruction on triangle and both hidden-leaf supports.
    triples = [(1, 2, 3, 4, 5, 6), (2, 1, 3, 7, 0, 0),
               (2, 3, 0, 0, 5, 11), (F(1, 3), F(2, 5), F(3, 7),
                                       F(5, 11), F(7, 13), F(11, 17))]
    for rates in triples:
        q = three_state(*rates)
        assert np.array_equal(reconstruct_three(q), q)
    q2 = matrix([[-2, 2], [3, -3]])
    z, first = derivatives(q2, 2)
    assert -first[1, 0]/z[1, 0]-z[1, 0] == 0
    assert -first[0, 1]/z[0, 1]-z[0, 1] == 0

    # Source-informed lumpable diamond, with a three-state quotient.
    lump = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]])
    quotient = matrix([[-3, 1, 2], [1, -3, 2], [1, 1, -2]])
    quotient_derivatives = derivatives(quotient, 7)
    lump_checks = []
    for u in [F(1), F(1, 2), F(1, 10), F(1, 1000)]:
        q = matrix([[-3, 1, u, 2-u], [1, -3, 1, 1],
                    [1, 1, -2, 0], [1, 1, 0, -2]])
        pi = matrix([[F(1, 4), F(1, 4), (u+1)/8, (3-u)/8]])[0]
        check_generator(q, pi)
        assert np.array_equal(q @ lump, lump @ quotient)
        assert all(np.array_equal(x, y) for x, y in
                   zip(derivatives(q, 7), quotient_derivatives))
        actual = entropy(q, pi)
        formula = float((u-1)/8) * math.log(float(u/(2-u)))
        assert math.isclose(actual, formula, rel_tol=1e-12, abs_tol=1e-14)
        lump_checks.append({"u": str(u), "entropy": actual})

    # Minimal four-state example: equality is certified exactly, then sampled
    # numerically using matrix exponentials as an independent implementation.
    base = minimal_family(F(0))
    reference = derivatives(base, 8)
    r0, t0, b0 = marked_system(base)
    ctrb_rank = exact_rank(np.concatenate([b0, t0 @ b0], axis=1))
    obsv_rank = exact_rank(np.concatenate([r0, r0 @ t0], axis=0))
    assert ctrb_rank == obsv_rank == 4
    times = np.concatenate(([0.0], np.geomspace(1e-6, 100.0, 65)))
    kernel0 = [np.asarray(r0, float) @ expm(np.asarray(t0, float)*time)
               @ np.asarray(b0, float) for time in times]
    rows = []
    for t in [F(0), F(1, 4), F(1, 2), F(2, 3)-F(1, 1000),
              F(2, 3)-F(1, 10**6), F(2, 3)-F(1, 10**12)]:
        q = minimal_family(t)
        pi = matrix([[F(1, 4), F(1, 4), (1-t)/4, (1+t)/4]])[0]
        check_generator(q, pi, complete=True)
        s, sinv = eye(4), eye(4)
        s[2, 2], s[2, 3] = 1-t, t
        sinv[2, 2], sinv[2, 3] = 1/(1-t), -t/(1-t)
        assert np.array_equal(s @ sinv, eye(4))
        assert np.array_equal(q, sinv @ base @ s)
        assert all(np.array_equal(x, y) for x, y in zip(derivatives(q, 8), reference))
        r, killed, b = marked_system(q)
        assert exact_rank(np.concatenate([b, killed @ b], axis=1)) == 4
        assert exact_rank(np.concatenate([r, r @ killed], axis=0)) == 4
        rf, tf, bf = np.asarray(r, float), np.asarray(killed, float), np.asarray(b, float)
        residual = max(float(np.max(np.abs(rf @ expm(tf*time) @ bf - expected)))
                       for time, expected in zip(times, kernel0))
        assert residual < 1e-12
        integrated = rf @ np.linalg.solve(-tf, bf)
        first_moment = rf @ np.linalg.solve(-tf, np.linalg.solve(-tf, bf))
        assert np.allclose(integrated.sum(axis=1), 1, rtol=0, atol=1e-12)
        rho = np.array([0.5, 0.5])
        assert np.allclose(rho @ integrated, rho, rtol=0, atol=1e-12)
        mean = float(rho @ first_moment @ np.ones(2))
        assert math.isclose(mean, 2.0, rel_tol=0, abs_tol=1e-12)
        actual, formula = entropy(q, pi), minimal_entropy_formula(t)
        assert math.isclose(actual, formula, rel_tol=1e-12, abs_tol=1e-14)
        rows.append({"parameter": str(t), "entropy": actual,
                     "formula_residual": abs(actual-formula),
                     "maximum_kernel_residual": residual,
                     "mean_interevent_time": mean,
                     "vanishing_reverse_rate": str(q[2, 0]),
                     "opposing_flux": str(pi[0]*q[0, 2])})
    assert math.isclose(rows[1]["entropy"], math.log(529/154)/16, abs_tol=1e-14)

    # Same fixed diamond topology: a distinct-escape identifiable example,
    # and a repeated-escape minimal family with varying, unbounded entropy.
    identifiable = matrix([[-4, 1, 2, 1], [1, -4, 1, 2],
                           [3, 1, -4, 0], [1, 2, 0, -3]])
    identifiable_pi = matrix([[F(29, 103), F(26, 103), F(21, 103), F(27, 103)]])[0]
    check_generator(identifiable, identifiable_pi)
    identifiable_entropy = entropy(identifiable, identifiable_pi)
    assert math.isclose(identifiable_entropy, 5/103*math.log(3/2), abs_tol=1e-14)
    equal_base = equal_escape_diamond(F(0))
    equal_reference = derivatives(equal_base, 8)
    equal_rows = []
    for t in [F(0), F(1, 4), F(1, 2)-F(1, 1000), F(1, 2)-F(1, 10**9)]:
        q = equal_escape_diamond(t)
        pi = matrix([[F(1, 4), F(1, 4), (1-t)/4, (1+t)/4]])[0]
        check_generator(q, pi)
        r, killed, b = marked_system(q)
        assert exact_rank(np.concatenate([b, killed @ b], axis=1)) == 4
        assert exact_rank(np.concatenate([r, r @ killed], axis=0)) == 4
        assert all(np.array_equal(x, y) for x, y in zip(derivatives(q, 8), equal_reference))
        formula = float(t/4)*math.log(float((2-t)*(1+2*t)/((1-2*t)*(2+t))))
        actual = entropy(q, pi)
        assert math.isclose(actual, formula, rel_tol=1e-12, abs_tol=1e-14)
        equal_rows.append({"parameter": str(t), "entropy": actual,
                           "vanishing_reverse_rate": str(q[2, 1])})

    # General equal-escape factorization used in the accompanying proof.
    x = matrix([[2, 1], [1, 2]])
    y = matrix([[2, 1], [1, 2]])
    m = x @ y
    alpha, beta, lam = F(5, 9), F(4, 9), F(3)
    for p, q in [(F(1, 10), F(3, 4)), (F(1, 10**6), F(3, 4))]:
        new_y = lam * matrix([[p, 1-p], [q, 1-q]])
        new_x = matrix([[3*(q-alpha)/(q-p), 3*(alpha-p)/(q-p)],
                        [3*(q-beta)/(q-p), 3*(beta-p)/(q-p)]])
        assert all(value > 0 for value in new_x.flat)
        assert all(value > 0 for value in new_y.flat)
        assert np.array_equal(new_x @ new_y, m)
        candidate = equal_base.copy()
        candidate[:2, 2:], candidate[2:, :2] = new_x, new_y
        assert all(np.array_equal(a, b) for a, b in zip(derivatives(candidate, 8), equal_reference))

    # Negative controls: genuine rate change and incorrect killing alter data.
    perturbed = base.copy()
    perturbed[0, 2] += F(1, 10)
    perturbed[0, 0] -= F(1, 10)
    assert not np.array_equal(derivatives(perturbed, 2)[1], reference[1])
    wrong = t0.copy()
    wrong[0, 0] += base[0, 1]
    wrong[1, 1] += base[1, 0]
    assert not np.array_equal(r0 @ wrong @ b0, reference[1])

    result = {
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__, "platform": platform.platform()},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "inputs": "Exact rational rates embedded in this script; no random sampling.",
        "checks": {"three_state_cases": len(triples), "two_state_case": True,
                   "lumped_exact_derivative_orders": [0, 6],
                   "minimal_exact_derivative_orders": [0, 7],
                   "controllability_rank": ctrb_rank, "observability_rank": obsv_rank,
                   "numerical_time_grid_points": len(times), "negative_controls": 2},
        "lumpable_family": lump_checks,
        "minimal_family": rows,
        "fixed_diamond": {"distinct_escape_rates": [4, 3],
                          "identifiable_example_entropy": identifiable_entropy,
                          "repeated_escape_family": equal_rows,
                          "general_equal_escape_factorizations_checked": 2},
        "limitation": "Finite checks validate the artifacts; all-time equality, minimality, "
                      "and unboundedness rely on the accompanying exact arguments. "
                      "No exhaustive topology search or novelty claim.",
    }
    output = Path(__file__).with_name("small-network-checks.json")
    output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
