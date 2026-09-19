# Full revised workflow

The root command `python -B reproduce_all.py` includes the original workflow below plus global-envelope, two-point inverse, complete-support mechanism, graph, rare-rate and unfolding checks; conditioning, 900 seeded trajectories, six figures and 41 tests. Add `--build --tectonic /path/to/tectonic --offline` for the manuscript. See [build guide](../README.md), [revision notes](../../REVISION_NOTES.md), the [last full workflow](../../outputs/correctness-2026-09-15/reproduction.json), and the [latest bounded review verification](../../outputs/supplied-verification-2026-09-19/verification.json). The latter runs all 41 tests and the 15-script driver without repeating the unchanged 900-trajectory campaign. The historical descriptions below retain their original scope.

# Computational reproduction

Run from the repository root, with assertions enabled:

```powershell
.\.venv\Scripts\python.exe -B manuscript/scripts/reproduce.py
```

Python 3.9 or later is required. The tested dependency pins are in
`analysis/requirements-research.txt`; the complete accepted Windows environment
is in `analysis/requirements-lock-py39-windows.txt`. Linux and macOS may use their
equivalent Python executable. No external dataset, stochastic input, graph
enumeration, network request, or formal prover is used by this driver. One
historical construction checker also replays deterministic linear-programming
diagnostics; these do not replace its exact certificates or prove exclusions.

The driver executes 15 deterministic historical scientific scripts and intercepts
their `Path.write_text` calls. Their complete new JSON results are nested in
`manuscript/supplementary/computational-results.json`; historical scientific JSON
files are hash-checked before and after the run and remain unchanged. The package
also includes an exact cone-to-path reconstruction from the endpoint audit and
an independently coded symbolic check of the three-state fixed-trace family.
Both use SymPy, so agreement does not supply an independent arithmetic engine.

Every replay must also agree with its historical scientific payload. Only the
driver's explicit provenance fields are excluded; scientific values and diagnostics
are compared exactly, with no blanket floating-point tolerance. Any mismatch
raises `RuntimeError` with its script and changed paths before figures or a new
success receipt are written. The regression tests exercise this failure through
the real standalone driver and separately accept a provenance-only change.

The endpoint checks use exact number-field arithmetic, rational root isolation,
explicit signs in the selected real embedding, and rational logarithm-series
bounds. Ten exact marked derivative matrices certify all-time equality under the
five-state cap. Finite time-grid diagnostics and high-precision evaluations are
additional checks, not the exact equality proof or a global support exhaustion.
The universal classification and limits rely on the manuscript's conventional
proofs; these computations are not formal verification.

The 100 plotted three-state points use 100-decimal-digit direct stationary solves
and independently evaluated edge-flux entropy. The inputs are the saved decimal
values of a logarithmic grid from 0.003 to 0.3; each reverse rate is computed as
the positive arbitrary-precision value `exp(-1/epsilon**2)`. Reverse rates are
never clipped, regularized, or converted to machine floats. The formula residual
must be below `1e-90 * max(1, abs(entropy))`. Numerical values illustrate the
proved limiting argument and do not prove it.

The driver writes two publication figures in vector PDF/SVG and 300-dpi PNG:

- `manuscript/figures/balanced-fiber.pdf`: actual supports of the two exactly
  certified endpoint generators, rounded independently recomputed entropy
  values, and the three qualitative regimes of the balanced-ray theorem. The
  regime boxes are a classification table, not a continuous entropy curve or
  parameter-scale plot. Bidirectional arrows indicate reciprocal support, not
  equal forward/reverse rates. The observed pair is red. All other edges are
  hidden. The displayed hidden labels agree with the exact coefficient matrices.
- `manuscript/figures/three-state-instability.pdf`: the fixed-trace sequence with
  `kappa=exp(-1/epsilon**2)`, entropy and its asymptote, exact maximum-entry
  generator error, and the proved upper bound `2*(epsilon+kappa)` on maximum
  joint-kernel row total variation. The TV line is an upper bound, not a measured
  distance. The horizontal axis decreases toward the right. Rates use the fixed
  time units in which both observed rates equal one; entropy uses natural logs
  and Boltzmann's constant one, and total variation is dimensionless.

To redraw figures from an already checked numerical manifest without replaying
the scientific calculations:

```powershell
.\.venv\Scripts\python.exe -B manuscript/scripts/reproduce.py --figures-only
```

The full run is required to refresh source and figure provenance. Figure-only
mode does not claim a new scientific replay. The manifest retains every fresh
result, source/output hash, package version, assertion outcome, and difference
from historical scientific payloads after excluding run metadata. Discovery
probes and capability examples are inventoried separately and not promoted into
the manuscript's proof evidence.

The stricter whole-interval bounds printed in the appendix table have a separate
exact replay using the shifted variable `z=21/2+xi`:

```powershell
.\.venv\Scripts\python.exe -B manuscript/scripts/check_table_bounds.py
```

It saves `manuscript/supplementary/table-bound-checks.json` and leaves the accepted
unshifted historical output unchanged. After the final manuscript build and all
checks, create a portable archive of the manuscript and its research dependencies:

```powershell
.\.venv\Scripts\python.exe -B manuscript/scripts/package.py
```

Use `--list` first to inspect its exact contents without writing. The archive at
`outputs/manuscript-package.zip` includes a SHA-256 manifest and preserves the
repository-relative paths required by the reproduction driver. It excludes Git
metadata, runtime environments, prompt history, compiler binaries, caches,
temporary files, manuscript QA images, and duplicate publication PNG exports.
