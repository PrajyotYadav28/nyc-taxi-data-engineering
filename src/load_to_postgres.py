
from pathlib import Path
import pandas as pd
import psycopg

PROJECT_DIR = Path(__file__).resolve().parents[1]

CSV_FILE = PROJECT_DIR / "data" / "processed" / "daily_analytics.csv"

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "nyc_taxi_db",
    "user": "postgres",
}


def load_daily_analytics():
    df = pd.read_csv(CSV_FILE)

    print("Rows in CSV:", len(df))

    password = None

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO daily_taxi_analytics
                (pickup_day, total_trips, total_fare,
                 average_distance, average_duration)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (pickup_day) DO UPDATE SET
                    total_trips = EXCLUDED.total_trips,
                    total_fare = EXCLUDED.total_fare,
                    average_distance = EXCLUDED.average_distance,
                    average_duration = EXCLUDED.average_duration
                """,
                df[
                    [
                        "pickup_day",
                        "total_trips",
                        "total_fare",
                        "average_distance",
                        "average_duration",
                    ]
                ].itertuples(index=False, name=None),
            )

    print("Daily analytics loaded successfully!")


if __name__ == "__main__":
    load_daily_analytics()
