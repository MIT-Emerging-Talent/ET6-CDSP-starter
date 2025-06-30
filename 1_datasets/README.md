# Dataset Folder README

This folder is dedicated to storing **raw data** used in our project. It is
organized so all team members can contribute their own data sources clearly
and consistently.

---

## Folder Structure

This `/dataset` folder includes:

- **/data_source_notes/**  
  Contains Markdown files explaining *how* each dataset was gathered,
  including source details, methods, and any processing steps.

- **/raw_datasets/**  
  Contains the actual raw or minimally processed data files (e.g., CSVs)
  ready for further analysis.

---

## Purpose of This README

This file is the **directory for all datasets** in this folder.  
Each dataset is added as a numbered item below with:

- Name or title
- Brief description
- Link to the data source note file
- Link to the raw data file

Team members should **add their dataset summaries here** as they contribute.

---

## Datasets in This Folder

### 1. USDT Volume Data (Ahmed)

- **Description:** Daily trading volumes for BTC/USDT, ETH/USDT, and SOL/USDT
  pairs on Binance from 2018 onward. Used as a proxy for overall USDT
  exchange volume over time.
- **Source:** Binance public REST API via CCXT Python library.
- **Data Source Notes:**  
  [USDT_VOLUME_DATA_DOCUMENTATION.md](./data_source_notes/USDT_VOLUME_DATA_DOCUMENTATION.md)
- **Raw Dataset:**  
  [combined_usdt_volumes.csv](./raw_datasets/combined_usdt_volumes.csv)

---

### 2. Crypto Access Barriers – Country × Exchange

- **Description:** Documents whether individuals in Sudan, Afghanistan,
  Lebanon, and Nigeria can register accounts on Binance, Coinbase, KuCoin,
  Bybit, and Crypto.com. Includes KYC requirements and access limitations
  (fiat, P2P, sanctions).
- **Source:** Gathered from official exchange websites and help/support
  pages.
- **Data Source Notes:**  
  [crypto_access_country_barriers.md](./data_source_notes/crypto_access_country_barriers.md)
- **Raw Dataset:**  
  [crypto_access_country_barriers.csv](./raw_datasets/crypto_access_country_barriers.csv)

---

### 3. Google Trends Crypto Interest (Anas)

- **Description:** Google Trends relative search interest for crypto topics
 including Bitcoin, Cryptocurrency, Markets, and NFTs in Lebanon, Sudan, Nigeria,
  and Afghanistan (2019–2024).  
- **Source:** Google Trends
- **Data Source Notes:**  
  [active_wallet_counts](data_source_notes/active_wallet_count_notes.md)
- **Raw Dataset:**  
  [active_wallet_counts](raw_datasets/google_trends_crypto_combined_2019_2024.csv)

---

### 4. [Placeholder for Contributor]

- **Description:** Add a short description of your dataset.
- **Source:** Where you got it from.
- **Data Source Notes:**  
  Link to your Markdown documentation.
- **Raw Dataset:**  
  Link to your data file.

---

## How to Contribute

1. Add your raw data file to the **/raw_datasets/** folder.  
2. Add a Markdown note to **/data_source_notes/** explaining your source and
   method.  
3. Update this README by adding your dataset under the numbered list.  

Please keep descriptions **short and clear** so everyone can quickly
understand what's in the folder.

---
