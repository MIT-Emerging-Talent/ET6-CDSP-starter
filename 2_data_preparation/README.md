# How We Model Our Research and Possible Limitations

Our research focuses on identifying linguistic differences between phishing emails and legitimate ones by studying how language is used in both.
Phishing emails often use certain writing tactics to trick or pressure readers, and we aim to uncover those patterns. To do this, we analyze the content of emails,
using mathematical models that help us understand and visualize natural language. We chose raw and mostly real language datasets
in order to keep our research broad and be able to apply different algorithms to help ourselves approach the data from different angles.

We work with large datasets made up of real emails. Each email includes a subject line, the main message (body), and a label marking it as either phishing or safe.

To study these emails, we will use several techniques that convert text into a form we can measure. For example:

- We will use tools that highlight which words are most frequent, important or unique in a message. This helps us identify phrases that show up more often in phishing emails than in legitimate ones.
- We are going to apply topic modeling methods that reveal the main themes in groups of emails. This helps us understand what phishing messages tend to talk about even if they use different words.
- We will also study how words relate to each other across different emails. By doing this, we can map the “meaning” and context of certain words, and how they are used differently in scam emails compared to safe ones.
- We will be analyzing how each category of linguistic feature increases or decreases the likelihood of an email being phishing or non-phishing.

These techniques help us turn language into patterns, allowing us to visualize and analyze how phishing emails are written and why they might be effective.

---

## About Our Data

Our source dataset was obtained from Zenodo, a reputable open-access research data platform. It was published by researchers Arifa I. Champa, Fazle Rabbi, and Minhaz F. Zibran in August 2024. The dataset is also referenced in multiple peer-reviewed academic papers, making it a trustworthy source for phishing research.

The Zenodo phishing validation dataset (2024) includes 11 datasets gathered from both historical corpora and curated sources. We used `Nazario.csv` and `Nazario_5.csv`.

- `Nazario.csv` is a well-known phishing corpus created by Jose Nazario in the mid-2000s using spam traps and public reports, containing phishing emails.
- `Nazario_5.csv` was curated by combining legitimate messages to create a balanced dataset for classification; it includes both phishing and non-phishing emails.

Our datset contains 1551 phishing and 1497 safe emails.Below we visually summarize the total class phishing and safe emails

![Class Distribution](class_distribution.png)

Other important things we will be looking at in order to better understand our data is the frequency of words

![Frequent Words](top_words.png)

And the existence of URL is another aspect we aim to analyze in phishing vs non phishing emails
![URL_Existence](url_proportion.png)

## Limitations of our data

Our dataset is from early 200's, while still widely applicable, phishing emails are evolving significantly.

Our research may incorporates some artificially constructed data and a few unknown combinations of sources. The Nazario_5 dataset fail to explicitly state where the non phishing originate from but were likely curated

Since our dataset is partially processed and curated from multiple sources, we cannot fully verify whether label assignment or content preservation was performed without error during cleaning, merging, or formatting.

Some emails have missing subject or body values entirely, reducing the effectiveness of content-based analysis. In some cases,the original dataset spans multiple lines within a single CSV cell therefore have to be excluded from our datasets.
  
Our final dataset after the cleaning script contains 1551 phishing and 1497 non-phishing emails , an imbalance between the two and might affect conclusion.
 We aim to mitigate it by :

-For word/category analysis: Use percentages within each class (phishing vs. safe), not raw counts.

-For machine learning: Apply techniques like class weighting, oversampling (adding more safe emails), or undersampling (reducing phishing emails).

-For model evaluation: Use metrics that account for imbalance, instead of just accuracy.

## Limitations of Our Approach

While our method gives us valuable insights, we’re aware of some limitations:

- **Lack of Regional and Cultural Focus**: Our data is mostly global and not grouped by region or culture. Since writing styles vary across different places, this could limit how well our findings apply to specific populations.
- **English-Only Data**: All of our analysis is based on emails written in English. This means our results may not apply to phishing messages written in other languages.
- **Combining Different Datasets**: Our research brings together emails from different sources, which can sometimes lead to inconsistencies in how messages are labeled or formatted. This might affect the accuracy of our comparisons.
- **Language Is Complex**: While mathematical models are powerful, they don’t always capture the full meaning behind language—like tone, sarcasm, or cultural references—which are often key parts of communication and deception.

Despite these challenges, our goal is to use language-based patterns to better understand phishing techniques and support the development of tools that can detect these threats more effectively. In addition to the research above, we also aim to analyze features like punctuation marks, length, grammatical error rates,
etc. to investigate more possible patterns

## Data Cleaning Scripts

## Objective

To create a fully reusable and reproducible Python script pipeline that:

1. Cleans and preprocesses raw email data.  
2. Prepares the text for linguistic analysis.  
3. Organizes it into training and validation sets for future modeling tasks.  

---

## Step-by-Step Plan

### 1. Input Requirements

- **Expected input format**: CSV (or structured `.eml` in future versions).  
- **Must include at least two columns**:  
  - **Email Text**: the full message body.  
  - **Email Type**: the label indicating if it's a phishing or legitimate email.  

### 2. Data Cleaning and Processing Pipeline

This script will follow a detailed pipeline inspired by Champa et al. (2024), adaptable for real-world, messy email data:

a. **Deduplication**  
   Remove repeated emails by comparing the content of **Email Text**.

b. **Discrepancy Removal**  
   Drop rows with missing, empty, or null text entries.  
   *Optionally* integrate language detection (e.g., `langdetect`) to retain only English emails.

c. **HTML & Text Normalization**  
   Strip HTML tags using **BeautifulSoup**. Retain only visible, meaningful plain text.

d. **Case Normalization and Punctuation Cleanup**  
   Convert all text to lowercase. Remove punctuation, symbols, and excessive whitespace using regex.

e. **Stop Word Removal**  
   Use **NLTK** or **spaCy** to filter out frequent stop words (e.g., “is”, “the”, “and”).

f. **(Optional) Tokenization**  
   If needed for later analysis or feature extraction, tokenize the cleaned text into word units.

---

*Once your merged dataset is finalized, simply run `clean_data.py` in this folder to produce `cleaned_phishing_dataset.csv` ready for modeling.*  
