from flask import Flask, request, redirect, url_for, render_template
import tweepy


import json

app = Flask(__name__)
ACCESS_TOKEN = '2309050262-pkZPWvaA8PxSqqyXYPrAVgEFNJKx3rEJjMTafzZ'
ACCESS_SECRET = 'U2XKNahEE38dO8oTNRe2Ms6n569SYIoCPiShg8GiqCzE7'
CONSUMER_KEY = 'vCU2EhCs53ti6Vph6qcThv6Zy'
CONSUMER_SECRET = 'SXtnxlNA0GAHDaLRfvEGHOXbpUxTD6i0sYFTTa972glBBmEOQF'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
FOLLOWED = []


class StdOutListener(tweepy.StreamListener):
    def __init__(self):
        self.limit = 25
        self.number_of_tweets = 0

    def on_data(self, status):
        self.number_of_tweets += 1

        user_id = json.loads(status)['user']['id']
        tweet_id = json.loads(status)['id_str']
        FOLLOWED.append(json.loads(status)['user']['screen_name'])
        api.create_friendship(user_id)
        api.create_favorite(tweet_id)
        if not (self.number_of_tweets < self.limit):
            print "LIMIT REACHED"
            return False


    def on_error(self, status):
        print status


@app.route("/twitter_bot", methods=["GET", "POST"])
def twitter_bot():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if request.form["optradio"] == "follow":
            key = request.form["key"]
            follow_like(key)

        elif request.form["optradio"] == "UnFollow":
            UnFollow()

        return redirect('/twitter_bot')


def follow_like(key):
    l = StdOutListener()
    stream = tweepy.Stream(auth, l)
    stream.filter(track=[key])


def UnFollow():
    for user in tweepy.Cursor(api.friends, screen_name='kaustuv deolal').items():
        if user.screen_name in FOLLOWED:
            api.destroy_friendship(user.screen_name)

    del FOLLOWED[:]


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
