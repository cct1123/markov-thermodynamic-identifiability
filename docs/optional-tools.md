# Optional exact, graph, and formal tools

This is a capability guide, not a scientific result. The 2026-09-10 Windows audit found Python at `C:\ProgramData\Miniconda3\python.exe` and no `sage`, `geng`, `lean`, or `lake` on PATH. That does not rule out installations elsewhere. SageMath, nauty/Traces, QEPCAD, and Lean/Mathlib were not installed: the default Python stack covers the current small-network scope, and formalization should follow a mature claim. All external sources below were directly inspected on 2026-09-10; optional installation/build examples were not run.

| Need | Weakest useful route | Escalation trigger |
| --- | --- | --- |
| Exact equations, rational functions, polynomial identities | SymPy over rational/algebraic domains | Sage/Singular for algebraic facilities or performance missing in SymPy |
| Real polynomial existence or a counterexample to a universal claim | Optional Z3, exact coefficients and a supported arithmetic fragment | QEPCAD/CAD when parameter conditions or quantified nonlinear formulas require elimination |
| All small simple supports | NetworkX graph atlas and explicit filtering | nauty `geng` beyond the atlas, for restricted graph classes, or to reproduce enumeration independently |
| Canonical labeling or automorphism groups | NetworkX isomorphism for small collections | nauty/Traces or Sage when scale or canonical forms justify them |
| Stable mathematical proof | Conventional proof and independent checks | [Lean/Mathlib scaffold](../formal/README.md) when formalization pays for itself |

## Exact constraints: a usable path and its limits

First state the field and domain: real, rational, integer, positive, nonnegative, bounded, or unrestricted. Build rational constants from integer ratios or decimal strings, not rounded floats. Transform rational equations to polynomials only with explicit nonzero denominators; multiplying inequalities requires denominator signs or a justified case split. Preserve strict inequalities and support assumptions. A polynomial encoding does not automatically represent logarithms, exponentials, or transcendental entropy expressions.

For `exists x: F(x)=0 and G(x)>0`, encode that conjunction directly. For `forall x: F(x)=0 implies H(x)=0`, search the negation `F(x)=0 and H(x)!=0`, including all original domain assumptions. An added search box changes the theorem's scope. For exact optimization, a feasible value is a lower bound for a maximization problem; certifying an optimum additionally requires excluding every larger value. Distinguish an attained maximum from a supremum or an unbounded family.

### Z3 (optional Python dependency)

