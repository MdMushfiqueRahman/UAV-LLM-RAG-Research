from pathlib import Path
import pandas as pd


# Dataset location
csv_path = (
    Path("dataset")
    / "UAVAttackData"
    / "Live GPS Spoofing and Jamming"
    / "GPS Spoofing"
    / "Processed"
    / "spoofing-merged-gps-only.csv"
)

# Load the dataset
df = pd.read_csv(csv_path)

# Basic information
print("Dataset Shape:", df.shape)

print("\nCOLUMN NAMES:")
for i, column in enumerate(df.columns, start=1):
    print(f"{i}. {column}")

# Print the first 5 rows of the dataset
print("\nFIRST 5 ROWS:")
print(df.head().to_string())

print("\nMISSING VALUES:")
print(df.isnull().sum().to_string())

print("\nLABEL DISTRIBUTION:")
print(df["label"].value_counts(dropna=False))

print("\nUNIQUE LABELS:")
print(df["label"].unique())

print("\nLABEL TRANSITIONS:")
changes = df["label"].ne(df["label"].shift())
print(df.loc[changes, ["timestamp", "label"]].to_string(index=True))

# Print the telemetry around a label transition
features = [
    "timestamp",
    "label",
    "lat_x",
    "lon_x",
    "alt_x",
    "lat_y",
    "lon_y",
    "alt_y",
    "satellites_used",
    "fix_type",
    "jamming_indicator",
    "vel_m_s"
]

print("\nTELEMETRY AROUND LABEL TRANSITION:")
print(df.loc[3120:3128, features].to_string(index=True))


# Print the feature statistics by label
features = [
    "jamming_indicator",
    "satellites_used",
    "vel_m_s",
    "alt_x",
    "alt_y"
]

print("\nFEATURE STATISTICS BY LABEL:")

stats = (
    df.groupby("label")[features]
    .agg(["mean", "std", "min", "max"])
)

print(stats.round(4).to_string())


# Save the feature statistics by label to a CSV file
output_dir = Path("results")
output_dir.mkdir(exist_ok=True)

stats.to_csv(output_dir / "feature_statistics_by_label.csv")

print("\nStatistics saved successfully!")

# Analyze the timestamp data
print("\n========== TIMESTAMP ANALYSIS ==========")

print("Timestamp data type:", df["timestamp"].dtype)

print("First timestamp:", df["timestamp"].iloc[0])
print("Last timestamp:", df["timestamp"].iloc[-1])

print("Timestamps increasing:",
      df["timestamp"].is_monotonic_increasing)

print("Duplicate timestamps:",
      df["timestamp"].duplicated().sum())

time_diff = df["timestamp"].diff().dropna()

print("\nTimestamp differences:")
print(time_diff.describe())

print("\nNon-positive timestamp differences:",
      (time_diff <= 0).sum())

# Analyze the duplicate data
print("\n========== DUPLICATE ANALYSIS ==========")

print("Total duplicate rows:", df.duplicated().sum())

print(
    "Duplicate rows excluding timestamp:",
    df.drop(columns=["timestamp"]).duplicated().sum()
) 