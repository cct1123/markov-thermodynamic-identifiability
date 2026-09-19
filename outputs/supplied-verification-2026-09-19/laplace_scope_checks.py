"""Independent bounded Laplace-scope audit; imports no repository modules.

Run from project root:
.venv/Scripts/python.exe -B outputs/supplied-verification-2026-09-19/laplace_scope_checks.py
"""
if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import sympy as s


def eq(left, right):
    difference = left - right
    if isinstance(difference, s.MatrixBase):
        assert all(s.cancel(x) == 0 for x in difference), difference
    else:
        assert s.cancel(difference) == 0, difference


def q3(r, t, a, b, c, d):
    return s.Matrix([[-r-a, r, a], [t, -t-c, c], [b, d, -b-d]])


def first_step(q, lam):
    """Solve the backward first-step equations for next-mark tests."""
    killed = q.copy()
    killed[0, 1] = killed[1, 0] = 0
    rhs = s.zeros(q.rows, 2)
    rhs[0, 0], rhs[1, 1] = q[0, 1], q[1, 0]
    solved = (lam*s.eye(q.rows)-killed).inv(method="DM")*rhs
    # F is ordered by starting physical state (x,y), not previous mark.
    return solved[:2, :].applyfunc(s.cancel)


def stationarity(q):
    mat = q.T.copy()
    mat[-1, :] = s.ones(1, q.rows)
    rhs = s.zeros(q.rows, 1)
    rhs[-1] = 1
    pi = (mat.inv(method="DM")*rhs).applyfunc(s.cancel)
    eq(q.T*pi, s.zeros(q.rows, 1))
    eq(sum(pi), 1)
    return pi, s.diag(*pi)*q


def entropy(q):
    pi, flux = stationarity(q)
    answer = 0
    for i in range(q.rows):
        for j in range(i+1, q.rows):
            if q[i,j] != 0:
                assert q[j,i] != 0
                answer += s.cancel(flux[i,j]-flux[j,i])*s.log(s.cancel(flux[i,j]/flux[j,i]))
    return s.expand_log(s.simplify(answer), force=True), pi


def stringify(matrix):
    return [[str(x) for x in matrix.row(i)] for i in range(matrix.rows)]


