# Fixed-order finite fibers: bounded primary-source audit

Retrieved 2026-09-10 (UTC). Agent-owned comparison; no novelty certification. This audit reads the current [formulation](../analysis/formulation.md), [balanced-theta theorem](../analysis/theta-balanced-boundary.md), and the existing [realization](realization-frontier.md), [positive-realization](positive-realization-frontier.md), and [three-state-cone](three-state-cone-frontier.md) audits as project context. It does not independently recheck the theta calculation.

## Outcome

**Inference:** the primary texts inspected below support established fixed-order equivalence machinery and show why a canonical representative is not a count of physical generators. They do not establish or refute the project's claimed exactly-two whole fiber. No directly covering theorem was located in this bounded search. The important Larget full-text gap remains unresolved despite two new preprint routes; absence of an accessible or located theorem is not evidence of novelty.

The comparison target is particularly restrictive: the exact joint next-mark/time kernel of one resolved bidirected edge, unknown competitor topology, irreducible bidirected CTMCs, at most five states, hidden relabelings identified, and two distinct entropy values at a specific algebraic boundary. A theorem about equivalent pairs, generic identifiability, a preferred topology, or all signed realizations does not by itself count that whole admissible fiber.

## Primary theorem inspected: positive HMM equivalence

**Source / primary result:** B. Vanluyten, K. De Cock, J. C. Willems, B. De Moor, *Equivalence of State Representations for Hidden Markov Models*, European Control Conference, 2–5 July 2007, [author-hosted slides](https://homes.esat.kuleuven.be/~sistawww/smc/jwillems/Lectures/2007/ECCVanluyten.pdf). Full 21-slide text inspected; locators below are displayed slide numbers.

Slides 6–8 define discrete-time Mealy output-string probabilities and signed quasi models. Slide 13 states: an invertible transformation with `T e = e`, `pi T^-1 >= 0`, and `T Pi(y) T^-1 >= 0` for every output yields an equivalent positive model. When the starting model is minimal as a quasi model, this characterizes the equivalent models of that order. Slide 14 leaves accurate geometric description of its example set as a problem. Slide 16 gives permutation uniqueness for a quasi Moore model minimal as quasi Mealy, with distinct state output distributions and a full-rank transition matrix.

**Comparison / inference:** this is direct precedent for intersecting a minimal similarity class with positivity constraints. It does not supply continuous-time generator, bidirected-support, resolved-edge, entropy, or exactly-two conclusions. Ordinary binary aggregation repeats state output distributions, so the stated Moore uniqueness conditions cannot simply be assumed.

### Journal and conference versions: access limits

The 2008 journal article has a different author list: B. Vanluyten, J. C. Willems, B. De Moor, *Systems & Control Letters* **57**(5), 410–419, [DOI 10.1016/j.sysconle.2007.10.004](https://doi.org/10.1016/j.sysconle.2007.10.004). Its [publisher abstract/introduction/section snippets](https://www.sciencedirect.com/science/article/pii/S0167691107001429) describe complete same-order equivalence sets, including positive Moore models. Those snippets were inspected; the complete journal theorem text was **not** obtained. Do not identify the slides with the full journal paper or transfer uninspected journal hypotheses.

The [author publication directory](https://homes.esat.kuleuven.be/~sistawww/cgi-bin/subpub.pl?Name=Willems+J&Sort=Type&Type=AccPub) supplies the [journal preprint](https://ftp.esat.kuleuven.be/pub/stadius/ida/reports/07-130.pdf); the PDF fetch failed. The separately indexed [conference report 06-157](https://ftp.esat.kuleuven.be/pub/sista/bvanluyt/reports/06-157.pdf) exposed theorem snippets in search but its direct PDF fetch timed out. An alternate old-author-directory journal path and Lirias record routes also failed. These are access attempts, not full-text reads.

## Primary continuous-time comparison: canonical aggregation forms

**Source / primary result:** W. J. Bruno, J. Yang, J. E. Pearson, *Using independent open-to-closed transitions to simplify aggregated Markov models of ion channel gating kinetics*, PNAS **102**(18), 6326–6331 (2005), [full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC1088360/), [DOI 10.1073/pnas.0409110102](https://doi.org/10.1073/pnas.0409110102). Main text inspected. Detailed proofs are delegated to supporting information; its linked endpoint failed here.

In Methods, “Equivalence and Canonical Forms” distinguishes equivalent models from equivalent topologies and allows nonphysical canonical rates. Results states generic MIR/BKU identifiability; “Canonical Forms and Detailed Balance” states that transforming an equilibrium model into either canonical form preserves detailed balance, while other equivalent models can violate it. “Rank 1 Topologies” gives nonnegative canonical realizations for rank-one detailed-balanced models and topology equivalence for fixed open/closed state counts.

**Comparison / inference:** these statements do not count every positive realization at an exceptional boundary. Their observation is binary state-aggregation dwell times. In the theta graph, any state partition separating the observed edge's endpoints also cuts each hidden path connecting those endpoints. Its aggregate record therefore includes transitions absent from the resolved-edge record. Applying these theorems requires an additional reduction, not merely renaming observations.

## Outstanding original-source gap: Larget

B. Larget, *A canonical representation for aggregated Markov processes*, *Journal of Applied Probability* **35**(2), 313–324 (1998), [DOI](https://doi.org/10.1239/jap/1032192850), remains abstract-only in this workspace. The abstract's unique canonical representative under regularity conditions is not a verified theorem about uniqueness of admissible physical models.

New routes tried in this audit:

- [Author-uploaded ResearchGate record](https://www.researchgate.net/publication/2673841_A_canonical_representation_for_aggregated_Markov_processes): search lists public author full text, but opening returned cache miss. Its displayed upload/publication dates conflict with the journal year; use the journal's 1998 citation.
- [CiteSeer indexed preprint PDF](https://citeseerx.ist.psu.edu/document?doi=72d00d79989bba34798fd4888b588fae03af9d4f&repid=rep1&type=pdf): search indexes a 17-page preprint, but opening failed. No theorem read.
- [Author CV](https://pages.stat.wisc.edu/~larget/cv.pdf): a bibliographic lead and dissertation title, not a replacement for the original theorem text.

The needed next evidence is the actual canonical-equivalence theorem and definitions: regularity, minimality notion, preservation of positive rates, whether order is fixed, and whether any exceptional finite nonsingleton physical class is classified. The present audit does not close the older Kienker or Förster–Nagy full-text gaps either; their previously failing publisher routes were not repeated.

## What remains a candidate contribution

The existing audits already separate scalar Coxian representation counts and isolated static nonnegative factorizations from joint dynamical realization. This audit adds a precise positive-HMM similarity precedent and a continuous-time aggregation comparison. Accordingly, the candidate contribution should be stated as the explicit **whole-fiber cardinality and distinct entropy values**, under the stated observation and five-state bidirected constraints, together with the proved boundary transition. Similarity equivalence, canonical forms, positive-realization constraints, and observational ambiguity themselves are established ideas.

Searches combined the exact paper titles and author names with `pdf`, `theorem`, `finite`, `isolated`, `minimal`, `positive realization`, and `aggregated Markov`. Most finite/isolated hits returned the already separated scalar or static-factorization settings; primary publisher abstracts on general positive-realization dimension bounds did not yield a relevant fixed-order classification. Searches and failed access do not establish completeness. The bounded stopping reason is that the accessible new theorem has been compared and the remaining decisive original-source gap is now tied to concrete preprint routes; broader novelty review remains open.
