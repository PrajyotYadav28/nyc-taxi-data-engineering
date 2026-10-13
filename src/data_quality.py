
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "yellow_tripdata_2024-01-cleaned.parquet"
)


def check_data_quality():
    print("Reading cleaned taxi data...")
    df = pd.read_parquet(DATA_FILE)

    print("\n========== DATA QUALITY REPORT ==========")
    print("Total rows:", len(df))
    print("Total columns:", len(df.columns))

    print("\nMissing values by column:")
    missing = df.isnull().sum()
    print(missing[missing > 0].to_string())

    print("\nDuplicate rows:", df.duplicated().sum())

    print(
        "\nInvalid trip distances:",
        (df["trip_distance"] <= 0).sum()
    )

    print(
        "Invalid fare amounts:",
        (df["fare_amount"] <= 0).sum()
    )

    print(
        "Invalid trip durations:",
        (df["trip_duration_minutes"] <= 0).sum()
    )

    print("\nData quality check completed.")

    print(
        "Trips longer than 24 hours:",
        (df["trip_duration_minutes"] > 1440).sum()
    )



if __name__ == "__main__":
    check_data_quality()
