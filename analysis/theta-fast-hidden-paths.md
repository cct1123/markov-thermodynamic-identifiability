# Hidden-path support audit for theta(100,100)

Date: 2026-09-10 UTC. Contribution: exhaustive visible-incidence reduction, exact rational elimination and polynomial sign certificates. Input is the committed theta family at \(a=b=100\), with the conventions in [theta-fast-case-audit.md](theta-fast-case-audit.md): five-state cap, known resolved pair \(x\leftrightarrow y\), simple bidirected irreducible CTMCs, and the complete joint waiting kernel. No new stochastic or parameter search was run. No novelty claim is made.

## Result and scope

Every compatible generator whose three hidden states form a path falls into one of two classes:

1. Its visible-incidence pattern immediately triggers the existing hidden-pair unboundedness theorem.
2. Its pattern is one of four residual patterns, all of which are impossible for a connected hidden path.

Thus **any connected hidden-path alternative would imply unbounded entropy**. Together with the already proved uniqueness among disconnected hidden blocks and the triangle-to-pair argument, this independently shows that the theta(100,100) entropy fiber cannot be bounded but nonunique: it is either a singleton or unbounded.

This path argument does not by itself exclude the path patterns in the first class. It is a support check independent of a global connected-hidden feasibility proof, not a claim that every hidden path has been excluded by the calculations below.

The separate [spectral-cone proof](theta-fast-spectral-audit.md) now excludes every connected hidden realization and establishes global uniqueness. This note preserves the independent support-elimination result and its exact certificate.

## 1. Data fixed by the waiting kernel

The visible block and the hidden response \(F(z)=X(zI-H)^{-1}Y\) are fixed. The source blocks are
\[
X=\begin{pmatrix}2&0&8\\0&7&11\end{pmatrix},\quad
Y=\begin{pmatrix}3&0\\0&6\\100&100\end{pmatrix},\quad
H=\begin{pmatrix}-7&4&0\\5&-11&0\\0&0&-200\end{pmatrix}.
\]
The zeroth and first time-domain hidden-response moments are
\[
M_0=XY=\begin{pmatrix}806&800\\1100&1142\end{pmatrix},
\qquad
M_1=XHY=\begin{pmatrix}-160042&-159952\\-219895&-220462\end{pmatrix}. \tag{1}
\]
These are not values of the Laplace transfer at \(z=0\).

The kernel is minimal of dimension five. Hence every model under the cap has exactly three hidden states and lies in the normalized hidden-similarity class. The nonsingular exit chart is
\[
C=[Y,\mathbf1],\qquad \det C=-882,
\]
\[
D=C^{-1}HC=
\begin{pmatrix}
-20579/147&-18524/147&-1\\
-18815/294&-11467/147&-1\\
19550/49&19700/49&0
\end{pmatrix}.                                         \tag{2}
\]
Every compatible exit chart \(C'=[Y',\mathbf1]\) is nonsingular because \(C'=U^{-1}C\). Its hidden generator is \(H'=C'D(C')^{-1}\).

The fixed visible entrance totals are \(10,18\), and the corresponding exit-plane anchor points are
\[
p=(403/5,80),\qquad q=(550/9,571/9).                    \tag{3}
\]
These values follow from the rows of \(XC\), divided by their respective totals.

## 2. Exhaustive reduction of visible-incidence patterns

Label the hidden path \(h-k-l\). Let \(S_i\subseteq\{x,y\}\) be the visible neighbors of hidden state \(i\); bidirectionality makes entrance and exit supports agree.

For the adjacent pair \(h,k\), their full external neighborhoods are
\[
N_h=S_h,\qquad N_k=S_k\cup\{l\}.
\]
Thus \(S_h\subseteq S_k\) gives an adjacent nested pair, which implies unbounded entropy by [hidden-pair-boundary-audit.md](hidden-pair-boundary-audit.md). The same applies if \(S_l\subseteq S_k\).

If \(S_h=S_l\), the nonadjacent endpoints are external twins:
\[
N_h=S_h\cup\{k\}=N_l.
\]
The same theorem gives unbounded entropy, regardless of endpoint escape ordering, when topology is unknown.

It remains to examine
\[
S_h\nsubseteq S_k,\qquad S_l\nsubseteq S_k,\qquad S_h\ne S_l. \tag{4}
\]
A middle state seeing both visible ports is impossible under (4), and both endpoints must have a nonempty visible neighborhood. Since \((M_0)_{xy}>0\), at least one hidden state must see both ports: every summand in \(M_{0,xy}=\sum_iX_{xi}Y_{iy}\) is nonnegative and is positive exactly for a shared visible neighbor.

