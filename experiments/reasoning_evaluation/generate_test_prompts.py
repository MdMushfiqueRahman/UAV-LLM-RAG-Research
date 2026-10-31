
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
SAMPLES_DIR = BASE_DIR / "samples"
PROMPTS_DIR = BASE_DIR / "prompts"

TEMPLATE_PATH = PROMPTS_DIR / "classification_reasoning_template.txt"
METADATA_PATH = BASE_DIR / "sample_metadata.csv"
MAPPING_PATH = BASE_DIR / "blind_sample_mapping.csv"

def main():
    metadata = pd.read_csv(METADATA_PATH)

    required_columns = {
        "sample_id",
        "ground_truth",
        "start_row",
        "end_row_inclusive",
        "filename",
    }

    if not required_columns.issubset(metadata.columns):
        raise ValueError("Missing required metadata columns.")

    if len(metadata) != 10:
        raise ValueError("Expected exactly 10 samples.")

    if metadata["sample_id"].duplicated().any():
        raise ValueError("Duplicate sample IDs found.")

    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    if "{{SAMPLE_ID}}" not in template or "{{TELEMETRY_DATA}}" not in template:
        raise ValueError("Required placeholders missing from template.")

    # Interleave benign and malicious samples in a fixed order.
    benign = metadata[metadata["ground_truth"] == "benign"]
    malicious = metadata[metadata["ground_truth"] == "malicious"]

    if len(benign) != 5 or len(malicious) != 5:
        raise ValueError("Expected five samples per class.")

    ordered_rows = []
    for i in range(5):
        ordered_rows.append(benign.iloc[i])
        ordered_rows.append(malicious.iloc[i])

    mapping = []

    for index, row in enumerate(ordered_rows, start=1):
        blind_id = f"S{index:03d}"

        sample_path = SAMPLES_DIR / row["filename"]

        if not sample_path.is_file():
            raise FileNotFoundError(sample_path)

        sample = pd.read_csv(sample_path)

        if len(sample) != 10:
            raise ValueError(f"Unexpected record count: {sample_path}")

        if "label" in sample.columns:
            raise ValueError(f"Ground-truth label leaked: {sample_path}")

        telemetry_text = sample.to_csv(index=False)

        prompt = (
            template
            .replace("{{SAMPLE_ID}}", blind_id)
            .replace("{{TELEMETRY_DATA}}", telemetry_text.strip())
        )

        output_path = PROMPTS_DIR / f"{blind_id}_prompt.txt"

        if output_path.exists():
            raise FileExistsError(
                f"Refusing to overwrite existing prompt: {output_path}"
            )

        output_path.write_text(prompt + "\n", encoding="utf-8")

        mapping.append({
            "blind_id": blind_id,
            "source_sample_id": row["sample_id"],
            "ground_truth": row["ground_truth"],
            "start_row": row["start_row"],
            "end_row_inclusive": row["end_row_inclusive"],
            "prompt_filename": output_path.name,
        })

    if MAPPING_PATH.exists():
        raise FileExistsError(
            f"Refusing to overwrite existing mapping: {MAPPING_PATH}"
        )

    pd.DataFrame(mapping).to_csv(MAPPING_PATH, index=False)

    print("Successfully generated 10 blind evaluation prompts.")
    print("Ground-truth mapping saved to:", MAPPING_PATH)
    print("Prompt files saved to:", PROMPTS_DIR)
    print()
    print("Generated prompt IDs:")
    for item in mapping:
        print(item["blind_id"])

if __name__ == "__main__":
    main()
