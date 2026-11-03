
# UAV LLM Classification and Reasoning Evaluation
## Research Progress Notes — Batch 01

**Research area:** UAV Cybersecurity, Large Language Models, and Retrieval-Augmented Generation  
**Research supervisor:** Dr. Lopamudra Praharaj  
**Institution:** University of North Carolina at Pembroke  
**Researcher:** Md Mushfique Rahman, Syeda Nawal (literature review)
**Status:** GPT-6 baseline testing completed; formal reasoning evaluation pending  
**Documentation updated:** November 3, 2026

---

## 1. Research Objective

This research investigates whether large language models can
classify UAV telemetry as benign or malicious and provide
evidence-supported explanations for their decisions.

The research supervisor emphasized that classification alone
is not the intended contribution, since conventional machine
learning approaches can also perform classification.

The current focus is evaluating whether LLM-generated
explanations accurately identify relevant telemetry patterns,
provide logically supported conclusions, consider alternative
explanations, and acknowledge uncertainty.

RAG integration is planned for a later research phase.

## 2. Dataset

The experiments use a processed GPS-spoofing telemetry CSV
from the UAV Attack Dataset.

Dataset exploration results:

- Records: 3,622
- Columns: 84
- Benign records: 3,124
- Malicious records: 498
- Missing values: 0
- Duplicate rows: 0

Earlier exploration also compared processed GPS telemetry
against original flight logs.

A total of 683 matching global-position timestamps were
identified. Altitude matched exactly at these timestamps,
while latitude and longitude showed very small differences.

These checks do not establish full validation of all
dataset features or preprocessing operations.

## 3. Preliminary Experiments

Before Batch 01, two transition-adjacent telemetry windows
were prepared:

- One 10-record benign window
- One 10-record malicious window

The labels were withheld from the model prompts.

The preliminary responses were:

| Experiment | Model | Dataset label | Prediction |
|---|---|---|---|
| EXP-001A | Claude Opus 5.5 | Benign | Insufficient Evidence |
| EXP-001B | GPT-6 | Benign | Suspicious |
| EXP-002 | GPT-6 | Malicious | Suspicious |

These tests were exploratory.

They were not controlled benchmarks and cannot establish
generalizable detection accuracy or model superiority.

The preliminary experiments used a different classification
vocabulary from Batch 01.

## 4. Batch 01 — Experimental Design

Following supervisor feedback, a new evaluation batch was
prepared to investigate both classification and explanation
quality.

The batch includes:

- Five benign telemetry windows
- Five malicious telemetry windows
- Ten consecutive records per window
- Ten windows in total
- One hundred telemetry records in total

Each telemetry window is treated as one classification task.

The windows are non-overlapping and systematically selected
from a single processed flight sequence.

They are not independent flight-level observations.

Previously used transition-adjacent windows were excluded.

The experiment uses eight input features:

1. timestamp
2. lat_x
3. lon_x
4. alt_x
5. satellites_used
6. fix_type
7. jamming_indicator
8. vel_m_s

Ground-truth labels are excluded from the model inputs.

## 5. Prompt Design

A standardized prompt was developed for Batch 01.

The model is instructed to:

- Analyze all ten telemetry records.
- Use only supplied observations.
- Avoid assuming that an attack occurred.
- Avoid inventing sensor readings or attack mechanisms.
- Distinguish observations from possible explanations.
- Avoid unsupported assumptions about feature definitions
  and measurement units.
- Report insufficient evidence when a definitive
  classification cannot be supported.

The permitted predictions are:

- Benign
- Malicious
- Insufficient Evidence

The model is also asked to provide:

- Supporting telemetry observations
- Reasoning
- Alternative explanations
- Qualitative confidence
- Additional evidence needed

Neutral sample identifiers S001–S010 were used.

Ground-truth labels and original source sample identifiers
were stored separately in blind_sample_mapping.csv.

The same standardized prompt template was used for all
ten Batch 01 GPT-6 tests.

## 6. Batch 01 — GPT-6 Results

Ten model responses were collected.

| Sample | Dataset label | GPT-6 prediction | Confidence |
|---|---|---|---|
| S001 | Benign | Insufficient Evidence | Medium |
| S002 | Malicious | Insufficient Evidence | High |
| S003 | Benign | Insufficient Evidence | High |
| S004 | Malicious | Insufficient Evidence | Medium |
| S005 | Benign | Insufficient Evidence | Medium |
| S006 | Malicious | Insufficient Evidence | Medium |
| S007 | Benign | Insufficient Evidence | Medium |
| S008 | Malicious | Insufficient Evidence | Medium |
| S009 | Benign | Insufficient Evidence | High |
| S010 | Malicious | Insufficient Evidence | Low |

