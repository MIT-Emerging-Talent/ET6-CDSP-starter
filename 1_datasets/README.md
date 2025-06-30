<!-- markdownlint-disable MD013 MD033 MD032 MD049-->
# Datasets

we have a **`raw_data`** folder that contains the original raw files used in preprocessing.  
Our data comes from the following sources:

- **IRENA Renewable Energy Statistics** – Published by the *International Renewable Energy Agency (IRENA)*, this dataset provides annual data on renewable energy capacity and generation, including both on-grid and off-grid solar PV deployment across countries and regions.

- **UN Comtrade** – The *United Nations International Trade Statistics Database*, offering detailed trade data on solar-related products (e.g., panels, inverters), helping us understand import/export trends in conflict-affected and stable regions.

1. **[Off-grid Renewable Energy Statistics 2024](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-08-repo/blob/main/1_datasets/raw_data/IRENA_OFGStats.raw.xlsx)**
2. **[On-grid Renewable Energy Statistics 2024](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-08-repo/blob/main/1_datasets/raw_data/IRENA_Stats_extract_2025_H1_raw.xlsx)**
3. **[UN Comtrade data](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-08-repo/blob/main/1_datasets/raw_data/UN_Comtrade_imports_dataset_raw.xlsx)**
  
Additionally, we have **`non-technical explaination of domain modeling.md`** file

---

## [Off-grid Renewable Energy Statistics 2024](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-08-repo/blob/main/1_datasets/raw_data/IRENA_OFGStats.raw.xlsx)

