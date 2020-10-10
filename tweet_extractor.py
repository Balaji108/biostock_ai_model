import re
import json
import time
import tweepy
import pandas as pd
from pytz import timezone
from datetime import datetime
from tweepy import OAuthHandler

# New york time zone
new_york_tz = timezone('America/New_York')

credentials = json.loads(open('twitter_keys.json').read())
consumer_key = credentials['consumer_key']
consumer_secret = credentials['consumer_secret']
access_key = credentials['access_key']
access_secret = credentials['access_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def fetch_tweets(tweet_ids, stock_name):
    list_of_tweet_status = api.statuses_lookup(tweet_ids)
    df_tweet = pd.DataFrame()
    for status in list_of_tweet_status:
        tweet_created_timestamp = status.created_at  # Get the timestamp
        text = status.text  # Get the tweet
        text = re.sub(r"http\S+", "", text)  # Remove links from the tweet
        new_york_time = new_york_tz.localize(tweet_created_timestamp)  # Convert the time zone
        tweet_elem = {
            "Stock": stock_name,
            "Date": new_york_time.date(),
            "Tweet": text
        }
        df_tweet = df_tweet.append(tweet_elem, ignore_index=True)
    return df_tweet


def scrape_tweets(stocks):
    # Create a dataframe to store values
    df_tweets = pd.DataFrame()
    # Append the stock links of all stocks into a single dataframe along with their respective name
    for stock in stocks:
        file_name = stock + ".txt"
        tweet_url = pd.read_csv(file_name, index_col=None, header=None, names=["links"])
        link = lambda x: x["links"].split("/")[-1]
        tweet_url['id'] = tweet_url.apply(link, axis=1)
        ids = tweet_url['id'].tolist()
        # Get the value of chunk to extract tweets using id
        total_count = len(ids)
        chunks = (total_count - 1) // 50 + 1
        for i in range(chunks):
            batch = ids[i * 50:(i + 1) * 50]
            df_tweet_out = fetch_tweets(batch, stock)
            df_tweets = df_tweets.append(df_tweet_out, ignore_index=True)
    return df_tweets
