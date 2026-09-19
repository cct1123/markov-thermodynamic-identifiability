"""Independent exact checks for the graph extension, not a numerical proof.

Run from project root:
  .\.venv\Scripts\python.exe -B outputs/novelty-loop-2026-09-19/referee_checks.py
Inputs are the exact integer constructions below; no random inputs are used.
"""
if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

import hashlib
import json
import platform
from pathlib import Path

import sympy as s


def generator(n, sparse=False):
    q = s.zeros(n)
    for i in range(n):
        for j in range(n):
            if i != j and (not sparse or (i < n - 1 and j < n - 1) or {i, j} == {0, n - 1}):
                q[i, j] = 1 + ((i + 2) * (j + 3) % 7)
    for i in range(n):
        q[i, i] = -sum(q[i, j] for j in range(n) if j != i)
    return q


def recover_one_hidden(q, pairs):
    n = q.rows
    p = n - 1
    marks = [(i, j) for i, j in pairs for i, j in ((i, j), (j, i))]
    e = s.zeros(n)
    bmat = s.zeros(n, len(marks))
    for k, (i, j) in enumerate(marks):
        e[i, j] = q[i, j]
        bmat[i, k] = q[i, j]
    t = q - e
    chosen = [next(k for k, (i, j) in enumerate(marks) if i == v) for v in range(p)]
    nodes = list(range(p))
    lambdas = [s.Rational(1), s.Rational(3), s.Rational(7)]
    ms, gs = [], []
    calibration = None
    for lam in lambdas:
        all_columns = ((lam * s.eye(n) - t).inv() * bmat)[nodes, :]
        f = all_columns[:, chosen]
        m = f.inv()
        c = m * all_columns * s.ones(len(marks), 1)
        if calibration is None:
            calibration = c
        else:
            assert c == calibration
        ms.append(m)
        gs.append((m * s.ones(p, 1) - c) / lam)
    branch = next(i for i in range(p) if gs[0][i] != gs[1][i])
    l1, l2, l3 = lambdas
    ratio = (gs[0][branch] - gs[1][branch]) / (gs[1][branch] - gs[2][branch]) * (l3-l2)/(l2-l1)
    h = (l3-ratio*l1)/(ratio-1)
    v = (gs[0] - gs[1]) * ((l1+h)*(l2+h)/(l2-l1))
    u = gs[0] - v/(l1+h)
    d = s.diag(*(1/ui for ui in u))
    entrance = d * v
    outer = (d*(ms[1]-ms[0]) - (l2-l1)*s.eye(p)) * ((l1+h)*(l2+h)/(l2-l1))
    exits = outer[branch, :] / entrance[branch]
    a = l1*s.eye(p) - d*ms[0] - outer/(l1+h)
    recovered_t = a.row_join(entrance).col_join(exits.row_join(s.Matrix([[-h]])))
    assert recovered_t == t
    assert h == sum(q[n-1, j] for j in range(p))
    # Recovered calibration includes every observed rate, even repeated columns.
    for k, (i, j) in enumerate(marks):
        ratios = ms[0] * (((l1*s.eye(n)-t).inv()*bmat)[nodes, k])
        assert d[i, i] * ratios[i] == q[i, j]
    return {"dimension": n, "pairs": pairs, "branch": branch, "hidden_escape": str(h), "recovered_exactly": True}


