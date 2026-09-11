# Exact entropy ceilings are unstable to observational tolerance

2026-09-10 UTC. Agent mathematical deductions and executed checks, under the [formulation](formulation.md). Conventional proofs, independently audited; no formal verification or novelty claim. The human brief is unchanged.

## Question, falsification condition and outcome

Does an exact singleton or bounded entropy fiber imply a finite upper ceiling in some positive neighborhood of its complete joint next-mark/time law, when state count and microscopic rates are bounded?

A confirming stability result would bound entropy for all admissible models in such a neighborhood. A falsifying witness must have a common finite state cap and rate cap, observable laws converging to an exactly bounded source, and stationary entropy tending to infinity. Large numerical entropy alone, a changing observation convention, added unbounded rates, or agreement on a finite time grid would not meet that test.

**Outcome:** the stability assertion is false. The [general proof](entropy-neighborhood-audit.md) establishes a stronger statement at every source with two fully hidden states: for every positive tolerance and every finite entropy threshold, there is a complete bidirected model with the same number of states, observed rates and **exact generator trace**, closer than that tolerance and above that threshold. The common microscopic rate cap is minus the source trace. The argument requires unknown competitor topology and no positive reverse-rate floor. It uses a complete trace-preserving perturbation, the existing exact hidden-pair boundary theorem, and two independent continuity arguments. It does not assume minimality.

The simplest sufficient tools were exact matrix algebra and a coupling argument. The following explicit four-state example makes the result independently checkable at a source whose linear order already saturates its state cap. The subsequent [three-state fixed-trace audit](three-state-fixed-trace-audit.md) achieves the smallest possible dimension, while [the two-state-source audit](three-state-precision-audit.md) treats a lower-order source. Four is not the smallest possible cap. This four-state family remains useful because, for each fixed positive perturbation, it contains an unbounded exact fiber; each of the three-state fibers is instead a singleton.

## Explicit source and transformed family

Use states `(x,y,h,k)` and observe only `x -> y` and `y -> x`, each with rate one. Set

\[
Q_0=\begin{pmatrix}-2&1&1&0\\1&-2&0&1\\1&0&-2&1\\0&1&1&-2\end{pmatrix},\quad
C=\begin{pmatrix}-1&0&0&1\\0&-1&1&0\\0&1&-1&0\\1&0&0&-1\end{pmatrix},\quad
Q_\varepsilon=Q_0+\varepsilon C.
\]

Both source and perturbed model are symmetric and have stationary distribution `(1,1,1,1)/4`. Let `0<epsilon<1/2`, `0<=t<epsilon`, and

\[
S_t=\operatorname{diag}\left(I_2,
\begin{pmatrix}1-t&t\\0&1\end{pmatrix}\right),\qquad
Q_{\varepsilon,t}=S_t^{-1}Q_\varepsilon S_t.
\]

Direct multiplication gives

\[
Q_{\varepsilon,t}=\begin{pmatrix}
-2-\varepsilon&1&1-t&\varepsilon+t\\
1&-2-\varepsilon&\varepsilon(1-t)&1+\varepsilon t\\
\frac{1-\varepsilon t}{1-t}&\frac{\varepsilon-t}{1-t}&-2-\varepsilon-t&1+t\\
\varepsilon&1&1-t&-2-\varepsilon+t
\end{pmatrix}.
\]

Every offdiagonal entry is strictly positive and at most `1+epsilon<3/2`. For the only potentially problematic quotient,

\[
1+\varepsilon-\frac{1-\varepsilon t}{1-t}
=\frac{\varepsilon-t}{1-t}>0.
\]

The remaining bounds follow directly from `0<=t<epsilon<1/2`. Row sums are zero and

\[
\pi_t=\tfrac14(1,1,1-t,1+t),\qquad \pi_tQ_{\varepsilon,t}=0.
\]

The exact observed kernel equals that of `Q_epsilon` for all `t` in this parameter interval: the killed generator transforms by the same similarity, the reset rows and observed-rate columns are fixed, and `S_t 1=1`. The parameter `t` in this construction is a dimensionless mixing coefficient, not elapsed physical time.

## Exact entropy and divergence

Put `J=t(1-epsilon)/4`. The stationary current on the four oriented edges `h->x`, `x->k`, `y->h`, `k->y` is `J`; currents on `x<->y` and `h<->k` vanish. Multiplying the four forward/reverse stationary flux ratios yields

\[
\boxed{\quad
\sigma(Q_{\varepsilon,t})=
\frac{t(1-\varepsilon)}4
\log\frac{(1-\varepsilon t)(\varepsilon+t)}
{(\varepsilon-t)(1+\varepsilon t)}.\quad}
\]

For each fixed positive `epsilon`, as `t` increases to `epsilon`, the rate `h->y` vanishes but the opposing stationary flux tends to `epsilon(1-epsilon)/4>0`. All stationary probabilities have positive limits. Thus

\[
\sigma(Q_{\varepsilon,t})=
\frac{\varepsilon(1-\varepsilon)}4\log\frac1{\varepsilon-t}+O(1)\longrightarrow\infty.
\]

No boundary model with an irreversible edge is admitted: every member before the boundary is finite, irreducible and bidirected. The divergent limit establishes an unbounded supremum of their finite entropy values. Rates and entropy rates have inverse-time units with `k_B=1`; no common positive lower rate bound is imposed.

## Source uniqueness and closeness of the full observed law

For `Q0`, the unobserved graph is the path `x-h-k-y`. Its killed cross-entry has derivatives of orders 0,1,2 equal to zero and order 3 equal to one. The [maximal path-delay theorem](path-cap-uniqueness-audit.md) therefore forces the whole generator under a four-state cap, up to hidden labels. Its controllability and observability ranks are both four. This source is globally identifiable with entropy zero; no unused state in its cap is responsible for the instability.

