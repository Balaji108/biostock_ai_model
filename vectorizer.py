import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess_data(corpus):
    # remove blank rows
    corpus['Tweet'].dropna(inplace=True)
    # change all text to lower case
    corpus['Tweet'] = [entry.lower() for entry in corpus['Tweet']]
    # tokenize
    corpus['Tweet'] = [word_tokenize(entry) for entry in corpus['Tweet']]
    return corpus


def lemmatize_data(corpus):
    # remove stopwords, non-numeric words
    for index, entry in enumerate(corpus['Tweet']):
        final_words = []
        word_lemmatizer = WordNetLemmatizer()
        for word in entry:
            if word not in stopwords.words('english') and word.isalpha():
                word_final = word_lemmatizer.lemmatize(word)
                final_words.append(word_final)
        corpus.loc[index, 'text_final'] = str(final_words)
    return corpus


def vectorize_tweets(df_tweet):
    data = df_tweet.copy()
    # 1. Preprocess the data
    data = preprocess_data(data)
    # 2. Perform Lemmatization
    data = lemmatize_data(data)
    # TfIdf Vectorization
    vectorizer = TfidfVectorizer(max_features=5000)
    vectorized_data = vectorizer.fit_transform(data['text_final'])
    df_tweet['Tweet Vector'] = list(vectorized_data.toarray())
    return df_tweet
