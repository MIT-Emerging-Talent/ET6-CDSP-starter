# Data Preparation

## On-Grid Data Preparation Script

This script processes the **on-grid electricity data** from the IRENA dataset.

### Input

- **File**: [IRENA_Stats_extract_2025_H1_raw.xlsx](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-08-repo/blob/main/1_datasets/raw_data/IRENA_Stats_extract_2025_H1_raw.xlsx)
  - **Sheet**: `Country`
  - **Path**: `1_datasets/raw_data/`

### Process

- Added `Conflict_Status` column by filtering conflict-affected countries.
- Fills missing values in key columns
- Filtered out years according to project scope (2010 - 2024)
- Drops unused column `M49 code`

### Output

- **File**: `IRENA_ONGRIDStats.cleaned.xlsx`
  - **Sheet**: `Cleaned_OnGrid_Data`
  - **Path**: `1_datasets/cleaned_data/`
