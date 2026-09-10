# Optional formal verification

**Status at infrastructure setup, 2026-09-10: scaffold only; not compiled.** Neither `lean` nor `lake` was found on the Windows PATH. No toolchain, Mathlib checkout, cache, or generated dependency manifest was installed. TOML parsing, the two version pins, module presence, and a source scan for proof placeholders/custom axioms passed static checks. The smoke theorem is a generic example, not a project result.

Use this layer when a consequential claim has a precise statement, reproducible support or a conventional proof, serious counterexample attempts, and enough stability to justify formalization. Keep informal candidates in the existing evidence record; add definitions and proved lemmas under `ResearchFormal/` when ready, and import every checked module from `ResearchFormal.lean`. A proof sketch is not formally verified.

## Install and check

Lean and Mathlib are isolated from ordinary Python work. Follow the official [Lean installation guide](https://lean-lang.org/install/) (Windows: VS Code and the Lean 4 extension's setup guide; Linux/WSL or command-line users: [manual installation](https://lean-lang.org/install/manual/)). Git and curl must be available. Open this `formal/` directory as the Lean project. Elan selects the version in `lean-toolchain`.

The pair is pinned to Lean **v4.33.0** and the Mathlib **v4.33.0** [release commit `db584cd6d46c92f209a44c0f1c829460d327499d`](https://github.com/leanprover-community/mathlib4/commit/db584cd6d46c92f209a44c0f1c829460d327499d), linked from the [Mathlib release page](https://github.com/leanprover-community/mathlib4/releases/tag/v4.33.0). Its [release toolchain file](https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.33.0/lean-toolchain) was directly read and contains `leanprover/lean4:v4.33.0`. [Lean's release](https://github.com/leanprover/lean4/releases/tag/v4.33.0) and [Lake's matching TOML dependency syntax](https://raw.githubusercontent.com/leanprover/lean4/v4.33.0/src/lake/README.md) were also inspected. Sources retrieved 2026-09-10.

From the repository root, after installing Elan, run the following in PowerShell or a Linux/WSL shell. Stop on any failed command; initial setup downloads a Lean toolchain and a substantial Mathlib cache.

```text
cd formal
lake update
lake exe cache get
lake build
lake env lean ResearchFormal/Smoke.lean
lean --version
git -C .lake/packages/mathlib rev-parse HEAD
```

`lake update` resolves the release pin and writes `lake-manifest.json`. Retain that generated file alongside the first checked proof, plus the actual Mathlib commit and build log; do not hand-invent a manifest. Subsequent verification uses `lake build` without updating dependencies. When changing versions, update both pins together, regenerate the manifest, and recheck every formal module. The [Mathlib project instructions](https://leanprover-community.github.io/install/project.html) describe the cache command; skipping it can trigger a lengthy source build. Native Windows and WSL have separate toolchains/caches: run all commands in the same environment.

## What counts as verification

A successful check applies to the **actual formal statement and its assumptions**. Read those against the intended mathematics. For each theorem, include `#print axioms Namespace.theorem_name` and preserve the output. Accept only dependencies within the standard logical axioms `propext`, `Classical.choice`, and `Quot.sound` (a subset, or none, is fine); reject `sorryAx`, new custom axioms, and native-evaluation axioms for this baseline. The example declares no custom axioms and uses neither `sorry` nor native evaluation. It remains **unverified until compiled**.

Check for errors and warnings, not just an exit status: Lean can accept incomplete proofs via `sorry`. Printing axioms also exposes such dependencies imported indirectly. Native evaluation and downloaded compiled libraries expand the trust boundary; publication-critical work can rebuild dependencies and consider the external checking routes in Lean's [proof-validation documentation](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) (read 2026-09-10). No compilation establishes that a formalization models the physical problem correctly, that a theorem is novel, or that a floating-point experiment is exact.

Promote a claim to **formally verified** only after a successful build, statement review, and axiom audit, with theorem name, source, pinned environment, command, and log linked from its existing evidence record. An SMT/CAS answer has a different trust basis; see [optional tools](../docs/optional-tools.md).
