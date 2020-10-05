import json
import time
import tweepy
import pandas as pd
from pytz import timezone
from datetime import datetime
from tweepy import OAuthHandler


def scrape_tweets(stock_name, search_words, date_since, date_until, num_tweets):
    credentials = json.loads(open('twitter_keys.json').read())

    consumer_key = credentials['consumer_key']
    consumer_secret = credentials['consumer_secret']
    access_key = credentials['access_key']
    access_secret = credentials['access_secret']

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    df_tweets = pd.DataFrame(columns=['Stock', 'Date', 'Tweet'])
    tweets = tweepy.Cursor(api.search,
                           q=search_words,
                           lang="en",
                           since=date_since,
                           # until=date_until,
                           tweet_mode='extended').items(num_tweets)

    tweet_list = [tweet for tweet in tweets]

    for tweet in tweet_list:
        # Pull the values
        tweet_created_timestamp = tweet.created_at
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:  # Not a Retweet
            text = tweet.full_text
        # Convert the time zone
        newyork_tz = timezone('America/New_York')
        newyork_time = newyork_tz.localize(tweet_created_timestamp)
        ith_tweet = [stock_name, newyork_time.date(), text]
        # Append to dataframe - df_tweets
        df_tweets.loc[len(df_tweets)] = ith_tweet
    return df_tweets
