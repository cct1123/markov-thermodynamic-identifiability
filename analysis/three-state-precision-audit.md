# Three-state finite-precision instability: independent audit

Checkpoint: 2026-09-10 UTC. Independent bounded audit requested by the coordinator; no evidence IDs, state, report, or other analysis outputs changed. Mathematical status: conventionally proved below, with exact symbolic checks and an independent high-precision stationary linear solve / edgewise entropy calculation. Not formally verified; no novelty claim.

**Result.** A two-state equilibrium has a globally unique exact resolved-edge kernel fiber among all finite irreducible admissible generators. Nevertheless, for every positive observational tolerance and every fixed finite observation horizon, a neighborhood of those data contains complete, minimal three-state generators with arbitrarily large entropy production, even when every off-diagonal rate is at most one. Three is the smallest possible number of states for this effect in the simple, even-state, single-channel formulation.

## 1. Assumptions, observation, and falsification conditions

Use the [repository formulation](formulation.md): finite irreducible row CTMCs; simple bidirected support; one channel per ordered pair; even states; entropy in units with `k_B=1`; fixed time unit; only the resolved jumps `+=(x,y)` and `-=(y,x)` observed. The endpoints are known. A rate upper bound refers to off-diagonal entries, not diagonal total escape rates. No common strictly positive lower bound on rates is imposed.

The reference model and its joint next-mark/time kernel, in mark order `(+,-)`, are

\[
Q_0=\begin{pmatrix}-1&1\\1&-1\end{pmatrix},\qquad
\Psi_0(t)=\begin{pmatrix}0&e^{-t}\\e^{-t}&0\end{pmatrix}.
\]

For `0<epsilon<1/2` and `0<kappa<1`, order the candidate states as `(x,y,h)` and put

\[
Q_{\epsilon,\kappa}=
\begin{pmatrix}
-1-\epsilon&1&\epsilon\\
1&-1-\epsilon&\epsilon\\
\kappa&1&-1-\kappa
\end{pmatrix}.                                      \tag{1}
\]

All six off-diagonal entries are positive and at most one. The graph is complete and irreducible for every admitted parameter pair. Diagonal magnitudes are less than two. Every individual candidate has finite entropy.

Write `TV(P,Q)=sup_A |P(A)-Q(A)|`, equivalently one half of the total variation norm of the signed probability measure. Let

\[
d_{\rm next}(Q,Q_0)=\max_{I\in\{+,-\}}
\operatorname{TV}\bigl(\psi^Q_{I,\cdot}(t)dt,
                         \psi^0_{I,\cdot}(t)dt\bigr),
\]

and let `d_H` be TV between stationary observed marked path laws on `[0,H]`. This does not assume that the microscopic initial state is observed.

**Targeted falsification conditions.** A positive parameter pair violating stationarity/current identities (2)–(3), the exact controllability/observability minors in Section 5, or either TV inequality (4)–(5) would refute the corresponding claimed step. A finite irreducible generator with this same resolved incidence, the exact kernel `Psi_0`, and a third reachable state would refute exact uniqueness. The main finite-precision assertion quantifies over every `delta>0`, finite `H>=0`, and finite target entropy `M`: there must be a candidate (1) with `d_next<delta`, `d_H<delta`, and `sigma>M`. These conditions are decided here by exact identities and coupling/path-density inequalities, not by an unsuccessful optimizer search. The weakest sufficient route is elementary algebra and probability; no optimizer, SMT solver, or graph enumeration was needed.

## 2. Exact stationary law and cycle entropy

With `D=(2+epsilon)(1+kappa+epsilon)`, the stationary law is

\[
\pi_x=\frac{1+\kappa+\epsilon\kappa}{D},\qquad
\pi_y=\frac1{2+\epsilon},\qquad
\pi_h=\frac{\epsilon}{1+\kappa+\epsilon}.                \tag{2}
\]

Indeed hidden-state balance gives `epsilon(1-pi_h)=(1+kappa)pi_h`; the `y` equation gives `1-pi_y=(1+epsilon)pi_y`. These equations and normalization determine (2), and substitution checks every stationary equation.

