# Autonomous research architecture

The research agent chooses useful actions in an adaptive, evidence-driven loop. The workspace preserves progress across runs. Actions below are options, not mandatory phases; delegation is optional under the operating rules, with no prescribed agent hierarchy.

```mermaid
flowchart TD
    Human["Human brief and supplied context"] --> Files["Persistent workspace files"]
    Files -.->|Read| Uncertainty["Identify consequential uncertainty"]
    Uncertainty ==> Choose["Choose the next useful action"]
    Choose ==> Search["Source retrieval"]
    Choose ==> Analyze["Calculation or modeling"]
    Choose ==> Test["Hypothesis testing"]
    Choose ==> Verify["Verification or falsification"]
    Search ==> Evidence["Save evidence and artifacts"]
    Analyze ==> Evidence
    Test ==> Evidence
    Verify ==> Evidence
    Evidence ==> Update["Update state and interpretation"]
    Update -.->|Checkpoint| Files
    Update ==> Assess{"Continue, pause, or finish?"}
    Assess -->|Useful authorized work remains| Uncertainty
    Assess -->|External input needed| Input["Record blocker and required input"]
    Input -->|Input supplied| Files
    Assess -->|Stop under operating rules| Report["Synthesis and matching state checkpoint"]
    Report -.->|Save| Files
```

[PROJECT.md](PROJECT.md) is the human brief; [AGENTS.md](AGENTS.md) supplies operating rules. The agent saves traceable evidence and consequential decisions in [evidence/RECORDS.md](evidence/RECORDS.md), reproducible work in [analysis/](analysis/README.md), and a concise handoff in [STATE.md](STATE.md). [outputs/REPORT.md](outputs/REPORT.md) holds the synthesis. Evidence and artifacts are saved before the state checkpoint that cites them.
