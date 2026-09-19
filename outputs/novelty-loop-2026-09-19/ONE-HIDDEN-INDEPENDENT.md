# Independent check: one fully hidden vertex

Status: the three-point inverse below has a conventional algebraic proof and exact checks; the hidden-incidence-only ceiling criterion is falsified. This note does not establish publication priority. It was derived independently of the coordinating agent's proof and imports no local scientific helper or accepted calculation.

## Scope and falsification conditions fixed before proof

Use a row CTMC generator on a known labelled set `V union {h}`, with `m=|V| >= 2`. It is finite, irreducible, and has reciprocal support. The nonempty resolved microscopic mark set `E` is reverse closed, contains positive rates, and its endpoint set is exactly `V`. The data at a positive argument `s` are the full, absolutely normalized next-mark Laplace matrix conditional on each previous mark; both mark labels and reset vertices are known. Rates have inverse-time units; entropy has Boltzmann constant one. Observed rates need not be calibrated. Competitors use these same vertex/mark labels and the same one-hidden-vertex restriction; their unobserved support can vary.

An inverse counterexample would require distinct admissible generators with exactly equal full matrices at three prescribed distinct positive arguments. A floating residual or matching a time grid would not suffice. Before proof, targeted strata were a hidden leaf, zero hidden entrances/exits at some visible vertices, full hidden incidence with missing visible edges, and full support, at N=4,5,6. The script checks one deterministic rational rate assignment in each stratum, not an exhaustive rate search. It also directly tests the candidate ceiling condition by opening a missing visible-visible pair. All-time claims below use an exact intertwining, not equality at finitely many samples.

## Three points recover the generator, including leaves and sparse strata

Let `T` be `Q` with all observed off-diagonal rates set to zero, retaining the generator diagonal. Write

```
T = [ A  u ] ,    d = v 1 > 0,
    [ v -d ]
k_i = sum_{(i,j) in E} q_ij > 0,    D=diag(k_i).
```

For every visible vertex choose any previous mark whose target is that vertex. Aggregate next-mark columns by their source vertex. This selects an `m x m` data matrix

```
F(s) = K(s) D,
K(s) = [(sI-T)^(-1)]_{VV},
H(s) = F(s)^(-1) = D^(-1)[sI-A-u v/(s+d)].
```

These inverses exist: `s>0` gives an invertible nonsingular M-matrix `sI-T`; its scalar hidden block `s+d` is positive, so the Schur complement is invertible; `D` is positive diagonal. The visible row-sum identity `A1+u=-k` yields the useful scalar identity

```
y_i(s) := [(H(s)1)_i-1]/s = a_i+b_i/(s+d),
a_i=1/k_i>0,    b_i=u_i/k_i>=0.
```

Order the three samples as `0<s1<s2<s3`. Irreducibility ensures some `u_p>0`; hence `y_p(s1)>y_p(s2)>y_p(s3)`. Define

```
r = [(y_p(s1)-y_p(s2))/(y_p(s2)-y_p(s3))]*(s3-s2)/(s2-s1),
d = (s3-r*s1)/(r-1),                         r=(s3+d)/(s1+d)>1,
b_i = (y_i(s1)-y_i(s2))*(s1+d)*(s2+d)/(s2-s1),
a_i = y_i(s1)-b_i/(s1+d),
k_i=1/a_i,    u_i=b_i/a_i.
```

All denominator exclusions are explicit and satisfied at the stipulated source. Then

```
W = {D[H(s2)-H(s1)]/(s2-s1)-I}*(s1+d)*(s2+d) = u v,
v_j=W_pj/u_p,
A=s1*I-D*H(s1)-W/(s1+d).
```

Finally, if `M(s)` is the full marked matrix and `r_i` is the chosen reset-into-i row, then for each mark `e=(i,j)`,

```
q_ij=k_i*M(s1)_{r_i,e}/F(s1)_{ii}.
```

The denominator is positive because `K(s1)_{ii}>0`. Insert these observed entries back into `T` to obtain all of `Q`. The formulas prove uniqueness without a controllability, minimality, spectral simplicity, or nonzero-all-entrances assumption. If `u_i=0`, the recovered `b_i` is exactly zero and its row still recovers `k_i`. Reciprocity gives `u_i=0 iff v_i=0`; a disconnected hidden vertex is excluded, whereas a hidden leaf is covered. The denominator selected from one positive `u_p` stays nonzero in a sufficiently small data neighborhood, giving a locally rational, hence locally Lipschitz inverse of the three sampled matrices.

With a known covered set and a state cap of `m+1`, a zero-hidden competitor is distinguishable: it has `y_i(s)=1/k_i` constant at every visible vertex. A genuine one-hidden source has a nonconstant row. Thus this inverse also excludes smaller models under that cap. A larger cap changes the conclusion, as shown below.

## Two points at complete sources; calibrated sharpness