Use Z3 for exact rational linear constraints and suitable polynomial real constraints, with `Real` variables, exact constants, and an explicit timeout. For a quantifier-free polynomial real problem, `SolverFor("QF_NRA")` or `Tactic("qfnra-nlsat").solver()` is a useful entry point. Generic nonlinear/mixed theories can return `unknown`. Z3's `qe` tactic is documented for selected theories, including linear arithmetic; it is not a promise of arbitrary nonlinear quantifier elimination. See Microsoft's [arithmetic guide](https://microsoft.github.io/z3guide/docs/theories/Arithmetic/) and [tactics reference: `qe`, `qfnra-nlsat`](https://microsoft.github.io/z3guide/docs/strategies/summary/).

Install [analysis/requirements-smt.txt](../analysis/requirements-smt.txt) into the research environment only when needed. From the repository root on Windows, use `.venv\Scripts\python.exe -m pip install -r analysis/requirements-smt.txt`; on Linux/WSL, use `.venv/bin/python -m pip install -r analysis/requirements-smt.txt`. These explicit interpreter paths avoid accidentally modifying the system/conda base environment.

Minimal Python example after that installation; this is an example for a future run, not a checked output:

```python
import z3

x = z3.Real("x")
s = z3.SolverFor("QF_NRA")
s.set(timeout=5000)
s.add(x*x == 2, x > 0)
print(z3.get_version_string())
print(s.sexpr())                 # Preserve exact encoded query.
answer = s.check()
print(answer)
if answer == z3.sat:
    print(s.model().sexpr())     # Preserve algebraic values, not decimal truncations.
elif answer == z3.unknown:
    print(s.reason_unknown())
```

Record `sat`, `unsat`, and `unknown` separately. `sat` supplies a model for the **encoded** constraints; independently substitute it into the original equations/inequalities when possible. `unsat` rules out that encoding under the solver's trust assumptions, not omitted domains or topologies. `unknown`, timeout, a crash, and absence of a returned model are no mathematical conclusion. Save query, result, version, options, timeout, model or proof output if supported, and the encoding justification. A solver's proof-production feature is not guaranteed for every tactic. Call a definitive trusted-solver decision **solver-certified** with that qualification; do not call it a Lean-checked proof or an independently checked certificate unless an appropriate checker actually ran.

### SageMath and nonlinear quantifier elimination

Sage offers exact polynomial rings, ideals, algebraic numbers, and mature backends. Its [`elimination_ideal` documentation](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/multi_polynomial_ideal.html#sage.rings.polynomial.multi_polynomial_ideal.MPolynomialIdeal.elimination_ideal) specifies Singular as the default backend and notes potentially expensive Gröbner computations. Example in a Sage console:

```python
R = PolynomialRing(QQ, names=("x", "y"), order="lex")
x, y = R.gens()
I = R.ideal([x**2 - y, x - 2])
print(I.groebner_basis())
print(I.elimination_ideal([x]))
```

Elimination equations usually give necessary conditions; they can retain closure points or complex solutions and do not enforce real-domain restrictions by themselves. Check lifting to the original system and retain positivity and denominator exclusions. SymPy/Sage symbolic answers are exact algebraic results only when the domain, transformations, and returned conditions warrant that statement.

For a small quantified polynomial-real problem, Sage's [QEPCAD interface](https://doc.sagemath.org/html/en/reference/interfaces/sage/interfaces/qepcad.html) exposes cylindrical algebraic decomposition and documents quantified equalities and inequalities. QEPCAD is a **separate optional component**, not guaranteed by installing Sage. A future Sage-console check is:

```python
from sage.interfaces.qepcad import qepcad, qepcad_formula
x, a = var("x a")
qf = qepcad_formula
print(qepcad(qf.exists(x, qf.and_(x**2 == a, x > 0))))
```

The mathematically expected condition is `a > 0`; this example has not been run here. Preserve the complete input, variable order, assumptions, output, engine version, and resource limits. CAD can become prohibitively expensive; neither failure nor unresolved quantifiers establishes nonexistence. CAS output needs an independent derivation or checker for stronger certification.

On Windows, Sage's [installation guide, Windows section](https://doc.sagemath.org/html/en/installation/index.html) recommends WSL. In WSL/Linux, install Miniforge/conda as described there, then use an isolated environment:

```sh
conda create -n research-sage -c conda-forge sage python=3.12
conda activate research-sage
sage --version
sage
```

For QEPCAD, the [Sage optional-package page](https://doc.sagemath.org/html/en/reference/spkg/qepcad.html) lists `sudo apt-get install qepcad` on Debian/Ubuntu. Use the distribution's supported method, ensure the executable is visible inside the Sage environment, and run the example before claiming availability. Package/interface integration can vary; a binary present on PATH is not an end-to-end check. Capture the resolved conda environment and backend versions for each consequential run. Do not add Sage to the ordinary Python requirements.

## Small graphs and nauty/Traces

NetworkX's [`graph_atlas_g`](https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html) provides all simple undirected graph isomorphism classes through seven vertices (1253 graphs total). Filtering by order and connectivity covers the stated `N <= 6` simple support scope. Bidirected support is obtained by replacing each undirected edge with both arcs; rates remain separately assigned. This does not enumerate arbitrary directed graphs, multigraphs, weighted models, or marked observations. Quotient observation subsets only by automorphisms preserving all scientifically meaningful colors/marks; a graph6 serialization or a graph hash is not automatically a canonical label.

The [nauty/Traces authors' page](https://users.cecs.anu.edu.au/~bdm/nauty/) documents automorphisms, canonical labeling, and `geng` enumeration, and recommends WSL on Windows. Install only when these add value. In a separate WSL tools directory, download the source release linked there (2.9.3 was listed at this audit), unpack it, then run `./configure` and `make`; retain the source version/checksum and build command. No system-wide installation is necessary. From that build directory:

```sh
./geng -c -l 6 connected6.g6
```

The [nauty 2.9 manual, utility help for `geng`, pp. 102-103](https://users.cecs.anu.edu.au/~bdm/nauty/nug29.pdf) documents connected filtering (`-c`), canonical output (`-l`), and graph6 output. Read the resulting file with `networkx.read_graph6`; compare counts and graph classes with the atlas. This independent backend check was not executed here. Canonical forms depend on the tool, options, and color encoding; preserve those with any stored labels.

## Result labels

Numerical evidence is approximate, including arbitrary precision without certified error bounds. Symbolic evidence comes from explicit exact domains and valid transformations; a printed expression alone is not a proof of the intended statement. Solver-certified results trust a named engine and an audited encoding. Formal proofs require a successful proof check and a reviewed statement/axiom boundary, as specified in [formal/README.md](../formal/README.md). None of these labels follows solely from failure to find a counterexample.
