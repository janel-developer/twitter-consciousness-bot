import tweepy
import os

# Assumes that the following variables are exported in the program running environment, from your twitter developer account:
# TWITTER_CONSUMER_KEY
# TWITTER_CONSUMER_SECRET
# TWITTER_ACCESS_TOKEN_KEY
# TWITTER_ACCESS_TOKEN_SECRET


# Constants
CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TOKEN_KEY = os.environ.get('TWITTER_ACCESS_TOKEN_KEY')
TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


def auth():  # authentication function returns api handle

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
    return tweepy.API(auth)
