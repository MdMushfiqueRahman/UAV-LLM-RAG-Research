# Cross-Model Reasoning Evaluation
## Claude Opus 5.5 vs DeepSeek V3.2 ? Prompt v2, S001?S010

### 1. Objective

Compare classification outcomes, abstention behavior,
and evidence-grounded reasoning from two LLMs given
the same ten UAV telemetry windows and frozen Prompt v2.

This is an exploratory comparison, not a validated
intrusion-detection benchmark or general model ranking.

### 2. Experimental Setup

- Dataset: Cyber-Physical UAV Dataset
- Samples: S001?S010
- Windows: 10 nonoverlapping windows
- Records: 10 records per window
- Dataset labels: 5 Benign, 5 Malicious
- Models: Claude Opus 5.5 and DeepSeek V3.2
- Prompt: Frozen Prompt v2
- Ground-truth labels: Withheld from model prompts
- Classification options: Benign, Malicious,
  Insufficient Evidence
- RAG: Not implemented or used
- Calls: One recorded Prompt v2 attempt per
  model and window in this comparison
- Model confidence: Qualitative, not calibrated

Both models were asked to classify each telemetry
window and provide observations, reasoning,
alternatives, confidence, and additional evidence.

### 3. Complete Classification Results

| Sample | Ground Truth | Claude Opus 5.5 | DeepSeek V3.2 |
|---|---|---|---|
| S001 | Benign | Benign | Insufficient Evidence |
| S002 | Malicious | Insufficient Evidence | Malicious |
| S003 | Benign | Benign | Malicious |
| S004 | Malicious | Insufficient Evidence | Insufficient Evidence |
| S005 | Benign | Benign | Benign |
| S006 | Malicious | Benign | Insufficient Evidence |
| S007 | Benign | Benign | Insufficient Evidence |
| S008 | Malicious | Benign | Benign |
| S009 | Benign | Benign | Malicious |
| S010 | Malicious | Insufficient Evidence | Insufficient Evidence |

### 4. Aggregate Classification Outcomes

| Metric | Claude Opus 5.5 | DeepSeek V3.2 |
|---|---:|---:|
| Correct definitive predictions | 5 | 2 |
| Correct Benign | 5 | 1 |
| Correct Malicious | 0 | 1 |
| False positives | 0 | 2 |
| False negatives | 2 | 1 |
| Abstentions | 3 | 5 |
| Definitive predictions | 7 | 5 |
| Classification coverage | 70.0% | 50.0% |
| Selective accuracy | 71.4% | 40.0% |

Classification coverage is the number of
definitive Benign/Malicious predictions divided
by all ten windows.

Selective accuracy is the number of correct
definitive predictions divided by the number
of definitive predictions.

Abstentions are excluded from selective accuracy,
but remain explicitly reported.

Neither metric should be interpreted as
generalizable model performance.

### 5. Malicious-Window Outcomes

The five malicious-labeled windows were
S002, S004, S006, S008, and S010.

Claude:
- Correct Malicious: 0
- Incorrect Benign: S006, S008
- Abstained: S002, S004, S010

DeepSeek:
- Correct Malicious: S002
- Incorrect Benign: S008
- Abstained: S004, S006, S010

These results indicate limited definitive
attack recognition within this selected set.

They do not show whether the attacks would
be detectable with additional contextual
telemetry, validated feature semantics,
or a different experimental design.

### 6. Benign-Window Outcomes

The five benign-labeled windows were
S001, S003, S005, S007, and S009.

Claude classified all five as Benign.

DeepSeek:
- Correct Benign: S005
- Incorrect Malicious: S003, S009
- Abstained: S001, S007

DeepSeek's benign-window errors are
important for analyzing unsupported
security interpretations.

### 7. Individual Reasoning Findings

#### S001 ? Benign

Claude predicted Benign.
DeepSeek abstained.

Different judgments about evidence sufficiency
occurred on the same benign-labeled window.

#### S002 ? Malicious

Claude abstained.
DeepSeek predicted Malicious.

DeepSeek considered multiple changing telemetry
features, including jamming_indicator,
satellites_used and vel_m_s.

The dataset label matches its prediction,
but the underlying attack mechanism was
not independently established by the prompt.

#### S003 ? Benign

Claude predicted Benign.
DeepSeek predicted Malicious.

DeepSeek claimed jamming_indicator and
vel_m_s were perfectly anti-correlated.

Previous verification found a Pearson
correlation of +1.0 on these ten records,
contradicting the anti-correlation claim.

DeepSeek additionally used unverified
synthetic/spoofing interpretations.

This is a documented numerical-reasoning
error accompanying a false positive.

#### S004 ? Malicious

Both models abstained.

