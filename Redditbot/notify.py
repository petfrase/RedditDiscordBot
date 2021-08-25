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

new = subreddit.new(limit = 3)

for submission in new:
    print(submission.title)
    time = get_date(submission)
    print(time)

