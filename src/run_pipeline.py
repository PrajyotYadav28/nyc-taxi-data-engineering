
import subprocess
import sys

from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]


SCRIPTS = [
    "src/extract.py",
    "src/transform.py",
    "src/analytics.py",
    "src/daily_analytics.py",
    "src/data_quality.py",
    "src/load_to_postgres.py",
    "src/load_hourly_to_postgres.py",
]



def run_pipeline():
    print("Starting NYC Taxi Data Engineering Pipeline")

    for script in SCRIPTS:
        print(f"\nRunning {script}...")

        subprocess.run(
            [sys.executable, str(PROJECT_DIR / script)],
            cwd=PROJECT_DIR,
            check=True,
        )

        print(f"Completed {script}")

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
