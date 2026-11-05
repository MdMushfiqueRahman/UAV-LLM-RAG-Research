
# Batch 01 — LLM Telemetry Classification and Reasoning Evaluation

**Project:** UAV Telemetry–Grounded LLM Intrusion Detection and RAG Research  
**Experiment:** Reasoning Evaluation — Batch 01  
**Model evaluated:** GPT-6  
**Evaluation date:** November 2026  
**Research stage:** Preliminary LLM-only baseline (without RAG)  
**Evaluation status:** Initial classification and single-reviewer reasoning assessment completed; independent validation pending

---

## 1. Objective

The objective of Batch 01 was to examine how GPT-6 interprets UAV telemetry records when asked to distinguish benign from malicious behavior using only the supplied observations.

The experiment evaluated two separate aspects:

1. **Classification behavior:** Whether the model produced a definitive Benign or Malicious classification or abstained because of insufficient evidence.
2. **Reasoning quality:** Whether the model accurately described telemetry, selected relevant evidence, reasoned consistently, considered alternatives, and avoided unsupported claims.

This experiment was intended as an initial baseline for later policy-grounded RAG experiments, not as a validated operational intrusion-detection system.

## 2. Dataset and Sample Preparation

The experiment used the selected Cyber-Physical UAV Dataset, containing physical and cybersecurity-related telemetry features.

The previously explored processed dataset contained 3,622 records, including 3,124 benign and 498 malicious records.

For Batch 01:

| Item | Value |
|---|---|
| Total telemetry windows | 10 |
| Benign windows | 5 |
| Malicious windows | 5 |
| Records per window | 10 |
| Total records represented | 100 |
| Model | GPT-6 |
| Responses evaluated | 10 |
| Experimental rounds | One recorded response per window |

The windows were selected as non-overlapping groups of consecutive records. Previously tested transition-adjacent exploratory windows were not reused.

Each window was provided to the model without its ground-truth label. Ground-truth labels were preserved separately for evaluation.

The ten windows are not independent flights. Therefore, the sample size must not be interpreted as ten independent UAV operational scenarios.

## 3. Experimental Procedure

The procedure consisted of the following stages:

1. Prepare ten telemetry windows with eight selected telemetry fields.
2. Preserve sample identifiers and ground-truth mapping separately.
3. Generate blind prompts for the selected model.
4. Request one of three classifications:
   - Benign
   - Malicious
   - Insufficient Evidence
5. Require the model to provide:
   - Supporting telemetry observations
   - Reasoning
   - Alternative explanations
   - Qualitative confidence
   - Additional evidence needed
6. Save each GPT-6 response.
7. Compare predictions against the preserved ground-truth labels.
8. Examine the response against the original telemetry records.
9. Conduct a preliminary single-reviewer reasoning assessment using rubric v1.
10. Record results in the evaluation CSV and formal assessment document.

The prompt emphasized using only supplied telemetry, avoiding invented measurements or attack mechanisms, and withholding definitive conclusions when supporting evidence was inadequate.

No external security policy retrieval or RAG augmentation was used during Batch 01.

## 4. Classification Results

GPT-6 returned **Insufficient Evidence for all ten telemetry windows**.

| Ground truth | Total windows | Benign predictions | Malicious predictions | Abstentions |
|---|---:|---:|---:|---:|
| Benign | 5 | 0 | 0 | 5 |
| Malicious | 5 | 0 | 0 | 5 |
| **Total** | **10** | **0** | **0** | **10** |

**Observed classification outcomes:**

- Abstention rate: 10/10 (100%)
- Definitive classification rate: 0/10 (0%)
- Malicious windows identified as Malicious: 0/5
- Benign windows identified as Benign: 0/5

The model neither issued a definitive malicious alert nor a definitive benign classification.

Because every prediction was an abstention, conventional binary classification accuracy, precision, recall, and F1 score should not be presented as if a standard binary classifier had been evaluated.

The zero definitive classifications do not establish the model's ability to detect attacks or distinguish benign operation.

## 5. Confidence Distribution

The confidence values reported by GPT-6 were qualitative and were not calibrated probabilities.

| Confidence | Samples | Count |
|---|---|---:|
| High | S002, S003, S009 | 3 |
| Medium | S001, S004, S005, S006, S007, S008 | 6 |
| Low | S010 | 1 |
| **Total** | | **10** |

