# Data Preparation

Adjusted Project Research Question:  
**How have armed conflicts over the past 15 years influenced the deployment, capacity utilization, and household consumption of solar photovoltaic systems—both environmentally and socially—in conflict-affected communities?**

These datasets provides a strong foundation for analyzing **solar energy** trends in *conflict-affected* countries. It helps us compare the **deployment** and **utilization** of *renewable sources*—particularly **solar**—between *conflict* and *non-conflict* areas, and track shifts between **on-grid** and **off-grid** solutions. Increased *off-grid* adoption may signal a response to *grid damage* or *instability*. Combined with **UN Comtrade** trade data, we can also observe how *conflicts* influence the **import** of *solar technologies*, offering further insight into how communities *adapt to energy disruptions*.

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
