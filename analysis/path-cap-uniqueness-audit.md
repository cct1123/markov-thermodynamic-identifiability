# A cardinality-cap path uniqueness theorem

Date: 2026-09-10 UTC. Contribution: analytic audit, source attribution, and targeted executed checks. This note uses the [working formulation](formulation.md). The general inverse-Jacobi machinery is established prior art; no novelty claim is made for the theorem or its application here.

## Verdict and exact theorem

The proposed theorem is correct with feasibility, bidirectionality, and the cardinality cap explicit.

Fix an integer `N>=3`. Assume the complete joint waiting kernels of one resolved observed pair `x<->y` admit at least one finite irreducible simple bidirected CTMC with at most `N` states. Write `T` for its killed generator, obtained by deleting only the observed off-diagonal entries, and `K(t)=[exp(Tt)]_VV` in visible-state order `(x,y)`. The full observed kernels determine this `K` and the observed rates `r=q_xy`, `s=q_yx`.

If

\[
K_{xy}^{(j)}(0)=0\quad(0\le j<N-1),\qquad
K_{xy}^{(N-1)}(0)>0,
\]

then every compatible model under that cap has exactly `N` states. Its killed off-diagonal support is the simple path from `x` to `y` through all vertices. All rates are uniquely determined, up to relabeling the internal path vertices, by the observed rates and the endpoint resolvent `Khat_xx`. The full kernel has minimal linear realization dimension `N` automatically. Hence entropy production is globally unique even when the topology and exact cardinality were initially unknown under the cap.

The derivative criterion is sufficient, not necessary, for global uniqueness. It is not a feasibility theorem for arbitrary supplied functions.

## 1. Why the derivative delay forces a path

Let `d` be the shortest number of unobserved jumps from `x` to `y` in the killed support. If no such path exists, every corresponding kernel derivative vanishes. Otherwise

\[
(T^j)_{xy}=0\quad(j<d),\qquad
(T^d)_{xy}=\sum_{\text{shortest paths }x=v_0,\ldots,v_d=y}
\prod_{i=0}^{d-1}q_{v_i v_{i+1}}>0.
\]

Diagonal factors cannot contribute at order `d`: using one would leave fewer than `d` off-diagonal steps. Thus negative generator diagonals cannot cancel the first nonzero derivative. The first nonzero derivative order is exactly the graph distance.

For any compatible model with `n<=N` vertices, the stated data therefore imply `d=N-1`. A shortest path is simple, so `d<=n-1<=N-1`; equality forces `n=N` and makes that path include every vertex.

There can be no additional killed off-diagonal edge. In the path order `v_0=x,...,v_{N-1}=y`, any extra edge joins `v_i,v_j` with `j-i>=2`. Bidirectionality supplies the forward shortcut, yielding an `x`-to-`y` route of length

\[
i+1+(N-1-j)=N-(j-i)\le N-2,
\]

contradicting the derivative delay. Edges between neighboring path vertices already exist, and the observed `x<->y` edge is the one removed from `T`. Thus `Q` is exactly the path plus that observed edge, a simple cycle on `N` states.

Bidirectionality matters: a backward-only chord in a directed model need not shorten the forward distance. The simple single-channel convention also matters; unresolved parallel channels would carry thermodynamic information not present in this generator reconstruction.

## 2. Endpoint resolvent recovers diagonal entries and edge products

Use the forced path order. Define

\[
d_i=T_{ii},\qquad f_i=T_{i,i+1}>0,\qquad
b_i=T_{i+1,i}>0,\qquad p_i=f_i b_i>0.
\]

Let `T_i` be the trailing path submatrix on vertices `i,...,N-1`, and let

\[
g_i(z)=\left[(zI-T_i)^{-1}\right]_{ii}.
\]

Then `g_0(z)=Khat_xx(z)`. A scalar Schur complement gives

\[
g_i(z)=\frac1{z-d_i-p_i g_{i+1}(z)}\quad(i<N-1),\qquad
g_{N-1}(z)=\frac1{z-d_{N-1}}.
\]

