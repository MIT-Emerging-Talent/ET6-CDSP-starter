# 📌 Milestone 2: Retrospective

> “Regardless of what we discover, we understand and truly believe that everyone
> did the best job they could, given what they knew at the time, their skills
> and abilities, the resources available, and the situation at hand.”
> — Norm Kerth

---

## ✅ What Went Well (Continue Doing)

- We quickly aligned on a revised research focus—studying linguistic patterns in phishing emails—which helped keep our efforts cohesive despite data limitations.
- Independent dataset exploration allowed the group to evaluate multiple options before converging on a well-balanced dataset through consensus.
- A robust and reusable Python preprocessing script was created to clean, format, and split the dataset for analysis and modeling.
- Clear documentation was produced explaining our modeling approach, dataset composition, and its limitations in accessible language.
- Version control and transparency were maintained through Git commits, structured folders, and public hosting of cleaned data.

---

## ⚠️ Challenges (Stop Doing)

- Some initial work went into datasets that were later discarded, indicating a need for earlier alignment on evaluation criteria.
- Handling multiline email entries and missing fields (subjects/bodies) in CSV format proved time-consuming and highlighted the need for earlier exploratory data analysis (EDA).
- Lack of metadata (e.g., timestamps, sender info, location) in the dataset limited the depth of analysis we could perform.
- Some legitimate email samples were curated from unclear sources, reducing real-world representativeness and raising concerns over label quality.

---

## 💡 New Ideas (Start Doing)

- Begin exploratory data analysis earlier in future sprints to catch formatting or data limitations before pipeline development.
- Improve early-week communication and syncs to unify independent research efforts and avoid duplicate work.
- Consider using data augmentation (e.g., text generation, paraphrasing) to improve linguistic variety—especially for legitimate emails.
- Increase visual storytelling (e.g., word clouds, URL analysis, bar charts) to better communicate linguistic differences.

---

## 🧠 Lessons Learned

- Dataset recency and source transparency are just as important as balance and size.
- Building reusable, modular scripts early on supports smoother iteration and group collaboration.
- Clear written communication—especially in documentation—helps clarify both our thinking and our deliverables for future stages.
- Collaboration worked best when expectations were clarified early and everyone shared ownership over deliverables.

---

## 📋 Strategy vs. Plan Reflection

- **What worked**: Our plan to build a preprocessing pipeline and conduct linguistic analysis aligned well with what we accomplished.
- **What changed**: The original plan to include behavioral features had to be dropped due to missing metadata.
- **What was added**: We incorporated more focus on linguistic feature engineering and data quality inspection than initially planned.
- **What was removed**: Time spent on initial datasets that didn't meet quality or relevance standards had to be let go, allowing us to refocus effectively.

---

## 🔄 Summary of Group Contribution

Each team member contributed to different aspects of Milestone 2, including:

- Researching and selecting datasets
- Developing and testing the preprocessing pipeline
- Hosting and organizing cleaned data
- Creating documentation and GitHub commits
- Drafting this retrospective and visuals for later milestones
