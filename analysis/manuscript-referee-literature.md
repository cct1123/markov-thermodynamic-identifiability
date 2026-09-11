# Independent manuscript review: literature, scope and PRE instructions

2026-09-11 UTC. Reviewed `manuscript/main.tex`, its incorporated `supplementary/proofs.tex`, the bibliography and [citation ledger](manuscript-literature-review.md). This review addresses attribution, claim scope and publication requirements; the independent mathematical review owns full proof correctness and the build review owns compilation. Source statements were compared with the primary passages inspected in the citation audit. The APS data-availability and AI policies were directly re-read for this review.

**Verdict:** the central scientific positioning is restrained and defensible relative to the inspected sources. Two literature sentences and the draft submission statements should be corrected before calling the package complete for expert review. No matching prior theorem or new scientific contradiction was identified in this bounded pass. The unresolved exact-theorem access gaps remain; this is not a novelty certificate.

## Required revisions

### 1. Preserve the static nature of the Mond precedent

At initial `main.tex:32`, “aggregated Markov systems can possess finite sets of compatible factorizations” cites `Mond2003`. The source proves statements about stochastic matrix factorizations and nested simplices. Its inspected Sec. 5/Fig. 13 gives an eight-point static factorization fiber. The source does not itself establish an equivalent-generator CTMC fiber. A later repository memo supplies a separate scalar-dynamics lift, but that deduction cannot be attributed to Mond et al.

