# Data Exploration: Guide

This folder is for any Python scripts or notebooks you use to _explore and
understand_ your datasets. These files should:

1. Read in prepared datasets from `0_datasets`
2. Explore and understand the dataset without running a deep analysis:
   - Generate some visualizations (in a notebook, or in a separate image file
     saved to this folder)
   - Run some descriptive statistics
     (_[beware](https://www.researchgate.net/publication/316652618_Same_Stats_Different_Graphs_Generating_Datasets_with_Varied_Appearance_and_Identical_Statistics_through_Simulated_Annealing)
     the
     [Datasaurus Dozen](https://www.research.autodesk.com/publications/same-stats-different-graphs/)!_)
   - ... let your curiosity guide you, but _avoid_ running any inferential
     statistics or using any machine learning at this stage.

**DO NOT modify an existing dataset in `0_datasets`!** This is critical to open
research: Someone should be able to clone this repository and run your scripts
to replicate your research. If you modify an original dataset, others cannot
replicate your work.

> [Chapter 4 - Exploratory Data Analysis](https://bookdown.org/rdpeng/artofdatascience/exploratory-data-analysis.html)
> from the Art of Data Science is a good starting reference.

## README.md

Use the README in this folder to give a quick summary of each script/notebook -
which dataset(s) it explores, and how.
