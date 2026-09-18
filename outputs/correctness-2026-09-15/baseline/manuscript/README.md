# Revised manuscript and reproduction

**Thermodynamic identifiability and unstable entropy inference under partial observation**

This is a complete research draft for expert human review in a readable one-column REVTeX format. The main text now prioritizes exact recovery, entropy instability, the sharp local-ceiling criterion, finite-data inference and physical priors. The special five-state construction and its new transverse perturbation follow those results. Essential proofs are included as Appendices A–G.

- [Compiled article](main.pdf), [main source](main.tex), [bibliography](references.bib)
- [Original proofs plus new Appendix G](supplementary/proofs.tex)
- [Revision notes](../REVISION_NOTES.md), [theorem/assumption map](../analysis/revision/AUDIT.md)
- [Source comparison](../analysis/revision/LITERATURE.md), [final referee review](../analysis/revision/FINAL-REFEREE.md)
- [Readiness assessment](../outputs/PUBLICATION-READINESS.md)

There are six publication figures and 31 cited references. No mathematical claim is formally verified. New numerical results are explicitly distinguished from exact certificates and conventional proofs. Author names/affiliations, funding, final disclosure and expert scientific approval remain human responsibilities. This revision performs no submission or upload.

## One-command reproduction

Use a scientific environment with [requirements-research.txt](../analysis/requirements-research.txt). The recorded Windows environment uses Python 3.9.12, NumPy 2.0.1, SciPy 1.13.1, SymPy 1.14.0, mpmath 1.3.0 and Matplotlib 3.9.4. [Full recorded lock](../analysis/requirements-lock-py39-windows.txt). Existing users should reuse the environment; a newer platform needs compatible versions and its own validation rather than assuming bitwise portability.

From the repository root, with assertions enabled:

```text
python -B reproduce_all.py
```

On the original Windows workspace replace `python` with `.venv/Scripts/python.exe`. The command regenerates 15 preserved scientific replays with writes intercepted; exact appendix interval and independent manuscript checks; new rare-rate, graph and local unfolding checks; wider numerical continuation; conditioning grids and 900 seeded CTMC trajectories; 21 tests; and all six figures. It preserves the 22 accepted historical scientific JSON outputs. One old replay includes deterministic linear-programming diagnostics; no optimizer or sampled graph set proves a nonexistence theorem.

The [full run manifest](../outputs/revision/reproduction.json) records commands, times, versions, outputs and hashes. The exact historical [manifest](supplementary/computational-results.json) retains all replay payloads. New experiment details are in [statistics](../analysis/revision/STATISTICS.md), [continuation](../analysis/revision/CONTINUATION.md), [rare-rate proof](../analysis/revision/RARE-EVENT.md), and [graph/priors](../analysis/revision/GRAPH-REGULARIZATION.md).

The inference pipeline observes the microscopic pair only, estimates joint Laplace moments, fits all six unknown rates and computes stationary entropy and sandwich uncertainty. Its positive rate box is an explicit computational restriction. Coverage is pointwise asymptotic and fails badly in the rare-reverse example; boundary/rank failures and a heuristic rare-count warning are exposed, not hidden from denominators.

## Build

Install a TeX distribution with REVTeX and AMS packages, graphicx, booktabs and hyperref. The driver selects Tectonic on PATH or standard pdfLaTeX/BibTeX:

```text
python manuscript/scripts/build.py
python -B reproduce_all.py --build --tectonic /path/to/tectonic --offline
```

The accepted local build uses Tectonic 0.17.0 and its official v33 cached bundle. Omit `--offline` only when resources need to be retrieved. The compiler archive used here was downloaded from the official release and checked against its published SHA-256. Compiler binaries, downloaded caches and temporary page renders are excluded from the package.

The driver halts on undefined references/citations and overfull boxes; [build-report.json](supplementary/build-report.json) records all supplementary source and figure hashes. The PDF uses a fixed source epoch; its metadata creation date is not the scientific revision date. Different distributions may produce different PDF bytes. The saved `.bbl` supports editorial portability.

A conventional build from `manuscript/` is `pdflatex main.tex`, `bibtex main`, then two more `pdflatex main.tex` passes, with halt-on-error and noninteractive flags as appropriate. The final PDF is also rendered with Poppler and visually inspected; successful LaTeX compilation alone does not establish good layout.

## Individual analyses and redraws

```text
python -B analysis/revision/rare_event.py
python -B analysis/revision/graph_checks.py
python -B analysis/revision/continuation.py
python -B -m analysis.revision.inference --replicates 100
python -B -m unittest analysis.capabilities.test_tools analysis.revision.test_inference analysis.revision.test_continuation -v
```

The original certificate figures and both new numerical figure sets can be redrawn from their saved payloads:

```text
python -B manuscript/scripts/reproduce.py --figures-only
python -B analysis/revision/continuation.py --figures-only
python -B -m analysis.revision.inference --figures-only
```

Figure-only mode does not constitute a new scientific replay. The conditioning and finite-data figures have separate redraw provenance; their original scientific payload remains unchanged. The boundary normal form and local sign rectangle are exact proof support; the 41-node wider continuation, numerical ranks and large-parameter entropy values are diagnostics.

## Package and preservation

```text
python -B manuscript/scripts/package.py
```

This writes [outputs/manuscript-package.zip](../outputs/manuscript-package.zip), with root-relative research dependencies and a verified per-file SHA-256 manifest. Extract the complete archive to rerun the science. Copying only `manuscript/` permits compilation with the supplied figures, but omits scientific dependencies. The archival package excludes Git metadata, environments, prompt history, compiler/cache files and page renders.

The [pre-revision baseline](../outputs/revision/baseline/) is historical source context. The [repository audit](../outputs/revision/repository-audit.json) checks original theorem/proof preservation, accepted JSON bytes, source parsing and file inventory; these structural checks do not replace mathematical review. The prior [archive replay](supplementary/archive-replay-checks.json) describes the September 11 package. Current revision verification is separately recorded under `outputs/revision/` and must not be inferred from that old replay.
