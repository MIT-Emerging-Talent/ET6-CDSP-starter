# 📌 Milestone 2: Data Collection – Team Retrospective & Contributions

## 🧠 Team Reflection

In Milestone 2, our team pivoted from behavioral analysis to exploring **linguistic patterns** that distinguish phishing emails from legitimate ones. This decision allowed us to move forward effectively despite the lack of metadata.

We began with **independent dataset exploration**, which helped us evaluate available data sources.
After reconvening in a virtual meeting, we collectively selected a well-balanced and curated dataset (Nazario.csv and Nazario_5.csv).
While not all initial findings were used, the early exploration enhanced our understanding of dataset quality—particularly regarding **recency**, **representativeness**, and **source transparency**.

We developed a **reproducible Python preprocessing pipeline** that:

- Cleaned and normalized raw email text
- Removed HTML, null values, duplicates, and punctuation
- Converted casing and handled multiline CSV cells
- Removed stopwords using NLTK
- Split the dataset into training and validation subsets

The technical work improved team proficiency in **real-world data wrangling** and encouraged clean, modular scripting. The cleaned dataset was hosted on GitHub, and our milestone was Git-tagged to support version control and transparency.

We also created accessible documentation describing our **modeling strategy**, dataset structure, and known limitations. Visualizations were initiated to support future storytelling and feature analysis.

---

## ⚠️ Challenges Faced

- The dataset contains **emails from the early 2000s**, limiting relevance to current phishing methods.
- A portion of emails had **missing content** (subject or body) or **inconsistent formatting** due to multiline CSV entries.
- The data lacked **rich metadata** (e.g., sender details, timestamps, geographic data).
- Some legitimate emails came from **unclear or curated sources**, reducing real-world reliability.

---

## 🔄 Lessons & Next Steps

- Begin **exploratory data analysis earlier** to surface structural or linguistic issues sooner.
- Incorporate more **visual storytelling** (e.g., charts, word clouds, heatmaps).
- Explore **advanced linguistic features** like tone, urgency, and grammatical anomalies.
- Use **data augmentation** (e.g., paraphrasing or synthesis) to increase diversity.
- Host an **early-week sync** to unify independent work streams.

---

## 👥 Team Contributions Summary

| Team Member | Contribution |
|-------------|--------------|
| **Musab**   | Wrote modeling overview and outlined domain limitations |
| **Meklit**  | Documented dataset origin, limitations, and applied Git tag |
| **Ahmad**   | Built data cleaning pipeline; handled deduplication and preprocessing |
| **Mahdia**  | Structured dataset folders; hosted cleaned data on GitHub |
| **Semira**  | Contributed to dataset research and authored the milestone retrospective |
| **Everyone**| Completed milestone survey and participated in dataset evaluation |
