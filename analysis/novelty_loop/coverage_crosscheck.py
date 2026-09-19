"""Coordinator crosscheck: exact lumped family and finite observation designs.

Run from project root with assertions enabled:
  .venv/Scripts/python.exe -B analysis/novelty_loop/coverage_crosscheck.py
Uses embedded exact inputs, no RNG, optimizer, tolerance, or external dataset.
The enumerations check the design corollary through N=6, not its universal proof.
"""
if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import platform

import sympy as s


def check_lumped_family():
    m, z = s.symbols('m z', positive=True)
    # Domain additionally m<2. Source m=1 is the reversible unit K4.
    q = s.ones(4) - 4 * s.eye(4)
    q[2, 3], q[3, 2] = m, 2 - m
    q[2, 2], q[3, 3] = -2 - m, -4 + m
    assert q * s.ones(4, 1) == s.zeros(4, 1)
    pi = s.Matrix([[s.Rational(1, 4), s.Rational(1, 4), (3-m)/8, (1+m)/8]])
    assert s.simplify(pi*q) == s.zeros(1, 4)
    assert sum(pi) == 1
    # Coarse states 0,1,{2,3}; exact intertwining independently of inversion.
    c = s.Matrix([[1,0,0], [0,1,0], [0,0,1], [0,0,1]])
    coarse = s.Matrix([[-3,1,2], [1,-3,2], [1,1,-2]])
    assert q*c == c*coarse
    t = q.copy()
    t[0,1] = t[1,0] = 0
    tc = coarse.copy()
    tc[0,1] = tc[1,0] = 0
    assert t*c == c*tc
    r = s.Matrix([[0,1,0,0], [1,0,0,0]])
    b = s.Matrix([[1,0], [0,1], [0,0], [0,0]])
    rc = s.Matrix([[0,1,0], [1,0,0]])
    bc = s.Matrix([[1,0], [0,1], [0,0]])
    assert r*c == rc and c*bc == b
    direct = (r*(z*s.eye(4)-t).inv()*b).applyfunc(s.cancel)
    lumped = (rc*(z*s.eye(3)-tc).inv()*bc).applyfunc(s.cancel)
    assert direct == lumped
    assert all(s.diff(x,m) == 0 for x in direct)
    assert s.trace(q) == -12
    forward = pi[2]*q[2,3]
    reverse = pi[3]*q[3,2]
    assert forward.subs(m,0) == 0
    assert reverse.subs(m,0) == s.Rational(1,4)
    # All outside fluxes have positive limits; their entropy terms remain bounded.
    assert all(pi[i].subs(m,0)>0 for i in range(4))
    for i,j in combinations(range(4),2):
        if (i,j)!=(2,3):
            assert (pi[i]*q[i,j]).subs(m,0)>0
            assert (pi[j]*q[j,i]).subs(m,0)>0
    # Thus sigma(m)=(1/4)*log(1/m)+O(1), m down to zero.
    assert pi.subs(m,1) == s.ones(1,4)/4
    assert q.subs(m,1) == s.ones(4)-4*s.eye(4)
    return {'domain':'0 < m < 2; source m=1; divergent path 0<m<=1',
            'Q':[[str(v) for v in row] for row in q.tolist()],
            'stationary':[str(v) for v in pi],
            'full_two_mark_transform':[[str(v) for v in row] for row in direct.tolist()],
            'killed_lumping_and_direct_resolvent_agree':True,
            'observed_rates':[1,1], 'trace':-12,
            'max_rate_supremum':2,
            'entropy_asymptotic':'(1/4)*log(1/m)+O(1)',
            'entropy_image_contains':'[0,infinity)',
            'why_image_is_all':'nonnegativity, reversible source, continuity, divergent path'}


def check_designs():
    results=[]
    for n in range(2,7):
        pairs=list(combinations(range(n),2))
        counts={str(k):0 for k in range(n+1)}
        minimum=len(pairs)
        passing=0
        for mask in range(1,1<<len(pairs)):
            covered=set()
            size=0
            for k,(i,j) in enumerate(pairs):
                if mask & (1<<k):
                    covered.update((i,j))
                    size+=1
            hidden=n-len(covered)
            counts[str(hidden)]+=1
            if hidden<=1:
                passing+=1
                minimum=min(minimum,size)
        assert minimum == n//2
        assert sum(counts.values())==(1<<len(pairs))-1
        results.append({'N':n, 'nonempty_observation_pair_sets':sum(counts.values()),
                        'counts_by_uncovered_vertices':counts,
                        'sets_with_finite_ceiling_at_complete_sources':passing,
                        'minimum_observed_pairs':minimum})
    return results


def check_arbitrary_two_samples():
    x,y,v,w,a,b=s.symbols('s1 s2 v0 w a0 b0',positive=True)
    denom=(x+v)*(y+v)
    aw=a+b*(v-w)/denom
    bw=b*(x+w)*(y+w)/denom
    for sample in (x,y):
        assert s.cancel(aw+bw/(sample+w)-a-b/(sample+v)) == 0
    z=7+10*aw+10*bw/w
    derivative=s.factor(s.diff(z,w))
    assert s.cancel(derivative+10*b*x*y/(denom*w**2)) == 0
    k,u,d=s.symbols('k u d',positive=True)
    q=s.Matrix([[-k-u,k/2,k/2,u],[2,-3,1,0],[1,1,-2,0],[d,0,0,-d]])
    weights=s.Matrix([[10/k,3,4,10*u/(k*d)]])
    assert s.simplify(weights*q) == s.zeros(1,4)
    assert s.simplify(weights[1]*q[1,0]-weights[0]*q[0,1]) == 1
    assert s.cancel(q[1,0]*q[0,2]*q[2,1]/(q[0,1]*q[2,0]*q[1,2])) == 2
    return {'domain':'s1,s2,v0,a0,b0>0; s1!=s2; w>0 near v0 and a(w)>0',
            'a(w)':str(aw),'b(w)':str(bw),'normalizer_Z(w)':str(z),
            'derivative_Z(w)':str(derivative),
            'two_sample_identities':True,'stationary_weight_check':True,
            'entropy':'log(2)/Z(w), strictly increasing in w on the admissible interval',
            'extension':'Each observed unit leaf at vertex 1 adds 3 to Z; derivative unchanged.'}


if __name__=='__main__':
    root=Path(__file__).resolve().parents[2]
    result={'status':'passed', 'timestamp_utc':datetime.now(timezone.utc).isoformat(),
            'python':platform.python_version(), 'sympy':s.__version__,
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'arithmetic':'exact rational/symbolic and exhaustive finite bit masks',
            'seed':None, 'lumped_family':check_lumped_family(),
            'observation_designs':check_designs(),
            'arbitrary_two_samples':check_arbitrary_two_samples(),
            'limitations':'Examples and finite counts check the written universal proof; no formal verification.'}
    target=root/'outputs/novelty-loop-2026-09-19/coverage-crosscheck.json'
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS: exact lumping, arbitrary two-sample entropy ambiguity, all observation sets N=2..6')
