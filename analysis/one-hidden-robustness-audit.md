# One hidden state: exact identification versus local entropy continuity

Independent analytic and symbolic audit, 2026-09-10 UTC. Assumptions are those in [formulation.md](formulation.md): known endpoints of one resolved bidirected observed edge, simple bidirected irreducible row CTMCs, at most three states, natural-log stationary entropy, and unknown hidden topology. Impose a common upper bound `M` on individual off-diagonal rates. Missing edges have both rates zero. This note independently checks the proposed example; it does not certify publication novelty.

## Answer and precise boundary

For a source with exactly three states, the generator is locally continuous as a function of the complete observed kernels within this bounded-rate class, including at a hidden-leaf tree. Entropy is locally continuous at a triangle with all six rates positive. At a tree, arbitrarily close triangle observations can have arbitrarily large entropy even with all rates at most one in the explicit example below. Thus exact generator identification does not suffice for entropy continuity at a paired-zero edge.

The kernel distance used here is the maximum, over the two visible reset states, of total variation distance between the joint next-mark/time probability laws. The continuity conclusion also holds if the distance is instead TV between stationary marked-record laws on any fixed window `[0,H]`, `H>0`; a justification is given below. These are population-law continuity statements, not a constructive finite-sample estimator or a uniform conditioning bound over all positive triangles.

## Explicit three-state divergence

Use state order `(x,y,h)` and observe only `x <-> y`. For `0<e<1`, let `k=exp(-1/e^2)` and

```text
Q(e,k) = [[-1-e,  1,    e],
          [1,     -2,   1],
          [k,      1,  -1-k]].
Q0 = Q(0,0).
```

Every perturbed generator is a complete bidirected triangle, and all off-diagonal rates are at most one. The limit is the connected tree `x-y-h`. Direct stationary and current calculations give

```text
Z = 3(1+e+k),
pi = (1+2k, 1+e+k, 1+2e)/Z,
J = (e-k)/Z,
sigma(Q(e,k)) = J log(e/k).
```

Here `J` is the common current in the cycle orientation `x -> h -> y -> x`. In particular, `pi_y=1/3`, `pi -> (1,1,1)/3`, and

```text
e sigma(Q(e,exp(-1/e^2))) -> 1/3.
```

Hence entropy diverges while the generator converges entrywise to the reversible tree. All entropies along the sequence are finite. The limiting missing edge contributes zero in the tree; continuity of the expression `flux difference * log(flux ratio)` cannot be assumed when both edge rates vanish at unequal speeds.

This extends to any positive-rate three-state tree in this observation scheme. Write its existing rates as `r=q_xy`, `s=q_yx`, `v=q_yh`, `w=q_hy`; add `q_xh=e` and `q_hx=k`. The cycle current is `(e*w*s-k*r*v)/Z(e,k)`, where the stationary tree-weight normalizer obeys `Z(e,k)->s*w+r*w+r*v>0`. Its affinity is `log(e*w*s/(k*r*v))`. The same choice `k=exp(-1/e^2)` makes entropy asymptotic to `w*s/[e(s*w+r*w+r*v)]`. The mirror tree follows by exchanging the visible labels. Choosing the added rates small respects any common bound `M` already containing the source rates. Restricting competitors to the source tree would remove this failure: every such tree is reversible.

## Full minimal dimension and exact uniqueness

For the explicit example, remove only the two observed off-diagonal entries to form `T`. Set

```text
R = [[0,1,0],[1,0,0]],  B = [[1,0],[0,1],[0,0]].
```

The reachability minor formed from the two columns of `B` and `T B[:,1]` is exactly `1`. The observability minor formed from the two rows of `R` and `(R T)[0,:]` is exactly `-1`. These identities hold for every `e,k`, including zero. Thus the whole sequence and the tree have minimal linear realization dimension three. No spare state or order reduction explains the construction.

