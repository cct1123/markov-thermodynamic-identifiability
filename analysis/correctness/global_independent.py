"""Independent algebra supporting the Sept 15 global five-state proof audit.

Run from root:
    .venv/Scripts/python.exe -B analysis/correctness/global_independent.py

The continuum exclusion is the conventional proof in GLOBAL-INDEPENDENT.md.
This script checks identities, sign certificates and the finite hidden-support
partition; it is not an optimizer, global feasibility solver or formal proof.
Historical calculations are replayed with JSON writes intercepted and are
explicitly labeled re-executions, not independent mathematical evidence.
"""
if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

from contextlib import redirect_stdout
from fractions import Fraction as F
import hashlib
import io
import itertools
import json
from pathlib import Path
import platform
import runpy
import sys
from unittest.mock import patch

import sympy as s

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"outputs/correctness-2026-09-15/global-independent.json"


def ia(x,y): return x[0]+y[0],x[1]+y[1]
def im(x,y):
    v=[a*b for a in x for b in y]
    return min(v),max(v)
def ii(v): return F(v),F(v)
def q6_interval(expr,rho,ri):
    expr=s.expand(s.radsimp(expr))
    b=expr.coeff(rho);a=s.simplify(expr-b*rho)
    assert a.is_Rational and b.is_Rational
    return ia(ii(F(a)),im(ii(F(b)),ri))
def poly_interval(expr,z,zi,rho,ri):
    answer=ii(0)
    for coeff in s.Poly(s.expand(expr),z).all_coeffs():
        answer=ia(im(answer,zi),q6_interval(coeff,rho,ri))
    return answer
