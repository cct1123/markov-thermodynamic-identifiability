# Publication audit: the balanced-theta two-generator endpoint

Independent audit, 2026-09-11 UTC. Scope: mathematical validity and claim boundaries of the exact balanced-theta whole-fiber theorem, with special attention to the endpoint. Only this audit file was written; accepted outputs were not overwritten. This is a conventional proof audit with exact calculations, not formal verification or a novelty certification.

**Result:** no substantive mathematical gap was found in the endpoint's two-generator exhaustion or entropy separation. The connected and disconnected hidden-support arguments are genuinely global. A new exact calculation independently reconstructs the generator from the cone equality conditions and matches the separately derived physical-path witness entry by entry. Publication still requires assembling the currently distributed argument and comparing the precisely scoped result with prior literature; successful reproduction alone does not discharge that latter obligation.

## 1. Precise theorem audited

Let `C5` consist of finite, time-homogeneous row CTMC generators with at most five states, two distinct named visible states `x,y`, nonnegative off-diagonal entries, zero row sums, irreducibility, and reciprocal support `q_ij>0 iff q_ji>0`. There is one kinetic channel per ordered pair. All states are even under time reversal. Only the two individual directed transitions `+=(x,y)` and `-=(y,x)` are marked; all other jumps are unobserved. No support graph, common positive rate cutoff, or bound on similarity coordinates is supplied to the inverse problem.

For a generator, delete the two marked off-diagonal entries and keep all diagonals to obtain `T`. In mark order `(+,-)`, use reset rows `R=(e_y^T;e_x^T)` and columns `B=(q_xy e_x,q_yx e_y)`. Equality means the entire shared matrix-valued function `Psi(u)=R exp(Tu) B`, including its joint mark probabilities and absolute time scale, agrees for every `u>=0`. Hidden permutations are identified; the visible states and mark meanings are fixed.

Define, in state order `(x,y,h,k,l)`,

```text
Q(z) = [[-11, 1, 2, 0, 8],
        [  2,-20,0, 7,11],
        [  3, 0,-7,4, 0],
        [  0, 6, 5,-11,0],
        [  z, z, 0, 0,-2z]],   z>0.
P(z) = 352z^4-3168z^3-4644z^2-11340z-7623.
```

Let `z*` be the unique positive real root of `P`, approximately `10.5571496686650`. Then the following claims survive this audit:

1. The kernel of `Q(z*)` has minimal linear realization dimension five. Its entire fiber in `C5` has exactly two generators up to hidden permutations: `Q(z*)` and the path generator defined exactly by equations (3)–(6) of [the endpoint note](theta-balanced-boundary.md). An alternative exact definition from the cone is given in Section 5 below.
2. With `sigma=sum_{i<j}(pi_i q_ij-pi_j q_ji) log[(pi_i q_ij)/(pi_j q_ji)]` on present edges, natural logs and `k_B=1`, the respective entropy values lie in the disjoint exact rational intervals `[0.062946400236,0.062946400237]` and `[0.065579685966,0.065579685967]`. The entropy fiber is therefore exactly a two-point set, not merely bounded or known to contain two points.
3. On the same balanced ray and under the same cap, the entropy fiber is unbounded for `0<z<z*`; the entire generator is unique for `z>z*`. These extensions use additional subcritical constructions reviewed separately below.
4. Allowing six physical states, including nonminimal realizations, makes the endpoint entropy fiber unbounded by splitting one fully hidden state. The sixth-state statement is a different admissible class.

The theorem does not assert that arbitrary five-state data have this behavior, that exact identification is statistically stable, or that the two-point phenomenon is new. “Minimal five-state example” here certifies the linear order of this specific kernel. A separate claim that five is the smallest order for *any* bounded-nonunique fiber additionally needs the repository's four-state classification, which is not re-audited in this file.

## 2. Data reduction and minimality checked independently

The zero-time values give `q_xy=1`, `q_yx=2`. The next coefficients recover the entire visible block, including the diagonals `-11,-20`. With the visible coordinate plane selected on both sides, the visible resolvent determines the hidden response by a Schur complement. Thus every competitor has the same hidden matrix transfer, not merely two separately fitted scalar phase-type laws.

The source hidden blocks are

```text
X = [[2,0,8],[0,7,11]],
Y = [[3,0],[0,6],[z,z]],
H = [[-7,4,0],[5,-11,0],[0,0,-2z]].
```

