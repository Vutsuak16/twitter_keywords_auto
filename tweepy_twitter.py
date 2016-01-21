__name__ = "vutsuak"

from twitter import Twitter,OAuth
import json


ACCESS_TOKEN = '2309050262-pkZPWvaA8PxSqqyXYPrAVgEFNJKx3rEJjMTafzZ'
ACCESS_SECRET = 'U2XKNahEE38dO8oTNRe2Ms6n569SYIoCPiShg8GiqCzE7'
CONSUMER_KEY = 'vCU2EhCs53ti6Vph6qcThv6Zy'
CONSUMER_SECRET = 'SXtnxlNA0GAHDaLRfvEGHOXbpUxTD6i0sYFTTa972glBBmEOQF'


oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

t = Twitter(auth=oauth)

keyword = raw_input("enter a keyword")  # takes only one keyword for the  time being
keyword = "#" + keyword

result = t.search.tweets(q=keyword, result_type='recent', lang='en',
                         count=5)  # serches for over 5 tweets matching the keyword
# print following
for tweet in result["statuses"]:
    user = str(tweet["user"]["screen_name"])
    id = str(tweet["user"]["id"])