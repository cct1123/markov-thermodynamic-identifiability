# Independent four-state finite-precision check

Checked 2026-09-10 UTC. This independently verifies the coordinator's proposed construction and a direct confidence-limit consequence. It does not recheck the earlier whole-fiber classification or certify novelty. No objection to the proposed entropy formula or rate bound was found.

## Exact calculation

Use row generators, state order `(x,y,h,k)`, and only the directed marks `x -> y` and `y -> x`. Put `0 < t < e < 1/2` and

```text
Qe = [[-2-e, 1,    1,    e],
      [1,    -2-e, e,    1],
      [1,    e,    -2-e, 1],
      [e,    1,    1,    -2-e]].
S = diag(I2, [[1-t,t],[0,1]]).
```

The required orientation is `A = S^-1 Qe S`, with stationary distribution `p = (1,1,1-t,1+t)/4`. Direct symbolic multiplication gives

```text
A = [[-2-e,              1,              1-t,    e+t],
     [1,                 -2-e,          e(1-t), 1+et],
     [(1-et)/(1-t),      (e-t)/(1-t),   -2-e-t, 1+t],
     [e,                 1,             1-t,    -2-e+t]].
```

All off-diagonal rates are positive, row sums vanish, and `p A = 0`. Hence every interior member is a complete, irreducible, bidirected four-state CTMC. All off-diagonal rates are at most `1+e < 3/2`: the only non-immediate upper bound is `(1-et)/(1-t) <= 1+e`, equivalent to `t <= e`. Also `(e-t)/(1-t) <= e`. No positive rate lower bound holds uniformly as `t` approaches `e`.

Let `J=t(1-e)/4`. The currents `p_i A_ij-p_j A_ji` for `(xy,xh,xk,yh,yk,hk)` are `(0,-J,J,J,-J,0)`. Multiplying the flux ratios with these signed exponents yields

```text
sigma(A) = J log[(1-et)(e+t) / ((e-t)(1+et))].
```

This uses the standard unordered-edge sum `sum_{i<j} (f_ij-f_ji) log(f_ij/f_ji)` with natural logarithms and `k_B=1`. At fixed `e>0`, its prefactor tends to `e(1-e)/4>0` and its logarithm diverges as `t -> e` from below. Rates remain bounded; the divergence comes from a reverse flux approaching zero. `Qe` itself is symmetric and has entropy zero, as does `Q0`.

## Equality of observations

Let `T` be `Qe` with just the two marked off-diagonals set to zero, keeping its diagonal; define `T_A` analogously. Exact multiplication verifies `T_A=S^-1 T S`. For the reset matrix `R` and mark-rate matrix `B` used below, `R S^-1=R` and `S B=B`. Consequently `R exp(T_A u) B = R exp(T u) B` for every `u>=0`, not just at the sampled derivative orders.

The equality also holds for the stationary finite-window marked point-process law, including no-event probabilities. Each marked jump matrix commutes with `S`, `S 1=1`, and the stationary row transforms from `pi=(1,1,1,1)/4` to `pi S=p`. Thus each product `p exp(T_A u1) J1 ... exp(T_A ur) 1` telescopes to its `Qe` counterpart. This explicitly fixes the initial-distribution issue. Arbitrary unrelated hidden initial distributions are not asserted equivalent.

## Coupling and confidence consequence

**Independent analytic check:** generate `Qe` by running `Q0` and an independent rate-`e` clock. At each extra clock tick, flip the current state by the permutation `(x k)(y h)`. Before its first tick, the two paths agree. Starting both with the same uniform stationary state, their observed laws on `[0,H]` therefore satisfy

```text
d_TV(Pe,H, P0,H) <= 1-exp(-e H) <= e H.
```

Here `d_TV` is the supremum over measurable events. The same bound applies after any further randomized observation/rounding mechanism independent of the model, by applying that mechanism to the coupled records. For a finite collection of independent windows, replace `H` by their total duration. Similarity identifies `Pe,H` with every stationary `A(e,t)` marked-record law at the same `e`.

For a visible reset and the complete next-mark/time outcome without a fixed time cutoff, solve `-T0 u=1`: `u=(2,2,3,3)`. The probability of an extra tick before the `Q0` next mark is at most `e E(tau)=2e`. Thus each next-mark/time row has TV distance at most `2e`, and the law of `m` successive marked waits from a fixed visible reset has distance at most `2me` by sequential coupling.

Let a measurable data-based upper limit `U` take values in `[0,infinity]` and satisfy uniform modelwise coverage `P_Q{U >= sigma(Q)} >= 1-alpha`, with `0<alpha<1`, over a class containing this family. At fixed `e`, the law `Pe` is independent of `t` and `sigma(A(e,t))` is unbounded. For every finite `M`, coverage for a member with entropy above `M` implies `Pe{U>=M}>=1-alpha`. Continuity from above gives `Pe{U=infinity}>=1-alpha`. TV convergence then gives

```text
P0{U=infinity} >= 1-alpha.
```

Therefore a uniformly honest upper limit cannot be finite almost surely even at the reversible limiting model. This is a finite-experiment statement; it does not forbid confidence procedures under a uniform reverse-rate cutoff, a smaller known topology class, or a non-uniform/asymptotic coverage target. It does not claim that a particular finite output is impossible: such outputs can occupy at most probability `alpha` under `P0` if uniform coverage is retained.

