
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

#### **College**

* Reflects broad academic divisions within the university.
* Focus on the most active in online learning:

  * *Medicine*: Clinical courses, patient simulation platforms.
  * *Engineering*: Heavy use of course materials, design software resources.
  * *Information Technology*: Strong Moodle usage for coding tasks, virtual labs.
* Include other colleges (e.g., Education, Sharia, Commerce) to maintain university-wide representation.

---

#### **Department / Specialization**

* Capture differences in online engagement between departments.

  * E.g., *Software Engineering* students may access Moodle differently from *Civil Engineering* or *Electrical Engineering* students due to varying content types and tools used.
* Important for identifying discipline-specific learning patterns.

---

#### **Level of Study**

* **Undergraduate** students may rely more on structured learning, while
* **Postgraduate** students may use Moodle for research supervision, seminars, or journal submissions.

---

#### **Year of Study**

* First-year students may be less familiar with Moodle.
* Final-year students often engage in project-based learning and thesis work, which alters usage behavior.
* Mid-program students might reflect more consistent usage habits.

---

#### **Gender**

* Include male and female students to ensure gender balance.
* Useful for analyzing digital equity and differences in engagement trends.

---

#### 💻 **Online Course Participation**

* Students may be:

  * Fully enrolled in online/hybrid courses,
  * Taking only one or two online-enabled courses, or
  * Not enrolled in any online courses (to serve as a control group).
* This variable helps segment users by their exposure to Moodle.

---

#### 📊 **Course Load** *(Detailed Explanation)*

* **Definition**: Number of academic courses or credit hours a student is registered for in a semester.
* **Data Source**: Moodle course enrollments, university SIS, or learning analytics export.
* **Why It Matters**:

  * Heavy course load often correlates with higher engagement (e.g., more logins, assignment submissions).
  * It may also increase student stress or lead to disengagement if not supported properly.
* **Use in Sampling**:

  * Group students into:

    * *Low load* (1–2 courses)
    * *Medium load* (3–4 courses)
    * *High load* (5+ courses)
  * Ensure all groups are proportionally represented in your sample.
* **Examples**:

  * A 2nd-year IT student taking 6 courses likely behaves very differently from a 1st-year Education student taking 2.

---

#### 🕒 **Time of Access**

* Capture when students are active on Moodle:

  * *Time of day*: Daytime vs. evening usage.
  * *Day of week*: Weekdays vs. weekends.
* Helps identify time-based engagement trends.

---

---

### **Step 3: List of Specializations**

#### 📘 **Medicine (Clinical Medicine only)** [Medicince College](https://medicine.iugaza.edu.ps/)

1. Medicine

#### **Engineering** [Engineering College](https://eng.iugaza.edu.ps/)

1. Civil Engineering
2. Electrical Engineering
3. Computer Engineering
4. Industrial Engineering
5. Mechanical Engineering
6. Mechatronics Engineering
7. Environmental Engineering
8. Renewable Energy Engineering

#### **Information Technology** [IT College](https://fit.iugaza.edu.ps/)

1. Computer Science
2. Information Technology
3. Software Development
4. Mobile application development.
5. Multimedia and web development.

---

### **Step 4: Choose a Sampling Strategy**

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

### **Step 5: Data to Extract from Moodle Logs**

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

### **Step 6: Sample Size Determination**

Use statistical tools to compute needed sample size with 95% confidence and 5% margin of error (adjustable).

* Use Cochran’s formula or `statsmodels.stats.power` in Python.
* Adjust for expected missing data or dropouts.

---

### **Step 7: Balance and Bias Checks**

* Compare sampled group against total population on key features (gender, college, engagement).
* Use **Chi-square tests** to test representativeness.
* Use **PCA or t-SNE** on activity vectors to check diversity in learning behavior.

---
