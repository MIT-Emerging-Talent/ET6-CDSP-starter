# Data Exploration

<!-- markdownlint-disable MD031 MD033 MD004 MD009 MD013 MD045 MD024 -->

## UN Comtrade data preparation script

### 1. **Input dataset**  

    File:../1_datasets/cleaned_data/UN_comtrade_clean_dataset.xlsx

### 2. Exploratory Data Analysis (EDA) Steps

- Load the cleaned dataset from GitHub

- Display general dataset information and description

- Generate descriptive statistics for numeric columns:
  
   'Mean, standard deviation, minimum, and maximum values'

- Identify potential outliers in relevant columns using simple statistical
   boxplot charts

- Analyze relationships between key variables

- Generate initial visualizations for selected conflict-affected countries
  (e.g., Sudan, Palestine, Ukraine) to highlight trade patterns and potential correlations.

### 3. Key Questions

- Do you have the right data?

The dataset contains relevant trade information; however, it is not
 comprehensive enough to address all aspects of our research questions.

- Do you need other data?

Yes, we require additional data on conflict events such as their dates,
intensity, and duration to provide a more complete analysis.

- Do you have the right question?
  
The research question is well-formulated, but to address it thoroughly, we need
 to collect additional data.

## On-Grid data preparation script

### 1. Input dataset

    File: ../1_datasets/cleaned_data/IRENA_ONGRIDStats.cleaned.xlsx  

### 2. Exploratory Data Analysis (EDA) Steps

- Load Dataset
  - Loaded from GitHub using pandas.read_excel() with openpyxl engine.

- General Information
  - Used .info() and .describe() to inspect structure, types, nulls, and distributions.

- Descriptive Statistics
  - Analyzed Electricity Installed Capacity (MW):  
    - Mean: Provided insight into average installed capacity
    - Std deviation: Identified variance across countries and years
    - Min/Max: Helped identify extreme values (potential outliers)

- Missing Values
Checked for nulls using df.isnull().sum() — no major issues found.

- Outlier Detection
  - Used boxplots on:
    - Electricity Installed Capacity (MW) by RE or Non-RE

- Key Variable Relationships
  - Compared capacity trends by:
    - Year vs Conflict_Status
    - Producer Type (On-grid/Off-grid) vs Conflict_Status
    - Visualized using seaborn lineplot and countplot

- Initial Country Visuals
  - Filtered for conflict-affected countries (e.g., Sudan, Palestine, Ukraine)
  - Plotted solar vs other renewables over time
  - Showed variation in growth rates and technology mix across countries

### 3. Key Questions

- **Do you have the right data?**  
 Partially. The dataset provides reliable installed capacity data across countries, years, and technology types, especially for renewable energy trends.
- **Do you need other data?**  
 Yes. To fully understand the role of solar adoption in conflict zones, we need:
  - Conflict event timelines, intensity & frequency (e.g., ACLED or UCDP)
  - Government energy policies during conflict years
  - Grid reliability and access metrics
- **Do you have the right question?**
 The guiding question — “How does solar capacity evolve in conflict-affected countries, and does conflict hinder or encourage adoption?” — is solid.  
But to answer it robustly, we must merge energy data with conflict datasets to measure correlation or causality, not just trend lines.
