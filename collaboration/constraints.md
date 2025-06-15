<!-- this template is for inspiration, feel free to change it however you like! -->

# Constraints

Some boundaries around our project.

## 1. External

Constraints coming from the outside that our team has no control over:

### 1.1. Project deadlines & milestones

> 1. The project must be completed within the assigned timeline.
> 2. The project is divided into milestones, each will have a deadline that we are
> required to meet it.
> 3. TODO: find the deadlines.

### 1.2. Dataset availability

> We are limited to publicly available or client-provided datasets.

### 1.3. Data privacy & compliance

> We must adhere to data privacy laws (e.g., GDPR)
  and avoid using any personally identifiable information (PII) unless **anonymized**.

### 1.4. Hardware limitations

> We are using our personal laptops with limited processing power and memory
  (e.g., no access to GPUs or high-performance computing).

### 1.5. Internet connectivity

> The project may be affected by slow or unstable internet connections when
 downloading data or accessing cloud services.

## Internal: Involuntary

## 2. Internal: Involuntary

<!--
  constraints that come from within your team, and you have no control over:
  - each of your individual skill levels
  - amount of time available to work on the project
-->
### 2.1. Team Skill Set

> The collective expertise and experience of the team members in specific areas (e.g.,\
machine learning algorithms,  data engineering, domain knowledge, specific tools)
> inherently limit the project's scope and complexity.\
> A lack of expertise in a critical area might necessitate simplification
> or external help.

### 2.2. Time Availability

> The total person-hours the team can realistically commit to the project,
> considering other responsibilities,holidays, and potential   unforeseen absences,
> acts as a fundamental constraint on the amount of work that can be accomplished.

### 2.3. Team Size and Structure

> The number of people on the team and how they are organized can impact
> communication overhead, coordination efforts, and the ability to parallelize tasks.

### 2.4. Prior Knowledge and Context

> The team's existing understanding of the problem domain, the data, and relevant
> prior work can influence the project's starting point and pace.\
> Gaps in knowledge may require additional time for research and learning.

## 3. Internal: Voluntary

### 3.1. Coding Standards and Style Guides

**To ensure consistency and maintainability in our project code.**\
**We should agree on setting up the following constraints:**

> 1. Coding conventions.
> 2. Documentation standards.
> 3. Version control practices (e.g., Git workflow)

### 3.2. Development Methodology

> We will have the following approch options:
> **[ Agile, Scrum, Kanban]**

### 3.3. Code Review Process

> Implementing mandatory code reviews with
a defined checklist ensures code quality but adds time to the development cycle.

### 3.4. Scope Limitations

> Deliberately deciding *not* to pursue certain features, analyses, or model complexities,
even if technically feasible, to ensure focus and timely completion of core objectives.

### 3.5. Testing Strategy

Defining the required level of unit testing, integration testing,
or validation procedures beyond any external requirements.

### 3.6. Technology stack

> We are required to use specific tools such as Python,\
> Jupyter Notebooks, google colab, and libraries like pandas, matplotlib,
  scikit-learn, or TensorFlow.

| **Framework / Tool** | **Intended Usage** |
| -------------------- | -----------------------------------|
| **Python**                  | Primary programming language            |
| **Google Colab**            | Cloud-based environment for development |
| **pandas**                  | Data manipulation and preprocessing |
| **NumPy**                   | Numerical computing and array operations|
| **scikit-learn**            | Building and evaluating machine learning models|
| **Matplotlib**              | Data visualization and EDA|
| **TensorFlow / PyTorch**    | (If needed) Deep learning model development |
| **SQL (e.g., SQLite/MySQL)**| Data querying and manipulation from relational databases|
| **Git + GitHub**            | Version control, collaboration, and code repo managment|
| **OpenCV / PIL**            | Image processing (if working with visual data) |
| **scipy.stats / statsmodels** | Statistical analysis and hypothesis testing|
| **MLflow** | Experiment tracking and model management  |

### 3.7. Submission requirements

```json
{
  "milestones": [
    {
      "name": "0_domain_study",
      "deliverables": [
        "Domain background report summarizing context and goals",
        "List of key questions or hypotheses to guide the project",
        "Initial stakeholder requirements (if applicable)"
      ]
    },
    {
      "name": "1_datasets",
      "deliverables": [
        "Dataset inventory (sources, size, format, licenses)",
        "Data collection script(s) or links to datasets",
        "Data dictionary describing features/columns",
        "Assessment of data quality and limitations"
      ]
    },
    {
      "name": "2_data_preparation",
      "deliverables": [
        "Cleaned and preprocessed dataset file (e.g., CSV or parquet)",
        "Data cleaning notebook or script (handling missing values, encoding, scaling)",
        "Updated data dictionary reflecting changes"
      ]
    },
    {
      "name": "3_data_exploration",
      "deliverables": [
        "Exploratory Data Analysis (EDA) notebook with visualizations and statistics",
        "Summary of insights, correlations, and anomalies",
        "Initial hypothesis validation (if applicable)"
      ]
    },
    {
      "name": "4_data_analysis",
      "deliverables": [
        "Modeling notebook(s) or pipeline script",
        "Model performance report (e.g., accuracy, precision, recall, RMSE)",
        "Feature importance or model interpretability analysis",
        "Experiment tracking records or logs (e.g., MLflow)"
      ]
    },
    {
      "name": "5_communication_strategy",
      "deliverables": [
        "Draft of data story (key insights and visuals)",
        "Slide deck outline or wireframe for final presentation",
        "Plan for communicating results to technical and non-technical audiences"
      ]
    },
    {
      "name": "6_final_presentation",
      "deliverables": [
        "Final slide deck or report",
        "Live or recorded presentation",
        "GitHub repository with documentation and code",
        "Optional: Dashboard or web app showcasing results"
      ]
    }
  ]
}
```
