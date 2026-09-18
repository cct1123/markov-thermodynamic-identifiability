# Publication-readiness assessment — substantial revision

14 September 2026. **Verdict: revised scientific draft ready for expert human review.** The package substantially strengthens the mathematical scope, statistical interpretation, physical assumptions and reproducibility. It is not a declaration of proven novelty, human-approved authorship, submission readiness or likely journal acceptance.

The [revised article](../manuscript/main.pdf) leads with exact recovery versus entropy stability and the general local upper-ceiling criterion. It contains 31 cited references, six reproducible publication figures and all essential proof appendices, including the new local unfolding proof. [Revision notes](../REVISION_NOTES.md) give the requested conceptual changes, new results, clarified claims, open questions and journal positioning. The [theorem/assumption map](../analysis/revision/AUDIT.md) identifies every conclusion's scope, proof and verification.

## Mathematical and scientific support

The six original main theorem statements are preserved verbatim, and the original Appendices A–F remain the prefix of the updated proof file. The 15 historical scientific scripts replay successfully, with unchanged scientific payloads and 22 protected accepted JSON outputs. Exact algebraic fields, rational interval signs and logarithm remainders support the balanced endpoint; conventional geometry and support exhaustion establish the global quantifiers. None is claimed formally verified.

New additions are: a full six-rate Jacobian and analytic relative-conditioning scaling; an explicitly quantified exponential rare-rate testing lower bound; a graph-coverage inverse from two Laplace points; an exact local exit-asymmetry unfolding; and a practical finite-trajectory moment estimator with dependence-aware uncertainty. The stronger activity–affinity ceiling is credited to Nishiyama–Hasegawa, not claimed new. [E065](../evidence/RECORDS.md#e065), [E066](../evidence/RECORDS.md#e066), [E067](../evidence/RECORDS.md#e067), [E068](../evidence/RECORDS.md#e068).

Important qualifications remain in the article:

- Absolute-rate regularity is compatible with poor relative-rate and entropy inference.
- Exponential testing cost requires independently variable reverse rates; a fixed functional prior can remove the hard alternatives.
- The five-state transition persists locally for a specified perturbation. Its boundary equation has a fold; the whole fiber has a subcritical continuum. The wider numerical grid is not global proof.
- The geometric rectangle has an exact certificate, but the two-entropy gap is asserted on a possibly smaller neighborhood by continuity.
- A sixth state destroys the finite exact fiber. Linear and positive minimal orders coincide for this particular family only.
- Activity, rate floors, rate ceilings and affinities are distinct constraints. Observed activity need not bound total activity.
- Physical entropy requires appropriate local detailed balance and channel/state resolution; abstract rates do not fix unique heat currents.

## Finite-data evidence

The executed study has 900 independently seeded actual CTMC trajectories and 7.65 million complete observed inter-event intervals. All six rates are fitted using only the resolved pair and timing. The unweighted constrained moment estimator has pointwise interior asymptotic justification via a martingale covariance argument; its numerical optimizer is not a certified global solver.

Interior models show useful estimation at thousands of events. The rare-reverse case has severe coverage failure even at 20,000 records, despite small observable residuals and optimizer convergence. Boundary/rank failures, conditional coverage, unconditional covered-and-interior fractions and Wilson Monte Carlo intervals are retained. The numerical lower rate floor and rare-count warning are expressly computational/heuristic, not physical evidence or a coverage theorem.

## Literature and independent review

The [source ledger](../analysis/revision/LITERATURE.md) compares observations, inferred objects, lower/upper direction, population/finite records, dimension assumptions and novelty implications. It distinguishes full journal reads, specified preprints, partial proof reads and inaccessible originals. The expanded literature does not establish literature-wide priority. [E069](../evidence/RECORDS.md#e069).

A separate [assembled-manuscript review](../analysis/revision/FINAL-REFEREE.md) read all main/supplementary text and found no theorem-level objection. Its two detector/citation corrections were incorporated. Separate analytical review checked the rare-rate coupling constant. These reviews share source models and software and are not external human peer review.

## Build and reproducibility

Run `python -B reproduce_all.py`; add `--build --tectonic /path/to/tectonic --offline` with a cached compiler. The [current run manifest](revision/reproduction.json) records the full exact/numerical workflow and 21 tests. [Build provenance](../manuscript/supplementary/build-report.json) covers all current supplementary sources and figure PDFs. [Source validation](../manuscript/supplementary/package-validation.json) checks labels, citations, imports, paths and hashes. [Repository preservation audit](revision/repository-audit.json) separates structural checks from semantic proof review.

Final visual and portable-extraction results are recorded in [delivery verification](revision/delivery-verification.json). The [package](manuscript-package.zip) has an internal hash manifest and excludes environments, prompt history, compiler/cache files and page renders. Prior September 11 archive/PDF checks remain historical and are not substituted for current verification.

## Human review and stopping rationale

The requested deliverables and accessible scientific tests are completed in the revised package. Further generic searches or more of the same Monte Carlo runs would not resolve the decisive remaining risks: expert assessment of global support exhaustion and attribution among older realization originals. New detector models, optimal rare-event inference, arbitrary-rate perturbations and unknown-dimension restrictions are substantive follow-on projects, not silently claimed solved.

Before submission, human authors should verify the main geometry and local extension, assess novelty against the primary comparison, fill names/affiliations and funding, finalize AI disclosure and data/code availability, and select a journal. PRE or JSTAT is the strongest current fit; a PRL version would require a separate focused short manuscript and a compelling breadth case. Nothing was submitted, committed, pushed or sent to another person during this revision.
