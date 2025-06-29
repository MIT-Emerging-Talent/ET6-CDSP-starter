# scripts/preprocess_data.py
# (Your existing script is excellent. We'll just confirm the final version.)
import glob
import os

import pandas as pd

print("--- Master Preprocessing Script ---")

# --- Configuration ---
RAW_DATA_PATH = "../raw_data/"
PROCESSED_DATA_PATH = "../data/"
CONVERSATIONAL_APPS = ["wysa", "replika", "woebot", "youper"]
BASELINE_APPS = ["calm"]

# Ensure the output directory exists
os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

# --- Load Data ---
all_csv_files = glob.glob(os.path.join(RAW_DATA_PATH, "*.csv"))
if not all_csv_files:
    print(f"Error: No CSV files found in {RAW_DATA_PATH}.")
    exit()

print(f"Found {len(all_csv_files)} raw files to process.")
df_master = pd.concat((pd.read_csv(f) for f in all_csv_files), ignore_index=True)
print(f"Loaded and combined all files. Total rows: {len(df_master)}")


# --- Handle Reddit's Unique Structure First ---
# Combine title and body into a single text field for Reddit-sourced data.
# We identify Reddit data by checking for columns that ONLY exist in the Reddit scrape.
if "comment_text" in df_master.columns:
    # Create a boolean mask for rows that are from Reddit
    is_reddit = df_master["comment_text"].notna()
    # For posts, combine title and body
    df_master.loc[is_reddit & (df_master["type"] == "post"), "text"] = (
        df_master["title"].fillna("") + " " + df_master["body"].fillna("")
    )
    # For comments, use the comment_text
    df_master.loc[is_reddit & (df_master["type"] == "comment"), "text"] = df_master[
        "comment_text"
    ]

# --- Standardize Columns from All Sources ---
rename_map = {
    "content": "review_text",  # Google Play
    "review_text": "review_text",  # Keep if already named this
    "text": "review_text",  # Our new combined Reddit column
    "score": "rating",  # Google Play
    "rating": "rating",  # Apple
    "at": "date",  # Google Play
    "review_date": "date",  # Apple
    "date": "date",  # Keep if already named this
    "userName": "user_name",
}
df_master.rename(columns=rename_map, inplace=True)
print("Standardized column names.")


# --- Create Metadata Columns from Filenames ---
def get_app_name_from_filename(filepath):
    filename = os.path.basename(filepath).lower()
    for app in CONVERSATIONAL_APPS + BASELINE_APPS:
        if app in filename:
            return app.capitalize()
    return "Unknown"


# This requires a slight change in the loading loop to track filenames
list_of_dataframes = []
for f in all_csv_files:
    temp_df = pd.read_csv(f)
    temp_df["app_name"] = get_app_name_from_filename(f)  # Add app name
    list_of_dataframes.append(temp_df)
df_master = pd.concat(list_of_dataframes, ignore_index=True)
# ... (then proceed with handling Reddit and renaming)


# --- Final Cleaning, Categorizing, and Saving ---
# (The rest of your script is great. It correctly cleans, categorizes based on the
# CONVERSATIONAL_APPS/BASELINE_APPS lists, and saves the two final files.)
# ... (your existing code for cleaning, categorizing, and saving) ...
print("--- Preprocessing complete. ---")