def enc(interval):
    return {"rational":[str(v) for v in interval],"decimal_diagnostic":[float(v) for v in interval]}
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def independent_algebra():
    a,d,W,ell,c,P,Q,A,B,m,L,R=s.symbols("a d W ell c P Q A B m L R",positive=True)
    k=a+1;eps=1-d
    g=ell*W/(a*ell+k*d)
    assert s.cancel(s.diff(g,ell)-W*k*d/(a*ell+k*d)**2)==0
    assert s.cancel(s.diff(g,ell,2)+2*a*W*k*d/(a*ell+k*d)**3)==0
    H=((c+m)*P+(ell-m)*Q)/(ell+c)
    assert s.cancel(s.diff(H,P)-(c+m)/(ell+c))==0
    assert s.cancel(s.diff(H,ell)-(c+m)*(Q-P)/(ell+c)**2)==0
    slope=(A+W)/eps
    line=slope*(c-d)-W
    hyperbola=c*W/(a*c-k*d)
    cstar=k/a*(d+W*eps/(A+W))
    qstar=(A*d+W)/(a*eps)
    assert s.cancel(cstar-k*d/a-k*W*eps/(a*(A+W)))==0
    assert s.cancel(line.subs(c,cstar)-qstar)==0
    assert s.cancel(hyperbola.subs(c,cstar)-qstar)==0
    assert s.cancel((line-hyperbola)*eps*(a*c-k*d)
                    -a*(A+W)*(c-d)*(c-cstar))==0
    expected_line_derivative=(ell-m)*(slope*(ell+d)+W+P)/(ell+c)**2
    assert s.cancel(s.diff(H.subs(Q,line),c)-expected_line_derivative)==0
    expected_hyperbola_derivative=(ell-m)*(P-hyperbola)/(ell+c)**2 \
        -(ell-m)*W*k*d/((ell+c)*(a*c-k*d)**2)
    assert s.cancel(s.diff(H.subs(Q,hyperbola),c)-expected_hyperbola_derivative)==0
    assert s.cancel(hyperbola-W/a-W*k*d/(a*(a*c-k*d)))==0
    t,r=s.symbols("t r",positive=True)
    envelope=t*(L*m+(1+L*r)*Q)/(m+t+r*Q)
    den=(m+t+r*Q)**2
    expected=[(L*m+(1+L*r)*Q)*(m+r*Q)/den,
              t*(m+t+L*r*t)/den,t*Q*(L*t-Q)/den]
    for var,expression in zip((t,Q,r),expected):
        assert s.cancel(s.diff(envelope,var)-expression)==0
    # Implicit left-root derivative has a strictly positive denominator.
    E=L*t*(a*(m+t)+k*d)-(m+t)*W
    wcurve=L*t*(a*(m+t)+k*d)/(m+t)
    assert s.cancel(s.diff(E,t).subs(W,wcurve)
                    -L*(a*(m+t)+k*d*m/(m+t)))==0
    # Four exact face velocity checks, with no assumed orientation conventions.
    u,v=s.symbols("u v",real=True)
    pl=(P+W)/(ell+d);qr=(Q+W)/(c-d)
    upper=((c-u)*P+(u+ell)*Q)/(ell+c)-v
    lower_left=v+W-pl*(d-u)
    lower_right=v+W-qr*(u-d)
    velocity=lambda f:s.diff(f,u)*(-u)+s.diff(f,v)*(-k*v)
    assert s.cancel(velocity(lower_left).subs({u:-ell,v:P})-(pl*ell-k*P))==0
    assert s.cancel(velocity(lower_right).subs({u:c,v:Q})-(qr*c-k*Q))==0
    assert s.cancel(velocity(upper).subs({u:-ell,v:P})
                    -((a*ell+k*c)*P+ell*Q)/(ell+c))==0
    assert s.cancel(velocity(upper).subs({u:c,v:Q})
                    -((k*ell+a*c)*Q+c*P)/(ell+c))==0

    z=s.symbols("z",real=True);rho=s.sqrt(6)
    rr=4*(rho-1)/5;mm=(7+2*rho)/5
    ll=(3-rho/2)/8;rw=35*rho/88
    kk=(2*z-9+2*rho)/(4*rho);aa=kk-1;J=aa*mm+kk
    ff=[z*rw*mm/ll-z/rr*J**2,
        z*(rw/ll+kk-aa*mm)+ll*J**2+rw*J-2*z/rr*J*aa,
        aa*(ll*J+rw-z*(1+ll*kk/rw)-z/rr*aa)]
    ff=[s.expand(s.radsimp(v)) for v in ff]
    poly=352*z**4-3168*z**3-4644*z**2-11340*z-7623
    disc=-(s.Rational(11,1200)+11*rho/4200)*(z+s.Rational(19,22))**2*poly/352
    assert s.expand(ff[1]**2-4*ff[0]*ff[2]-disc)==0
    zi=(F("10.55714966866"),F("10.55714966867"))
    ri=(F("2.449489742783178098197284"),F("2.449489742783178098197285"))
    assert ri[0]**2<6<ri[1]**2
    root_signs=[F(poly.subs(z,s.Rational(q))) for q in zi]
    assert root_signs[0]<0<root_signs[1]
    signs=[s.sign(v) for v in s.Poly(poly,z).all_coeffs()]
    assert sum(x!=y for x,y in zip(signs,signs[1:]))==1
    bounds=[poly_interval(v,z,zi,rho,ri) for v in ff]
    assert bounds[0][1]<0 and bounds[1][0]>0 and bounds[2][1]<0
    apex=s.radsimp(ll*(mm+1)/(ll+rw)-1/(kk-rw/z))
    apex_interval=q6_interval(apex.subs(z,s.Rational(21,2)),rho,ri)
    assert apex_interval[0]>F(14259,10**6)
    local_quadratic=z*z-11*z+s.Rational(211,44)
    assert local_quadratic.subs(z,s.Rational(zi[0]))>0 and 2*zi[0]-11>0
    # The original reflected scalar comparison after clearing a positive
    # denominator is exact, including its advertised z>=10 shifted form.
    reflected_bound=(s.Rational(25,8)+s.Rational(25,18)*(z+1))/(z-7)
    assert s.cancel((z-reflected_bound)*72*(z-7)
                    -(72*(z-10)**2+836*(z-10)+835))==0
    # Pair reconstruction: eliminate no denominator that may vanish in a
    # physical pair; all x_i,y_i,h,k below are required strictly positive.
    h0,k0=s.symbols("h0 k0",positive=True)
    assert s.expand(h0*(11-k0)-8*(7-h0)-(19*h0-h0*k0-56))==0
    assert F(48*105,6*42)==20
    assert (F(56+20,19),F(20,4))==(4,5)
    # Independent subcritical opening formulas. These certify the velocity
    # algebra; positivity over the intervals uses the inequalities in the note.
    source=s.Matrix([[-11,1,2,0,8],[2,-20,0,7,11],[3,0,-7,4,0],
                     [0,6,5,-11,0],[z,z,0,0,-2*z]])
    ds=2*(rho-1);alpha=9-2*rho;beta=9+2*rho
    def embedded_direction(entries):
        K=s.zeros(5)
        for (i,j),value in entries.items():K[i,j]=value
        for i in range(2,5):K[i,i]=-sum(K[i,j] for j in range(5) if j!=i)
        return K
    K=embedded_direction({(2,4):-4,(3,4):-ds,(4,2):5,(4,3):ds})
    velocity=source*K-K*source
    hidden_missing=[(2,4),(3,4),(4,2),(4,3)]
    for ij,value in zip(hidden_missing,[4,ds,5,ds]):
        assert s.expand(velocity[ij]-(alpha-2*z)*value)==0
    for ij,value in zip([(0,3),(1,2),(2,1),(3,0)],[8*ds,55,4*z,ds*z]):
        assert s.expand(velocity[ij]-value)==0
    ph,qh,rh,uh,vh=s.symbols("p_h q_h r_h u_h v_h",real=True)
    K=embedded_direction({(2,3):ph,(2,4):qh,(3,2):rh,(3,4):-1,(4,2):-vh,(4,3):uh})
    velocity=source*K-K*source
    MS=2*z-11;LS=MS+4
    expected=[2*ph+8*uh,7*rh-11*vh,-6*ph-z*qh,LS*qh-4,
              -3*rh+z,5*qh-MS,LS*vh-5*uh,4*vh-MS*uh]
    missing=[(0,3),(1,2),(2,1),(2,4),(3,0),(3,4),(4,2),(4,3)]
    assert all(s.expand(velocity[ij]-value)==0 for ij,value in zip(missing,expected))
    u2,t2=s.symbols("u2 t2",positive=True);s0=2*z;Delta=4*rho
    P2=s.Matrix([[1,1],[-t2,u2]])
    X2=s.Matrix([[8,2*ds],[11,-35]])
    Y2=s.Matrix([[z,z],[3/Delta,-24/(ds*Delta)]])
    H2=s.diag(-s0,-beta)
    expected_H=s.Matrix([[-s0*u2-beta*t2,u2*(beta-s0)],
                          [t2*(beta-s0),-s0*t2-beta*u2]])/(t2+u2)
    assert (P2.inv()*H2*P2-expected_H).applyfunc(s.simplify)==s.zeros(2)
    assert s.simplify(Y2.det()+z*(24/ds+3)/Delta)==0
    assert (expected_H.subs(z,beta/2)+beta*s.eye(2)).applyfunc(s.simplify)==s.zeros(2)
    return {"status":"executed exact symbolic identities and rational interval signs",
            "identities_checked":["left intersection derivatives","both derivatives of upper input height",
                "right line/hyperbola intersection and pole separation","line-minus-hyperbola factorization",
                "monotonicity of both right arcs","all three final-envelope partial derivatives",
                "implicit left-root monotonicity under W increase","four triangle-face velocity formulas",
                "balanced discriminant identity","reflected scalar bound","disconnected-pair elimination",
                "all eight below-slow-pole opening velocities","all eight fast-opening velocities",
                "two-mode hidden similarity, rank-two input and repeated-fast-pole scalar limit"],
            "line_minus_hyperbola":"a*(A+W)*(c-d)*(c-cstar)/((1-d)*(a*c-k*d))",
            "root_interval":[str(x) for x in zi],"polynomial_endpoint_signs":[str(v) for v in root_signs],
            "endpoint_f_coefficients":[enc(v) for v in bounds],"apex_margin_at_10_5":enc(apex_interval),
            "root_uniqueness":"one Descartes sign change plus opposite endpoint signs",
            "floating_point_used_for_decisive_signs":False}


