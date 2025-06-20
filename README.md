# Data Strikers — Football Analytics Hub

Welcome to **Data Strikers**, a collaborative research initiative that explores
football through the lens of data science. Our mission is to build reproducible,
insight‑rich projects that illuminate how the beautiful game really works—from
the factors behind an individual’s scoring prowess to the subtle dynamics of
match officiating and injury risk. This repository collects our code, data
workflows, and findings so that students, practitioners, and fans can learn
from—and build upon—our work.

---

## Problem Statements

### 1. Goal‑Scoring Drivers *(Hamid)*

Which player metrics best explain and predict seasonal goal totals? We will
quantify the influence of expected goals (xG), shot volume, minutes played, and
other accessible performance indicators to determine which factors truly separate
prolific scorers from the rest.

### 2. Success After a League Jump *(Abdul Qader)*

When footballers move from a lower‑tier competition (e.g., the Eredivisie) to an
elite league (e.g., the Premier League), which personal attributes—such as height,
sprint speed, age, or prior‑league experience—most strongly forecast
a successful transition?

### 3. Real‑Time Referee Bias and Crowd Emotion *(Tibyan)*

Can live crowd sentiment (cheers, silence, boos) be leveraged to predict referee
decisions as a match unfolds? By pairing audio‑derived emotion signals with event
data, we will test whether referees unconsciously favor the home side in
emotionally charged moments.

### 4. Optimal Substitution Timing *(Khusro)*

Given the current game state—leading, drawing, or trailing—and contextual opponent
behavior (pressing intensity, prior substitutions), what is the mathematically
optimal minute to introduce a substitute to maximize win probability?

### 5. Injury‑Risk Forecasting *(Saeed)*

Can a player’s future injury likelihood be predicted from match workload metrics
(minutes, high‑speed runs, accelerations) and historical injury records? We aim
to build a model that alerts staff before fatigue turns into lost playing time.

---

## Data Sources

We rely on publicly available data sets wherever possible, including FBref match
and player statistics, Understat expected‑goals data, Sofascore event feeds,
and historical injury logs published by reputable analytics blogs.

---

## Repository Layout

`/1_datasets` holds the unmodified CSV exports or scraped files;

`/2_data_preparation` contains cleaned versions ready for analysis.

`/6_final_presentation` will hosts the finding of our research question which
you can see in `/0_domain_study/summary_of_group_problem_domain`.

`/collaboration` contains the communication and group dynamics information.

---

## License

All code is released under the MIT License. Data files remain under the terms
specified by their original providers.

---

*For questions or collaboration proposals, open an issue or reach out to any
member of **Data Strikers**.*
