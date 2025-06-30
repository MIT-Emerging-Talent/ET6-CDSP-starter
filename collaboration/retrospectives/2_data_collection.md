# Project Retrospectives

This document captures our reflections at the end of each project milestone. It
is a living document that will be updated as the project progresses.

---

## **Milestone 2: Data Collection & Processing (Due June 30)**

### **Group Retrospective**

*(Note: This section is a collaborative summary of the team’s experience
during this milestone.)*

#### What Went Well

- **Successful Data Scraping:** We developed and ran scripts to collect a
substantial volume of data from multiple sources, including the Google Play Store,
Apple App Store, and Reddit.
- **Strong Technical Base:** We set up a flexible data processing pipeline capable
of handling diverse and inconsistent raw data, which prepares us well for the
upcoming analysis stage.
- **Clearer Project Scope:** The decision to split our analysis into “conversational”
vs. “baseline” apps has given the project a clear focus and will strengthen our
final insights.

#### What Could Have Gone Better

- **Coordination & Timing:** Synchronizing the delivery of raw data from everyone
was sometimes challenging and caused a few slowdowns.
- **Requirement Clarity:** Early on, there was some confusion about whether we
needed to pre-filter data by ratings, which highlighted the need for more specific
task definitions from the start.

#### What We’ll Do Differently for Milestone 3

- **Internal Checkpoints:** For the next milestone, we’ll set clearer interim
deadlines for smaller tasks to help avoid last-minute crunches.
- **Better Communication:** We’ll be more consistent about sharing updates and
blockers in our team channel to keep everyone on the same page and spot issues early.

---

## **Individual Retrospective: Sadam Husen**

### What I Contributed

- I helped build and run parts of the data pipeline, including scraping data for
the target apps to ensure we had good coverage even if other sources were delayed.
- I contributed to the main `preprocess_data.py` script, working on standardizing
raw files, cleaning inconsistencies, and combining them into the final datasets.
- I supported our data documentation by contributing notes on file structures and
processing steps.

#### What I Learned

- **Technical Skills:** I got more comfortable handling large, messy datasets
with Pandas, and learned practical ways to avoid common issues like duplicate
rows and mismatched columns.
- **Collaboration:** I learned the value of checking in regularly and clarifying
overlaps before taking on extra tasks, so everyone’s work stays aligned.
- **Communication:** I saw how clear documentation and quick updates can help the
whole team stay on track, especially when multiple people are working on related
scripts.

#### What I’m Focusing on Next

- For Milestone 3, I plan to stay actively involved in the data analysis phase and
help break down tasks so everyone can contribute meaningfully.
- I’ll keep sharing any blockers or ideas early, and help review each part of the
work to maintain clean, well-organized outputs.

---

## **Zizi**

### **Individual Retrospective – Milestone 2: Data Collection**

Aziz Azizi
Date: June 30, 2025

🔹 What Went Well (For Me Personally)

- Skill Growth: I improved my understanding of web scraping and worked hands-on
with tools like BeautifulSoup or Selenium which was new for me.

- Ownership: I took ownership of Replica and was able to
gather clean, well-structured data for the team to use **but my teammate did my
part without discussing it with me.**

- What Could Have Gone Better
  - Time Management: I underestimated how long some of the manual steps (e.g.,
  login-based scraping or data cleaning) would take, which delayed my deliverables
  slightly.

  - Task Clarity: A task I had already taken ownership of was later completed by
  someone else without team discussion. This led to some redundancy and
  frustration, and it highlighted the need for better respect for assigned
  responsibilities and clearer communication within the team.