Replace the clause with: “stochastic matrices can possess finite sets of nonnegative factorizations.” The following sentence about physical resets then makes the added dynamical restrictions clear. The [original paper](https://doi.org/10.1098/rspa.2003.1150), Theorem 2.4/Corollary 2.5 and Sec. 5, supports this narrower wording.

### 2. State the time-reversal condition in the introductory lower-bound sentence

At initial `main.tex:30`, “the entropy production of an observed process generally bounds the microscopic value from below” is broader than justified for an arbitrary observed-process time-reversal convention. The repository itself records the coarse-graining/time-reversal caveat. The current model is appropriate, but the introductory sentence should say which operation is meant.

Suggested replacement: “For the resolved-transition observation with its physically induced reversal, observed path irreversibility bounds microscopic entropy production from below.” Cite `vanDerMeer2022` or `Harunari2022` at that sentence. Van der Meer et al., Sec. VI.3–VI.4, fixes the required reversal explicitly; the observation is not an arbitrary coarse-grained Markov approximation. This is a wording correction, not an objection to the manuscript's own observation model.

### 3. Add factual AI research-use disclosure in Methods

At initial `main.tex:308`, the acknowledgment accurately names substantive tasks and does not fabricate human verification. However, [APS's AI policy](https://journals.aps.org/authors/appropriate-use-ai-tools), introductory research-use rule and “Authors/Disclosure,” asks for tool/version, assistance, and verification; research use belongs in Methods. Acknowledgments alone do not yet satisfy that instruction.

Suggested Methods paragraph: “This manuscript audit and preparation used OpenAI Codex, an assistant based on GPT-6, for literature retrieval, mathematical auditing, code preparation, computational checks, and drafting. The executed checks and source comparisons are documented in the accompanying package; they are distinct from the expert human review required before submission.” The system confirms GPT-6-based Codex, but no more specific runtime suffix is confirmed. Do not supply one. If prior research used other models, the human authors should complete that history from actual records. Retain pending human authorship and accountability explicitly until the responsible human approves them.

### 4. Do not imply that a permanent public identifier is an APS submission mandate

At initial `main.tex:312`, “A permanent public archive identifier must be supplied by the authors before submission” is a reasonable recommended release plan but overstates the inspected journal rule if presented as compliance. [APS's data policy](https://journals.aps.org/authors/data-availability-statements), “Overview of Policies,” requires an accurate data/software availability statement and encourages public deposition; its “Data Citation Requirements” requires citation when material is publicly shared. It does not universally require a public DOI before initial submission.

Suggested revision: “The supplied package contains the analytic inputs, source code and outputs used here. Public deposition and its persistent citation remain to be completed by the human authors; no public archive is claimed in this draft.” The final statement must specify actual access arrangements when submitted. Public deposition is preferable for this package, but this review does not authorize or perform it. This paragraph is still a review-stage statement, not final submission prose.

## Checks that pass

- The abstract states the cap-five exact theorem separately from the fixed-count local criterion. It does not silently claim an arbitrary five-state census, a minimum-state theorem omitted from the paper, or an unrestricted rate-cap result.
- The introduction and discussion credit normalized similarities, positive-model equivalence, invariant polytopes, reverse-rate singularities and generic confidence-set impossibility. They make no “first ever” claim or absence-of-search-match novelty argument.
- `Ehrich2021` is used for compatible hidden-model entropy and ambiguity, not as a proof of numerical unboundedness. The paper distinguishes its discrete-time observation scope from its own complete resolved-transition CTMC fiber through the explicit model formulation and discussion.
- `Vanluyten2008` and `HorvathTelek2007` support the broad realization antecedents. The appendix supplies its own minimality/similarity proof, rather than importing mismatched positive/minimality assumptions. The corrected bibliography lists Telek first.
- `HeZhang2006` supports invariant-polytopic methods without an attribution of the project's sharp two-port envelope to it. `Zeraati2012` and `SasonVerdu2016` are cited for established singularity mechanisms, not the project's constrained classification.
- The entropy formula cites both Schnakenberg and Nishiyama–Hasegawa. Schnakenberg's original full text remains unavailable, but the formula is explicitly present in Nishiyama–Hasegawa Eq. (4), and stationary cancellation is derived in the paper. No unsupported Schnakenberg theorem locator appears.
- The activity/rate-ratio paragraph credits stronger known upper bounds. The three-cycle counterexample correctly retains activity dependence. `Moss2022` is used as a mechanism antecedent; the manuscript proves its own model-indexed TV-transfer statement with the required fixed-horizon and uniform-coverage quantifiers.
- Reciprocal support, unknown topology, fixed kinetic channel count, known incidence, even variables, absolute time, joint amplitudes, state cap, fixed count, and minimality are explicitly separated. The tight-cap counterexample and spare-state splitting boundary are retained.
- Essential proofs are incorporated by `\input` after `\appendix`, so they are part of the main PDF despite the source directory being called `supplementary`. This satisfies PRE's requirement that the main article stand alone; it is not an attempt to hide a critical proof in optional supplemental material.
- The present `aps,pre,onecolumn` REVTeX layout is a readable regular-article draft. PRE supports lengthy regular articles and does not require the literal `preprint` class option. Reference titles and conventional numbered sections are appropriate. Human author names and affiliations are honestly pending.

## Optional focused improvement

`Nitzan2023` is verified in the bibliography but currently uncited, so BibTeX will omit it. One sentence recognizing compatible-model lower-bound optimization would make the closest prior optimization scope more explicit: “Compatible-model minimization also yields entropy lower bounds when coarse statistics and conditional waiting laws are imposed on a specified topology~\cite{Nitzan2023}.” Its preprint Eq. (16) supports that statement. This is useful context, not an essential scientific repair. Alternatively remove the unused entry only if the final package must contain no unused references; no fake citation should be inserted merely to use an entry.

## Remaining limits and review status

The major residual novelty risk is an uninspected or differently termed physical realization theorem, especially in the inaccessible originals recorded in the ledger. The major correctness risk belongs to expert assessment of the long global support exhaustion and its equality conditions; this literature review does not independently certify every proof step. Successful symbolic certificates and compilation do not replace that assessment.

After the four revisions above, the citation and journal-style portion is suitable for expert human review. Actual submission still requires responsible human authorship, affiliation, final scientific approval, accurate disclosure, and a completed availability statement. No additional scientific experiment is required by this literature review, and no external submission or communication has been performed.
