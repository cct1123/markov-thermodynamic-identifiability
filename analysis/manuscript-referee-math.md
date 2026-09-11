# Mathematical referee review of the assembled manuscript

2026-09-11 UTC. Reviewed `manuscript/main.tex` and `manuscript/supplementary/proofs.tex` as a self-contained article, against the underlying proofs and exact artifacts. Also inspected the reproduction driver where its scientific descriptions affected the manuscript. I did not edit the manuscript or its scripts. The first independent review and computation remain in [manuscript-mathematical-review.md](manuscript-mathematical-review.md).

**Verdict:** the central theorem statements and their assembled proofs agree. The all-support argument and four-part subcritical covering now appear in the article, rather than relying on historical audit labels. One material transcription error in a stationary weight was found and reported; the coordinator corrected it during this review, and I verified the correction on disk. The zero-entry wording was also corrected. The remaining items below concern precise notation, full generality of one lemma, arithmetic reproducibility, and explanatory completeness; none changes the two central conclusions.

## 1. Corrections found and current status

### Corrected: the three-state hidden stationary weight

In the initial main-file version, the proof of the fixed-trace three-state proposition displayed

\[
w_h=1+2e-ek.
\]

The correct weight is

\[
\boxed{w_h=1-k+2e-ek.}
\]

With the missing `-k`, the weights do not sum to the stated Z and do not solve wQ=0. The equation for Z, the current, entropy, and finite-window bound were already the correct formulas. The coordinator inserted `-k`; the current `main.tex` line 186 has the correct expression. I independently checked by exact SymPy arithmetic that the corrected weights solve wQ=0, sum to Z, and satisfy

\[
3w_h-Z=(e-k)(5+e-k).
\]

Thus the finite-window stationary-TV term used later is consistent.

### Corrected: six zero entries, three missing reciprocal pairs

The initial endpoint paragraph said “six absent directed pairs.” There are six absent **off-diagonal entries**, representing three absent unordered reciprocal pairs. The current `proofs.tex` paragraph uses “six absent off-diagonal entries.” Its seven present reciprocal edges and fourteen positive offdiagonals agree with the exact certificate.

### Remaining small changes recommended

1. **Define the observation for the larger observed set in the two-hidden-state lemma.** Section II defines Obs, R, B, and d only for two marks. The neighborhood lemma then allows any nonempty reverse-closed resolved set. Add: for a mark I=(a_I,b_I), use reset row R_I=e_{b_I}^T, column B_I=q_{a_Ib_I}e_{a_I}, and maximum row TV over all marks. The hidden shear fixes every endpoint, so its converse observation-invariance argument works directly for these matrices. This avoids silently using two-by-two notation for the general statement. The central one-pair theorem is unaffected.

2. **Replace “sign change between positive zero and infinity.”** Write `P(0)<0`, `P(z) tends to +infinity as z tends to +infinity`, together with Descartes' rule. “Positive zero” is not the intended mathematical statement.

3. **Make the cone parameter range explicit before its reuse.** The modal paragraph first says the poles are distinct at z>=z_*, while the subcritical proof later uses the same cone construction on [21/2,z_*). All modal/Perron arguments hold on the larger range z>=21/2 because 2z>beta there. State that range explicitly; reserve the z>=z_* condition for the disconnected-exhaustion conclusion where desired. This is a scope clarification, not a failure at a subcritical pole.

4. **Specify the rational square-root enclosure in the interval table recipe.** The text tells a reader to use a rational enclosure of sqrt(6) but does not say which one establishes the printed constants. The executed independent computation uses

   \[
   2.449489742783178098197284<\sqrt6<
   2.449489742783178098197285,
   \]

   with exact squaring to check endpoints, and outward rational rounding at 24 decimal places after each interval operation. These details plus the already printed z interval and shifted-polynomial evaluation make the finite certificate directly reproducible without selecting an unstated precision.