Independent exact minors are

```text
det[Y[:,0],Y[:,1],(HY)[:,0]] = -9z(4z-9),
det[Y[:,0],Y[:,1],(HY)[:,1]] = -18z(2z-3),
det[X[0,:];X[1,:];(XH)[1,:]] = -14(22z+19).
```

The first two cannot vanish simultaneously at positive `z`; the last never vanishes there. Hence every balanced source, including the endpoint and repeated-hidden-pole parameters, has hidden reachable/observable dimension three and full marked dimension five. At the endpoint even the first control minor alone suffices. The visible plane adds two dimensions because `R,B` directly select it; subtracting its contributions from successive powers of `T` leaves precisely the hidden reachability/observability spaces.

The basis proof in [compatibility-orbit.md, Sections 1–2](compatibility-orbit.md#1-short-proof-of-minimal-realization-similarity) is valid: equality of Markov parameters identifies a unique invertible map on reachable vectors; observability makes the map well-defined. The visible rows and columns pin this map to `diag(I2,U)`. Invertibility of the killed generator and `T1=-B1` then give `U1=1`. The entries of `U` can have either sign. Minimality plus the cap forces every competitor to have exactly five states and to lie in this orbit; a smaller, nonminimal, or differently dimensioned competitor is not silently omitted.

As a valid data weakening, exact equality of derivative matrices of orders `0,...,9` suffices within `C5` by the block-diagonal Cayley–Hamilton argument. Approximate moments, rounded derivatives, separately normalized waiting densities and finitely many approximate time samples do not have this implication.

## 3. Disconnected hidden support is fully exhausted

At the endpoint `2z*>beta=9+2sqrt(6)>alpha=9-2sqrt(6)>0`. The hidden transfer has three distinct rank-one residues at `-alpha,-beta,-2z*`. The middle residue has negative off-diagonal entries; the other two residues are strictly positive. Their explicit outer-product factors in [theta-fast-spectral-audit.md, Section 2](theta-fast-spectral-audit.md#2-modal-realization-and-fixed-order-completeness) multiply correctly.

A disconnected **bidirected** hidden block on three vertices has either three singletons or one connected pair and a singleton. Three singletons, or a singleton assigned the `beta` pole, contradict the negative middle residue. Assigning the singleton the `alpha` pole leaves a pair whose dominant pole is `-beta`; its Perron projector gives a nonnegative transfer residue, another contradiction. Thus the singleton must carry `-2z*`.

The pair's zeroth response is `diag(6,42)`. Nonnegativity and reciprocal visible support force its two states to attach separately to `x` and `y`: a shared-port state would create positive off-diagonal entries, while both positive diagonal entries require one state for each port. The first moments and row sums yield

```text
x1*y1=6, x2*y2=42, y1+h=7, y2+k=11,
x1*h*y2=48, x2*k*y1=105.
```

They give `hk=20`, `19h-hk=56`, and uniquely `h=4,k=5,y1=3,y2=6,x1=2,x2=7`. The singleton residue and its exit sum fix entrances `(8,11)` and exits `(z*,z*)`. This proves exactly the source generator in this branch. It is not merely an exclusion of complete graphs or of a chosen residue reassignment.

Reciprocal support matters here: without it a reducible hidden matrix can have directed intercomponent links and need not be block diagonal. The proof does not classify that enlarged class.

## 4. Connected hidden support: global inequality and equality audit

For connected bidirected hidden support, the hidden matrix is irreducible Metzler. In its minimal modal realization, Perron left and right eigenvectors at `-alpha` are strictly positive. The sign is fixed by the positive source output vector. Consequently every cone generator has a strictly positive first modal coordinate, and its section at coordinate one is a **finite nondegenerate triangle containing the origin in its interior**. This covers signed similarities, arbitrary conditioning, both hidden paths and hidden triangles, and every allowed paired-zero visible incidence.

Put `rho=sqrt(6)`, `m=(7+2rho)/5`, `L=(3-rho/2)/8`, `Rw=35rho/88`, `A=z`, `B=z/[4(rho-1)/5]`, `k=(2z-9+2rho)/(4rho)`, and `a=k-1`. The triangle contains `(1,A),(-m,B)`, lies in `v>=L(-m-u), v>=Rw(u-1)`, and is invariant under `(u,v)->(exp(-t)u,exp(-kt)v)`.

The sign exhaustion is sound. Two vertices must have positive height, since a sole positive-height vertex could not reach both input abscissae while all nonpositive-height wedge points lie between `-m` and `1`. An interior origin forces the third height negative. Thus vertices can be labeled `(-ell,P),(c,Q),(d,-W)` with `ell>=m,c>=1,-m<d<1,P,Q,W>0`. This is a consequence of feasibility, not a graph restriction.

For `z>=10.5`, the negative-bottom-abscissa case `d<0` is excluded by the inherited inequality with strict polynomial margin `72(z-10)^2+836(z-10)+835>0`. For `d>=0`, lower-face invariance gives `P<10/7`, while the inputs force `Q>=A>B>2` and `ell>m`. The bottom-coordinate bound and the exact wedge-apex inequality then force `d>d0>0` and `W<=Rw(1-d)`. All source constants and the apex comparison are checked with rational enclosures of `sqrt(6)`.

The subsequent envelope maximizations are valid on the entire physical domain:

- At fixed `d,W,c,Q`, left containment/invariance bound `ell` by the unique intersection of `L(ell-m)` and `ell W/(a ell+kd)`. The containment height increases strictly in both `ell` and `P` because `Q>P`. Equality forces both to their intersection values.
- For the right vertex, the increasing lower-input line and decreasing invariance hyperbola have a unique relevant crossover `c*` beyond the pole `kd/a`. On `c>=1`, the height increases up to that crossover and decreases afterwards whenever it could reach `B`. If `c*<1`, even the bound at `c=1` is below `A`, impossible. The algebraic intersection `c=d` is outside the physical domain; uniqueness should be stated on `c>=1`, not for unrestricted real `c`.
- Increasing `W` to `Rw(1-d)` strictly increases the final height envelope. In the notation of the cone note, `t,Q*` increase and `r=c*/Q*` decreases; the corresponding height partial derivatives have signs `+,+,-` since `Lt<Q*`. The inequalities `Q*>=A` and `P*<2` persist during this relaxation.

Writing `J=am+k`, the final necessary condition is

```text
f0+f1*t+f2*t^2 >= 0 for some t>0,
f0=A*Rw*m/L-B*J^2,
f1=A*(Rw/L+k-a*m)+L*J^2+Rw*J-2*B*J*a,
f2=a*(L*J+Rw-A*(1+L*k/Rw)-B*a).
```

The envelope differs from `B` by this numerator divided by `(J+at)^2`. Its discriminant is

```text
f1^2-4f0*f2 = -(11/1200+11sqrt(6)/4200)*(z+19/22)^2*P(z)/352.
```

At `z*`, rigorous signs give `f0<0,f1>0,f2<0`, so the numerator is nonpositive everywhere and zero only at `t*=-f1/(2f2)>0`. Every step in the chain must therefore attain equality, forcing a single triangle up to vertex permutation. Above `z*`, `f0<0` and the negative discriminant make the quadratic strictly negative everywhere, excluding all connected hidden realizations.

This proof does not optimize over a compact, arbitrarily truncated set of similarities. Every actual connected hidden realization has finite vertices, however large, and is included. A cone ray on the first-coordinate-zero plane is impossible in this connected branch by the strict Perron vector. The disconnected branch, where such a ray can occur, was separately exhausted in Section 3.

## 5. Exact cone construction independently matches the path witness

The equality triangle has an alternative explicit definition:

```text
t=-f1/(2f2), epsilon=L*t*(J+a*t)/[Rw*m+(k*L+Rw)*t],
d=1-epsilon, W=Rw*epsilon, ell=m+t, P=L*t,
c=(k/a)[d+W*epsilon/(A+W)], Q=(A*d+W)/(a*epsilon),
V = [[1,1,1],[-ell,c,d],[P,Q,-W]].
```

Take the modal `D,Xm,Ym` of [the spectral audit](theta-fast-spectral-audit.md#2-modal-realization-and-fixed-order-completeness), and set

```text
Hbar=V^-1 D V, Xbar=Xm V, Ybar=V^-1 Ym,
w=-Hbar^-1 Ybar 1, Wdiag=diag(w),
Hpath=Wdiag^-1 Hbar Wdiag,
Xpath=Xbar Wdiag, Ypath=Wdiag^-1 Ybar.
```

Adjoin the fixed visible block `[[-11,1],[2,-20]]`. In the column order of `V`, the hidden states are `(y-only endpoint, shared endpoint, x-only center)`. Exchanging the final two hidden coordinates gives exactly the path-chart witness's order.

I computed this construction with exact pair arithmetic `a+b*sqrt(6)` over the existing number field `Q(z*)`, independently of the path exit equations. Every entry of the resulting five-state generator equals the path-chart certificate's entry after that permutation. Every final `sqrt(6)` coefficient cancels. The discriminant equality and every division in this reconstruction were exact; no numerical matching tolerance was used.

The replayed physical certificate proves that `V`/chart normalization leads to a physical generator: its seven undirected edges are `xy,x-center,x-shared,y-endpoint,y-shared,endpoint-center,center-shared`, each positive in both directions. Every other off-diagonal entry is exactly zero. The full graph is connected. The source has six undirected edges, so these two classes cannot be hidden relabelings.

Uniqueness of the triangle really does give uniqueness of the normalized generator: for a chosen set of cone rays, positive column rescaling is the only remaining freedom before row normalization, and `w=-Hbar^-1 Ybar1` is uniquely determined because all hidden eigenvalues are nonzero. Physical positivity fixes the allowed scaling. It introduces no free thermodynamic parameter.

## 6. Denominators, boundaries and proof-status limits

The endpoint lies strictly above `beta/2`, away from both hidden-pole coincidences and the exit-chart singularity `det[Y,1]=18-9z=0` at `z=2`. The path formula divides by its quadratic leading coefficient, a tangency denominator, input-anchor coordinates, `1-cd`, and the chart determinant. Exact number-field divisions and inversion succeed in the replay; the leading coefficient is strictly positive. For a physical path, the original tangency denominator equals `-u` times a positive hidden rate, and coincident anchor lines would force a singular chart. The global count does not discard any of the other path-polynomial factors: it is proved by the cone equality argument. Those factors remain in `balanced-path-polynomial.json`.

In the cone proof, `L,Rw,a,W,t,1-d,ell+d,c-d,ell+c,J+at` have the required strict signs in the stated range. The right invariance expression `ac-kd` can be nonpositive before its pole; the proof does not divide by it on that branch. Its hyperbolic bound is used only on the positive-denominator side. At equality the crossover is strictly beyond the pole. Lower-dimensional/collinear triangles are excluded by minimality and the positive Perron normalization; zero-height bottom vertices are excluded by an interior origin.

Existence does not follow solely from equality of the necessary envelope. It is supplied by the exact physical witness. Likewise the finite generator count alone would not establish different entropy values: this is supplied by separate rigorous logarithm bounds. In the fold checker I verified the positive-root isolation, descending coefficient convention, interval evaluation of field elements, powers-of-two log reduction, positive atanh-series tail bound, signed-current interval multiplication, and unordered-edge sum. There is no missing factor of two or unsupported sign decision from a coefficient's sign. Numerical stationary solves and matrix exponentials are diagnostics only.

The resulting entropy difference is enclosed by `[0.002633285729,0.002633285730]`. Thus the endpoint's nonuniqueness is thermodynamic, not just a pair of different generators that happen to dissipate equally.

## 7. Neighboring parameters and the sixth-state caveat

The whole balanced-ray extension is supported by an explicit covering argument, not by extrapolating the fold:

- For `2z<alpha`, a strict simultaneous hidden opening gives a complete realization and the hidden-pair divergence theorem applies.
- At `2z=alpha`, the residue-redistribution construction gives a bidirected pair-plus-singleton realization with unequal pair exit rows; the same divergence theorem applies without needing complete hidden support.
- For `alpha<2z<=beta`, balanced coordinates satisfy both strict thresholds of the two-mode spectral construction.
- For `beta<=2z` and `z<zc=(11+sqrt(1120/11))/2`, the balanced ratio satisfies the first strict opening condition. Thus the old construction covers all `0<z<zc`.
- The new strict cone construction covers `[10.5,z*)`; `10.5<zc<z*`, so there is no uncovered interval. Its strict input/output/inward-flow inequalities survive the stated three small perturbations. These produce a complete normalized CTMC before invoking the adjacent-hidden-pair theorem.

The hidden-pair theorem is valid here: minimality rules out equal full external exit rows, and the complete target gives adjacent external twins. Its normalized two-coordinate path keeps stationary masses bounded away from zero while a directional rate vanishes with its reverse flux positive. This supplies divergence, rather than inferring it from numerical largeness or generator nonuniqueness.

At the endpoint there are three fully hidden states, so the [state-splitting construction](state-splitting-audit.md) applies with one added state. Strong lumping preserves the killed kernel; explicit clone stationary probabilities give positive opposing flux at the vanishing internal rate. Its six-state realizations are nonminimal. Consequently the cap, or an equivalent restriction to minimal realizations, is consequential.

## 8. Assumptions that can and cannot be weakened

The mathematics needs no separate uniform upper rate bound: similarity fixes `-tr Q=49+2z*`, which already bounds every nonnegative off-diagonal rate in the exact fiber. It needs no arbitrary lower rate cutoff, no positive similarity assumption and no fixed hidden topology. Stationarity of the experiment is not needed for the reset-conditioned kernel; stationary entropy refers to the underlying generator.

Explicit full-chain irreducibility can be omitted if one instead assumes a nonnegative row generator under the same cap and exact kernel. Minimality forces every state to be reachable from the visible plane and able to return to it; the positive observed reverse pair then makes the whole chain irreducible. This argument does not remove the reciprocal-support assumption used in the disconnected-hidden classification.

Removing the cap while permitting nonminimal realizations, allowing unresolved/multiple channels, changing which microscopic edges marks denote, allowing one-way physical edges, or replacing the joint kernel by normalized conditional shapes changes the theorem. A fixed complete topology excludes both sparse endpoint representatives. A fixed source topology retains only the source; the path topology retains only the path. Replacing even-state entropy by a different time-reversal convention also requires a new thermodynamic statement.

## 9. Falsification attempts, significance and remaining obligation

The strongest actual counterexample in the saved development remains the exact rational complete realization on `[10.545,10.5455]`, crossing the former local-opening threshold `zc`. Its second-order opening falsified the proposed first-order global boundary. Larger unrounded steps failed positivity and were retained as failed attempts. The current envelope explicitly contains the finite-vertex effect that defeated that shortcut; its `t->0` limit recovers the old threshold. The 26-start SLSQP probe is discovery evidence only and was not rerun or used to certify exclusion.

In this audit I specifically tested the potential omitted branches: a Perron coordinate tending to zero, disconnected pole reassignment, a right-vertex crossover on the wrong side of its pole, equality without an admissible triangle, arbitrary column scalings, and an accidental mismatch between the geometric and physical-path endpoints. The first three are excluded by the proof's stated domains; the final three are closed by normalization and the new exact cross-construction check. No counterexample to the endpoint resulted. The first replay of this file's embedded code failed its final minimality assertion because SymPy structural equality compared a factored expression with its expanded form; their expanded difference was exactly zero. The assertion now compares that difference to zero. This was a check-implementation error, not a failed mathematical identity. The historical interrupted symbolic simplifications remain algorithmic failures, not evidence for or against feasibility.

The potentially publishable feature is the **entire two-point entropy fiber under unknown reciprocal topology at fixed minimal order**, with the neighboring unbounded/unique transition. Similarity equivalence, isolated positive representations, invariant cones, and entropy ambiguity are established mechanisms. This audit performs no new broad novelty search; [the finite-fiber prior-art audit](../evidence/finite-fiber-prior-art.md) records the closest inspected comparisons and remaining original-source gaps. Exact count in this CTMC class must not be advertised as a first-ever finite positive-realization phenomenon without resolving that comparison.

No remaining mathematical obligation for the endpoint was found. For a publication, the principal presentation obligation is to assemble Sections 2–6 into one self-contained proof, state the right-crossover uniqueness on its physical domain, and retain the exact witness/entropy certificate with pinned dependencies. The broad five/six-state classification and novelty question remain separate, unresolved claims.

## 10. Coverage and reproduction record

Read and audited the relevant proof chains: `formulation.md`; `compatibility-orbit.md` Sections 1–2; `theta-parameter-strata-audit.md` rank/chart argument; `theta-fast-spectral-audit.md` complete modal/Perron/sign/reducible proof; `theta-family-construction-audit.md` Sections 1–5 and support conclusion; `balanced-cone-bound.md` all six proof sections; `theta-balanced-boundary.md`; `theta-fast-hidden-paths.md` support and exit-chart derivation; `balanced-boundary-witness.md`; `hidden-pair-boundary-audit.md` Sections 1–6; `positive-realization-obstructions.md`, including the slow-pole construction; `state-splitting-audit.md` construction, lumping and stationary-flux proof; and `theta-global-audit.md` for the stronger historical local-isolation counterexample. Older four-state classifications were not treated as newly verified conclusions.

Read the complete implementations of `check_balanced_cone_bound.py`, `check_balanced_cone_sufficiency.py`, `check_balanced_fold.py`, `derive_balanced_path.py`, and `check_theta_fast_spectral.py`. Inspected their relevant accepted result objects plus `balanced-boundary-witness.json` and the discovery probe metadata. Existing source-hash mappings checked for those result objects had no detected mismatch. The new exact source-minor and cone/path comparison does not rely on the older spectral checker's arithmetic helper.

On 2026-09-11 UTC, Python 3.9.12 / SymPy 1.14.0 replayed the four endpoint scripts with `Path.write_text` replaced by an in-memory JSON capture. All assertions passed; the exact fold matrices, stationary vectors, support and entropy intervals matched the saved result. Approximate elapsed times were 1.419 s (cone bound), 0.295 s (strict sufficiency), 0.852 s (fold), and 37.614 s (path factorization). No accepted file was written by these replays.

Reproduction from the project root, PowerShell:

```powershell
@'
import sys, runpy, json
from pathlib import Path
sys.path.insert(0, 'analysis')
captured = []
def capture(path, data, *args, **kwargs):
    captured.append((str(path), json.loads(data)))
    return len(data)
Path.write_text = capture
for name in ['check_balanced_cone_bound.py', 'check_balanced_cone_sufficiency.py',
             'check_balanced_fold.py', 'derive_balanced_path.py']:
    runpy.run_path(str(Path('analysis')/name), run_name='__main__')
for path, data in captured:
    if path.endswith('balanced-fold-checks.json'):
        old = json.loads(Path(path).read_text())
        for key in ['U','source','target','stationary_source','stationary_target',
                    'target_support','entropy_source_certified',
                    'entropy_target_certified','entropy_difference_certified']:
            assert data[key] == old[key], key
print('PASS: four replays captured without writes; exact fold output unchanged')
'@ | .\.venv\Scripts\python.exe -B -
```

Audited source SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `analysis/check_balanced_fold.py` | `74ea7faa7caa6ad20f0df0ce2ba16b197a283a79d4e058639a04a657a2f02c81` |
| `analysis/check_balanced_cone_bound.py` | `f1247b3f17f9b3f641c3d041500009acce74e721ee2aa1cf316517afbadf2c9b` |
| `analysis/check_balanced_cone_sufficiency.py` | `0d27522282f0012ecc76ec3b82b68f5946c7e5d05a8a91c99937303fb23e1e2e` |
| `analysis/derive_balanced_path.py` | `4fc6839878d804990cfa4a8bfa2346cf8fbf395d9967d33f277b0693310243a5` |
| `outputs/balanced-fold-checks.json` | `a854889cd532ea094c8f8eeac88cd736223e5725d0611ec43649380cd90e9be8` |

### Independent cone-to-path exact check

The following code preserves the new calculation. It uses exact arithmetic in pairs over `Q(z*)`, and only reads the path witness's encoded coefficient lists for comparison. It does not reuse its path exit-chart formula or its generator construction.

```python
import sympy as sp, json
from pathlib import Path
zs=sp.Symbol('z')
poly=sp.Poly(352*zs**4-3168*zs**3-4644*zs**2-11340*zs-7623,zs)
zr=sp.CRootOf(poly,1)
F=sp.QQ.algebraic_field(zr)
class Pair:
    def __init__(self,a=0,b=0):
        if isinstance(a,Pair): self.a,self.b=a.a,a.b
        else: self.a,self.b=F.convert(a),F.convert(b)
    def __add__(x,y):
        y=Pair(y); return Pair(x.a+y.a,x.b+y.b)
    __radd__=__add__
    def __neg__(x): return Pair(-x.a,-x.b)
    def __sub__(x,y): return x+-Pair(y)
    def __rsub__(x,y): return Pair(y)+-x
    def __mul__(x,y):
        y=Pair(y); return Pair(x.a*y.a+6*x.b*y.b,x.a*y.b+x.b*y.a)
    __rmul__=__mul__
    def __truediv__(x,y):
        y=Pair(y); n=y.a*y.a-6*y.b*y.b
        if n==F.zero: raise ZeroDivisionError('zero conjugate norm')
        return x*Pair(y.a/n,-y.b/n)
    def __rtruediv__(x,y): return Pair(y)/x
    def __pow__(x,n):
        if n<0: return (Pair(1)/x)**(-n)
        r=Pair(1)
        for _ in range(n): r=r*x
        return r
    def __eq__(x,y):
        y=Pair(y); return x.a==y.a and x.b==y.b
def mat(rows): return [[Pair(x) for x in row] for row in rows]
def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def inv(a):
    n=len(a); r=[row[:]+[Pair(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        i=next(i for i in range(j,n) if r[i][j]!=0)
        r[j],r[i]=r[i],r[j]
        pivot=r[j][j]; r[j]=[x/pivot for x in r[j]]
        for i in range(n):
            if i!=j:
                scale=r[i][j]; r[i]=[x-scale*y for x,y in zip(r[i],r[j])]
    return [row[n:] for row in r]
z=Pair(F.from_sympy(zr)); rho=Pair(0,1)
L=(3-rho/2)/8; Rw=35*rho/88; m=(7+2*rho)/5
k=(2*z-9+2*rho)/(4*rho); a=k-1; J=a*m+k
A=z; B=z/(4*(rho-1)/5)
f0=A*Rw*m/L-B*J**2
f1=A*(Rw/L+k-a*m)+L*J**2+Rw*J-2*B*J*a
f2=a*(L*J+Rw-A*(1+L*k/Rw)-B*a)
assert f1**2-4*f0*f2==0
t=-f1/(2*f2); eps=L*t*(J+a*t)/(Rw*m+(k*L+Rw)*t)
d=1-eps; W=Rw*eps; ell=m+t; P=L*t
c=k/a*(d+W*eps/(A+W)); Q=(A*d+W)/(a*eps)
V=mat([[1,1,1],[-ell,c,d],[P,Q,-W]])
D=mat([[-9+2*rho,0,0],[0,-9-2*rho,0],[0,0,-2*z]])
Xm=mat([[3+rho/2,3-rho/2,8],[35*rho/8,-35*rho/8,11]])
Ym=mat([[1,4*(rho-1)/5],[1,-4*(rho+1)/5],[z,z]])
Vi=inv(V); Hb=mm(mm(Vi,D),V); Xb=mm(Xm,V); Yb=mm(Vi,Ym)
w=mm(inv(Hb),mm(Yb,mat([[-1],[-1]])))
q=mat([[-11,1,0,0,0],[2,-20,0,0,0],[0]*5,[0]*5,[0]*5])
for i in range(3):
    for j in range(3): q[2+i][2+j]=Hb[i][j]*w[j][0]/w[i][0]
    for j in range(2): q[2+i][j]=Yb[i][j]/w[i][0]
    for j in range(2): q[j][2+i]=Xb[j][i]*w[i][0]
order=[0,1,2,4,3]; q=[[q[i][j] for j in order] for i in order]
old=json.loads(Path('outputs/balanced-fold-checks.json').read_text())
def decode(coeffs):
    out=Pair(0)
    for c in coeffs: out=out*z+Pair(sp.Rational(c))
    return out
expected=[[decode(x) for x in row] for row in old['target']]
assert q==expected
assert all(x.b==F.zero for row in q for x in row)
X=sp.Matrix([[2,0,8],[0,7,11]])
Y=sp.Matrix([[3,0],[0,6],[zs,zs]])
H=sp.Matrix([[-7,4,0],[5,-11,0],[0,0,-2*zs]])
assert sp.factor(sp.Matrix.hstack(Y,H*Y[:,0]).det())==-9*zs*(4*zs-9)
assert sp.factor(sp.Matrix.hstack(Y,H*Y[:,1]).det())==-18*zs*(2*zs-3)
assert sp.expand(sp.Matrix.vstack(X,(X*H)[1,:]).det()+14*(22*zs+19))==0
print('PASS exact cone/path equality, cancellation, invertibility and minimality minors')
```

To replay the last block from PowerShell:

```powershell
$auditText = Get-Content -Raw -LiteralPath analysis/publication-endpoint-audit.md
$auditCode = [regex]::Match($auditText, '(?s)```python\r?\n(.*?)\r?\n```').Groups[1].Value
$auditCode | .\.venv\Scripts\python.exe -B -
```
