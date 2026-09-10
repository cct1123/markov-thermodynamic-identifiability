# Research capability checks

These are generic smoke/regression tests of infrastructure, **not scientific results**. They neither run the saved next research action nor overwrite historical analysis outputs. No evidence IDs are assigned to them.

Use the repository's `.venv` interpreter; [setup and pinned dependencies](../../docs/research-stack.md). From the root:

```powershell
.\.venv\Scripts\python.exe -B -m analysis.capabilities.smoke --require-z3
.\.venv\Scripts\python.exe -B -m analysis.capabilities.counterexample_demo
.\.venv\Scripts\python.exe -B -m unittest analysis.capabilities.test_tools -v
.\.venv\Scripts\python.exe -m pip check
```

Omit `--require-z3` for the core environment; the optional constraint check then reports a skip if Z3 is absent. Linux/macOS use `.venv/bin/python`. Tests intentionally use Python assertions: do not run them with `-O`/`PYTHONOPTIMIZE`. They fail on unexpected results; an optimizer's unsuccessful termination is preserved separately from independently checked candidate feasibility.

| Script | Coverage | Output |
| --- | --- | --- |
| [smoke.py](smoke.py) | Numerical/exact/symbolic stationary laws, 50/100-digit recomputation, spectrum, transfer resolvent vs Laplace quadrature, exact algebra/elimination/limits, graph counts/cycles/observation orbits, sweep plot, search, optional Z3 `sat`/`unsat`/`unknown` and linear QE | [results/smoke.json](results/smoke.json), [sweep.png](results/sweep.png), [existence.smt2](results/existence.smt2), [impossible.smt2](results/impossible.smt2) |
| [counterexample_demo.py](counterexample_demo.py) | Falsifies a deliberately false toy inequality by log-uniform random search, DE, constrained SLSQP, high precision and exact rational substitution | [results/counterexample.json](results/counterexample.json) |
| [test_tools.py](test_tools.py) | Guards units/scaling, entropy conventions, support/irreducibility, conditioning, exact-input handling, precision, independent n=4 support generation, observation orbits | [results/unit-tests.txt](results/unit-tests.txt) |

Manifests identify the toy inputs, source hashes, versions, seed, precision, settings and result; the scripts contain all calculations and original rational inputs. The smoke run also hashes its plot and exact SMT query files. A generic rational constraint witness is independently substituted with SymPy. The limited solver's `unknown` is deliberately induced by `rlimit=1`, not interpreted as a theorem. No Lean toolchain was installed or compiled; [formal setup](../../formal/README.md) remains optional.

Default reruns overwrite only capability outputs. Use `--output-dir analysis/capabilities/results/replay` for smoke or `--output analysis/capabilities/results/replay/counterexample.json` for the toy search to retain a comparison run. Remove disposable replay files after comparison; keep accepted output paths small. See [audit](../../docs/capability-audit.md) for executed validation and initial failures, and [research workflow](../../docs/research-workflow.md) for interpreting actual research results.
