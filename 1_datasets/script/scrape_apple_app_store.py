# scripts/scrape_apple_app_store.py

import os

import pandas as pd
from app_store_scraper import AppStore

print("--- Apple App Store Scraper ---")

# --- Configuration ---
# A dictionary mapping app names to their Apple App Store names (from the URL).
APPS_TO_SCRAPE = {
    "Wysa": "wysa-ai-therapist-chat-bot",
    "Replika": "replika-my-ai-friend",
    "Woebot": "woebot-your-self-care-expert",
    "Youper": "youper-cbt-therapy-journal",
    "Calm": "calm",
}

# The list of major App Store countries to scrape from.
COUNTRIES_TO_SCRAPE = ["us", "gb", "ca", "au", "in"]
REVIEWS_LIMIT_PER_APP = (
    5000  # Total reviews to try and get for one app across all countries.
)
OUTPUT_PATH = "../raw_data/"

# Ensure the output directory exists
os.makedirs(OUTPUT_PATH, exist_ok=True)

# --- Scraping Loop ---
for app_name, app_url_name in APPS_TO_SCRAPE.items():
    print(f"\nScraping: {app_name}")

    all_reviews_for_this_app = []

    # Loop through each country code in our list
    for country in COUNTRIES_TO_SCRAPE:
        print(f"  -- Checking country: {country}...")
        try:
            # Initialize the scraper for the current app and country
            app = AppStore(country=country, app_name=app_url_name)

            # Scrape reviews. This might take a while.
            app.review(how_many=REVIEWS_LIMIT_PER_APP)

            # Add the country code to each review dictionary for tracking
            for review in app.reviews:
                review["country"] = country

            all_reviews_for_this_app.extend(app.reviews)
            print(f"  -- Found {len(app.reviews)} reviews in '{country}'.")

        except Exception as e:
            # This handles cases where the app isn't in a store or an error occurs
            print(
                f"  -- Could not scrape '{country}' for {app_name}. Skipping. Error: {e}"
            )
            continue

    if not all_reviews_for_this_app:
        print(f"No reviews were found for {app_name} across any countries.")
        continue

    print(f"Total raw reviews scraped for {app_name}: {len(all_reviews_for_this_app)}")

    df = pd.DataFrame(all_reviews_for_this_app)

    # Save the raw data with a clear filename
    output_file = os.path.join(
        OUTPUT_PATH, f"{app_name.lower()}_apple_app_store_raw.csv"
    )
    df.to_csv(output_file, index=False)
    print(f"Saved raw data for {app_name} to {output_file}")

print("\n--- Apple App Store scraping complete. ---")
