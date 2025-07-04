# 🧠 Modeling the Domain: A Non-Technical Explanation

We explored how media violence might influence psychological and behavioral
outcomes in Gen Z by focusing on two key responses:

- **Desensitization** (emotional detachment, normalization, inaction)
- **Civic Engagement** (empathy-driven actions like protesting, donating, or
  sharing)

To model this, we used a three-pronged approach:

- 📺 Event-based media data (**GDELT**)
- 🪧 Real-world civic response data (**Mass Mobilization**)
- 💬 Individual-level psychological survey (**Custom Survey**)

This structure allowed us to examine patterns at both:

- The **societal level**: Are more violent events reported? Are people
  mobilizing in response?
- The **individual level**: How are people emotionally and behaviorally
  reacting to violent media?

---

## 🧩 Simplified Model

Media Exposure → Emotional & Cognitive Processing → Behavioral Outcomes  
Violent Content → 😐 Numbness / Empathy → 💤 Inaction / 🪧 Activism

We attempted to map:

- Media content volume and tone (via **GDELT**)
- Public protest activity (via **MM data**)
- Psychological response types (via **our survey**)

---

## ⚠️ Limitations of Our Approach

- **Causation vs. correlation**: We can't confirm causality—only pattern
  alignment.
- **Time mismatch**: GDELT is real-time; MM ends in 2020; our survey is
  current.
- **Survey bias**: Our sample may not reflect the general public; responses
  are self-reported.
- **Emotional scoring**: Emotions like numbness or empathy are difficult to
  quantify and can oversimplify lived experience.

---

## 📊 Dataset 1: Mass Mobilization (MM) – Harvard Dataverse

- **Source**: Harvard Dataverse
- **Method**: Human-coded protest data from news and academic sources
- **Coverage**: 1990–2020
- **Content**: Protest dates, size, cause, location, government response
- **Use**: Helps quantify civic action by region/time to compare with trends in
  media violence.

---

## 📊 Dataset 2: GDELT Conflict Data – GitHub

- **Source**: Global Database of Events, Language, and Tone (GDELT)
- **Method**: Automated extraction of global news events in real time
- **Content**: Political conflict, violence, unrest + emotional tone metadata
- **Use**: Tracks frequency and tone of media coverage on violent events.
  Compared with MM to explore media–mobilization correlation.

---

## 📋 Dataset 3: Custom Survey on Media Violence Response

- **Source**: Collected via our team's online survey
- **Why We Built It**: No dataset existed for personal emotional/behavioral
  responses to violent content.

### Survey Structure

**Sections**:

- **Demographics & Exposure**: Region, platform use, exposure frequency
- **Emotional**: Numbness, anger, detachment
- **Cognitive**: Normalization, curiosity, empathy
- **Behavioral**: Sharing, donating, ignoring, scrolling

### Scoring & Categorization

- Responses scored from **1–5** (low = engaged; high = desensitized)
- Final categories:
  - 🟢 Highly Engaged
  - 🟡 Mixed Response
  - 🔴 Highly Desensitized

**Use**: Offers insight into how individuals emotionally and behaviorally
respond to media violence, grounding the broader patterns from GDELT and MM.

---
