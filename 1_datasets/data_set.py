
# 📘 README — Dynamic Supply Chain & Logistics Dataset

## 🗂️ Dataset Overview
This dataset originates from Kaggle’s Logistics and Supply Chain Dataset and captures the real-world operations of a logistics network operating in Southern California. The data spans a period from January 2021 to January 2024 and is structured to provide detailed, hour-by-hour records of logistics activity.

It incorporates a wide range of variables, reflecting the complexities of modern supply chain environments. Data was collected from GPS tracking systems, IoT sensors, warehouse management software, and external sources like weather and traffic APIs. The dataset includes observations for different modes of transportation—trucks, drones, and rail—offering a comprehensive view of logistics operations across urban and intermodal transport corridors.

## 🧠 Modeling the Domain: A Non-Technical Explanation

### 🎯 Project Goal
The primary objective of this project was to design a predictive model that can anticipate disruptions, forecast delays, and classify risk levels in the logistics process. By doing so, supply chain managers can make proactive decisions that reduce operational costs, improve on-time delivery, and better allocate resources.

### 🧱 How We Structured the Data
We approached the modeling task by treating each row in the dataset as a snapshot in time—an observation of a specific shipment, at a specific moment, under certain operational, environmental, and behavioral conditions.

This data was structured into a flat table, which is common in applied machine learning. Each row contains features such as the vehicle’s real-time GPS coordinates, the level of port congestion at the time, the temperature of the cargo, and whether the handling equipment was available at the warehouse.

We opted for this structure because it allows for rapid development of classification and regression models. The simplicity of a tabular format also enables clear visualizations, explainability, and reproducibility across platforms and tools like Python, R, or Excel.

## 🖼️ Feature Flow Diagram: How the Variables Connect
C:\Users\alema\Downloads\supply_chain_modeling.md
```
                     ┌────────────────────┐
                     │   Vehicle & Route  │
                     │  ────────────────  │
                     │  GPS Coordinates   │
                     │  Fuel Consumption  │
                     │  Driver Behavior   │
                     └────────┬───────────┘
                              │
                              ▼
        ┌──────────────┬───────────────────────┬───────────────┐
        │ Traffic &    │ Warehouse & Inventory │ Environmental │
        │ Congestion   │ Levels, Lead Time     │ Factors       │
        └──────────────┴───────────────────────┴───────────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │  Delivery Risk Outcome │
                  │ (Risk Class & Delay)   │
                  └────────────────────────┘
```

This diagram shows how different data sources (such as route data, traffic patterns, and warehouse activity) flow into predictive variables like risk classification or delivery time deviation. These insights enable logistics planners to act in advance rather than react to delays or failures.

## 🧾 Dataset Structure

- **Time Period**: The data covers a continuous timeline from January 1, 2021 to January 2024, with records at hourly intervals.
- **Variables**: There are 27 columns in the dataset, each tracking a different facet of logistics or supply chain activity.
- **Format**: The dataset is stored in CSV format. The first column contains timestamps, with headers labeling each variable clearly.

## 🔑 Key Variables Breakdown

### 📍 Location Data
- `vehicle_gps_latitude`, `vehicle_gps_longitude`: These fields capture the real-time position of each vehicle. Although detailed, the GPS coordinates are raw and not aggregated into higher-level geographies like cities or states.

### 🚚 Vehicle Performance
- `fuel_consumption_rate`: Indicates fuel efficiency in liters per hour.
- `eta_variation_hours`: Shows how far ahead or behind schedule a shipment is compared to its estimated time of arrival.

### 🏭 Operational Factors
- `traffic_congestion_level`: Reflects real-time traffic bottlenecks (0 = low congestion, 10 = severe).
- `warehouse_inventory_level`: Indicates stock availability at a warehouse location.
- `loading_unloading_time`: Tracks time spent on logistics handoffs.
- `handling_equipment_availability`: Denotes whether equipment like forklifts were operational at the time.

### 🌤 Environmental Conditions
- `weather_condition_severity`: A severity score ranging from 0 (clear) to 1 (extreme).
- `port_congestion_level`: A separate congestion metric reflecting delays at shipping terminals.

### 📊 Performance Metrics
- `delivery_time_deviation`: Captures how early or late a shipment arrives relative to its scheduled delivery (used as a regression target).
- `risk_classification`: Categorical label that classifies each shipment as Low, Moderate, or High risk (used for classification tasks).

## 🧩 Complete Feature Summary

