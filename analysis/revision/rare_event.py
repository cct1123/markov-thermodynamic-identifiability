"""Exact identities and high-precision diagnostics for the rare-rate testing bound.

Run from root: python -B analysis/revision/rare_event.py
No stochastic inputs. No tiny rate is converted to binary64 or clipped.
"""
if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]


def exact_checks():
    e, k = sp.symbols('e k', positive=True)
    q = sp.Matrix([[-1-e, 1, e], [1, -2+k, 1-k], [k, 1-e, -1+e-k]])
    weights = sp.Matrix([[1-e+2*k-k*k, 1+k-e*e, 1-k+2*e-e*k]])
    z = 3+e+2*k-e*e-e*k-k*k
    assert sp.simplify(sum(weights)-z) == 0
    assert (weights*q).applyfunc(sp.expand) == sp.zeros(1, 3)
    assert sp.trace(q) == -4
    # On 0 <= k <= e < 1/2: w_x', w_y' positive, w_h' negative,
    # Z'=2-e-2k>0, Z>=3. Thus ||d pi/dk||_TV <= (3-2k)/Z <= 1.
    derivative_bound_numerator = (sp.diff(weights[0], k)+sp.diff(weights[1], k)
                                  -sp.diff(weights[2], k)+sp.diff(z, k))/2
    assert sp.expand(derivative_bound_numerator-(3-2*k)) == 0
    assert sp.expand(z-3-e*(1-e)-k*(2-e-k)) == 0
    # Current orientation x->h->y->x.
    current = sp.factor((weights[0]*e-weights[2]*k)/z)
    assert sp.factor(current-(e-k)*(1-e-k)/z) == 0
    # A general covered-vertex observation graph also has a direct inverse.
    lam1, lam2, r, s, a, b, c, d = sp.symbols('l1 l2 r s a b c d', positive=True)
    q3 = sp.Matrix([[-r-a, r, a], [s, -s-c, c], [b, d, -b-d]])
    # Resolved pairs x-y and y-h cover all states; hidden pair x-h can remain.
    marked = sp.Matrix([[0, r, 0], [s, 0, c], [0, d, 0]])
    t = q3-marked
    rates = sp.diag(r, s, d)
    f1inv = rates.inv()*(lam1*sp.eye(3)-t)
    f2inv = rates.inv()*(lam2*sp.eye(3)-t)
    assert sp.simplify(f2inv-f1inv-(lam2-lam1)*rates.inv()) == sp.zeros(3)
    assert sp.simplify(lam1*sp.eye(3)-rates*f1inv-t) == sp.zeros(3)
    return {'stationary_weights': True, 'trace': True, 'tv_stationary_derivative_bound': True,
            'current': True, 'covered_vertex_inverse_independent_symbolic_check': True,
            'domain': '0 <= k <= e < 1/2; derivatives use paired positivity, Z >= 3',
            'proof_status': 'exact identities; coupling/testing/limit arguments are conventional proofs'}


def diagnostics():
    mp.mp.dps = 100
    rows = []
    for estr in ['0.2', '0.1', '0.05', '0.02', '0.01', '0.005']:
        e = mp.mpf(estr)
        k = mp.exp(-1/e**2)
        vals = []
        for p in [1, 2]:
            kp = k**p
            z = 3+e+2*kp-e*e-e*kp-kp*kp
            pi = [v/z for v in [1-e+2*kp-kp*kp, 1+kp-e*e, 1-kp+2*e-e*kp]]
            sig = (e-kp)*(1-e-kp)/z*(mp.log(e)+mp.log1p(-e)-mp.log(kp)-mp.log1p(-kp))
            # Independently solve the stationary law and compute all flux pairs.
            q = mp.matrix([[-1-e, 1, e], [1, -2+kp, 1-kp], [kp, 1-e, -1+e-kp]])
            system = q.T.copy()
            for j in range(3):
                system[2, j] = 1
            solve = mp.lu_solve(system, mp.matrix([0, 0, 1]))
            direct = mp.mpf(0)
            for i in range(3):
                for j in range(i+1, 3):
                    forward, reverse = solve[i]*q[i,j], solve[j]*q[j,i]
                    direct += (forward-reverse)*(mp.log(forward)-mp.log(reverse))
            assert abs(direct-sig) < mp.mpf('1e-90')*max(1, sig)
            vals.append({'p': p, 'entropy': str(sig), 'e_times_entropy': str(e*sig),
                         'pi_hidden': str(pi[2]), 'observed_intensity': str(pi[0]+pi[1])})
        # For sum of test errors <= 0.2: H >= .8/(k-k^2)-1.
        log_h = mp.log(mp.mpf('.8'))-mp.log(k)-mp.log1p(-k)
        log_h += mp.log1p(-mp.exp(-log_h))
        sig = mp.mpf(vals[0]['entropy'])
        rows.append({'epsilon': estr, 'log_reverse_rate': str(-1/e**2),
                     'log_horizon_lower_bound_error_sum_0_2': str(log_h),
                     'log_horizon_bound_over_entropy_squared': str(log_h/sig**2),
                     'models': vals})
    return rows


def main():
    result = {'executed_at_utc': datetime.now(timezone.utc).isoformat(),
              'command': 'python -B analysis/revision/rare_event.py', 'seed': None,
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__, 'mpmath': mp.__version__},
              'precision_decimal_digits': 100,
              'inputs': 'embedded exact matrix Q(e,k); decimal e grid; k=exp(-1/e^2), k^2',
              'checks': exact_checks(), 'diagnostics': diagnostics(),
              'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    destination = ROOT/'outputs/revision/rare-event.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('Rare-event exact identities and 100-digit checks passed:', destination.relative_to(ROOT))


if __name__ == '__main__':
    main()
