
from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Location of the cleaned dataset
INPUT_FILE = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "yellow_tripdata_2024-01-cleaned.parquet"
)

# Where we will save the hourly summary
OUTPUT_FILE = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "hourly_analytics.csv"
)


def create_hourly_analytics():
    print("Reading cleaned taxi data...")

    df = pd.read_parquet(INPUT_FILE)

    # Group trips by pickup hour
    hourly_summary = (
        df.groupby("pickup_hour")
        .agg(
            total_trips=("pickup_hour", "size"),
            total_fare=("fare_amount", "sum"),
            average_distance=("trip_distance", "mean"),
            average_duration=("trip_duration_minutes", "mean")
        )
        .reset_index()
        .sort_values("pickup_hour")
    )

    # Round numeric results for readability
    hourly_summary["total_fare"] = (
        hourly_summary["total_fare"].round(2)
    )
    hourly_summary["average_distance"] = (
        hourly_summary["average_distance"].round(2)
    )
    hourly_summary["average_duration"] = (
        hourly_summary["average_duration"].round(2)
    )

    # Save the summary for reporting
    hourly_summary.to_csv(OUTPUT_FILE, index=False)

    print("\nHourly analytics created!")
    print(hourly_summary.to_string(index=False))
    print("\nSaved to:", OUTPUT_FILE)


if __name__ == "__main__":
    create_hourly_analytics()
