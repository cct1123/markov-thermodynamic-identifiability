"""Deterministic independent checks of three-state precision counterexamples.

Run from root: .venv/Scripts/python.exe -B analysis/check_three_state_precision.py
Writes outputs/three-state-precision-checks.json. No external data or search.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp
import sympy as s


def zero(expr):
    return s.cancel(expr) == 0


def clean(matrix):
    return matrix.applyfunc(s.factor)


def strings(matrix):
    return [[str(x) for x in matrix.row(i)] for i in range(matrix.rows)]


def kernel(q):
    t = q.copy()
    t[0, 1] = t[1, 0] = 0
    r = s.Matrix([[0, 1, 0], [1, 0, 0]])
    b = s.Matrix([[q[0, 1], 0], [0, q[1, 0]], [0, 0]])
    return t, r, b


def main():
    e, k = s.symbols("epsilon kappa", positive=True)
    tree = s.Matrix([[-1, 1, 0], [1, -2, 1], [0, 1, -1]])
    q_rare = s.Matrix([[-1-e, 1, e], [1, -1-e, e], [k, 1, -1-k]])
    q_added = s.Matrix([[-1-e, 1, e], [1, -2, 1], [k, 1, -1-k]])
    q_fixed = s.Matrix([[-1-e, 1, e], [1, -2+k, 1-k], [k, 1-e, -1+e-k]])
    z = 3+e+2*k-e**2-e*k-k**2
    families = {
        "rare_hidden_state": (q_rare, s.Matrix([[1+k+e*k, 1+k+e, e*(2+e)]])/
                              ((2+e)*(1+k+e)), e*(1-k)/((2+e)*(1+k+e)), 1/k),
        "added_tree_edge": (q_added, s.Matrix([[1+2*k, 1+e+k, 1+2*e]])/
                            (3*(1+e+k)), (e-k)/(3*(1+e+k)), e/k),
        "fixed_trace_tree": (q_fixed, s.Matrix([[1-e+2*k-k**2, 1+k-e**2, 1-k+2*e-e*k]])/z,
                             (e-k)*(1-e-k)/z, e*(1-e)/(k*(1-k)))
    }
    symbolic = {}
    numeric = []
    for label, (q, pi, current, ratio) in families.items():
        assert clean(q*s.ones(3, 1)) == s.zeros(3, 1)
        assert clean(pi*q) == s.zeros(1, 3) and zero(sum(pi)-1)
        # The same oriented cycle x->h->y->x supports every current.
        for i, j in ((0, 2), (2, 1), (1, 0)):
            assert zero(pi[i]*q[i, j]-pi[j]*q[j, i]-current)
        direct_ratio = s.prod(pi[i]*q[i, j]/(pi[j]*q[j, i])
                              for i, j in ((0, 2), (2, 1), (1, 0)))
        assert zero(direct_ratio-ratio)
        t, r, b = kernel(q)
        # These particular nonzero minors certify full linear order.
        controllability = s.Matrix.hstack(b, t*b[:, 1])
        observability = s.Matrix.vstack(r, (r*t)[1 if label == "rare_hidden_state" else 0, :])
        dc, do = s.factor(controllability.det()), s.factor(observability.det())
        assert dc != 0 and do != 0
        if label == "fixed_trace_tree":
            assert s.trace(q) == s.trace(tree) == -4
            assert zero(pi[2]-s.Rational(1, 3)-(e-k)*(5+e-k)/(3*z))
            assert zero(pi[0]-s.Rational(1, 3)-(k-e)*(4-e-2*k)/(3*z))
            assert zero(pi[1]-s.Rational(1, 3)-(k-e)*(1+2*e+k)/(3*z))
        symbolic[label] = {"q": strings(q), "stationary": strings(pi),
                           "cycle_current": str(current), "cycle_rate_ratio": str(ratio),
                           "trace": str(s.trace(q)), "rank_minors": [str(dc), str(do)]}

        for n in (2, 5, 10, 20, 50):
            ctx = mp.mp.clone()
            ctx.dps = 100
            ev, kv = ctx.mpf(1)/n, ctx.exp(-n*n)
            convert = s.lambdify((e, k), q, modules="mpmath")
            # lambdify uses mpmath's global context; evaluate at the same precision.
            with mp.workdps(100):
                a = convert(ev, kv)
            a = ctx.matrix(a)
            assert all(0 < a[i, j] <= 1 for i in range(3) for j in range(3) if i != j)
            system = ctx.matrix([[a[j, i] for j in range(3)] for i in range(2)]
                                + [[1, 1, 1]])
            p = ctx.lu_solve(system, ctx.matrix([0, 0, 1]))
            assert all(v > 0 for v in p)
            direct = ctx.mpf(0)
            for i in range(3):
                for j in range(i+1, 3):
                    f, rev = p[i]*a[i, j], p[j]*a[j, i]
                    direct += (f-rev)*(ctx.log(f)-ctx.log(rev))
            with mp.workdps(100):
                expected_current = s.lambdify((e, k), current, "mpmath")(ev, kv)
                expected_ratio = s.lambdify((e, k), ratio, "mpmath")(ev, kv)
            expected = expected_current*ctx.log(expected_ratio)
            assert abs(direct-expected) < ctx.mpf("1e-80")*max(1, abs(expected))
            numeric.append({"family": label, "n": n, "epsilon": str(ev),
                            "log_kappa": str(-n*n), "entropy_100dps": str(direct),
                            "epsilon_times_entropy": str(ev*direct),
                            "formula_residual": str(abs(direct-expected)),
                            "stationary_solve": [str(v) for v in p]})

    tt, r, b = kernel(tree)
    assert -tt.inv()*s.ones(3, 1) == s.Matrix([1, 2, 3])
    assert s.Matrix.hstack(b, tt*b[:, 1]).det() != 0
    assert s.Matrix.vstack(r, (r*tt)[0, :]).det() != 0

    # Closed-generator reconstruction used in the positive-triangle continuity proof.
    a, b0, c, d, h, f = s.symbols("a b c d h f", positive=True)
    generic = s.Matrix([[-a-c, a, c], [b0, -b0-d, d], [h, f, -h-f]])
    tg, _, _ = kernel(generic)
    assert zero((tg**2)[0, 0]-(a+c)**2-c*h)
    assert zero((tg**2)[0, 1]-c*f)
    assert zero((tg**2)[1, 0]-d*h)
    assert zero((tg**2)[1, 1]-(b0+d)**2-d*f)

    result = {"all_checks_passed": True,
              "kind": "exact identities and independent high-precision stationary solve; conventional limit proofs are in the notes",
              "executed_at_utc": datetime.now(timezone.utc).isoformat(),
              "command": ".venv/Scripts/python.exe -B analysis/check_three_state_precision.py",
              "environment": {"python": platform.python_version(), "sympy": s.__version__,
                              "mpmath": mp.__version__, "platform": platform.platform()},
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "inputs": "Explicit q matrices; 0<kappa<epsilon<1/2 for tree families. Numerical endpoint epsilon=1/2 is also strictly admissible. No data or random input.",
              "symbolic_families": symbolic, "independent_numeric_cases": numeric,
              "tree_source_rank": 3, "tree_source_mean_next_event": [1, 2, 3],
              "generic_three_state_reconstruction_checked": True,
              "limitations": "Numerical convergence examples are not proofs of divergence or continuity. Coupling, compactness and exact asymptotic arguments are documented in the corresponding audits. No novelty or formal-proof claim."}
    destination = Path("outputs/three-state-precision-checks.json")
    destination.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"all_checks_passed": True, "numeric_cases": len(numeric),
                      "source_tree_rank": 3, "output": str(destination),
                      "rank_minors": {name: value["rank_minors"] for name, value in symbolic.items()}}, indent=2))


if __name__ == "__main__":
    main()
