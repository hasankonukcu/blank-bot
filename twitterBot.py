from time import sleep
from numpy import full
from comment import comment
from follow import Follow
from getTweets import *
from random import randint
from like import like
from randomName import getRandomName
from retweet import retweet
import time




tweetList = []
while True:
    try:
        tweets = getTweets()
        for tweet in tweets["globalObjects"]["tweets"]:
            full_text = tweets["globalObjects"]["tweets"][tweet]["full_text"]
            #if "like" in full_text or "follow" in full_text or "RT" in full_text or "wallet":
            print(full_text)
            tweetId = str(tweet)
            print(tweetId)
            if tweetId not in tweetList and "Drop your" not in full_text:  
                if "Follow" in full_text or "follow" in full_text:
                    if "Follow me" in full_text or "follow me" in full_text:
                        id = tweets["globalObjects"]["tweets"][tweet]["id_str"]
                        Follow(id)
                        print("Twit sahibi takip edildi")
                        value = 0
                        for _ in range(50):
                            value = randint(100, 150)
                        time.sleep(value)
                        

                    if len(tweets["globalObjects"]["tweets"][tweet]["entities"]["user_mentions"]) != 0:
                        indexForMention = 0
                        while indexForMention < len(tweets["globalObjects"]["tweets"][tweet]["entities"]["user_mentions"]):
                            mentionUser = tweets["globalObjects"]["tweets"][tweet]["entities"]["user_mentions"][indexForMention]["id_str"]
                            Follow(mentionUser)
                            print("Mentionlar takip edildi")
                            indexForMention = indexForMention + 1
                            for _ in range(50):
                                value = randint(100, 150)
                            time.sleep(value)
                                                                                                                                                        
          
                        

                if " ♥️+" in full_text or "+♥️ " in full_text or "&♥️ " in full_text or " ♥️ " in full_text or "Like" in full_text or "like" in full_text or "LIKE" in full_text or "LİKE" in full_text or "RT🔄" in full_text or "2⃣RT " in full_text or " RT " in full_text or " Retweet " in full_text or " rt " in full_text  or " Rt " in full_text or " Rt," in full_text or " RT," in full_text or "+RT" in full_text or "RT+" in full_text:
                    for _ in range(50):
                        value = randint(100, 150)
                    time.sleep(value)
                    retweet(tweetId)
                    print("Rt Atıldı")  
                    for _ in range(50):
                        value = randint(100, 150)
                    time.sleep(value)
                    like(tweetId)
                    print("Like Atıldı") 

                if "Tag 3" in full_text or "tag 3" in full_text or "Tag frenz" in full_text or "Tag frends" in full_text :
                    for _ in range(50):
                        value = randint(100, 150)
                    time.sleep(value)
                    randomNameList = getRandomName()
                    mension1 = str(randomNameList[0])
                    mension2 = str(randomNameList[1])
                    mension3 = str(randomNameList[2])
                    print(mension1)
                    print(mension2)
                    print(mension3)
                    comment(tweetId=tweetId,message=mension1+ " " +mension2+ " " +mension3)
                    print("3 COMMENT ATILDI")  
                    
                    
                if "Tag 2" in full_text or "tag 2" in full_text:
                    for _ in range(50):
                        value = randint(100, 150)
                    time.sleep(value)
                
                    comment(tweetId=tweetId,message=mension2+ " " +mension1)
                    print("2 COMMENT ATILDI")  
                    
                if "Tag friend" in full_text or "Tag fren" in full_text:
                    for _ in range(50):
                        value = randint(100, 150)
                    time.sleep(value)
               
                    comment(tweetId=tweetId,message=mension3)    
                    print("1 COMMENT ATILDI")  
                    
            tweetList.append(tweetId)
            print(len(tweetList))    
            time.sleep(100)
    except:
        time.sleep(100)
        continue 

  

            
            
        
        