For completeness, the derivative reconstruction in [the small-network audit](small-network-audit.md#1-identification-for-at-most-three-states) extends to **closed nonnegative generators**, without assuming irreducibility of the candidate limit. Write

```text
q_xy=r, q_yx=s, q_xh=a, q_yh=c, q_hx=b, q_hy=d.
T = [[-r-a,0,a],[0,-s-c,c],[b,d,-b-d]].
```

The zero-time observed kernel fixes `r,s>0`. Let `K(u)` be the visible principal block of `exp(Tu)`, obtained by swapping the kernel rows and dividing its columns by `r,s`. Then

```text
a = -K'xx(0)-r,                  c = -K'yy(0)-s,
K''xx(0) = (r+a)^2+a*b,          K''xy(0) = a*d,
K''yx(0) = c*b,                  K''yy(0) = (s+c)^2+c*d.
```

If `a>0`, divide the first row's second-order identities by `a` to recover `b,d`. Otherwise the three-state source has `c>0`, and the second row recovers `b,d`. For `Q0`, the recovered values are `r=s=c=d=1`, `a=b=0`. This pins even a possibly reducible or one-way closed candidate to the original tree. A two-state candidate, padded with one isolated zero row/column, has `a=c=0` and cannot produce these source data. Every perturbed triangle is likewise globally unique under the cap of three.

Every irreducible bidirected three-state model with this observed edge is linearly minimal: both visible states are directly selected by `R,B`; some hidden entrance is positive, supplying the third observable coordinate; and some hidden exit is positive, supplying the third reachable coordinate. With at most two states, stationary entropy is identically zero. Therefore three is the smallest cap, and the smallest fixed minimal dimension, exhibiting this finite-precision divergence. This differs from an exact unbounded fiber: each exact three-state data fiber here is a singleton.

## Why positive triangles retain local continuity

Let `Qn` be any admissible sequence with at most three states, rates at most `M`, and kernels converging in row TV to a source `Q*` with exactly three states. Pad two-state candidates by an isolated hidden state. Their six off-diagonal entries lie in the compact cube `[0,M]^6`. Any subsequence has a further subsequence converging to a nonnegative row generator `Qbar`; it need not be irreducible or bidirected.

Matrix-exponential continuity implies that its kernel densities converge uniformly on each bounded time interval to those of `Qbar`. Row TV convergence forces those continuous limit densities to equal the source densities. Equality on an interval implies equality of their analytic derivatives at zero. The reconstruction above then pins `Qbar=Q*`, since the source has at least one positive hidden entrance. Every subsequential limit is the source, so `Qn -> Q*`.

For an all-positive triangle, all six rates are eventually bounded away from zero. The normalized stationary vector is continuous at the irreducible source, and its components are positive. Every entropy term is consequently continuous, giving `sigma(Qn)->sigma(Q*)`. No irreducibility assumption on an unverified subsequential limit was used: irreducibility follows after reconstructing the limit as the source.

For the alternative stationary-window metric, compactness applies jointly to `(Qn,pi_n)`. The observed count is uniformly dominated by a Poisson count of rate `M`, so TV convergence of record laws transfers expected mark counts and expected consecutive-mark pair counts. A stationary model has mean number of marks `I` equal to `H nu_I`, and consecutive `I,J` pairs with lag in `du`, `0<u<H`, have mean measure `(H-u) nu_I psi_IJ(u) du`. Both source intensities `nu_I` are positive. Therefore any compact limit has the source kernels on `(0,H)`, and analyticity plus the same reconstruction again gives `Qbar=Q*`. This supplies the stated stationary-window version without treating TV convergence as unrestricted continuity of numerical differentiation.

## Explicit distances and a confidence consequence

At arbitrary positive `e,k`, stationary initial distributions differ from the uniform tree law in TV by

```text
delta = |e-k|/[3(1+e+k)].
```

Couple these initial states maximally, and then couple the tree paths until the first added-edge jump. The added hazard is at most `m=max(e,k)`. Thus the stationary marked-record distance on `[0,H]` is at most

```text
delta + 1-exp(-m H) <= delta+m H.
```

For `k=exp(-1/e^2)` and `0<e<1`, this is at most `e(1/3+H)`. Applying any common rounding/noise mechanism to the coupled records preserves the bound. A finite number of independent stationary windows also converges in TV, using the sum of their individual coupling bounds.

From a fixed visible reset, the tree's next-mark mean vector solves `-T0 u=1` and equals `(1,2,3)` in state order `(x,y,h)`. Coupling up to that mark gives row TV at most `2m`; `n` successive marked waits have TV at most `2nm`. Thus the divergence occurs in the full joint-kernel metric as well as every fixed finite-window experiment.

The direct statistical consequence needs no exact common law at fixed `e`. If an extended-real upper bound `U` has coverage at least `1-alpha` for every admissible model, choose this sequence with entropy tending to infinity and finite-experiment laws `Pn` converging in TV to `P0`. For every finite `L`, eventually `sigma(Qn)>=L`, hence `P0(U>=L)>=1-alpha-d_TV(Pn,P0)`. First let `n` tend to infinity, then `L` tend to infinity. It follows that `P0(U=infinity)>=1-alpha`. This is the direct argument already compared with statistical prior art in [the four-state independent check](finite-precision-independent-check.md); no additional statistical theorem is imported here.

Local continuity at a positive triangle does **not** assert existence of a globally honest, almost surely finite upper confidence bound there. For a stationary finite window, every tree record has alternating observed marks. Any irreducible competitor with positive rates on the observed edge gives positive density to every such finite mark/time record: the path can start at the first mark's source and make only the specified alternating visible jumps. The empty record also has positive probability. With counting measure on mark strings and Lebesgue measure on ordered time simplices, plus the empty-record atom, this proves `P0 << P_Q`. Therefore `P0(U=infinity)>0` forces `P_Q(U=infinity)>0`, including at any fixed positive triangle, if coverage is required over the whole class containing the divergent sequence.

For the subfamily with both observed rates fixed at one, the transfer has an explicit constant. A tree record density is at most one because each killed semigroup and unit-rate mark matrix is substochastic. The direct alternating path in a fixed competitor has density at least `c=min(pi_x,pi_y)*exp(-lambda_max H)>0`, where `lambda_max` is its largest exit rate. For the empty record, no jumps has probability at least `exp(-lambda_max H)>=c`. Consequently `P_Q >= c P0` as measures and `P_Q(U=infinity)>=c(1-alpha)`. The density comparison does not claim a common constant for arbitrary observed rates: repeated marks would introduce additional rate products. The unquantified absolute-continuity conclusion still holds. Common observation rounding preserves both absolute continuity and the stated measure domination.

## Executed validation

The following embedded code was run from the project root with Python 3.9.12 / SymPy 1.14.0 in `.venv`; no randomness or seed is involved. It checks the stationary law, all cycle currents, the exact flux-ratio product, full-order minors including the tree, the mean waiting vector, the closed-generator derivative reconstruction, and two rational entropy calculations. Analytic positivity, coupling, compactness and limiting arguments are conventional proofs above, not formally verified by these checks.

```python
import sympy as s
e, k = s.symbols('e k', positive=True)
Q = s.Matrix([[-1-e,1,e],[1,-2,1],[k,1,-1-k]])
Z = 3*(1+e+k)
p = s.Matrix([[1+2*k,1+e+k,1+2*e]])/Z
assert s.simplify(p*Q) == s.zeros(1,3)
assert s.simplify(p*s.ones(3,1)) == s.ones(1,1)
J = (e-k)/Z
cycle = [(0,2),(2,1),(1,0)]
for i,j in cycle:
    assert s.factor(p[i]*Q[i,j]-p[j]*Q[j,i]-J) == 0
ratio = s.factor(s.prod(p[i]*Q[i,j]/(p[j]*Q[j,i]) for i,j in cycle))
assert s.factor(ratio-e/k) == 0
T = s.Matrix(Q)
T[0,1] = T[1,0] = 0
R = s.Matrix([[0,1,0],[1,0,0]])
B = s.Matrix([[1,0],[0,1],[0,0]])
assert s.Matrix.hstack(B,T*B[:,1]).det() == 1
assert s.Matrix.vstack(R,(R*T)[0,:]).det() == -1
assert (-T.subs({e:0,k:0})).inv()*s.ones(3,1) == s.Matrix([1,2,3])
r, u, a, b, c, d = s.symbols('r u a b c d', positive=True)
G = s.Matrix([[-r-a,0,a],[0,-u-c,c],[b,d,-b-d]])
K1, K2 = G[:2,:2], (G*G)[:2,:2]
assert s.simplify(-K1[0,0]-r-a) == 0
assert s.simplify(-K1[1,1]-u-c) == 0
assert s.simplify(K2[1,0]/c-b) == 0
assert s.simplify((K2[1,1]-(u+c)**2)/c-d) == 0
for ev,kv in [(s.Rational(1,10),s.Rational(1,100)),
              (s.Rational(1,2),s.Rational(1,100))]:
    v = {e:ev,k:kv}
    pn, qn = p.subs(v), Q.subs(v)
    direct = sum((pn[i]*qn[i,j]-pn[j]*qn[j,i])*
        s.log(pn[i]*qn[i,j]/(pn[j]*qn[j,i]))
        for i in range(3) for j in range(i+1,3))
    proposed = (J*s.log(e/k)).subs(v)
    assert abs(s.N(direct-proposed,30)) < s.Float('1e-25')
    print(ev, kv, s.N(direct,20))
print('stationarity, entropy, minimality and reconstruction checks passed')
```

Replay command, PowerShell from the project root:

```powershell
$auditText = Get-Content -Raw -LiteralPath analysis/one-hidden-robustness-audit.md
$auditCode = [regex]::Match($auditText, '(?s)```python\r?\n(.*?)\r?\n```').Groups[1].Value
$auditCode | .\.venv\Scripts\python.exe -B -
```

Recorded numerical checks: entropy `0.062232029540379613082` at `(e,k)=(1/10,1/100)` and `0.42315480632666480546` at `(1/2,1/100)`; all exact assertions passed.