The three edge currents in orientation `x -> h -> y -> x` agree:

\[
\pi_x\epsilon-\pi_h\kappa
=\pi_h-\pi_y\epsilon
=\pi_y-\pi_x
=J=\frac{\epsilon(1-\kappa)}{D}>0.
\]

The stationary-probability factors cancel in the product of the three forward/reverse flux ratios. The cycle affinity and entropy are therefore

\[
\mathcal A=\log\frac{\epsilon\cdot1\cdot1}
                         {\kappa\cdot\epsilon\cdot1}
=\log(1/\kappa),\qquad
\sigma=\frac{\epsilon(1-\kappa)}
              {(2+\epsilon)(1+\kappa+\epsilon)}\log(1/\kappa).       \tag{3}
\]

For `kappa=exp(-1/epsilon^2)`,

\[
\sigma=\frac{1-\kappa}
 {\epsilon(2+\epsilon)(1+\kappa+\epsilon)},\qquad
\epsilon\sigma\longrightarrow\frac12.
\]

For every `0<epsilon<1/2`, this choice has `kappa<exp(-4)<1/2`, so the numerator exceeds `1/2` and `(2+epsilon)(1+kappa+epsilon)<5`. Consequently `sigma>1/(10 epsilon)`. The bound is deliberately simple; the displayed exact expression gives the sharper asymptotic.

## 3. Exact observational bounds and their quantifiers

After either observed mark, the state is its visible endpoint. Couple the source's next observed event clock of rate one with the candidate's same clock. The candidate has, in addition, a jump to `h` of rate `epsilon`. If the observed event wins the race, both next marks and waiting times agree exactly. The probability of failure of this coupling is `epsilon/(1+epsilon)`, independently of `kappa`. Hence

\[
d_{\rm next}(Q_{\epsilon,\kappa},Q_0)
\leq\frac{\epsilon}{1+\epsilon}.                       \tag{4}
\]

The two stationary visible masses are below one half:

\[
\frac12-\pi_x=\frac{\epsilon(3-\kappa+\epsilon)}{2D}>0,
\qquad
\frac12-\pi_y=\frac{\epsilon}{2(2+\epsilon)}>0.
\]

Thus the TV distance from the embedded reference initial law `(1/2,1/2,0)` is **exactly** `pi_h`, since the visible deficits sum to `pi_h`. Adding a separate visible-mismatch term would double-count this discrepancy.

On microscopic paths that never visit `h`, the candidate stationary path density relative to the reference path density is `2 pi_i exp(-epsilon H)`, where `i` is the initial visible state. This ratio is at most one. The probability under the candidate of never visiting `h` is `(1-pi_h)exp(-epsilon H)`: the killing hazard from either visible state is the constant `epsilon`. The reference assigns probability one to those paths. It follows directly that the TV distance between the **microscopic** stationary path laws, after embedding the reference state space, is exactly `1-(1-pi_h)exp(-epsilon H)`. Projecting both paths to the recorded marks can only decrease TV, yielding

\[
\begin{aligned}
d_H(Q_{\epsilon,\kappa},Q_0)
&\leq1-(1-\pi_h)e^{-\epsilon H}\\
&\leq\pi_h+\epsilon H
\leq\epsilon(1+H).                                   \tag{5}
\end{aligned}
\]

Equality is established for the microscopic law, not claimed for the observed law. The bound holds for each fixed finite `H`, and is uniform over `0<kappa<1`. It is not uniform over arbitrarily long horizons. The stationary observed event rate is `pi_x+pi_y=1-pi_h<1`, versus one for the source; exact infinite-statistics data distinguish them.

**Every finite-precision ball is unbounded.** Given `delta>0` and finite `H`, choose a fixed `0<epsilon<min(1/2,delta/(1+H))`. Both observational distances stay strictly below `delta` for every `0<kappa<1`. Holding this `epsilon` fixed and taking `kappa down to 0` gives

