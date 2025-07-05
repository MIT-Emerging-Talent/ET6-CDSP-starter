# Data Exploration

This folder contains Jupyter notebooks for the exploratory data analysis (EDA)
of all processed datasets in the project. Each subfolder corresponds to a dataset
and contains:

- A Jupyter notebook (`explore_*.ipynb`) for EDA
- A `figures/` directory with generated visualizations and summary CSVs

The EDA follows the guidelines in `guide.md`: it focuses on descriptive
statistics, visualizations, and understanding the structure and patterns in the
data, without performing inferential statistics or machine learning.

---

## Contents

### 1. AFDR Cleaned Data (`afdr_cleaned/`)

- **Notebook:** `explore_afdr_cleaned.ipynb`
- **What it does:**
  - Loads the cleaned AFDR dataset with columns: Year, Quarter, All_Loan_Sizes,
    $1k–9k, $10k–24k, $25k–49k, $50k–99k, $100k–249k, $250k+.
  - Constructs a time index from `Year` and `Quarter` for time series analysis.
  - Generates:
    - Time series plots of total loan volume and by loan size category.
    - Pie chart of loan size distribution.
    - Correlation heatmap of loan size categories.
    - Boxplots, quarterly and yearly trends, and growth rates.
    - (If available) Analysis by loan characteristic.
  - Saves summary statistics and processed data.
- **Figures:** Saved in `afdr_cleaned/figures/` (e.g., overview visualizations,
  statistical analysis, characteristic breakdowns).

---

### 2. BNPL Cleaned Data (`BNPL_cleaned/`)

- **Notebook:** `explore_BNPL_cleaned.ipynb`
- **What it does:**
  - Loads the cleaned BNPL dataset.
  - Generates:
    - Histograms for all numeric columns.
    - Correlation heatmap.
    - Boxplots and barplots for financial stress and BNPL usage by
      over-indebtedness.
    - Grouped analysis by time (if `Year`/`Quarter` present).
  - Saves summary statistics and processed data.
- **Figures:** Saved in `BNPL_cleaned/figures/` (e.g., numeric distributions,
  correlation heatmap, stress/usage by indebtedness).

---

### 3. BNPL Intention to Use (`BNPL_intention_to_use_cleaned/`)

- **Notebook:** `explore_BNPL_intention_to_use_cleaned.ipynb`
- **What it does:**
  - Loads the cleaned survey dataset on intention to use BNPL.
  - Generates:
    - Histograms for Likert-scale survey items.
    - Correlation heatmap of survey items.
    - Grouped analysis and mean score distributions by construct (e.g., FL, PE,
      EE, etc.).
  - Saves summary statistics and processed data.
- **Figures:** Saved in `BNPL_intention_to_use_cleaned/figures/` (e.g., Likert
  histograms, mean score distributions, correlation heatmap).

---

### 4. FRBNY SCE Credit Access (`FRBNY_SCE_Credit_Access_cleaned/`)

- **Notebook:** `explore_FRBNY_SCE_Credit_Access_cleaned.ipynb`
- **What it does:**
  - Loads the cleaned FRBNY SCE Credit Access dataset.
  - Generates:
    - Histograms for all numeric columns.
    - Correlation heatmap.
    - Barplots for product ownership and respondent count by month.
    - Time series plots for numeric features and product ownership (if
      `Year`/`Quarter` present).
    - Grouped analysis by product.
  - Saves summary statistics and processed data.
- **Figures:** Saved in `FRBNY_SCE_Credit_Access_cleaned/figures/` (e.g.,
  numeric distributions, product ownership, time trends, correlation heatmap).

---

## How to Use

1. Navigate to the relevant subfolder.
2. Open and run the Jupyter notebook to reproduce the EDA and generate
   figures.
3. All outputs are saved in the corresponding `figures/` directory.

For more details on the EDA philosophy and best practices, see `guide.md`.
