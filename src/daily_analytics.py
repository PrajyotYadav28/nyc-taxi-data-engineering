
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "yellow_tripdata_2024-01-cleaned.parquet"
)

OUTPUT_FILE = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "daily_analytics.csv"
)


def create_daily_analytics():
    print("Reading cleaned taxi data...")
    df = pd.read_parquet(INPUT_FILE)

    # Keep only January 2024 pickups
    df = df[
        (df["tpep_pickup_datetime"] >= "2024-01-01")
        & (df["tpep_pickup_datetime"] < "2024-02-01")
    ].copy()

    # Group trips by pickup date
    df["pickup_day"] = (
        df["tpep_pickup_datetime"].dt.date
    )

    daily_summary = (
        df.groupby("pickup_day")
        .agg(
            total_trips=("pickup_day", "size"),
            total_fare=("fare_amount", "sum"),
            average_distance=("trip_distance", "mean"),
            average_duration=("trip_duration_minutes", "mean")
        )
        .reset_index()
        .sort_values("pickup_day")
    )

    # Round numeric results
    daily_summary["total_fare"] = (
        daily_summary["total_fare"].round(2)
    )
    daily_summary["average_distance"] = (
        daily_summary["average_distance"].round(2)
    )
    daily_summary["average_duration"] = (
        daily_summary["average_duration"].round(2)
    )

    # Save the daily report
    daily_summary.to_csv(OUTPUT_FILE, index=False)

    print("\nDaily analytics created!")
    print("Number of days:", len(daily_summary))
    print(daily_summary.head(10).to_string(index=False))
    print("\nSaved to:", OUTPUT_FILE)


if __name__ == "__main__":
    create_daily_analytics()