\[
\sigma\sim\frac{\epsilon}{(2+\epsilon)(1+\epsilon)}
\log(1/\kappa)\longrightarrow\infty.
\]

Alternatively the diagonal sequence `kappa=exp(-1/epsilon^2)`, `epsilon down to 0` simultaneously makes (4)–(5) vanish and entropy diverge. To satisfy a particular finite `M>0`, choosing in addition `epsilon<1/(10M)` suffices on that sequence. These are data-neighborhood results, not data-preserving exact-fiber families.

## 4. Why the exact reference data are globally unique

For an arbitrary finite model with the stated resolved incidence, let `T` be its generator with only the two observed off-diagonal entries removed. The diagonal is retained. Then

\[
\psi_{+,-}(0)=q_{yx},\quad
\psi_{-,+}(0)=q_{xy},\qquad
\psi'_{+,-}(0)=q_{yy}q_{yx},\quad
\psi'_{-,+}(0)=q_{xx}q_{xy}.
\]

Equality to the reference kernel forces `q_xy=q_yx=1` and `q_xx=q_yy=-1`. Nonnegativity and row normalization now give

\[
\sum_{h\notin\{x,y\}}q_{xh}=0,
\qquad
\sum_{h\notin\{x,y\}}q_{yh}=0.
\]

Every possible hidden entrance from either visible endpoint is zero, so `{x,y}` is a closed communicating class. Irreducibility excludes every additional state. The only admissible generator is `Q_0`, with entropy zero, independently of the finite state cap. This argument would fail if disconnected inaccessible states were allowed, or if incidence/parallel channels changed; those are outside this audit's class.

The candidate is never exactly equivalent for positive `epsilon`: already `psi'_{+,-}(0)=psi'_{-,+}(0)=-1-epsilon`. **Corrected shortcut:** zero-time densities alone identify the observed rates, not total visible escape rates. The first derivatives are needed to establish zero visible deficits. This distinction was retained rather than silently treating immediate densities as escape-rate measurements.

## 5. Minimality and dimension limitation

For (1),

\[
T=\begin{pmatrix}-1-\epsilon&0&\epsilon\\
0&-1-\epsilon&\epsilon\\
\kappa&1&-1-\kappa\end{pmatrix},\quad
B=(e_x,e_y),\quad R=(e_y^T;e_x^T).
\]

The controllability submatrix `(e_x,e_y,T e_y)` has determinant one. The observability submatrix with rows `(e_y^T,e_x^T,e_x^T T)` has determinant `-epsilon`. Both are nonzero throughout the declared domain. Thus `R exp(Tt) B` has ordinary linear realization order exactly three for every positive `epsilon`, with no generic-spectrum exception. The reference kernel has linear order two because its `R` and `B` are invertible at that order.

Any simple two-state irreducible CTMC obeys `pi_x q_xy=pi_y q_yx`, so its only edge contributes zero entropy. There are no additional channels in the formulation. Therefore a candidate with positive, let alone unbounded, entropy needs at least three states, and (1) reaches that minimum.

This construction crosses from a minimal two-state source to minimal three-state nearby data. It does not keep the source's minimal order or trace fixed: `tr(Q_epsilon,kappa)=-(3+2epsilon+kappa)`, versus `tr(Q_0)=-2`. Its diagonal-sequence limit on the three-state space is reducible; `h` becomes inaccessible from the visible class. The small reverse rate `kappa` approaches zero, so a common positive rate lower bound would remove this divergent sequence. These are explicit assumptions and limits, not failures of the finite-precision claim. A construction retaining the full source order or trace addresses an additional restriction.

## 6. Reproduced checks and exact replay

Executed from the repository root on 2026-09-10 using CPython 3.9.12, SymPy 1.14.0, mpmath 1.3.0. No random numbers, optimizer tolerances, sampled topology coverage, or external inputs are involved. The exact inputs are (1) and the parameter domain above. No failed execution occurred. No existing scientific output was overwritten; this note is the sole new artifact of this audit.