- This dataset is from the International Renewable Energy Agency, which
is an intergovernmental organization that promotes the adoption and
sustainable use of renewable energy worldwide.
- The file consists of two sheets:
the first one is an ‘about’ file, and the other is the ‘data’ sheet that
contains the actual data. The data sheet consists of 16 columns, namely:
Region, UN sub-region, Country, IRENA label, ISO code, Flow, Group technology,
Sub-technology, Technology, Product code, DataType, Value, Unit, Year, Ptype, Publication.
- **How it was collected**
  - According to the [measurement and estimation](https://www.irena.org/publications/2018/Dec/Measurement-and-estimation-of-off-grid-solar-hydro-and-biogas-energy) file of IRENA:
    - The data was collected from a mix of national databases, international organizations
    (like GOGLA and SNV), and online sources such as project reports and news articles.
    Where direct data was unavailable, IRENA used estimation methods (e.g.,
    trade data, technical assumptions) and peer review to validate and fill gaps.
- **Some possible flaws are:**
  - There is no a direct connection between off-grid renewable energy and
   conflict countries.
  - The dataset has different unit types in the Units column, depending
   on the technology utilized.
  - It has quite a lot of zero values, especially in our targeted countries.
- **<p>How it is related to our problem?<br>**
    This dataset will be a huge asset to our research question, it’s like
    a baseline layer dataset, for example:
  - We can use the “value” column to get a sense of the deployment or
    utilization rate of different renewable energy sources and make a
    comparison between conflict and non-conflicts countries.
  - Identify whether conflicts correlate to a slowdown, shift or
    an increase in solar pv utilization.<br>

  However, alone, it won’t be enough; we’ll need to introduce other
  resources to showcase conflicts regions, e.g (ACLED, UDCP)</p>

---

## [On-Grid  Renewable Energy Statistics 2024](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-08-repo/blob/main/1_datasets/raw_data/IRENA_Stats_extract_2025_H1_raw.xlsx)

- This dataset is from the **International Renewable Energy Agency**, which
is an intergovernmental organization that promotes the adoption and
sustainable use of renewable energy worldwide.  
_Showing electricity access by country from 2000 to 2025_

- **Quantitative Data**  
Format: Excel (.xlsx) file  
It contains three sheets:  
  - **Country:**  
Each row represents a region(continents); Columns include Sub-region, country, ISO3 Code, M49 Code, renewable or nonrenewable, Group Technology, technology, sub-technology, producer type(on-grid and off-grid electricity), year and sum of Electricity Installed Capacity (MW)
  - **Region:**
Each row represents a region; Columns include year, renewable or nonrenewable, Group Technology and Sum of Electricity Installed Capacity (MW)
  - **Global:**
Columns include year, renewable or nonrenewable, Group Technology and Sum of Electricity Installed Capacity (MW)

- **How it was collected**
  - According to the [measurement and estimation](https://www.irena.org/publications/2018/Dec/Measurement-and-estimation-of-off-grid-solar-hydro-and-biogas-energy) file of IRENA:
    - The data was collected from a mix of national databases, international organizations
    (like GOGLA and SNV), and online sources such as project reports and news articles.
    Where direct data was unavailable, IRENA used estimation methods (e.g.,
    trade data, technical assumptions) and peer review to validate and fill gaps.

- **Some Possible flaws are:**
  - The dataset does not include _conflict status labels,_ so these must be added manually.
  - Some entries contain _missing or zero values_, which may indicate either a lack of reported data or no deployment during that period.

- **How can someone recreate it?**  
Go to [IRENA- Renewable Capacity Statistics 2025](https://www.irena.org/Publications/2025/Mar/Renewable-capacity-statistics-2025) , select the latest Renewable Capacity Statistics report, choose format: Excel or CSV and download the full dataset

- **<p>How it is related to our problem?<br>**
Look at how **reliance on the main power grid (on-grid electricity) drops in conflict-affected countries.**  
Since the electric grid often _gets damaged or becomes unreliable during conflict,_ we want to **track this decline and show how it affects energy access,** especially how people are forced to **shift** to off-grid solar or other backup sources.

> From the _Country_, _Region_, and _Global_ sheets, we aim to analyze how **armed conflicts influence solar PV deployment over time**. Specifically, we want to **compare conflict-affected versus non-conflict countries** to detect differences in growth, and examine **on-grid versus off-grid trends** to see if _conflicts are driving shifts toward off-grid solutions_ when infrastructure is damaged. _Regional groupings_ will help us identify **clusters or trends tied to specific conflict zones**. Additionally, **increases in solar capacity** can act as a _proxy for cleaner energy adoption_ in place of diesel or coal. The _Region_ and _Global_ sheets will provide **context—allowing us to contrast local deployment patterns in conflict areas with broader global and continental trends**, and assess whether **renewables are prioritized** or if _instability leads to a fallback on non-renewables_.
---

## [UN Comtrade Imports Data](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-08-repo/blob/6f1a08ecd0694b2366bf9896625c5510f18b63b6/1_datasets/raw_data/UN_Comtrade_imports_dataset_raw.xlsx)

- **The world's most comprehensive global trade data platform**
The United Nations Comtrade database aggregates detailed global annual and monthly trade statistics by product and trading partner for use by governments, academia, research institutes, and enterprises. Data compiled by the United Nations Statistics Division covers approximately 200 countries and represents more than 99% of the world's merchandise trade. Information can be extracted in a variety of formats, including API developer tools for integration into enterprise applications and workflows.

- **Possible flaws:**
  - The tables have many columns that are irrelevant to our purpose.
  - Some countries have missing data or no data at all.
  - The need to be familiar with the HS Commodity code to be comfortable with it.

- **How can someone recreate it?**
  - _Step 1_: Go to the UN Comtrade Website
    Navigate to the [modern data portal](https://comtradeplus.un.org/TradeFlow)

  - _Step 2_: Open the Data Query Tool
    On the homepage, click the large "Data" button in the main navigation menu at the top of the page. This will take you to the query builder.

  - _Step 3_: Configure Your Query Filters
  This is the most important part. You need to tell the database exactly what you're looking for. Fill out the filters on the left-hand side of the page.  
    Type of Product: Keep this as Goods.  
  **Frequency**: Select Annual.  
  **Period**: Select the range of years you want. Click on the box, select 2012 from the start year dropdown, and 2023 (or the latest available year) from the end year dropdown.  
  **Reporter**: This is the importing country. Click the box, type Nigeria, and select it from the list. (You can select multiple countries here if you want).  
  **Partner**: To get total imports from the entire world, select World.  
  Trade Flows: Select Import.  
  **HS (as reported) commodity codes**: This is where you enter the product codes.

  - _Step 4_: You can preview the data before downloading it in the preferred format.

- **<p>How it is related to our problem?<br>**
This data set provides detailed solar energy devices (panels, batteries, inverters) import data for the following countries in the period from 2007 to 2024:
- Syria
- Iraq
- Sudan
- South Sudan
- Palestine
- Mali
- Ethiopia
- Ukraine
- Yemen
- Libya
- Afghanistan
- Nigeria
- Central African Republic
- Somalia
- Pakistan
- Mozambique
- Myanmar

By observing this data set one can get valuable insights about the effect of conflicts and events on the overall deployment and use of solar energy. For example in 2013 in Pakistan a single coordinated attack in August  destroyed four 220 kV towers, cutting off some 100 MW to 15 districts and extending daily load‑shedding by several hours. By observing the imports data of solar panels and batteries to Pakistan in 2013 and 2014, one can notice a dramatic surge in the imported amounts of these products, which could indicate a clear shift to off grid solar energy as a result of that event (this is an initial observation that needs to be analyzed further to draw concrete results from it).

- **Here is a table that provides brief descriptions for some of the HS commodity codes used in this data set:**

| Category              | HS Code(s)        | Years      | Research Purpose                                                                 |
|-----------------------|-------------------|------------|----------------------------------------------------------------------------------|
| Solar Generation (DC) | 8541.40           | Before 2022 | Main code for all solar panels and semiconductor devices.|
|                       |                   |            | Was split into 8541.41, 8541.42, 8541.43 after 2022.                             |
| Solar Generation (DC) | 8541.42, 8541.43  | 2022+      | 8541.42: Bare photovoltaic cells (unassembled).                                  |
|                       |                   |            | 8541.43: Assembled PV panels ready for mounting.                                |
| Solar Generation (AC) | 8501.80           | 2022+      | For “AC Modules” – panels with built-in microinverters. Small but important.     |
| Productive Use        | 8501.71, 8501.72  | 2022+       | Complete generator sets (panel + electronics). Reported as one commodity.        |
|                       | 851310            | All Years  |Lamps; portable, electric, designed to function by their own source of energy (Solar Lanterns)|
| Energy Storage        | 8507.60           | All years  | Lithium-ion batteries. Crucial for off-grid systems.                             |
| Power Conversion      | 8504.40           | All years  | Static converters, including inverters and charge controllers.                  |