Define `d` as the maximum, over prior marks, of the total variation between the **joint** next-mark/time laws:

\[
d(Q,P)=\max_I\frac12\sum_J\int_0^\infty
|\psi^Q_{IJ}(u)-\psi^P_{IJ}(u)|\,du.
\]

The perturbation adds a jump clock of rate `epsilon` at every state, flipping `x<->k` or `y<->h`. Couple all original jumps. Before an extra clock rings, both observed records agree. The mean time to the next observed jump under `Q0`, starting in either visible reset state, is two: solving the killed equations gives the vector `(2,2,3,3)`. Consequently

\[
d(Q_0,Q_{\varepsilon,t})=d(Q_0,Q_\varepsilon)\le2\varepsilon.
\]

This is an analytic all-time bound, independent of the divergent-entropy parameter. A fixed prefix of `m` next-mark/time observations starting after a specified mark has TV distance at most `2m epsilon` by sequential coupling.

For a stationary observed record in a fixed physical window `[0,H]`, the initial laws of `Q0` and `Qepsilon` are both uniform. The same coupling gives

\[
\operatorname{TV}(\mathbb P^H_{Q_0},\mathbb P^H_{Q_\varepsilon})
\le1-e^{-\varepsilon H}\le\varepsilon H.
\]

This bound also holds with `Qepsilon,t` in place of `Qepsilon`. Indeed each stationary marked-path density, including the final no-event interval, is

\[
\pi e^{Tu_1}E_{J_1}e^{T(u_2-u_1)}\cdots
E_{J_m}e^{T(H-u_m)}\mathbf1.
\]

Substitute `pi'=pi S`, `T'=S^-1 T S`, `S E_J=E_J S` and `S1=1`: every similarity cancels. This also covers an entirely empty record. Exact equality of pairwise densities is not being assumed to suffice for arbitrary blurred observations or a specified microscopic hidden initial state.

## Consequence for uniform finite-sample upper confidence limits

Let `U` be a measurable extended-real upper limit computed from that finite stationary record. Suppose for some `0<alpha<1` it has coverage at least `1-alpha` for **every** admissible model with at most four states, these observed rates, unknown bidirected topology and every offdiagonal rate at most `3/2`:

\[
\mathbb P_Q^H\{U\ge\sigma(Q)\}\ge1-\alpha.
\]

For fixed `epsilon`, all members indexed by `t` have the same record law but unbounded entropy. For every finite threshold `K`, coverage forces `P_epsilon(U>K)>=1-alpha`. Letting `K` tend to infinity gives `P_epsilon(U=+infinity)>=1-alpha`. Transfer this event to `P0` using the TV bound and let `epsilon` decrease to zero:

\[
\boxed{\mathbb P^H_{Q_0}\{U=+\infty\}\ge1-\alpha.}
\]

Thus a uniformly valid procedure cannot be almost surely finite even at this uniquely identified equilibrium source. The same conclusion holds for the general fixed-trace class in the [independent audit, Section 6](entropy-neighborhood-audit.md#6-finite-horizon-statistical-implication-audit-of-the-added-claim). Independent randomization does not help, since a common auxiliary seed preserves TV distance.

This is a model-indexed coverage statement, not an assertion that entropy is a single-valued functional of the observed law. It does not contradict lower entropy estimators or pointwise asymptotic consistency in restricted models. It does not supply a TV confidence ball from an empirical distribution of continuous waiting times. A positive reverse-rate floor or known sparse topology changes the admissible class. General confidence-set impossibility is established statistical machinery; see the [primary-source comparison](finite-precision-independent-check.md#primary-statistical-analogy-and-source-limits).

## Reproducibility, verification and failed attempts

Run from the repository root:

```powershell
.venv/Scripts/python.exe -B analysis/check_finite_precision_instability.py
```

The [checker](check_finite_precision_instability.py) writes [finite-precision-checks.json](../outputs/finite-precision-checks.json), recording its SHA-256, execution time, environment, exact inputs and 12 rational cases. Generic exact algebra checks row sums, stationarity, similarity, fixed mark matrices, current directions, entropy flux-ratio identity and rate-cap identity. Exact source ranks and path derivatives verify the uniqueness premise. At the rational cases, direct killed powers through order seven independently certify the all-time kernel identity, and 100-digit direct edge-flux entropy agrees with the formula.

Independent semigroup quadrature gives row TV approximately `0.06138236`, `0.00324627`, `0.00032864` for `epsilon=1/4,1/100,1/1000`, below the analytic bounds `1/2,1/50,1/500`. These values and their estimated quadrature errors are diagnostics, not rigorous interval proofs. No seed, numerical optimization or external dataset was used.

The first checker run failed because SymPy structural equality compared two differently factored versions of the same rational expression. It stopped before writing a result. Replacing that assertion and the analogous rate-cap comparison with exact rational-function difference checks fixed the verifier; the mathematical formulas did not change. The failure is also recorded in the successful JSON.

A separate worker derived the generator, currents, entropy and coupling independently, then executed the embedded symbolic check in [finite-precision-independent-check.md](finite-precision-independent-check.md). Its initial scratch run failed on matrix-copy handling and was corrected before the successful replay. The general audit separately verified the exact-trace construction and the statistical quantifiers. Shared reliance on the existing pair/path theorems is explicit; repeated agreement on those dependencies is not a new independent proof of them.

The four-state additive illustration has trace `-8-4epsilon`, not exactly the source trace `-8`. Only the general convex-completion construction proves the stronger exact-trace result. The two constructions must not be conflated.