## Reproduced symbolic check

Environment actually used: workspace `.venv`, Python 3.9.12, SymPy 1.14.0. No stochastic calculation or seed. The first scratch run obtained rates and currents but stopped on mutation of a SymPy immutable matrix; converting that matrix explicitly resolved it. The following final check was run successfully from the project root. It preserves the exact inputs in this note rather than creating another script/output.

```python
import sympy as s
e, t = s.symbols('e t', positive=True)
Q = s.Matrix([[-2-e,1,1,e],[1,-2-e,e,1],
              [1,e,-2-e,1],[e,1,1,-2-e]])
S = s.diag(s.eye(2), s.Matrix([[1-t,t],[0,1]]))
A = s.Matrix(s.simplify(S.inv()*Q*S))
p = s.Matrix([[s.Rational(1,4)]*4])*S
assert s.simplify(A*s.ones(4,1)) == s.zeros(4,1)
assert s.simplify(p*A) == s.zeros(1,4)
T, TA = s.Matrix(Q), s.Matrix(A)
T[0,1] = T[1,0] = TA[0,1] = TA[1,0] = 0
R = s.Matrix([[0,1,0,0],[1,0,0,0]])
B = s.Matrix([[1,0],[0,1],[0,0],[0,0]])
assert s.simplify(TA-S.inv()*T*S) == s.zeros(4)
assert s.simplify(R*S.inv()-R) == s.zeros(2,4)
assert s.simplify(S*B-B) == s.zeros(4,2)
for k in range(8):
    assert s.simplify(R*T**k*B-R*TA**k*B) == s.zeros(2)
J = t*(1-e)/4
ratio = s.prod(s.factor((p[i]*A[i,j])/(p[j]*A[j,i]))**
    s.simplify((p[i]*A[i,j]-p[j]*A[j,i])/J)
    for i in range(4) for j in range(i+1,4))
expected = ((1-e*t)*(e+t))/((e-t)*(1+e*t))
assert s.factor(ratio-expected) == 0
assert (-T.subs(e,0)).inv()*s.ones(4,1) == s.Matrix([2,2,3,3])
for ev,tv in [(s.Rational(1,4),s.Rational(1,8)),
              (s.Rational(1,10),s.Rational(999,10000))]:
    d = {e:ev,t:tv}
    an, pn = A.subs(d), p.subs(d)
    direct = sum((pn[i]*an[i,j]-pn[j]*an[j,i])*
        s.log(pn[i]*an[i,j]/(pn[j]*an[j,i]))
        for i in range(4) for j in range(i+1,4))
    proposed = (J*s.log(expected)).subs(d)
    assert abs(s.N(direct-proposed,30)) < s.Float('1e-25')
    print(ev, tv, s.N(direct,20))
print('exact identities and rational numerical cross-checks passed')
```

Replay in PowerShell from the project root:

```powershell
$auditText = Get-Content -Raw -LiteralPath analysis/finite-precision-independent-check.md
$auditCode = [regex]::Match($auditText, '(?s)```python\r?\n(.*?)\r?\n```').Groups[1].Value
$auditCode | .\.venv\Scripts\python.exe -B -
```

Observed entropy values: `0.024283404648908805513` at `(e,t)=(1/4,1/8)` and `0.17038892808274812515` at `(1/10,999/10000)`. These are numerical cross-checks; the exact flux-ratio identity supplies the symbolic verification.

## Primary statistical analogy and source limits

**Primary result inspected:** Jonas Moss, *Infinite diameter confidence sets in Hedges' publication bias model*, Journal of the Korean Statistical Society **51**, 946–960 (2022), published 22 April 2022, [publisher full text](https://link.springer.com/article/10.1007/s42952-022-00169-1), [arXiv v3 PDF](https://arxiv.org/pdf/1912.09180v3), retrieved 2026-09-10. Section 3, Theorem 4 (PDF p.6), and its appendix proof (PDF p.9), were read. The generalized Gleser–Hwang theorem combines pointwise density convergence, divergence of a parameter-class size, and support inclusion. Its proof first forces infinite confidence-set extent at the limiting distribution, then uses support inclusion to extend positive probability to other distributions. The proof explicitly requires positive coverage `1-alpha`; use `0<alpha<1` here.

**Comparison:** the direct model-indexed argument above uses TV and needs no support inclusion for its conclusion at `P0`. In this problem, distinct entropy values can share one observation law, so entropy is not automatically a functional on a partition of distinct observation distributions. This is a statistical analogy, not an unverified application of Moss's theorem.

The original Gleser–Hwang (1987), DOI [10.1214/aos/1176350597](https://doi.org/10.1214/aos/1176350597), was not read: its [Purdue 1985 preprint route](https://www.stat.purdue.edu/docs/research/tech-reports/1985/tr85-15.pdf) timed out. Bahadur–Savage (1956), DOI [10.1214/aoms/1177728077](https://doi.org/10.1214/aoms/1177728077), also remained inaccessible beyond bibliographic/secondary descriptions; the original theorem is not attributed as inspected evidence. Moss is primary evidence for the stated generalization, not independent primary access to those older papers.