Writing the large-`z` expansion as

\[
g_i(z)=z^{-1}+\mu_{i,1}z^{-2}+\mu_{i,2}z^{-3}+\cdots,
\]

recovers

\[
d_i=\mu_{i,1},\qquad p_i=\mu_{i,2}-\mu_{i,1}^{\,2},\qquad
g_{i+1}(z)=\frac{z-d_i-g_i(z)^{-1}}{p_i}.
\]

The last step needs only the leading two coefficients to obtain `d_(N-1)`. Thus the endpoint function uniquely determines the ordered diagonal entries and positive adjacent products. No ordering of interior poles has to be guessed.

In finite data terms, endpoint derivatives `Kxx^(j)(0)` for `j=0,...,2N-1` suffice for this recursion. Each step consumes two Laurent coefficients; after `N-1` steps two coefficients remain for the final diagonal. Full exact waiting kernels provide these derivatives in the working data model.

## 3. CTMC row sums split the products into directed rates

At the first endpoint the only outgoing rates are `r` on the observed edge and `f_0` on the path. Hence

\[
f_0=-d_0-r,\qquad b_0=p_0/f_0.
\]

Continue through the internal vertices:

\[
f_i=-d_i-b_{i-1},\qquad b_i=p_i/f_i,
\qquad i=1,\ldots,N-2.
\]

The last endpoint supplies the consistency condition

\[
-d_{N-1}=b_{N-2}+s.
\]

Feasibility under the theorem's hypotheses guarantees every reconstructed `f_i,b_i` is positive and the terminal condition holds. These equations split the symmetrized edge products uniquely. They show why an endpoint spectral measure by itself identifies the products, while the CTMC normalization and known observed escape rate identify the individual directed rates.

The observed rates are determined before this reconstruction by `r=psi_(-,+)(0)` and `s=psi_(+,-)(0)`. The two observed labels fix the endpoint orientation; internal path labels remain an irrelevant permutation.

Once rates are known, the stationary distribution and entropy are determined. For example, with the observed current `J=pi_x r-pi_y s`, the cycle expression is

\[
\sigma=J\log\frac{r\prod_{i=0}^{N-2}b_i}{s\prod_{i=0}^{N-2}f_i}.
\]

This uses the cycle oriented along the observed `x->y` jump and then backward along the hidden path.

## 4. Minimality is automatic

The columns `e_x,T e_x,...,T^(N-1)e_x` form a triangular Krylov matrix in the forced path order. The component at distance `j` in `T^j e_x` is `b_0...b_(j-1)>0`, while components beyond distance `j` vanish. It therefore has full rank `N`. The transposed endpoint rows `e_x^T,e_x^T T,...,e_x^T T^(N-1)` have the analogous nonzero diagonal products of the `f_i` and also have full rank.

The actual absorption matrix includes a positive multiple of `e_x`, and the reset matrix includes `e_x^T`. Thus the full marked realization is both controllable and observable, of minimal dimension `N`. No minimality assumption or general similarity theorem is required to force the path or reconstruct it.

## 5. Primary inverse-Jacobi pointer and attribution

Fritz Gesztesy and Barry Simon, *m-Functions and inverse spectral analysis for finite and semi-infinite Jacobi matrices*, Journal d'Analyse Mathématique 73, 267-297 (1997), [DOI](https://doi.org/10.1007/BF02788147), [author preprint](https://math.caltech.edu/papers/bsimon/p261.pdf). Relevant primary pages independently inspected on 2026-09-10: Theorem 3.5 on printed p. 12 gives finite endpoint-measure uniqueness; Theorem 3.1, Eq. (3.1), printed p. 8 gives the leading expansion; reconstruction steps (i)-(iii), printed p. 11, give the recursive removal procedure. The [frontier note](../evidence/five-state-frontier-followup.md) records the broader source review.

