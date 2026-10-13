
from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Define input and output files
INPUT_FILE = (
    PROJECT_DIR / "data" / "raw"
    / "yellow_tripdata_2024-01.parquet"
)

OUTPUT_FILE = (
    PROJECT_DIR / "data" / "processed"
    / "yellow_tripdata_2024-01-cleaned.parquet"
)


def transform_data():
    print("Reading raw taxi data...")
    df = pd.read_parquet(INPUT_FILE)

    original_rows = len(df)
    print("Original rows:", original_rows)

    # Identify records with valid timestamps
    valid_timestamps = (
        df["tpep_pickup_datetime"].notna()
        & df["tpep_dropoff_datetime"].notna()
        & (
            df["tpep_dropoff_datetime"]
            > df["tpep_pickup_datetime"]
        )
    )

    # Keep positive distances and fares
    valid_distance = df["trip_distance"] > 0
    valid_fare = df["fare_amount"] > 0

    # Keep records that pass all initial checks
    df_clean = df[
        valid_timestamps
        & valid_distance
        & valid_fare
    ].copy()
    # Calculate trip duration in minutes
    df_clean["trip_duration_minutes"] = (
        df_clean["tpep_dropoff_datetime"]
        - df_clean["tpep_pickup_datetime"]
    ).dt.total_seconds() / 60
    # Extract pickup hour
    df_clean["pickup_hour"] = (
        df_clean["tpep_pickup_datetime"].dt.hour
    )
            
    # Extract pickup date
    df_clean["pickup_day"] = (
        df_clean["tpep_pickup_datetime"].dt.date
    )

    # Check trip duration quality
    print("\nTrip duration summary (minutes):")
    print(df_clean["trip_duration_minutes"].describe())

    print("\nTrips lasting longer than 24 hours:")
    print(
        (df_clean["trip_duration_minutes"] > 1440).sum()
    )


    removed_rows = original_rows - len(df_clean)

    # Save the cleaned dataset
    df_clean.to_parquet(OUTPUT_FILE, index=False)

    print("\nTransformation complete!")
    print("Original rows:", original_rows)
    print("Cleaned rows:", len(df_clean))
    print("Rows removed:", removed_rows)
    print("Saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    transform_data()
