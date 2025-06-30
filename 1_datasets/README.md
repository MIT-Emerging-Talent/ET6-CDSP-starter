<!-- markdownlint-disable MD013 MD033 MD032 MD049-->
# Datasets

we have a **`raw_data`** folder that contains the original raw datasets used in preprocessing.  
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