| **Category**         | **Feature**                         | **Description**                             |
|----------------------|-------------------------------------|---------------------------------------------|
| Location             | vehicle_gps_latitude / longitude    | Real-time shipment location (GPS coords)    |
| Vehicle Performance  | fuel_consumption_rate               | Liters per hour                             |
|                      | eta_variation_hours                 | Difference from estimated arrival time      |
| Warehouse & Ops      | warehouse_inventory_level           | Units in stock at warehouse                 |
|                      | loading_unloading_time              | Time to load/unload (hrs)                   |
|                      | handling_equipment_availability     | 0 (unavailable) to 1 (fully available)      |
| Traffic & Ports      | traffic_congestion_level            | Scale of 0–10                                |
|                      | port_congestion_level               | Port delay score (0–10)                     |
| Environment          | weather_condition_severity          | 0 (clear) to 1 (severe)                     |
| IoT & Condition      | iot_temperature                     | °C inside cargo containers                  |
|                      | cargo_condition_status              | 0 (poor) to 1 (good)                         |
| Risk & Behavior      | driver_behavior_score               | 0 (unsafe) to 1 (safe)                       |
|                      | fatigue_monitoring_score            | 0 (rested) to 1 (fatigued)                  |
| Targets              | disruption_likelihood_score         | Probability of a disruption (0–1)           |
|                      | delay_probability                   | Probability of delay (0–1)                  |
|                      | risk_classification                 | Low/Moderate/High                           |
|                      | delivery_time_deviation             | Hours deviated from expected delivery       |

## 🔍 Key Use Cases

This dataset is valuable for several real-world applications in logistics, including:

- **Risk Prediction**: Use machine learning to classify whether a shipment is likely to experience problems (e.g., High Risk).
- **Delivery Forecasting**: Build regression models to estimate delivery delays in real time.
- **Route Optimization**: Use GPS and traffic data to identify better paths through congested regions.
- **Predictive Maintenance**: Monitor driver fatigue and vehicle fuel consumption to schedule maintenance before breakdowns.
- **Inventory Planning**: Use demand history and lead times to improve warehouse stock levels.

## Potential Modeling Flaws and Limitations

### Oversimplification
Although the dataset is detailed, it simplifies many aspects of real-world supply chains. It does not model upstream and downstream dependencies or cascading failures that can occur due to a single delay.

### Assumption of Linearity
Many modeling approaches assume a linear relationship between input features and outcomes. However, in real logistics systems, non-linear or threshold effects often occur—where small issues suddenly create major delays (e.g., a 10-minute customs delay causing a missed rail connection).

### Static Snapshots
This dataset treats each record independently. It does not track how a shipment’s condition evolves over time or across locations. This limits our ability to model long-term trends or predict evolving risks.

### Geographic Limitations
The dataset is constrained to Southern California, which means any models trained on it may not generalize well to international or rural supply chain settings.

### Location Granularity
While GPS coordinates are available, there are no fields for city, state, or country. This makes it difficult to group records by geographic region or analyze regional trends.

### Missing Product-Level Information
One notable gap is the lack of product or commodity type in the shipment data. Risk and delay patterns can vary significantly between perishable goods, electronics, or heavy industrial components, but this context is missing.

### Temporal Gaps or Constraints
Despite claiming coverage through 2024, the dataset may only include 13 days of records, which could limit its usefulness in long-term forecasting or seasonal trend analysis.

---

## 🧰 Data Cleaning & Splitting Script

Below is the Python code used to clean and prepare the dataset for modeling. This includes converting timestamps, handling missing values, converting categorical data, and splitting the dataset into training and testing subsets.

```python
import pandas as pd
from sklearn.model_selection import train_test_split

def clean_dataset(input_file, output_file):
    """
    Load and clean the dataset.

    Steps:
    - Converts 'timestamp' to datetime
    - Fills missing values using forward fill
    - Converts 'risk_classification' to a categorical variable
    - Saves cleaned dataset to output_file
    """
    df = pd.read_csv(supply_chain_data)

    # Convert timestamp to datetime
    try:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    except Exception as e:
        print("Error converting timestamp:", e)

    # Fill missing values (forward fill as placeholder)
    df.fillna(method='ffill', inplace=True)

    # Convert risk classification to category
    if 'risk_classification' in df.columns:
        df['risk_classification'] = pd.Categorical(df['risk_classification'])

    # Save cleaned dataset
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

    return df

def split_data(cleaned_supply_chain_data.csv, train_file, test_file, test_size=0.2):
    """
    Split cleaned data into training and test sets and save to CSV.

    Parameters:
    - test_size: Proportion of data to use for testing
    - Stratifies split based on 'risk_classification' if available
    """
    df = pd.read_csv(cleaned_supply_chain_data.csv)

    stratify_col = df['risk_classification'] if 'risk_classification' in df.columns else None

    train_df, test_df = train_test_split(
        df,
        test_size=test_size,
        random_state=42,
        stratify=stratify_col
    )

    train_df.to_csv(train_file, index=False)
    test_df.to_csv(test_file, index=False)

    print(f"Training data saved to {train_file}")
    print(f"Testing data saved to {test_file}")

    return train_df, test_df
