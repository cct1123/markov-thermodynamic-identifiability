# Evidence and decision records

Agent-maintained. **No research evidence or decision records exist yet.** Add only material that supports continuity, auditability, or a conclusion. Assign stable `E001`, `E002`, etc. evidence IDs and `D001`, `D002`, etc. decision IDs. Use ID-only headings; put a descriptive title beneath each heading. Existing IDs must not be renamed or reused.

The fenced formats below are **examples only, not findings or assigned IDs**. Adapt fields to the evidence and combine related facts. When a real record is added, link it from state and report using its heading anchor. For example, the following link patterns become valid only after an actual `E001` record exists:

```markdown
From a root document: [E001](evidence/RECORDS.md#e001)
From outputs/REPORT.md: [E001](../evidence/RECORDS.md#e001)
```

## Evidence record format

```markdown
## E001

**Short finding**

- Recorded: YYYY-MM-DD, with time and timezone when useful.
- Kind: observation | primary result | secondary statement | reproduced calculation | inference | assumption | hypothesis | speculation
- Finding: the claim or result, with scope and units when relevant.
- Provenance: author/organization, title, date/version, URL/DOI or local path; retrieval date for online sources; page/section/table/figure/data locator. For an inference, assumption, or hypothesis, identify its author and evidence or rationale instead of inventing an external source.
- Access / method: what was actually read, observed, or executed; any access limitation. For computation, link inputs, method, run instructions, and outputs.
- Bearing on the objective: what this supports or challenges; separate the source result from the agent's interpretation.
- Limitations / counterevidence: relevant uncertainty, dependencies on other evidence, contrary records, or untested assumptions.
```

Reuse provenance by linking an existing record for the same source and specifying the new locator. Do not count reuse of that source as corroboration. For a source-reported number, say whether it was independently checked. Add a correction or supersession link if a recorded claim changes; retain enough of the earlier record to explain the change. Label unsuccessful or incomplete work accurately; absence of a result is not evidence against a hypothesis.

## Decision record format

```markdown
## D001

**Short decision**

- Date: YYYY-MM-DD, with time and timezone when useful.
- Decision / change: the adopted interpretation, rejected hypothesis, consequential assumption, or scope decision.
- Basis: concise evidence-based justification, linking relevant E records or artifacts and any consequential contrary evidence.
- Consequence / reconsider when: what changes next, and which new evidence or input could reverse this decision.
```

No exhaustive search diary or private reasoning transcript is required. Record a failed avenue when it matters to interpretation, prevents duplicated work, or supports the stopping rationale. If records are split into topic files, keep this entry point and preserve existing links. Full operating conventions are in [AGENTS.md](../AGENTS.md).