For responses that explicitly qualified confidence, the rating referred to the model's assessment of evidentiary sufficiency, not the probability of malicious behavior.

The confidence labels must not be interpreted as calibrated intrusion probabilities or measured detection reliability.

## 6. Preliminary Reasoning Evaluation

Each response was evaluated using a proposed five-dimension reasoning rubric.

The dimensions were:

A. Observation Accuracy  
B. Evidence Relevance  
C. Logical Consistency  
D. Alternative Explanations  
E. Avoidance of Unsupported Claims

The rubric used the categories Supported, Partially Supported, Unsupported, and Not Assessable.

The recorded single-reviewer assessment assigned Supported to all five dimensions for each of the ten responses.

| Dimension | Supported ratings | Total assessments |
|---|---:|---:|
| A. Observation Accuracy | 10 | 10 |
| B. Evidence Relevance | 10 | 10 |
| C. Logical Consistency | 10 | 10 |
| D. Alternative Explanations | 10 | 10 |
| E. Avoidance of Unsupported Claims | 10 | 10 |
| **Total** | **50** | **50** |

These results describe the preliminary reviewer's assessment of the explanations.

They do **not** demonstrate:

- Correct classification of benign or malicious samples.
- Independent validation of the reasoning rubric.
- Agreement between multiple evaluators.
- Faithfulness of generated explanations to the model's internal decision process.
- Successful intrusion detection.
- Generalizability to independent flights or attack scenarios.

The results suggest that the model often produced telemetry-grounded, cautious explanations under the current prompt, while abstaining from definitive classification.

This interpretation remains preliminary.

## 7. Observations Across the Evaluated Windows

The saved responses frequently discussed changes in `jamming_indicator`, satellite availability, GPS fix type, velocity, altitude, and position.

Several important patterns emerged.

### 7.1 Jamming Indicator Changes Were Not Sufficient for Classification

The model identified increasing or decreasing `jamming_indicator` trends across different windows.

For example:

- S006 (Malicious): `jamming_indicator` increased from 15.90909091 to 17.95454545.
- S007 (Benign): `jamming_indicator` increased from 28.56521739 to 36.78260870.
- S008 (Malicious): `jamming_indicator` decreased from 35.85714286 to 28.14285714.
- S010 (Malicious): `jamming_indicator` decreased from 35.51612903 to 33.77419355.

Both increasing and decreasing trends appeared in the evaluated malicious windows, while an increasing trend was also observed in a benign window.

These examples indicate that the direction of change alone is not a reliable distinguishing rule within the selected samples.

No general relationship between the indicator and attack status can be established from these examples.

### 7.2 Stable Satellite Count and Fix Type Did Not Establish Benign Operation

Several windows maintained constant values for `satellites_used` and `fix_type` despite having different ground-truth labels.

For example:

- S006 (Malicious): `satellites_used` remained 10.0; `fix_type` remained 3.
- S007 (Benign): `satellites_used` remained 11.0; `fix_type` remained 3.
- S008 (Malicious): `satellites_used` remained 10.0; `fix_type` remained 3.
- S010 (Malicious): `satellites_used` remained 11.0; `fix_type` remained 3.

The stability of these fields does not independently establish that a window is benign.

The model generally recognized this limitation in its explanations.

### 7.3 Motion-Related Trends Were Ambiguous Without Flight Context

The evaluated responses described gradual changes in velocity, altitude, and coordinates.

For example:

- S006 (Malicious): Velocity increased while altitude decreased.
- S007 (Benign): Velocity and altitude both increased.
- S008 (Malicious): Velocity and altitude both decreased.
- S010 (Malicious): Velocity increased while altitude changed only slightly.

Without an expected flight trajectory, operating state, normal reference behavior, or independently established interpretation thresholds, these patterns do not by themselves identify an attack.

These examples are descriptive and are not proposed detection rules.

## 8. Interpretation of the 100% Abstention Rate

The most notable Batch 01 result is that GPT-6 abstained for all ten samples, regardless of ground truth.

Several possible explanations require further investigation:

1. **Prompt conservatism:** The instructions may discourage definitive classifications when feature definitions or reference thresholds are unavailable.
2. **Limited telemetry context:** Ten-record windows with eight selected features may omit useful evidence.
3. **Missing domain knowledge:** The model was not provided with documented feature semantics, operational policies, or normal operating thresholds.
4. **Decision ambiguity:** Different cybersecurity states may produce overlapping telemetry patterns in the selected windows.