These labels follow the documented sample preparation and
blind mapping procedure. An independent cross-check of the
mapping against sample_metadata.csv remains pending.

### Classification summary

- Total evaluated windows: 10
- Insufficient Evidence predictions: 10
- Definitive predictions: 0
- Abstentions: 10
- Observed abstention rate: 100%
- Classification coverage: 0%
- Selective classification accuracy: Undefined

No definitive benign or malicious classification was made
under the current prompt condition.

This is a descriptive result for the tested samples and
experimental conditions, not a general claim about GPT-6's
ability to detect UAV cybersecurity attacks.

The model's qualitative confidence values are self-reported
and must not be interpreted as calibrated probabilities.

## 7. Preliminary Explanation Observations

Initial manual reviews found that the model frequently:

- Identified changes in jamming_indicator.
- Described satellite-count and fix-type behavior.
- Examined velocity, position, and altitude trends.
- Distinguished observed measurements from hypothetical causes.
- Considered possible non-malicious explanations.
- Requested additional evidence before confirming an attack.

These observations are preliminary.

Individual explanations have not yet undergone complete
source-telemetry verification or standardized formal scoring.

Therefore, explanation accuracy and reasoning quality
must not yet be reported as validated quantitative results.

## 8. Experimental Integrity Checks

The following checks were performed during sample
preparation and testing.

### Sample preparation

- Ten windows were generated.
- Each contains ten telemetry records.
- Selected windows do not overlap.
- Source row ranges were stored in sample_metadata.csv.

### Blind prompt generation

- Ten neutral sample IDs were generated.
- Ground-truth labels were omitted from model prompts.
- A basic search found no leaked source sample identifiers
  or unresolved template placeholders.

### Source-to-prompt checks

Source CSV records and generated prompt telemetry were
compared for tested samples.

Exact-match checks were reported for later samples,
including S004–S010.

These checks establish consistency between the selected
source CSV and generated prompts. They do not independently
validate original dataset annotations or feature semantics.

### Evaluation results CSV

A leading blank line was identified in evaluation_results.csv.

After its removal, PowerShell parsing checks reported:

- Ten experiment records
- Ten unique experiment IDs
- Thirteen columns
- Ten recorded abstentions

### Response file audit

All ten response files were found.

A keyword-based structural check confirmed that all files
were nonempty and contained the expected response sections.

This does not prove that every saved response is identical
to the original model output.

## 9. Methodological Limitations

### A. Single processed flight

All ten windows come from one processed telemetry sequence.

Consequently, the windows should not be treated as
independent flights or representative of other attacks.

### B. Small sample size

The batch consists of ten classification tasks.

The results cannot support broad performance claims.

### C. Unknown feature semantics

Complete definitions, expected ranges, and preprocessing
details for selected telemetry features have not yet
been independently verified.

In particular, interpreting jamming_indicator requires
appropriate documentation and context.

### D. Prompt sensitivity

All ten GPT-6 responses selected Insufficient Evidence.

One possible explanation is that the conservative prompt
encourages abstention.

However, this hypothesis has not been tested using a
controlled alternative prompt.

### E. Limited experimental control

Tests were conducted using chat interfaces rather than
a fully controlled API-based evaluation pipeline.

Model settings, hidden system instructions, and sampling
behavior may not be fully reproducible.

### F. Explanation versus internal reasoning

The experiment evaluates generated explanations.

These explanations must not be equated with direct access
to the model's hidden internal reasoning process.

### G. Formal evaluation pending

A detailed reasoning scoring rubric has not yet been
finalized or consistently applied.

Preliminary assessments must not be interpreted as
validated reasoning scores.

## 10. Pending Research Tasks

The following tasks remain:

- Verify blind_sample_mapping.csv against sample_metadata.csv.
- Audit all saved model responses for content integrity.
- Verify model-reported telemetry observations against
  the corresponding source CSV records.
- Finalize detailed reasoning evaluation criteria.
- Apply the same evaluation rules to every response.
- Distinguish classification correctness from abstentions.
- Investigate prompt sensitivity in a separately
  documented experimental batch.
- Conduct additional model comparisons if approved.
- Verify feature semantics and dataset preprocessing.
- Explore policy-grounded RAG after the baseline
  reasoning evaluation, following supervisor guidance.

## 11. Research Status

As of November 3, 2026, the first GPT-6 baseline
classification-and-explanation testing batch has been
completed.

All ten responses selected Insufficient Evidence.

The principal next task is to determine how accurately
and logically the model explains the telemetry it receives.

No RAG system has been implemented or evaluated in
this experimental phase.

No validated numerical reasoning-performance score
has been established.

The research remains in the baseline evaluation stage.