def main():
    r, t, a, b, c, d, lam, l1, l2 = s.symbols("r s a b c d lambda lambda_1 lambda_2", positive=True)
    q = q3(r, t, a, b, c, d)
    f = first_step(q, lam)
    m = f.inv(method="DM").applyfunc(s.cancel)
    h = b+d
    eq(m[0,1], -a*d/(r*(lam+h)))
    eq(m[1,0], -c*b/(t*(lam+h)))
    g = ((m*s.ones(2,1)-s.ones(2,1))/lam).applyfunc(s.cancel)
    eq(g, s.Matrix([1/r+a/(r*(lam+h)), 1/t+c/(t*(lam+h))]))
    # Clearing the two off-diagonal denominators determines h linearly.
    m1, m2 = m.subs(lam,l1), m.subs(lam,l2)
    recovered_h = s.cancel((l2*m2[0,1]-l1*m1[0,1])/(m1[0,1]-m2[0,1]))
    eq(recovered_h, h)
    delta = (g.subs(lam,l1)-g.subs(lam,l2))/(l2-l1)
    recovered_v = (delta*(l1+recovered_h)*(l2+recovered_h)).applyfunc(s.cancel)
    recovered_u = (g.subs(lam,l1)-recovered_v/(l1+recovered_h)).applyfunc(s.cancel)
    eq(recovered_u,s.Matrix([1/r,1/t]))
    eq(recovered_v,s.Matrix([a/r,c/t]))
    recovered_d = s.cancel(-m1[0,1]*(l1+recovered_h)/recovered_v[0])
    eq(recovered_d,d)
    eq(recovered_h-recovered_d,b)

    strata = {
        "x_leaf": q3(r,t,a,b,0,0),
        "y_leaf": q3(r,t,0,0,c,d),
        "two_state": s.Matrix([[-r,r],[t,-t]])
    }
    for name, model in strata.items():
        fs = first_step(model,lam)
        eq(fs[0,1],0)
        eq(fs[1,0],0)
        pi, flux = stationarity(model)
        eq(flux,flux.T)

    # Strongest simple attempted extension: zero cross tests beyond the cap.
    q4 = s.Matrix([[-4,1,2,1],[1,-1,0,0],[1,0,-3,2],[2,0,1,-3]])
    f4 = first_step(q4,lam)
    eq(f4[0,1],0)
    eq(f4[1,0],0)
    sigma4, pi4 = entropy(q4)
    eq(pi4,s.ones(4,1)/4)
    eq(sigma4,3*s.log(2)/4)

    # A bounded additional check: one positive argument can miss entropy.
    qa = q3(1,1,1,1,2,1)
    qb = q3(s.Rational(9,11),1,s.Rational(5,11),1,s.Rational(10,3),3)
    fa, fb = first_step(qa,1), first_step(qb,1)
    eq(fa,fb)
    expected_f = s.Matrix([[s.Rational(5,13),s.Rational(1,26)],
                           [s.Rational(1,13),s.Rational(4,13)]])
    eq(fa,expected_f)
    sigma_a, pi_a = entropy(qa)
    sigma_b, pi_b = entropy(qb)
    eq(sigma_a,s.log(2)/12)
    eq(sigma_b,9*s.log(2)/110)
    eq(sigma_a-sigma_b,s.log(2)/660)
    # Stationary cycle current agrees with the independent product formula.
    for model, pi, expected in ((qa,pi_a,s.Rational(1,12)),(qb,pi_b,s.Rational(9,110))):
        eq(pi[0]*model[0,1]-pi[1]*model[1,0],expected)
    assert first_step(qa,2) != first_step(qb,2)

    out = {
        "all_exact_checks_passed": True,
        "executed_at_utc":datetime.now(timezone.utc).isoformat(),
        "command":".venv/Scripts/python.exe -B outputs/supplied-verification-2026-09-19/laplace_scope_checks.py",
        "environment":{"python":platform.python_version(),"sympy":s.__version__},
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "method":"Exact first-step equations and independent stationary-flux solve; no project imports; shared SymPy engine with project checks.",
        "randomness":"none",
        "precision":"exact rational and symbolic arithmetic; no tolerance",
        "generic_domain":"All six rates positive; lambda_2>lambda_1>0; distinctness imposed in rational identities.",
        "generic_inverse_cross_entries":[str(m[0,1]),str(m[1,0])],
        "generic_recovered_h":str(recovered_h),
        "generic_recovered_u":list(map(str,recovered_u)),
        "generic_recovered_v":list(map(str,recovered_v)),
        "symbolic_zero_entropy_strata":list(strata),
        "outside_cap_zero_cross_positive_entropy":{"Q":stringify(q4),"F":stringify(f4),"pi":list(map(str,pi4)),"entropy":str(sigma4)},
        "one_point_entropy_counterexample":{"Q_A":stringify(qa),"Q_B":stringify(qb),"common_F_at_1":stringify(fa),"pi_A":list(map(str,pi_a)),"pi_B":list(map(str,pi_b)),"sigma_A":str(sigma_a),"sigma_B":str(sigma_b),"gap":str(sigma_a-sigma_b),"F_at_2_differs":True},
        "limitations":"Not formal verification, not a novelty check, and not a complete audit of other supplied JSON fields. Outside-cap example refutes extension of the zero-pattern support classification; no claim that it matches a three-state law."
    }
    path=Path(__file__).with_name("laplace-scope-checks.json")
    path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"all_exact_checks_passed":True,"output":str(path)},indent=2))


if __name__ == "__main__":
    main()
