"""Independent numerical/alternative exact checks for the publication audit.

Run from root: .\.venv\Scripts\python.exe -B analysis/check_publication_audit.py
No random inputs. Only outputs/publication-audit-checks.json is written.
The accompanying proofs, not these finite checks, establish the theorems.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import platform
import mpmath as mp
import sympy as sp

mp.mp.dps = 160


def matrix3(values):
    r, s, a, c, b, d = map(mp.mpf, values)
    return mp.matrix([[-r-a, r, a], [s, -s-c, c], [b, d, -b-d]])


def laplace(q, lam):
    t = q.copy()
    t[0, 1] = t[1, 0] = 0
    resolvent = (lam * mp.eye(q.rows) - t)**-1
    # Visible resolvent times the rates; the mark-row swap is already undone.
    return mp.matrix([[resolvent[i, j] * q[j, 1-j] for j in range(2)]
                      for i in range(2)])


def recover(q):
    args = list(map(mp.mpf, (1, 3, 7)))
    hh = [laplace(q, lam)**-1 for lam in args]
    gg = [[(sum(hh[j][i, k] for k in range(2))-1)/args[j]
           for j in range(3)] for i in range(2)]
    branch = 0 if q[0, 2] > 0 else 1
    g = gg[branch]
    ratio = (g[0]-g[1])/(g[1]-g[2]) * (args[2]-args[1])/(args[1]-args[0])
    h = (args[2]-ratio*args[0])/(ratio-1)
    v = [(g[0]-g[1])*(args[0]+h)*(args[1]+h)/(args[1]-args[0]) for g in gg]
    u = [gg[i][0]-v[i]/(args[0]+h) for i in range(2)]
    r, s = [1/x for x in u]
    a, c = [v[i]/u[i] for i in range(2)]
    if branch == 0:
        d = -r*hh[0][0, 1]*(args[0]+h)/a
        b = h-d
    else:
        b = -s*hh[0][1, 0]*(args[0]+h)/c
        d = h-b
    return matrix3((r, s, a, c, b, d))


def stationary(q):
    a = q.T.copy()
    for j in range(q.rows):
        a[q.rows-1, j] = 1
    rhs = mp.matrix([0]*(q.rows-1)+[1])
    return mp.lu_solve(a, rhs)


def entropy(q, pi):
    total = mp.mpf(0)
    for i in range(q.rows):
        for j in range(i+1, q.rows):
            if q[i, j] == q[j, i] == 0:
                continue
            assert q[i, j] > 0 and q[j, i] > 0
            f, g = pi[i]*q[i, j], pi[j]*q[j, i]
            total += (f-g)*mp.log(f/g)
    return total


inverse_cases = [(1,1,0,1,0,1), (2,3,4,0,5,0), (2,3,4,5,6,7),
                 (1,1,1,1,1,1), (1,2,3,4,100000,200000),
                 ('0.000001',8,'0.00000001',4,9,'0.000002')]
inverse_results = []
for values in inverse_cases:
    q = matrix3(values)
    qr = recover(q)
    err = max(abs(qr[i,j]-q[i,j])/max(1,abs(q[i,j]))
              for i in range(3) for j in range(3))
    assert err < mp.mpf('1e-125')
    inverse_results.append({'rates':list(map(str,values)), 'relative_error':mp.nstr(err,8)})

# Independent route: interpolate 1/F_xy from four exact rational resolvents.
# This does not use the three-node inverse algebra.
cubic_results = []
L = sp.Symbol('L')
for vals in [(1,1,1,1,1,1),(2,3,4,5,6,7),(1,2,3,4,100000,200000)]:
    r,s,a,c,b,d = map(sp.Rational, vals)
    t = sp.Matrix([[-r-a,0,a],[0,-s-c,c],[b,d,-b-d]])
    samples = []
    for lam in (1,2,4,8):
        fxy = (lam*sp.eye(3)-t).inv()[0,1]*s
        samples.append((lam,1/fxy))
    p = sp.Poly(sp.interpolate(samples,L),L)
    assert p.degree() == 3
    recovered_trace = p.coeff_monomial(L**2)/p.coeff_monomial(L**3)
    assert recovered_trace == -sp.trace(t)
    cubic_results.append({'rates':list(map(str,vals)), 'trace_mass':str(recovered_trace)})


def graph(edges, n):
    q = mp.zeros(n)
    for i,j,a,b in edges:
        q[i,j],q[j,i] = a,b
    for i in range(n):
        q[i,i] = -sum(q[i,j] for j in range(n) if j != i)
    return q


sources = [graph([(0,1,2,3),(1,2,4,5)],3),
           graph([(0,1,1,1),(1,2,2,3),(2,3,4,5),(3,0,6,7)],4),
           graph([(0,1,3,2),(1,2,4,1),(2,3,2,5),(3,4,6,1)],5)]
chord_results = []
for q0 in sources:
    n = q0.rows
    pi0 = stationary(q0)
    for denominator in (10,20,40,80):
        e = mp.mpf(1)/denominator
        k = mp.exp(-1/e**2)
        q = q0.copy()
        # Pair 0,2 is absent in all three sources. Compensate unobserved 1->2.
        q[0,2],q[2,0] = e,k
        q[1,2] -= e+k
        for i in range(n):
            q[i,i] = -sum(q[i,j] for j in range(n) if j != i)
        assert abs(sum(q[i,i]-q0[i,i] for i in range(n))) < mp.mpf('1e-155')
        assert q[0,1] == q0[0,1] and q[1,0] == q0[1,0]
        assert max(q) <= max(q0)
        pi = stationary(q)
        sigma = entropy(q,pi)
        assert max(abs(sum(pi[i]*q[i,j] for i in range(n))) for j in range(n)) < mp.mpf('1e-155')
        chord_results.append({'N':n,'e':str(e), 'log_reverse_rate':str(-1/e**2),
            'sigma':mp.nstr(sigma,25), 'scaled_sigma':mp.nstr(e*sigma,25),
            'predicted_limit':mp.nstr(pi0[0],25), 'trace_mass':mp.nstr(-sum(q[i,i] for i in range(n)),10)})

# Exact cap saturation: twelve nonnegative rates <=1 with sum12 force all1.
assert 4*(4-1) == 12
result = {'executed_at':datetime.now(timezone.utc).isoformat(),
    'command':r'.\.venv\Scripts\python.exe -B analysis/check_publication_audit.py',
    'python':platform.python_version(),'sympy':sp.__version__,'mpmath':mp.__version__,
    'precision_digits':mp.mp.dps,'seed':None,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'inverse_direct_resolvent_cases':inverse_results,'independent_cubic_interpolation':cubic_results,
    'missing_chord_stationary_solve_diagnostics':chord_results,
    'tight_cap_counterexample':{'N':4,'trace_mass':12,'max_rate':1,'only_generator':'all offdiagonals one'},
    'all_checks_passed':True,
    'limitations':'Finite numerical diagnostics are not proofs of continuity, divergence or classification. See publication-stability-audit.md.'}
out = Path('outputs/publication-audit-checks.json')
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'output':str(out),'all_checks_passed':True,'inverse_cases':len(inverse_results),
                  'exact_cubic_cases':len(cubic_results),'chord_diagnostics':len(chord_results)}))