def support_partition():
    pairs=[(0,1),(0,2),(1,2)];rows=[]
    for bits in itertools.product((0,1),repeat=3):
        edges=[p for p,b in zip(pairs,bits) if b]
        unseen=set(range(3));components=[]
        while unseen:
            component={next(iter(unseen))}
            while True:
                larger=component|{j for i,j in edges if i in component}|{i for i,j in edges if j in component}
                if larger==component:break
                component=larger
            unseen-=component;components.append(sorted(component))
        sizes=sorted(map(len,components))
        assert sizes in ([1,1,1],[1,2],[3])
        rows.append({"edges":edges,"components":components,"sizes":sizes})
    assert sum(r["sizes"]==[1,1,1] for r in rows)==1
    assert sum(r["sizes"]==[1,2] for r in rows)==3
    assert sum(r["sizes"]==[3] for r in rows)==4
    return {"all_labeled_reciprocal_hidden_supports":rows,
            "interpretation":"Each reciprocal pair is present in both directions or absent in both. This graph partition is exhaustive for exactly three hidden states. It is not rate feasibility enumeration."}


def replay(name):
    captures={};stdout=io.StringIO()
    def intercept(path,data,*args,**kwargs):
        path=Path(path).resolve()
        assert path.suffix==".json" and path.is_relative_to(ROOT)
        captures[path.relative_to(ROOT).as_posix()]=json.loads(data)
        return len(data)
    with patch.object(Path,"write_text",intercept),redirect_stdout(stdout):
        runpy.run_path(str(ROOT/"analysis"/name),run_name="__main__")
    assert len(captures)==1
    target,result=next(iter(captures.items()))
    return {"script":"analysis/"+name,"script_sha256":sha(ROOT/"analysis"/name),
            "historical_output":target,"historical_output_sha256":sha(ROOT/target),
            "fresh_assertions_passed":True,"captured_result":result,"stdout":stdout.getvalue(),
            "independence":"Re-execution of the accepted checker; not independent of its encoding or mathematical premises."}


