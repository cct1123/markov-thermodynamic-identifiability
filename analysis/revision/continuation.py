"""Exact local unfolding certificate and bounded numerical continuation.

Run from root: .venv/Scripts/python.exe -B analysis/revision/continuation.py
The exact interval rectangle supports a local theorem; the wider continuation
grid is a diagnostic, not an exhaustive classification of off-balanced models.
Historical files are read only. No stochastic input or optimizer is used.
"""
from __future__ import annotations

if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

import argparse
from fractions import Fraction as Rat
import hashlib
import json
from pathlib import Path
import platform

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
import scipy
from scipy.linalg import expm
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs/revision/continuation.json"
FIG = ROOT / "manuscript/figures"
DPS = 80


class Interval:
    """Rational endpoints, rounded OUTWARD to 45 decimals after operations."""
    scale = 10**45

    def __init__(self, lower, upper=None):
        lo = Rat(lower)
        hi = lo if upper is None else Rat(upper)
        assert lo <= hi
        self.lo = Rat((lo*self.scale).__floor__(), self.scale)
        self.hi = Rat((hi*self.scale).__ceil__(), self.scale)

    @staticmethod
    def cast(v):
        return v if isinstance(v, Interval) else Interval(v)

    def __add__(self, other):
        other = self.cast(other)
        return Interval(self.lo+other.lo, self.hi+other.hi)
    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        other = self.cast(other)
        vals = [x*y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return Interval(min(vals), max(vals))
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.cast(other)
        assert other.lo*other.hi > 0, "denominator interval contains zero"
        return self * Interval(1/other.hi, 1/other.lo)

    def __rtruediv__(self, other):
        return self.cast(other) / self

    def __pow__(self, n):
        assert n >= 0 and int(n) == n
        if n == 0:
            return Interval(1)
        if n % 2 == 0 and self.lo <= 0 <= self.hi:
            return Interval(0, max(self.lo**n, self.hi**n))
        vals = [self.lo**n, self.hi**n]
        return Interval(min(vals), max(vals))

    def encode(self):
        return {"rational": [str(self.lo), str(self.hi)],
                "decimal_diagnostic": [float(self.lo), float(self.hi)]}


def polynomial(z, delta):
    return (352*z**4-3168*z**3-4644*z**2-11340*z-7623
            -(20160*z+14112)*delta
            -(352*z**2-3168*z+15768)*delta**2)


def parameters(z, delta, rho):
    L = (3-rho/2)/8
    R = 35*rho/88
    m = (7+2*rho)/5
    ry = 4*(rho-1)/5
    A, B = z+delta, (z-delta)/ry
    k = (2*z-9+2*rho)/(4*rho)
    a = k-1
    J = a*m+k
    f0 = A*R*m/L-B*J**2
    f1 = A*(R/L+k-a*m)+L*J**2+R*J-2*B*J*a
    f2 = a*(L*J+R-A*(1+L*k/R)-B*a)
    return dict(L=L, R=R, m=m, ry=ry, A=A, B=B, k=k, a=a,
                J=J, f0=f0, f1=f1, f2=f2)


def shifted_interval(expr, z, delta, zi, di, rho, ri):
    """Exact polynomial evaluation after shifting z to rectangle midpoint."""
    center = Rat(21115, 2000)  # 10.5575
    x, y = sp.symbols("xi eta")
    shifted = sp.Poly(sp.expand(expr.subs({z:x+sp.Rational(center), delta:y})), x, y)
    value = Interval(0)
    xi = zi-center
    for powers, coefficient in shifted.terms():
        coefficient = sp.expand(sp.radsimp(coefficient))
        b = coefficient.coeff(rho)
        a = sp.simplify(coefficient-b*rho)
        assert a.is_Rational and b.is_Rational
        value += (Interval(Rat(a))+Rat(b)*ri) * xi**powers[0] * di**powers[1]
    return value


def exact_certificate():
    z, delta, t = sp.symbols("z delta t", real=True)
    rho = sp.sqrt(6)
    p = parameters(z, delta, rho)
    f = [sp.expand(sp.radsimp(p["f"+str(i)])) for i in range(3)]
    disc = sp.expand(f[1]**2-4*f[0]*f[2])
    C = sp.Rational(11,1200)+11*rho/4200
    expected = -C*(z+sp.Rational(19,22))**2*polynomial(z,delta)/352
    assert sp.expand(disc-expected) == 0
    center = -f[1]/(2*f[2])
    assert sp.cancel(sum(f[i]*t**i for i in range(3))
                     -(f[2]*(t-center)**2-disc/(4*f[2]))) == 0
    # The perturbed modal transfer really is the source transfer.
    X = sp.Matrix([[2,0,8],[0,7,11]])
    Y = sp.Matrix([[3,0],[0,6],[z+delta,z-delta]])
    H = sp.Matrix([[-7,4,0],[5,-11,0],[0,0,-2*z]])
    Xm = sp.Matrix([[3+rho/2,3-rho/2,8],[35*rho/8,-35*rho/8,11]])
    Ym = sp.Matrix([[1,p["ry"]],[1,-4*(rho+1)/5],[z+delta,z-delta]])
    D = sp.diag(-9+2*rho,-9-2*rho,-2*z)
    for j in range(6):
        assert (X*H**j*Y-Xm*D**j*Ym).applyfunc(sp.simplify) == sp.zeros(2)
    # A nonzero pair of hidden reachability minors plus observability proves
    # minimal order five at delta=0; openness extends it locally.
    reach = sp.factor(sp.Matrix.hstack(Y,H*Y[:,0]).det())
    observ = sp.factor(sp.Matrix.vstack(X,(X*H)[1,:]).det())
    # Explicit open-neighborhood certificate: all z,delta in this rectangle.
    zi = Interval("10.55", "10.565")
    di = Interval("-0.005", "0.005")
    ri = Interval("2.449489742783178098197284074705891391965947480",
                  "2.449489742783178098197284074705891391965947481")
    assert ri.lo**2 < 6 < ri.hi**2
    pi = parameters(zi,di,ri)
    for i in range(3):
        pi["f"+str(i)] = shifted_interval(f[i],z,delta,zi,di,rho,ri)
    L,R,m,A,B,k,a,J = [pi[key] for key in ("L","R","m","A","B","k","a","J")]
    tc = -pi["f1"]/(2*pi["f2"])
    eps = L*tc*(J+a*tc)/(R*m+(k*L+R)*tc)
    d = 1-eps
    W = R*eps
    ell,P = m+tc,L*tc
    c = k/a*(d+W*eps/(A+W))
    Qv = (A*d+W)/(a*eps)
    sl = (P+W)/(ell+d)
    eps0 = L*(m+1)/(L+R)
    # These first inequalities are uniform necessary-condition reductions for
    # ALL candidate triangles, not merely tests of the constructed triangle.
    margins = {
        "source_exits_positive": zi-Interval("0.005"),
        "fast_pole_gap": 2*zi-(9+2*ri),
        "A_minus_B": A-B,
        "B_minus_two": B-2,
        "a_minus_seven_tenths": a-Rat(7,10),
        "exclude_negative_bottom": A-L/a*(m+(B+1)/R),
        "bottom_right_of_apex": eps0-1/(k-R/A),
        "minus_f0": -pi["f0"], "f1": pi["f1"], "minus_f2": -pi["f2"],
        "t_positive": tc, "epsilon_positive": eps, "one_minus_epsilon": d,
        "right_abscissa_minus_one": c-1,
        "bottom_left_output": L*(m+d)-W,
        "right_right_output": Qv-R*(c-1),
        "input_B_above_left_lower": B+W-sl*(d+m),
        "input_A_below_upper": ((c-1)*P+(ell+1)*Qv)/(ell+c)-A,
        "left_origin_margin": a*P, "right_origin_margin": a*Qv,
        "bottom_left_invariance": a*(W+P), "bottom_right_invariance": a*(W+Qv),
        "negative_reachability_minor": -shifted_interval(reach,z,delta,zi,di,rho,ri),
        "negative_observability_minor": -shifted_interval(observ,z,delta,zi,di,rho,ri),
        "Pdelta_z_positive": shifted_interval(sp.diff(polynomial(z,delta),z),z,delta,zi,di,rho,ri),
        "Pdelta_lower_negative": -shifted_interval(polynomial(z,delta).subs(z,sp.Rational("10.55")),z,delta,zi,di,rho,ri),
        "Pdelta_upper_positive": shifted_interval(polynomial(z,delta).subs(z,sp.Rational("10.565")),z,delta,zi,di,rho,ri),
    }
    for name, interval in margins.items():
        assert interval.lo > 0, (name,interval.encode())
    return {"status":"exact symbolic identities and rational interval sign certificate",
            "discriminant_identity":str(expected), "P_delta":str(sp.expand(polynomial(z,delta))),
            "normal_form":"F=f2*(t+f1/(2*f2))^2-Delta/(4*f2)",
            "source_reachability_minor":str(reach),"source_observability_minor":str(observ),
            "modal_moments_checked":list(range(6)),
            "rectangle":{"z":["10.55","10.565"],"delta":["-0.005","0.005"]},
            "rounding":"rational interval operations, outward to 45 decimal places; no float sign tests",
            "strict_margins":{k:v.encode() for k,v in margins.items()},
            "interpretation":"The sign certificate supports the accompanying conventional local cone proof. It is not formal verification or a general off-balanced classification."}


def numeric_parameters(ctx,z,delta):
    return parameters(ctx.mpf(z),ctx.mpf(delta),ctx.sqrt(6))


def critical(ctx, delta):
    return ctx.findroot(lambda z:polynomial(z,delta),(ctx.mpf(10),ctx.mpf(11)))


def triangle(ctx,z,delta,t=None,opening=0):
    p = numeric_parameters(ctx,z,delta)
    L,R,m,A,B,k,a,J = [p[key] for key in ("L","R","m","A","B","k","a","J")]
    if t is None:
        t = -p["f1"]/(2*p["f2"])
    eps = L*t*(J+a*t)/(R*m+(k*L+R)*t)
    d = 1-eps
    W = R*eps
    ell,P = m+t,L*t
    # Explicit strictification from the proof, with a deterministically
    # backtracked common step. This changes the realization, not the data.
    if opening:
        step=ctx.mpf(opening)
        W *= 1-step
        b=L*(a*m+k*d)-W
        t=(-b+ctx.sqrt(b*b+4*L*a*m*W))/(2*L*a)
        ell=m+t*(1-step)
        P=(L*(ell-m)+ell*W/(a*ell+k*d))/2
    c=k/a*(d+W*eps/(A+W))
    Qv=(A*d+W)/(a*eps)
    if opening:
        Qv *= 1-ctx.mpf(opening)
    V=ctx.matrix([[1,1,1],[-ell,c,d],[P,Qv,-W]])
    return V,p


def source(ctx,z,delta):
    return ctx.matrix([[-11,1,2,0,8],[2,-20,0,7,11],[3,0,-7,4,0],
                       [0,6,5,-11,0],[z+delta,z-delta,0,0,-2*z]])


def realize(ctx,z,delta,V):
    rho=ctx.sqrt(6)
    Xm=ctx.matrix([[3+rho/2,3-rho/2,8],[35*rho/8,-35*rho/8,11]])
    Ym=ctx.matrix([[1,4*(rho-1)/5],[1,-4*(rho+1)/5],[z+delta,z-delta]])
    D=ctx.diag([-9+2*rho,-9-2*rho,-2*z])
    Hbar=V**-1*D*V
    Ybar=V**-1*Ym
    w=-(Hbar**-1)*Ybar*ctx.matrix([1,1])
    W=ctx.diag(list(w))
    H=W**-1*Hbar*W
    X=Xm*V*W
    Y=W**-1*Ybar
    q=ctx.zeros(5)
    q[0,0],q[0,1],q[1,0],q[1,1]=-11,1,2,-20
    for i in range(3):
        for j in range(3):q[i+2,j+2]=H[i,j]
        for j in range(2):q[j,i+2],q[i+2,j]=X[j,i],Y[i,j]
    return q,w


def stationary(ctx,q):
    M=q.T.copy()
    for j in range(5):M[4,j]=1
    return ctx.lu_solve(M,ctx.matrix([0,0,0,0,1]))


ABSENT = {(0,2),(2,0),(1,4),(4,1),(2,3),(3,2)}


def diagnostics(ctx,z,delta,q,path):
    pi=stationary(ctx,q)
    positive=[q[i,j] for i in range(5) for j in range(5) if i!=j and (not path or (i,j) not in ABSENT)]
    absent=max([abs(q[i,j]) for i,j in ABSENT]) if path else ctx.mpf(0)
    assert min(positive)>0 and min(pi)>0
    assert absent < ctx.mpf("1e-65")
    entropy=ctx.mpf(0)
    for i in range(5):
        for j in range(i+1,5):
            if path and (i,j) in ABSENT:continue
            f,g=pi[i]*q[i,j],pi[j]*q[j,i]
            entropy+=(f-g)*ctx.log(f/g)
    q0=source(ctx,z,delta)
    # Finite all-time equality certificate in high precision is a numerical
    # cross-check. Exact equality follows from the modal similarity identities.
    qk=q.copy();q0k=q0.copy()
    for mat in (qk,q0k):mat[0,1]=mat[1,0]=0
    reset=ctx.matrix([[0,1,0,0,0],[1,0,0,0,0]])
    exit=ctx.matrix([[1,0],[0,2],[0,0],[0,0],[0,0]])
    eq=[]
    for lam in map(ctx.mpf,("0.1","1","10","100")):
        aa=reset*(lam*ctx.eye(5)-qk)**-1*exit
        bb=reset*(lam*ctx.eye(5)-q0k)**-1*exit
        eq.append(max(abs(v) for v in aa-bb))
    assert max(eq)<ctx.mpf("1e-65")
    qn=np.array(q.tolist(),dtype=float)
    dirs=[]
    alloff=[(i,j) for i in range(5) for j in range(5) if i!=j]
    for i in range(2,5):
        for j in range(2,5):
            if i==j:continue
            K=np.zeros((5,5));K[i,j]=1;K[i,i]=-1
            dirs.append(qn@K-K@qn)
    full=np.array([[v[i,j] for v in dirs] for i,j in alloff])
    active=np.array([[v[i,j] for v in dirs] for i,j in sorted(ABSENT)])
    sfull=np.linalg.svd(full,compute_uv=False)
    sactive=np.linalg.svd(active,compute_uv=False)
    return {"entropy":str(entropy),"minimum_present_rate":str(min(positive)),
            "minimum_stationary_mass":str(min(pi)),"maximum_absent_rate_residual":str(absent),
            "maximum_resolvent_residual":str(max(eq)),
            "row_sum_residual":str(max(abs(sum(q[i,j] for j in range(5))) for i in range(5))),
            "orbit_jacobian_singular_values":sfull.tolist(),
            "active_zero_jacobian_singular_values":sactive.tolist(),
            "active_zero_jacobian_rank_at_relative_1e-10":int(sum(sactive>sactive[0]*1e-10)),
            "orbit_jacobian_rank_at_relative_1e-10":int(sum(sfull>sfull[0]*1e-10)),
            "generator":[[str(v) for v in row] for row in q.tolist()],
            "stationary":[str(v) for v in pi]}


def source_entropy(ctx,z,delta):
    q=source(ctx,z,delta);pi=stationary(ctx,q);total=ctx.mpf(0)
    for i in range(5):
        for j in range(i+1,5):
            if q[i,j]==q[j,i]==0:continue
            f,g=pi[i]*q[i,j],pi[j]*q[j,i]
            total+=(f-g)*ctx.log(f/g)
    return total


def continue_grid():
    ctx=mp.mp.clone();ctx.dps=DPS
    rows=[]
    for index in range(-20,21):
        delta=ctx.mpf(index)/40  # [-0.5,0.5], deterministic 41 nodes
        zc=critical(ctx,delta)
        V,p=triangle(ctx,zc,delta)
        q,w=realize(ctx,zc,delta,V)
        diag=diagnostics(ctx,zc,delta,q,True)
        assert min(w)>0 and diag["active_zero_jacobian_rank_at_relative_1e-10"]==5
        phases=[]
        for offset in ("-0.001","0","0.001"):
            z=zc+ctx.mpf(offset)
            p=numeric_parameters(ctx,z,delta)
            disc=p["f1"]**2-4*p["f0"]*p["f2"]
            candidates=[]
            if offset=="0":
                candidates=[diag]
            elif disc>0:
                for sign in (-1,1):
                    t=(-p["f1"]+sign*ctx.sqrt(disc))/(2*p["f2"])
                    VV,_=triangle(ctx,z,delta,t)
                    qq,_=realize(ctx,z,delta,VV)
                    candidate=diagnostics(ctx,z,delta,qq,True)
                    assert candidate["active_zero_jacobian_rank_at_relative_1e-10"]==6
                    candidates.append(candidate)
            phase={"z_offset":offset,"z":str(z),"discriminant":str(disc),
                   "active_boundary_path_candidate_count":len(candidates),"path_candidates":candidates}
            if offset=="-0.001":
                for exponent in range(2,15):
                    opening=ctx.mpf(10)**(-exponent)
                    VV,_=triangle(ctx,z,delta,opening=opening)
                    qq,_=realize(ctx,z,delta,VV)
                    try:proof=diagnostics(ctx,z,delta,qq,False)
                    except AssertionError:continue
                    phase["complete_realization"]={"opening_step":str(opening),**proof}
                    break
                assert "complete_realization" in phase
            phases.append(phase)
        tc=-p["f1"]/(2*p["f2"])
        # Derivatives are evaluated at the critical point, independently of
        # the phase loops. The 2x2 residual map (F,F_t) has full rank there.
        def f(t,z):
            pp=numeric_parameters(ctx,z,delta)
            return pp["f0"]+pp["f1"]*t+pp["f2"]*t*t
        pc=numeric_parameters(ctx,zc,delta);tc=-pc["f1"]/(2*pc["f2"])
        fz=ctx.diff(lambda zz:f(tc,zz),zc)
        ftt=2*pc["f2"]
        slope=-ctx.diff(lambda dd:polynomial(zc,dd),delta)/ctx.diff(lambda zz:polynomial(zz,delta),zc)
        rows.append({"delta":str(delta),"z_critical":str(zc),"slope":str(slope),
                     "P_delta_residual":str(abs(polynomial(zc,delta))),
                     "source_entropy":str(source_entropy(ctx,zc,delta)),"critical_path":diag,
                     "critical_triangle":[[str(v) for v in row] for row in V.tolist()],
                     "F_z":str(fz),"F_tt":str(ftt),
                     "det_d(F,Ft)_d(t,z)":str(-fz*ftt),"phases":phases})
    # Independent precision and formulation checks at selected original inputs.
    ctx2=mp.mp.clone();ctx2.dps=120
    precision=[]
    for delta in map(ctx2.mpf,("-0.5","0","0.5")):
        z=critical(ctx2,delta);V,_=triangle(ctx2,z,delta);q,_=realize(ctx2,z,delta,V)
        higher=diagnostics(ctx2,z,delta,q,True)
        original=next(r for r in rows if ctx2.mpf(r["delta"])==delta)
        error=abs(ctx2.mpf(original["critical_path"]["entropy"])-ctx2.mpf(higher["entropy"]))
        assert error<ctx2.mpf("1e-65")
        qn=np.array(q.tolist(),dtype=float);q0n=np.array(source(ctx2,z,delta).tolist(),dtype=float)
        for mat in (qn,q0n):mat[0,1]=mat[1,0]=0
        reset=np.array([[0,1,0,0,0],[1,0,0,0,0.]])
        exit=np.array([[1,0],[0,2],[0,0],[0,0],[0,0.]])
        err=max(np.max(np.abs(reset@(expm(qn*t)-expm(q0n*t))@exit)) for t in (0,.01,.1,1,10))
        assert err<1e-12
        precision.append({"delta":str(delta),"entropy_80_vs_120dps_absolute_difference":str(error),
                          "direct_time_domain_kernel_max_error_float64":float(err)})
    return rows,precision


def figures(rows):
    FIG.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({"font.family":"DejaVu Serif","font.size":9,"mathtext.fontset":"dejavuserif",
                         "axes.spines.top":False,"axes.spines.right":False,
                         "pdf.fonttype":42,"svg.fonttype":"none"})
    ds=np.array([float(r["delta"]) for r in rows]);zs=np.array([float(r["z_critical"]) for r in rows])
    fig,axs=plt.subplots(1,3,figsize=(7.15,2.7),layout="constrained")
    axs[0].plot(ds,zs,color="#26768B",lw=1.8)
    axs[0].axvspan(-.005,.005,color="#B23A31",alpha=.35,label="Certified local strip")
    axs[0].set(xlabel=r"Exit asymmetry $\delta$",ylabel=r"Critical $z_*(\delta)$",title="(a) Boundary curve")
    axs[0].legend(frameon=False,fontsize=6.5)
    axs[1].plot(ds,[float(r["source_entropy"]) for r in rows],color="#172A3A",label="Source")
    axs[1].plot(ds,[float(r["critical_path"]["entropy"]) for r in rows],color="#B23A31",label="Path")
    axs[1].set(xlabel=r"Exit asymmetry $\delta$",ylabel=r"Network entropy rate $\sigma$",title="(b) Entropy at boundary")
    axs[1].legend(frameon=False,fontsize=7)
    node=rows[len(rows)//2]
    p=numeric_parameters(mp.mp,float(node["z_critical"]),0)
    tc=float(-p["f1"]/(2*p["f2"]))
    ts=np.linspace(tc-.13,tc+.13,301)
    for dz,color in [(-.001,"#26768B"),(0,"#172A3A"),(.001,"#B23A31")]:
        p=numeric_parameters(mp.mp,float(node["z_critical"])+dz,0)
        ys=[float(p["f0"]+p["f1"]*t+p["f2"]*t*t) for t in ts]
        axs[2].plot(ts,ys,color=color,label=f"{dz:+.3f}" if dz else "0")
    axs[2].axhline(0,color=".5",lw=.6)
    axs[2].set(xlabel=r"Triangle parameter $t$",ylabel=r"Envelope numerator $F$",title="(c) Feasibility: $F\geq0$")
    axs[2].legend(title=r"$z-z_*(0)$",frameon=False,fontsize=6.5,title_fontsize=7)
    for ax in axs:ax.grid(alpha=.18)
    for ext in ("pdf","svg","png"):fig.savefig(FIG/("continuation."+ext),dpi=300)
    plt.close(fig)
    V=np.array(node["critical_triangle"],dtype=float)
    p=numeric_parameters(mp.mp,float(node["z_critical"]),0)
    fig,axs=plt.subplots(1,2,figsize=(7.15,3.1),layout="constrained")
    # An invertible vertical scaling preserves all incidences and the flow.
    scale=1/float(V[2].max())
    vertices=V[1:].T.copy();vertices[:,1]*=scale
    vertices=np.vstack([vertices,vertices[0]])
    for ax in axs:
        xx=np.linspace(-2.9,2.4,500)
        lower=np.maximum(float(p["L"])*(-float(p["m"])-xx),float(p["R"])*(xx-1))*scale
        ax.fill_between(xx,lower,1.2,color="#EEF2F3")
        ax.plot(xx,lower,color="#71828D",lw=1)
        ax.fill(vertices[:,0],vertices[:,1],color="#26768B",alpha=.10)
        ax.plot(vertices[:,0],vertices[:,1],color="#26768B",lw=1.5)
        ax.scatter([1,-float(p["m"])],[float(p["A"])*scale,float(p["B"])*scale],c="#B23A31",s=25,zorder=4)
        ax.scatter([0],[0],color="#172A3A",s=17,zorder=5)
        ax.set_xlabel(r"Modal coordinate $u$")
        ax.grid(alpha=.15)
    axs[0].set(xlim=(-2.8,2.3),ylim=(-.025,1.08),ylabel=r"Rescaled height $v/Q_v$",title="(a) Critical invariant triangle")
    axs[0].annotate("High vertex",vertices[1],xytext=(1.0,.83),arrowprops={"arrowstyle":"->","lw":.7},fontsize=8)
    axs[1].set(xlim=(-2.8,1.35),ylim=(-.0012,.075),title="(b) Inputs and active faces")
    axs[1].annotate(r"$(-m,B_0)$",(-float(p["m"]),float(p["B"])*scale),xytext=(-2.1,.059),fontsize=8,arrowprops={"arrowstyle":"->","lw":.7})
    axs[1].annotate(r"$(1,A)$",(1,float(p["A"])*scale),xytext=(-.1,.065),fontsize=8,arrowprops={"arrowstyle":"->","lw":.7})
    axs[1].annotate("Origin",(0,0),xytext=(-.85,.013),fontsize=8,arrowprops={"arrowstyle":"->","lw":.7})
    for ext in ("pdf","svg","png"):fig.savefig(FIG/("realization-geometry."+ext),dpi=300)
    plt.close(fig)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--figures-only",action="store_true")
    args=parser.parse_args()
    if args.figures_only:
        figures(json.loads(OUT.read_text())["numerical_continuation"])
        return
    certificate=exact_certificate()
    rows,precision=continue_grid()
    figures(rows)
    inputs=[Path(__file__),ROOT/"manuscript/supplementary/proofs.tex",ROOT/"analysis/check_balanced_cone_bound.py",
            ROOT/"analysis/check_balanced_cone_sufficiency.py",ROOT/"outputs/balanced-fold-checks.json"]
    result={"all_checks_passed":True,"command_from_root":".venv/Scripts/python.exe -B analysis/revision/continuation.py",
            "environment":{"python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__,
                           "numpy":np.__version__,"scipy":scipy.__version__,"matplotlib":matplotlib.__version__},
            "input_sha256":{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
            "random_seed":None,"precision_digits":DPS,"exact_certificate":certificate,
            "numerical_continuation":rows,"cross_checks":precision,
            "numerical_scope":{"delta":"41 nodes in [-0.5,0.5], step 0.025","z_offsets":["-0.001","0","0.001"],
                               "counts":"active-boundary path candidates only; never total fiber counts outside proved local rectangle",
                               "rank_tolerance":"float64 relative 1e-10; rank results are diagnostics",
                               "positivity":"present rates strictly positive at 80 dps; structurally zero rates excluded from entropy and checked <1e-65; no clipping or reverse epsilons",
                               "wider_range_status":"numerical evidence, not interval-certified feasibility or an exhaustive off-balanced theorem"}}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    mid=rows[len(rows)//2]
    print(json.dumps({"all_checks_passed":True,"output":str(OUT),"critical_slope_at_zero":mid["slope"],
                      "local_certificate_rectangle":certificate["rectangle"],"continued_nodes":len(rows)},indent=2))


if __name__=="__main__":
    main()
