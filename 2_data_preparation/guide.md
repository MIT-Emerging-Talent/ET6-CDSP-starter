# Data Preparation: Guide

This folder is for any Python scripts or notebooks you use to clean & prepare
your datasets. These files should:

1. Read in datasets from `0_datasets`
2. Clean, reformat, or otherwise process the datasets for later.
3. Write the processed dataset into `0_datasets` with a helpful file name.

**DO NOT modify an existing dataset in `0_datasets`! Instead, save your
processed data to a _new_ file.** This is critical to open research: Someone
should be able to clone this repository and run your scripts to replicate your
research. If you modify an original dataset, others cannot replicate your work.

## README.md

Use this folder's README to give a quick summary of each script/notebook - which
dataset(s) does it process and how? which datasets does it create and save to
`/1_datasets`?.
