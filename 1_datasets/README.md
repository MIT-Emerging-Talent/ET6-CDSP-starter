# Datasets

## Logistics and Supply Chain Dataset

### Source

- **Platform**: [Kaggle](https://www.kaggle.com/datasets/datasetengineer/logistics-and-supply-chain-dataset)
- **Uploader**: `datasetengineer`  
- **Listed Author**: `Austin Lasseter`  
- **Access**: Publicly available for educational and research use  

---

### Structure and Content

- Covers logistics operations in Southern California **(Jan 2021–Jan 2024)**
- Provides **hourly** data on transport, warehousing, and routing  
- Focuses on high-traffic urban corridors  
- Useful for analyzing efficiency, risks, and delivery performance

#### Features

- **Timestamp**: Date and time of the logistics event  
- **Vehicle GPS Latitude / Longitude**: Vehicle’s geolocation coordinates  
- **Fuel Consumption Rate**: Liters of fuel consumed per hour  
- **ETA Variation (hours)**: Gap between estimated and actual arrival  
- **Traffic Congestion Level**: Congestion level on a 0–10 scale  
- **Warehouse Inventory Level**: Units currently in warehouse  
- **Loading/Unloading Time**: Time in hours to load/unload cargo  
- **Handling Equipment Availability**: Equipment status (0 = no, 1 = yes)  
- **Order Fulfillment Status**: Fulfillment on time (0 = no, 1 = yes)  
- **Weather Condition Severity**: Weather impact (0–1 scale)  
- **Port Congestion Level**: Port congestion level (0–10 scale)  
- **Shipping Costs**: Cost of shipping in USD  
- **Supplier Reliability Score**: Reliability score (0–1 scale)  
- **Lead Time (days)**: Average supplier delivery time  
- **Historical Demand**: Past logistics service demand (units)  
- **IoT Temperature**: Temperature from sensors (°C)  
- **Cargo Condition Status**: Cargo condition (0 = poor, 1 = good)  
- **Route Risk Level**: Risk rating for the route (0–10 scale)  
- **Customs Clearance Time**: Hours required for customs processing  
- **Driver Behavior Score**: Driver pattern score (0–1 scale)  
- **Fatigue Monitoring Score**: Driver fatigue score (0–1 scale)  

#### Target Variables

- **Disruption Likelihood Score**: Probability of disruption (0–1)  
- **Delay Probability**: Likelihood of delivery delay (0–1)  
- **Risk Classification**: Risk category — Low, Moderate, High  
- **Delivery Time Deviation**: Hours deviated from expected delivery  

---

### Data Collection

Collected from:

- GPS tracking systems  
- IoT sensors on vehicles and warehouses  
- Warehouse management systems  
- External sources (e.g., weather and port data)  

The dataset is anonymized to preserve privacy while retaining analytical value.

---

### Possible Limitations

- The dataset is not specific to the **retail sector**, which may limit direct
alignment with our focus on retail supply chains.  
- All data is sourced from **Southern California**, potentially limiting
generalizability to other U.S. regions with different infrastructure and
logistics environments.

---

### Relevance to Our Project

This dataset supports our investigation of **delivery
delays in the U.S. retail supply chain** through:

- **Delay-focused target variables** such as delay probability and delivery time
deviation
- **Contextual features** that influence delays, including:
  - Traffic congestion  
  - Weather conditions  
  - Route risk  
  - Inventory levels and equipment availability  
- **General logistics operations** applicable to retail supply chains, despite
not being retail-specific

---

### Recreating the Dataset

To recreate the cleaned dataset:

1. **Download the raw CSV**  
   From [Kaggle](https://www.kaggle.com/datasets/datasetengineer/logistics-and-supply-chain-dataset)
   File: `dynamic_supply_chain_logistics_dataset.csv`

2. **Run the cleaning script**  
   - Drops 3 irrelevant columns: `vehicle_gps_latitude`, `vehicle_gps_longitude`,`fuel_consumption_rate`
   - Confirms no missing or duplicate values
   - Saves output as `cleaned_data.csv`

The script is available in `final_data_with_scripts/cleaning_script.py`.
