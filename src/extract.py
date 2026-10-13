from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Locate the January 2024 taxi dataset
DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "yellow_tripdata_2024-01.parquet"
)

# Read the dataset
df = pd.read_parquet(DATA_FILE)

# Display basic information
print("Dataset loaded successfully!")
print("Number of rows and columns:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst five taxi records:")
print(df.head())

# Display information about the dataset
print("\nDataset Information:")
df.info()

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for invalid trip distances
print("\nTrips with zero or negative distance:")
print((df["trip_distance"] <= 0).sum())

# Check for invalid fare amounts
print("\nTrips with zero or negative fare:")
print((df["fare_amount"] <= 0).sum())

# Check for drop-off before pickup
print("\nDrop-off before pickup:")
print(
    (df["tpep_dropoff_datetime"] <
     df["tpep_pickup_datetime"]).sum()
)

# Check for duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())