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

print("\nFIRST 5 ROWS:")
print(df.head().to_string())

print("\nMISSING VALUES:")
print(df.isnull().sum().to_string())