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
 customer records, including behavioral, financial, and demographic
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

This directory contains scripts and notebooks for cleaning and preparing our
financial datasets for analysis. Each script processes specific datasets and
outputs cleaned versions for use in our modeling and exploration work.

## 📊 Script Overview

### Jupyter Notebooks

#### `01_clean_afdr_data.ipynb`

- **Input**: `../1_datasets/raw_data/afdr_a8.csv` (USDA Agricultural Finance
  Databook Table A8)
- **Purpose**: Cleans quarterly loan volume data across various loan sizes for
  U.S. farms
- **Processing**:
  - Renames messy column names to cleaner versions
    (e.g., "$1,000 to!$9,000" → "$1k–9k")
  - Converts numeric columns to proper data types
  - Handles missing values by filling with 0
- **Output**: `../1_datasets/processed_datasets/afdr_cleaned.csv`
- **Use Case**: Provides historical insights into traditional loan structures
  for comparison with BNPL patterns

#### `02_clean_afdr_charts.ipynb`

- **Input**: `../1_datasets/raw_data/afdr_charts.csv` (USDA Agricultural
  Finance Databook Table A2)
- **Purpose**: Processes quarterly statistics on non-real-estate farm loans
  (volume, interest rates, loan sizes, floating-rate shares)
- **Processing**:
  - Renames columns to shorter, cleaner names
  - Ensures numerical values are float type
  - Handles missing values
- **Output**: `../1_datasets/reference/afdr_charts_cleaned.csv`
- **Use Case**: Historical benchmark for comparing financial behavior evolution
  (NOT used for modeling due to aggregated nature)

#### `03_clean_BNPL.ipynb`

- **Input**: `../1_datasets/raw_data/BNPL.csv` (Kaggle dataset with 1,000
  customer records)
- **Purpose**: Cleans BNPL user profiles with behavioral, financial, and
  demographic features
- **Processing**:
  - Validates data quality (checks for missing values, duplicates)
  - Ensures proper data types
  - No missing values found, minimal cleaning required
- **Output**: `../1_datasets/processed_datasets/BNPL_cleaned.csv`
- **Use Case**: Primary dataset for BNPL default risk modeling with features
  like:
  - `failed_traditional_credit`, `over_indebtedness_flag`,
    `financial_stress_score`
  - `bnpl_usage_frequency`, `payment_delinquency_count`,
    `credit_limit_utilisation`

#### `04_clean_BNPL_intention_to_use.ipynb`

- **Input**: `../1_datasets/raw_data/BNPL Intention to use.xlsx` (IIM Lucknow
  survey data)
- **Purpose**: Processes survey responses from 226 young shoppers on BNPL
  adoption intentions
- **Processing**:
  - Handles Likert-scale responses for behavioral constructs
  - Validates data types and missing values
  - Preserves coded headers (FL1, PE3, etc.) for behavioral analysis
- **Output**: `../1_datasets/reference/BNPL_intention_to_use_cleaned.csv`
- **Use Case**: Exploratory analysis of attitudes and intentions (NOT for
  modeling due to lack of outcome labels)

#### `05_clean_FRBNY-SCE-Credit-Access-complete_microdata.ipynb`

- **Input**: `../1_datasets/raw_data/FRBNY-SCE-Credit-Access-complete_microdata.xlsx`
  (Federal Reserve Bank of New York SCE Credit Access microdata)
- **Purpose**: Brief overview notebook for SCE Credit Access microdata cleaning
- **Use Case**: Introduction to the more comprehensive Python script below

### Python Scripts

#### `clean_FRBNY_SCE_microdata.py`

- **Input**: `../1_datasets/raw_data/FRBNY-SCE-Credit-Access-complete_microdata.xlsx`
  (Federal Reserve Bank of New York SCE Credit Access microdata)
- **Purpose**: Comprehensive cleaning of Federal Reserve Bank of New York
  Survey of Consumer Expectations (SCE) Credit Access microdata (2013-2017)
- **Processing**:
  - Extracts column names from second row and data from third row onwards
  - Removes empty rows and columns
  - Cleans column names (spaces to underscores, removes special characters)
  - Renames columns using comprehensive mapping
    (e.g., `userid` → `respondent_id`, `n1_1` → `has_credit_card`)
  - Handles credit product ownership, balances, applications, and denial reasons
- **Output**: `../1_datasets/processed_datasets/FRBNY_SCE_Credit_Access_cleaned.csv`
- **Use Case**: Individual-level credit access patterns and borrowing behavior
  analysis

#### `create_complete_data.py`

- **Input**: `../1_datasets/processed_datasets/FRBNY_SCE_Credit_Access_cleaned.csv`
- **Purpose**: Creates a subset of the SCE data with only complete columns
  (no missing values)
- **Processing**:
  - Identifies columns with no missing values
  - Creates subset with only complete columns
  - Removes completely empty rows
- **Output**: `../1_datasets/processed_datasets/FRBNY_SCE_Credit_Access_complete_columns.csv`
- **Use Case**: Provides a clean dataset for modeling when complete cases are
  required

## 📁 Output Structure

### Processed Datasets (for modeling)

- `afdr_cleaned.csv` - Traditional loan volume data
- `BNPL_cleaned.csv` - BNPL user profiles and behavior
- `FRBNY_SCE_Credit_Access_cleaned.csv` - Credit access survey data
- `FRBNY_SCE_Credit_Access_complete_columns.csv` - Complete cases subsets

### Reference Datasets (for exploration)

- `afdr_charts_cleaned.csv` - Historical loan statistics
- `BNPL_intention_to_use_cleaned.csv` - BNPL adoption intentions

## 🔄 Data Flow

```mermaid
Raw Data → Cleaning Scripts → Processed Datasets → Analysis
     ↓
Reference Datasets (for context)
```

## 🎯 Key Features

- **Consistent naming conventions** across all datasets
- **Proper data type handling** (numeric, categorical)
- **Missing value management** (filling, removal, or flagging)
- **Duplicate detection and removal**
- **Comprehensive documentation** of transformations
- **Separation of modeling vs. reference datasets**
