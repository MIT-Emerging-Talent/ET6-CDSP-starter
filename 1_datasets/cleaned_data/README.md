# 🧹 Cleaned Data

This folder contains cleaned versions of the raw datasets used in our project.

Each file here has undergone basic preprocessing steps such as:

- Removing regional aggregates and keeping only countries
- Standardizing column names
- Converting country names to ISO 3-letter codes
- Dropping irrelevant columns
- Filtering out years we don't use in our analysis

---

## 📁 Files

| File Name                           | Based on Raw File                    | Description                                      |
|------------------------------------|--------------------------------------|--------------------------------------------------|
| `math_proficiency.cleaned.csv`     | `minimum_proficiency.raw.csv`        | Cleaned math proficiency data (2019, 2023 only) |
| `gov_spending.cleaned.csv`         | `gov_expending.raw.csv`              | Cleaned gov education spending data             |
| `completion_rate.cleaned.csv`      | `completion_rate.raw.csv`            | Cleaned primary completion rates                |
| `out_of_school.cleaned.csv`        | `out_of_school.raw.csv`              | Cleaned out-of-school rates                     |
| `trained_teacher_ratio.cleaned.csv`| `pupil_teacher_ratio.raw.csv`        | Cleaned teacher quality data                    |
| `digital_connectivity.cleaned.csv` | `School-Age-Digital-Connectivity...` | Filtered for primary level + standardized ISO   |
| `school_closure.cleaned.csv`       | `duration-of-school-closures.raw...` | Filtered, summarized school closure durations   |

---

## ✅ Purpose

The cleaned files are used as input to the final merging process, where we combine all variables into a single dataset:  
📄 `datasets/final_dataset.csv`

These files ensure consistent structure and comparability across countries and years before modeling.

---

## 📌 Notes

- Cleaning was performed using the script: `scripts/data_cleaning_script.ipynb`
- No imputation or interpolation was applied — missing values are retained
- All files use ISO 3-letter country codes (`ISO`) and standard column names