These restrictions leave exactly the following four patterns, up to reflection of the hidden path:

| \(S_h\) | \(S_k\) | \(S_l\) |
| --- | --- | --- |
| \(\{x\}\) | \(\varnothing\) | \(\{x,y\}\) |
| \(\{y\}\) | \(\varnothing\) | \(\{x,y\}\) |
| \(\{x\}\) | \(\{y\}\) | \(\{x,y\}\) |
| \(\{y\}\) | \(\{x\}\) | \(\{x,y\}\) |

For example, if the middle sees only \(x\), each endpoint must see \(y\); unequal endpoint neighborhoods then force \(\{y\}\) and \(\{x,y\}\). The other middle choices give the remaining rows. The checker also verifies this finite subset classification exhaustively. No rate grid is involved. The additional escape-order test for nested nonadjacent endpoints is not needed below.

## 3. First moments exclude an empty hidden middle

For the first pattern, \(y\) attaches only to endpoint \(l\), while \(x\) attaches to \(h,l\). Since \(H_{hl}=0\) and the middle has no visible links,
\[
(M_1)_{xy}=-\lambda_l(M_0)_{xy},\qquad
(M_1)_{yy}=-\lambda_l(M_0)_{yy}.
\]
But the moments in (1) give
\[
(M_1)_{xy}(M_0)_{yy}-(M_0)_{xy}(M_1)_{yy}
=-6295584\ne0.
\]
This is an exact contradiction. For the second pattern, exchange \(x,y\); the necessary equality instead fails by
\[
(M_1)_{yx}(M_0)_{xx}-(M_0)_{yx}(M_1)_{xx}
=-1189170\ne0.
\]
Thus both empty-middle patterns are excluded globally.

## 4. One-variable reduction for the two remaining patterns

First take \(S_h=\{x\}, S_k=\{y\}, S_l=\{x,y\}\). Write the exit rows as
\[
Y'_h=(u,0),\qquad Y'_k=(0,v),\qquad Y'_l=(A,B),
\qquad u,v,A,B>0.
\]
The symbols \(u,v\) are visible exit rates, not the total hidden-state escape rates.

Use six coefficients from (2):
\[
a_1=D_{11},\quad a_2=D_{12},\quad
b_1=D_{21},\quad b_2=D_{22},\quad c_1=D_{31},\quad c_2=D_{32}.
\]
The exit-plane vector field is
\[
g_x(A,B)=A^2+AB+a_1A+b_1B+c_1,\quad
g_y(A,B)=AB+B^2+a_2A+b_2B+c_2.                          \tag{5}
\]
At any hidden vertex \(P_i\),
\[
g(P_i)=\sum_{j\ne i}H'_{ij}(P_j-P_i).
\]

