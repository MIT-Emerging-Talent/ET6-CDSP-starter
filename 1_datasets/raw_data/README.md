# 📊 Project Data Overview

This folder contains the raw datasets used to investigate how the COVID-19 pandemic affected math learning outcomes in primary education.  
The majority of the data was collected from **UNESCO's UIS (Institute for Statistics)** open data platform, ensuring internationally comparable indicators.

We also included supporting datasets from **UNICEF** and the **World Bank** to add context and enrich our analysis.

---

## 🔹 Datasets Summary

| File Name                                 | Description                                                                                  | Source           | Format | Years Used   |
|------------------------------------------|----------------------------------------------------------------------------------------------|------------------|--------|--------------|
| `minimum_proficiency.raw.csv`            | % of students at the end of primary school achieving minimum proficiency in mathematics       | UNESCO UIS       | CSV    | 2019, 2023   |
| `completion_rate.raw.csv`                | Completion rate of primary education (both sexes)                                            | UNESCO UIS       | CSV    | 2019–2023    |
| `gov_expending.raw.csv`                  | Government expenditure on education as % of GDP                                              | UNESCO UIS       | CSV    | 2019–2023    |
| `out_of_school.raw.csv`                  | % of primary-aged children not attending school                                              | UNESCO UIS       | CSV    | 2019–2023    |
| `pupil_teacher_ratio.raw.csv`            | Pupil-to-trained-teacher ratio (primary level)                                               | UNESCO UIS       | CSV    | 2019–2023    |
| `duration-of-school-closures.raw.xlsx`   | Number of days schools were fully or partially closed due to COVID-19                       | UNESCO SDG Tracker | Excel  | 2020–2022    |
| `School-Age-Digital-Connectivity.raw.xlsx` | Estimated digital connectivity access for school-age children                             | UNICEF           | Excel  | 2010–2020  |
| `worldbank_classification.csv`           | World Bank classification of countries by income group (Low, LM, UM, High)                  | World Bank       | CSV    | 2023         |

---

## ⚠️ Notes

- Raw files are **not modified** — we preserve them to ensure transparency and reproducibility.
- All data cleaning and merging steps are performed in Python (see `scripts/data_cleaning_script.ipynb`).
- The final processed dataset is saved as `data/final_dataset.csv`.
