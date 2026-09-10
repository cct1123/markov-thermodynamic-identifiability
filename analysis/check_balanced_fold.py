"""Exact physical fold witness and rigorous entropy separation.

Run from root: .venv/Scripts/python.exe -B analysis/check_balanced_fold.py
Arithmetic uses SymPy's number field Q[z]/P(z), exact rational root isolation,
and an elementary rational logarithm-series remainder bound. No solver or
formal-proof label is claimed. Global exhaustion requires the separate cone
argument; this script certifies the specific algebraic candidate.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp
import numpy as np
from scipy.linalg import expm
import scipy
import sympy as sp
from sympy.polys.matrices import DomainMatrix


def add(a,b): return a[0]+b[0],a[1]+b[1]
def multiply(a,b):
    corners=[x*y for x in a for y in b]
    return min(corners),max(corners)


def log_series(x,terms=24):
    """Rational enclosure of ln(x), for rational 1 <= x <= 2."""
    assert 1 <= x <= 2
    t=(x-1)/(x+1)
    partial=2*sum((t**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    remainder=2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return partial,partial+remainder


def log_bound(x):
    """Range reduction and monotone exact logarithm bounds, x>0 rational."""
    assert x > 0
    power=0
    while x < 1: x*=2; power-=1
    while x > 2: x/=2; power+=1
    base=log_series(x)
    return add(base,multiply((F(power),F(power)),log_series(F(2))))


def decimal_enclosure(bounds,digits=12):
    scale=10**digits
    low=(bounds[0]*scale).numerator//(bounds[0]*scale).denominator
    high=-((-bounds[1]*scale).numerator//(-bounds[1]*scale).denominator)
    return {"lower":str(F(low,scale)),"upper":str(F(high,scale)),
            "decimal_lower":str(sp.Rational(low,scale).evalf(digits+5)),
            "decimal_upper":str(sp.Rational(high,scale).evalf(digits+5))}


def main():
    z=sp.Symbol('z')
    polynomial=sp.Poly(352*z**4-3168*z**3-4644*z**2-11340*z-7623,z)
    assert polynomial.count_roots(0,sp.oo)==1
    assert polynomial.count_roots(-sp.oo,0)==1
    root=sp.CRootOf(polynomial,1)
    intervals=polynomial.intervals(eps=sp.Rational(1,10**35))
    (lo,hi),multiplicity=next((i,m) for i,m in intervals if i[0]>0)
    assert multiplicity==1 and polynomial.eval(lo)<0<polynomial.eval(hi)
    low,high=F(int(lo.p),int(lo.q)),F(int(hi.p),int(hi.q))
    assert F(10557149668664,10**12)<low<high<F(10557149668666,10**12)
    field=sp.QQ.algebraic_field(root)
    zz=field.from_sympy(root)
    zero,one=field.zero,field.one

    def scalar(x): return field.convert(x)
    def dm(rows):
        rows=[[scalar(x) for x in row] for row in rows]
        return DomainMatrix(rows,(len(rows),len(rows[0])),field)
    def identity(n): return dm([[int(i==j) for j in range(n)] for i in range(n)])
    def enclosure(value):
        # DO NOT use AlgebraicField.is_positive: its coefficient sign is not
        # the order of the selected real embedding. Bound its actual polynomial.
        coeffs=[F(int(c.numerator),int(c.denominator)) for c in reversed(value.to_list())]
        result=(F(0),F(0))
        for power,c in enumerate(coeffs):
            result=add(result,multiply((c,c),(low**power,high**power)))
        return result
    def sign(value):
        if value==zero: return 0
        lower,upper=enclosure(value)
        if lower>0: return 1
        if upper<0: return -1
        raise ArithmeticError('root isolation too coarse for requested sign')
    def encode(value): return [str(c) for c in value.to_list()]
    def matrix_encode(matrix): return [[encode(x) for x in row] for row in matrix.to_list()]

    q=dm([[-11,1,2,0,8],[2,-20,0,7,11],[3,0,-7,4,0],
          [0,6,5,-11,0],[zz,zz,0,0,-2*zz]])
    c=dm([[3,0,1],[0,6,1],[zz,zz,1]])
    h=dm([[-7,4,0],[5,-11,0],[0,0,-2*zz]])
    d=(c.inv()*h*c).to_list()
    # Independent exit-chart fold equation: the y-only endpoint u is a double
    # root of a(z)u^2+b(z)u+c(z), whose discriminant is a multiple of P(z).
    aa=100*zz**4-840*zz**3+3741*zz**2-6867*zz+3978
    bb=-408*zz**4-2916*zz**3+8766*zz**2+3105*zz-12474
    cc=2412*zz**4-5724*zz**3+891*zz**2+3402*zz
    assert bb*bb-4*aa*cc==zero and sign(aa)>0
    u=-bb/(2*aa)
    a1,a2,b1,b2,c1,c2=d[1][1],d[1][0],d[0][1],d[0][0],d[2][1],d[2][0]
    v=-u*(a2*u+c2)/(u*u+a1*u+c1)
    px,py=(42+11*zz)/18,11*zz/18
    qx,qy=8*zz/10,(6+8*zz)/10
    slope1,slope2=(px-u)/py,(qy-v)/qx
    a=(u+slope1*v)/(1-slope1*slope2)
    b=(v+slope2*u)/(1-slope1*slope2)
    cp=dm([[0,u,1],[v,0,1],[b,a,1]])
    hidden_similarity=c*cp.inv()
    srows=identity(5).to_list()
    for i,row in enumerate(hidden_similarity.to_list()): srows[i+2][2:]=row
    similarity=dm(srows)
    target=similarity.inv()*q*similarity
    assert similarity*dm([[1]]*5)==dm([[1]]*5)
    assert target*dm([[1]]*5)==dm([[0]]*5)
    source_rows,target_rows=q.to_list(),target.to_list()
    support=[]
    for i in range(5):
        for j in range(i+1,5):
            forward,reverse=sign(target_rows[i][j]),sign(target_rows[j][i])
            assert forward==reverse and forward>=0
            if forward: support.append([i,j])
    assert support==[[0,1],[0,3],[0,4],[1,2],[1,4],[2,3],[3,4]]
    assert [row[:2] for row in target_rows[:2]]==[row[:2] for row in source_rows[:2]]
    # Displayed graph is connected, with hidden path 2-3-4; exact support proves it.

    def stationary(matrix):
        rows=matrix.transpose().to_list()
        rows[-1]=[one]*5
        pi=dm(rows).inv()*dm([[0],[0],[0],[0],[1]])
        assert pi.transpose()*matrix==dm([[0]*5])
        assert sum((row[0] for row in pi.to_list()),zero)==one
        assert all(sign(row[0])>0 for row in pi.to_list())
        return pi
    pi,pi_target=stationary(q),stationary(target)
    assert pi.transpose()*similarity==pi_target.transpose()

    # Exact finite marked-kernel derivative certificate, independent of the
    # chart's missing-edge polynomial. Ten orders suffice at a five-state cap.
    reset=dm([[0,1,0,0,0],[1,0,0,0,0]])
    exits=dm([[1,0],[0,2],[0,0],[0,0],[0,0]])
    killed=[]
    for rows in (source_rows,target_rows):
        rows=[row[:] for row in rows]
        rows[0][1]=rows[1][0]=zero
        killed.append(dm(rows))
    powers=[identity(5),identity(5)]
    for order in range(10):
        assert reset*powers[0]*exits==reset*powers[1]*exits
        powers=[power*t for power,t in zip(powers,killed)]

    def entropy_enclosure(matrix,stationary_law):
        rows=matrix.to_list(); pp=[row[0] for row in stationary_law.to_list()]
        total=(F(0),F(0))
        for i in range(5):
            for j in range(i+1,5):
                if rows[i][j]==zero: continue
                forward,reverse=pp[i]*rows[i][j],pp[j]*rows[j][i]
                current=enclosure(forward-reverse)
                ratio=enclosure(forward/reverse)
                assert ratio[0]>0
                logarithm=(log_bound(ratio[0])[0],log_bound(ratio[1])[1])
                total=add(total,multiply(current,logarithm))
        return total
    sigma_source=entropy_enclosure(q,pi)
    sigma_target=entropy_enclosure(target,pi_target)
    difference=(sigma_target[0]-sigma_source[1],sigma_target[1]-sigma_source[0])
    assert difference[0]>F(26,10000)  # rigorously > 0.0026, no float sign claim

    def approximate(value,ctx,root_value):
        result=ctx.mpf(0)
        for coefficient in value.to_list():
            result=result*root_value+ctx.mpf(str(coefficient.numerator))/int(coefficient.denominator)
        return result
    high_precision=[]
    for digits in [60,100]:
        ctx=mp.mp.clone();ctx.dps=digits
        rr=ctx.findroot(lambda x:352*x**4-3168*x**3-4644*x*x-11340*x-7623,ctx.mpf('10.557'))
        sigmas=[]
        for matrix,law in [(q,pi),(target,pi_target)]:
            rows=matrix.to_list();pp=[approximate(row[0],ctx,rr) for row in law.to_list()]
            sigma=ctx.mpf(0)
            for i in range(5):
                for j in range(i+1,5):
                    if rows[i][j]==zero: continue
                    ff=pp[i]*approximate(rows[i][j],ctx,rr)
                    rf=pp[j]*approximate(rows[j][i],ctx,rr)
                    sigma+=(ff-rf)*ctx.log(ff/rf)
            sigmas.append(str(sigma))
        high_precision.append({'dps':digits,'z_star':str(rr),'entropies':sigmas})
    ctx=mp.mp.clone();ctx.dps=80;rr=ctx.mpf(high_precision[-1]['z_star'])
    numeric=lambda matrix:np.array([[float(approximate(x,ctx,rr)) for x in row] for row in matrix.to_list()])
    qn,sn,tn=numeric(q),numeric(similarity),numeric(target)
    direct=np.linalg.solve(sn,qn@sn)
    assert np.max(np.abs(direct-tn))<1e-12
    lhs=tn.T.copy();lhs[-1]=1;rhs=np.array([0,0,0,0,1])
    pn=np.linalg.solve(lhs,rhs)
    assert np.max(np.abs(pn-numeric(pi_target).ravel()))<1e-13
    rnum,bnum=numeric(reset),numeric(exits)
    times=[0.0,0.001,0.1,1.0,10.0]
    numerical_kernel_residual=max(np.max(np.abs(rnum@expm(numeric(killed[0])*time)@bnum-
                                               rnum@expm(numeric(killed[1])*time)@bnum)) for time in times)
    assert numerical_kernel_residual<1e-12
    sources=[Path(__file__),Path('analysis/derive_balanced_path.py')]
    output={'kind':'reproduced exact algebraic calculation with rigorous sign/log bounds',
            'executed_at_utc':datetime.now(timezone.utc).isoformat(),
            'command':'.venv/Scripts/python.exe -B analysis/check_balanced_fold.py',
            'environment':{'python':platform.python_version(),'sympy':sp.__version__,'mpmath':mp.__version__,
                           'numpy':np.__version__,'scipy':scipy.__version__,'platform':platform.platform()},
            'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
            'root_polynomial':str(polynomial.as_expr()),'root_interval':[str(lo),str(hi)],
            'representation':'Each coefficient list is a polynomial in the unique positive root z*, descending powers, degree<4.',
            'U':matrix_encode(hidden_similarity),'source':matrix_encode(q),'target':matrix_encode(target),
            'stationary_source':matrix_encode(pi),'stationary_target':matrix_encode(pi_target),
            'target_numeric':tn.tolist(),'target_support':support,'exact_marked_derivatives_checked':list(range(10)),
            'entropy_source_certified':decimal_enclosure(sigma_source),
            'entropy_target_certified':decimal_enclosure(sigma_target),
            'entropy_difference_certified':decimal_enclosure(difference),
            'log_bound_method':'24-term positive atanh series after powers-of-two range reduction; explicit rational geometric remainder',
            'high_precision_cross_checks':high_precision,'numerical_kernel_times':times,
            'numerical_kernel_residual':float(numerical_kernel_residual),
            'all_checks_passed':True,
            'limitation':'This verifies an endpoint witness and distinct entropy, not global exhaustion; the separate analytic cone proof supplies that.'}
    Path('outputs/balanced-fold-checks.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:output[k] for k in ['all_checks_passed','entropy_source_certified',
                                         'entropy_target_certified','entropy_difference_certified']},indent=2))


if __name__=='__main__': main()