def equal_exit_pair():
    m = s.symbols("m", positive=True)
    q = s.Matrix([[-6, 1, 2, 3], [2, -11, 4, 5], [6, 7, -13-m, m], [6, 7, 9-m, -22+m]])
    assert q*s.ones(4, 1) == s.zeros(4, 1)
    e = s.zeros(4)
    e[0, 1], e[1, 0] = 1, 2
    t = q-e
    c = s.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]])
    lump = s.Matrix([[-6, 1, 5], [2, -11, 9], [6, 7, -13]])
    assert q*c == c*lump
    kill_lump = lump-s.Matrix([[0, 1, 0], [2, 0, 0], [0, 0, 0]])
    assert t*c == c*kill_lump
    lam = s.symbols("lambda", positive=True)
    bmat = s.Matrix([[1, 0], [0, 2], [0, 0], [0, 0]])
    r = s.Matrix([[0, 1, 0, 0], [1, 0, 0, 0]])
    transfer = r*(lam*s.eye(4)-t).inv()*bmat
    derivative = transfer.diff(m).applyfunc(s.cancel)
    assert derivative == s.zeros(2)
    raw_pi = q.T.nullspace()[0]
    pi = raw_pi/sum(raw_pi)
    flux_f = s.cancel(pi[2]*m)
    flux_b = s.cancel(pi[3]*(9-m))
    assert s.limit(flux_f, m, 0, dir="+") == 0
    positive_limit = s.limit(flux_b, m, 0, dir="+")
    assert positive_limit > 0
    assert s.diff(s.trace(q), m) == 0
    return {"parameter_domain": "0 < m < 9", "trace": str(s.trace(q)), "all_time_transfer_derivative_zero": True,
            "lumping_identity": True, "limiting_reverse_internal_flux": str(positive_limit),
            "limiting_stationary_law": [str(s.limit(x, m, 0, dir="+")) for x in pi]}


def unequal_exit_pair_internal_boundary():
    eps = s.symbols("epsilon", nonnegative=True)
    q = s.Matrix([[-6,1,2,3], [2,-9,3,4], [1,100,-102,1], [2,1,1,-4]])
    transform = s.eye(4)
    transform[2,2], transform[2,3] = 1-eps, eps
    qp = (transform.inv()*q*transform).applyfunc(s.cancel)
    killed = s.zeros(4)
    killed[0,1], killed[1,0] = 1,2
    assert transform*killed == killed*transform
    assert (qp*s.ones(4,1)).applyfunc(s.cancel) == s.zeros(4,1)
    assert s.trace(qp) == s.trace(q)
    pi_raw = q.T.nullspace()[0]
    pi = (pi_raw/sum(pi_raw)).T
    pip = pi*transform
    assert (pip*qp).applyfunc(s.cancel) == s.zeros(1,4)
    boundary = s.sqrt(2402)-49
    assert boundary > 0 and boundary < s.Rational(1,2)
    f = 1-98*eps-eps**2
    assert s.cancel(qp[2,3]-f/(1-eps)) == 0
    assert s.simplify(qp[2,3].subs(eps,boundary)) == 0
    reverse = s.simplify((pip[3]*qp[3,2]).subs(eps,boundary))
    assert reverse > 0
    assert all(s.simplify(p.subs(eps,boundary)) > 0 for p in pip)
    lam = s.symbols("lambda", positive=True)
    bmat = s.Matrix([[1,0],[0,2],[0,0],[0,0]])
    r = s.Matrix([[0,1,0,0],[1,0,0,0]])
    # Intertwining identities prove all-time equality without expanding a large inverse.
    assert transform*bmat == bmat and r*transform == r
    assert ((q-killed)*transform-transform*(qp-killed)).applyfunc(s.cancel) == s.zeros(4)
    return {"parameter_domain": "0 <= epsilon < sqrt(2402)-49", "ratio_boundary": "1/2",
            "first_internal_boundary": str(boundary), "all_time_intertwining_identity": True,
            "limiting_reverse_internal_flux": str(reverse), "trace": str(s.trace(q))}


