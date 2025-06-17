# Data Mavericks
<!-- markdownlint-disable MD013 -->

Welcome to **Data Mavericks** – Group 13 of the MIT Emerging Talent Certificate
Program. This repository is our shared workspace for tackling data-science
challenges: gathering and cleaning datasets, experimenting with analytical
methods, and turning results into clear insights.

Our final research direction focuses on how **cryptocurrency can foster
financial inclusion in crisis-affected countries**. This domain emerged from
our diverse team’s lived experience, with several of us witnessing firsthand
how crypto enabled financial access during times of banking collapse or
instability. This topic intersects data, finance, and humanitarian value.

---

## Table of Contents

- [Data Mavericks](#data-mavericks)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [How to Contribute](#how-to-contribute)
  - [Project Goals](#project-goals)
  - [Team Composition](#team-composition)
  - [Repository Structure](#repository-structure)
    - [Repository Structure (Expand to view)](#repository-structure-expand-to-view)
  - [Setup and Usage](#setup-and-usage)
    - [Prerequisites](#prerequisites)
    - [1 · Clone the repository](#1--clone-the-repository)
    - [2 · Create and activate a virtual environment](#2--create-and-activate-a-virtual-environment)
    - [3 · Install project dependencies](#3--install-project-dependencies)
    - [4 · Run the test suite](#4--run-the-test-suite)
    - [5 · Download datasets (if needed)](#5--download-datasets-if-needed)
    - [6 · Launch Jupyter Lab](#6--launch-jupyter-lab)
  - [Roles and Responsibilities](#roles-and-responsibilities)
    - [Core Responsibilities (everyone)](#core-responsibilities-everyone)
  - [Task Breakdown](#task-breakdown)
    - [Week of 17–23 June 2025 · Data Research and Planning](#week-of-1723-june-2025--data-research-and-planning)
  - [Definition of Done](#definition-of-done)
  - [Tools and Technologies](#tools-and-technologies)
  - [Milestones](#milestones)
  - [License](#license)

---

## Project Overview

This repository serves as the hub for our group collaboration, where we:

1. **Collaborate on data-science projects**: Explore real-world datasets
   together to sharpen our analytical and coding skills.  
2. **Learn from each other**: Share knowledge, resources, and tips to help
   everyone grow.  
3. **Code & notebook reviews**: Provide constructive feedback to improve
   quality, reproducibility, and best practices.  
4. **Tell the story with data**: Turn findings into clear visualizations and
   concise write-ups.  
5. **Build community**: Strengthen our team spirit as we progress through the
   MIT Emerging Talent Program.  
6. **Focus Area**: Our project explores **the role of cryptocurrency in
   improving financial inclusion in countries affected by conflict or
   instability**. We aim to analyze public datasets and case studies where
   crypto use has replaced or supplemented traditional banking systems.

---

## How to Contribute

We encourage every team member to jump in. You can contribute by:

1. **Picking up tasks** – Check the [Task Breakdown](#task-breakdown) for your
   assignments or claim an open issue.  
2. **Setting up locally** – Follow [Setup and Usage](#setup-and-usage) to
   install dependencies and run tests.  
3. **Working in a feature branch** – Name it `<firstname>/<short_description>`
   (e.g. `sukhrob/data_cleaning_pipeline`).  
4. **Adding code or notebooks** – Keep notebooks reproducible (clean outputs,
   random seeds fixed) and adhere to our lint rules.  
5. **Submitting a pull request** – Link any related issue, ensure CI passes,
   and confirm your work meets the [Definition of Done](#definition-of-done).  
6. **Reviewing peers’ PRs** – Leave constructive comments, suggest improvements,
   and approve when ready.  
7. **Opening issues or discussions** – Use issue templates for bugs, ideas, or
   dataset proposals so we can track them transparently.

---

## Project Goals

1. Master professional GitHub workflows (branches, PRs, reviews, CI checks) for
   reproducible analytics.  
2. Build teamwork and collaboration skills by pairing on notebooks, code, and
   documentation.  
3. Explore the full data-science lifecycle—data collection, cleaning,
   modelling, and validation—on finance-related datasets.  
4. Apply advanced Python libraries (pandas, NumPy, scikit-learn,
   matplotlib/plotly, pytest) to create robust analysis pipelines, rich
   visualizations, and a comprehensive unit-test suite.  
5. Communicate insights clearly through well-designed visuals and concise,
   audience-appropriate write-ups.

---

## Team Composition

| **Name**              | **GitHub**                               | **Time Zone** |
|-----------------------|-------------------------------------------|---------------|
| Ahmed Elhassan        | [Goutbi](https://github.com/Goutbi)       | GMT +4        |
| Anass Ziadah          | [ziadahanass](https://github.com/ziadahanass) | GMT +3    |
| Clement Mugisha       | [Bikaze](https://github.com/Bikaze)       | GMT +2        |
| Emre Biyik            | [emrebiyik](https://github.com/emrebiyik) | GMT +2        |
| Mustafa Mangal        | [Mustafa-Mangal](https://github.com/Mustafa-Mangal) | GMT +2 |
| Sukhrob Muborakshoev  | [suhrobmuboraksho](https://github.com/suhrobmuboraksho) | GMT -7 |

---

## Repository Structure

### Repository Structure (Expand to view)

</pre>

```plaintext
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── .vscode/
├── 0_domain_study/
├── 1_datasets/
├── 2_data_preparation/
├── 3_data_exploration/
├── 4_data_analysis/
├── 5_communication_strategy/
├── 6_final_presentation/
├── collaboration/
├── notes/
├── .gitignore
├── .ls-lint.yml
├── .markdownlint.yml
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── guide.md
```

</details>

---

## Setup and Usage

### Prerequisites

- **Python 3.9+**
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
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\Activate.ps1  # Windows PowerShell
```

### 3 · Install project dependencies

```bash
pip install -r requirements.txt
pre-commit install
```

### 4 · Run the test suite

```bash
pytest -q
```

### 5 · Download datasets (if needed)

```bash
dvc pull
```

### 6 · Launch Jupyter Lab

```bash
jupyter lab
```

---

## Roles and Responsibilities

### Core Responsibilities (everyone)

- Acquire and prepare data
- Analyze and model
- Create code, notebooks, visuals, and reports
- Review peers’ work
- Follow repo hygiene and update docs

---

## Task Breakdown

### Week of 17–23 June 2025 · Data Research and Planning

**Goal:** Research relevant datasets that support our topic:
_The role of cryptocurrency in fostering financial inclusion in
crisis-affected countries._

| Team Member          | Task                                | Due Date    |
|----------------------|-------------------------------------|-------------|
| All members          | Research and summarize 1–2 datasets | 18 Jun 2025 |

We will meet **Tuesday after Evan’s workshop** to review findings.

> Save results to `0_domain_study/` as short `.md` files or notebooks.

---

## Definition of Done

A task is complete when:

1. Code/notebooks pass tests and lint checks  
2. Documents are peer-reviewed and approved  
3. CI/CD runs without errors

---

## Tools and Technologies

- Git + GitHub  
- Python 3.9+  
- pandas, NumPy, scikit-learn  
- matplotlib, Plotly  
- Jupyter Lab  
- pytest  
- GitHub Actions  
- Markdown docs

---

## Milestones

| Phase                        | Dates             |
|-----------------------------|-------------------|
| Collaboration               | May 27 – June 2   |
| Problem Identification      | June 3 – June 16  |
| Data Collection             | June 17 – June 30 |
| Data Analysis               | July 1 – July 21  |
| Communicating Results       | July 22 – Aug 11  |
| Final Presentation          | Aug 12 – Aug 24   |

---

## License

This project is licensed under the [MIT License](LICENSE).
