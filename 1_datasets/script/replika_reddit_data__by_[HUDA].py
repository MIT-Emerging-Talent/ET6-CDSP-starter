import praw
import pandas as pd
import time
import hashlib
import prawcore
from datetime import datetime
import os
from langdetect import detect

# === Your Reddit API credentials ===

reddit = praw.Reddit(
    client_id="wG0FLf94gXnCc4ssiA9DpQ",
    client_secret="9mo6X-sfFW4T81DlbMWCR0kRutMhag",
    user_agent="Scraper by u/Equal_Negotiation417",
    username="Equal_Negotiation417",
    password="i]dg1ifm2",
)


# === Search Keywords ===
search_keywords = [
    "lonely",
    "alone",
    "loneliness",
    "depression",
    "anxiety",
    "panic",
    "tired",
    "sleep",
    "schizophrenia",
    "bipolar",
    "numb",
    "empty",
    "suicidal",
    "self-harm",
]

# === Settings ===
subreddit_name = "Replika"
app_name = "Replika"
posts_per_keyword = 300
batch_size = 500
min_timestamp = int(datetime(2020, 1, 1).timestamp())

os.makedirs("output", exist_ok=True)

data = []
batch_count = 1
seen_hashes = set()

print("\U0001f50d Starting keyword-based scraping in r/Replika...\n")


def save_batch(data, batch_count):
    df = pd.DataFrame(data)
    csv_filename = f"output/reddit_keyword_batch_{batch_count}.csv"
    xlsx_filename = f"output/reddit_keyword_batch_{batch_count}.xlsx"
    df.to_csv(csv_filename, index=False)
    df.to_excel(xlsx_filename, index=False)
    print(f"\U0001f4be Saved batch {batch_count} to {csv_filename} and {xlsx_filename}")


for keyword in search_keywords:
    print(f"   🔍 Searching for '{keyword}' in r/{subreddit_name}...")
    subreddit = reddit.subreddit(subreddit_name)

    try:
        for post in subreddit.search(
            query=keyword, sort="new", limit=posts_per_keyword
        ):
            try:
                if post.created_utc < min_timestamp:
                    continue
                post_title = post.title
                post_body = post.selftext
                post_id = post.id
                post_author = str(post.author) if post.author else "deleted"
                post_created_utc = datetime.utcfromtimestamp(
                    post.created_utc
                ).isoformat()
                source = "Reddit"
                context_type = "keyword-search"

                if not post_body.strip():
                    continue

                try:
                    if detect(post_body) != "en":
                        continue
                except:  # noqa: E722
                    continue

                content_hash = hashlib.md5(
                    (post_title + post_body).encode("utf-8")
                ).hexdigest()
                if content_hash in seen_hashes:
                    continue
                seen_hashes.add(content_hash)

                post.comments.replace_more(limit=None)
                time.sleep(1)

                for comment in post.comments.list():
                    try:
                        if detect(comment.body) != "en":
                            continue
                    except:
                        continue

                    comment_body = comment.body
                    comment_id = comment.id
                    comment_author = (
                        str(comment.author) if comment.author else "deleted"
                    )
                    comment_created_utc = datetime.utcfromtimestamp(
                        comment.created_utc
                    ).isoformat()

                    data.append(
                        {
                            "app_name": app_name,
                            "context_type": context_type,
                            "matched_keyword": keyword,
                            "subreddit": subreddit_name,
                            "post_id": post_id,
                            "post_title": post_title,
                            "post_body": post_body,
                            "comment_id": comment_id,
                            "comment_body": comment_body,
                            "source": source,
                            "created_utc": comment_created_utc,
                            "author": comment_author,
                        }
                    )

                    if len(data) >= batch_size:
                        save_batch(data, batch_count)
                        data = []
                        batch_count += 1

            except prawcore.exceptions.TooManyRequests:
                print("\u26a0\ufe0f Rate limit hit inside post. Waiting 60 seconds...")
                time.sleep(60)
                continue

    except prawcore.exceptions.TooManyRequests:
        print("\u23f3 Rate limit hit on subreddit search. Waiting 60 seconds...")
        time.sleep(60)

if data:
    save_batch(data, batch_count)

print(
    "\n\u2705 Keyword scraping complete. Check the 'output' folder for CSV and Excel files."
)
