"""Exact two/three-Laplace-point audit, independent of the numerical estimator.

Run: .venv/Scripts/python.exe -B -m analysis.correctness.laplace_two
Rate tuples IN THIS MODULE use the user's order (r,s,a,b,c,d), unlike the
older numerical inference module's (r,s,a,c,b,d). Generators are explicit.
All arithmetic is exact SymPy arithmetic; no tolerance or random search.
"""

if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp


P = sp.Matrix([[0, 1], [1, 0]])
R = sp.Matrix([[0, 1, 0], [1, 0, 0]])


def clean(matrix):
    return matrix.applyfunc(sp.cancel)


def generator(rates):
    """User order (r,s,a,b,c,d); row convention with state order x,y,h."""
    r, s, a, b, c, d = map(sp.sympify, rates)
    return sp.Matrix([[-r-a, r, a], [s, -s-c, c], [b, d, -b-d]])


def transform(rates, lam):
    """Full 2x2 joint transform, including r,s in B and row order (+,-).

    Direct 3x3 resolvent: this does not use any reconstruction formula.
    """
    q = generator(rates)
    t = q.copy()
    t[0, 1] = t[1, 0] = 0
    b = sp.Matrix([[q[0, 1], 0], [0, q[1, 0]], [0, 0]])
    return clean(R*(sp.sympify(lam)*sp.eye(3)-t).inv()*b)


def inverse_visible_matrix(psi):
    return clean((P*psi).inv())


def row_tests(matrices, lambdas):
    return [clean((m*sp.ones(2, 1)-sp.ones(2, 1))/lam)
            for m, lam in zip(matrices, lambdas)]


def recover_from_hidden_escape(matrices, lambdas, h):
    l1, l2 = map(sp.sympify, lambdas[:2])
    g1, g2 = row_tests(matrices[:2], (l1, l2))
    v = clean((g1-g2)*(l1+h)*(l2+h)/(l2-l1))
    u = clean(g1-v/(l1+h))
    r, s = sp.cancel(1/u[0]), sp.cancel(1/u[1])
    a, c = sp.cancel(v[0]/u[0]), sp.cancel(v[1]/u[1])
    if a != 0:
        d = sp.cancel(-r*matrices[0][0, 1]*(l1+h)/a)
        b = sp.cancel(h-d)
    elif c != 0:
        b = sp.cancel(-s*matrices[0][1, 0]*(l1+h)/c)
        d = sp.cancel(h-b)
    else:
        raise ValueError("Two-state row tests do not determine a reachable hidden state")
    return tuple(map(sp.cancel, (r, s, a, b, c, d)))


def recover_two(transforms, lambdas):
    """Exact two-point reconstruction when an inverse off-diagonal is nonzero."""
    l1, l2 = map(sp.sympify, lambdas)
    if sp.cancel(l2-l1) == 0:
        raise ValueError("Laplace arguments must be distinct")
    m = list(map(inverse_visible_matrix, transforms))
    if m[0][0, 1] != 0:
        i, j = 0, 1
    elif m[0][1, 0] != 0:
        i, j = 1, 0
    else:
        raise ValueError("Both inverse off-diagonals vanish: uncalibrated leaf case")
    ratio = sp.cancel(m[0][i, j]/m[1][i, j])
    h = sp.cancel((l2-ratio*l1)/(ratio-1))
    return recover_from_hidden_escape(m, (l1, l2), h)


def recover_two_calibrated(transforms, lambdas, r, s):
    """With both observed rates calibrated, two points cover leaf cases too."""
    l1, l2 = map(sp.sympify, lambdas)
    m = list(map(inverse_visible_matrix, transforms))
    g1, g2 = row_tests(m, (l1, l2))
    constants = (1/sp.sympify(r), 1/sp.sympify(s))
    selected = next((i for i in (0, 1) if sp.cancel(g1[i]-constants[i]) != 0), None)
    if selected is None:
        raise ValueError("No reachable hidden entrance")
    ratio = sp.cancel((g1[selected]-constants[selected])/(g2[selected]-constants[selected]))
    h = sp.cancel((l2-ratio*l1)/(ratio-1))
    return recover_from_hidden_escape(m, (l1, l2), h)


def recover_three(transforms, lambdas):
    """Replay the existing rational three-point proof, including either leaf."""
    l1, l2, l3 = map(sp.sympify, lambdas)
    m = list(map(inverse_visible_matrix, transforms))
    g = row_tests(m, (l1, l2, l3))
    selected = next((i for i in (0, 1) if sp.cancel(g[0][i]-g[1][i]) != 0), None)
    if selected is None:
        raise ValueError("No reachable hidden entrance")
    ratio = sp.cancel((g[0][selected]-g[1][selected])/(g[1][selected]-g[2][selected])
                      *(l3-l2)/(l2-l1))
    h = sp.cancel((l3-ratio*l1)/(ratio-1))
    return recover_from_hidden_escape(m, (l1, l2), h)


