# Raw Datasets for Blockchain for Financial Inclusion: Identity and Credit Access for Migrants Research

The folder `raw_datasets_files` contains the raw datasets used for our research into whether blockchain-based identity and credit systems can help address financial exclusion among migrants and refugees. As per the repository guidelines, these files are kept in their original, unmodified state.

---

## 1. International Migrant Stock 2024 Datasets

**Source:** United Nations Department of Economic and Social Affairs (DESA), Population Division.

**Official Source Link:** [https://www.un.org/development/desa/pd/content/international-migrant-stock](https://www.un.org/development/desa/pd/content/international-migrant-stock)

**Description:** These datasets provide the latest United Nations estimates of the numbers and characteristics of international migrants globally, covering the period from 1990 to 2024. They include estimates of the total number of international migrants by sex, as well as their places of origin and destination, for 233 countries and areas.

**Relevance to Problem:** This data is foundational for understanding the scale and demographics of the international migrant and refugee population, which are our target groups for addressing financial exclusion. It provides baseline statistics on where migrants are located and their characteristics, which can inform the scope and design of identity and credit systems.

**Classification by Data Type:**

* **Quantitative (Numerical) Data:** Primarily discrete (counts of migrants, populations) and continuous (percentages, rates of change).
* **Time Series Data:** Contains sequential data points collected over specific time intervals (1990-2024).

**Classification by Structure:**

* **Structured Data:** Organized in a consistent, predefined tabular format (Excel files).

**Classification by Access Type:**

* **Public Data:** Freely available from the UN website.

**Associated Files (Local raw copies will be named `.raw.xlsx`):**

* [`undesa_pd_2024_ims_stock_by_sex_and_destination.raw.xlsx`](/1_datasets/raw_datasets_files/undesa_pd_2024_ims_stock_by_sex_and_destination.raw.xlsx)
  * **Contents:** International migrant stock, total population, migrant stock as a percentage of total population, female migrants as a percentage of migrant stock, and annual rate of change of migrant stock – all by sex and destination (1990-2024).
* [`undesa_pd_2024_ims_stock_by_sex_and_origin.xlsx`](/1_datasets/raw_datasets_files/undesa_pd_2024_ims_stock_by_sex_and_origin.raw.xlsx)
  * **Contents:** International migrant stock and female migrants as a percentage of migrant stock – by sex and origin (1990-2024).
* [`undesa_pd_2024_ims_stock_by_sex_destination_and_origin.xlsx`](/1_datasets/raw_datasets_files/undesa_pd_2024_ims_stock_by_sex_destination_and_origin.raw.xlsx)
  * **Contents:** International migrant stock by sex, destination, and origin (1990-2024), including specific snapshots for "both sexes combined" by region of destination and origin for various years (1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024).

---

## 2. UNHCR Refugee Data Finder (Refugee Statistics)

**Source:** United Nations High Commissioner for Refugees (UNHCR).

**Official Source Links:**

* [https://www.unhcr.org/refugee-statistics](https://www.unhcr.org/refugee-statistics)
* [https://www.unhcr.org/refugee-statistics/data-summaries](https://www.unhcr.org/refugee-statistics/data-summaries)

**Description:** This resource provides global refugee statistics, summarizing the number of forcibly displaced people worldwide, including refugees, internally displaced persons (IDPs), asylum-seekers, and stateless individuals. It also highlights key demographics such as the number of children displaced and where refugees typically reside.

**Relevance to Problem:** This data offers crucial high-level statistics on the total population of forcibly displaced individuals, providing context for the scope of financial exclusion issues and the need for identity solutions. It helps quantify the target demographic for our research.

**Classification by Data Type:**

* **Quantitative (Numerical) Data:** Primarily discrete (counts of displaced persons, refugees, IDPs, asylum-seekers, stateless individuals).
* **Time Series Data:** Provides figures as of a specific point in time (e.g., end of 2024), and mentions trends over years (children born as refugees between 2018-2024).

**Classification by Structure:**

* **Unstructured/Semi-structured Data (from web summaries):** The initial information is presented as a concise summary on web pages rather than a downloadable structured file. While the underlying data may be structured, the direct source link points to a summary.

**Classification by Access Type:**

* **Public Data:** Freely accessible on the UNHCR website.

---

## 3. Refugee Economies (Oxford) Dataset

**Source:** Refugee Economies Programme, University of Oxford.

**Official Source Links:**

* [https://www.refugee-economies.org/dataset?send=download](https://www.refugee-economies.org/dataset?send=download)
* [https://www.refugee-economies.org//assets/downloads/ELR_replication.zip](https://www.refugee-economies.org//assets/downloads/ELR_replication.zip)

**Description:** This original panel dataset was collected between 2016 and 2021 to understand and explain variations in socio-economic outcomes for refugees. It is a cross-sectional dataset focusing exclusively on refugees, covering urban and rural areas in Uganda, Kenya, and Ethiopia. The dataset includes nearly 9,000 refugees from six research sites and comprises data on income, expenditure, assets, health, education, migration, and attitudes.

**Relevance to Problem:** This dataset is highly relevant as it contains detailed micro-level data on the socio-economic status and financial behaviors of refugees. This granular information can directly inform our understanding of the specific financial exclusion challenges faced by refugees and potentially highlight areas where blockchain-based identity and credit systems could be most impactful.

**Classification by Data Type:**

* **Quantitative (Numerical) Data:** Income, expenditure, assets, health metrics, etc.
* **Qualitative (Categorical) Data:** Attitudes, education levels (likely ordinal or nominal categories).
* **Time Series Data:** Collected as a panel dataset over multiple years (2016-2021).

**Classification by Structure:**

* **Structured Data:** Provided in CSV format, implying a tabular structure.

**Classification by Collection Method:**

* **Primary Data:** Collected firsthand specifically for the Refugee Economies research.

**Classification by Access Type:**

* **Public Data:** Available for download directly from the Refugee Economies website.

**Associated File (Local raw copy will be named `.raw.zip`):**

* [`ELR_replication.raw.zip`](/1_datasets/raw_datasets_files/ELR_replication.raw.zip)
  * **Contents:** CSV package with README and survey documentation, containing data on income, expenditure, assets, health, education, migration, attitudes, and more for almost 9,000 refugees.

---

## 4. Refugee Financial Inclusion and Financial Health, Baseline Survey - 2024

**Source:** United Nations High Commissioner for Refugees (UNHCR).

**Official Source Links:**

* [https://microdata.unhcr.org/index.php/catalog/1346/related-materials](https://microdata.unhcr.org/index.php/catalog/1346/related-materials)
* [https://microdata.unhcr.org/index.php/catalog/1346/download/4120](https://microdata.unhcr.org/index.php/catalog/1346/download/4120)

**Description:** This refers to a baseline survey on Refugee Financial Inclusion and Financial Health, conducted in 2024. The provided links point to related materials and the possibility to download microdata after providing research information.

**Relevance to Problem:** This dataset is highly relevant as it directly addresses financial inclusion and financial health among refugees, which is a core component of our research. It can provide specific insights into the barriers and opportunities for refugees in accessing financial services.

**Classification by Data Type:**

* **Quantitative (Numerical) Data:** Likely includes numerical measures of financial health and inclusion.
* **Qualitative (Categorical) Data:** May include categorical responses related to financial access and behaviors.

**Classification by Structure:**

* **Structured Data:** The underlying microdata, once downloaded, is expected to be structured for analysis.

**Classification by Collection Method:**

* **Primary Data:** A baseline survey suggests direct data collection for this specific purpose.

**Classification by Access Type:**

* **Private Data/Restricted Public Data:** Access to the microdata requires providing research information, implying a controlled access mechanism.

**Associated Files (Local raw copies will be named `.raw.zip`):**

* [`UNCHR_JOR_2024_FIFH_report.raw.zip`](/1_datasets/raw_datasets_files/UNCHR_JOR_2024_FIFH_report.raw.zip)
  * **Contents:** Includes PDF reports and annexes related to the survey. Actual microdata access is via a separate process.
    * `UNHCR Jordan_2024 Refugee FI FH BLS_Two Pager Brief_2025.05.07_final.pdf`
    * `UNHCR Jordan_2024 Refugee FI FI BLS_Annexes 01.pdf`
    * `UNHCR Jordan_Refugee FI FH BLS Report_Final 01.pdf`

**Data Access Note:** Microdata can be downloaded from [https://microdata.unhcr.org/index.php/catalog/1346/get-microdata](https://microdata.unhcr.org/index.php/catalog/1346/get-microdata) after providing necessary research information.
