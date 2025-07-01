# App Review Scraper - Quick Start Guide

Welcome! This guide will help you quickly understand, set up, and run the App Review Scraper project from GitHub.

---

## Overview

This project scrapes user reviews from both the Apple App Store and Google Play Store, merges them to remove duplicates, and outputs combined data in JSON and CSV formats for easy analysis.

It is designed to be:

- **Modular:** Clear folder structure for scripts, data, and workflows.  
- **Automated:** Supports GitHub Actions for scheduled scraping.  
- **Scalable:** Easily configurable for different apps by changing app IDs.  

---

## Getting Started

### 1. Clone the repository

```
git clone https://github.com/fevziismailsahin/app-review-scraper.git
cd app-review-scraper
npm install
```

### 2. Configure your app IDs

Open scripts/playstore_scraper.js and set the Play Store app ID (e.g., com.calm.android).

Open scripts/appstore_scraper.js and set the App Store app ID (e.g., 571800810).

These IDs tell the scraper which app’s reviews to collect.

### 3. Run the scraping scripts

```
node scripts/playstore_scraper.js
node scripts/appstore_scraper.js
node scripts/merge_reviews.js
```

The first two scripts fetch reviews from their respective stores.

The last script merges and deduplicates all collected reviews.

### 4. Review the output

Scraped and merged reviews will be saved inside the data/ folder as .json and .csv files.

These files can be directly used for further analysis or visualization.
