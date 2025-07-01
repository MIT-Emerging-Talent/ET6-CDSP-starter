# Dataset Documentation: DataCo Supply Chain Dataset

## Overview

This dataset was reviewed as part of our preliminary data exploration phase.
Although it contains real-world transactional data and is rich in customer and
product attributes, it does not align with our project’s research objectives.
Specifically, the features necessary to analyze the factors contributing to
delivery delays are either absent or not sufficiently detailed. As a result, this
dataset was not selected for further analysis.

---

## I. Data Source

The **DataCo Supply Chain Dataset** was originally published by **DataCo
International** and is publicly accessible via platforms such as Kaggle and Data
World. It is intended for educational and practical use in data analytics,
machine learning, and supply chain optimization.

- **Original Publisher:** DataCo International  
- **Accessed via:** Kaggle  
- **Files Included:**
  - `DataCoSupplyChainDataset.csv` – Main structured dataset
  - `DescriptionDataCoSupplyChain.csv` – Variable descriptions and metadata
  - `Tokenized_access_logs.csv` – Unstructured access log data *(not used in our
    review)*

The structured dataset includes over **180,000 records** across **53 features**,
encompassing information on orders, customers, products, shipping, and financial
transactions.

---

## II. Dataset Structure

Each row represents a single customer order, including details on shipping
logistics, customer demographics, product categories, and profitability metrics.
Selected key variables include:

- **Shipping Mode** – Shipment type (e.g., Standard Class, First Class)
- **Product Category** – Item classification (e.g., Office Supplies, Technology)
- **Order Date / Shipping Date** – Date the order was placed and shipped
- **Delivery Status** – Outcome of the delivery (e.g., Delivered, Late, Cancelled)
- **Late Delivery Risk** – Predicted risk score of delivery delay
- **Product Price** – Unit sale price of the product
- **Order Quantity** – Number of items per order
- **Profit per Order** – Revenue margin generated per transaction
- **Customer Segment** – Segment label (Consumer, Corporate, Home Office)

This dataset can support analyses in profitability, shipping performance,
customer segmentation, and fulfillment efficiency.

---

## III. Limitations and Considerations

Despite its size and structure, the dataset has several limitations which
influenced our decision to not proceed with its use:

- **Feature Gaps** – Key variables directly affecting delivery delays (e.g.,
  carrier reliability, traffic/weather data, distance, warehouse location) are
  missing.
- **Data Age** – The dataset appears outdated, which may reduce its relevance to
  current logistics operations.
- **Missing Values** – Incomplete entries in delivery-related and financial
  columns.
- **Data Format Issues** – Some columns, particularly date and numeric fields,
  require preprocessing.
- **Delivery Bias** – The data skews heavily toward successful deliveries,
  limiting failure-case analysis.
- **Limited Geographic Context** – Location data lacks granularity (e.g., zip
  codes, coordinates).

---

## IV. Reproducibility and Access

The dataset can be accessed and reused for other exploratory purposes:

- **Access Source:** [Kaggle – DataCo Supply Chain
  Dataset](https://www.kaggle.com/datasets)
- **Preprocessing Recommendations:**
  - Normalize date and numeric formats
  - Address missing values via appropriate imputation
  - Consider enriching with external geolocation or weather data for delivery
    modeling

---

## Conclusion

While the **DataCo Supply Chain Dataset** is valuable for general supply chain
analysis and instructional use, it does not meet the specific requirements of our
research into delivery delays. We have therefore opted to explore alternative
datasets better aligned with our research objectives.
