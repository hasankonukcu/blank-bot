from time import sleep
from numpy import full
from comment import comment
from getTweets import *

from like import like
from retweet import retweet
import time

def getFollowText(full_text):
    #index = full_text.find("@")
    list = []
    i = 0
    while i < len(full_text):
        if full_text[i] == "@":
            while i < len(full_text):
                if full_text[i] == "," or full_text[i] == "&" or full_text[i] == "+" or full_text[i] == "/" or full_text[i] == " " or full_text[i] == "." or full_text[i] == "!" or full_text[i] == "@"  or full_text[i] == ":":
                    break
                else:
                    list.append(full_text[i])
                    print(full_text[i])
        i = i+1

    return list




tweetList = []
while True:
    try:
        tweets = getTweets()
        for tweet in tweets["globalObjects"]["tweets"]:
            full_text = tweets["globalObjects"]["tweets"][tweet]["full_text"]
            #if "like" in full_text or "follow" in full_text or "RT" in full_text or "wallet":
            print(full_text)
            print(tweets["globalObjects"]["tweets"][tweet]["id_str"])
            
            tweetId = str(tweet)
            if tweetId not in tweetList:  
                print(tweet)

            print(len(tweetList))        
            time.sleep(60)
    except:
        time.sleep(60)
        continue 

  

            
            
        
        
