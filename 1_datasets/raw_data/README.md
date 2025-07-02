# Raw Data Documentation

Detailed documentation for the raw data files stored in the
`1_datasets/raw_data/` directory of the DataCents project. Each entry includes
information about the file's origin, content, and any known characteristics or
limitations.

## 1. BNPL Intention to use.xlsx

* **Source:** [Dataset on Buy-Now-Pay-Later Adoption (Mendeley)](https://data.mendeley.com/datasets/8kj2rn7m9x/1)
* **Description:** This Excel file contains survey responses from 226 shoppers to
    understand their intention to adopt Buy Now Pay Later services. It includes
    demographic information and variables related to factors influencing BNPL
    adoption. This dataset is associated with a published academic study.
* **Relevance:** High. Provides insights into the characteristics and behaviors of
    BNPL users, which can be valuable for understanding the target demographic for
    over-indebtedness prediction.
* **Known Limitations:** Small sample size (226 respondents), focus on adoption
    rather than direct default data, and convenience sampling from young
    shoppers in
    India may limit generalizability to a broader population.

## 2. BNPL.csv

* **Source:** [BNPL Ethical Risk Synthetic Data (Kaggle)](https://www.kaggle.com/datasets/vangelistsiligiris/bnpl-ethical-risk-synthetic-data)
* **Description:** This CSV file is a synthetic dataset consisting of 1000 customer
    records of BNPL profiles. It is designed to facilitate analysis around the
    classification of ethical risk in BNPL. It contains demographic and
    financial behavior features of BNPL users.
* **Relevance:** High. Useful for exploring potential relationships between features
    and risk in the BNPL context and for initial model development and testing.
* **Known Limitations:** As a synthetic dataset, it does not reflect real-world
    complexities and may not accurately represent actual user behavior or default
    patterns. Findings derived solely from this dataset may not be
    generalizable to real-world scenarios.

## 3. FRBNY-SCE-Credit-Access-Data.xlsx and FRBNY-SCE-Credit-Access-complete_microdata.xlsx

* **Source:** These files originate from the Federal Reserve Bank of New York
    (FRBNY) Survey of Consumer Expectations (SCE) Credit Access Survey. The
    `complete_microdata.xlsx` contains the full microdata from the survey,
    while `Data.xlsx` is a summary/subset.
  * **Source:** [https://www.newyorkfed.org/microeconomics/sce/credit-access](https://www.newyorkfed.org/microeconomics/sce/credit-access)
* **Description:** The Survey of Consumer Expectations (SCE) Credit Access Survey
    provides detailed information on consumers' experiences and expectations regarding
    credit access. This includes data on applications for credit, approvals,
    rejections, and reasons for credit decisions. The microdata contains
    individual-level responses.
* **Relevance:** High. This data is highly relevant for understanding consumer credit
    behavior and access to traditional loans, which is crucial for comparing
    with BNPL.
    It can provide a baseline for traditional loan default analysis and insights
    into factors affecting credit access.
* **Known Limitations:** The specific variables related to default or
    over-indebtedness would need to be identified and potentially engineered
    from the raw survey responses. The data is self-reported, which can
    introduce biases.

## 4. public2024.csv

* **Source:** This file is the public use microdata from the
    **2024 Survey of Household Economics and Decisionmaking (SHED)**
    conducted by the
    Federal Reserve Board.
  * **Source:** [https://www.federalreserve.gov/consumerscommunities/shed_data.htm](https://www.federalreserve.gov/consumerscommunities/shed_data.htm)
        (The SHED data is typically released annually, and `public2024.csv`
        correspond to the 2024 release).
* **Description:** The SHED survey provides a comprehensive look at the financial
    lives of U.S. households, covering topics such as financial well-being, income,
    expenses, savings, debt, and various financial behaviors. This CSV file
    contains individual-level responses to the survey questions.
* **Relevance:** High. This dataset is crucial for understanding the financial
    landscape of U.S. households, identifying factors related to financial distress,
    and potentially constructing a proxy for over-indebtedness. It can also provide
    demographic and economic context for BNPL users.
* **Known Limitations:** While comprehensive, the SHED dataset may not have a direct
    variable specifically for BNPL loan defaults. A proxy for over-indebtedness would
    need to be constructed from existing variables. The data is self-reported, which
    can introduce reporting biases.

## 5. afdr_a8.csv and afdr_charts.csv

* **Source:** These files originates from the **Federal Reserve Board's
    Agricultural Finance Databook (AFDR)**. The `afdr_a8.csv` contains
    data for a
    specific table (e.g., Table A.8), and `afdr_charts.csv` contains
    data used to
    generate charts in the databook.
  * **Source:** [https://www.federalreserve.gov/releases/e15/](https://www.federalreserve.gov/releases/e15/)
* **Description:** The Agricultural Finance Databook provides detailed statistics
    on agricultural finance, including farm income, expenses, debt, and credit
    conditions.
    These CSV files would contain time-series or cross-sectional data
    related to these agricultural financial indicators.
* **Relevance:** Low. As noted in the previous data source evaluation, agricultural
    finance data is generally not directly relevant to consumer loans, BNPL services,
    or their default rates. This data would likely not be used for the core research
    question but might provide very broad economic context if needed.
* **Known Limitations:** Highly specific to the agricultural sector, making it
    largely irrelevant for a project focused on consumer finance and BNPL. The data
    might also be aggregated, limiting its use for individual-level analysis.

## 6. sce-household-spending-chart-data.xlsx

* **Source:** This file likely comes from the Federal Reserve Bank of New York
    (FRBNY) Survey of Consumer Expectations (SCE), specifically data used for charts
    related to household spending.
  * **Source:** [https://www.newyorkfed.org/microeconomics/sce/](https://www.newyorkfed.org/microeconomics/sce/)
* **Description:** This Excel file contains aggregated data points
    used to generate charts on household spending trends, expectations, or
    behaviors. It would
    not contain individual-level microdata but rather summary statistics
    over time or
    across different groups.
* **Relevance:** Medium. While it provides insights into household spending,
    which is related to financial well-being, it is aggregated data and may not
    be directly
    usable for predictive modeling at an individual level. It can provide valuable
    contextual information and trends.
* **Known Limitations:** Aggregated data limits its use for granular analysis.
