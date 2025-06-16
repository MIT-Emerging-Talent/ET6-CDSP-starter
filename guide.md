# ET6 CDSP Starter

This repository provides a template and guidelines for the
**Emerging Talent 6 Collaborative Data Science Project (CDSP)**. It is
designed to support a reproducible workflow so that anyone can clone,
run, and verify your analysis from start to finish.

---

## Project Overview

The CDSP is a six‐milestone initiative where teams work together to
identify a research question, collect and analyze data, and communicate
findings. This repository’s structure follows those milestones and
encourages best practices in collaboration, version control, and
documentation.

Use this template to:

- Organize your files and code in a clear, consistent folder structure
- Maintain reproducibility so others can run your pipeline without issues
- Document team norms, communication plans, and milestone retrospectives
- Track tasks, issues, and pull requests through GitHub’s project boards

---

## Directory Structure

```text
/
├── README.md                   # Project overview and main instructions
├── guide.md                    # Detailed guide on using this template
├── /collaboration/             # Team norms, strategies, and retrospectives
├── /notes/                     # Shared resources and learning materials
├── /0_domain_study/            # Domain research and background
├── /1_datasets/                # Raw and processed datasets
├── /2_data_preparation/        # Scripts for cleaning and processing data
├── /3_data_exploration/        # Scripts for initial data understanding
├── /4_data_analysis/           # Scripts for in-depth analysis
├── /5_communication_strategy/  # Materials for communicating findings
└── /6_final_presentation/      # Final presentation materials

```

Below are some suggestions on how to use the folders/files in this repository,
but they're just suggestions! Your group should find a system that works for you

---

## 1. Cross-Cultural Collaboration

- Use `/collaboration` to document team norms (in `README.md`), collaboration
  strategies, project goals, and your milestone retrospectives. This folder is a
  living document — you should update it through the whole project.
- Use `/notes` to share useful resources: tools, tutorials, examples, or
  anything else that helps your team learn and work better.
- In the main `README.md`, write a short intro to your team and what you're
  hoping to study.
- Create a retrospective for this milestone in `/collaboration` using the
  template.

---

## 2. Problem Identification

- Use `/0_domain_study` to build a reference folder for your research domain. A
  new teammate should be able to catch up using this folder.
- Use `/0_domain_study/README.md` to organize your notes in `0_domain_study` so
  people don't have to read every single file to find what they need.
- In the main `README.md`, write a summary of your research question, relevant
  background, and why you think this is a meaningful problem to work on.
- Create a retrospective for this milestone in `/collaboration` using the
  template.

---

## 3. Data Collection

- Store **all datasets** (raw or processed) in `/1_datasets`. This folder is for
  data only — not code. (Unless you happen to have a dataset that's inside a
  `.py` file…)
- In `/1_datasets/README.md`, document each dataset: where it's from, how it was
  collected, how it connects to your research question, and any limitations or
  caveats.
- Use `/2_data_preparation` to keep all your cleaning, transformation, and prep
  scripts. These scripts should read data from `/1_datasets` and write new
  datasets back to that same folder.
- In `/2_data_preparation/README.md`, explain what each script does: which
  datasets it reads, what it does to them, and what outputs it creates.
- Use `/3_data_exploration` to explore, visualize, and get a feel for your
  datasets. This isn't the place for answering research questions — it's just to
  understand your data.
- In `/3_data_exploration/README.md`, summarize what each script/notebook
  explores, and which datasets it uses.
- In the main `README.md`, describe how you're modeling your research question
  with data, what datasets you're using, and how you prepared them.
- Create a retrospective for this milestone in `/collaboration` using the
  template.

---

## 4. Data Analysis

- Use `/4_data_analysis` for scripts and notebooks that actually analyze your
  data to answer your research question. Don’t try to cram everything into one
  file — you can have many scripts/notebooks in here as long as they are clearly
  named. It's expected that your research findings and conclusions will be the
  result of many smaller analyses, trying to fit everything into a single
  notebook will be unhelpful. You can always cite different scripts/notebooks to
  support different parts of your conclusions.
- In `/4_data_analysis/README.md`, outline your analysis strategy and summarize
  what each script or notebook does.
- In the main `README.md`, include:
  - A short summary of your analysis approach
  - A clear statement of your research conclusions (right at the top)
  - How confident you are in your results
  - What limitations your work has
  - Any ideas for future research
- Create a retrospective for this milestone in `/collaboration` using the
  template.

---

## 5. Communication Strategy

- Use `/5_communication_strategy` for planning and drafting your communication
  artefact. That includes audience research, message development, and assets
  like images or scripts.
- You don’t need to store the final artefact here if that doesn’t make sense For
  example, in cohort 6 a group created an instagram account and meme campaign as
  their communication strategy! You can't push that to a folder on GitHub.
- In `/5_communication_strategy/README.md`, summarize your strategy: who you’re
  reaching, what you’re saying, and why.
- In the main `README.md`, include a summary of your communication strategy and
  a link (if possible) to your final artefact.
- Create a retrospective for this milestone in `/collaboration` using the
  template.

---

## 6. Final Presentation

- Use `/6_final_presentation` to store slides, scripts, or notes from preparing
  your final presentation.
- In `/6_final_presentation/README.md`, list what’s in the folder and link to
  your actual presentation.
- Create a retrospective for this milestone in `/collaboration` using the
  template.

---

## General Tips

- Keep README files updated as you go. They’re for humans. Future-you is a
  human.
- Reproducibility is key. Someone else should be able to run your pipeline
  without tweaking your code or guessing what goes where.
- Use clear, consistent file names — you don’t want to waste time figuring out
  what `final_final_revised3.ipynb` was supposed to do.
- Document your work as you’re doing it. Waiting until the end = pain.
- Cross-reference when needed. ("This analysis uses the cleaned data from
  `/2_data_preparation/clean_survey_data.py`.")
- Commit early and often. Write commit messages that your teammates (and your
  future self) will understand.
- Do regular repo reviews as a team. Is everything findable? Understandable?

---

---

Happy studies!
