import os
from tweets_management import tweets_management
from ngrams import ngrams
from tweets_classification import tweets_classification

user = 'luisvicenteleon'

def management():
    
    user_twitter = tweets_management(user)

    # user_twitter.scraping(500)
    # user_twitter.cleaning()
    user_twitter.sentiment_analysis()

def classification():
    
    sorter = tweets_classification(user)

    sorter.training(0.20)
    sorter.test_Naive_Bayes()
    sorter.test_SVM()
    sorter.test_Decision_Forest()
    sorter.test_Max_Entropy()

def ngramas():
    user_tweets_ngrams = ngrams(user)
    user_tweets_ngrams.monogramming()
    user_tweets_ngrams.ngraming()
    
    
management()
classification()
ngramas()
