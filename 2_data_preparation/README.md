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

## UN Comtrade data preparation script

1. **Input dataset**  
   - **File**: `../1_datasets/raw_data/UN_Comtrade_imports_dataset_raw.xlsx`  
   - **Loaded as**: `raw_df` (and copied to `df`)

2. **Processing steps**  
   - **Drop unneeded columns**: Drop unneeded columns: a long list of technical
  fields (e.g. frequency codes, partner metadata, alternative quantity fields,
   legacy flags, etc.) is removed in one go.
   - **Rename columns**:

     | original       | new name               |
     | -------------- | ---------------------- |
     | `refYear`      | `Year`                 |
     | `\tISO_Code`   | `Country_Code`         |
     | `reporterDesc` | `Country`              |
     | `cmdCode`      | `Product_Code`         |
     | `cmdDesc`      | `Product_Description`  |
     | `netWgt`       | `Net_Weight_kg`        |
     | `primaryValue` | `Value_USD`            |

   - **Handle missing values**: fill missing `Net_Weight_kg`
    entries with the column mean.  
   - **Inspect**: prints `.shape`, `.info()`, `.isna().sum()`,
    duplicate counts, and random samples to verify cleaning.

  **Output dataset**  

- **Cleaned data** written to Excel at:  

`../1_datasets/cleaned_data/UN_comtrade_clean_dataset.xlsx`

- No other files are created or saved under `/1_datasets`.
