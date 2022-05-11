from getFollowers import *
from unfollow import *
import time 

followers = getFollowers()
for user in followers ["data"]["user"]["result"]["timeline"]["timeline"]["instructions"][3]["entries"]:
    try:
        if user["content"]["itemContent"]["user_results"]["result"]["legacy"]["followers_count"] < 10000:
            print(user["content"]["itemContent"]["user_results"]["result"]["legacy"]["followers_count"])
            userId = user["content"]["itemContent"]["user_results"]["result"]["rest_id"]
            UnFollow(userId)
            time.sleep(10)

    except:
        continue