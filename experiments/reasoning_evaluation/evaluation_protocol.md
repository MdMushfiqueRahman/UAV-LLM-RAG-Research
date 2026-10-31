
# UAV LLM Classification and Reasoning Evaluation

## 1. Objective

Evaluate whether large language models can:

1. Classify UAV telemetry as benign or malicious.
2. Identify observations that support their classifications.
3. Provide explanations consistent with the supplied telemetry.
4. Consider alternative non-malicious explanations.
5. Recognize insufficient evidence and avoid unsupported claims.

This study evaluates model-generated explanations, not the
models' hidden internal reasoning processes.

## 2. Dataset

Source: UAV Attack Dataset

Scenario: GPS spoofing

Processed dataset:
- Total records: 3,622
- Benign records: 3,124
- Malicious records: 498
- Total columns: 84

The ground-truth labels come from the processed dataset.
They indicate the dataset's assigned classes, not independently
verified attack evidence for each individual telemetry window.

## 3. Evaluation Batch 01

Number of windows: 10

- Benign windows: 5
- Malicious windows: 5
- Records per window: 10
- Total telemetry records: 100

Each window will receive one classification and one explanation.

The windows are non-overlapping and systematically selected
from one processed flight dataset. They must not be described
as statistically independent flights or random samples.

The original dataset row ranges are recorded in
sample_metadata.csv.

## 4. Input Features

Each window contains:

- timestamp
- lat_x
- lon_x
- alt_x
- satellites_used
- fix_type
- jamming_indicator
- vel_m_s

The ground-truth label is excluded from model inputs.

Feature semantics, measurement units, preprocessing, and
the interpretation of jamming_indicator require further
verification against dataset documentation.

## 5. Model Output Requirements

For each telemetry window, request:

1. Classification:
   - Benign
   - Malicious
   - Insufficient Evidence

2. Supporting observations:
   Identify specific values, trends, or relationships.

3. Explanation:
   Explain how the observations support the classification.

4. Alternative explanations:
   Consider plausible non-malicious causes.

5. Uncertainty:
   State limitations and missing evidence.

6. Additional evidence:
   Identify information needed to strengthen the conclusion.

Models must not be provided with the ground-truth labels.

## 6. Classification Evaluation

For each window, compare the model prediction against
the dataset ground-truth label.

- Correct: Benign predicted for benign, or Malicious
  predicted for malicious.
- Incorrect: Benign predicted for malicious, or Malicious
  predicted for benign.
- Abstention: Insufficient Evidence.

Abstention is tracked separately rather than automatically
counted as a correct or incorrect classification.

Report:

- Total windows evaluated
- Number of correct classifications
- Number of incorrect classifications
- Number of abstentions
- Coverage = (correct + incorrect) / total
- Selective accuracy = correct / (correct + incorrect)
- Abstention rate = abstentions / total

Selective accuracy is undefined if the model makes
no definitive classifications.

Because the initial batch is small and derived from
a single processed flight, these results are descriptive
and must not be generalized to other flights or attacks.

## 7. Explanation Quality Evaluation

Evaluate each model-generated explanation on five dimensions.

### A. Observation accuracy

Do the reported telemetry values and trends match the input?

### B. Evidence relevance

Are the cited observations relevant to the classification?

### C. Logical consistency

Does the conclusion follow reasonably from the stated evidence?

### D. Alternative explanations

Does the model consider plausible non-malicious explanations?

### E. Unsupported claims

Does the model invent readings, events, attack mechanisms,
or certainty unsupported by the supplied evidence?

Each dimension will initially be assessed using:

- Supported
- Partially supported
- Unsupported
- Not assessable

A detailed scoring rubric with examples and decision rules
must be finalized before assigning numerical reasoning scores.

Explanation quality will be reported separately from
classification correctness.

## 8. Model Comparison

If Claude and GPT-6 are compared:

- Use identical telemetry inputs.
- Use identical prompt wording.
- Preserve complete original responses.
- Record model names and available configuration details.
- Record test dates and interface/API details.
- Avoid claiming controlled reproducibility when using
  chat interfaces with unknown settings.

## 9. Experiment Records

For every test, retain:

- Experiment ID
- Sample ID
- Dataset row range
- Ground-truth label
- Model and available version information
- Exact input prompt
- Original model response
- Parsed classification
- Classification outcome
- Explanation assessment
- Experiment date
- Relevant limitations

## 10. Study Limitations

- One processed GPS spoofing dataset
- One flight sequence
- Small initial evaluation batch
- No independent flight-level test set
- Unverified feature definitions and units
- Potential temporal and preprocessing effects
- Limited control over chat-interface model settings
- No implemented RAG system in this phase

## 11. Future Research

After completing the baseline LLM-only evaluation,
investigate policy-grounded RAG as discussed with
the research supervisor.

Evaluate LLM-only and RAG-assisted responses on
the same held-fixed samples and criteria.

RAG implementation and results are not part of the
current completed experiments.
