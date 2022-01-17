import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'awUe63nCtu1zSOKWrhNXfWIQ2'
consumer_secret = 'tP45Jfq2qvvRQy1mB2c6IinHTX6YU7H4pPr693tAmuThjpbsIF'
access_token = '1118160884285632515-si3GnHioeMoUXtuJqNHS5iLEAUqC3A'
access_token_secret = 'gu4fxwKy8ddjVnZW6mLMs4dNT3iGAjeUxA3iE3rNOq4Yk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=200,
                           lang="en",
                           since="2019-11-07").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
