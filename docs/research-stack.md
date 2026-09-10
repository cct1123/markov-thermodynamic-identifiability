# Scientific computation guide

This stack supports research without prescribing a method or conclusion. Use hand derivation or the standard package directly when that is sufficient. Only CTMC validation, small observation-orbit enumeration, and provenance have shared helpers. Existing scientific scripts and their recorded outputs retain their historical implementation and pins.

## Start with ordinary Python

From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r analysis/requirements-research.txt
.\.venv\Scripts\python.exe -B -m analysis.capabilities.smoke
.\.venv\Scripts\python.exe -B -m unittest analysis.capabilities.test_tools -v
```

If `.venv` already exists, use its interpreter; do not recreate it unnecessarily. Activation is optional. In Linux/macOS use `.venv/bin/python` in place of `.venv\Scripts\python.exe`. New scripts can import `analysis.research_tools` when run from root with `python -m analysis.your_script`; no editable install, package build, notebook server or service is required.

The tested environment is **CPython 3.9.12, Windows x64**, preserving NumPy 2.0.1/SciPy 1.13.1 from accepted runs. The new direct pins are in [requirements-research.txt](../analysis/requirements-research.txt), and the fully resolved tested environment, including optional Z3, is in [requirements-lock-py39-windows.txt](../analysis/requirements-lock-py39-windows.txt). This is a legacy reproduction baseline, not a recommendation to install Python 3.9 on a new machine. For a newer interpreter/platform, resolve compatible versions in a separate environment and rerun the capability checks before changing accepted pins. Cross-version/platform reproducibility has not been tested. The lock records versions, not wheel hashes or a bitwise reproducibility guarantee.

Optional Z3 installation and test:

```powershell
.\.venv\Scripts\python.exe -m pip install -r analysis/requirements-smt.txt
.\.venv\Scripts\python.exe -B -m analysis.capabilities.smoke --require-z3
.\.venv\Scripts\python.exe -m pip check
```

Z3 is installed and checked in this workspace's `.venv` but remains outside core requirements. A normal smoke run skips it when absent; `--require-z3` fails if absent. No Sage, nauty, Lean or Mathlib download occurs in ordinary Python runs. See [optional tools](optional-tools.md) and [formal setup](../formal/README.md).

At setup this host set `PIP_NO_INDEX=1`; network installation required setting `$env:PIP_NO_INDEX='0'` **for the installation process** and authorized network access. Its unactivated Conda interpreter also needed `C:\ProgramData\Miniconda3\Library\bin` on that process's PATH for SSL DLL loading. These are machine-specific bootstrap fixes, not repository-wide environment settings. Use an activated Conda prompt if recreating with this interpreter, keep TLS verification enabled, and do not modify the base environment. The existing `.venv` passes checks without these PATH changes. Initial offline/proxy/SSL installation attempts failed; the subsequent authorized PyPI installation succeeded.

## Choose a layer

| Capability | Available route | Meaning and limit |
| --- | --- | --- |
| Arrays, linear systems, spectra, exponentials | NumPy; `scipy.linalg.solve`, `eig`, `schur`, `expm` | Floating-point diagnostics; inspect conditioning, residuals and multiplicities |
| CTMC generators, stationary distributions, currents, entropy | [ctmc.py](../analysis/research_tools/ctmc.py) | Row convention, validated support and residuals; no silent rate clipping |
| Arbitrary precision | mpmath; `stationary_mp` from exact rationals | Repeat at higher `dps`; more digits alone are not rigorous error bounds |
| Exact arithmetic and matrices | `fractions.Fraction`; SymPy `Rational`, `Matrix`, `stationary_exact` | No floats; generic parameter solutions require exceptional-stratum analysis |
| Determinants, characteristic polynomials, eigenvalues | SymPy matrix methods | Algebraic roots/`RootOf` can remain exact; repeated roots need case handling |
| Polynomial systems and elimination | SymPy `solve`, `solveset`, `factor`, `resultant`, `groebner(..., order='lex')` | Choose domains and variable order; elimination alone does not certify positive real lifting |
| Rational functions and transfer matrices | SymPy `cancel`, `together`; `R*(s*I-T).inv()*B` | Keep denominator exclusions; linear realization equivalence need not preserve positivity |
| Limits, asymptotics, Laplace transforms | SymPy `limit`, `series`, `laplace_transform`; SciPy `quad` / mpmath `quad` | Retain convergence domains and limit paths; numerical inversion/quadrature is approximate |
| Graph supports and invariants | NetworkX; [graphs.py](../analysis/research_tools/graphs.py) | Atlas exhausts simple undirected supports through 7 vertices; cycle basis/rank and bidirected conversion are direct APIs |
| Observation subsets and symmetry | `observation_subsets(g,k)` / `quotient=False`; `GraphMatcher` | Reverse-closed edge observations only; quotient only interchangeable labels and rates |
| Random search and parameter sweeps | `numpy.random.default_rng(seed)`, log sampling, loops/arrays | Sampling measure, support, rate bounds and stopping budget must be explicit |
| Nonlinear/constrained optimization and local refinement | SciPy `differential_evolution`, `minimize`, `NonlinearConstraint`, `linprog` | Feasible candidates and optimizer status are distinct; no exact existence/uniqueness certificate |
| Exact real constraints / quantified claims | Optional Z3; Sage/QEPCAD when justified | Audited encoding, named trusted solver; preserve `unknown` and resource limits |
| Diagnostic plots / tabular results | matplotlib; JSON and standard-library CSV | pandas is optional only if real data wrangling warrants it; no current need |
| Theorem/conjecture management | Existing evidence records plus [claim fields](research-workflow.md#claim-status-and-promotion) | No duplicate registry or automatic promotion |
| Formal proof checking | Optional pinned Lean/Mathlib project | Scaffold uncompiled; status requires actual checking and axiom review |

## Numerical and exact examples

Executable, generic examples are in [smoke.py](../analysis/capabilities/smoke.py) and the [adversarial demo](../analysis/capabilities/counterexample_demo.py). They cover stationary laws, a transfer resolvent versus numerical Laplace quadrature, exact Laplace/limit/series calculations, eigenvalues, factorization, a resultant and a lexicographic Gröbner elimination, scalar real inequalities, graph invariants and a plotted parameter sweep. These are capability tests, not research findings.

```python
import sympy as sp
from analysis.research_tools.ctmc import stationary, stationary_exact, stationary_mp