5. **Clarify the converse from inward derivatives to a Metzler realization.** One short sentence or displayed identity would close the only geometric step currently left as a standard fact: with first row of V equal to 1^T, `A_c=V^{-1}(D+alpha I)V` has zero column sums. Its off-diagonal entry `(A_c)_{ji}` is the inward derivative at vertex i toward the facet opposite vertex j, divided by that vertex's positive facet height. Strict inward conditions therefore give positive offdiagonals of `Hbar=A_c-alpha I`. This justifies the complete realization asserted after the three strict perturbations. Necessity and sufficiency then have equally explicit derivations.

6. **Correct the reproduction README's no-optimizer wording.** `manuscript/scripts/README.md` says no optimizer is used by the driver. The driver replays `analysis/check_five_state_extensions.py`, which imports and calls `scipy.optimize.linprog`. The mathematical conclusion is properly certified afterwards by exact checks and is not inferred from optimization. Say this, or restrict the no-optimizer assertion to the new manuscript figure/inverse computations. The main article's narrower statement that optimization is not a nonexistence proof is accurate.

7. **Attribute the independent cone check to the driver, rather than the path checker alone.** The exact cone/path equality is present in `embedded_cone_check()` in the reproduction driver; `check_balanced_fold.py` itself constructs the path witness. The main methods paragraph can refer to “the endpoint checks” or “a separate exact cone reconstruction” to match this arrangement. There is no missing check: the package actually executes it.

## 2. Global balanced-fiber proof

The assembled argument now meets the consequential global obligations:

* The cap-five minimum order is proved by the three explicit minors, including the z=2 chart singularity and both repeated-hidden-pole parameters.
* The realization-basis map pins both visible rows and columns and normalizes through invertibility of the killed generator. Signed hidden similarities remain allowed.
* The disconnected hidden partitions are exhausted by nonnegative singleton residues and the Perron residue of the possible pair. The remaining pair-plus-singleton case is pinned by exact zeroth and first moments and row sums.
* The connected case covers both paths and triangles, including paired-zero visible incidence. Strict Perron coordinates rule out finite-chart omissions at infinity. The triangle sign pattern is derived from the wedge and interior origin.
* The d<0 branch is explicitly excluded and the apex bound controls the d>=0 branch. Left and right envelope maximizations retain their strictness and domains. In particular, the irrelevant second line/hyperbola intersection c=d is excluded, and no division is made across the pole without a domain condition.
* The discriminant identity excludes all connected supports above z_*, while the equality chain forces one triangle at z_*. Unique row normalization removes ray-scaling freedom.
* The explicit algebraic witness separately supplies existence, connected reciprocal support, and a second entropy value. Equality in a necessary envelope is not used as a substitute for admissibility.

The phrase “precisely the hidden path specified below” follows first as forced zero constraints and then as exact positivity of all remaining rates in the endpoint certificate. The final exact support check is essential; it is correctly included.

The proof does not need a classification of every five-state model, an exclusion based on optimizer failure, or the separate smallest-cap theorem. The current manuscript avoids these stronger claims.

## 3. Complete subcritical covering

All four intervals are valid and cover the entire positive subcritical ray. The first commutator opens all missing directions below alpha/2. The two-mode construction covers the closed interval from alpha/2 to beta/2, where its strict entrance and exit inequalities are already satisfied at the lower endpoint. It remains physical at both repeated poles: at beta/2 its pair is unjoined with equal escapes, exactly the allowed special case of the shear lemma. The isolated z=2 chart failure is covered by the first construction.

The explicit fast K has no hidden singular denominator: M_s>0 and z>0. Its midpoint interval condition is precisely 11M_s^2<1120, and the displayed range strengthens that to <=1100. Together with L_s M_s>=20 this proves all eight opening derivatives positive, including the two bounds that use the redundant factor L_s M_s. The four choices q,v,u,p/r are correctly ordered and need no numerical search.

In the final interval the positive discriminant supplies the one strict input margin omitted from the table. The other table inequalities hold on the larger closed rational enclosure. The three perturbations open every input/output incidence and every offdiagonal inward derivative while preserving a finite list of strict margins. They need a positive perturbation size for each fixed z<z_*; no uniform size as z approaches the fold is claimed. The resulting normalized complete model is minimal by the common observation, so its full external exit rows cannot coincide. The shear then gives genuine divergence, rather than merely a second generator.

## 4. Local criterion and finite records

