from secrets import *
from flask import Flask
from twitter import *

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, World!"

@app.route("/tweet")
def tweet():
    t = Twitter(auth=OAuth(access_token(), access_token_secret(), api_key(), api_secret_key()))
    t.statuses.update(status="Cheers!")
    return "Successful tweet!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)