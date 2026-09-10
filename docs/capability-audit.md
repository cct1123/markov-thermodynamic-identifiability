# Scientific capability upgrade audit

**Scope:** infrastructure only, requested 2026-09-10. No scientific investigation, new scientific evidence record, commit or push. PROJECT.md, STATE.md, scientific derivations, existing Python scripts, recorded scientific JSON and outputs/REPORT.md are preserved. The finished research status is not reopened. Infrastructure continuity is recorded here rather than in the scientific state.

**Status:** complete. **Last checkpoint:** 2026-09-10 22:11:07 UTC. Final artifact verification, dependency check and disposable-cache cleanup completed; no unfinished assignments.

## Gaps and choices

The inspected baseline had strong provenance, Fraction arithmetic, custom small exact-matrix checks, NumPy/SciPy computations and seeded SLSQP probes. It lacked an isolated reproducible research environment, installed SymPy/mpmath/NetworkX, general topology enumeration, a reusable high-precision path, explicit mathematical-status fields and an optional constraint/formal verification path. Arbitrary precision, polynomial elimination, real constraints and rigorous solver-result distinctions were not first-class workflows. The historical code was useful and was not replaced.

| Change | Why it is sufficient |
| --- | --- |
| Additive pinned Python environment and a full Windows/Python 3.9 lock | Retains accepted numerical dependency versions; adds SymPy, mpmath, NetworkX and compatible plotting |
| Three small helper modules plus a package marker | CTMC validation/stationary laws/flux/entropy, atlas and observation orbits, reproducibility manifests; no custom CAS/isomorphism/optimizer framework |
| Generic executable capability examples and nine regression tests | Exercises exact algebra, precision, graph support, adversarial search and numerical failure boundaries |
| Optional Z3 requirement, installed and tested here | Exact rational polynomial constraints, audited model, `sat`/`unsat`/`unknown`, and a linear QE example |
| Optional pinned Lean/Mathlib scaffold | Clean promotion/build/axiom-audit path without forcing formalization or a large download |
| Operating-rule and architecture updates | Explicit falsification, exactification, independent checking, claim status and scope-aware tool choice |

No pandas was added: the current inputs are small structured matrices, graphs and JSON, with no tabular-data workload needing it. SageMath/Singular, QEPCAD and nauty/Traces remain documented options: SymPy and the NetworkX atlas cover initial needs, while heavier algebra/CAD/canonical-labeling tools should follow a specific gap. Lean/Mathlib remain uninstalled because no claim was being promoted to formal proof in this run. No external commercial CAS, plugins, services or new agent hierarchy were introduced. One bounded worker audited optional tools/formal setup and independently reviewed the new helpers; its assignments are complete.

## Executed validation

The accepted capability artifacts are in [analysis/capabilities/results](../analysis/capabilities/README.md). Commands ran from repository root with `.venv\Scripts\python.exe`, CPython 3.9.12 Windows x64:

```powershell
.\.venv\Scripts\python.exe -B -m analysis.capabilities.smoke --require-z3
.\.venv\Scripts\python.exe -B -m analysis.capabilities.counterexample_demo
.\.venv\Scripts\python.exe -B -m unittest analysis.capabilities.test_tools -v
.\.venv\Scripts\python.exe -m pip check
```

- [Smoke manifest](../analysis/capabilities/results/smoke.json): all requested checks passed. The toy stationary law agrees numerically, exactly and at 50/100 digits. Spectral and characteristic-polynomial checks, rational resolvent versus independent Laplace quadrature, factorization, limits/series, symbolic inequalities, resultant and Gröbner elimination passed.
- Graph checks: connected simple-support counts for n=1..6 are 1, 1, 2, 6, 21, 112; n=4 was independently generated from all labelled edge subsets and compared by NetworkX isomorphism. Square cycle rank and two-edge observation orbits passed. This is infrastructure validation, not a project topology classification.
- [Adversarial toy manifest](../analysis/capabilities/results/counterexample.json): seeded log-uniform sampling, differential evolution and constrained SLSQP found numerical candidates for a deliberately false generic inequality; rational substitution checked the reconstructed witness exactly, with an 80-digit cross-check. Optimizer statuses and feasibility are retained separately.
- Z3: saved [satisfiable query](../analysis/capabilities/results/existence.smt2) and [unsatisfiable query](../analysis/capabilities/results/impossible.smt2); rational model independently substituted with SymPy. A resource-limited query returned `unknown` as intended; simple linear quantifier elimination passed. These rely on the trusted solver, not a formally checked proof certificate.
- [Nine regression tests](../analysis/capabilities/results/unit-tests.txt) passed: rate scaling, entropy/zero/one-way conventions, normalization/irreducibility, tiny rates, ill-conditioning and exact fallback, float/complex rejection, conversion underflow, precision context, graph-generation comparison and observation orbits.
- [Sweep plot](../analysis/capabilities/results/sweep.png) rendered headlessly and was visually inspected. `pip check` reported no broken requirements.
- Formal files: static TOML/module/pin checks passed and matching Lean/Mathlib release sources were inspected; **no Lean theorem was compiled or formally verified**. See [formal status](../formal/README.md).

