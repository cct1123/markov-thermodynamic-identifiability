"""Exact constants and modal identities for the global fast-theta cone proof.

Run: python -B analysis/check_theta_fast_spectral.py
Standard library plus the local Q(sqrt(6)) helper; no search or sampling.
The proof's universal triangle exclusion is analytic, not a numerical test.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

from check_theta_residue_construction import (
    ALPHA, BETA, Q6, ROOT6, Z_ALPHA, Z_BETA, encode, entropy, identity,
    inverse, matrix, multiply, parameters_and_ranks, rank, theta, validate,
)


def diagonal(values):
    return matrix([[value if i == j else 0 for j in range(len(values))]
                   for i, value in enumerate(values)])


def check_case(value):
    a = b = Q6(value)
    source = theta(a, b)
    pi = validate(source)
    _, ranks = parameters_and_ranks(source)
    assert ranks == {"controllability": 5, "observability": 5}
    x = [row[2:] for row in source[:2]]
    y = [row[:2] for row in source[2:]]
    h = [row[2:] for row in source[2:]]
    p = [3+ROOT6/2, 35*ROOT6/8]
    q = [3-ROOT6/2, -35*ROOT6/8]
    r_y = 4*(ROOT6-1)/5
    f_y = -4*(ROOT6+1)/5
    xm = matrix([[p[0], q[0], 8], [p[1], q[1], 11]])
    ym = matrix([[1, r_y], [1, f_y], [a, b]])
    modes = diagonal([-ALPHA, -BETA, -a-b])
    basis = matrix([[p[0]/2, q[0]/2, 0],
                    [p[1]/7, q[1]/7, 0], [0, 0, 1]])
    assert multiply(h, basis) == multiply(basis, modes)
    assert multiply(x, basis) == xm
    assert multiply(inverse(basis), y) == ym
    assert multiply([[v] for v in p], [ym[0]]) == Z_ALPHA
    assert multiply([[v] for v in q], [ym[1]]) == Z_BETA
    assert [[Z_ALPHA[i][j]+Z_BETA[i][j] for j in range(2)]
            for i in range(2)] == diagonal([6, 42])
    hidden_observability, hidden_control = [], [[], [], []]
    power = identity(3)
    for _ in range(3):
        hidden_observability.extend(multiply(x, power))
        hidden_control = [old+new for old, new in
                          zip(hidden_control, multiply(power, y))]
        power = multiply(power, h)
    assert rank(hidden_observability) == rank(hidden_control) == 3
    m = (7+2*ROOT6)/5
    k_left = q[0]/8
    k_right = p[1]/11
    assert p[0]/q[0] == m and f_y/r_y == -m
    assert p[1] == -q[1]
    input_a, input_b = a, b/r_y
    kappa_minus_one = (a+b-BETA)/(BETA-ALPHA)
    assert a+b > BETA and kappa_minus_one > 0
    first_margin = kappa_minus_one*input_b-k_right*(1+(input_a+1)/k_left)
    second_margin = kappa_minus_one*input_a-k_left*(m+(input_b+1)/k_right)
    assert first_margin > 0 and second_margin > 0
    return {"balanced_rate": a, "source_generator": source,
            "source_stationary": pi, "source_entropy_numeric": entropy(source, pi),
            "full_ranks": ranks, "hidden_ranks": [3, 3],
            "modal_basis": basis, "modal_generator": modes,
            "modal_entrance": xm, "modal_exit": ym,
            "inputs": [[1, input_a], [-m, input_b]],
            "kappa_minus_one": kappa_minus_one,
            "strict_region_margins": [first_margin, second_margin],
            "all_exact_checks_passed": True}


def shifted_quadratic(a, b, c, origin=40):
    return [a*origin*origin+b*origin+c, 2*a*origin+b, a]


def main():
    r_y = 4*(ROOT6-1)/5
    m = (7+2*ROOT6)/5
    k_left = (3-ROOT6/2)/8
    k_right = 35*ROOT6/88
    assert Q6(F(12, 5)) < ROOT6 < Q6(F(5, 2))
    assert 2 < m < Q6(F(5, 2))
    assert Q6(F(1, 5)) < k_left < Q6(F(1, 4))
    assert Q6(F(9, 10)) < k_right < 1
    assert 1 < r_y < Q6(F(6, 5))
    assert k_left*(1+m) < Q6(F(7, 8)) < 1
    input_b_100 = 100/r_y
    assert input_b_100 == 25*(ROOT6+1)
    assert 80 < input_b_100 < 90
    assert (200-BETA)/(BETA-ALPHA) > 18
    bound_positive_bottom = F(1+5*101, 18)
    bound_negative_bottom = (F(5, 2)+91/F(9, 10))/72
    assert bound_positive_bottom == F(253, 9) < 29 < 80
    assert bound_negative_bottom == F(1865, 1296) < 2 < 100
    polynomial_left = shifted_quadratic(1, -37, -36)
    polynomial_right = shifted_quadratic(72, -604, -325)
    assert polynomial_left == [84, 43, 1]
    assert polynomial_right == [90715, 5156, 72]
    assert all(value > 0 for value in polynomial_left+polynomial_right)
    cases = [check_case(100), check_case(40)]
    path = Path(__file__).resolve()
    helper = path.with_name("check_theta_residue_construction.py")
    result = {"executed_at": datetime.now(timezone.utc).isoformat(),
              "environment": {"python": platform.python_version(),
                              "platform": platform.platform(),
                              "dependencies": "Python standard library only"},
              "script_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in (path, helper)},
              "inputs": "Embedded exact theta generators at (100,100) and (40,40); no search",
              "wedge_constants": {"m": m, "k_left": k_left, "k_right": k_right,
                                   "r_y": r_y, "universal_W_upper_bound": Q6(F(7, 8))},
              "point_100_coarse_bounds": {"positive_bottom": Q6(bound_positive_bottom),
                                           "negative_bottom": Q6(bound_negative_bottom)},
              "balanced_ray_shifted_polynomials": {
                  "coordinate": "t=z-40 >=0; coefficients ascending",
                  "z_squared_minus_37z_minus_36": polynomial_left,
                  "72z_squared_minus_604z_minus_325": polynomial_right},
              "cases": cases,
              "scope": "Exact arithmetic support for the analytic invariant-triangle exclusion; no finite sampling or optimizer-based nonexistence claim.",
              "all_exact_checks_passed": True}
    destination = path.parents[1]/"outputs"/"check_theta_fast_spectral.json"
    destination.write_text(json.dumps(encode(result), indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"executed_at": result["executed_at"],
                      "all_exact_checks_passed": True,
                      "balanced_rates": [100, 40], "output": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
