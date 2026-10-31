
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parents[2]

DATASET_PATH = (
    PROJECT_DIR
    / "dataset"
    / "UAVAttackData"
    / "Live GPS Spoofing and Jamming"
    / "GPS Spoofing"
    / "Processed"
    / "spoofing-merged-gps-only.csv"
)

OUTPUT_DIR = Path(__file__).resolve().parent
SAMPLES_DIR = OUTPUT_DIR / "samples"

# Experiment configuration
WINDOW_SIZE = 10
WINDOWS_PER_CLASS = 5

FEATURES = [
    "timestamp",
    "lat_x",
    "lon_x",
    "alt_x",
    "satellites_used",
    "fix_type",
    "jamming_indicator",
    "vel_m_s",
]

# Load dataset
df = pd.read_csv(DATASET_PATH)

required_columns = FEATURES + ["label"]
missing = [col for col in required_columns if col not in df.columns]

if missing:
    raise ValueError(f"Missing dataset columns: {missing}")

SAMPLES_DIR.mkdir(parents=True, exist_ok=True)

metadata = []

for label in ["benign", "malicious"]:
    class_rows = df.index[df["label"] == label].tolist()

    # Avoid the 10 records previously used near the label transition
    if label == "benign":
        class_rows = class_rows[:-10]
    else:
        class_rows = class_rows[10:]

    # Construct consecutive, non-overlapping candidate windows
    candidate_starts = []

    for i in range(len(class_rows) - WINDOW_SIZE + 1):
        positions = class_rows[i:i + WINDOW_SIZE]

        if positions[-1] - positions[0] == WINDOW_SIZE - 1:
            candidate_starts.append(positions[0])

    # Select systematically spaced windows
    available = len(candidate_starts) // WINDOW_SIZE

    if available < WINDOWS_PER_CLASS:
        raise ValueError(f"Not enough windows for {label}")

    selected_positions = [
        int(i * (available - 1) / (WINDOWS_PER_CLASS - 1))
        for i in range(WINDOWS_PER_CLASS)
    ]

    for number, position in enumerate(selected_positions, start=1):
        start_row = candidate_starts[position * WINDOW_SIZE]
        end_row = start_row + WINDOW_SIZE

        window = df.iloc[start_row:end_row].copy()

        if len(window) != WINDOW_SIZE:
            raise ValueError("Unexpected window size")

        if not (window["label"] == label).all():
            raise ValueError("Window contains mixed labels")

        sample_id = f"{label}_{number:02d}"
        filename = f"{sample_id}.csv"

        window[FEATURES].to_csv(
            SAMPLES_DIR / filename,
            index=False
        )

        metadata.append({
            "sample_id": sample_id,
            "ground_truth": label,
            "start_row": start_row,
            "end_row_inclusive": end_row - 1,
            "record_count": len(window),
            "filename": filename,
        })

# Save labels and provenance separately
metadata_df = pd.DataFrame(metadata)

metadata_df.to_csv(
    OUTPUT_DIR / "sample_metadata.csv",
    index=False
)

print("Evaluation samples created successfully!")
print(metadata_df.to_string(index=False))
