#!/usr/bin/env python3
"""
Author: Ahmad Hamed Dehzad
Date:   2025-06-30

Description:
    Load, clean, and save the merged phishing dataset.
    - Fills missing fields
    - Parses dates
    - Cleans HTML, punctuation, and whitespace from text
    - Drops duplicates based on subject AND body
    - Outputs cleaned_phishing_dataset.csv
"""

import os
import pandas as pd
import re
from bs4 import BeautifulSoup
import warnings
from bs4 import MarkupResemblesLocatorWarning

# Suppress BeautifulSoup locator warnings
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


def clean_text(text: str) -> str:
    """Remove HTML, punctuation, extra whitespace, and lowercase the text."""
    # strip HTML
    text = BeautifulSoup(str(text), "html.parser").get_text()
    # collapse whitespace
    text = re.sub(r"\s+", " ", text)
    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    return text.lower().strip()


def main():
    # Determine the directory where this script lives
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build full paths for input and output
    input_path = os.path.join(script_dir, "merged_phishing_dataset.csv")
    output_path = os.path.join(script_dir, "cleaned_phishing_dataset.csv")

    # 1. Load the dataset
    df = pd.read_csv(input_path)

    # 2. Handle missing values
    df["sender"] = df["sender"].fillna("missing")
    df["receiver"] = df["receiver"].fillna("missing")
    df["subject"] = df["subject"].fillna("missing")
    df["body"] = df["body"].fillna("")

    # 3. Parse dates (with UTC to avoid mixed-timezone issues)
    df["date"] = pd.to_datetime(df["date"], errors="coerce", utc=True)
    df["date"] = df["date"].dt.tz_localize(None).fillna(pd.Timestamp("1970-01-01"))

    # 4. Clean text columns
    df["subject"] = df["subject"].apply(clean_text)
    df["body"] = df["body"].apply(clean_text)
    df["urls"] = df["urls"].astype(str).apply(clean_text)

    # 5. Drop duplicates where both cleaned subject and body match exactly
    df = df.drop_duplicates(subset=["subject", "body"], keep="first").reset_index(
        drop=True
    )

    # 6. Save cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Done! Saved cleaned dataset to:\n  {output_path}")


if __name__ == "__main__":
    main()