These are hypotheses, not experimentally established causes of abstention.

Additional controlled experiments are necessary to distinguish among them.

The current results do not establish that the model would classify successfully if a different prompt, longer window, or RAG context were supplied.

## 9. Limitations

Batch 01 has several important limitations:

- Only one recorded GPT-6 response was evaluated per telemetry window.
- Only ten windows were included.
- All windows originated from the selected dataset rather than ten independent flight scenarios.
- The windows contained ten records each and only eight selected telemetry fields.
- The experiment did not include policy-grounded RAG.
- Ground-truth labels were withheld during prompting but used for subsequent evaluation.
- All predictions were abstentions, limiting assessment of definitive classification performance.
- Reasoning assessments were conducted by a single reviewer.
- The scoring rubric is preliminary and has not been independently validated.
- The assessments evaluate the content of generated explanations, not their internal model faithfulness.
- The reported confidence values were qualitative rather than calibrated probabilities.
- Results cannot be generalized to operational UAV intrusion-detection performance.

## 10. Recommended Next Experiments

The following directions are proposed for discussion with the research supervisor.

### Experiment A — Repeated LLM Trials

Run additional trials using the same samples and the same controlled prompt.

Evaluate whether the model repeatedly abstains and whether its reasoning remains consistent across trials.

Model configuration and other relevant experimental conditions should be documented.

### Experiment B — Controlled Prompt Comparison

Compare the existing conservative prompt with a revised prompt while keeping the telemetry samples and other conditions fixed.

A revised prompt could explicitly separate the model's best-supported label from its evidentiary uncertainty.

The purpose would be to test whether the instructions influence classification behavior, not to force unsupported attack predictions.

### Experiment C — Policy-Grounded RAG

Introduce verified, relevant UAV telemetry documentation or cybersecurity policies through a retrieval system.

Compare:

- LLM-only baseline
- LLM with retrieved policy or domain context

Assess whether retrieved information improves evidence interpretation, classification coverage, and the quality of cited reasoning.

The retrieved material should have documented provenance, and unsupported interpretations should remain prohibited.

### Experiment D — Independent Reasoning Evaluation

Have another evaluator assess the same saved responses using an agreed rubric.

Compare reviewer ratings and identify ambiguous scoring criteria.

A separate judge LLM may be explored, but judge-model ratings should not be treated as independent ground truth without appropriate validation.

### Experiment E — Expanded Telemetry Context

Evaluate longer windows or additional documented features, while preserving blind evaluation and controlling sample selection.

Measure whether richer telemetry changes abstention behavior and classification outcomes.

## 11. Proposed Questions for the Supervisor

1. Should the next experiment first investigate the 100% abstention rate through controlled prompt comparisons?
2. Should we introduce validated feature definitions and reference thresholds before implementing RAG?
3. Which UAV policy documents or domain references should form the initial retrieval knowledge base?
4. Should reasoning assessment be performed by an independent human evaluator, a different judge LLM, or both?
5. What additional sample sizes, repeated trials, and evaluation metrics would be appropriate for the next research phase?

## 12. Conclusion

Batch 01 established a preliminary LLM-only experimental baseline for telemetry-grounded UAV cybersecurity reasoning.

GPT-6 processed ten blind telemetry windows consisting of five benign and five malicious samples.

All ten responses selected Insufficient Evidence, yielding a 100% abstention rate and no definitive benign or malicious classifications.

The preliminary five-dimension reasoning review recorded Supported ratings across all ten responses, but those ratings are single-reviewer judgments and do not demonstrate successful attack detection or independently validated reasoning quality.

The findings highlight an important distinction between generating a cautious, evidence-grounded explanation and producing a useful ground-truth classification.

The next research stage should determine why the baseline abstains and whether controlled prompt changes, verified domain context, repeated trials, or policy-grounded RAG improve classification coverage while preserving evidence-based reasoning.

---

**Associated research artifacts:**

- `evaluation_protocol.md`
- `reasoning_scoring_rubric_v1.md`
- `sample_metadata.csv`
- `blind_sample_mapping.csv`
- `evaluation_results.csv`
- `formal_reasoning_assessments.md`
- `samples/`
- `prompts/`
- `responses/`

**Document status:** Draft for supervisor review. Results are preliminary and have not undergone independent evaluation.
