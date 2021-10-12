# Pytweet
Twitter Bot made using Tweepy in Python

## What does this bot do?

The bot will reply to every tweet in which it got mentioned with a specific hashtag(#qod). The reply will be in the form of an image with a quote written on it.

> ![Example](example_tweet.png)

### **Checkout [@Zeal_Quote](https://twitter.com/zeal_quote)** on Twitter to try it out!


## Major Libraries

- Flask
- pillow
- requests
- requests-oauthlib
- tweepy
- urllib3

## Detailed Blog Link
Here's the complete link for the article, explaining each and every step - https://auth0.com/blog/how-to-make-a-twitter-bot-in-python-using-tweepy/. It also includes deployment process to AWS elastic beanstalk

I have stored credentials in a `credentials.py` file in the following format:
```
access_token=""
access_token_secret=""
API_key=""
API_secret_key=""
```
> You can choose to store it in any other format as well.
