from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/twitter_bot", methods=["GET", "POST"])
def twitter_bot():
    if request.method == "GET":
        return render_template("index.html")
    else:
        pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