def main():
    sys.path.insert(0,str(ROOT/"analysis"))
    protected=list((ROOT/"analysis").glob("*.json"))+list((ROOT/"outputs").glob("*.json"))
    before={str(p.relative_to(ROOT)):sha(p) for p in protected}
    algebra=independent_algebra()
    partition=support_partition()
    replays=[replay(name) for name in ("check_balanced_cone_bound.py","check_balanced_cone_sufficiency.py","check_balanced_fold.py")]
    assert before=={str(p.relative_to(ROOT)):sha(p) for p in protected}
    sources=[Path(__file__),ROOT/"analysis/correctness/GLOBAL-INDEPENDENT.md",ROOT/"analysis/correctness/global-proof.tex",
             ROOT/"manuscript/supplementary/proofs.tex",ROOT/"analysis/balanced-cone-bound.md",ROOT/"analysis/theta-fast-spectral-audit.md"]
    out={"all_checks_passed":True,"command_from_root":".venv/Scripts/python.exe -B analysis/correctness/global_independent.py",
         "environment":{"python":platform.python_version(),"sympy":s.__version__},"random_seed":None,
         "source_sha256":{str(p.relative_to(ROOT)):sha(p) for p in sources},"independent_algebra":algebra,
         "finite_hidden_support_partition":partition,"reexecuted_historical_certificates":replays,
         "historical_outputs_unchanged":True,
         "limits":"No numerical search, feasibility solver, proof-assistant or literature novelty claim. Universal exhaustion and equality rigidity require the explicitly expanded conventional arguments in GLOBAL-INDEPENDENT.md."}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"all_checks_passed":True,"output":str(OUT),"replayed_certificates":len(replays),"historical_outputs_unchanged":True},indent=2))


if __name__=="__main__":main()
