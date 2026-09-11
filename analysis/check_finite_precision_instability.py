"""Exact four-state witness for finite-precision entropy instability.

Run from root: .venv/Scripts/python.exe -B analysis/check_finite_precision_instability.py
No search or random inputs. Writes only outputs/finite-precision-checks.json.
The continuum and confidence-bound arguments are in finite-precision-instability.md.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import quad_vec
from scipy.linalg import expm
import sympy as sp


def clean(matrix):
    return matrix.applyfunc(sp.factor)


def strings(matrix):
    return [[str(x) for x in matrix.row(i)] for i in range(matrix.rows)]


def kernel_data(q):
    killed = q.copy()
    killed[0, 1] = killed[1, 0] = 0
    reset = sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0]])
    output = sp.Matrix([[1, 0], [0, 1], [0, 0], [0, 0]])
    return killed, reset, output


def number(ctx, x):
    return ctx.mpf(int(x.p)) / int(x.q)


def main():
    epsilon, t = sp.symbols("epsilon t", positive=True)
    q0 = sp.Matrix([[-2, 1, 1, 0], [1, -2, 0, 1],
                    [1, 0, -2, 1], [0, 1, 1, -2]])
    c = sp.Matrix([[-1, 0, 0, 1], [0, -1, 1, 0],
                   [0, 1, -1, 0], [1, 0, 0, -1]])
    qe = q0 + epsilon*c
    s = sp.eye(4)
    s[2, 2], s[2, 3] = 1-t, t
    target = clean(s.inv()*qe*s)
    pi = sp.Matrix([[1, 1, 1-t, 1+t]])/4
    assert clean(target*sp.ones(4, 1)) == sp.zeros(4, 1)
    assert clean(pi*target) == sp.zeros(1, 4)
    assert clean(pi-sp.ones(1, 4)*s/4) == sp.zeros(1, 4)
    assert sp.trace(target) == sp.trace(qe) == -8-4*epsilon
    te, reset, output = kernel_data(qe)
    tt, _, _ = kernel_data(target)
    assert clean(s*tt-te*s) == sp.zeros(4)
    assert reset*s == reset and s*output == output and s*sp.ones(4, 1) == sp.ones(4, 1)
    for i, j in ((0, 1), (1, 0)):
        mark = sp.zeros(4)
        mark[i, j] = 1
        assert mark*s == s*mark

    t0, _, _ = kernel_data(q0)
    controllability = sp.Matrix.hstack(*[t0**k*output for k in range(4)])
    observability = sp.Matrix.vstack(*[reset*t0**k for k in range(4)])
    assert controllability.rank() == observability.rank() == 4
    path_delay = [(t0**k)[0, 1] for k in range(4)]
    assert path_delay == [0, 0, 0, 1]
    mean_times = -t0.inv()*sp.ones(4, 1)
    assert mean_times == sp.Matrix([2, 2, 3, 3])

    flux = clean(sp.diag(*list(pi))*target)
    current = clean(flux-flux.T)
    j = t*(1-epsilon)/4
    expected = sp.Matrix([[0, 0, -j, j], [0, 0, j, -j],
                          [j, -j, 0, 0], [-j, j, 0, 0]])
    assert clean(current-expected) == sp.zeros(4)
    ratio = ((flux[2, 0]/flux[0, 2])*(flux[0, 3]/flux[3, 0])
             *(flux[1, 2]/flux[2, 1])*(flux[3, 1]/flux[1, 3]))
    expected_ratio = (1-epsilon*t)*(epsilon+t)/((epsilon-t)*(1+epsilon*t))
    assert sp.cancel(ratio-expected_ratio) == 0
    assert target[2, 1].subs(t, epsilon) == 0
    boundary_reverse = sp.factor(flux[1, 2].subs(t, epsilon))
    assert sp.cancel(boundary_reverse-epsilon*(1-epsilon)/4) == 0
    # The only rate with a potentially large denominator is bounded exactly:
    assert sp.cancel(1+epsilon-target[2, 0]-(epsilon-t)/(1-t)) == 0

    rational_checks = []
    ctx = mp.mp.clone()
    ctx.dps = 100
    for e in (sp.Rational(1, 4), sp.Rational(1, 100), sp.Rational(1, 1000)):
        base = qe.subs(epsilon, e)
        for digits in (1, 3, 8, 20):
            u = e*(1-sp.Rational(1, 10**digits))
            values = {epsilon: e, t: u}
            q = target.subs(values)
            p = pi.subs(values)
            assert all(0 < q[i, k] <= 1+e for i in range(4) for k in range(4) if i != k)
            assert all(x > 0 for x in p) and sum(p) == 1 and p*q == sp.zeros(1, 4)
            killed, _, _ = kernel_data(q)
            original, _, _ = kernel_data(base)
            # Direct powers are an independent finite all-time certificate.
            for k in range(8):
                assert reset*killed**k*output == reset*original**k*output
            entropy = ctx.mpf(0)
            for i in range(4):
                for k in range(i+1, 4):
                    f, r = number(ctx, p[i]*q[i, k]), number(ctx, p[k]*q[k, i])
                    entropy += (f-r)*(ctx.log(f)-ctx.log(r))
            formula = number(ctx, j.subs(values))*ctx.log(number(ctx, expected_ratio.subs(values)))
            assert abs(entropy-formula) < ctx.mpf("1e-75")
            rational_checks.append({"epsilon": str(e), "t": str(u), "gap_digits": digits,
                                    "entropy_100dps": str(entropy),
                                    "formula_residual": str(abs(entropy-formula)),
                                    "max_rate": str(max(q[i, k] for i in range(4)
                                                        for k in range(4) if i != k))})

    numerical_tv = []
    a0 = np.array(t0).astype(float)
    for e in (sp.Rational(1, 4), sp.Rational(1, 100), sp.Rational(1, 1000)):
        ae = np.array(te.subs(epsilon, e)).astype(float)
        # Swapping reset/mark order does not affect the maximum row TV.
        def integrand(time):
            return np.abs(expm(ae*time)[:2, :2]-expm(a0*time)[:2, :2]).sum(axis=1)/2
        integral, error = quad_vec(integrand, 0, np.inf, epsabs=1e-10, epsrel=1e-10)
        assert max(integral)+error < 2*float(e)
        numerical_tv.append({"epsilon": str(e), "row_tv_quadrature": integral.tolist(),
                             "quadrature_error_estimate": float(error),
                             "analytic_coupling_upper_bound": str(2*e)})

    result = {"kind": "exact witness and numerical cross-check; no optimizer or formal proof",
              "executed_at_utc": datetime.now(timezone.utc).isoformat(),
              "command": ".venv/Scripts/python.exe -B analysis/check_finite_precision_instability.py",
              "environment": {"python": platform.python_version(), "sympy": sp.__version__,
                              "mpmath": mp.__version__, "numpy": np.__version__, "scipy": scipy.__version__,
                              "platform": platform.platform()},
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "assumptions": "0 < epsilon < 1/2; 0 <= t < epsilon; unknown bidirected topology; exactly four states; only x<->y observed; stationary finite-horizon sampling for statistical corollary",
              "q0": strings(q0), "perturbation_C": strings(c), "target": strings(target),
              "stationary": strings(pi), "current": strings(current),
              "source_minimal_ranks": [4, 4], "source_path_delay_derivatives": list(map(str, path_delay)),
              "source_mean_next_event_times": list(map(str, mean_times)),
              "exact_similarity_and_stationary_observed_path_identities": True,
              "entropy_formula": str(j)+" * log("+str(expected_ratio)+")",
              "divergence_coefficient": str(boundary_reverse),
              "uniform_rate_bound": "all off-diagonal rates <= 1+epsilon < 3/2",
              "kernel_tv_bound": "2*epsilon, analytically from extra-jump coupling",
              "stationary_observed_record_tv_bound": "epsilon*H for every fixed physical horizon H",
              "rational_and_high_precision_cases": rational_checks,
              "numerical_tv_cross_checks": numerical_tv,
              "limitation": "Quadrature and high precision are diagnostics. Continuum inequalities, divergence and uniform-confidence impossibility use the accompanying conventional proof. No novelty or formal-verification claim.",
              "failed_attempts": ["Initial run stopped at a structural SymPy equality comparing differently factored versions of epsilon*(1-epsilon)/4. Replaced this and the analogous rate-cap assertion by exact rational-function difference checks; no mathematical formula changed."],
              "all_checks_passed": True}
    destination = Path("outputs/finite-precision-checks.json")
    destination.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"all_checks_passed": True, "output": str(destination),
                      "rational_cases": len(rational_checks), "tv_cross_checks": numerical_tv}, indent=2))


if __name__ == "__main__":
    main()
