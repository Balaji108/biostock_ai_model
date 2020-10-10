# biostock_ai_model
Deep learning model to predict biostock 

List of Stocks:

Eli Lilly and Company (NYSE:LLY), 
Bristol-Myers Squibb (NYSE:BMY), 
Johnson & Johnson (NYSE:JNJ) 
AbbVie (NYSE:ABBV), 
Merck (NYSE:MRK), 
Zoetis (NYSE:ZTS),
Perrigo Company (NYSE:PRGO),
Elanco Animal Heath (NYSE:ELAN).
Teva Pharmaceutical Industries Limited (NYSE:TEVA), 
Novo Nordisk (NYSE:NVO)

The id of the tweets of given stocks can be extracted by executing the following commands in the Terminal.

Number of tweets per stock, Name of the stock, Date Since and Date Until can be modified.

snscrape --max-results 500 twitter-search "#NYSE:JNJ since:2018-01-01 until:2020-02-28 lang:en" > JNJ.txt

snscrape --max-results 500 twitter-search "#NYSE:BMY since:2018-01-01 until:2020-02-28 lang:en" > BMY.txt

snscrape --max-results 500 twitter-search "#NYSE:LLY since:2018-01-01 until:2020-02-28 lang:en" > LLY.txt

snscrape --max-results 500 twitter-search "#NYSE:ABBV since:2018-01-01 until:2020-02-28 lang:en" > ABBV.txt

snscrape --max-results 500 twitter-search "#NYSE:MRK since:2018-01-01 until:2020-02-28 lang:en" > MRK.txt

snscrape --max-results 500 twitter-search "#NYSE:ZTS since:2018-01-01 until:2020-02-28 lang:en" > ZTS.txt

snscrape --max-results 500 twitter-search "#NYSE:PRGO since:2018-01-01 until:2020-02-28 lang:en" > PRGO.txt

snscrape --max-results 500 twitter-search "#NYSE:ELAN since:2018-01-01 until:2020-02-28 lang:en" > ELAN.txt

snscrape --max-results 500 twitter-search "#NYSE:TEVA since:2018-01-01 until:2020-02-28 lang:en" > TEVA.txt

snscrape --max-results 500 twitter-search "#NYSE:NVO since:2018-01-01 until:2020-02-28 lang:en" > NVO.txt
