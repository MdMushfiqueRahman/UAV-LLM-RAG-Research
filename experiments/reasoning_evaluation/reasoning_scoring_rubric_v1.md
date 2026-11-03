
# UAV LLM Reasoning Evaluation
## Scoring Rubric — Version 1.0

**Project:** UAV Telemetry–Grounded LLM Intrusion Detection
**Evaluation batch:** Batch 01
**Status:** Proposed rubric; to be finalized before formal scoring
**Date:** November 3, 2026

---

## 1. Evaluation Objective

Evaluate the factual accuracy, evidence grounding, and
logical quality of LLM-generated explanations for UAV
telemetry classification.

The evaluation examines generated explanations, not
the model's inaccessible internal reasoning process.

Classification correctness and explanation quality
must be evaluated separately.

## 2. Evaluation Inputs

For each sample, the evaluator uses:

1. The original 10-record telemetry CSV.
2. The exact prompt provided to the model.
3. The preserved original LLM response.
4. The experiment metadata.

Dataset ground-truth labels are used for classification
evaluation, not as evidence that every stated explanation
is factually correct.

When possible, explanation reviewers should initially
assess responses without seeing the dataset labels.

## 3. Assessment Categories

Each dimension receives one of four categorical ratings:

### Supported (S)

The applicable requirements are satisfied and no material
contradiction is found in the available evidence.

### Partially Supported (P)

The response satisfies some applicable requirements,
but contains a material omission, imprecision, or
weakly justified statement.

### Unsupported (U)

The response materially contradicts available evidence,
fails the dimension's essential requirement, or makes
a substantive claim without sufficient support.

### Not Assessable (NA)

The dimension cannot reasonably be evaluated because
necessary information is unavailable or the dimension
does not apply.

NA must not be used to conceal a failure when the
necessary evidence is actually available.

These are proposed ordinal categories, not calibrated
numerical scores.

## 4. Dimension A — Observation Accuracy

**Question:**
Does the model correctly report the supplied telemetry?

### Supported

- Reported measurements match the source records.
- Described trends accurately reflect the data.
- Reported changes and calculations are accurate
  within reasonable rounding.
- No material invented measurement is identified.

### Partially Supported

- Most observations are correct.
- One or more minor mistakes or imprecisions occur.
- The mistakes do not fundamentally misrepresent
  the principal telemetry behavior.

### Unsupported

- Important values are incorrect.
- A major trend is reversed or misreported.
- The response invents material sensor measurements.
- The response materially misrepresents the telemetry.

### Not Assessable

The original telemetry is unavailable or unreadable.

### Evaluation procedure

Verify numerical statements against the source CSV.

For every material discrepancy, record:

- Sample ID
- Model statement
- Actual value or trend
- Relevant source rows
- Reason for the assigned rating

The evaluator must not infer unprovided sensor events
from the dataset class label.

## 5. Dimension B — Evidence Relevance

**Question:**
Are the observations used by the model relevant to
its cybersecurity assessment?

### Supported

- The model identifies meaningful telemetry features.
- It explains how the observations relate to the
  classification question.
- It recognizes limitations of individual indicators.
- Evidence is not treated as proof of an attack
  without adequate justification.

### Partially Supported

- Relevant features are identified.
- Their connection to the conclusion is incomplete
  or insufficiently explained.

### Unsupported

- The conclusion relies primarily on irrelevant
  observations.
- The model treats an unsupported relationship as
  decisive security evidence.
- The response fails to identify any relevant
  evidence despite clearly available observations.

### Not Assessable

There is insufficient material in the response to
evaluate the relevance of its evidence.

A response with no relevant evidence should be
rated Unsupported rather than NA.

## 6. Dimension C — Logical Consistency

**Question:**
Does the explanation logically support the selected
classification or abstention?

### Supported

- The conclusion is consistent with cited observations.
- Observations and hypotheses are distinguished.
- Uncertainty is represented appropriately.
- No material internal contradiction is present.
- The model avoids inferring causation from
  correlation without justification.

### Partially Supported

- The overall explanation is understandable.
- Some reasoning steps are weak or insufficiently
  justified, without a major contradiction.

### Unsupported

- The conclusion contradicts the evidence presented.
- The explanation includes major logical contradictions.
- The model claims an attack is confirmed without
  adequate evidence.
- The conclusion relies on an invented premise.

### Not Assessable

The response contains no interpretable reasoning
from which consistency can be evaluated.

If meaningful reasoning was required but entirely
omitted, rate Unsupported rather than NA.

### Important distinction

An Insufficient Evidence classification is not
automatically logically correct.

The evaluator must examine whether the stated
uncertainty is adequately justified.

Likewise, a correct dataset-label prediction does
not automatically imply a sound explanation.

## 7. Dimension D — Alternative Explanations

**Question:**
Does the model consider plausible non-malicious
explanations for the observed telemetry?

### Supported

- At least one relevant alternative is identified.
- The alternative is reasonably connected to
  an observed telemetry pattern.
- Hypothetical explanations are not presented
  as verified events.

### Partially Supported

