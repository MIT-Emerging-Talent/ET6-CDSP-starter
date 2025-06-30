# Datasets

## Logistics and Supply Chain Dataset

### Source

This dataset is publicly available on Kaggle:  
[https://www.kaggle.com/datasets/datasetengineer/logistics-and-supply-chain-dataset]
Uploaded by the user "datasetengineer" for educational and research use.

### Structure and Content

The dataset captures detailed logistics and supply chain operations from a
Southern California network spanning **January 2021 to January 2024**. It provides
**hourly** data on transportation, warehouse management, route planning, and
real-time monitoring across high-traffic urban corridors.

The data offers insights into operational efficiency, risk factors, and supply
chain performance.

Features include:

- **Timestamp**: Date and time of the recorded logistics event (hourly).  
- **Vehicle GPS Latitude**: Latitude coordinate of the vehicle’s location.  
- **Vehicle GPS Longitude**: Longitude coordinate of the vehicle’s location.  
- **Fuel Consumption Rate**: Fuel used by the vehicle per hour (liters/hour).  
- **ETA Variation (hours)**: Difference between estimated and actual arrival time.
- **Traffic Congestion Level**: Traffic intensity on the route (scale 0–10).  
- **Warehouse Inventory Level**: Number of units currently stored in the warehouse.
- **Loading/Unloading Time**: Time taken to load or unload cargo (hours).  
- **Handling Equipment Availability**: Availability of equipment like
forklifts (0 = no, 1 = yes).  
- **Order Fulfillment Status**: Indicates if an order was fulfilled on time
(0 = no, 1 = yes).
- **Weather Condition Severity**: Severity of weather impacting operations (0–1 scale).
- **Port Congestion Level**: Level of congestion at the shipping port (0–10 scale).
- **Shipping Costs**: Cost of shipping in US dollars.  
- **Supplier Reliability Score**: Supplier trustworthiness rating (0–1 scale).  
- **Lead Time (days)**: Average supplier delivery time.  
- **Historical Demand**: Past demand volume for logistics services (units).  
- **IoT Temperature**: Temperature measured by IoT sensors (°C).  
- **Cargo Condition Status**: Indicates the cargo’s condition as detected by
IoT monitoring (0 = poor, 1 = good).
- **Route Risk Level**: Risk score for the logistics route (0–10 scale).  
- **Customs Clearance Time**: Time required for customs processing (hours).  
- **Driver Behavior Score**: Driver’s driving pattern rating (0–1 scale).  
- **Fatigue Monitoring Score**: Driver fatigue level (0–1 scale).

**Target variables:**

- **Disruption Likelihood Score**: Probability of disruption in logistics (0–1 scale).
- **Delay Probability**: Chance of shipment delay (0–1 scale).  
- **Risk Classification**: Categorical risk level (Low, Moderate, High).  
- **Delivery Time Deviation**: Difference in hours from expected delivery time.

These features enable analysis of delay causes, risk assessment, and process  
optimization.

### Data Collection

Collected via:

- GPS tracking devices  
- IoT sensors installed on vehicles and warehouses  
- Warehouse management software  
- External datasets (e.g., weather, port congestion)  

The data is anonymized and processed to preserve analytical value while  
protecting privacy.

### Possible Limitations

- The dataset does not explicitly focus on the retail sector, which limits direct
  alignment with our focus on retail supply chain delivery delays.
- All data is from Southern California, which may reduce the generalizability of
  findings to other U.S. regions with different logistics challenges and infrastructure.

### Relevance to Our Project

This dataset supports our investigation of delivery delays in the U.S. retail
supply chain by offering delay-related target variables and contextual features
like traffic, weather, and route risk. While not retail-specific, it captures
key logistics challenges relevant to our analysis.

### Recreating the Dataset

---
