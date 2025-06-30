# USDT Volume Dataset Summary

## Overview

This dataset tracks daily trading volume for key USDT pairs on Binance,
starting in 2018. It serves as an approximate measure of USDT trading
activity over multiple years using actual exchange data.

---

## Data Source

- Data was collected from Binance's free public REST API.
- The CCXT Python library was used to fetch daily OHLCV (open, high, low,
  close, volume) data.
- Selected trading pairs:
  - BTC/USDT
  - ETH/USDT
  - SOL/USDT

These pairs were chosen for their high liquidity and long historical record.

---

## Method

- Downloaded daily candle data for each pair starting from 2018.
- Extracted daily trading volume in USDT terms.
- Combined all pairs into a single table joined on date.
- Filled any missing dates with zero volume.
- Calculated a total daily USDT volume column.
- Saved the final data as a single CSV file.

---

## Resulting CSV File

- Filename: `combined_usdt_volumes.csv`
- Columns:
  - `date`
  - `BTC_USDT`
  - `ETH_USDT`
  - `SOL_USDT`
  - `TOTAL_USDT_VOLUME`

This structure allows easy analysis of individual pair volumes and their
combined daily total.

---

## Usefulness for the Project

This dataset provides a practical, transparent view of USDT trading volume on
Binance over several years. It can be used to:

- Analyze trends in stablecoin demand over time.
- Support research on crypto adoption in emerging markets.
- Offer a reproducible, real-world data source without expensive licensing.

---

## Files Included in Repo

- `combined_usdt_volumes.csv`: Daily USDT trading volumes for selected
  Binance pairs with total sum.
- This Markdown file: Documentation of source, method, and dataset use.