The checker below first uses exact symbolic identities, then separately solves the numerical stationary linear system and sums all three undirected edge contributions to entropy at 60 and 100 decimal digits. That numerical route does not insert the closed-form stationary law into the entropy sum. It shares the original generator and entropy convention with the proof and supplies an implementation cross-check, not an independent theorem or rigorous numerical error enclosure. The proof itself is algebraic and analytic.

Observed values were identical at the displayed precision in both runs:

| epsilon | kappa = exp(-1/epsilon^2) | sigma | epsilon sigma |
| --- | --- | --- | --- |
| 1/4 | 1.12535175e-7 | 1.422221934132201 | 0.35555548353305 |
| 1/10 | 3.72007598e-44 | 4.329004329004329 | 0.43290043290043 |
| 1/20 | 1.91516960e-174 | 9.291521486643438 | 0.46457607433217 |
| 1/50 | 1.83567267e-1086 | 24.26713259561250 | 0.48534265191225 |

Every exact assertion and numerical residual assertion passed. Arbitrary-precision exponentials retained the tiny positive reverse rates; none were clipped to zero or evaluated as an underflowed floating-point logarithm.

For a replay without writing another file, run the following PowerShell command from the project root:

```powershell
@'
import sys
import sympy as s
import mpmath as mp
e,k=s.symbols('epsilon kappa', positive=True)
Q=s.Matrix([[-1-e,1,e],[1,-1-e,e],[k,1,-1-k]])
D=(2+e)*(1+k+e)
p=s.Matrix([[(1+k+e*k)/D,1/(2+e),e/(1+k+e)]])
assert s.simplify(sum(p)-1)==0
assert (p*Q).applyfunc(s.factor)==s.zeros(1,3)
J=e*(1-k)/D
for f in (p[0]*e-p[2]*k,p[2]-p[1]*e,p[1]-p[0]):
    assert s.factor(f-J)==0
assert s.factor(s.Rational(1,2)-p[0]-e*(3-k+e)/(2*D))==0
assert s.factor(s.Rational(1,2)-p[1]-e/(2*(2+e)))==0
T=Q.copy(); T[0,1]=T[1,0]=0
ex=s.eye(3)[:,0]; ey=s.eye(3)[:,1]
C=s.Matrix.hstack(ex,ey,T*ey)
O=s.Matrix.vstack(ey.T,ex.T,ex.T*T)
assert C.det()==1 and O.det()==-e
R=s.Matrix.vstack(ey.T,ex.T); B=s.Matrix.hstack(ex,ey)
assert R*T*B==s.Matrix([[0,-1-e],[-1-e,0]])
print('Exact identities PASS')
print('Python',sys.version.split()[0],'SymPy',s.__version__,'mpmath',mp.__version__)
for dps in (60,100):
    mp.mp.dps=dps
    for n in (4,10,20,50):
        ee=mp.mpf(1)/n; kk=mp.exp(-1/ee**2)
        QQ=mp.matrix([[-1-ee,1,ee],[1,-1-ee,ee],[kk,1,-1-kk]])
        A=QQ.T.copy()
        for j in range(3): A[2,j]=1
        pp=mp.lu_solve(A,mp.matrix([0,0,1]))
        ss=mp.mpf(0)
        for i,j in ((0,1),(0,2),(1,2)):
            ff=pp[i]*QQ[i,j]; gg=pp[j]*QQ[j,i]
            ss+=(ff-gg)*mp.log(ff/gg)
        closed=(1-kk)/(ee*(2+ee)*(1+kk+ee))
        assert abs(ss-closed)<mp.mpf(10)**(-dps+8)*closed
        assert max(abs(v) for v in (pp.T*QQ))<mp.mpf(10)**(-dps+8)
        print(dps,n,mp.nstr(kk,9),mp.nstr(ss,16),mp.nstr(ee*ss,14))
print('Independent numerical stationary solve and edgewise entropy PASS')
'@ | .\.venv\Scripts\python.exe -B -
```

No inference rests on failure to find a counterexample. The consequence is a precise discontinuity of exact identifiability under the stated observational TV tolerances; it is not a claim that equal exact kernels can have different entropy with at most three states.