The three-Laplace inverse is consistent with the row/column convention F=K diag(r,s). The source-positive entrance branch prevents division by an entrance that opens from zero at a tree. Its Schur matrix is invertible for every positive Laplace argument; the difference ratio and rates have nonzero source denominators. Two-state candidates cannot approach the positive source differences. Consequently the cap-free positive triangle result is proved from bounded continuous tests, not from differentiating approximately known densities.

The sparse construction preserves trace and observed rates because it compensates on an existing positive unobserved direction. Such a direction exists for a connected source with one observed pair and N>=3. For a complete generator the stationary law and entropy are smooth locally; for any missing pair the asymmetric opening gives a pi_i^0/e divergence. The all-N completion argument properly takes its two limits in order and creates unequal full external exit rows without a minimality assumption. Its Duhamel bound controls the integrated joint laws over all waiting times. The sharp iff follows in both TV and weak topology, and the tight-cap counterexample correctly rejects an arbitrary additional cap.

The fixed-trace explicit family's separation hazard is at most e+k: the three row sums of offdiagonal absolute rate differences are e, k, e+k. Reset-conditioned source mean waiting times are 1 and 2, so d<=2(e+k)<4e. For stationary windows the initial-TV term equals `(e-k)(5+e-k)/(3Z)` with the corrected stationary weight. Since Z>3 and e<1/2, it is at most 11e/18; e+k<2e gives the printed window bound. The exact hidden-pair similarity cancels in every marked-record likelihood, including the empty record. This separately proves the finite-window convergence needed for the confidence result; no implication from row TV alone is assumed.

The upper-confidence proof is valid for measurable extended-real statistics with uniform finite-sample coverage and a fixed stationary window. The probability-of-infinity conclusion uses the appropriate order: first transfer each finite threshold through total variation, then send that threshold to infinity. It does not make a pointwise asymptotic or Bayesian assertion.

## 5. Arithmetic statements checked directly in this review

I inspected the printed endpoint rational field formulas and selected root interval against `outputs/balanced-fold-checks.json`. Direct exact Horner interval evaluation of the saved degree-at-most-three field coefficients confirms there are exactly fourteen nonzero offdiagonal entries, and every resulting positive-rate interval lies strictly inside (1/5,12), as newly stated in the manuscript. This is a fresh bound check from the saved exact coefficients and original root interval, not a fresh independent construction of those coefficients.

The short executed check also verifies the corrected stationary weight and finite-window identity. It can be reproduced from the project root with the local Python environment:

```python
import json
from pathlib import Path
from fractions import Fraction as F
import sympy as s
p=json.loads(Path('outputs/balanced-fold-checks.json').read_text(encoding='utf-8'))
lo,hi=map(F,p['root_interval'])
def bounds(coeff):
    low=high=F(0)
    for value in coeff:
        corners=[low*lo,low*hi,high*lo,high*hi]
        low,high=min(corners)+F(value),max(corners)+F(value)
    return low,high
vals=[bounds(p['target'][i][j]) for i in range(5) for j in range(5)
      if i!=j and any(F(c) for c in p['target'][i][j])]
assert len(vals)==14 and all(F(1,5)<a<=b<12 for a,b in vals)
e,k=s.symbols('e k')
q=s.Matrix([[-1-e,1,e],[1,-2+k,1-k],[k,1-e,-1+e-k]])
w=s.Matrix([[1-e+2*k-k*k,1+k-e*e,1-k+2*e-e*k]])
Z=3+e+2*k-e*e-e*k-k*k
assert s.expand(sum(w)-Z)==0
assert (w*q).applyfunc(s.expand)==s.zeros(1,3)
assert s.expand(3*w[2]-Z-(e-k)*(5+e-k))==0
```

All assertions passed in Python 3.9.12 / SymPy 1.14.0. The strict cone table constants agree with the separately executed, new shifted-polynomial/rational-interval computation recorded in [manuscript-math-independent-checks.json](../outputs/manuscript-math-independent-checks.json). These checks support the arithmetic; universal support exhaustion, continuity, and divergent limits rest on the conventional arguments above. No formal-verification status or originality certification is supplied by this review.