Because \(h\) is an endpoint adjacent only to \(k\) within the hidden block, put \(m=H'_{hk}>0\). Then
\[
g_x(u,0)=-mu<0,\qquad g_y(u,0)=mv>0.
\]
Consequently
\[
v=-\frac{u(a_2u+c_2)}{u^2+a_1u+c_1}.                 \tag{6}
\]

Entrance incidence forces \(p\) from (3) onto the open edge joining \((u,0)\) to \((A,B)\), and \(q\) onto the open edge joining \((0,v)\) to \((A,B)\). Define
\[
c=\frac{p_x-u}{p_y},\qquad d=\frac{q_y-v}{q_x}.
\]
The shared vertex is therefore fixed by
\[
A=u+cB,\qquad B=v+dA,
\]
or
\[
A=\frac{u+cv}{1-cd},\qquad B=\frac{v+du}{1-cd}.        \tag{7}
\]
All rates have now been reduced to rational functions of \(u\).

The missing reverse edge \(l\to h\) gives one final necessary equation:
\[
\Phi(u):=A\,g_y(A,B)+(v-B)g_x(A,B)=0.                 \tag{8}
\]
Indeed \(\Phi(u)/\det C'=H'_{lh}\). The exact checker confirms this identity against direct matrix conjugation.

### No physical singular cases are lost

The denominator in (6) equals \(-mu<0\), so it cannot vanish in a connected bidirected path. In (7), a vanishing \(1-cd\) makes the two anchor-line equations either inconsistent or coincident. In the coincident case, \((u,0),(0,v),(A,B)\) are collinear, contradicting \(\det C'\ne0\). Thus every physical candidate is in the rational chart used for the elimination.

Cancelling polynomial factors while forming rational functions cannot remove a physical solution: all these original denominators are nonzero there. Additional zeros of the final denominator are likewise outside the physical domain.

For the last visible-incidence pattern, exchange the two visible coordinates. Equations (5)–(8) remain valid after
\[
(a_1,a_2,b_1,b_2,c_1,c_2)
\mapsto(b_2,b_1,a_2,a_1,c_2,c_1),
\]
and
\[
(p_x,p_y,q_x,q_y)\mapsto(q_y,q_x,p_y,p_x).
\]
The scalar \(u\) then denotes the \(y\)-only endpoint exit rate. This accounts for both remaining patterns, not just one orientation.

## 5. Exact polynomial exclusions

Substitute (6)–(7) into (8), reduce the rational function, and make its numerator a primitive integer polynomial. The result factors as follows, up to a nonzero overall constant; the factor \(u\) has no root in the positive physical domain:
\[
\operatorname{num}\Phi_x(u)=u(u-3)P_x(u),\qquad
\operatorname{num}\Phi_y(u)=u(u-6)P_y(u).              \tag{9}
\]
The coefficients in the following lists are ordered from constant term to degree six:
\[
\begin{aligned}
P_x:\ [&6795757108159032937500,\quad
2803167844993931242500,\\
&-8801651567495855699325,\quad
-2678255044753626096678,\\
&-591548240074648696848,\quad
-59085567980076927630,\quad
-1949901507081235775],\\[2mm]
P_y:\ [&11040703820013481200000,\quad
-14933195710419027348000,\\
&-3986346390515229397320,\quad
845827447059675263826,\\
&-280680097299813200457,\quad
3179611303879586274,\quad
57126221020570157].
\end{aligned}                                       \tag{10}
\]

For the \(x\)-only endpoint, physicality requires \(u>1\): if \(0<u\le1\), then
\[
g_x(u,0)\ge\frac{19550}{49}-\frac{20579}{147}
=\frac{38071}{147}>0,
\]
contrary to \(g_x(u,0)=-mu<0\). The descending coefficient sequence of \(P_x\) has exactly one sign change, so Descartes' rule gives exactly one positive root, counting multiplicity. Since \(P_x(0)>0\) and
\[
P_x(1)=-2533565368658324476256<0,
\]
that root lies below one. Therefore the only possible physical root in (9) is \(u=3\).

For the \(y\)-only endpoint, \(u>5\), since for \(0<u\le5\),
\[
g_x(u,0)\ge\frac{19700}{49}-5\frac{11467}{147}
=\frac{1765}{147}>0.
\]
Also \(g_y(u,0)>0\) gives
\[
u<\frac{23460}{3763}<7.
\]
Write the degree-six Bernstein expansion on \([5,7]\),
\[
P_y(5+2t)=\sum_{j=0}^6 B_j\binom6j t^j(1-t)^{6-j}.
\]
Its exact coefficients are
\[
\begin{aligned}
(B_0,\ldots,B_6)=(&-222151681896816116971000,\\
&-262382431152563743375250,\\
&-310317414229024637097928,\\
&-1837443267871824524263798/5,\\
&-2178099618086793852019256/5,\\
&-516600652645071258880442,\\
&-612456168602395564601608).
\end{aligned}
\]
All are strictly negative; the Bernstein basis is nonnegative and sums to one on that interval. Thus \(P_y<0\) on the entire physical interval, leaving only \(u=6\).

Finally (6)–(7) give
\[
(u,v,A,B)=(3,6,100,100)
\]
in the first orientation, and \((6,3,100,100)\) after exchanging ports. These reconstruct the source, up to hidden labels. Its shared hidden state has no link to the other two: in particular \(H'_{kl}=H'_{lk}=0\). Neither root is a connected hidden path.

This excludes both remaining patterns and completes the exhaustive conditional result stated at the start.

## 6. Reproduction and provenance

The exact rational elimination and certificates were executed with Python 3.9.12 and its standard library. Inputs are (1)–(3), the finite visible-incidence sets and the two endpoint orientations. There is no random seed or external dataset. Approximate polynomial roots were inspected during derivation to select convenient exact sign certificates; no approximate root or optimizer result is used in the proof.

The embedded checker regenerates the rational functions and primitive polynomial factors, checks every coefficient in (10), verifies the two moment contradictions, the finite incidence reduction, the Descartes signs and Bernstein coefficients, and the reconstructed source rates. It also evaluates the formulas at one rational diagnostic point in each orientation and checks the missing-edge identities by direct matrix conjugation. These diagnostics verify algebraic identities; they are not claimed as physical alternative generators.

Run from the repository root:

~~~powershell
python -B -c "from pathlib import Path; t=Path('analysis/theta-fast-hidden-paths.md').read_text(encoding='utf-8'); exec(t.rsplit('<!-- HIDDEN_PATH_CHECK -->',1)[1].split(chr(96)*3+'python',1)[1].split(chr(96)*3,1)[0])"
~~~

Accepted output reports the two residual coefficient lists, the seven negative Bernstein coefficients, roots 3 and 6 reconstructing the disconnected source, and:
`All exact moment, incidence, polynomial, sign and chart checks passed.`

<!-- HIDDEN_PATH_CHECK -->

```python
from fractions import Fraction as F
def trim(p):
    p=list(p)
    while len(p)>1 and not p[-1]: p.pop()
    return p
def add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for i,x in enumerate(p):r[i]+=x
    for i,x in enumerate(q):r[i]+=x
    return trim(r)
def neg(p):return [-x for x in p]
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return trim(r)
def divmodp(p,q):
    p=trim(p);q=trim(q)
    if q==[0]:raise ZeroDivisionError
    r=[F(0)]*max(1,len(p)-len(q)+1)
    while len(p)>=len(q) and p!=[0]:
        k=len(p)-len(q);c=p[-1]/q[-1];r[k]=c
        p=add(p,neg([F(0)]*k+[c*x for x in q]))
    return trim(r),p
def gcd(p,q):
    while q!=[0]:p,q=q,divmodp(p,q)[1]
    return [x/p[-1] for x in p]
class R:
    def __init__(self,n,d=None):
        self.n=[F(x) for x in n] if isinstance(n,list) else [F(n)]
        self.d=[F(1)] if d is None else [F(x) for x in d]
        g=gcd(self.n,self.d)
        self.n=divmodp(self.n,g)[0];self.d=divmodp(self.d,g)[0]
        c=self.d[-1];self.n=[x/c for x in self.n];self.d=[x/c for x in self.d]
    def __add__(self,o):
        o=o if isinstance(o,R) else R(o)
        return R(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
    __radd__=__add__
    def __neg__(self):return R(neg(self.n),self.d)
    def __sub__(self,o):return self+-rr(o)
    def __rsub__(self,o):return rr(o)+-self
    def __mul__(self,o):
        o=rr(o);return R(mul(self.n,o.n),mul(self.d,o.d))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=rr(o);return R(mul(self.n,o.d),mul(self.d,o.n))
    def __rtruediv__(self,o):return rr(o)/self
    def __repr__(self):return str(([str(x) for x in self.n],[str(x) for x in self.d]))
def rr(x):return x if isinstance(x,R) else R(x)
def primitive(p):
    import math,functools
    scale=functools.reduce(lambda a,b:a*b//math.gcd(a,b),[x.denominator for x in p],1)
    vals=[int(x*scale) for x in p]
    g=functools.reduce(math.gcd,vals)
    return [x//g for x in vals]
def evaluate(p,x):
    value=0
    for c in reversed(p):value=value*x+c
    return value

def derive(swap=False):
    aa,bb,cc,dd,ee,ff=F(-20579,147),F(-18524,147),F(-18815,294),F(-11467,147),F(19550,49),F(19700,49)
    px,py,qx,qy=F(403,5),F(80),F(550,9),F(571,9)
    sourceu=F(3)
    if swap:
        aa,bb,cc,dd,ee,ff=dd,cc,bb,aa,ff,ee
        px,py,qx,qy=qy,qx,py,px
        sourceu=F(6)
    u=R([0,1])
    gx=u*u+aa*u+ee;gy=bb*u+ff
    v=-u*gy/gx
    c=(px-u)/py;d=(qy-v)/qx
    A=(u+c*v)/(1-c*d);B=(v+d*u)/(1-c*d)
    Gx=A*A+A*B+aa*A+cc*B+ee
    Gy=A*B+B*B+bb*A+dd*B+ff
    phi=A*Gy+(v-B)*Gx
    polynomial=[F(x) for x in primitive(phi.n)]
    factors=[F(0),sourceu]
    for root in factors:
        polynomial,remainder=divmodp(polynomial,[-root,F(1)])
        assert remainder==[0]
    residual=primitive(polynomial)
    return dict(u=u,v=v,A=A,B=B,phi=phi,residual=residual,sourceu=sourceu,
                D=[[aa,bb,F(-1)],[cc,dd,F(-1)],[ee,ff,F(0)]])
def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def inverse(a):
    n=len(a);r=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        i=next(i for i in range(j,n) if r[i][j])
        r[j],r[i]=r[i],r[j]
        pivot=r[j][j];r[j]=[x/pivot for x in r[j]]
        for i in range(n):
            if i!=j:
                scale=r[i][j];r[i]=[x-scale*y for x,y in zip(r[i],r[j])]
    return [row[n:] for row in r]
def ev(r,u):return evaluate(r.n,u)/evaluate(r.d,u)
def chart_check(d,u):
    v,A,B=[ev(d[name],u) for name in ('v','A','B')]
    C=[[u,F(0),F(1)],[F(0),v,F(1)],[A,B,F(1)]]
    H=mm(mm(C,d['D']),inverse(C))
    det=u*v-u*B-v*A
    assert H[0][2]==0
    assert H[2][0]*det==ev(d['phi'],u)
    return v,A,B,H
def bernstein(p,a,b):
    from math import comb
    n=len(p)-1
    monomial=[sum(F(p[i])*comb(i,j)*a**(i-j)*(b-a)**j for i in range(j,n+1)) for j in range(n+1)]
    return [sum(monomial[i]*F(comb(k,i),comb(n,i)) for i in range(k+1)) for k in range(n+1)]
PX=[6795757108159032937500,2803167844993931242500,-8801651567495855699325,-2678255044753626096678,-591548240074648696848,-59085567980076927630,-1949901507081235775]
PY=[11040703820013481200000,-14933195710419027348000,-3986346390515229397320,845827447059675263826,-280680097299813200457,3179611303879586274,57126221020570157]
X=[[F(2),F(0),F(8)],[F(0),F(7),F(11)]]
Y=[[F(3),F(0)],[F(0),F(6)],[F(100),F(100)]]
H=[[F(-7),F(4),F(0)],[F(5),F(-11),F(0)],[F(0),F(0),F(-200)]]
M0,M1=mm(X,Y),mm(mm(X,H),Y)
assert M0==[[806,800],[1100,1142]]
assert M1==[[-160042,-159952],[-219895,-220462]]
assert M1[0][1]*M0[1][1]-M0[0][1]*M1[1][1]==-6295584
assert M1[1][0]*M0[0][0]-M0[1][0]*M1[0][0]==-1189170
C=[[F(3),F(0),F(1)],[F(0),F(6),F(1)],[F(100),F(100),F(1)]]
first=derive(False)
assert mm(mm(inverse(C),H),C)==first['D']
ports=[frozenset(),frozenset('x'),frozenset('y'),frozenset('xy')]
residual_supports=set()
for a in ports:
    for b in ports:
        for c in ports:
            if a<=b or c<=b or a==c:continue
            if frozenset('xy') not in (a,b,c):continue
            if a==frozenset('xy'):a0,c0=c,a
            else:a0,c0=a,c
            residual_supports.add((''.join(sorted(a0)),''.join(sorted(b)),''.join(sorted(c0))))
assert residual_supports=={('x','','xy'),('y','','xy'),('y','x','xy'),('x','y','xy')}
for swap,expected in [(False,PX),(True,PY)]:
    d=derive(swap)
    assert d['residual']==expected
    if not swap:
        assert expected[0]>0 and expected[1]>0 and all(x<0 for x in expected[2:])
        assert evaluate(expected,F(1))==-2533565368658324476256
        assert F(19550,49)+F(-20579,147)>0
    else:
        bs=bernstein(expected,F(5),F(7))
        assert all(x<0 for x in bs)
        assert F(19700,49)+5*F(-11467,147)==F(1765,147)>0
        assert F(23460,3763)<7
        print('y_case_Bernstein_coefficients',[str(x) for x in bs])
    chart_check(d,d['sourceu']+F(1,10))
    v,A,B,Hn=chart_check(d,d['sourceu'])
    assert (v,A,B)==(F(3 if swap else 6),F(100),F(100))
    assert Hn[1][2]==Hn[2][1]==0
    print('case','y_endpoint' if swap else 'x_endpoint','residual_coefficients',expected,
          'only_physical_root',str(d['sourceu']),'source_reconstructed',True)
print('All exact moment, incidence, polynomial, sign and chart checks passed.')
import platform
print('Python',platform.python_version(),'standard library only; no random input')
```