DeepSeek's reasoning acknowledged missing
baseline and feature-interpretation context.

A minor description error concerned the
longitude trend.

#### S005 ? Benign

Both models predicted Benign.

DeepSeek interpreted fix_type = 3 as a
good 3D fix, although that meaning was
not established within the supplied prompt.

This illustrates an unverified semantic
assumption in an otherwise correct prediction.

#### S006 ? Malicious

Claude predicted Benign.
DeepSeek abstained.

DeepSeek avoided a definitive false-negative
classification but did not detect the attack.

Its explanation described jamming_indicator
as the only clearly changing feature,
despite changes in other telemetry fields.

#### S007 ? Benign

Claude predicted Benign.
DeepSeek abstained.

DeepSeek considered rising jamming_indicator
and vel_m_s trends but did not conclude
that these distinguished the hypotheses.

Feature semantics and possible preprocessing
effects were not independently verified.

#### S008 ? Malicious

Both models predicted Benign.

Both explanations emphasized relatively stable
GNSS-related fields, smooth movement and a
decreasing jamming_indicator trend.

This was a shared false-negative outcome,
not proof of an identical causal failure mode.

#### S009 ? Benign

Claude predicted Benign.
DeepSeek predicted Malicious.

Direct inspection of the ten records showed:

- jamming_indicator first decreases,
  then increases.
- vel_m_s first increases, then decreases.
- alt_x mainly rises and later falls.

DeepSeek incorrectly described the first
two features as monotonic across the
entire window.

Its inference about spoofing or jamming
was not grounded in mechanism-specific
evidence.

This is a documented false positive with
incomplete whole-window trend interpretation.

#### S010 ? Malicious

Both models abstained.

DeepSeek accurately reported the main
numerical trends:
- Constant satellite count and fix type
- Decreasing jamming_indicator
- Increasing vel_m_s
- Nearly constant coordinates
- A small altitude rise followed by a
  slight decline

It considered benign and malicious
hypotheses and treated potential
manipulation as unverified.

No model produced a definitive
Malicious prediction.

### 8. Cross-Model Interpretation

The models differ in both classification
behavior and evidence-sufficiency judgments.

Claude produced more correct definitive
predictions on this selected sample, but
failed to produce any correct Malicious
classification.

DeepSeek correctly predicted one
malicious-labeled window while also producing
two false positives on benign-labeled data.

The same Prompt v2 did not eliminate
model-specific interpretation differences.

Examples of observed limitations include:
- Unsupported feature-semantic assumptions
- Errors in describing whole-window trends
- Inferences about attack mechanisms
  without corroborating evidence
- Treating stable GNSS fields as relatively
  strong Benign evidence
- Difficulty distinguishing missing evidence
  from affirmative evidence of Benign behavior

These findings are descriptive, not causal
explanations of model behavior.

### 9. Evaluation Limitations

1. Only ten selected 10-record windows were used.

2. The windows are from the same dataset;
   they should not be treated as independent
   flights or a representative test population.

3. Only one recorded attempt per model and
   sample is analyzed here; run-to-run
   variability was not established.

4. Responses were generated through model APIs
   without validated calibration of confidence.

5. The prompt does not provide verified
   feature definitions, normal ranges or
   mission-specific reference thresholds.

6. Ground-truth agreement does not by itself
   establish valid causal reasoning.

7. Manual reasoning assessments are provisional,
   not independent judge-LLM scores.

8. No RAG retrieval, security-policy knowledge
   base or retrieval-grounded comparison
   was included in this experiment.

9. No claim of statistically significant
   superiority or deployment readiness
   is supported by these observations.

### 10. Next Research Steps

- Verify and document feature semantics
  and dataset preprocessing.
- Develop an explicit evidence-grounding
  evaluation rubric.
- Apply a separate judge model, with
  careful human review, to reasoning quality.
- Consider reproducibility across repeated
  model calls and additional windows.
- Develop a UAV-security policy and
  contextual evidence knowledge base.
- Later compare non-RAG reasoning against
  a controlled RAG-based condition.
- Preserve exact prompts, responses,
  model identifiers and experiment metadata.

### 11. Conclusion

Across ten selected telemetry windows,
Claude Opus 5.5 produced five correct
definitive classifications, two false
negatives and three abstentions.

DeepSeek V3.2 produced two correct
definitive classifications, two false
positives, one false negative and five
abstentions.

Reasoning review identified specific
problems involving numerical trend
description, unsupported security
interpretations and differing standards
for evidence sufficiency.

The central research opportunity is
not merely choosing the model with
more correct labels. It is investigating
whether domain-grounded evidence and
explicit reasoning evaluation can
improve reliability and interpretability
of UAV telemetry classification.
