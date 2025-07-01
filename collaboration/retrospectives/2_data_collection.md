# 📌 Milestone 2: Retrospective

> “Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand.”  
> — Norm Kerth

---

## ✅ What Went Well (Continue Doing)

- We quickly aligned on a revised research focus—studying linguistic patterns in phishing emails—which helped keep our efforts cohesive despite data limitations.
- Independent dataset exploration allowed the group to evaluate multiple options before converging on a curated and balanced dataset using **Nazario.csv** and **Nazario_5.csv**.
  - *Nazario.csv* contained phishing emails collected via spam traps in the early 2000s.
  - *Nazario_5.csv* included more recent legitimate (non-phishing) emails to improve class balance, though the exact sources of the legitimate emails were not fully disclosed.
- A robust and reusable Python preprocessing script was created to:
  - Clean and normalize raw email text
  - Remove HTML tags, null values, duplicates, and punctuation
  - Handle multiline CSV cells and casing
  - Remove stopwords (using NLTK)
  - Split the dataset into training and validation subsets
- Clear documentation was produced describing our modeling strategy, dataset structure, and known limitations in accessible language.
- GitHub version control was maintained via commits, structured folders, and tagging (e.g., `milestone-2`) to support transparency.

---

## ⚠️ Challenges (Stop Doing)

- Some initial work went into datasets that were later discarded, indicating a need for earlier alignment on evaluation criteria.
- Handling multiline email entries and missing content (subjects or bodies) proved time-consuming and required extra cleaning logic.
- The dataset lacked rich metadata (e.g., timestamps, sender info), which limited behavioral and contextual analysis.
- Some legitimate email samples came from unclear or curated sources, raising concerns over real-world representativeness.

---

## 💡 New Ideas (Start Doing)

- Begin exploratory data analysis (EDA) earlier in the sprint to uncover issues with structure, formatting, or labeling.
- Improve early-week syncs to unify independent research efforts and reduce duplicated work.
- Explore data augmentation methods (e.g., paraphrasing or synthesis) to improve linguistic variety, especially for legitimate emails.
- Incorporate more visual storytelling tools (e.g., word clouds, URL structure charts, spam keyword analysis) in deliverables.

---

## 🧠 Lessons Learned

- Dataset recency and source transparency are just as important as dataset balance and size.
- Modular, reusable scripting enhances group collaboration and supports future iteration.
- Clear written documentation sharpens thinking and deliverables, especially in cross-functional collaboration.
- Setting shared expectations early improved group alignment and accountability.

---

## 📋 Strategy vs. Plan Reflection

- **What worked**: The plan to build a preprocessing pipeline and conduct linguistic feature analysis was executed successfully.
- **What changed**: The behavioral analysis component was dropped due to lack of metadata.
- **What was added**: We incorporated a deeper focus on data quality, structure, and linguistic feature engineering.
- **What was removed**: Earlier datasets that didn’t meet quality standards were abandoned after evaluation.

---

## 👥 Summary of Group Contributions

| Team Member | Contribution |
|-------------|--------------|
| **Musab**   | Wrote modeling overview and outlined domain limitations |
| **Meklit**  | Documented dataset origin, limitations, and applied Git tag |
| **Ahmad**   | Built data cleaning pipeline; handled deduplication and preprocessing |
| **Mahdia**  | Structured dataset folders; hosted cleaned data on GitHub |
| **Semira**  | Contributed to dataset research and authored the milestone retrospective |
| **Everyone**| Participated in dataset evaluation and completed the milestone survey |

---
