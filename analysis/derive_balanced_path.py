"""Exact residual hidden-path polynomial along balanced theta(z,z).

Derivation reuses the analytic exit-chart equations (6)-(8) of
theta-fast-hidden-paths.md, now with symbolic z rather than the settled z=100.
It supplies necessary path equations, not a global feasibility certificate.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp


def derive(swapped=True):
    z,u=sp.symbols('z u')
    c=sp.Matrix([[3,0,1],[0,6,1],[z,z,1]])
    h=sp.Matrix([[-7,4,0],[5,-11,0],[0,0,-2*z]])
    d=c.inv()*h*c
    a1,a2,b1,b2,c1,c2=d[0,0],d[0,1],d[1,0],d[1,1],d[2,0],d[2,1]
    px,py=(6+8*z)/10,8*z/10
    qx,qy=11*z/18,(42+11*z)/18
    if swapped:
        a1,a2,b1,b2,c1,c2=b2,b1,a2,a1,c2,c1
        px,py,qx,qy=qy,qx,py,px
    v=sp.cancel(-u*(a2*u+c2)/(u*u+a1*u+c1))
    slope1,slope2=(px-u)/py,(qy-v)/qx
    aa=sp.cancel((u+slope1*v)/(1-slope1*slope2))
    bb=sp.cancel((v+slope2*u)/(1-slope1*slope2))
    gx=aa**2+aa*bb+a1*aa+b1*bb+c1
    gy=aa*bb+bb**2+a2*aa+b2*bb+c2
    phi=sp.factor(sp.cancel(aa*gy+(v-bb)*gx))
    numerator,denominator=sp.fraction(phi)
    return z,u,v,aa,bb,numerator,denominator


def main():
    z,u,v,a,b,num,den=derive()
    factors=sp.factor_list(num)
    print('numerator factors:',factors,flush=True)
    quadratics=[p for p,k in factors[1] if sp.degree(p,u)==2]
    polynomial=next(p for p in quadratics if sp.degree(p,z)==4)
    output={'kind':'exact symbolic necessary path equation, no global exclusion',
            'executed_at_utc':datetime.now(timezone.utc).isoformat(),
            'python':platform.python_version(),'sympy':sp.__version__,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'command':'.venv/Scripts/python.exe -B analysis/derive_balanced_path.py',
            'orientation':'endpoint y only; middle x only; other endpoint x,y',
            'v':str(v),'A':str(a),'B':str(b),'numerator':str(num),'denominator':str(den),
            'residual_polynomial':str(polynomial),
            'all_quadratic_factors':list(map(str,quadratics)),
            'discriminant':str(sp.factor(sp.discriminant(polynomial,u))),
            'physical_denominators':'all chart denominators nonzero; g_x(u,0)<0 and all reciprocal rates required'}
    Path('analysis/balanced-path-polynomial.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print('saved necessary path polynomial',flush=True)


if __name__=='__main__': main()
