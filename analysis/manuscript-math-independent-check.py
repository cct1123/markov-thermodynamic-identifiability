"""Independent algebra and outward-rational interval check for manuscript review.

Run from root: .venv/Scripts/python.exe -B analysis/manuscript-math-independent-check.py
No historical checker or historical numerical output is imported. No RNG.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import platform
import sympy as s


class I:
    """Exact rational intervals, rounded outward after every operation."""
    scale = 10**24

    def __init__(self, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        assert lo <= hi
        self.lo = F((lo*self.scale).__floor__(), self.scale)
        self.hi = F((hi*self.scale).__ceil__(), self.scale)

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        other = I.cast(other)
        return I(self.lo+other.lo, self.hi+other.hi)
    __radd__ = __add__

    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, other): return self + (-I.cast(other))
    def __rsub__(self, other): return I.cast(other) + (-self)

    def __mul__(self, other):
        other = I.cast(other)
        values = [x*y for x in (self.lo,self.hi) for y in (other.lo,other.hi)]
        return I(min(values),max(values))
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I.cast(other)
        assert other.lo*other.hi > 0
        return self*I(1/other.hi,1/other.lo)
    def __rtruediv__(self, other): return I.cast(other)/self

    def __pow__(self, power):
        assert power >= 0 and int(power) == power
        result = I(1)
        for _ in range(power): result = result*self
        return result

    def serial(self):
        scale = 10**6
        return [str(F((self.lo*scale).__floor__(),scale)),
                str(F((self.hi*scale).__ceil__(),scale))]


def main():
    z,x = s.symbols('z x',real=True)
    rho = s.sqrt(6)
    alpha,beta = 9-2*rho,9+2*rho
    X=s.Matrix([[2,0,8],[0,7,11]])
    Y=s.Matrix([[3,0],[0,6],[z,z]])
    H=s.Matrix([[-7,4,0],[5,-11,0],[0,0,-2*z]])
    minors=[Y.row_join(H*Y[:,0]).det(),Y.row_join(H*Y[:,1]).det(),
            X.col_join((X*H)[1,:]).det()]
    expected=[-9*z*(4*z-9),-18*z*(2*z-3),-14*(22*z+19)]
    assert all(s.expand(v-w)==0 for v,w in zip(minors,expected))

    A=z; B=z/(4*(rho-1)/5); m=(7+2*rho)/5
    L=(3-rho/2)/8; R=35*rho/88
    k=(2*z-9+2*rho)/(4*rho); a=k-1; J=a*m+k
    f=[A*R*m/L-B*J**2,
       A*(R/L+k-a*m)+L*J**2+R*J-2*B*J*a,
       a*(L*J+R-A*(1+L*k/R)-B*a)]
    f=[s.expand(s.radsimp(v)) for v in f]
    poly=352*z**4-3168*z**3-4644*z**2-11340*z-7623
    assert s.simplify(f[1]**2-4*f[0]*f[2]+(s.Rational(11,1200)+11*rho/4200)*(z+s.Rational(19,22))**2*poly/352)==0
    lo=F('10.55714966866'); hi=F('10.55714966867')
    assert poly.subs(z,s.Rational(lo)) < 0 < poly.subs(z,s.Rational(hi))
    assert s.Poly(poly,z).count_roots(0,s.oo)==1

    # Shift before interval evaluation, unlike historical expanded-z checker.
    ri=I('2.449489742783178098197284','2.449489742783178098197285')
    assert ri.lo**2<6<ri.hi**2
    def constant(expr):
        expr=s.expand(s.radsimp(expr))
        c=expr.coeff(rho); d=s.expand(expr-c*rho)
        assert c.is_Rational and d.is_Rational
        return I(F(d))+I(F(c))*ri
    def evaluate(expr,interval):
        p=s.Poly(s.expand(expr.subs(z,x+s.Rational(21,2))),x)
        ans=I(0); xx=interval-F(21,2)
        for c in p.all_coeffs(): ans=ans*xx+constant(c)
        return ans
    zi=I(F(21,2),hi)
    fi=[evaluate(v,zi) for v in f]
    assert fi[1].lo>0 and fi[2].hi<0
    rootfi=[evaluate(v,I(lo,hi)) for v in f]
    assert rootfi[0].hi<0<rootfi[1].lo and rootfi[2].hi<0
    Li,Ri,mi=map(constant,(L,R,m)); Ai=zi; Bi=evaluate(B,zi)
    ki=evaluate(k,zi); ai=ki-1; Ji=ai*mi+ki
    ti=-fi[1]/(2*fi[2])
    eps=Li*ti*(Ji+ai*ti)/(Ri*mi+(ki*Li+Ri)*ti)
    di=1-eps; Wi=Ri*eps; ell=mi+ti; Pi=Li*ti
    cr=ki/ai*(di+Wi*eps/(Ai+Wi)); Qi=(Ai*di+Wi)/(ai*eps)
    slope=(Pi+Wi)/(ell+di)
    margins={
        't':ti,'epsilon':eps,'1-epsilon':di,'c-1':cr-1,
        'bottom-left-output':Li*(mi+di)-Wi,
        'right-right-output':Qi-Ri*(cr-1),
        'B-above-left-lower':Bi+Wi-slope*(di+mi),
        'A-below-upper':((cr-1)*Pi+(ell+1)*Qi)/(ell+cr)-Ai,
        'left-origin':ai*Pi,'right-origin':ai*Qi,
        'bottom-left-inward':ai*(Wi+Pi),'bottom-right-inward':ai*(Wi+Qi)}
    assert all(v.lo>0 for v in margins.values())
    apex=Li*(mi+1)/(Li+Ri)-1/(evaluate(k,I(F(21,2)))-Ri/F(21,2))
    assert apex.lo>0
    # Balanced ray covering needs no special slow-pole redistribution result.
    assert constant(alpha/2-35*rho/88).lo>0
    assert constant(alpha/2-rho/4).lo>0
    assert 11*(2*F(21,2)-11)**2 < 1120

    # Generic two-state hidden shear, checked without historical helpers.
    mh,nh,sh,sk,e=s.symbols('m n sh sk e',positive=True)
    u=s.Matrix([[1-e,e],[0,1]])
    hh=s.Matrix([[-mh-sh,mh],[nh,-nh-sk]])
    transformed=u.inv()*hh*u
    assert s.factor(transformed[1,0]-nh*(1-e))==0
    assert s.factor(transformed[0,1]-(mh+e*(nh+sk-mh-sh)-nh*e**2)/(1-e))==0

    # Three-Laplace inverse derived directly from full killed resolvent.
    rr,ss,aa,cc,bb,dd,lam=s.symbols('r s a c b d lambda',positive=True)
    T=s.Matrix([[-rr-aa,0,aa],[0,-ss-cc,cc],[bb,dd,-bb-dd]])
    FF=(lam*s.eye(3)-T).inv()[:2,:2]*s.diag(rr,ss)
    HH=FF.inv(); gg=(HH*s.ones(2,1)-s.ones(2,1))/lam
    assert s.cancel(gg[0]-1/rr-aa/(rr*(lam+bb+dd)))==0
    assert s.cancel(gg[1]-1/ss-cc/(ss*(lam+bb+dd)))==0
    v0,h0,u0,l1,l2,l3=s.symbols('v h u l1 l2 l3',positive=True)
    g=lambda ll:u0+v0/(ll+h0)
    ratio=s.cancel((g(l1)-g(l2))/(g(l2)-g(l3))*(l3-l2)/(l2-l1))
    assert s.cancel((l3-ratio*l1)/(ratio-1)-h0)==0

    inputs=['analysis/balanced-cone-bound.md','analysis/theta-family-construction-audit.md',
            'analysis/publication-stability-audit.md','analysis/entropy-neighborhood-audit.md']
    result={'kind':'reproduced exact algebra and rigorous interval computation',
        'time_utc':datetime.now(timezone.utc).isoformat(),
        'command':'.venv/Scripts/python.exe -B analysis/manuscript-math-independent-check.py',
        'environment':{'python':platform.python_version(),'sympy':s.__version__},
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in inputs},
        'method':'Exact symbolic identities; rational intervals rounded outward at 24 decimal places after each operation; shifted polynomial evaluation. No historical check imports, numerical grid, optimizer, or RNG.',
        'root_interval':[str(lo),str(hi)],'sqrt6_interval':[str(ri.lo),str(ri.hi)],
        'geometric_parameter_interval':[str(zi.lo),str(zi.hi)],
        'f_over_geometric_interval':[i.serial() for i in fi],
        'f_at_root_interval':[i.serial() for i in rootfi],
        'strict_margins':{name:value.serial() for name,value in margins.items()},
        'apex_margin':apex.serial(),
        'checks':{'all_minimality_minors':True,'quartic_discriminant':True,
                  'unique_positive_root':True,'strict_cone_margins':True,
                  'simplified_balanced_covering':True,'hidden_pair_shear':True,
                  'direct_three_laplace_inverse':True},
        'all_checks_passed':True,
        'earlier_attempt':'First run stopped at a syntactic SymPy expression-equality assertion comparing factored and expanded identical polynomials. Replaced it by exact expanded-zero checks; no mathematical discrepancy.',
        'limits':'Checks identities and interval signs. Global support exhaustion and divergence follow from the separately reviewed conventional proofs, not this script. Not formal verification.'}
    out=Path('outputs/manuscript-math-independent-checks.json')
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'all_checks_passed':True,'output':str(out),'strict_margins':result['strict_margins']},indent=2))


if __name__=='__main__': main()
