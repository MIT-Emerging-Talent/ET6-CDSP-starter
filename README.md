# 👋 Welcome to *The Express*

Welcome to **The Express** – our Collaborative Data Science Project!

## 📊 Analyzing and Investigating Supply Chain Delays: A Data-Driven Approach

Together, we’ll explore and analyze the root causes of delivery delays in the
U.S. retail supply chain using a systems thinking approach and data-driven
techniques. This project is a great opportunity to collaborate, learn, and
generate impactful solutions.

## 👥 Team Members with this Project  

- [Jawid Mohseni](https://github.com/JawidMohseni)  
- [Razan Ibrahim](https://github.com/Razan-O-Elobeid)  
- [Rumiya](https://github.com/Ismatova-Rumiya)  
- [Alemayehu Desta](https://github.com/Alemayehu-Desta)  
- [Omnia](https://github.com/omniaNS)

### 🤝 Collaboration Framework

- 📋 [Our Group Norms](collaboration/README.md)
- 🎯 [Learning Goals](collaboration/learning_goals.md)
- 💬 [Communication](collaboration/communication.md)
- 🚧 [Constraints](collaboration/constraints.md)
- 🔍 [Retrospective](collaboration/retrospective.md)

### 🧩 Problem Statement

Despite being one of the world’s most developed economies, the United States
continues to face nationwide retail supply chain delays, affecting both large
chains and small-to-mid-sized businesses. These disruptions are especially
severe during peak periods like holidays, back-to-school seasons, and major
promotional events, resulting in stockouts, delivery delays, and lost customer
trust.
A 2021 report by [the National Retail Federation](https://nrf.com/media-center/press-releases/nrf-calls-white-house-address-port-congestion-challenges)
revealed that 97% of U.S.
retailers experienced shipping or port delays, [with 70% reporting delays of two
to three weeks](https://splash247.com/biden-pressured-to-fix-us-port-congestion-issues/).
Additionally, [the U.S. is
short over 78,000 truck drivers in
late 2022](https://www.trucknews.com/human-resources/u-s-is-short-78000-drivers-ata-says/1003170001/),
contributing to late
deliveries and increased freight costs. Lead
times for replenishment and raw materials have increased by up to 30 to 40
days, while [65% of grocery and retail merchants lack real-time supply chain
data](https://www.pymnts.com/news/retail/2025/65percent-of-grocery-retailers-lack-real-time-supply-chain-data/),
this reduces
their ability to respond dynamically to disruptions.
These delays are not confined to specific geographies—they affect retail
operations nationwide, from large coastal distribution hubs to inner-city
stores. As a result, businesses struggle to maintain inventory balance, meet
demand, and compete with more digitally advanced competitors like Amazon, which
leverage predictive analytics and automation.
This growing gap between the current state of retail supply chain operations
and the desired state of responsive, tech-enabled systems highlights the urgent
need for scalable solutions. Addressing this issue is critical to improving
customer satisfaction, reducing operational costs, and preserving the
competitiveness of the U.S. retail sector.

---

## 📌 Research Questions

### 🎯 Actionable Research Question

- **What are the key factors that contribute to delivery delays in the retail
  supply chain, and how can they be mitigated?**

---

### 🧠 Supporting Questions

- What transportation and environmental factors most significantly contribute to
  delivery delays in the U.S. retail supply chain, and how accurately can machine
  learning models predict these delays?

- How do environmental and event-based anomalies (e.g., weather, COVID) affect
  last-mile delivery delays in urban retail supply chains, and how accurately can
  machine learning models predict these delays in the U.S.?

- What are the major transportation and logistics-related causes of delivery
  delays in the U.S. retail supply chain, and how can predictive models help
  identify high-risk deliveries?

- How can machine learning be used to predict and reduce delivery delays in the
  U.S. retail supply chain based on traffic, weather, and logistics data?

- How can machine learning models improve the accuracy of demand forecasting in
  retail supply chains during seasonal fluctuations?

---

### 🧠 Systems Thinking Approach

#### 🕸 Understanding Delivery Delays in the U.S. Retail Supply Chain

We understand that delivery delays in the U.S. retail supply chain is the
outcome of multiple interdependent systems. Using systems thinking, we analyzed
how infrastructure, labor shortages, environmental variability, consumer
expectations, and technological limitations interact to produce a recurring
pattern of delivery disruptions. From this lens, our team’s approach is to
understand the leverage points where smarter interventions can improve
resilience across the system.

---

### ❄️ The Iceberg Model: Understanding Systemic Delivery Delays

#### 📍 Event

The end user experiences a delayed shipment beyond its expected delivery time.
Consumers, both individuals and businesses, experience missing delivery
windows, tracking errors, or unfulfilled expectations. But this event is just
the tip of the iceberg, in which the end user has minimal capability to
understand.

#### 📈 Patterns & Trends

Delays spike during holidays, in congested cities, or under severe weather
conditions.
These patterns are not random. We consistently observe delays in:

- Urban centers like Los Angeles and NYC (traffic congestion, density)
- Winter-prone areas like Chicago (weather disruptions)
- Seasonal surges (Black Friday, Christmas)
- During national labor shortages or strikes

#### 🏗️ Systemic Structures

**Why do these delays persist despite tech and logistics innovation?**

Underlying structures create the conditions for recurring delays:

- Outdated or underfunded transportation infrastructure
- Long-term truck driver shortages (80,000+ unfilled positions, ATA 2023)
- Fragmented communication between warehouses, carriers, and platforms
- Uniform delivery guarantees that don’t adjust for local or temporal realities
- Reactive scheduling and lack of data-driven optimization
- Fatigued labor, minimal buffer time, and rigid delivery windows

These structural flaws create bottlenecks and friction points that increase
system stress during peak demand.

#### 💭 Mental Models

**What beliefs sustain these fragile systems?**

- The belief that faster is always better encourages unrealistic promises and
over-optimistic routing.
- Automation will fix everything, ignoring socio-environmental realities like
human fatigue and weather patterns.
- When an entity believes delays are external, not internal, it shifts the
blame to weather or drivers, rather than poor planning or systemic
inflexibility.
- The concept that the customer is always right pressures the system into
overpromising and overextending.

These mental models limit innovation, reduce flexibility, and intensify
systemic fragility.

![Delivery Delays in the U.S. Retail Supply Chain][def]

---

*For more information, see the [`0_domain_study`](./0_domain_study) folder.*

🛠️ *By addressing both the visible symptoms and underlying systems, our team
aims to develop meaningful, data-driven solutions to reduce delivery delays and
improve the efficiency of retail supply chains.*

[def]: image1.png
# 📦 Data Modeling: Non-technical Explanation

In this project, we explore what causes delivery delays and operational risks in
a real-world logistics network operating in Southern California. The dataset includes
hourly data collected between 2021 and 2024 from trucks, rail, and warehouses. These
records reflect the conditions in which deliveries were made—whether that means
navigating through traffic, waiting at ports, or responding to equipment shortages.

To make sense of the dataset, we grouped the input features (variables) into three
broad categories:

- **Logistics Data**:-fuel usage, driver behavior, equipment status, and loading
  times
- **Environmental Factors**:-traffic congestion, weather conditions, port delays,
 and cargo condition
- **Economic & Operational Inputs**:-shipping costs, lead times, customs clearance
  duration, and supplier reliability

**Feature formats:**

- Binary variables (e.g., cargo status: 0 = bad, 1 = good)
- Scaled inputs (e.g., traffic levels: 0–10)
- Continuous measures (e.g., fuel in liters, shipping cost in USD)

Each row in the dataset is treated as a snapshot in time-representing a delivery
and the surrounding conditions at that moment.

## 🎯 Target Variables

The goal is to describe what factors cause delivery delay and predict delivery
risk and delays before they occur. We model this through:

- **Delivery Time Deviation**:-how early or late a delivery is (in hours)
- **Risk Classification**:-Low, Moderate, or High
- **Delay Probability / Disruption Likelihood**:- values between 0 and 1

## ✅ Why This Model Works

### Interpretability

Each feature in the dataset corresponds directly to a real-world logistics factor,
such as traffic congestion, fuel consumption, or driver behavior. This connection
makes model outputs easier to explain and justify to decision-makers, because
the model is built on the same variables they already monitor and understand.

### Flexibility

The dataset is structured to support multiple types of machine learning tasks.
It can be used to train regression models that estimate delivery delays in hours,
classification models that categorize shipments by risk level. This dual-purpose
flexibility is ideal for real-world applications where different problems require
different modeling approaches.

### Real-Time Fit

Because the data is recorded on an hourly basis, it aligns well with how logistics
operations are managed in practice. Planners and dispatchers make decisions throughout
the day, and having time-stamped snapshots allows models to provide insights that
are both timely and actionable during live operations.

## 🔄 Delivery Modeling Flow

![modeling_flow](https://github.com/user-attachments/assets/57e280a4-e092-460e-a8ed-85790c50f8f5)

## Limitations of the Model

### Lacks Temporal Tracking

The dataset treats each shipment record as an isolated snapshot in time.
While this is useful for analysis, it limits the ability to understand how
a shipment's condition evolves hour by hour. Without tracking progression across
time steps, the model can miss trends or cascading delays.

### GPS-Only Location Data

Although the dataset includes precise latitude and longitude, it lacks contextual
location fields such as city, state, or route identifiers. This makes it harder to
analyze trends regionally or understand how geography affects delivery performance.

### No Product Type Information

All shipments are treated thesame, regardless of what’s being delivered. However,
different types of cargo—such as perishable food, electronics, or industrial
equipment—may be more or less sensitive to delays or environmental conditions. Without
this information, the model may overlook key risk differences.

### Limited Extreme Disruption Data

The dataset may not contain many examples of high-impact disruptions such as natural
disasters, labor strikes, or system-wide breakdowns. As a result, models trained
on this data may not perform well under rare but critical scenarios that demand
fast and accurate predictions.

