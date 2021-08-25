import praw
import datetime
from functions import get_date

reddit = praw.Reddit(
                    client_id = "",
                    client_secret = "",
                    username = "",
                    password = "",
                    user_agent = ""
                    )

subreddit = reddit.subreddit("appleswap")

new = subreddit.new(limit = 10)

for submission in reddit.subreddit("appleswap").search('flair:RAM', limit = 15):
    print(submission.title)
    time = get_date(submission)
    print(time)