from secrets import *
from flask import Flask
from twitter import *

app = Flask(__name__)

count = 0

@app.route("/")
def main():
    return "<p style='text-align:center';>Hello, World!<br><br>I created this Twitter bot through GPT-2 Text-Generating Model.<br><br>Check out my GitHub repo <a href='https://github.com/geomin76/geobot' target='_blank'>here</a></p>"

@app.route("/bot_tweet")
def tweet():
    global count
    count+=1
    file = open('goodtweets.txt')
    all_lines = file.readlines()
    t = Twitter(auth=OAuth(access_token(), access_token_secret(), api_key(), api_secret_key()))
    # t.statuses.update(status = all_lines[count])
    test = "Hello world\nThis is a test"
    t.statuses.update(status = test)
    string = "Currently on tweet number: " + str(count)
    return string

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)