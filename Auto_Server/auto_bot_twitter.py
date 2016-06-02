from flask import Flask, request, redirect, url_for, render_template
import tweepy


app = Flask(__name__)
ACCESS_TOKEN = '2309050262-pkZPWvaA8PxSqqyXYPrAVgEFNJKx3rEJjMTafzZ'
ACCESS_SECRET = 'U2XKNahEE38dO8oTNRe2Ms6n569SYIoCPiShg8GiqCzE7'
CONSUMER_KEY = 'vCU2EhCs53ti6Vph6qcThv6Zy'
CONSUMER_SECRET = 'SXtnxlNA0GAHDaLRfvEGHOXbpUxTD6i0sYFTTa972glBBmEOQF'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)


@app.route("/twitter_bot", methods=["GET", "POST"])
def twitter_bot():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if request.form["optradio"] == "follow":
            key = request.form["key"]

        elif request.form["optradio"] == "UnFollow":
            key = request.form["key"]

        return redirect('/twitter_bot')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
