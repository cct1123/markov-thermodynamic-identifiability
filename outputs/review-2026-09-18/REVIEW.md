# Repository review — 18 September 2026

The pending manuscript revision and its computational workflow were reviewed for the user's request to fix issues, commit and push. This maintenance review does not reopen the finished scientific investigation or certify publication priority.

## Fixes

- Preserve both baseline directories byte-for-byte through Git. The saved manuscript README contains mixed line endings; Git's previous text conversion changed its hash and would break the baseline audit after checkout. Narrow `.gitattributes` rules now disable conversion for these immutable copies.
- Normalize `analysis/revision/graph_checks.py` to the repository's LF convention before recording its source hash. A staged checkout caught this separate mismatch; the full workflow was rerun after normalization.
- Reject optimized Python execution before work in eight standalone scientific/audit entrypoints. The previous `assert __debug__` guards vanished under `-O`; other entrypoints lacked a guard. Tests exercise both `-O` and `PYTHONOPTIMIZE=1` in isolated copies and require no writes.
- Verify the computational receipt's recorded source and historical-output hashes in the manuscript validator, together with success flags. Previously the validator loaded the manifest without checking it. Regression tests reject changed inputs, failed receipts and inconsistent duplicate hashes.
- Compare the union of fresh and historical output fields in the independent replay. Previously a removed field could silently pass the claimed full-payload comparison. Tests cover missing, added and changed values, preserving only the documented execution-time exception.
- Replace the introduction's ambiguous “cap-free” inverse with “without a rate cap.” Its three-state dimension restriction remains essential and unchanged.

## Verification

The complete [13-job workflow](reproduction.json) passed, including 15 historical script replays, exact proof-support calculations, 900 seeded trajectories, **36 tests**, six figures, offline Tectonic compilation and source/build validation. The [repository audit](../correctness-2026-09-15/repository-audit.json) verifies 23 preserved baseline hashes, 22 accepted historical JSON files, the original six theorem statements and unchanged human-owned brief/instructions. The current PDF has 55 pages, with no overfull boxes or unresolved references/citations.

All 55 before/after pages were rendered with Poppler at a maximum dimension of 1400 pixels and compared pixel-for-pixel. Only page 2 changed; it was visually inspected and has no clipping, overlap or broken text. The other 54 pages match the previously inspected version exactly at that rendering resolution. Hashes and executed checks are recorded in [verification.json](verification.json).

The mathematical review inspected the compactness/tail argument, fixed-count moment confidence proof, two-/three-point reconstruction, global support/equality argument, subcritical construction and local continuation. The computational review inspected inference, continuation, reconstruction and mechanism code. Neither found a substantive scientific error within this bounded review. Both share the supplied premises and local sources; they are not independent formal verification or a new literature audit.

## Reproduction

From the repository root, using the existing pinned environment:

```powershell
.\.venv\Scripts\python.exe -B reproduce_all.py --build --tectonic tmp/tectonic/tectonic.exe --offline
.\.venv\Scripts\python.exe -B analysis/revision/audit_repository.py
.\.venv\Scripts\python.exe -B manuscript/scripts/package.py
```

The compiler and disposable review workspaces remain under ignored `tmp/`. The package is regenerated after the final documentation and receipts. Git checkout preservation and final package integrity are checked separately; those checks do not upgrade any mathematical claim. Commit and push are explicitly authorized by the user; no journal submission is authorized or performed.
