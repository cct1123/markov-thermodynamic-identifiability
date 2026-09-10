# Markov thermodynamic identifiability

An agentic scientific research workspace for investigating whether complete, infinite-statistics waiting-time distributions between selected observable transitions determine the steady-state entropy-production rate of a finite-state continuous-time Markov network. The investigation begins with small networks, initially targeting $N \le 6$. See [PROJECT.md](PROJECT.md) for the human-owned objective.

Claims in progress are provisional until supported by recorded evidence, with limitations stated. [STATE.md](STATE.md) holds the latest checkpoint; its status is not a live process indicator.

The [research report](outputs/REPORT.md) gives an exact four-state classification and now classifies the entire balanced theta(z,z) entropy ray under a five-state cap: unbounded below z_*≈10.5571496686650, exactly two different finite entropy values at z_*, and a unique generator above it. The boundary is the positive root of an explicit quartic; its two-point fiber supplies a minimal-five-state bounded-nonunique example. General five-state classification and publication novelty remain unestablished. See [analysis/README.md](analysis/README.md) for the proofs and reproducible checks.

## Start or resume

Open this repository in a capable research agent and send:

> Read AGENTS.md, PROJECT.md, and STATE.md. Start or resume the research defined in PROJECT.md, following the operating rules and saved handoff. Preserve the human brief, record evidence and reproducible analyses, and checkpoint STATE.md before stopping.

Follow the saved handoff and verify existing work before repeating it. The files preserve continuity across interruptions; they do not run an agent or schedule work. Reading the workspace needs no packages; historical numerical checks use [analysis/requirements.txt](analysis/requirements.txt). New numerical, symbolic, graph and adversarial work uses the [scientific stack guide](docs/research-stack.md), with an isolated environment and [capability checks](analysis/capabilities/README.md). The [workflow](docs/research-workflow.md) distinguishes numerical evidence, exact results, solver certification and formal proof. Optional heavyweight tools remain separate.

## Files and ownership

| Location | Owner | Purpose |
| --- | --- | --- |
| [PROJECT.md](PROJECT.md) | Human | Compact research objective; preserve it during research. |
| [AGENTS.md](AGENTS.md) | Framework maintainer | General operating rules, evidence conventions, autonomy, and stopping rules. |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Framework maintainer | The adaptive research loop and persistence model. |
| [STATE.md](STATE.md) | Agent | Current understanding, uncertainty, success criteria, and next action. |
| [evidence/RECORDS.md](evidence/RECORDS.md) | Agent | Stable evidence and decision records with source provenance. |
| [analysis/](analysis/README.md) | Agent | Reproducible calculations, scripts, symbolic work, and derived artifacts. |
| [docs/](docs/research-stack.md) | Framework maintainer | Computation guide, proof/falsification rules, optional tools and capability audit. |
| [formal/](formal/README.md) | Agent / framework maintainer | Optional pinned Lean/Mathlib project; scaffold not yet compiled. |
| [outputs/REPORT.md](outputs/REPORT.md) | Agent | Evidence-backed synthesis, exact findings, limitations, and next question. |

Add `inputs/` for supplied material and `evidence/sources/` for permitted source copies only when needed. Preserve supplied originals. Keep detailed findings in records and artifacts, linked from state and report; add computational infrastructure when actual analysis requires it.

## Framework provenance

Adapted from the blank [cct1123/agentic-research-template](https://github.com/cct1123/agentic-research-template/tree/c1e6088fbed34f9965993317cad914eed2bc1371) at commit `c1e6088fbed34f9965993317cad914eed2bc1371`, inspected on 2026-09-10 UTC. Its general operating rules, ownership model, evidence conventions, and persistence model are retained. Setup performed no scientific investigation and selected no computational stack.

The later infrastructure upgrade is documented in the [capability audit](docs/capability-audit.md). It adds a tested research stack without reopening the scientific investigation or changing its evidence.
