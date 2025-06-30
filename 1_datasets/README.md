# Datasets

## Raw fake jobs

This dataset can be found in **Kaggle**, referred to as **_'Recruitment Scam
Dataset'_**, or in
**EMSCAD** project **website**, referred to as **_'Employment Scam Aegean Dataset'_**.

This dataset was collected and curated by the **_Laboratory of Information and Communication
Systems Security_** at the **_University of the Aegean_** in **_Greece_**.
It contains **18,000** job postings, with around **800** labeled as fraudulent.

This dataset
was mainly designed to  provide a realistic and comprehensive resource for research
on employment scams. It was collected from real online job ads between **2012**
and **2014**.
The job postings were gathered from multiple **_online_** sources, including **_job
portals_** and **_corporate websites_**.

Each entry in the dataset includes a
variety of features such as **_job title, location, department, salary range, company_**
**_profile, job description, requirements, benefits, telecommuting status, company
logo_**, **_presence, employment type, required experience, required education, industry,
function,_** and a **_class label_** indicating whether the posting is fraudulent
or not.

The dataset is publicly available and has been widely used in academic research
for developing and testing machine learning models to detect fraudulent job postings.

The main goal of this data is to clean it based on specific features that we aim
to use in the job board, organize it, refine it by Gemini, then use it to test
humans' ability to detect if the job provided is legitimate or fraudulent when
it's written by AI, since it mimics real job posts.

## Processed fake jobs

The raw data was collected between **2012** and **2014**, before the development
of AI, therefore, **_thirty_** fake job posts were randomly selected from **_raw
fake jobs_**
file and used an algorithm to automatically refine them, using the Gemini API to
generate AI-enhanced fraudulent postings.

## Raw real jobs

This dataset was manually collected by **_The Hypatia Circle_** group members.
**_Thirty_** real job postings were collected from **_LinkedIn_** and **_Indeed_**.
Each entry in this dataset includes **_job title, company name, full job description,_**
**_announcement platform, URL, and date_**. All jobs were posted in 2025.

This data is only internally available via the shared link.

## Past relevant studies

The research, **_Assessing AI vs Human-Authored Spear Phishing SMS Attacks: An
Empirical Study_**, a **2025** study, was conducted by researchers at **_Brigham
Young University._**

To collect data, participants were recruited and asked to provide personal
information that could be used to personalize phishing messages.

Meanwhile, on the other hand, both human and AI authors used this personal information
to craft spear phishing SMS messages tailored to each participant.

There were mainly **_four_** steps for the data collection procedure. **_Firstly_**
participants were shown a set of personalized SMS messages (some human-authored,
some AI-generated).
**_Secondly_**, they were asked to rank the messages by how convincing they found
them. **_Thirdly_**, participants also provided qualitative feedback on each message.
**_Lastly_**, they were then asked to guess whether each message was written by a
human or by AI.

This experiment measured how convincing the messages were (both written by humans
and AI) and whether participants could distinguish between human and AI authorship.

There was **_no study_** that specifically tested humans' ability to differentiate
if a job post is legitimate or fraudulent when the post is AI-generated that we
know of, hence we're planning to use this study as a foundation for the process
of building and analyzing the job board.