def stationary_and_mark_intensities(rates):
    q = generator(rates)
    system = q.T.copy()
    system[2, :] = sp.ones(1, 3)
    pi = clean(system.inv()*sp.Matrix([0, 0, 1]))
    assert clean(pi.T*q) == sp.zeros(1, 3)
    intensities = (sp.cancel(pi[0]*q[0, 1]), sp.cancel(pi[1]*q[1, 0]))
    return pi, intensities


def x_leaf_family(l1, l2, g1, g2, beta, s):
    """All these x-leaf rates match the two specified scalar G tests.

    Analytic admissible domain: beta>0 and u(beta)>0; g1>g2, l2>l1>0.
    """
    delta = sp.cancel((g1-g2)/(l2-l1))
    v = sp.cancel(delta*(l1+beta)*(l2+beta))
    u = sp.cancel(g1-delta*(l2+beta))
    return (sp.cancel(1/u), sp.sympify(s), sp.cancel(v/u), sp.sympify(beta), sp.S.Zero, sp.S.Zero)


def strings(matrix):
    return [[str(value) for value in matrix.row(i)] for i in range(matrix.rows)]


def main():
    r, s, a, b, c, d, lam, l1, l2 = sp.symbols("r s a b c d lambda lambda_1 lambda_2", positive=True)
    rates = (r, s, a, b, c, d)
    direct = transform(rates, lam)
    actual_m = inverse_visible_matrix(direct)
    h = b+d
    expected_m = sp.diag(1/r, 1/s)*(sp.diag(lam+r+a, lam+s+c)
                                   -sp.Matrix([a, c])*sp.Matrix([[b, d]])/(lam+h))
    assert clean(actual_m-expected_m) == sp.zeros(2)
    assert sp.cancel(actual_m[0, 1]+a*d/(r*(lam+h))) == 0
    assert sp.cancel(actual_m[1, 0]+c*b/(s*(lam+h))) == 0
    recovered = recover_two([direct.subs(lam, l1), direct.subs(lam, l2)], [l1, l2])
    assert all(sp.cancel(x-y) == 0 for x, y in zip(recovered, rates))

    first = (1, 1, 1, 1, 0, 0)
    second = (sp.Rational(6, 5), 1, sp.Rational(12, 5), 2, 0, 0)
    expected = [sp.Matrix([[0, sp.Rational(1, 2)], [sp.Rational(2, 5), 0]]),
                sp.Matrix([[0, sp.Rational(1, 3)], [sp.Rational(3, 11), 0]])]
    cases = []
    for p in (first, second):
        psi = transform(p, lam)
        at_two = [psi.subs(lam, value) for value in (1, 2)]
        assert at_two == expected
        assert recover_three([psi.subs(lam, value) for value in (1, 2, 3)], [1, 2, 3]) == tuple(map(sp.sympify, p))
        assert recover_two_calibrated(at_two, [1, 2], p[0], p[1]) == tuple(map(sp.sympify, p))
        pi, intensity = stationary_and_mark_intensities(p)
        cases.append({"rates_user_order": list(map(str, p)), "generator": strings(generator(p)),
                      "full_transform": strings(psi), "at_lambda_1": strings(at_two[0]),
                      "at_lambda_2": strings(at_two[1]), "at_lambda_3": strings(psi.subs(lam, 3)),
                      "stationary": list(map(str, pi)), "mark_intensities": list(map(str, intensity)),
                      "total_mark_intensity": str(sum(intensity)), "trace": str(sp.trace(generator(p))),
                      "network_entropy": "0 (reciprocal tree / detailed balance)"})
    difference = clean(transform(first, lam)-transform(second, lam))
    assert difference.subs(lam, 3) == sp.Matrix([[0, 0], [-sp.Rational(2, 893), 0]])
    assert sp.factor(difference[1, 0]) == -lam*(lam-1)*(lam-2)/((lam**2+3*lam+1)*(5*lam**2+28*lam+12))

    beta = sp.symbols("beta", positive=True)
    family = x_leaf_family(1, 2, sp.Rational(3, 2), sp.Rational(4, 3), beta, 1)
    family_expected = (6/(7-beta), sp.S.One, (beta**2+3*beta+2)/(7-beta), beta, sp.S.Zero, sp.S.Zero)
    assert all(sp.cancel(x-y) == 0 for x, y in zip(family, family_expected))
    family_psi = transform(family, lam)
    assert [clean(family_psi.subs(lam, point)) for point in (1, 2)] == expected
    _, family_intensities = stationary_and_mark_intensities(family)
    assert all(sp.cancel(value-3*beta/(8*beta+1)) == 0 for value in family_intensities)
    general_family = x_leaf_family(l1, l2,
                                 1/r+a/(r*(l1+b)), 1/r+a/(r*(l2+b)), beta, s)
    family_general_psi = transform(general_family, lam)
    original_leaf = transform((r, s, a, b, 0, 0), lam)
    for point in (l1, l2):
        assert clean(family_general_psi.subs(lam, point)-original_leaf.subs(lam, point)) == sp.zeros(2)

    one_first = (1, 1, 1, 1, 1, 1)
    one_second = (2, 2, 3, sp.Rational(2, 5), 3, sp.Rational(2, 5))
    one_data = transform(one_first, 1)
    assert one_data == transform(one_second, 1)
    assert one_data == sp.Matrix([[sp.Rational(1, 21), sp.Rational(8, 21)],
                                  [sp.Rational(8, 21), sp.Rational(1, 21)]])
    assert transform(one_first, 2) != transform(one_second, 2)

    vector_two = sp.Matrix.vstack(*(direct.subs(lam, point).reshape(4, 1) for point in (1, 2)))
    vector_three = sp.Matrix.vstack(*(direct.subs(lam, point).reshape(4, 1) for point in (1, 2, 3)))
    jac_two = vector_two.jacobian(rates)
    jac_three = vector_three.jacobian(rates)
    leaf_subs = dict(zip(rates, first))
    triangle_subs = dict(zip(rates, one_first))
    leaf_two_jac = clean(jac_two.subs(leaf_subs))
    leaf_three_jac = clean(jac_three.subs(leaf_subs))
    assert leaf_two_jac.rank() == 5
    assert leaf_three_jac.rank() == 6
    assert clean(jac_two.subs(triangle_subs)).rank() == 6
    tangent = sp.Matrix([sp.Rational(1, 6), 0, 1, 1, 0, 0])
    assert leaf_two_jac*tangent == sp.zeros(8, 1)

    output = {"all_exact_checks_passed": True,
              "kind": "exact algebraic identities and explicit counterexamples; conventional proof, not formal verification",
              "executed_at_utc": datetime.now(timezone.utc).isoformat(),
              "command": ".venv/Scripts/python.exe -B -m analysis.correctness.laplace_two",
              "environment": {"python": platform.python_version(), "sympy": sp.__version__, "platform": platform.platform()},
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "parameter_order": ["r", "s", "a", "b", "c", "d"],
              "domains": "r,s>0; connected reciprocal 3-state support; lambda_2>lambda_1>0. Generic symbolic triangle check uses a,b,c,d>0. Leaf beta family requires beta>0,u(beta)>0; explicit family 0<beta<7.",
              "randomness": "none", "precision": "exact symbolic/rational arithmetic; no numeric tolerances",
              "generic_schur_inverse": strings(clean(expected_m)),
              "generic_two_point_reconstruction": list(map(str, recovered)),
              "leaf_counterexamples": cases,
              "full_law_difference": strings(difference),
              "explicit_two_point_leaf_family": list(map(str, family)),
              "explicit_family_each_mark_intensity": str(sp.factor(family_intensities[0])),
              "generic_two_point_leaf_family": list(map(str, general_family)),
              "exact_jacobian_ranks": {"one_point_complete": clean(jac_two[:4, :].subs(triangle_subs)).rank(),
                                       "two_points_complete": 6, "two_points_leaf": 5, "three_points_leaf": 6,
                                       "two_point_leaf_null_tangent_user_order": list(map(str, tangent))},
              "one_point_complete_counterexample": {"first": list(map(str, one_first)),
                                                    "second": list(map(str, one_second)), "data_at_1": strings(one_data)},
              "calibration": "Leaf pair distinguished by r, absolute stationary mark intensities, trace, or a third positive transform. Both have s=1, normalized mark proportions (1/2,1/2), entropy=0. No full-law equivalence is claimed.",
              "empirical_TV_and_moment_rectangle": "Analytic measure-theoretic and martingale arguments in LAPLACE-TWO.md; not claims certified by this symbolic script."}
    path = Path("outputs/correctness-2026-09-15/laplace-two.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"all_exact_checks_passed": True, "output": str(path),
                      "generic_two_point_reconstruction": list(map(str, recovered)),
                      "leaf_difference_at_3": strings(difference.subs(lam, 3))}, indent=2))


if __name__ == "__main__":
    main()
