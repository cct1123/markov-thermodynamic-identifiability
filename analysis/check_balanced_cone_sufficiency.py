"""Exact interval checks for the strict balanced-cone construction.

Run: .\.venv\Scripts\python.exe -B analysis/check_balanced_cone_sufficiency.py
Preserves the previously accepted exclusion checker and its output.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp

from check_balanced_cone_bound import (
    add, mul, polynomial_interval, interval_json, constant_interval,
)


def neg(x):
    return -x[1], -x[0]


def sub(x,y):
    return add(x,neg(y))


def div(x,y):
    assert y[0]*y[1] > 0
    return mul(x,(1/y[1],1/y[0]))


def scalar(value):
    value = F(value)
    return value,value


def main():
    z = sp.Symbol("z",real=True)
    rho = sp.sqrt(6)
    A = z
    ry = 4*(rho-1)/5
    B = z/ry
    L = (3-rho/2)/8
    R = 35*rho/88
    m = (7+2*rho)/5
    k = (2*z-9+2*rho)/(4*rho)
    a = k-1
    J = a*m+k
    f = [A*R*m/L-B*J**2,
         A*(R/L+k-a*m)+L*J**2+R*J-2*B*J*a,
         a*(L*J+R-A*(1+L*k/R)-B*a)]
    f = [sp.expand(sp.radsimp(sp.simplify(v))) for v in f]
    zi = (F("10.5"),F("10.55714966867"))
    ri = (F("2.449489742783178"),F("2.449489742783179"))
    assert ri[0]**2 < 6 < ri[1]**2
    fi = [polynomial_interval(v,z,zi,rho,ri) for v in f]
    assert fi[1][0] > 0 and fi[2][1] < 0
    ci = lambda value: constant_interval(value,rho,ri)
    Li, Ri, mi = [ci(v) for v in (L,R,m)]
    Ai = zi
    Bi = polynomial_interval(sp.expand(sp.radsimp(B)),z,zi,rho,ri)
    ki = polynomial_interval(sp.expand(sp.radsimp(k)),z,zi,rho,ri)
    ai = sub(ki,scalar(1))
    Ji = add(mul(ai,mi),ki)
    ti = div(neg(fi[1]),mul(scalar(2),fi[2]))
    eps = div(mul(mul(Li,ti),add(Ji,mul(ai,ti))),
              add(mul(Ri,mi),mul(add(mul(ki,Li),Ri),ti)))
    di = sub(scalar(1),eps)
    Wi = mul(Ri,eps)
    ell = add(mi,ti)
    Pi = mul(Li,ti)
    cr = mul(div(ki,ai),add(di,div(mul(Wi,eps),add(Ai,Wi))))
    Qi = div(add(mul(Ai,di),Wi),mul(ai,eps))
    left_slope = div(add(Pi,Wi),add(ell,di))
    margins = {
        "t_positive": ti,
        "epsilon_positive": eps,
        "one_minus_epsilon_positive": di,
        "right_abscissa_minus_one": sub(cr,scalar(1)),
        "bottom_left_output": sub(mul(Li,add(mi,di)),Wi),
        "right_right_output": sub(Qi,mul(Ri,sub(cr,scalar(1)))),
        "input_B_above_left_lower": sub(add(Bi,Wi),mul(left_slope,add(di,mi))),
        "input_A_below_upper": sub(div(add(mul(sub(cr,scalar(1)),Pi),
                                              mul(add(ell,scalar(1)),Qi)),add(ell,cr)),Ai),
        "left_origin_margin_via_tangency": mul(ai,Pi),
        "right_origin_margin_via_tangency": mul(ai,Qi),
        "bottom_left_invariance_via_tangency": mul(ai,add(Wi,Pi)),
        "bottom_right_invariance_via_tangency": mul(ai,add(Wi,Qi)),
    }
    assert all(v[0] > 0 for v in margins.values())
    # Remaining strict inequalities have manifest signs: P,Q,L,R,ell,c>0;
    # input A's other lower face and input B's right lower face are negative;
    # the two upper-face inward derivatives have positive coefficients.
    assert Pi[0] > 0 and Qi[0] > 0 and ai[0] > 0

    # Independent symbolic identities behind the origin/bottom checks.
    ap, lp, dp, pp, wp = sp.symbols("a ell d P W",positive=True)
    kp = ap+1
    tangent_w = pp*(ap*lp+kp*dp)/lp
    slope = (pp+tangent_w)/(lp+dp)
    assert sp.cancel(tangent_w-slope*dp-ap*pp) == 0
    assert sp.cancel(kp*tangent_w-slope*dp-ap*(tangent_w+pp)) == 0

    files = [Path(__file__),Path(__file__).with_name("check_balanced_cone_bound.py"),
             Path(__file__).with_name("balanced-cone-bound.md")]
    result = {
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "command_from_root": r".\.venv\Scripts\python.exe -B analysis/check_balanced_cone_sufficiency.py",
        "environment": {"python": platform.python_version(),"sympy":sp.__version__,
                        "platform":platform.platform()},
        "source_sha256": {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
        "method": "Rational outward interval arithmetic with a rational sqrt(6) enclosure; no finite parameter sampling",
        "parameter_enclosure": interval_json(zi),
        "scope": "Geometric strict margins hold on the entire enclosure. Top-input-B slack additionally requires z<z_star, proved from the discriminant sign; it is zero at z_star.",
        "f_intervals": [interval_json(v) for v in fi],
        "triangle_coordinates_enclosures": {name:interval_json(v) for name,v in
            {"t":ti,"epsilon":eps,"d":di,"W":Wi,"ell":ell,"P":Pi,"c":cr,"Q":Qi}.items()},
        "strict_geometric_margins": {name:interval_json(v) for name,v in margins.items()},
        "tangency_origin_and_bottom_identities_exactly_zero": True,
        "proof_status": "Exact interval support for the analytic construction and continuity perturbation. Not formal verification.",
        "all_checks_passed": True,
    }
    output = Path(__file__).with_name("balanced-cone-sufficiency-checks.json")
    output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"all_checks_passed":True,"output":str(output),
                      "strict_margin_count":len(margins)},indent=2))


if __name__ == "__main__":
    main()
