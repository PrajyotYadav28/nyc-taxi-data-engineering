# NYC Taxi Data Engineering Project

An end-to-end Data Engineering project using NYC Yellow Taxi trip data for January 2024. This project demonstrates data extraction, cleaning, validation, analytics, PostgreSQL integration, and interactive visualization with Power BI.

## Project Overview

The project processes NYC taxi trip data to identify daily travel patterns, hourly demand, fare revenue, average trip distance, and trip duration.

## Technologies Used

- **Python** — Data processing and pipeline automation
- **Pandas & PyArrow** — Data manipulation and Parquet processing
- **PostgreSQL** — Analytics storage and SQL queries
- **Power BI** — Interactive dashboard and data visualization
- **SQL** — Data analysis and aggregation
- **Git & GitHub** — Version control and project sharing

## Pipeline Workflow

1. **Extract:** Read the raw January 2024 Yellow Taxi Parquet dataset.
2. **Transform:** Remove invalid timestamps, non-positive trip distances, and non-positive fares; calculate trip duration and extract pickup hour and date.
3. **Analyze:** Generate hourly and daily taxi analytics.
4. **Validate:** Check duplicates, missing values, invalid durations, and other data-quality issues.
5. **Load:** Store daily and hourly summary data in PostgreSQL.
6. **Visualize:** Connect Power BI to PostgreSQL and build an interactive dashboard.

## Project Structure

```text
nyc-taxi-data-engineering/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── analytics.py
│   ├── daily_analytics.py
│   ├── data_quality.py
│   ├── load_to_postgres.py
│   ├── load_hourly_to_postgres.py
│   └── run_pipeline.py
├── sql/
│   └── daily_analytics_queries.sql
├── NYC_Taxi_Analytics_Dashboard.pbix
├── PROJECT_NOTES.md
└── README.md
```

## Key Analytics

- Daily taxi trip counts for January 2024
- Hourly taxi demand across 24 hours
- Total fare revenue
- Average trip distance
- Average trip duration
- Data-quality checks on processed records

## Database Tables

- `daily_taxi_analytics` — Daily trip counts, fare totals, average distance, and average duration.
- `hourly_taxi_analytics` — Hourly trip counts, fare totals, average distance, and average duration.

## How to Run

### Prerequisites
- Python 3.10 or later
- PostgreSQL
- Power BI Desktop (to view the dashboard)

### 1. Install Python dependencies

```bash
pip install pandas pyarrow "psycopg[binary]"
```

### 2. Prepare the dataset

Download the NYC Yellow Taxi trip dataset for January 2024 in Parquet format and place it at:

`data/raw/yellow_tripdata_2024-01.parquet`

### 3. Configure PostgreSQL

Create a PostgreSQL database named `nyc_taxi_db` and create the required analytics tables before running the pipeline.

The loader scripts use the following local connection settings by default:

- Host: `localhost`
- Port: `5432`
- Database: `nyc_taxi_db`
- User: `postgres`

Update `DB_CONFIG` in the loader scripts if your local PostgreSQL settings differ. The scripts prompt for the database password at runtime; do not store passwords in source code.

### 4. Run the pipeline

From the project root directory, execute:

```bash
python src/run_pipeline.py
```

The pipeline extracts and transforms the data, generates daily and hourly analytics, runs data quality checks, and loads the analytics into PostgreSQL.

### 5. View the dashboard

Open `NYC_Taxi_Analytics_Dashboard.pbix` using Power BI Desktop.

**Note:** The PostgreSQL analytics tables must exist before running the loader scripts.

## Learning Outcomes

- Built a Python-based data processing pipeline.
- Worked with Parquet datasets and large tabular data.
- Applied data cleaning and quality validation.
- Generated analytics using Pandas and SQL.
- Loaded aggregated data into PostgreSQL.
- Created a Power BI dashboard connected to a relational database.

## Future Improvements

- Automate scheduled pipeline execution.
- Add stronger data-quality rules and logging.
- Process additional months of taxi data.
- Deploy the pipeline to a cloud platform.
- Improve dashboard design and analytical measures.

---

**Project Type:** Data Engineering  
**Dataset Period:** January 2024  
**Visualization:** Power BI


## Dashboard Preview

![NYC Taxi Analytics Dashboard](dashboard.png) Prajyot@2811
