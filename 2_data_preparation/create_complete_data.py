import os

import pandas as pd

# Define file paths
CLEANED_DATA_PATH = (
    "../1_datasets/processed_datasets/FRBNY_SCE_Credit_Access_cleaned.csv"
)
OUTPUT_DIR = "../1_datasets/processed_datasets"
COMPLETE_COLS_FILE = f"{OUTPUT_DIR}/FRBNY_SCE_Credit_Access_complete_columns.csv"

# Load the cleaned data
print("Loading cleaned data...")
cleaned_data = pd.read_csv(CLEANED_DATA_PATH)

print(f"Original data shape: {cleaned_data.shape}")

# Keep only columns with no missing values
complete_columns = [
    col for col in cleaned_data.columns if cleaned_data[col].isnull().sum() == 0
]
complete_cols_data = cleaned_data[complete_columns]

print(f"Shape with only complete columns: {complete_cols_data.shape}")

# Optionally, drop rows that are completely empty (shouldn't be any)
complete_cols_data = complete_cols_data.dropna(how="all")

# Save the data with only complete columns
os.makedirs(OUTPUT_DIR, exist_ok=True)
complete_cols_data.to_csv(COMPLETE_COLS_FILE, index=False)

print(f"Data with only complete columns saved to: {COMPLETE_COLS_FILE}")
print(f"File size: {os.path.getsize(COMPLETE_COLS_FILE) / 1024**2:.2f} MB")
