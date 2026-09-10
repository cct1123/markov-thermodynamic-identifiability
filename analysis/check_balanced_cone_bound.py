"""Exact algebra and isolating intervals for balanced-cone-bound.md.

Run from root: .\.venv\Scripts\python.exe -B analysis/check_balanced_cone_bound.py
No search, randomness, or solver-based nonexistence claim.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp


def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def mul(x, y):
    choices = [a*b for a in x for b in y]
    return min(choices), max(choices)


def rational(value):
    value = sp.Rational(value)
    return F(int(value.p), int(value.q))


def constant_interval(value, rho, rho_interval):
    value = sp.expand(sp.radsimp(value))
    b = value.coeff(rho)
    a = sp.simplify(value-b*rho)
    assert a.is_Rational and b.is_Rational
    af, bf = rational(a), rational(b)
    return add((af, af), mul((bf, bf), rho_interval))


def polynomial_interval(expr, z, zi, rho, ri):
    result = (F(0), F(0))
    for coefficient in sp.Poly(sp.expand(expr), z).all_coeffs():
        result = add(mul(result, zi), constant_interval(coefficient, rho, ri))
    return result


def interval_json(value):
    return {"rational_endpoints": [str(x) for x in value],
            "decimal_endpoints_diagnostic": [float(x) for x in value]}


def main():
    A, B, k, m, L, R, t = sp.symbols("A B k m L R t", positive=True)
    a = k-1
    J = a*m+k
    # E/D is epsilon. Clear the explicitly positive denominators before
    # expansion rather than asking cancel() to rediscover their structure.
    E = L*t*(J+a*t)
    D = R*m+(k*L+R)*t
    upper_numerator = t*(L*m*a*E*(A*D+R*E)
                         +(A*D+(R+k*L)*E)*(A*D+(R-A)*E))
    upper_denominator = E*(a*(A*D+R*E)*(m+t)
                           +k*(A*D+(R-A)*E))
    generic_f = [A*R*m/L-B*J**2,
                 A*(R/L+k-a*m)+L*J**2+R*J-2*B*J*a,
                 a*(L*J+R-A*(1+L*k/R)-B*a)]
    polynomial_f = sum(value*t**i for i,value in enumerate(generic_f))
    assert sp.expand(upper_numerator*(J+a*t)**2
                     -(B*(J+a*t)**2+polynomial_f)*upper_denominator) == 0

    z = sp.Symbol("z", real=True)
    rho = sp.sqrt(6)
    ry = 4*(rho-1)/5
    constants = {A: z, B: z/ry, k: (2*z-9+2*rho)/(4*rho),
                 m: (7+2*rho)/5, L: (3-rho/2)/8, R: 35*rho/88}
    f = [sp.expand(sp.radsimp(sp.simplify(v.subs(constants)))) for v in generic_f]
    quartic = 352*z**4-3168*z**3-4644*z**2-11340*z-7623
    expected_f0 = -(19+9*rho)*z*(z**2-11*z+sp.Rational(211, 44))/100
    expected_disc = -(sp.Rational(11, 1200)+11*rho/4200)*(z+sp.Rational(19,22))**2*quartic/352
    assert sp.simplify(f[0]-expected_f0) == 0
    assert sp.expand(f[1]**2-4*f[0]*f[2]-expected_disc) == 0

    root_interval = (F("10.55714966866"), F("10.55714966867"))
    rho_interval = (F("2.449489742783178"), F("2.449489742783179"))
    assert rho_interval[0]**2 < 6 < rho_interval[1]**2
    root_signs = [rational(quartic.subs(z, sp.Rational(x.numerator, x.denominator)))
                  for x in root_interval]
    assert root_signs[0] < 0 < root_signs[1]
    signs = [1 if c > 0 else -1 for c in sp.Poly(quartic,z).all_coeffs()]
    assert sum(x != y for x,y in zip(signs,signs[1:])) == 1
    f_intervals = [polynomial_interval(v,z,root_interval,rho,rho_interval) for v in f]
    assert f_intervals[0][1] < 0
    assert f_intervals[1][0] > 0
    assert f_intervals[2][1] < 0

    z0 = sp.Rational(21,2)
    lv, rv, mv = [constants[x] for x in (L,R,m)]
    k0 = constants[k].subs(z,z0)
    apex_d = (rv-lv*mv)/(lv+rv)
    apex_epsilon = lv*(mv+1)/(lv+rv)
    apex_margin = sp.radsimp(sp.simplify(apex_epsilon-1/(k0-rv/z0)))
    apex_margin_interval = constant_interval(apex_margin,rho,rho_interval)
    apex_d_interval = constant_interval(apex_d,rho,rho_interval)
    assert apex_margin_interval[0] > 0
    assert apex_d_interval[0] > 0
    assert constant_interval(sp.radsimp(k0-1-sp.Rational(7,10)),rho,rho_interval)[0] > 0

    # The old local threshold lies below the new isolating interval: its
    # upward-opening quadratic is strictly positive and increasing there.
    old_quadratic = z**2-11*z+sp.Rational(211,44)
    old_interval = polynomial_interval(old_quadratic,z,root_interval,rho,rho_interval)
    assert old_interval[0] > 0 and 2*root_interval[0]-11 > 0

    local_files = [Path(__file__), Path(__file__).with_name("balanced-cone-bound.md"),
                   Path(__file__).with_name("theta-fast-spectral-audit.md"),
                   Path(__file__).with_name("theta-family-construction-audit.md")]
    result = {
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "command_from_root": r".\.venv\Scripts\python.exe -B analysis/check_balanced_cone_bound.py",
        "environment": {"python": platform.python_version(), "sympy": sp.__version__,
                        "platform": platform.platform()},
        "source_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in local_files},
        "inputs": "Exact embedded modal constants and symbolic generic envelope; no sampled data",
        "generic_envelope_identity": "upper-B=(f0+f1*t+f2*t^2)/(J+a*t)^2",
        "generic_identity_exactly_zero": True,
        "f_coefficients": [str(v) for v in f],
        "discriminant_factorization": str(expected_disc),
        "quartic": str(quartic),
        "positive_root_count_descartes_and_sign_change": 1,
        "root_isolating_interval": interval_json(root_interval),
        "quartic_at_isolating_endpoints": [str(v) for v in root_signs],
        "sqrt6_certified_interval": interval_json(rho_interval),
        "f_coefficient_intervals_at_root_interval": [interval_json(x) for x in f_intervals],
        "apex_margin_at_21_over_2": interval_json(apex_margin_interval),
        "apex_d": interval_json(apex_d_interval),
        "old_local_quadratic_at_root_interval": interval_json(old_interval),
        "proof_status": "Exact supporting algebra; universal inequality argument is in the note. Not formal verification.",
        "incomplete_attempts": ["Initial nested seven-variable cancel(upper-B-f/(J+a*t)^2) formulation was manually interrupted before producing output; replaced by the identical denominator-cleared polynomial identity. No scientific finding was produced by that attempt."],
        "all_checks_passed": True,
    }
    destination = Path(__file__).with_name("balanced-cone-bound-checks.json")
    destination.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"all_checks_passed": True, "output": str(destination),
                      "root_interval": [str(x) for x in root_interval]},indent=2))


if __name__ == "__main__":
    main()
