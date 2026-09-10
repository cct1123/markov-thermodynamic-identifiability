# Reproducible analysis

No analyses have been performed. This directory reserves a place for calculations, symbolic derivations, scripts, models, and derived data when the investigation requires them. No language, dependency set, solver, or package structure has been selected.

For each consequential analysis, keep a short note alongside the artifact documenting:

- The question, definitions, assumptions, units, and method.
- Input provenance and selection rules; dataset versions or checksums when needed. Preserve supplied originals separately from transformations.
- Required runtime and dependency versions, and the exact run command relative to the repository root. For a transparent hand calculation or symbolic derivation, preserve enough steps and definitions to check it.
- Parameters, random seeds for stochastic work, numerical precision or tolerances where relevant, and result/output paths.
- What was actually executed and checked, meaningful validation or sensitivity checks, and any failures, incomplete runs, or unverified outputs.

Link conclusion-relevant results to stable records in [evidence/RECORDS.md](../evidence/RECORDS.md) and summarize their implications in [STATE.md](../STATE.md). Do not label an unexecuted calculation as verified. Add environment files, subdirectories, and other infrastructure only when actual analysis needs them; retain the inputs and outputs necessary to reproduce important claims.
