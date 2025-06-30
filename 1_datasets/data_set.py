# 📘 Supply Chain & Logistics Dataset

## 🗂️ Dataset Overview
This dataset originates from Kaggle’s Logistics and Supply Chain Dataset and captures real-world operations in Southern California from January 2021 to January 2024. It includes data from GPS, IoT sensors, warehouse systems, and external sources like weather and traffic APIs.

## 🧠 Modeling the Domain: A Non-Technical Explanation

### 🎯 Project Goal
Build predictive models to anticipate disruptions, forecast delays, and classify logistics risk to improve planning and efficiency.

### 🧱 How We Structured the Data
Each row is a snapshot of a shipment in time. This flat, tabular structure allows easy use in machine learning tools and enhances model explainability.

## 🖼️ How the Variables Connect
```
         ┌────────────────────────────┐
         │     Logistics-Related      │
         │  • Port Congestion         │
         │  • Fuel Consumption        │
         │  • Loading Time
         └────────────┬───────────────┘
                      │
    ┌─────────────────▼─────────────────┐
    │          Environmental            │
    │  • Disruption Likelihood Score    │
    │  • Temperature (Cargo/Weather)    │
    └────────────┬────────────┬────────┘
                 │            │
     ┌───────────▼──┐    ┌────▼──────────┐
     │ Human Factors │    │ Economic Factors │
     │ • Fatigue Score │  │ • Shipping Costs │
     │ • Driver Behavior│ │ • Historical Demand │
     └───────────┬────┘    └──────────────┬────┘
                 │                        │
                 ▼                        ▼
           ┌────────────────────────────────┐
           │     Delivery Risk Outcome      │
           │  (Delay & Risk Classification) │
           └────────────────────────────────┘
```

## ⚠️ Modeling Flaws & Limitations

- **Oversimplification**: No upstream/downstream chain effects.
- **Linearity Assumption**: Ignores thresholds or non-linear impact.
- **Static Snapshots**: Can't model shipment evolution over time.
- **Geographic Gaps**: No location labels beyond GPS.
- **No Product Types**: Omits perishable vs. durable distinctions.
- **Temporal Limits**: May only reflect short windows of time.