Initial smoke assertions exposed SymPy representation details (characteristic-polynomial generator assumptions and equivalent inequality expression ordering); checks now compare coefficients and solution sets. The deliberately ill-conditioned float test can fail its positivity check, which is an acceptable refusal; it still must warn and the exact/high-precision routes must pass. An independent review found float conversion could erase extremely tiny reverse edges or discard complex rates, and Python 3.9 could lose `-m` in provenance. These were corrected, guarded, and retested. Failed initial attempts are not accepted validation outputs or scientific counterevidence.

## Environment and verification limits

The base environment had NumPy 2.0.1, SciPy 1.13.1, matplotlib 3.7.2 and Python 3.9.12; SymPy, mpmath, NetworkX, Z3 and optional external executables were not found through the inspected environment/PATH. The isolated environment now has the [recorded pins](../analysis/requirements-lock-py39-windows.txt). Setup initially failed because `PIP_NO_INDEX=1`, Conda SSL DLL lookup, then restricted proxy access blocked downloads. Process-local settings and an authorized PyPI installation resolved this; the base environment was not changed. Details are in [setup notes](research-stack.md#start-with-ordinary-python).

The tested lock is platform/interpreter-specific and contains versions rather than wheel hashes. Newer Python or another platform needs fresh resolution and checks. Numerical residuals and arbitrary precision do not provide universal error certification. The graph atlas and observation-orbit helper handle the documented simple, reverse-closed support scope; canonical labeling, directed/weighted exhaustive enumeration, general nonlinear QE and Lean compilation were not tested here. Optional guides clearly label unrun examples. Existing research proofs were not rerun or newly certified by this infrastructure task.

## Final review and handoff

The accepted scientific artifacts remain unchanged; computation capability and proof-status conventions are additive. Source/output manifest hashes passed verification; both recorded commands successfully replayed their module invocation with `--help`. All local link paths in the ten updated/new documentation files resolved; static formal configuration and `git diff --check` passed. Every previously tracked file outside the four intended documentation updates matched HEAD after normalizing checkout line endings. Disposable bytecode from the two new analysis directories was removed. No new scientific claim is asserted. All worker assignments are complete; there is no infrastructure blocker requiring user input.

Recommended next research-loop prompt (a future authorization, not executed here):

> Read AGENTS.md, PROJECT.md, STATE.md and docs/research-stack.md. Resume only the single next research action saved in STATE.md. Review its linked proof and evidence, state the precise unresolved claim and an admissible falsification condition, then choose the cheapest numerical, symbolic or constraint-based action that can change the answer. Independently verify consequential candidates, preserve exact assumptions and failed attempts, and checkpoint evidence/state. Do not infer proof from unsuccessful search, repeat settled work, or broaden the scientific scope without a reason.

## Subsequent publication review, 2026-09-10

The later user instruction, “review prune commit push,” authorizes publishing this upgrade together with the completed boundary research. The infrastructure-only scope above records the original upgrade; it does not prohibit this later publication.

A fresh independent review found that NumPy complex scalars inside lists or object arrays could still lose their imaginary parts at float conversion. For example, `validate_generator([[np.complex128(-1+3j), np.complex128(1-3j)], [np.complex128(1), np.complex128(-1)]])` incorrectly returned a real generator with a `ComplexWarning`; supplied complex stationary probabilities could be similarly accepted. The expanded regression reproduced six failing generator subcases before the fix. Both conversion paths now explicitly reject complex elements. Regression coverage includes Python complex and NumPy complex64/complex128/clongdouble, in lists and object arrays, for both generators and probabilities. All nine test methods and the complete smoke run passed after correction; the accepted smoke manifest and unit-test log were refreshed. The mathematical smoke results are unchanged.

The standalone toy search, optional Z3 checks and `pip check` also passed in an isolated replay. Explicit Git line-ending rules preserve the hashed proof/source and dependency bytes, including the historical CRLF baseline requirements and Windows SMT queries. Historical scientific outputs and failed attempts are retained; disposable replay copies are removed after comparison. This review does not install Lean or promote a claim to formal verification. Scientific review and the publication decision are recorded separately in [E053](../evidence/RECORDS.md#e053) and [D016](../evidence/RECORDS.md#d016).
