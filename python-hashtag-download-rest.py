import tweepy
import csv
import pandas as pd
import sys

import codecs

# API credentials here
consumer_key = 'VrbOSG9tAgSkgIsQj80jCG7j6'
consumer_secret = '6vnwSiZlCYCyKm7kt59hCM4BWHD0zSJjZ6HymToUyVMeWIU77Y'
access_token = '65368089-fda4fqY2QNtq32WJgpVr8RpP8L7TRvWq3wN3RfPpL'
access_token_secret = 'UveNOiZi6bNqy0nELTXOPv7VBdN0z7UK8yY2cnSLrRkkX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# Search word/hashtag value 
HashValue = ""

# search start date value. the search will start from this date to the current date.
StartDate = ""

# getting the search word/hashtag and date range from user
HashValue = input("Enter the hashtag you want the tweets to be downloaded for: ")
StartDate = input("Enter the start date in this format yyyy-mm-dd: ")

# Open/Create a file to append data
# csvFile = open(HashValue+'.csv', 'a', encoding="utf-8")

with codecs.open(HashValue+'.csv', "w", 'utf-8') as fp:
    csvWriter = csv.writer(fp)
    # csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(api.search,q=HashValue,count=2000,lang="th",since=StartDate, tweet_mode='extended').items():
        if (not tweet.retweeted) and ('RT @' not in tweet.full_text) and ('http' not in tweet.full_text) :
            print (tweet.created_at, tweet.full_text)
            # csvWriter.writerow([tweet.created_at, (tweet.full_text)])
            csvWriter.writerow([(tweet.full_text)])

print ("Scraping finished and set_access_tokenved to "+HashValue+".csv")
#sys.exit()