- Alternatives are mentioned.
- Their relevance is weakly explained, generic,
  or incomplete.

### Unsupported

- Relevant alternatives are entirely omitted.
- Alternatives materially contradict known evidence.
- Hypothetical causes are falsely presented
  as established facts.

### Not Assessable

Use only when the criterion is genuinely inapplicable,
with a documented justification.

## 8. Dimension E — Avoidance of Unsupported Claims

**Question:**
Does the model avoid inventing or overstating facts?

This dimension evaluates safe evidence handling.
It does not require the model to prove that
the window is benign or malicious.

### Supported

- No material fabricated readings or events.
- No unsupported confirmed-attack statements.
- Unverified sensor meanings are not stated as facts.
- Speculative explanations are clearly qualified.

### Partially Supported

- Minor unsupported assumptions or overstatements
  are present.
- They do not materially determine the conclusion.

### Unsupported

- Material fabricated telemetry or security events.
- Unsupported claims about attack mechanisms.
- Undocumented thresholds or feature meanings
  presented as established facts.
- Unjustified certainty that materially affects
  the assessment.

### Not Assessable

The response is unavailable or otherwise
cannot be meaningfully reviewed.

### Important

Record this dimension as:

"avoidance_of_unsupported_claims"

A Supported rating means the model adequately
avoided unsupported claims.

It does not mean unsupported claims were found.

## 9. Classification Evaluation

The dataset provides two ground-truth classes:

- Benign
- Malicious

The model can output:

- Benign
- Malicious
- Insufficient Evidence

Use the following outcome mapping:

| Ground truth | Prediction | Outcome |
|---|---|---|
| Benign | Benign | Correct |
| Benign | Malicious | Incorrect |
| Malicious | Malicious | Correct |
| Malicious | Benign | Incorrect |
| Either class | Insufficient Evidence | Abstention |

Abstentions must not be silently counted as
correct classifications.

Report:

- Total samples
- Correct classifications
- Incorrect classifications
- Abstentions
- Classification coverage
- Abstention rate
- Selective classification accuracy, when defined

Coverage = (Correct + Incorrect) / Total

Abstention rate = Abstentions / Total

Selective accuracy =
Correct / (Correct + Incorrect)

Selective accuracy is undefined when there are
zero definitive predictions.

Explanation ratings remain separate from
classification outcomes.

## 10. Evaluation Workflow

For each sample:

1. Load the source telemetry.
2. Load the original model response.
3. Extract the model's stated prediction.
4. Verify numerical observations.
5. Assess Dimensions A through E.
6. Record supporting evidence for each rating.
7. Record discrepancies and unsupported claims.
8. Compare the prediction with ground truth
   for classification evaluation.
9. Preserve all original source materials.

Do not modify a model response to improve its score.

If a response has formatting problems, retain
the original and create a separately identified
readable copy when necessary.

## 11. Reviewer Procedure

To reduce subjective bias:

- Use the same rubric for all samples.
- Assess telemetry statements against actual CSV values.
- Prefer explicit evidence over general impressions.
- Record reasons for Partially Supported and
  Unsupported ratings.
- Do not assign scores based solely on whether
  the dataset label was predicted correctly.
- Document reviewer identity and assessment date.

A second independent reviewer is recommended.

When reviewers disagree:

1. Preserve both original assessments.
2. Identify the disputed statements.
3. Compare each statement against the evidence.
4. Record the agreed rating, if consensus is reached.
5. Retain unresolved disagreements transparently.

Do not claim inter-rater reliability unless it
has been formally calculated from independent ratings.

## 12. Reporting Rules

For each evaluation dimension, report:

- Number Supported
- Number Partially Supported
- Number Unsupported
- Number Not Assessable

Do not combine these categories into an overall
numerical reasoning score without defining and
justifying an aggregation procedure in advance.

Do not interpret the categorical ratings as
validated probabilities or measurements on
an interval scale.

Do not claim that the rubric is externally
validated unless such validation is conducted.

## 13. Batch 01 Status

Ten GPT-6 responses have been collected.

All ten selected:

Insufficient Evidence

Observed classification coverage: 0%

Observed abstention rate: 100%

Selective classification accuracy: Undefined

Formal explanation scoring has not yet been
performed using this rubric.

The existing preliminary qualitative observations
do not constitute final standardized scores.

## 14. Limitations

- Small sample size
- One processed flight sequence
- Correlated telemetry windows
- Unverified feature definitions and preprocessing
- Limited control over chat-interface model settings
- Possible prompt-induced abstention
- Proposed, not externally validated, scoring rubric
- Subjectivity in explanation assessment
- No completed RAG evaluation

## 15. Future Evaluation

After completing the baseline explanation assessment,
consider controlled prompt-comparison experiments.

Potential conditions include:

- Abstention-allowed classification
- Forced binary classification with uncertainty reporting

Prompt conditions must be documented separately.

Any RAG comparison should use appropriately controlled
inputs, a documented retrieval knowledge base, and
predefined evaluation criteria.

Future experiments require supervisor guidance
and should not be presented as already completed.
