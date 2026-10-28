# UAV LLM/RAG Research — Experiment Notes

## October 28, 2026 — Initial LLM-Only Experiments

### Objective
Explore whether general-purpose LLMs can identify potentially suspicious patterns in UAV GPS telemetry without being given ground-truth attack labels.

### Dataset
UAV Attack Dataset — GPS Spoofing scenario.

### Experimental Setup
- Two 10-record telemetry windows were selected from opposite sides of the benign-to-malicious label transition.
- Eight telemetry fields were included.
- Ground-truth labels were excluded from the model inputs.
- No retrieval-augmented generation (RAG) was used.
- Claude Opus 5.5 and GPT-6 were tested through chat interfaces.

### Preliminary Observations
- Claude Opus 5.5 abstained on the benign window, reporting insufficient evidence.
- GPT-6 classified the benign window as suspicious.
- GPT-6 also classified the malicious window as suspicious.
- Both GPT-6 responses acknowledged that the observations did not confirm an attack.

### Limitations
- Only two telemetry windows were examined.
- Each model produced one response per tested window.
- Windows were adjacent to a single dataset label transition.
- Data preprocessing and feature semantics require further verification.
- The model-reported confidence levels are not calibrated probabilities.
- Model settings and chat-interface behavior were not fully controlled.
- No classification accuracy, false-positive rate, or generalization claim can be established from these observations.

### Next Research Direction
Verify telemetry feature definitions and preprocessing, then develop a structured evaluation protocol with additional benign and malicious windows. Introduce documented UAV security knowledge through retrieval and compare LLM-only responses against RAG-assisted responses using the same model and test cases.