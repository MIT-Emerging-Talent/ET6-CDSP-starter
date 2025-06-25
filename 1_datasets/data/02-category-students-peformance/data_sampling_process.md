
# Sampling Technique

This document outlines the thought process for identifying what data we need and how we should request it from the Islamic University of Gaza (IUG).

## Objectives

### **Objectives of This Document**

1. **Define Data Requirements:**
   Identify the specific types of Moodle activity data needed to analyze student engagement across various colleges and specializations at the Islamic University of Gaza (IUG).

2. **Establish a Data Request Framework:**
   Outline a clear and structured approach for formally requesting the necessary data from IUG’s IT or academic affairs departments.

3. **Ensure Ethical and Legal Compliance:**
   Highlight the importance of ethical considerations, including student privacy, informed consent (if needed), and compliance with institutional data protection policies.

4. **Support Representative Sampling:**
   Provide a rationale for selecting a balanced and representative sample of students from colleges actively engaged in online learning (e.g., Medicine, Engineering, and Information Technology).

## Step 1: Define the Objective of sampling

Before sampling, define the exact purpose. Examples might be:

* Evaluate impact of war events on students' attendance/performance.
* Predict student success or dropout risks based on Moodle usage.

---

### **Step 2: Identify Key Variables for Sampling**

From Moodle logs and university structure,  sampling should reflect diversity in:

* **College** (Medicine, Engineering, IT, others)
* **Department/Specialization** (e.g., Software Engineering, Civil Engineering, etc.)
* **Level of Study** (Undergrad, Postgrad)
* **Year of Study** (1st year, final year, etc.)
* **Gender** (Male, Female)
* **Online Course Participation**
* **Course Load**
* **Time of Access** (day/night, weekend)

---

### 🌐 **Step 3: List of Specializations**

#### 📘 **Medicine (Clinical Medicine only)** [Medicince College](https://medicine.iugaza.edu.ps/)

1. Medicine

#### 🛠 **Engineering** [Engineering College](https://eng.iugaza.edu.ps/)

1. Civil Engineering
2. Electrical Engineering
3. Computer Engineering
4. Industrial Engineering
5. Mechanical Engineering
6. Mechatronics Engineering
7. Environmental Engineering
8. Renewable Energy Engineering

#### 💻 **Information Technology** [IT College](https://fit.iugaza.edu.ps/)

1. Computer Science
2. Information Technology
3. Software Development
4. Mobile application development.
5. Multimedia and web development.

---

### 📊 **Step 4: Choose a Sampling Strategy**

#### **Stratified Sampling**

we want proportional representation **from each college and department**, adjusted for their:

* Total student population
* Online course enrollment
* Activity level on Moodle

> **Strata**: College → Department → Year of Study

**Example:**
If 60% of online learners are from IT, 25% from Engineering, and 15% from Medicine, then in a 1000-student sample:

* 600 from IT → spread across its 6 departments
* 250 from Engineering → spread across 8 departments
* 150 from Medicine

Use Moodle logs to define what "engaged" means (e.g., more than 10 logins/week or submissions/month) — we can further stratify by **engagement level**.

---

### 📥 **Step 5: Data to Extract from Moodle Logs**

* `user_id`
* `timestamp`
* `event_type` (view, submit, login, forum post, etc.)
* `course_id`
* `module`
* `duration_on_page`
* `grade_items`
* `cohort` or department identifiers
* `gender`, `level_of_study` (if linked via user profiles)

---

### 🧪 **Step 6: Sample Size Determination**

Use statistical tools to compute needed sample size with 95% confidence and 5% margin of error (adjustable).

* Use Cochran’s formula or `statsmodels.stats.power` in Python.
* Adjust for expected missing data or dropouts.

---

### ⚖️ **Step 7: Balance and Bias Checks**

* Compare sampled group against total population on key features (gender, college, engagement).
* Use **Chi-square tests** to test representativeness.
* Use **PCA or t-SNE** on activity vectors to check diversity in learning behavior.

---
