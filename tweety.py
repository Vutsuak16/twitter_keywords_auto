__name__ = "vutsuak"

import tweepy

ACCESS_TOKEN = '2309050262-pkZPWvaA8PxSqqyXYPrAVgEFNJKx3rEJjMTafzZ'
ACCESS_SECRET = 'U2XKNahEE38dO8oTNRe2Ms6n569SYIoCPiShg8GiqCzE7'
CONSUMER_KEY = 'vCU2EhCs53ti6Vph6qcThv6Zy'
CONSUMER_SECRET = 'SXtnxlNA0GAHDaLRfvEGHOXbpUxTD6i0sYFTTa972glBBmEOQF'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
following = []
keyword = raw_input("enter a keyword")  # takes only one keyword for the  time being
keyword = "#" + keyword
for user in tweepy.Cursor(api.friends, screen_name="kaustuv deolal").items():
    following.append((str(user.screen_name)))


ct = 5 #only for 5 tweets
for tweet in tweepy.Cursor(api.search, q=keyword).items():
    if ct == 0:
        break
    try:
        if tweet.user.screen_name not in following:
                api.create_friendship(tweet.user.id)
                api.create_favorite(tweet.id)
    except:
        pass

    ct -= 1
