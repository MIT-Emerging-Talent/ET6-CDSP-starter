# Group Intro

We are proudly part of the MIT Computer and Data Science Certificate Project  2024-2025

DATA ALCHEMISTS is dedicated to fostering a culture of trust, respect, and accountability
 while promoting open communication and efficient collaboration. Our goal is to
  create an environment that values diverse perspectives, encourages teamwork,
   and drives success. We support continuous learning and innovative thinking.
    Our shared commitment to growth and development empowers each member to
     contribute and learn from collective experiences, ensuring we work
      together effectively to achieve success.

## Problem statement

In regions affected by war, the education system is one of the first societal structures to collapse.
 Students who once demonstrated high academic performance and consistent attendance often experience
  a significant decline in both after conflict begins. Violence, displacement, psychological trauma,
   and the breakdown of infrastructure such as internet access or school availability contribute
    to reduced academic outcomes and disrupted attendance.

This project investigates how armed conflict affects students' performance and attendance over time.
 By comparing pre-conflict and during-conflict academic records, we aim to understand the depth
  of disruption and identify patterns that can inform targeted interventions.

## research question

How does war disruption such as violence, displacement, and infrastructure breakdown impact students' academic performance and attendance on online learning for students in colleges in war affected zones?

## Group Summary of the Problem Domain (with Systems Thinking)

Our group is focused on understanding the effects of the challenges faced by students in war-affected zones on their educational performance. These students are forced to rely on online education under extreme hardships-from exposure to violence,
displacement, and constant unreliable internet.

Using a systems thinking approach, we analyze the student's environment as a complex system, where various elements—physical safety, mental health, access to education, family displacement, and technology
 infrastructure—interact and reinforce one another. For instance:

      Displacement leads to unstable living conditions → Limited or no access to schools.

      Violence and trauma increase stress → Reduced concentration and motivation.

      Interrupted school services → Lower attendance and academic decline.

These effects often create a negative feedback loop, where low performance leads to disengagement, further worsening outcomes. By understanding these relationships, we aim to propose data-driven strategies to identify at-risk students against these effects.

**For further explanation of the problem, the iceberg model is applied** [in this file](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-03-repo/blob/main/0_domain_study/systems_tkinking.md)

## 5 Ws and 1 H for our problem statement

| **Question** | **Answer** |
| ------------ | ---------------------------------------------------------------- |
| **Who**      | Students in war-affected regions who rely on online platforms for education.|
| **What**     | Their academic engagement and performance are being negatively impacted by conflict-related challenges such as violence, displacement, and unreliable internet access. |
| **Where**    | Conflict zones and war-affected areas where traditional education systems are disrupted.    |
| **When**     | During and after the onset of armed conflicts, particularly when students are displaced or formal schools are shut down.|
| **Why**      | War introduces instability and trauma, while displacement disrupts routine and internet access; these factors collectively harm students’ ability to learn and perform academically.|
| **How**      | By analyzing student interaction and performance data on online platforms,and assessing whether AI tools (e.g., adaptive learning, offline content, emotional support bots) can help mitigate the negative impacts and support effective learning.|

### How are we modeling our problem?

We are collecting data from the Islamic University of Gaza (IUG), this data includes Moodle logs capturing various student interactions in online learning during wartime, with fields such as:

* Timestamp
* Event type (e.g., view, submit, login, forum post)
* Course ID
* Module
* Duration on page
* Grade items
* Cohort or department identifiers
* Gender
* Level of study (when linked via user profiles), we believe these features

We believe these variables are going to be good indicators of college students’ academic engagement and performance during wartime. For example, we can tell how engaged a student is by capturing their number of logins, their duration on the page,
and by considering their grades as well.

We have also gathered  war events data from online websites, we are planning to use these to prove the harsh events going on in Gaza and correlate them with students' performance.

Since we do not have access to these same students’ data before the war (IUG students) to compare their academic performance before and after the war, we are going to be collecting data from another Palestinian university in the West Bank as proxy data.

Taking into consideration college students in the WestBank are not affected by war, but they might be indirectly affected by the situation currently taking place in Gaza from war to starvation to ongoing displacement, we think we can extract much more
valuable insights than if we just used any other proxy data from a non-war affected country.

**Possible flaws**:

* Some of the war events data we collected online contains untrue or misleading values, like the number of fatalities in a lot of datasets is in fact less than the actual number.
* We are going to be trying our best to take into consideration all of the harsh war events that college students in Gaza go through, but
due to a lack of data availability online about war events, we might miss some important effects like starvation.
* Some of the war events data that we have is not really up to date with the situation.
