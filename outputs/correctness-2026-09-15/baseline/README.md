# Markov thermodynamic identifiability

Exact recovery of partially observed Markov dynamics does not by itself guarantee stable or bounded inference of microscopic entropy production. This repository combines conventional proofs, exact computational certificates, reproducible numerical studies and a revised research manuscript.

## Read the revised paper

**Thermodynamic identifiability and unstable entropy inference under partial observation**

- [Manuscript PDF](manuscript/main.pdf) and [LaTeX/build guide](manuscript/README.md)
- [Revision notes and remaining questions](REVISION_NOTES.md)
- [Theorem, assumption and verification map](analysis/revision/AUDIT.md)
- [Primary literature comparison](analysis/revision/LITERATURE.md): 31 cited references, actual access/version limitations
- [Reproducibility archive](outputs/manuscript-package.zip)
- [Publication-readiness assessment](outputs/PUBLICATION-READINESS.md)

The draft is prepared for **expert human review**. Proof status is conventional, with exact algebraic/interval support and separately labeled numerical experiments; it is not formally verified. Author and submission details remain pending. The [baseline](outputs/revision/baseline/) preserves the earlier article.

## Scientific results

The primary experiment observes a known microscopic reverse transition pair in a finite irreducible CTMC with reciprocal, otherwise unknown support. It retains complete joint next-mark/waiting-time laws and their absolute time scale. The stationary network entropy functional has a physical dissipation interpretation only with appropriate state/channel resolution and local detailed balance.

- **Exact recovery versus conditioning:** three distinct positive Laplace points identify every three-state generator. The absolute-rate inverse remains regular at trees, while relative-rate conditioning and entropy sensitivity can diverge near rare reverse rates.
- **Sharp local ceiling:** with exactly N states and one resolved pair, a finite local entropy upper bound exists precisely for N=2 or a complete N=3 source. Negative cases persist with observed rates and trace fixed. A tighter individual cap or known support can change the admissible class.
- **Finite data:** a constructive six-rate estimator and martingale-sandwich uncertainty calculation are tested on 900 actual CTMC trajectories. Interior examples permit useful inference; a rare-reverse example exposes serious interval failure despite small residuals.
- **Quantitative impossibility:** testing independently variable reverse rates with a fixed multiplicative entropy gap can require an exponentially long observation horizon, even with complete microscopic paths. This is not a theorem for a known one-parameter rate prior.
- **Graph coverage and physical priors:** two Laplace points recover Q when observed reciprocal edges cover every vertex. Microscopic activity plus an affinity ceiling bounds entropy. Neither an upper rate cap alone nor a rate floor plus activity alone suffices.

The preserved exact five-state construction gives the entire entropy fiber under a five-state cap:

| Balanced parameter | Compatible entropy |
| --- | --- |
| 0 < z < z* | Unbounded above |
| z = z* | Exactly two distinct finite values |
| z > z* | Singleton, with a unique physical generator |

A nontrivial exit-asymmetry perturbation now has a proved local critical curve and a separately labeled wider numerical continuation. The transition is a fold of boundary constraints; the full subcritical fiber has a continuum. Allowing a sixth hidden state makes the exact fiber unbounded. Fixed count, state cap and minimal realization restrictions must always be stated.

## Reproduce all essential results

Use the project's isolated scientific Python environment. The tested baseline is Python 3.9.12 on Windows with [pinned dependencies](analysis/requirements-research.txt); this is a reproducibility record, not a recommendation to install an obsolete interpreter on a new machine. From the repository root:

```text
python -B reproduce_all.py
```

This runs the preserved exact certificates and independent checks, new rare-rate/graph/unfolding calculations, conditioning grids, 900 seeded trajectories, 21 tests and all six manuscript figures. It records commands, versions, source hashes and outcomes in [reproduction.json](outputs/revision/reproduction.json). Historical accepted scientific outputs are protected. Numerical continuation, Monte Carlo and exact proof-support calculations have distinct status labels.

To also compile and validate the paper with an installed Tectonic and cached resources:

```text
python -B reproduce_all.py --build --tectonic /path/to/tectonic --offline
```

