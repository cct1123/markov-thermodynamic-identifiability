"""Exact witness crossing the balanced theta strict-first-order boundary.

Run from root: .\.venv\Scripts\python.exe -B analysis/check_balanced_boundary_witness.py
Outputs only outputs/balanced-boundary-witness.json. No random search.
The rational witness uses Fraction elimination; an independent SymPy adjugate
calculation checks equality of the complete hidden transfer rational function.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def inv(a):
    n = len(a)
    aug = [list(a[i])+eye(n)[i] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        d = aug[k][k]
        aug[k] = [v/d for v in aug[k]]
        for i in range(n):
            if i != k:
                d = aug[i][k]
                aug[i] = [v-d*w for v, w in zip(aug[i], aug[k])]
    return [row[n:] for row in aug]


def theta(z):
    return mat([[-11, 1, 2, 0, 8], [2, -20, 0, 7, 11],
                [3, 0, -7, 4, 0], [0, 6, 5, -11, 0],
                [z, z, 0, 0, -2*z]])


def embed(u):
    t = eye(5)
    for i in range(3):
        for j in range(3):
            t[i+2][j+2] = u[i][j]
    return t


def stationary(q):
    n = len(q)
    a = [list(row) for row in zip(*q)]
    a[-1] = [F(1)]*n
    pi = [row[-1] for row in inv(a)]
    assert sum(pi) == 1 and min(pi) > 0
    assert mul([pi], q) == [[F(0)]*n]
    return pi


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, sp.Basic):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def positive_quadratic(x):
    """Prove positivity by a checked rational enclosure of sqrt(770)."""
    x = sp.expand(sp.radsimp(x))
    r = sp.sqrt(770)
    b = x.coeff(r)
    a = sp.expand(x-b*r)
    assert a.is_Rational and b.is_Rational
    lower = sp.Rational(27748873851023, 10**12)
    upper = lower+sp.Rational(1, 10**12)
    assert lower > 0 and lower**2 < 770 < upper**2
    bound = a+b*(lower if b >= 0 else upper)
    assert bound > 0
    return {"exact": x, "certified_positive_lower_bound": bound,
            "approximate": float(x)}


def local_check():
    root = sp.sqrt(770)
    m = 4*root/11
    zc = (11+m)/2
    k = sp.Matrix([[0, -zc*m/30, m/5], [zc/3, 0, -1],
                   [-7*zc/33, zc*m/120, 0]])
    ell = sp.Matrix([[0, sp.Rational(1081, 100), sp.Rational(301, 50)],
                     [sp.Rational(699, 100), 0, sp.Rational(573, 100)],
                     [-sp.Rational(213, 50), -sp.Rational(49, 20), 0]])
    for matrix in (k, ell):
        for i in range(3):
            matrix[i, i] = -sum(matrix[i, j] for j in range(3) if i != j)
    k = k.applyfunc(sp.expand)
    q = sp.Matrix([[-11, 1, 2, 0, 8], [2, -20, 0, 7, 11],
                   [3, 0, -7, 4, 0], [0, 6, 5, -11, 0],
                   [zc, zc, 0, 0, -2*zc]])
    ke, le = sp.zeros(5), sp.zeros(5)
    ke[2:, 2:], le[2:, 2:] = k, ell
    first = (q*ke-ke*q).applyfunc(sp.expand)
    second = (q*le-le*q-ke*first).applyfunc(sp.expand)
    missing = [(0, 3), (1, 2), (2, 1), (2, 4),
               (3, 0), (3, 4), (4, 2), (4, 3)]
    active = [0, 1, 2, 4, 5, 7]
    assert all(first[missing[i]] == 0 for i in active)
    first_openings = [positive_quadratic(first[missing[i]]) for i in (3, 6)]
    second_openings = [positive_quadratic(second[missing[i]]) for i in active]
    p, qq, rr, v, t, u = sp.symbols("p q r v t u")
    aa = sp.Matrix([2*p+8*u, 7*rr+11*t, -6*p-zc*qq,
                    -3*rr-zc*v, 5*qq+m*v, -4*t-m*u]).jacobian(
                        [p, qq, rr, v, t, u])
    dual = aa.T.nullspace()[0].applyfunc(lambda x: sp.expand(sp.radsimp(x)))
    assert aa.rank() == 5 and (aa.T*dual).applyfunc(sp.simplify) == sp.zeros(6, 1)
    dual_checks = [positive_quadratic(x) for x in dual]
    raw_second = -ke*first
    curvature = sp.simplify(sum(dual[j]*raw_second[missing[i]]
                               for j, i in enumerate(active)))
    assert sp.simplify(curvature-(2077*root/sp.Integer(11979)
                                 +sp.Rational(8869, 1815))) == 0
    return {"zc": zc, "zc_approximate": float(zc), "K": k.tolist(),
            "L": ell.tolist(), "missing_rate_order": missing,
            "active_zero_first_order_indices": active,
            "positive_first_order_openings": first_openings,
            "positive_second_order_openings": second_openings,
            "positive_active_dual": dual_checks,
            "active_rank": 5, "dual_curvature": positive_quadratic(curvature),
            "status": "exact checks supporting the local analytic construction"}


def transfer_identity(source, target):
    """Polynomial rational-function identity, independent of Fraction inverse."""
    lam = sp.symbols("lambda")
    outputs = []
    for rows in (source, target):
        q = sp.Matrix(rows)
        x, y, h = q[:2, 2:], q[2:, :2], q[2:, 2:]
        pencil = lam*sp.eye(3)-h
        denominator = sp.Poly(pencil.det(), lam)
        numerator = (x*pencil.adjugate()*y).applyfunc(sp.expand)
        outputs.append((denominator, numerator))
    assert outputs[0][0] == outputs[1][0]
    assert outputs[0][1] == outputs[1][1]
    return {"common_denominator": outputs[0][0].as_expr(),
            "common_numerator": outputs[0][1].tolist(),
            "all_time_identity": True,
            "method": "independent SymPy determinant/adjugate polynomial identity"}


def main():
    u = mat([[F(31297248897, 31250000000), -F(176804231, 50000000000),
              F(506029979, 250000000000)],
             [F(220129579, 62500000000), F(7792751537, 7812500000),
              -F(99427, 100000000)],
             [-F(70035349, 31250000000), F(176854731, 200000000000),
              F(1001356857513, 1000000000000)]])
    assert all(sum(row) == 1 for row in u)
    t, ti = embed(u), inv(embed(u))
    assert mul(t, ti) == eye(5) == mul(ti, t)
    low, high = F(2109, 200), F(21091, 2000)
    # zc=(11+sqrt(1120/11))/2 lies strictly between these rationals.
    assert 0 < 2*low-11 and (2*low-11)**2 < F(1120, 11) < (2*high-11)**2
    cases = []
    for z in (low, high):
        q = theta(z)
        qp = mul(mul(ti, q), t)
        rates = [(qp[i][j], [i, j]) for i in range(5) for j in range(5) if i != j]
        minimum, at = min(rates)
        assert minimum > 0
        assert all(sum(row) == 0 for row in qp)
        assert [row[:2] for row in qp[:2]] == [row[:2] for row in q[:2]]
        pi, pip = stationary(q), stationary(qp)
        assert mul([pi], t)[0] == pip
        cases.append({"z": z, "source": q, "target": qp,
                      "stationary_source": pi, "stationary_target": pip,
                      "minimum_offdiagonal": minimum,
                      "minimum_offdiagonal_approximate": float(minimum),
                      "minimum_location_zero_based": at,
                      "transfer_identity": transfer_identity(q, qp)})
    result = {"created_utc": datetime.now(timezone.utc).isoformat(),
              "command": ".\\.venv\\Scripts\\python.exe -B analysis/check_balanced_boundary_witness.py",
              "environment": {"python": platform.python_version(), "sympy": sp.__version__,
                              "platform": platform.platform()},
              "assumptions": "row CTMC; five states (x,y,h,k,l); only x<->y observed; exact joint marked waiting kernels; positive bidirected rates",
              "method": "fixed rational normalized hidden similarity; exact endpoint positivity and affine interpolation; independent full rational transfer identity",
              "topology": "both targets have all 20 ordered off-diagonal rates positive",
              "units": "common arbitrary inverse-time unit, Boltzmann constant one",
              "random_seed": None, "search_bounds": None, "optimizer": None,
              "witness_U": u, "det_U": sp.Matrix(u).det(),
              "certified_balanced_parameter_interval": [low, high],
              "interval_reason": "For this fixed U, every transformed rate is affine in z. Strict endpoint positivity proves strict positivity throughout the interval, including zc.",
              "cases": cases, "local_boundary_check": local_check(),
              "failed_exploration": [
                  {"attempt": "initial verification run compared unsimplified symbolic matrix expressions structurally",
                   "status": "checker assertion failed; corrected to simplify each exact residual before zero comparison, with no change to the mathematical candidate"},
                  {"attempt": "unrounded algebraic U=I+epsilon K+epsilon^2 L at zc, epsilon=1/100",
                   "status": "inadmissible; a negative off-diagonal detected",
                   "numerical_minimum": -0.0001789484982661008},
                  {"attempt": "same algebraic curve, epsilon=1/50",
                   "status": "inadmissible; a negative off-diagonal detected",
                   "numerical_minimum": -0.002439293210325819},
                  {"attempt": "same algebraic curve, epsilon=1/20",
                   "status": "inadmissible; a negative off-diagonal detected",
                   "numerical_minimum": -0.05684530238957748}],
              "limitations": "This is an existence certificate on one small interval and an analytic local opening, not a sharp boundary or global exclusion. Failed larger epsilon choices are not impossibility evidence.",
              "all_checks_passed": True}
    paths = [Path(__file__), ROOT/"analysis/theta-family-construction-audit.md",
             ROOT/"analysis/theta-fast-spectral-audit.md"]
    result["source_sha256"] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    output = ROOT/"outputs/balanced-boundary-witness.json"
    output.write_text(json.dumps(encode(result), indent=2)+"\n", encoding="utf-8")
    print(f"PASS: exact complete realizations for every z in [{low}, {high}], containing zc.")
    print(f"Minimum endpoint rates: {[case['minimum_offdiagonal_approximate'] for case in cases]}")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
