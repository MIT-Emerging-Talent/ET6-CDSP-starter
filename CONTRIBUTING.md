# Contributing Guidelines

Welcome! We're excited you're here and want to contribute to
the **Emerging Talent 6 Collaborative Data Science Project (CDSP)**.
 This guide outlines how to set up the repository, what tools you need, and how
to collaborate effectively.

---

## 🚀 Getting Started

To contribute to this project, follow these steps to set up your environment locally:

### 1. Clone the Repository

```bash
git clone https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-08-repo.git
cd ET6-CDSP-group-08-repo.git
```

### 2. Install Required Packages

Install all required Python packages using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

> If you're using `conda`, you can create an environment with:  
> `conda create --name et6-cdsp python=3.10`  
> Then:  
> `conda activate et6-cdsp`  
> `pip install -r requirements.txt`

---

## 🧰 Tools & Environment

This project primarily uses the following tools:

- **Python 3.10+**
- **Jupyter Notebook / JupyterLab** (for interactive data exploration)
- **pandas, numpy, matplotlib, seaborn, scikit-learn** (core data science libraries)
- **Git** for version control
- **GitHub Project Boards** for task tracking

Optional tools:

- **VS Code** or another IDE with Python support  
- **Black** or **Flake8** for code formatting and linting

---

## 📂 Folder Structure

Refer to the `README.md` and `guide.md` for an overview of the directory layout.
Please place files in the correct folders, and link across scripts and notebooks
clearly.

> Example: If you use a cleaned dataset from `/2_data_preparation`,
mention that in your script or notebook in `/3_data_exploration`.

---

## 🔄 Workflow Guidelines

To ensure smooth collaboration:

### 1. Create a Branch

Always work on a new branch based on `main`:

```bash
git checkout main
git pull
git checkout -b your-feature-name
```

### 2. Make Meaningful Commits

- Commit early and often.  
- Use clear, descriptive messages like `Cleaned null values from survey dataset`.

### 3. Push and Open a Pull Request (PR)

Once your work is ready:

```bash
git push origin your-feature-name
```

Then go to GitHub and **open a pull request** (PR) against the `main` branch.

### 4. PR Review Policy

> **Every pull request must be reviewed by**
> **at least one team member before being merged.**

- Request a reviewer on your team.  
- Add a short description of what you did and what to look for in the review.  
- Only merge after approval.

---

## 📓 Documentation

- Keep notebooks and scripts clearly documented with comments and markdown cells.
- Update related `README.md` files in relevant folders
  whenever you add or change content.  
- Avoid vague file names like `final2_updated.ipynb`. Use names like `explore_survey_responses.ipynb`.

---

## 🔁 Retrospectives & Communication

- Use the `/collaboration` folder to log retrospectives at the end of each milestone.
- Document changes in team strategy, feedback, or lessons learned.

---

## 🧠 General Tips for Data Science Projects

To keep your work clean, reproducible, and team-friendly, keep these best
practices in mind:

- **Reproducibility is critical**: Others should be able to run your code
  without having to guess file paths, dependencies, or assumptions.
- **Clean as you go**: Document and structure your data cleaning steps clearly.
  Don't overwrite raw data — save processed versions separately.
- **Keep it modular**: Break your work into logical steps or scripts
  (e.g., preparation, exploration, modeling, visualization).
- **Use markdown and comments generously**: Explain what you’re doing
  and why — not just how.
- **Version control your data** (if feasible): Track changes to processed
  data files using DVC or manual versioning.
- **Test your pipeline**: Before committing code, make sure it runs from
  start to finish on a clean setup.
- **Avoid duplication**: Reuse functions or code snippets via helper scripts
  rather than copying and pasting cells.
- **Respect notebook hygiene**: Restart and run all cells before committing.
  Avoid leaving out-of-order execution numbers.
- **Cross-reference files**: If your script relies on output from another,
  state that clearly with file paths and purpose.
- **Ask for help early**: Data science is collaborative — if you're stuck or
  unsure, open an issue or post in the team chat.

---

Thank you for helping us build a clear, reproducible,
and collaborative data science project!
