# Data Exploration

This exploration is based on the
[`cleaned_data.csv`](../1_datasets/final_data_with_scripts/cleaned_data.csv)
file, which contains the final cleaned version of the supply chain dataset. The
file is located in the `1_datasets/final_data_with_scripts/` directory of the
repository. The purpose of this phase is to become familiar with the structure,
quality, and general characteristics of the data before proceeding to more
rigorous analysis or modeling. Importantly, this stage is observational: it
involves visualizing and describing the data without applying machine learning
algorithms or conducting statistical inference.

All notebooks and scripts in this folder are designed to support transparency
and reproducibility. In keeping with open research principles, no original
dataset is modified at any point in this process. Instead, we rely on reading
data as-is and using Python tools to observe patterns, distributions, and any
early indicators of trends or data quality issues.

---

## Summary

### Dataset Explored

The notebook works with a dataset named `supply_chain_data.csv`, located in the
`0_datasets` directory. This dataset is assumed to contain structured
information relevant to supply chain operations — such as order history,
delivery performance, stock levels, supplier information, or similar features,
depending on the context of the broader project.

### Purpose

The aim of this notebook is to conduct an initial exploratory data analysis
(EDA) on the supply chain dataset. This helps establish a baseline understanding
of the dataset's contents and structure. Such understanding is crucial for
guiding subsequent decisions about data preprocessing, feature engineering, or
selecting appropriate analytical methods.

### Activities Performed

- **Data Loading**: The dataset is loaded into memory using standard Python
  tools, such as pandas, without modifying the source file. All exploration is
  done in-memory to preserve data integrity.

- **Descriptive Statistics**: Basic statistics are computed to understand
  central tendencies, variability, and data completeness. This includes
  examining the mean, median, standard deviation, minimum and maximum values,
  and missing data counts.

- **Visual Exploration**: Several types of plots are generated to provide visual
  context:

  - Histograms to show the distribution of numerical features
  - Box plots to detect outliers and compare distributions across groups
  - Time series plots for temporal trends if applicable
  - Correlation heatmaps to reveal linear relationships between numerical
    variables

- **Qualitative Observations**: Based on visual and statistical cues, the
  notebook highlights potential anomalies, trends, or areas that warrant deeper
  investigation in later stages. For instance, spikes in order delays or strong
  correlations between supplier regions and product categories might be flagged.

### What This Notebook Does *Not* Do

- No inferential statistics are performed. This means the notebook does not
  include hypothesis testing, confidence intervals, or p-values.

- No machine learning models are built or applied. Predictive analysis and
  pattern recognition through algorithms are deferred to later stages of the
  project.

- No transformations are written back to the original dataset. The integrity of
  files in `0_datasets` remains untouched, ensuring full reproducibility by any
  third party who wishes to clone and rerun the repository.

---

## Guidelines and Best Practices

The purpose of exploratory data analysis at this stage is not to reach
conclusions but to ask better questions. It is a space for curiosity — for
identifying what the data might be telling us, and just as importantly, what it
is not.

Please keep the following in mind:

- **Do not alter the original dataset**. Any data transformation or filtering
  should occur within the notebook and should not overwrite source files. This
  maintains transparency and allows others to reproduce your findings exactly.

- **Avoid jumping into analysis too early**. Inferential statistics, machine
  learning models, or attempts at causal reasoning should not be part of this
  folder’s scope. That work belongs in later stages of the project pipeline.

- **Document your observations**. As you create plots and statistics, include
  markdown commentary that explains what you see. These insights can become
  useful hypotheses or directions for future analysis.
