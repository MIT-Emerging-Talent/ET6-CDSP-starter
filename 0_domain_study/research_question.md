# 🎯 Research Question & Objectives

This document outlines the central inquiry and guiding objectives for "The Public
Failure Analysis" project.

---

## Main Research Question

Our project's primary research question has been refined to focus on analyzing
real-world user feedback. The central inquiry that guides all our work is:

**What are the most prevalent themes of user-reported conversational failure in
leading mental health chatbots, and what do these themes reveal about the gap
between user expectations for emotional support and current algorithmic capabilities?**

---

## General Objective

To systematically analyze a large corpus of public user feedback
(from app stores and forums) in order to build an evidence-based taxonomy
of conversational failures in mental health chatbots.

---

## Specific Objectives

To achieve our general objective and answer the main research question,
we will pursue the following specific objectives:

1. **To Collect a Representative Dataset:**
    * Scrape thousands of user reviews for a curated set of three distinct
    mental health apps (Wysa, Replika, Calm) from the Google Play Store.
    * Scrape relevant user discussions from targeted subreddits to supplement
    the app store data with qualitative context.

2. **To Isolate a Corpus of "Failure" Narratives:**
    * Filter the collected data to create a focused corpus of negative sentiment,
    specifically by selecting reviews with 1-3 star ratings.
    * Apply standard Natural Language Processing (NLP) preprocessing techniques
    to clean and prepare the text data for analysis.

3. **To Identify and Quantify Failure Themes:**
    * Employ unsupervised topic modeling (Latent Dirichlet Allocation - LDA) to
    automatically identify the recurring themes and topics within the failure narratives.
    * Interpret the resulting topics and assign human-readable labels (e.g.,
    "Repetitive Looping," "Generic Responses," "Pricing Issues").
    * Quantify the prevalence of each identified failure theme across the dataset.

4. **To Synthesize and Communicate Findings:**
    * Compare the prevalence of conversational failure themes against
    non-conversational themes (e.g., technical bugs, cost).
    * Juxtapose quantitative findings (charts of topic prevalence) with powerful
    qualitative examples (anonymous user quotes) to create a compelling final
    report and presentation.
