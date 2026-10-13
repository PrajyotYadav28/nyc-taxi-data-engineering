
# NYC Taxi Data Engineering Project

## Project Overview
This project processes NYC Yellow Taxi trip data for January 2024 using Python and Pandas.

## Completed Steps
1. Downloaded the raw taxi dataset in Parquet format.
2. Inspected the dataset and checked its columns and missing values.
3. Cleaned records with invalid timestamps, non-positive trip distances, and non-positive fares.
4. Created trip duration, pickup hour, and pickup day columns.
5. Generated hourly analytics in CSV format.
6. Generated daily analytics in CSV format.
7. Created a data quality report.

## Current Data Quality Findings
- Cleaned dataset rows: 2,869,658
- Cleaned dataset columns: 22
- Duplicate rows: 0
- Invalid trip distances: 0
- Invalid fare amounts: 0
- Trips with zero or negative duration: 56
- Trips longer than 24 hours: 11
- Missing values remain in some columns.

## Tools Used
- Python
- Pandas
- PyArrow
- Parquet
- CSV
- Visual Studio Code

## Next Steps
- Review trip-duration anomalies.
- Validate daily analytics output.
- Load data into a SQL database.
- Build a dashboard.
