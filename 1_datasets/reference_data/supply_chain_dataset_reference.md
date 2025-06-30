
# 📦 Supply Chain Dataset Documentation

Due to this uncertainty, we may not use this dataset in our final analysis,  
but we have decided to keep it for reference and potential future use.

---

## 📌 Dataset Source

- **Origin**: [Kaggle - Supply Chain Dataset]  
[https://www.kaggle.com/datasets/natasha0786/supply-chain-dataset](https://www.kaggle.com/datasets/natasha0786/supply-chain-dataset)  
- **Curator**: Natasha0786 (Kaggle contributor)  
- **Type**: Synthetic dataset modeling global supply chain operations  
- **Format**: CSV file containing structured tabular data  

---

## 🧱 Original Data Structure

The dataset consists of supply chain records from global suppliers, with each row
capturing detailed logistics and delivery attributes tied to a product-supplier
combination.

### 📋 Column Descriptions
<!-- markdownlint-disable MD013 -->

| Column Name                     | Description                                                                                 |
|--------------------------------|---------------------------------------------------------------------------------------------|
| `warehouse_inventory_level`    | Volume of inventory at the warehouse (numeric).                                             |
| `handling_equipment_availability` | Readiness of shipping/loading equipment at the warehouse (scale from 0 to 1).              |
| `order_fulfillment_status`     | Degree to which supplier fulfills orders successfully (0 = none, 1 = fully complete).       |
| `weather_condition_severity`   | Environmental severity impacting logistics (0 = clear, 1 = severe).                         |
| `shipping_costs`               | Total cost of shipping goods from supplier to destination (in dollars).                     |
| `supplier_reliability_score`   | Metric representing the consistency and reliability of the supplier (scale from 0 to 1).    |
| `lead_time_days`               | Time (in days) from order placement to delivery.                                            |
| `historical_demand`            | Historical average demand for the product over a defined period.                            |
| `cargo_condition_status`       | Measure of cargo condition upon arrival (0 = poor, 1 = perfect).                            |
| `route_risk_level`             | Index of transportation route risk (higher values indicate higher risk).                    |
| `customs_clearance_time`       | Duration (in days) for customs procedures to complete.                                      |
| `disruption_likelihood_score`  | Estimated probability of delays or disruption on the supply route.                          |
| `delay_probability`            | Likelihood that the delivery will not arrive on schedule (0 = very unlikely, 1 = very likely). |
| `risk_classification`          | Categorical label indicating shipment risk: High, Moderate, or Low.                         |
| `delivery_time_deviation`      | Difference between scheduled and actual delivery time (in days).                            |
| `product_id`                   | Unique identifier assigned to the product being shipped.                                    |
| `supplier_id`                  | Unique identifier of the supplier providing the product.                                    |
| `supplier_country`             | Country in which the supplier is located.                                                   |

<!-- markdownlint-enable MD013 -->

---

## ⚠️ Dataset Limitations and Considerations

1. **Synthetic Nature**: Data is fabricated to mimic real supply chains;  
   it may not fully capture operational complexity.  
2. **Duplicate Patterns**: Several rows repeat with slight modifications  
   (often across different suppliers for the same product).  
3. **Category Imbalance**: Some supplier countries, routes, or risk types are  
   more frequent, which may skew statistical models.  
4. **Unspecified Units**: While some columns are clearly labeled, others require
   contextual assumptions (e.g. condition scores or risk levels).  
5. **Numerical Variability**: Columns vary in scale—normalization or  
   transformation may be needed before modeling.  

---

## 🔁 Recreating or Adapting the Dataset

You can recreate the dataset workflow using the following steps:

1. Download the original file from  
   [Kaggle](https://www.kaggle.com/datasets/natasha0786/supply-chain-dataset)  
   and save it as `dynamic.csv`.  
2. Use a data processing tool such as Python (with pandas) or Excel to explore  
   and modify the dataset.  
3. Remove irrelevant or redundant columns depending on your analysis goals.  
4. Apply filters based on supplier country or product ID  
   to create focused subsets.  
5. Ensure the dataset is free from missing values and duplicates before  
   exporting your final version.  

---

## ✅ Data Cleaning and Preparation Summary

After importing the dataset from Kaggle, a series of preprocessing steps were
performed to streamline the data and tailor it for focused analysis—
specifically targeting supplier performance within the United States. The
objective was to eliminate irrelevant features, reduce complexity, and improve
the dataset’s analytical value.

---

## 🔧 Changes Applied

### 🔹 Removed 8 Columns

- `handling_equipment_availability`  
- `supplier_reliability_score`  
- `historical_demand`  
- `cargo_condition_status`  
- `disruption_likelihood_score`  
- `risk_classification`  
- `product_id`  
- `supplier_id`  

#### Python Code

```python
df = df.drop(columns=[
    'handling_equipment_availability', 
    'supplier_reliability_score',
    'historical_demand',
    'cargo_condition_status',
    'disruption_likelihood_score',
    'risk_classification',
    'product_id',
    'supplier_id',

    ])
```

**Reasoning:**  
These columns were removed due to redundancy, lack of interoperability, or limited
relevance to the core analysis. For example:

- Identifiers like `product_id` and `supplier_id` are not analytically  
  meaningful for aggregate insights.  
- Several risk-related scores overlap with more interpretable features like
  `delay_probability` and `route_risk_level`.

---

## 🌍 Filtered to U.S. Suppliers Only

**Condition Applied:**  

```python
df = df[df['supplier_country'] == 'USA']
```

**Reasoning:**  
Focusing exclusively on suppliers based in the United States helps eliminate
variability caused by international trade factors such as customs delays,
geopolitical risks, or cross-border shipping regulations. This allows for a more
controlled and region-specific analysis of supply chain performance.

---

## ✅ Data Integrity Checks

- **No missing values**: Verified that all columns have complete data.  
- **No duplicate rows**: Ensured that each record is unique.  

---

## 💾 Final Output

The cleaned dataset was saved as:

```python
df.to_csv('dynamic_cleared.csv', index=False)
print("Data cleared and saved to dynamic_cleared.csv")
```