A bidirected tridiagonal killed generator is diagonally similar to a symmetric Jacobi matrix with off-diagonals `sqrt(f_i b_i)`: choose positive scaling ratios `w_(i+1)/w_i=sqrt(b_i/f_i)`. Diagonal resolvents are unchanged. The paper's resolvent convention gives `m=-g` relative to this note. Endpoint recovery is therefore established inverse-Jacobi machinery. The cardinality-cap argument forcing the path and the CTMC rate splitting are the additional deductions audited here; no novelty is inferred for them.

## 6. Audit of the existing implementation and executed checks

Inspected [check_five_state_extensions.py](check_five_state_extensions.py), specifically `scalar_peel` and `cycle_check`.

`scalar_peel` correctly applies the reciprocal-series recurrence. If `g=z^-1 M(z^-1)` and `V=1/M`, its coefficients obey `v_0=1` and `v_k=-sum_(j=1)^k mu_j v_(k-j)`. The code obtains `d=mu_1`, `p=-v_2`, and the next suffix moments from `-v_2/p,-v_3/p,...`. The list loses exactly two entries on each step and terminates with the last diagonal. The current caller supplies exactly `2N` moments, so the terminating length-two condition is correct.

`cycle_check` also uses the correct marked-kernel entries: `joint[0][1,0]=r`, `joint[0][0,1]=s`, `joint[j][1,1]/s=Kxy^(j)(0)`, and `joint[j][1,0]/r=Kxx^(j)(0)`. Initializing its variable `backward=r` implements the first-endpoint equation; subsequent iterations replace it with the preceding path backward rate.

**Check scope:** the negative-control chord `path[0]<->path[2]` is a genuine killed-graph chord only for `N>=4`. At `N=3` it is the already observed edge. The consolidated script explicitly restricts this diagnostic to `N>=4`, with current calls at `N=5,6`. The theorem and reconstruction are valid for `N=3`; a separate exact check below covers it without that negative control.

The following read-only command was executed from the repository root with bytecode writes disabled. It reruns the existing five- and six-state checks and independently supplies a three-state boundary case:

~~~powershell
python -B -c "import sys,json; sys.path.insert(0,'analysis'); from check_five_state_extensions import cycle_check,scalar_peel,ranks; from check_small_networks import matrix,derivatives; outputs=[]; [outputs.append({k:v for k,v in cycle_check(n).items() if k!='generator'}) for n in (5,6)]; q=matrix([[-25,23,2],[29,-43,14],[11,4,-15]]); joint=derivatives(q,6); diagonal,products=scalar_peel([v[1,0]/23 for v in joint]); assert diagonal==[-25,-15,-43] and products==[22,56]; assert ranks(q)==(3,3); assert next(i for i,v in enumerate(joint) if v[1,1])==2; outputs.append({'states':3,'diagonal':[str(v) for v in diagonal],'products':[str(v) for v in products],'ranks':ranks(q),'first_cross_derivative':2}); print(json.dumps(outputs,indent=2))"
~~~

All assertions passed on 2026-09-10 using the repository's Python 3.9.12 environment and existing NumPy/SciPy helpers. The five-state case has first cross derivative order four, reconstruction through order nine, and ranks `(5,5)`; its added chord lowers the first order to three. The six-state case gives orders five and eleven, ranks `(6,6)`, and chord order four. The three-state case recovers path diagonals `(-25,-15,-43)` and products `(22,56)`, with first cross derivative order two and ranks `(3,3)`.

These representative calculations check the implementation and indexing. The all-`N` theorem follows from the graph-distance argument, exact recursion, and row sums, not from extrapolating a finite set of examples.

## Limits

The cap is essential. Without it, extra hidden states can coexist with the same shortest-path length, and the path-plus-edge conclusion fails; previously established state splitting can also destroy uniqueness when a spare state is allowed. The result presumes exact derivative zeros, not small estimated values. It does not classify general graphs with smaller endpoint distance, blurred events, one-way support, parallel channels, or uncertain physical time scale.