q = sp.Matrix([[-2, 2], [3, -3]])
pi, diagnostics = stationary(q)
exact_pi = stationary_exact(q)
ctx, high_pi, high_diagnostics = stationary_mp(q, dps=100)
# Use ctx.mpf("...") and ctx.log(...) for further high-precision arithmetic.
```

Use exact strings such as `sp.Rational("0.1")`, `sp.Rational(1,10)` or `Fraction(1,10)`. `Rational(0.1)` records the binary float, not the intended decimal. `nsimplify` and rational reconstruction generate candidates; substitute them into the original exact equations and check inequalities/denominators before assigning any stronger status. `stationary_exact` rejects float-containing matrices; symbolic nullspaces give generic formulas and do not independently certify positivity or all parameter strata.

For arbitrary-precision entropy, construct every rate from the original rationals in the returned `ctx`, form `f=pi[i]*q[i,j]`, `r=pi[j]*q[j,i]`, then sum `(f-r)*(ctx.log(f)-ctx.log(r))` over unordered supported pairs, with the same zero/one-way conventions as the float helper. Recompute from original inputs at multiple precisions; do not convert an already rounded float answer to a long decimal. mpmath is not interval certification. If a claim depends on a sign or exact zero, seek an exact identity, analytic bound or certified enclosure.

SymPy's `charpoly` can create a fresh polynomial generator whose assumptions differ from an existing symbol: compare coefficients or use the returned generator. Symbolic Boolean expressions can be mathematically equal without identical expression trees; compare sets/equivalent formulas where justified. Neither string comparison nor a floating spot check replaces exact domain-aware validation.

## Finite network exploration

```python
import networkx as nx
from analysis.research_tools.graphs import connected_supports, observation_subsets

for g in connected_supports(4):
    cycle_rank = g.number_of_edges() - len(g) + nx.number_connected_components(g)
    cycles = nx.cycle_basis(g)
    arcs = g.to_directed()  # assign independent positive rates to each arc
    for marks in observation_subsets(g, 1):
        pass  # formulate the scientific test before iterating over parameters
```

Support enumeration is exhaustive; continuous rates are not enumerated by this loop. Define any finite rate grid separately and record its Cartesian product/domain, rational values, observation policy, graph IDs and completion counts. Avoid a default combinatorial explosion. Enumerate tiny instances or a scientific subclass first. Automorphism orbits may discard meaningful cases when state labels, mark identities, rates, or colors are fixed; disable quotienting in that situation. For one-way observations generate directed arc subsets explicitly with `itertools.combinations` and preserve their meaning.

Graph6 records adjacency order, not necessarily a canonical label. Graph hashes are filters, not isomorphism certificates. Use NetworkX isomorphism for small sets; canonical labeling and larger enumeration have an optional [nauty/Sage route](optional-tools.md#small-graphs-and-nautytraces). The capability checks compare n=4 atlas classes against independently generated labelled supports; both comparisons still trust NetworkX isomorphism. No claim is made that all weighted/marked networks have been exhausted.

## Reproduce an experiment

Keep a small executable script, exact run command from root, input/topology/mark definitions, parameters, units, seed and RNG, rate bounds or sampling measure, optimizer settings and outcomes, constraints and residuals, tolerances, precision, and outputs. Use [provenance.py](../analysis/research_tools/provenance.py) for source/input SHA-256, dependency versions, timestamp, platform and Git state; explicitly pass all local helpers and input files. It does not decide which inputs matter or promote a computation into evidence. Add unlisted optional package/backend versions explicitly to settings.

For a consequential result, retain the resolved environment (`python -m pip freeze`) and script hashes, including a dirty working tree's actual files. A Git commit alone does not identify uncommitted code. Archive original outputs before changing a script that would overwrite them. The new capability scripts write only under `analysis/capabilities/results/` by default; use `--output-dir` / `--output` to separate replays. Reproducibility can mean agreement within a stated tolerance, not bitwise-identical optimizer trajectories across BLAS/platforms.

The shared manifest records explicit settings plus available invocation arguments; on Python 3.9, `sys.orig_argv` is unavailable, so it reconstructs a replayable module invocation from `__main__.__spec__` and labels the omission of original interpreter flags. Unit-test logs are separately retained. Do not record credentials or environment-variable dumps. Scratch calculations need no permanent manifest unless they affect a consequential claim.

## Package references

Primary documentation inspected on 2026-09-10: [SciPy 1.13.1 differential evolution](https://docs.scipy.org/doc/scipy-1.13.1/reference/generated/scipy.optimize.differential_evolution.html), [SymPy polynomial reference](https://docs.sympy.org/latest/modules/polys/reference.html), [NetworkX graph atlas](https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html), and [mpmath precision contexts](https://mpmath.org/doc/current/basics.html). The SciPy pin accepts `seed=rng`; newer releases use `rng`, so copy examples against the installed version. Optional-tool and Lean references are in their linked guides. The capability [audit and validation record](capability-audit.md) states what actually ran.
