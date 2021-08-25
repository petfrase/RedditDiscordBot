import praw
import datetime

reddit = praw.Reddit(
                    client_id = "",
                    client_secret = "",
                    username = "",
                    password = "",
                    user_agent = ""
                    )


def get_new_submissions():
    subreddit = reddit.subreddit("appleswap")
    new = subreddit.new(limit = 5)
    title = "*these are the top 5 new submissions* \n"
    for submission in new:
        print(submission.title)
        time = '\n' + get_date(submission) + '\n'
        print(time)
        title +=  submission.title 
        title += time
        title += '\n'

    
    return title

def get_latest_macbook_pros():
    subreddit = reddit.subreddit("appleswap")
    new = subreddit.new(limit = 10)
    title = "*these are the top 5 new submissions* \n"
    ##uselessSubstrings = ['[USA-','NIKE','APPLE']
    neededSubstrings = ['[H]','MACBOOK','16', '32','GB']
    for submission in new:
        time = '\n' + get_date(submission) + '\n'
        print(submission.title)
        if "Pro" in submission.title:
            titleString = str(submission.title)
            state = titleString.upper()
            stateShortened = state.replace('[USA-', '')
            title += stateShortened[3:] 
            title += time

    
    return title + '---------------------\n'

def stream_submissions():
    for submission in reddit.subreddit("appleswap").stream.submissions(skip_existing=True):
        title = submission.title
        title.lower()
        time = get_date(submission)
        if "pro" not in title:
            print(submission.title + "\n" + time)
        elif "ssd" not in title:
            print(submission.title + "\n" + time)
        else:
            print("there was a submission not anything you are looking for though")

    return "i is done"    


def stream_submissionsV2():
    
    newLastProcessed = None
    lastProcessed = newLastProcessed

    for post in reddit.subreddit("appleswap").new():
        if not newLastProcessed:
            newLastProcessed = post
        if post == lastProcessed:
            break
        # Do something

    lastProcessed = newLastProcessed

    



# retrieves and formats the data of the submission
def get_date(submission):
    time_date = submission.created

    date = datetime.datetime.fromtimestamp(time_date)
    d1 = date.strftime("%B %d, %Y")
    d2 = date.strftime("%I:%M %p")

    return d1 + " " + d2