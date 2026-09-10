# Fast-escape theta kernel: local evidence and global coordinates

Date: 2026-09-10 UTC. This note preserves the earlier local evidence and global coordinates. **Later resolution:** the [spectral-cone proof](theta-fast-spectral-audit.md) establishes global generator uniqueness at theta(100,100). The search below remains inconclusive as numerical evidence and is not used in that proof.

Take the [theta family](theta-parameter-strata-audit.md) at `a=b=100`, so `s=200>beta=9+2sqrt(6)`. The full marked kernel is minimal of dimension five. The [construction audit](theta-family-construction-audit.md) proves that every compatible model with a reducible bidirected hidden block is the source itself up to hidden labels. Thus any distinct compatible five-state model must have a connected hidden block. This is a global exclusion for disconnected hidden blocks, not an exclusion for connected ones.

## Exact local isolation

Use the six normalized hidden-similarity coordinates and eight missing directed rates from [the earlier theta audit](theta-global-audit.md), in row order `(xk,yh,hy,hl,kx,kl,lh,lk)`. At this source the first-order matrix has rank six, and the strictly positive vector

\[
c=\left(3,1,1,\frac{53200}{109371},\frac73,
\frac{133900}{109371},\frac{1983}{36457},\frac{4577}{36457}\right)
\]

annihilates it on the left. Therefore `Av>=0` forces `Av=0`, then `v=0`. The normalized-sequence argument excludes any nonconstant sequence of compatible generators converging to the source. The exit chart determinant is `-882`, so this is isolation in generator space as well as in similarity coordinates. These equalities and signs were executed with exact rational arithmetic in [the targeted script](probe_theta_fast_case.py).

This has the same local obstruction as the earlier `(3,3)` example, whose distant unbounded component is already known. Local isolation at `(100,100)` therefore provides no global thermodynamic conclusion.

## Global coordinates available for an exact next step

The entire five-state fiber can be parameterized by three noncollinear exit points `(u_i,v_i)`, because minimality exhausts fixed-order realizations by hidden similarities. Put

\[
C=\begin{pmatrix}3&0&1\\0&6&1\\100&100&1\end{pmatrix},\quad
B=XC=\begin{pmatrix}806&800&10\\1100&1142&18\end{pmatrix},
\]

\[
D=C^{-1}HC=
\begin{pmatrix}
-20579/147&-18524/147&-1\\
-18815/294&-11467/147&-1\\
19550/49&19700/49&0
\end{pmatrix}.
\]

For `C'` with rows `(u_i,v_i,1)`, the compatible blocks are

\[
U=C(C')^{-1},\quad X'=B(C')^{-1},\quad
H'=C'D(C')^{-1},\quad Y'=C'_{[:,1:2]}.
\]

The visible entrance condition is that the triangle contains the two points `(403/5,80)` and `(550/9,571/9)`. The hidden positivity condition is that the vector field

\[
g(u,v)=\left(
u^2+uv-\frac{20579}{147}u-\frac{18815}{294}v+\frac{19550}{49},
uv+v^2-\frac{18524}{147}u-\frac{11467}{147}v+\frac{19700}{49}
\right)
\]

lies in the cone of inward edge directions at each vertex. Precisely, `g(p_i)=sum_{j!=i} H'ij(p_j-p_i)`. All exit coordinates must be nonnegative. Reciprocal support, finite rates and irreducibility of the full generator must also be imposed. These formulas are a global parameterization, not a claim that the feasible triangles form a convex or connected set.

The rational matrices B and D were calculated directly with the existing exact helpers. Reproduce from the repository root:

```powershell
python -B -c "import sys; sys.path.insert(0,'analysis'); from check_five_state_extensions import theta,inverse,strings; from check_small_networks import matrix; q=theta(100,100); c=matrix([[3,0,1],[0,6,1],[100,100,1]]); print(strings(q[:2,2:]@c)); print(strings(inverse(c)@q[2:,2:]@c))"
```

## Bounded numerical diagnostic

Run `python -B analysis/probe_theta_fast_case.py`. The [saved JSON](theta-fast-probe.json) records the exact certificate, environment, source hashes, seed `20260911`, and all thirteen starts. The search uses six coordinates bounded by `[-3,3]`, determinant floor `1e-4`, a common off-diagonal margin in `[0,2]`, and at most 400 iterations per start. The initial research run was `2026-09-10T06:55:19.969603+00:00`; [E044](../evidence/RECORDS.md#e044) records the unchanged maintenance replay after the probes were consolidated.

No start produced a positive complete representative; the best returned source identity has minimum off-diagonal rate zero. The local linear program reported infeasibility of a strictly positive missing-rate direction, agreeing with the exact local certificate. SLSQP emitted its standard bound-clipping warning; all return statuses are retained.

**Limit:** neither this bounded search nor a successful optimizer termination proves absence of a complete model. It also does not search all connected sparse hidden supports. No global entropy bound follows.

## Original discriminating action, now completed

The original action was to determine whether any admissible exit-coordinate triangle produces a connected hidden block, covering both paths and triangles. The [spectral-cone proof](theta-fast-spectral-audit.md) now excludes every such realization and completes global uniqueness. The geometric exit-coordinate triangle itself does not specify hidden support. [D012](../evidence/RECORDS.md#d012) records the next parameter-boundary question.