For any observed edge `(i,j)`, `A_ij=0`. If both endpoints are adjacent to the hidden vertex, then

```
H_ij(s)=-u_i*v_j/[k_i*(s+d)] != 0,
r=H_ij(s1)/H_ij(s2)=(s2+d)/(s1+d)>1,
d=(s2-r*s1)/(r-1).
```

The remaining two-point reconstruction is the same as above. Consequently two points suffice whenever the hidden-neighbor set contains an observed edge, including every complete generator and every source with full hidden incidence. Competitors with a different hidden-neighbor pattern cannot defeat this inverse because its nonzero observed off-diagonal sample is directly checked in the data. This gives a locally rational two-point inverse at these sources. The condition here is sufficient; no necessity classification for every other hidden-neighbor pattern is claimed.

If the observed rates are calibrated, `K=F D^(-1)` is known. At two arguments define

```
z_i(s)=[(K(s)^(-1)1)_i-k_i]/s-1=u_i/(s+d).
```

A positive component gives `z_i(s1)/z_i(s2)=(s2+d)/(s1+d)` and determines `d`; the same Schur reconstruction determines the generator. Thus two points suffice at every calibrated one-hidden source, including leaves. One point can fail even for entropy: in the N4 example below keep all observed rates fixed and replace `(u,v)=(1,1)` by `(3/2,2)`. The full six-mark matrices agree at `s=1`; their entropy rates are `log(2)/17` and `4 log(2)/63`.

## Exact two-point entropy counterexample, and worst-case sharpness

Observe all six directed edges of the triangle on visible vertices 0,1,2; vertex 3 is fully hidden. The two generators are

```
Q1 = [-3  1  1  1]      Q2 = [-24/5  6/5  6/5  12/5]
     [ 2 -3  1  0]           [    2   -3    1     0]
     [ 1  1 -2  0]           [    1    1   -2     0]
     [ 1  0  0 -1]           [    2    0    0    -2].
```

Their stationary distributions are respectively `(5,3,4,5)/17` and `(25,18,24,30)/97`. The hidden leaf carries zero stationary current. The visible cycle has affinity `log(2)` and current `1/17` or `6/97`; hence the entropy gap is exactly `5 log(2)/1649 > 0`.

After every reset to a visible vertex, the next observed edge has that same visible origin: all visible-visible jumps are observed, and the only unobserved excursion returns from the hidden leaf to vertex 0. The origin-zero transform is

```
f(s)=k/[s+k+s*u/(s+v)].
```

For `(k,u,v)=(2,1,1)` and `(12/5,12/5,2)` its values are `4/7` at `s=1` and `3/7` at `s=2`. The observed outgoing fractions are `(1/2,1/2)` in both models. All other waiting transforms and outgoing fractions agree. Thus the full six-by-six marked matrices agree exactly at two points. At `s=3`, the origin-zero transforms differ (`8/23` versus `20/57`), and the full matrices differ. The script retains the full matrices at all three points, verifies the stationary identities and the cycle entropy formula, and recovers both generators from three points.

This is not peculiar to the samples 1 and 2. For any prescribed `s1,s2>0`, `s1!=s2`, write a reference leaf response as `y(s)=a0+b0/(s+v0)`, with `a0,b0,v0>0`. For `w>0` near `v0` set

```
C=(s1+v0)*(s2+v0),
a(w)=a0+b0*(v0-w)/C,
b(w)=b0*(s1+w)*(s2+w)/C,
k(w)=1/a(w),    u(w)=b(w)/a(w),    v(w)=w.
```

The two `y` values, hence the two transforms, agree exactly. The domain also requires `a(w)>0`, which holds in an open interval around `v0`. Using the same visible triangle rates (origin-zero outgoing fractions one half, and the other rows fixed as above), stationary unnormalized weights are `(10/k,3,4,10*u/(k*v))`. Its entropy is `log(2)/Z(w)`, where

```
Z(w)=7+10*a(w)+10*b(w)/w,
Z'(w)=-10*b0*s1*s2/(C*w^2)<0.
```

Thus any two prescribed positive arguments admit distinct entropy rates in this N4 class. Add any number `r` of visible leaves to vertex 1, with both directions observed and rate one. The exact observation agreement persists, all but one vertices remain covered, and the two displayed entropies become `log(2)/(17+3r)` and `6 log(2)/(97+18r)`, which remain different. N5 and N6 extensions are checked exactly. Three is therefore the sharp worst-case number for both generator and entropy recovery in this observation class for every fixed `N>=4`. This conclusion does not assert that three is necessary at complete sources; two suffice there.

## Corrected local-ceiling condition: every microscopic pair matters

Within the specified fixed-count one-hidden class with unknown reciprocal support, a finite local upper entropy ceiling exists exactly when the source generator has complete support.

