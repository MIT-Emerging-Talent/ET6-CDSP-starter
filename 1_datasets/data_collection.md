# Data Documentation for "The Public Failure Analysis" Project

This document provides a detailed overview of the datasets collected and processed
for our analysis of mental health chatbot failures.

## Data Access & Hosting

The final, analysis-ready datasets are publicly hosted on Kaggle. This ensures
accessibility and keeps our repository lightweight.

* **Kaggle Dataset Link:** [https://www.kaggle.com/datasets/sadamhali/user-reviews-of-mental-health-chatbots-2022-2025](https://www.kaggle.com/datasets/sadamhali/user-reviews-of-mental-health-chatbots-2022-2025)

## Data Provenance & Collection

* **Platforms:** Google Play Store, Apple App Store, Reddit.
* **Applications Scraped:** Wysa, Replika, Calm, Woebot, Youper.
* **Collection Period:** Data was scraped in June 2024, filtered for reviews/posts
on or after January 1, 2022.
* **Collection Method:** Data was collected using custom Python scripts located
in the `/scripts` directory of this repository.

## Final Processed Files

The raw data has been processed into two distinct files for a robust comparative
analysis.

### 1. `conversational_apps_dataset.csv`

* **Purpose:** This is the primary dataset for analyzing the failures of
conversational AI.
* **Contents:** Contains preprocessed feedback for apps with a core conversational
component: **Wysa, Replika, Woebot, and Youper**.
* **Schema:**

    | Column Name   | Data Type | Description                                  |
    |---------------|-----------|----------------------------------------------|
    | `user_name`   | string    | The username of the reviewer/poster.         |
    | `review_text` | string    | The full text content of the feedback.       |
    | `rating`      | integer   | The star rating (1-3).Not for Reddit data,   |
    | `date`        | datetime  | The date the feedback was posted.            |
    | `app_name`    | string    | The target application being discussed.      |
    | `source`      | string    | The platform the data was scraped from.      |
    | `category`    | string    | `'conversational'`                           |

#### 2. `baseline_app_dataset.csv`

* **Purpose:** This dataset serves as a baseline to understand common issues in
a non-conversational wellness app.
* **Contents:** Contains preprocessed reviews for **Calm**.
* **Schema:**

    | Column Name   | Data Type | Description                                   |
    |---------------|-----------|-----------------------------------------------|
    | `user_name`   | string    | The username of the reviewer.                 |
    | `review_text` | string    | The full text content of the review.          |
    | `rating`      | integer   | The star rating given by the user (1-5).      |
    | `date`        | datetime  | The date the review was posted.               |
    | `app_name`    | string    | `'Calm'`                                      |
    | `source`      | string    | The platform the data was scraped from.       |
    | `category`    | string    | `'baseline'`                                  |
