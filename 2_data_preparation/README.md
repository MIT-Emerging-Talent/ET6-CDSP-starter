# Data Preparation

This folder contains Jupyter notebooks for cleaning and preparing datasets
used in the project. Each notebook focuses on a specific raw data source and
produces a cleaned dataset for further analysis or modeling.

## Notebooks Overview

### 01_clean_afdr_data.ipynb

- **Purpose:** Cleans and prepares the USDA Agricultural Finance Databook
  (Table A8) data (`afdr_a8.csv`), which contains quarterly loan volume
  data for U.S. farms by loan size.
- **Output:** `afdr_cleaned.csv` in `1_datasets/processed_datasets/`

### 02_clean_afdr_charts.ipynb

- **Purpose:** Cleans the USDA Agricultural Finance Databook (Table A2) data
  (`afdr_charts.csv`), which provides national-level statistics on
  non-real-estate farm loans (volume, interest rates, loan sizes, etc.).
- **Note:** This dataset is for historical comparison and not used for modeling.
- **Output:** `afdr_charts_cleaned_historical_match.csv` in `1_datasets/additional_data/`

### 03_clean_BNPL.ipynb

- **Purpose:** Cleans a Kaggle-sourced BNPL dataset (`BNPL.csv`) with 1,000
  customer records. This includes behavioral, financial, and demographic
  features relevant to BNPL risk analysis.
- **Output:** `BNPL_cleaned.csv` in `1_datasets/processed_datasets/`

### 04_clean_BNPL_intention_to_use.ipynb

- **Purpose:** Cleans a survey dataset (`BNPL Intention to use.xlsx`) from
  IIM Lucknow, measuring young shoppers' intention to adopt BNPL services
  via Likert-scale responses.
- **Note:** This dataset is for exploratory analysis of attitudes and
  intentions, not for modeling default risk.
- **Output:** `BNPL_intention_to_use_cleaned.csv` in `1_datasets/reference/`

### 05_clean_FRBNY-SCE-Credit-Access-complete_microdata.ipynb

- **Purpose:** Cleans the Federal Reserve Bank of New York SCE Credit Access
  microdata (`FRBNY-SCE-Credit-Access-complete_microdata.xlsx`), covering
  credit access, usage, and borrowing intentions from 2013–2017.
- **Output:** `FRBNY_SCE_Credit_Access_cleaned.csv` in `1_datasets/processed_data/`

---

Each notebook includes:

- Data loading and inspection
- Cleaning steps (handling missing values, renaming columns, type conversion)
- Output of a cleaned CSV for downstream analysis

Refer to each notebook for detailed steps and variable descriptions.
