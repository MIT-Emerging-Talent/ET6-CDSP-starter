# scripts/scrape_google_play.py

import pandas as pd
from google_play_scraper import reviews, Sort
from datetime import datetime
import os

print("--- Google Play Scraper ---")

# --- Configuration ---
# A dictionary mapping app names to their Google Play IDs.
# This makes it easy to add or remove apps in the future.
APPS_TO_SCRAPE = {
    'Wysa': 'bot.wysa.ai',
    'Replika': 'ai.replika.app',
    'Youper': 'br.com.youper',
    'Woebot': 'com.woebot',
    'Calm': 'com.calm.android'
}

REVIEWS_TO_SCRAPE_PER_APP = 10000  # Adjust as needed
OUTPUT_PATH = '../raw_data/' # Save raw data to a dedicated folder

# Ensure the output directory exists
os.makedirs(OUTPUT_PATH, exist_ok=True)

# --- Scraping Loop ---
for app_name, app_id in APPS_TO_SCRAPE.items():
    print(f"\nScraping: {app_name} ({app_id})")
    
    try:
        result, _ = reviews(
            app_id,
            lang='en',
            sort=Sort.NEWEST,
            count=REVIEWS_TO_SCRAPE_PER_APP
        )

        if not result:
            print(f"No reviews found for {app_name}.")
            continue

        print(f"Scraped {len(result)} raw reviews for {app_name}.")
        
        df = pd.DataFrame(result)
        
        # Save the raw data with a clear filename
        output_file = os.path.join(OUTPUT_PATH, f'{app_name.lower()}_google_play_raw.csv')
        df.to_csv(output_file, index=False)
        print(f"Saved raw data to {output_file}")

    except Exception as e:
        print(f"An error occurred while scraping {app_name}: {e}")

print("\n--- Google Play scraping complete. ---")
