
import logging
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
LOG_DIR = PROJECT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)


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
    logging.info("Starting NYC Taxi Data Engineering Pipeline")
    print("Starting NYC Taxi Data Engineering Pipeline")

    for script in SCRIPTS:
        print(f"\nRunning {script}...")
        logging.info("Running %s", script)

        try:
            subprocess.run(
                [sys.executable, str(PROJECT_DIR / script)],
                cwd=PROJECT_DIR,
                check=True,
            )
            print(f"Completed {script}")
            logging.info("Completed %s", script)

        except subprocess.CalledProcessError:
            logging.exception("Pipeline failed while running %s", script)
            print(f"Pipeline failed while running {script}")
            raise

    logging.info("Pipeline completed successfully")
    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()