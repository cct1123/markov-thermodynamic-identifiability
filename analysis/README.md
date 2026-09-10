# Reproducible analysis

The investigation uses exact hand derivations and one small deterministic verification script. It does not enumerate graphs or build an inference framework.

| Artifact | Purpose |
| --- | --- |
| [formulation.md](formulation.md) | Model, data, admissible classes, entropy image, finite exact kernel certificate |
| [small-network-audit.md](small-network-audit.md) | At-most-three-state recovery; lumpable and minimal four-state counterexamples |
| [compatibility-orbit.md](compatibility-orbit.md) | Minimal hidden-similarity parameterization; full-positive fixed-diamond classification |
| [check_small_networks.py](check_small_networks.py) | Exact rational identities plus independent numerical checks |
| [small-network-checks.json](small-network-checks.json) | Executed outputs, versions, timestamp and script checksum |
| [requirements.txt](requirements.txt) | Versions used for numerical cross-checks |

## Reproduce

From the repository root, using Python with the listed dependencies:

~~~powershell
python analysis/check_small_networks.py
~~~

The accepted run used Python 3.9.12, NumPy 2.0.1 and SciPy 1.13.1 on Windows. The script overwrites only its generated JSON result.

All input matrices and rational parameter choices are embedded in the script and motivated in the derivation notes. No external dataset or randomness is used. Rates have inverse-time units; entropy has inverse-time units with Boltzmann constant one.

## What was checked

Fraction arithmetic verifies generator row sums, positive required rates, stationary probabilities, intertwining/similarity, full-rank minimality, and sufficient finite derivative identities for equality at every time. These exact finite identities, with the Cayley–Hamilton argument in the formulation, supply the all-time certificate.

Independent floating-point checks evaluate matrix exponentials at 66 times (zero and a logarithmic grid from 10^-6 through 100), compare closed entropy formulas with stationary edge-flux sums, and verify kernel normalization and stationary event statistics. The script contains its explicit numerical tolerances. A rate perturbation and an incorrectly reconstructed killed diagonal are negative controls. Their kernels must differ.

The exact general factorization and uniqueness proofs in compatibility-orbit.md are analytic deductions; the script checks representative rational inputs, not every rate assignment by enumeration. A finite numerical grid is not treated as proof of functional equality.

The JSON records the script SHA-256. [E020](../evidence/RECORDS.md#e020) preserves the corrected initial arithmetic failure and successful-run provenance.

Consequential results are indexed by [E017–E021](../evidence/RECORDS.md#e017). These checks establish the stated examples and support the derivations; they do not establish literature novelty or a classification of every four-state graph.