def final_draft_entropy_witness(n):
    q1 = s.Matrix([[-3,1,1,1], [2,-3,1,0], [1,1,-2,0], [1,0,0,-1]])
    q2 = s.Matrix([[-s.Rational(24,5),s.Rational(6,5),s.Rational(6,5),s.Rational(12,5)],
                   [2,-3,1,0], [1,1,-2,0], [2,0,0,-2]])
    originals = [q1,q2]
    qs = []
    for original in originals:
        q = s.zeros(n)
        q[:4,:4] = original
        # The stated N-extension requires these unit observed leaves at vertex 1.
        for leaf in range(4,n):
            q[1,leaf] = q[leaf,1] = 1
            q[1,1] -= 1
            q[leaf,leaf] = -1
        qs.append(q)
    pairs = [(0,1),(0,2),(1,2)] + [(1,leaf) for leaf in range(4,n)]
    marks = [(i,j) for pair in pairs for i,j in (pair,pair[::-1])]
    transforms = []
    stationary_laws = []
    coefficients = []
    for q in qs:
        e = s.zeros(n)
        bmat = s.zeros(n,len(marks))
        r = s.zeros(len(marks),n)
        for idx,(i,j) in enumerate(marks):
            e[i,j], bmat[i,idx], r[idx,j] = q[i,j], q[i,j], 1
        transforms.append([r*(lam*s.eye(n)-(q-e)).inv()*bmat for lam in (1,2,3)])
        assert q*s.ones(n,1) == s.zeros(n,1)
        pi_raw = q.T.nullspace()[0]
        pi = pi_raw/sum(pi_raw)
        stationary_laws.append([str(x) for x in pi])
        cycle_current = pi[1]*q[1,0] - pi[0]*q[0,1]
        affinity_ratio = q[1,0]*q[0,2]*q[2,1]/(q[0,1]*q[2,0]*q[1,2])
        assert affinity_ratio == 2
        assert pi[0]*q[0,3] == pi[3]*q[3,0]
        for leaf in range(4,n):
            assert pi[1]*q[1,leaf] == pi[leaf]*q[leaf,1]
        coefficients.append(cycle_current)
    assert transforms[0][0] == transforms[1][0]
    assert transforms[0][1] == transforms[1][1]
    assert transforms[0][2] != transforms[1][2]
    assert coefficients == [s.Rational(1,17+3*(n-4)),s.Rational(6,97+18*(n-4))]
    assert coefficients[1]-coefficients[0] > 0
    return {"dimension":n,"observed_pairs":pairs,"full_matrix_shape":list(transforms[0][0].shape),
            "equal_at_1_and_2":True,"unequal_at_3":True,"stationary_laws":stationary_laws,
            "entropy_log2_coefficients":[str(c) for c in coefficients]}


def any_two_arguments_witness():
    s1,s2,a0,b0,v0,w = s.symbols("s1 s2 a0 b0 v0 w", positive=True)
    c0=(s1+v0)*(s2+v0)
    a=a0+b0*(v0-w)/c0
    b=b0*(s1+w)*(s2+w)/c0
    for point in (s1,s2):
        assert s.cancel(a+b/(point+w)-(a0+b0/(point+v0))) == 0
    k,u,v = 1/a,b/a,w
    q=s.Matrix([[-k-u,k/2,k/2,u],[2,-3,1,0],[1,1,-2,0],[v,0,0,-v]])
    weights=s.Matrix([[10/k,3,4,10*u/(k*v)]])
    assert (weights*q).applyfunc(s.cancel) == s.zeros(1,4)
    z=7+10*a+10*b/w
    assert s.cancel(z-sum(weights)) == 0
    assert s.cancel(s.diff(z,w)+10*b0*s1*s2/(c0*w**2)) == 0
    return {"symbolic_interpolation_identity":True,"symbolic_stationary_weights":True,
            "strict_normalizer_derivative":"-10*b0*s1*s2/((s1+v0)*(s2+v0)*w^2)",
            "domain":"s1,s2,a0,b0,v0>0; s1!=s2; w>0 near v0 with a(w)>0"}


if __name__ == "__main__":
    here = Path(__file__).resolve()
    result = {
        "status": "exact checks passed; examples supplement the general proof",
        "python": platform.python_version(), "sympy": s.__version__,
        "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
        "seed": None, "arithmetic": "exact rational and symbolic; no tolerance",
        "reconstruction": [recover_one_hidden(generator(4), [(0,1),(1,2)]),
                           recover_one_hidden(generator(5), [(0,1),(2,3)]),
                           recover_one_hidden(generator(6, sparse=True), [(0,1),(2,3),(3,4)])],
        "equal_exit_pair": equal_exit_pair(),
        "unequal_exit_pair_internal_boundary": unequal_exit_pair_internal_boundary(),
        "final_draft_entropy_witness": [final_draft_entropy_witness(n) for n in (4,5,6)],
        "any_two_arguments_witness": any_two_arguments_witness(),
    }
    destination = here.with_name("referee_checks.json")
    destination.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
