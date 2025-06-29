# scripts/scrape_reddit.py

import praw
import pandas as pd
import os
from dotenv import load_dotenv # To manage environment variables

print("--- Reddit Scraper ---")

# --- Authentication using Environment Variables ---
# Create a file named .env in your project root and add your credentials:
# REDDIT_CLIENT_ID="your_client_id"
# REDDIT_CLIENT_SECRET="your_client_secret"
# REDDIT_USER_AGENT="your_user_agent"
# REDDIT_USERNAME="your_username"
# REDDIT_PASSWORD="your_password"
# Make sure to add .env to your .gitignore file!
load_dotenv()

try:
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
    )
    print(f"Authenticated to Reddit as: {reddit.user.me()}")
except Exception as e:
    print(f"Could not authenticate to Reddit. Please check your .env file and credentials. Error: {e}")
    exit()

# --- Configuration ---
# Define what to search for and where.
# This structure allows you to easily add more apps or subreddits.
SEARCH_CONFIG = {
    'Replika': {
        'subreddits': ['replika', 'mentalhealth'],
        'keywords': ['replika', 'update', 'sad', 'disappointed']
    },
    'Wysa': {
        'subreddits': ['wysa', 'mentalhealthsupport', 'anxiety'],
        'keywords': ['wysa', 'chatbot', 'therapy bot']
    }
    # Add other apps here as needed
}

POST_LIMIT_PER_QUERY = 50 # Number of posts to fetch for each keyword search
OUTPUT_PATH = '../raw_data/'

# Ensure the output directory exists
os.makedirs(OUTPUT_PATH, exist_ok=True)

# --- Scraping Loop ---
all_reddit_data = []

for app_name, config in SEARCH_CONFIG.items():
    print(f"\nScraping Reddit for: {app_name}")
    for sub_name in config['subreddits']:
        subreddit = reddit.subreddit(sub_name)
        for keyword in config['keywords']:
            print(f"  -- Searching r/{sub_name} for '{keyword}'...")
            
            try:
                search_results = subreddit.search(keyword, sort="top", time_filter="year", limit=POST_LIMIT_PER_QUERY)
                
                for post in search_results:
                    all_reddit_data.append({
                        'app_name_mentioned': app_name,
                        'subreddit': sub_name,
                        'post_id': post.id,
                        'post_title': post.title,
                        'post_body': post.selftext,
                        'post_score': post.score,
                        'post_url': post.url,
                    })
            except Exception as e:
                print(f"  -- An error occurred searching r/{sub_name} for '{keyword}'. Skipping. Error: {e}")

if not all_reddit_data:
    print("No Reddit data was collected.")
else:
    print(f"\nCollected a total of {len(all_reddit_data)} posts from Reddit.")
    df = pd.DataFrame(all_reddit_data)
    
    # Remove duplicate posts that might have been found with different keywords
    df.drop_duplicates(subset=['post_id'], inplace=True)
    print(f"After removing duplicates, we have {len(df)} unique posts.")
    
    output_file = os.path.join(OUTPUT_PATH, 'reddit_raw_posts.csv')
    df.to_csv(output_file, index=False)
    print(f"Saved raw Reddit data to {output_file}")

print("\n--- Reddit scraping complete. ---")