On the original Windows workspace use `.venv/Scripts/python.exe` in place of `python`. On another platform use that environment's Python; the pinned Windows runtime has not been independently provisioned on every platform. Do not use `-O`, which disables scientific assertions. A standard pdfLaTeX/BibTeX build is also supported. See [manuscript/README.md](manuscript/README.md) for setup, individual analyses, figure-only redraws and packaging.

The [research report](outputs/REPORT.md) gives the current synthesis. Unknown dimensions, arbitrary observation graphs, missed events and optimal rare-event inference remain specific open problems, not solved by this reproduction workflow.

## Explore the research atlas

The [interactive knowledge atlas](knowledge/README.md) connects claims, assumptions, proofs, calculations, counterexamples, and prior work across 12 views. After cloning or extracting the repository, open `knowledge/interactive/index.html` locally; it has no network dependencies. On GitHub, start with the [static overview](knowledge/views/research_overview.svg) or [scientific story](knowledge/views/scientific_story.svg).

The atlas provides navigation and provenance, not additional proof or novelty certification. Its source of truth is the linked evidence and mathematical artifacts.

## Start or resume

The current manuscript task is finished. For a subsequent research or revision task, open this repository in a capable research agent and send:

> Read AGENTS.md, PROJECT.md, and STATE.md. Follow my current task scope and the saved handoff. Preserve the human brief and established evidence, verify relevant existing work before repeating it, and checkpoint any consequential new result. A finished investigation should reopen only for a concrete reason.

[PROJECT.md](PROJECT.md) is the human-owned research objective; [STATE.md](STATE.md) is the current checkpoint, not a live process indicator. These files preserve continuity across interruptions; they do not run an agent or schedule work. The [workflow](docs/research-workflow.md) distinguishes numerical evidence, conventional proof, solver certification, and formal verification.

## Files and ownership

| Location | Owner | Purpose |
| --- | --- | --- |
| [PROJECT.md](PROJECT.md) | Human | Compact research objective; preserve it during research. |
| [AGENTS.md](AGENTS.md) | Framework maintainer | General operating rules, evidence conventions, autonomy, and stopping rules. |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Framework maintainer | The adaptive research loop and persistence model. |
| [STATE.md](STATE.md) | Agent | Current understanding, uncertainty, success criteria, and next action. |
| [evidence/RECORDS.md](evidence/RECORDS.md) | Agent | Stable evidence and decision records with source provenance. |
| [analysis/](analysis/README.md) | Agent | Reproducible calculations, scripts, symbolic work, and derived artifacts. |
| [manuscript/](manuscript/README.md) | Agent draft / human authors | Complete article, proofs, bibliography, figures, and reproduction/build scripts. |
| [knowledge/](knowledge/README.md) | Agent | Interactive and static maps of claims, evidence, assumptions, and open questions. |
| [docs/](docs/research-stack.md) | Framework maintainer | Computation guide, proof/falsification rules, optional tools and capability audit. |
| [formal/](formal/README.md) | Agent / framework maintainer | Optional pinned Lean/Mathlib project; scaffold not yet compiled. |
| [outputs/REPORT.md](outputs/REPORT.md) | Agent | Evidence-backed synthesis, exact findings, limitations, and next question. |

Add `inputs/` for supplied material and `evidence/sources/` for permitted source copies only when needed. Preserve supplied originals. Keep detailed findings in records and artifacts, linked from state and report; add computational infrastructure when actual analysis requires it.

## Framework provenance

Adapted from the blank [cct1123/agentic-research-template](https://github.com/cct1123/agentic-research-template/tree/c1e6088fbed34f9965993317cad914eed2bc1371) at commit `c1e6088fbed34f9965993317cad914eed2bc1371`, inspected on 2026-09-10 UTC. Its general operating rules, ownership model, evidence conventions, and persistence model are retained. Setup performed no scientific investigation and selected no computational stack.

The later infrastructure upgrade is documented in the [capability audit](docs/capability-audit.md). It adds a tested research stack without reopening the scientific investigation or changing its evidence.
