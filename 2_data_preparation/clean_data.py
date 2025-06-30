#!/usr/bin/env python3
"""
Author: Ahmad Hamed Dehzad
Date:   2025-06-30
Description:
    Load, clean, and save the merged phishing dataset.
    - Fills missing fields
    - Parses dates
    - Cleans HTML, punctuation, and whitespace from text
    - Drops duplicates
    - Outputs cleaned_phishing_dataset.csv
"""

import pandas as pd
import re
from bs4 import BeautifulSoup
import warnings

# Suppress BeautifulSoup locator warnings
from bs4 import MarkupResemblesLocatorWarning

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


def clean_text(text):
    """Remove HTML, punctuation, extra whitespace, and lowercase."""
    text = BeautifulSoup(str(text), "html.parser").get_text()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text.lower().strip()


def main():
    # 1. Load the dataset
    df = pd.read_csv("merged_phishing_dataset.csv")

    # 2. Handle missing values
    df["sender"] = df["sender"].fillna("missing")
    df["receiver"] = df["receiver"].fillna("missing")
    df["subject"] = df["subject"].fillna("missing")

    # 3. Parse dates (with UTC to avoid mixed-timezone issues)
    df["date"] = pd.to_datetime(df["date"], errors="coerce", utc=True)
    df["date"] = df["date"].dt.tz_localize(None).fillna(pd.Timestamp("1970-01-01"))

    # 4. Apply text cleaning
    df["subject"] = df["subject"].apply(clean_text)
    df["body"] = df["body"].apply(clean_text)
    df["urls"] = df["urls"].astype(str).apply(clean_text)

    # 5. Drop duplicates and reset index
    df = df.drop_duplicates().reset_index(drop=True)

    # 6. Save cleaned dataset
    df.to_csv("cleaned_phishing_dataset.csv", index=False)
    print("Done! cleaned_phishing_dataset.csv created.")


if __name__ == "__main__":
    main()
