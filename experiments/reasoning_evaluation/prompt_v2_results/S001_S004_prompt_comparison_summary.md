# Prompt Sensitivity Study ? Exploratory Results (S001?S004)

## Research Context
Project: UAV Telemetry?Grounded LLM Intrusion Detection and RAG Research

Researcher: Md Mushfique Rahman
Supervisor: Dr. Lopamudra Praharaj

## Objective
Investigate whether revising the classification instructions
changes Claude Opus 5.5's decisions on the same UAV telemetry windows.

This study compares the original conservative prompt (v1)
with a revised evidence-comparison prompt (v2).

## Experimental Setup
- Model: anthropic/claude-opus-5.5
- API: OpenRouter
- Windows: S001?S004
- Records: 10 per window; 40 total records
- Input features: 8
- Three possible classifications:
  Benign, Malicious, Insufficient Evidence
- Ground-truth labels withheld from model prompts
- Same telemetry records for v1 and v2
- One completed response per prompt version per sample
- RAG: Not used

The windows were previously inspected during prompt development.
Therefore, these results are exploratory, not independent validation.

## Classification Results

| Sample | Ground Truth | Claude v1 | Claude v2 |
|---|---|---|---|
| S001 | Benign | Insufficient Evidence | Benign |
| S002 | Malicious | Insufficient Evidence | Insufficient Evidence |
| S003 | Benign | Insufficient Evidence | Benign |
| S004 | Malicious | Insufficient Evidence | Insufficient Evidence |

## Descriptive Results

### Prompt v1
- Definitive predictions: 0/4
- Abstentions: 4/4
- Classification coverage: 0%

### Prompt v2
- Definitive predictions: 2/4
- Abstentions: 2/4
- Classification coverage: 50%
- Benign predictions: 2
- Malicious predictions: 0
- Correct definitive predictions: 2/2

The 2/2 figure is agreement with dataset labels among
non-abstained predictions. It is not overall detection accuracy.

## Reasoning Observations

Both prompt versions generally identified the main
numerical trends in the supplied telemetry.

The revised prompt explicitly encouraged comparison
of evidence for Benign and Malicious.

Some v2 explanations included interpretations whose
validity could not be established from the selected fields,
including physical consistency assumptions, generic
GNSS attack behavior, and data-preprocessing hypotheses.

Preliminary manual assessments noted potential concerns
in logical consistency and avoidance of unsupported claims.

These judgments have not been independently validated.

## Interpretation

The revised prompt changed classification behavior in
two benign-labeled exploratory windows.

However, neither malicious-labeled window received a
definitive Malicious prediction.

The results suggest prompt sensitivity, but they do
not demonstrate improved intrusion detection or establish
the cause of the original abstention behavior.

## Limitations
- Only four exploratory windows.
- Two benign and two malicious labels.
- Windows were reviewed before v2 design.
- One response per prompt/sample condition.
- No repeated trials or variability analysis.
- No independent judge-LLM evaluation.
- No RAG or security-policy retrieval.
- No independent-flight generalization assessment.

## Next Research Steps
1. Freeze and preserve Prompt v1 and Prompt v2.
2. Apply both prompts to additional telemetry windows
   without modifying instructions based on their results.
3. Compare classification coverage and ground-truth
   agreement, including mistakes and abstentions.
4. Review the quality and support of model explanations.
5. Investigate feature definitions, attack-specific context,
   and policy-grounded RAG in subsequent experiments.

## Conclusion
Prompt v2 increased classification coverage from 0/4
to 2/4 in this exploratory set.

Both definitive predictions were Benign and matched
their dataset labels.

No definitive malicious detection was observed.

Further evaluation is needed before claiming improvement
in classification or reasoning performance.
