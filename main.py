import praw, re, pandas as pd
from datetime import datetime

CLIENT_ID = ""
CLIENT_SECRET = ""
USER_AGENT = ""

read = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
manga = read.subreddit("manga")

title = input("Name of the series?\n\n")

chapters_dict = {"Chapter #": [], "Upvotes": [], "Date": [], "Link": []}

for submission in manga.search(f"[DISC] {title}", limit=None):
    if f"[DISC] {title}" in submission.title and re.search("\d" , submission.title):
        chapters_dict["Link"].append(submission.shortlink)
        chapters_dict["Date"].append(datetime.fromtimestamp(submission.created_utc).strftime("%m/%d/%y"))
        chapters_dict["Upvotes"].append(submission.score)
        chapters_dict["Chapter #"].append(re.search("\d+", submission.title).group(0))

posts = pd.DataFrame(chapters_dict)
posts.to_csv(f'{title}.csv', index=False)