Sufficiency follows from the two-point inverse at complete sources: bounded continuous Laplace statistics vary continuously under weak convergence of the row waiting laws; the local rational inverse forces every nearby admissible generator into a small neighborhood of the positive complete source. All rates there are bounded and bounded away from zero, stationary probabilities are continuous, and the finite sum of flux-log-ratio terms is locally bounded (indeed locally Lipschitz in the sampled matrix coordinates).

For necessity, take any missing unordered pair `{i,j}`. It is unobserved because resolved marks have positive rates. Open `q_ij=epsilon` and `q_ji=2^(-1/epsilon^2)`. Keep other off-diagonal rates fixed, and adjust the corresponding generator diagonals. The generators converge to `Q0`, preserve irreducibility and reciprocal support for every positive sufficiently small epsilon, and have `pi_i -> pi_i^0>0`. The new edge contributes asymptotically `pi_i^0*log(2)/epsilon`; the other edge contributions stay finite. Thus entropy diverges while waiting laws converge. The law convergence follows from finite-dimensional killed semigroup continuity and a uniform exponential tail in a neighborhood of the irreducible source; in particular it holds in row TV and weak topology.

For fixed observed rates and fixed trace, subtract the sum of the opened rates from any existing positive **unobserved ordered rate** before adjusting diagonals. Such a rate always exists with one fully hidden vertex. Its positivity survives for small epsilon. The original common upper rate cap also survives because the opened rates eventually lie below it and the compensating rate decreases. More generally, outside the one-hidden scope, the exception is a zero unobserved-rate budget: if all positive rates are observed and their calibrated sum already fixes the trace, the constrained class is a singleton and this compensation is impossible.

The proposed weaker condition, adjacency of the hidden vertex to every visible vertex, is therefore false. An explicit N4 source has unit bidirectional rates on `{01,12,03,13,23}`, observed pairs `{01,12}`, and the missing visible-visible pair `{02}`. The hidden vertex 3 touches every visible vertex and the source is reversible with `pi=(1,1,1,1)/4`. For integers `n>=2` set

```
q02=1/n,    q20=2^(-n^2),    q03=1-1/n-2^(-n^2).
```

Keep all other original rates. Observed rates, trace `-10`, and upper rate cap one are fixed, but `sigma/n -> log(2)/4`. Exact stationary solves and 100-digit entropy diagnostics for n=2,4,8,16,32 are retained. The limit proof, not the finite list of values, establishes unboundedness.

If the microscopic support itself is fixed, this necessity fails: no missing pair can open. The three-point inverse instead gives a local entropy bound at every reciprocal irreducible one-hidden source, since each fixed supported rate stays positive locally.

## Larger models invalidate the exact state-cap conclusion

Given any one-hidden source, split h into two hidden clones h1,h2. Split every visible entrance rate equally between the clones; give both clones the original exit row `v`; keep visible-visible rates; add internal rates `h1->h2=1` and `h2->h1=t>0`. The model is irreducible and reciprocal. The membership matrix `C` collapsing the two clones satisfies exactly

```
Q_split*C=C*Q,     T_split*C=C*T,
C*B=B_split,      R_split*C=R,
```

where `B` is the marked exit matrix and `R` selects mark reset states. The semigroup intertwining proves equality of all full marked waiting laws at every time. At `t=0` the limiting split chain remains irreducible because both clones receive positive inflow from visible vertices and have positive visible exits. Thus `pi_h1(t)` tends to a positive limit, and the internal edge contributes `-pi_h1(0)*log(t)+O(1)`. Other supported edge terms remain finite. One additional fully hidden vertex consequently permits an unbounded exact entropy fiber, even above a complete source. This is a direct application of established lumpability/state-splitting mechanisms, not a claimed new general mechanism.

The checker constructs a complete N4 source, N5 split models at rational t, and verifies the exact killed intertwining and three independent resolvent evaluations. The intertwining is the all-time certificate; the samples are secondary arithmetic checks.

## Reproduction and limits

Run from the repository root:

```
.venv\Scripts\python.exe -B analysis/novelty_loop/one_hidden_independent.py
```

The self-contained script and inputs are [one_hidden_independent.py](../../analysis/novelty_loop/one_hidden_independent.py). The execution output, source SHA-256, UTC timestamp, interpreter/platform, SymPy/mpmath versions, exact rational generators, observed mark definitions, and numerical precision are in [one-hidden-independent.json](one-hidden-independent.json). The successful run records 12 exact reconstruction cases, the N4/N5/N6 entropy witnesses, the calibrated witness, the missing-pair family, and killed-intertwining checks. No optimizer, RNG, tolerance-based equality, symbolic generic parameter solver, or formal proof assistant was used. The matrix identities are exact rational calculations; the parameter-domain, continuity, and divergent-limit arguments are conventional proofs. A broader necessity classification for two-point recovery in all sparse hidden-incidence patterns remains open in this note. No external primary literature was read for this bounded algebraic check, and no publication-priority claim is made.
