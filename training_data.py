#
#training_data.py
#To run:
#   python training_data.py
#

import pandas as pd
import yfinance as yf

from tweet_extractor import scrape_tweets
from vectorizer import vectorize_tweets

START_DATE = '2018-01-01'
END_DATE = '2020-02-28'
STOCKS = ['LLY', 'BMY', 'JNJ', 'ABBV', 'MRK', 'ZTS', 'PRGO', 'ELAN', 'TEVA', 'NVO']
DATA_FILENAME = "data/stock_data.csv"
TWEETS_DATA_FILENAME = "data/tweet_stock_data.csv"

class StockData():

    def __init__(self, stocks):
        self.stocks = stocks
        self._get_stock_prices()
	self._get_tweets()
    
    def _get_stock_prices(self):
        df = pd.DataFrame()
        for stock in self.stocks:
            df_ = yf.download(stock, 
                      start=START_DATE, 
                      end=END_DATE, 
                      interval='1d',
                      progress=False)
            df_.reset_index(inplace=True)
            df_['Stock'] = stock
            df = df.append(df_, sort=False)
        cols = ['Stock', 'Date', 'Open', 'Close', 'High', 'Low', 'Volume']
        self.stock_prices = df[cols]
        self.stock_prices.to_csv(DATA_FILENAME)
        print (f"Stock prices data available in {DATA_FILENAME}")

    def _get_tweets(self):
        stocks = " OR ".join(STOCKS)
        search_words = "biotech stock OR pharma stock (" + stocks +  ") -filter:retweets"
        num_tweets = 50

        df_tweets = scrape_tweets(search_words, START_DATE, END_DATE, num_tweets)
        df_tweets = vectorize_tweets(df_tweets)

        # Store the data in a csv file
        df_tweets.to_csv('new_stock_tweets.csv', index=False)

        self.stock_tweets = df_tweets
        self.stock_tweets.to_csv(TWEETS_DATA_FILENAME)
        print(f"Stock Tweets data available in {TWEETS_DATA_FILENAME}")
        
    def _get_news(self):
        pass
        
    def get_data(self):
        return self.data

def main():
    print (f"Start gathering stock data ...")
    stock_data = StockData(STOCKS)
    print (f"Completed gathering stock data ...")

if __name__ == "__main__":
    main()


