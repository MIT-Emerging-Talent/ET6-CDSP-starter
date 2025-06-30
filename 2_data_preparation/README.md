# Data Cleaning Scripts

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
