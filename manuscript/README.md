# Exact entropy-production fibers and local upper bounds

This is a complete research-article draft for **expert human review**, prepared in a readable one-column Physical Review E / REVTeX style. Essential proofs are incorporated in the main PDF as Appendices A–F. The manuscript states the full balanced five-state entropy-fiber theorem and the sharp fixed-count local upper-ceiling criterion; it does not claim a general five/six-state classification or literature-wide priority.

- [Compiled manuscript](main.pdf)
- [LaTeX source](main.tex) and [bibliography](references.bib)
- [Proof appendices](supplementary/proofs.tex)
- [Publication-readiness assessment](../outputs/PUBLICATION-READINESS.md)
- [Audit and claim-to-evidence map](../analysis/manuscript-audit.md)

Author names and affiliations remain explicitly unfilled. The draft discloses substantive Codex assistance and pending expert human verification. Human authors must finalize authorship, funding, disclosure, scientific approval, and the actual data/code-access arrangement before submitting. Nothing has been submitted, committed, or pushed in this manuscript task.

## Build the paper

Use a TeX distribution containing `revtex4-2`, AMS packages, `graphicx`, `booktabs`, `hyperref`, and BibTeX. Run from the repository root:

```text
python manuscript/scripts/build.py
```

The script selects Tectonic on PATH, otherwise pdfLaTeX and BibTeX. With a specified Tectonic binary:

```text
python manuscript/scripts/build.py --tectonic /path/to/tectonic
```

The verified build uses Tectonic 0.17.0 and its official v33 resource bundle, containing REVTeX 4.2e, LaTeX 2021-11-15 and BibTeX 0.99d. The source also follows the currently documented REVTeX 4.2 interface; no claim is made that the bundled 4.2e is the latest release. Tectonic retrieves standard TeX resources on the first build. Add `--offline` after they are cached. The resource URL is explicit because the environment's default-bundle discovery initially failed. A conventional build from `manuscript/` is:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The build driver halts on failed compilation, undefined references/citations or overfull boxes and writes [build provenance](supplementary/build-report.json). It fixes the PDF source epoch; identical output bytes across different TeX distributions are not promised. The saved `.bbl` is included for editorial portability. Compiler binaries and downloaded TeX caches are excluded from the archive.

## Reproduce the science and figures

Extract the complete `outputs/manuscript-package.zip`, preserving its root-relative directory structure. Copying only `manuscript/` is sufficient to compile its existing figures but **not** to rerun the scientific checks, which deliberately reuse preserved `analysis/` scripts and proof artifacts.

Create an environment and install [research requirements](../analysis/requirements-research.txt), using that environment's Python. Tested versions: Python 3.9.12, NumPy 2.0.1, SciPy 1.13.1, SymPy 1.14.0, mpmath 1.3.0, Matplotlib 3.9.4. The complete Windows lock is [here](../analysis/requirements-lock-py39-windows.txt). From the extracted root:

```text
python -B manuscript/scripts/reproduce.py
python -B manuscript/scripts/check_table_bounds.py
python -B analysis/manuscript-math-independent-check.py
```

On the original Windows workspace these commands used `.venv/Scripts/python.exe`. Do not use Python `-O`: assertions are part of the checks. The full driver replays 15 historical scientific scripts with their output writes intercepted, compares scientific payloads, verifies preservation of 22 existing JSON files, reconstructs the endpoint independently in cone coordinates, and computes the two publication figures. One legacy replay includes five linear-programming diagnostics; those diagnostics do not establish the nonexistence theorem. The final conventional proofs and exact certificates have no optimizer-dependent exclusion step. More details are in [scripts/README.md](scripts/README.md).

[Computational results](supplementary/computational-results.json), [table bounds](supplementary/table-bound-checks.json), and [independent mathematical checks](../outputs/manuscript-math-independent-checks.json) retain input rules, versions, hashes, precision, tolerances and outputs. The high-precision figures illustrate analytic limits; they are not numerical proofs of unboundedness. No Lean/formal-verification claim is made.

The paper has two reproducible publication figures, available as vector PDF and SVG. PNG exports in the workspace are conveniences and are omitted from the archive. Educational knowledge-map graphics and generic capability examples remain separate from publication figures.

## Rebuild the archival package

After the final scientific and PDF checks, run:

```text
python -B manuscript/scripts/package.py
```

This produces `outputs/manuscript-package.zip`, including the surrounding research dependencies, scientific provenance, draft and compiled PDF. `PACKAGE-MANIFEST.json` inside the archive lists every payload's SHA-256. The script tests ZIP integrity and verifies every archived hash. `--list` previews contents. It excludes environments, credentials/prompt history, Git metadata, compiler/cache files and temporary page renders. It performs no upload or Git operation.

A [fresh-extraction replay](supplementary/archive-replay-checks.json) passed all scientific checks and reproduced a byte-identical PDF using the same installed Python environment and cached Tectonic resources. This verifies root-relative dependency packaging; it is not a test on a separately provisioned operating system.

The final [readiness report](../outputs/PUBLICATION-READINESS.md) distinguishes verified results from residual originality and expert-proof-review risk. The inaccessible-original caveats in the [citation audit](../analysis/manuscript-literature-review.md) remain visible; bibliography verification is not an exhaustive novelty certificate.
