# Markov thermodynamic identifiability

An agentic scientific research workspace for investigating whether complete, infinite-statistics waiting-time distributions between selected observable transitions determine the steady-state entropy-production rate of a finite-state continuous-time Markov network. The investigation begins with small networks, initially targeting $N \le 6$. See [PROJECT.md](PROJECT.md) for the human-owned objective.

Claims in progress are provisional until supported by recorded evidence, with limitations stated. [STATE.md](STATE.md) holds the latest checkpoint; its status is not a live process indicator.

The [research report](outputs/REPORT.md) gives an exact four-state classification for one observed pair and constructive five-state results, including unbounded parameter regions, exceptional-pole analysis and locally isolated generators with distant divergent alternatives. The next question is exact global feasibility for one unresolved five-state kernel. Publication novelty remains unestablished. See [analysis/README.md](analysis/README.md) to reproduce the checks.

## Start or resume

Open this repository in a capable research agent and send:

> Read AGENTS.md, PROJECT.md, and STATE.md. Start or resume the research defined in PROJECT.md, following the operating rules and saved handoff. Preserve the human brief, record evidence and reproducible analyses, and checkpoint STATE.md before stopping.

Follow the saved handoff and verify existing work before repeating it. The files preserve continuity across interruptions; they do not run an agent or schedule work. The workspace itself needs no packages; numerical checks use the dependencies listed in [analysis/requirements.txt](analysis/requirements.txt).

## Files and ownership

| Location | Owner | Purpose |
| --- | --- | --- |
| [PROJECT.md](PROJECT.md) | Human | Compact research objective; preserve it during research. |
| [AGENTS.md](AGENTS.md) | Framework maintainer | General operating rules, evidence conventions, autonomy, and stopping rules. |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Framework maintainer | The adaptive research loop and persistence model. |
| [STATE.md](STATE.md) | Agent | Current understanding, uncertainty, success criteria, and next action. |
| [evidence/RECORDS.md](evidence/RECORDS.md) | Agent | Stable evidence and decision records with source provenance. |
| [analysis/](analysis/README.md) | Agent | Reproducible calculations, scripts, symbolic work, and derived artifacts. |
| [outputs/REPORT.md](outputs/REPORT.md) | Agent | Evidence-backed synthesis, exact findings, limitations, and next question. |

Add `inputs/` for supplied material and `evidence/sources/` for permitted source copies only when needed. Preserve supplied originals. Keep detailed findings in records and artifacts, linked from state and report; add computational infrastructure when actual analysis requires it.

## Framework provenance

Adapted from the blank [cct1123/agentic-research-template](https://github.com/cct1123/agentic-research-template/tree/c1e6088fbed34f9965993317cad914eed2bc1371) at commit `c1e6088fbed34f9965993317cad914eed2bc1371`, inspected on 2026-09-10 UTC. Its general operating rules, ownership model, evidence conventions, and persistence model are retained. Setup performed no scientific investigation and selected no computational stack.
