# Data Mavericks
<!-- markdownlint-disable MD013 -->

Welcome to **Data Mavericks** – Group 13 of the MIT Emerging Talent Certificate Program.  
This repository is our shared workspace for tackling data-science challenges: gathering and cleaning datasets, experimenting with analytical methods, and turning results into clear insights. Our specific research angle is still being finalized, but we expect to dive into finance-focused datasets and problems.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [How to Contribute](#how-to-contribute)
3. [Project Goals](#project-goals)
4. [Team Composition](#team-composition)
5. [Repository Structure](#repository-structure)
6. [Setup and Usage](#setup-and-usage)
7. [Roles and Responsibilities](#roles-and-responsibilities)
8. [Task Breakdown](#task-breakdown)
9. [Definition of Done](#definition-of-done)
10. [Tools and Technologies](#tools-and-technologies)
11. [Milestones](#milestones)
12. [License](#license)

---

## Project Overview

This repository serves as the hub for our group collaboration, where we:  

1. **Collaborate on data-science projects**: Explore real-world datasets together to sharpen our analytical and coding skills.  
2. **Learn from each other**: Share knowledge, resources, and tips to help everyone grow.  
3. **Code & notebook reviews**: Provide constructive feedback to improve quality, reproducibility, and best practices.  
4. **Tell the story with data**: Turn findings into clear visualizations and concise write-ups.  
5. **Build community**: Strengthen our team spirit as we progress through the MIT Emerging Talent Program.

---

## How to Contribute

We encourage every team member to jump in. You can contribute by:

1. **Picking up tasks** – Check the [Task Breakdown](#task-breakdown) for your assignments or claim an open issue.
2. **Setting up locally** – Follow [Setup and Usage](#setup-and-usage) to install dependencies and run tests.
3. **Working in a feature branch** – Name it `<firstname>/<short_description_snake_case>` (e.g. `sukhrob/data_cleaning_pipeline`).
4. **Adding code or notebooks** – Keep notebooks reproducible (clean outputs, random seeds fixed) and adhere to our lint rules.
5. **Submitting a pull request** – Link any related issue, ensure CI passes, and confirm your work meets the [Definition of Done](#definition-of-done).
6. **Reviewing peers’ PRs** – Leave constructive comments, suggest improvements, and approve when ready.
7. **Opening issues or discussions** – Use issue templates for bugs, ideas, or dataset proposals so we can track them transparently.

---

## Project Goals

1. Master professional GitHub workflows (branches, PRs, reviews, CI checks) for reproducible analytics.
2. Build teamwork and collaboration skills by pairing on notebooks, code, and documentation.
3. Explore the full data-science lifecycle—data collection, cleaning, modelling, and validation—on finance-related datasets.
4. Apply advanced Python libraries (pandas, NumPy, scikit-learn, matplotlib/plotly, pytest) to create robust analysis pipelines, rich visualizations, and a comprehensive unit-test suite.
5. Communicate insights clearly through well-designed visuals and concise, audience-appropriate write-ups.

---

## Team Composition

| **Name**              | **GitHub** | **Time Zone** |
|-----------------------|-----------|---------------|
| Ahmed Elhassan        | [Goutbi](https://github.com/Goutbi) | GMT +4 |
| Anass Ziadah          | [ziadahanass](https://github.com/ziadahanass) | GMT +3 |
| Clement Mugisha       | [Bikaze](https://github.com/Bikaze) | GMT +2 |
| Emre Biyik            | [emrebiyik](https://github.com/emrebiyik) | GMT +2 |
| Mustafa Mangal        | [Mustafa-Mangal](https://github.com/Mustafa-Mangal) | GMT +2 |
| Sukhrob Muborakshoev  | [suhrobmuboraksho](https://github.com/suhrobmuboraksho) | GMT -7 |

---

## Repository Structure

<details>
<summary>Click to expand/collapse the repository structure</summary>

```plaintext
.
│   .gitignore
│   .ls-lint.yml
│   .markdownlint.yml
│   CONTRIBUTING.md
│   LICENSE
│   README.md
│   guide.md
│
├───.github
│   ├───ISSUE_TEMPLATE
│   └───workflows
├───.vscode
│
├───0_domain_study
├───1_datasets
├───2_data_preparation
├───3_data_exploration
├───4_data_analysis
├───5_communication_strategy
├───6_final_presentation
│
├───collaboration
└───notes 
```

</details>

---

## Setup and Usage

### Prerequisites

- **Python 3.9 +**
- **Git**
- A code editor (VS Code, PyCharm, etc.)

### 1 · Clone the repository

```bash
git clone https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-13-repo.git
cd ET6-CDSP-group-13-repo
```

### 2 · Create and activate a virtual environment

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 3 · Install project dependencies

```bash
pip install -r requirements.txt          # add this file when you freeze libs
pre-commit install                       # optional: auto-lint on every commit
```

### 4 · Run the test suite

```bash
pytest -q
```

### 5 · (If needed) download large datasets

```bash
# Example: pull data versioned with DVC or Git LFS
dvc pull                           # or: git lfs pull
```

### 6 · Launch Jupyter Lab for notebooks

```bash
jupyter lab
```

> **Tip:** keep notebooks in a dedicated `notebooks/` folder to minimise merge conflicts.

---

## Roles and Responsibilities

### Shared Role

**Data Scientist & Reviewer**

### Core Responsibilities (everyone)

- **Acquire and prepare data** – source datasets, clean them, and document provenance.
- **Analyze and model** – explore patterns, build statistical / ML models, and validate results.
- **Create artifacts** – code modules, notebooks, visualizations, and concise reports.
- **Review and improve** – give constructive feedback on peers’ pull requests and notebooks.
- **Maintain project hygiene** – follow branch naming, pass CI checks, and update documentation.

### Team Members

- Ahmed Elhassan  
- Anass Ziadah  
- Clement Mugisha  
- Emre Biyik  
- Mustafa Mangal  
- Sukhrob Muborakshoev

---

## Task Breakdown

### Week of 3 – 16 June 2025 · Problem Identification

**Goal:** Each team member drafts **one finance-data-science project idea** to discuss in this week’s meeting.  
Include ⬇️

1. Problem statement (1–2 sentences)  
2. Potential dataset(s) / data source  
3. Expected value or insight  
4. Sketch of analysis approach (very high-level)

| Team Member          | Deliverable                       | Due (before meeting) |
|----------------------|-----------------------------------|----------------------|
| Ahmed Elhassan       | Project-idea brief (≤1 page)      | 14 Jun 2025 |
| Anass Ziadah         | Project-idea brief (≤1 page)      | 14 Jun 2025 |
| Clement Mugisha      | Project-idea brief (≤1 page)      | 14 Jun 2025 |
| Emre Biyik           | Project-idea brief (≤1 page)      | 14 Jun 2025 |
| Mustafa Mangal       | Project-idea brief (≤1 page)      | 14 Jun 2025 |
| Sukhrob Muborakshoev | Project-idea brief (≤1 page)      | 14 Jun 2025 |

> **Tip:** Save your idea as `0_domain_study/ideas/<firstname>/idea.md` (or a short notebook) in a feature branch named `firstname/project_idea`.

---

## Definition of Done

A task is complete when:

1. Code modules and notebooks pass automated tests, lint checks, and receive approval in code review.
2. Collaboration documents are reviewed and approved.
3. CI/CD pipelines run successfully.

---

## Tools and Technologies

- **Version Control:** Git + GitHub
- **Project Management:** GitHub Issues & Project boards
- **Languages / Libraries**
  - Python 3.9+
  - pandas · NumPy · scikit-learn
  - matplotlib / Plotly (visualization)
- **Environment:** Jupyter Lab · virtualenv
- **Testing:** pytest
- **CI/CD:** GitHub Actions (lint, unit tests)
- **Documentation:** Markdown (MkDocs optional for future docs site)

---

## Milestones

| Phase | Date Range (2025) |
|-------|------------------|
| Cross-Cultural Collaboration | **May 27 – June 2** |
| Problem Identification | **June 3 – June 16** |
| Data Collection | **June 17 – June 30** |
| Data Analysis | **July 1 – July 21** |
| Communicating Results | **July 22 – August 11** |
| Final Presentation | **August 12 – August 24** |

---

## License

This project is licensed under the [MIT License](LICENSE).
