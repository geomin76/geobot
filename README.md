# geobot
Twitter bot for Geo

An attempt to create a Twitter bot for my twitter account @geomin76

I plan to analyze my own tweets and generate tweets.

I followed this tutorial [here](https://minimaxir.com/2020/01/twitter-gpt2-bot/)

### Set-up
```sh
$ git clone https://github.com/geomin76/geobot.git
$ cd geobot
$ python3 -m venv venv
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install flask
$ pip3 install twitter
$ pip3 install twint=2.1.4 fire tqdm
$ python main.py
```

### Getting your tweets 
(from: https://github.com/minimaxir/download-tweets-ai-text-gen)
```sh
$ python3 download_tweets.py <twitter_username>
```
After this script, you'll find a file in your directory username_tweets.csv

For example, I can obtain my tweets by python3 download_tweets.py geomin76. This python script obtains all tweets except for retweets, replies, quote tweets. 

### Training a model and generating texts
Here's how you train an AI model (for free!) with your tweets:
[Follow the tutorial here!](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce#scrollTo=KBkpRgBCBS2_)

Through this link, you can train a GPT-2 Text-Generating Model and generate text (potential tweets) from the model.

You can download your generated tweets into a .txt file and look at them! WArning: you won't get quality tweets all the time.

I hand-picked my favorite generated tweets and set them into a .txt file, and will let cron schedule the tweets.