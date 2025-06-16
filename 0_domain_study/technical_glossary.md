# 🛠️ Technical Glossary

This glossary defines key technical concepts, frameworks, and metrics used  
throughout our domain study and analysis of chatbot, human, and hybrid mental  
health support systems.

---

## Natural Language Processing (NLP)

Automated techniques for understanding and generating human language. Common  
tasks include tokenization, part-of-speech tagging, parsing, and semantic  
analysis.

## Tokenization

The process of breaking text into individual units (tokens), such as words,  
punctuation, or subwords, which serve as the basis for further NLP tasks.

## Lemmatization

Reducing words to their base or dictionary form (lemma), enabling the grouping of
related word forms (e.g., "running" → "run").

## Stop Words

Common words (e.g., "the", "and", "is") that carry minimal semantic content and
are often removed to focus on meaningful terms.

## Sentiment Analysis

A subfield of NLP that determines the emotional tone of text (positive,  
negative, or neutral). Used here to detect empathy or distress in chatbot  
replies.

## Sentiment Scoring

Quantitative measures assigned to text based on sentiment analysis. Examples:

- **VADER**: Rule-based sentiment scoring optimized for social media text.  
- **Lexicon-based**: Uses predefined lists of positive/negative terms.

## Thematic Clustering

Grouping text samples (e.g., user messages or chatbot responses) into clusters  
based on semantic similarity to identify common themes or topics. Techniques  
include k-means clustering on embeddings.

## Emotion Detection

Beyond sentiment, identifying specific emotions (e.g., joy, anger, sadness) in  
text using supervised models trained on annotated corpora.

## Transformer Models

Deep learning architectures (e.g., BERT, GPT) that use self-attention mechanisms
to model long-range dependencies in text, enabling powerful contextual  
representations.

## Pre-trained Models & Pipelines

Reusable NLP models (often hosted on platforms like Hugging Face) that come with
built-in tokenization, embeddings, and inference pipelines for tasks such as  
sentiment or named-entity recognition.

## Rule-based vs. Machine Learning Approaches

- **Rule-based**: Uses handcrafted rules or lexicons (e.g., VADER).  
- **Machine Learning**: Trains statistical or neural models on labeled data to  
  automatically learn patterns.

## Rubric & Evaluation Metrics

A structured guide for scoring chatbot, human, and hybrid interactions based on
professional guidelines. Key metrics include:  

- **Precision**: Proportion of correctly identified positive instances.  
- **Recall**: Proportion of actual positives correctly identified.  
- **F1 Score**: Harmonic mean of precision and recall, balancing both.  
- **Cohen’s Kappa (κ)**: Measures inter-rater agreement beyond chance for  
  rubric scoring.

## Inter-Rater Reliability

The degree of agreement among multiple evaluators scoring the same content, often
quantified using Cohen’s Kappa.

## Data Anonymization & Privacy

Techniques (e.g., de-identification, pseudonymization) used to remove or obscure
personal identifiers in chat logs to protect user privacy and comply with IRB  
and legal requirements.

## Ethical Constraints & IRB

- **Institutional Review Board (IRB)**: Committee that oversees research  
  involving human subjects to ensure ethical standards.  
- Ethical constraints include safe handling of high-risk messages (e.g., self-  
  harm disclosures) and informed consent.

## Escalation Mechanism

Predefined workflow for transferring a conversation from chatbot to human support,
such as triggering live counselor intervention after detecting high-risk content.

## Hybrid Model

Systems that combine automated chatbot interactions with human-in-the-loop  
support, balancing scalability with empathetic depth.

## FRESCO Criteria

Framework for crafting and evaluating research questions:  

- **F**easible: Achievable within resource and time constraints.  
- **R**elevant: Addresses an important problem in the field.  
- **E**thical: Complies with moral and regulatory standards.  
- **S**pecific: Clearly defined scope and outcomes.  
- **C**loud (Collaborative): Designed for teamwork and reproducibility.  
- **O**rganized: Structured for systematic investigation.
