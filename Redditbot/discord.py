import praw
import datetime
import time
import requests
import json
from functions import get_new_submissions, stream_submissions, stream_submissionsV2, get_latest_macbook_pros

## Paste your Discord webhook url below
url = ""

data = {}
##data["content"] = "How do i send the submissions"
# data["content"] = get_new_submissions()
data["content"] = get_latest_macbook_pros()
data["username"] = "appleswapbot"

while True:
    result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))      

    time.sleep(5)
    

    
##stream_submissions()
