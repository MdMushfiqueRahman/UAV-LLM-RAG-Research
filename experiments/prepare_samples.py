import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = (
    BASE_DIR
    / "dataset"
    / "UAVAttackData"
    / "Live GPS Spoofing and Jamming"
    / "GPS Spoofing"
    / "Processed"
    / "spoofing-merged-gps-only.csv"
)

OUTPUT_DIR = BASE_DIR / "experiments"

# Load dataset
df = pd.read_csv(DATASET_PATH)

# Select 10 consecutive records from each class
benign = df[df["label"] == "benign"].iloc[-10:].copy()
malicious = df[df["label"] == "malicious"].iloc[:10].copy()

# Select telemetry features
features = [
    "timestamp",
    "lat_x",
    "lon_x",
    "alt_x",
    "satellites_used",
    "fix_type",
    "jamming_indicator",
    "vel_m_s",
]

# Save ground-truth labels separately
benign[features].to_csv(
    OUTPUT_DIR / "benign_sample.csv", index=False
)
#Save malicious sample
malicious[features].to_csv(
    OUTPUT_DIR / "malicious_sample.csv", index=False
)

#Print the number of records in each sample
print("Benign sample:", len(benign), "records")
print("Malicious sample:", len(malicious), "records")
print("Sample files created successfully!")