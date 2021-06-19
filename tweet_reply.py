import tweepy
import json
import requests
import logging

import Wallpaper
import time

import credentials

consumer_key = credentials.API_key
consumer_secret_key = credentials.API_secret_key
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)


def get_quote():
    url = "https://api.quotable.io/random"

    try:
        response = requests.get(url)
    except:
        logger.info("Error while calling API...")

    res = json.loads(response.text)
    print(res)
    return res['content'] + "-" + res['author']


def get_last_tweet(file):
    f = open(file, 'r')
    lastId = int(f.read().strip())
    f.close()
    return lastId


def put_last_tweet(file, Id):
    f = open(file, 'w')
    f.write(str(Id))
    f.close()
    logger.info("Updated the file with the latest tweet Id")
    return


def respondToTweet(file='tweet_ID.txt'):
    last_id = get_last_tweet(file)
    mentions = api.mentions_timeline(last_id, tweet_mode='extended')
    if len(mentions) == 0:
        return

    new_id = 0
    logger.info("someone mentioned me...")

    for mention in reversed(mentions):
        logger.info(str(mention.id) + '-' + mention.full_text)
        new_id = mention.id

        if '#qod' in mention.full_text.lower():
            logger.info("Responding back with QOD to -{}".format(mention.id))
            try:
                tweet = get_quote()
                Wallpaper.get_wallpaper(tweet)

                media = api.media_upload("created_image.png")

                logger.info("liking and replying to tweet")

                api.create_favorite(mention.id)
                api.update_status('@' + mention.user.screen_name + " Here's your Quote", mention.id,
                                  media_ids=[media.media_id])
            except:
                logger.info("Already replied to {}".format(mention.id))

    put_last_tweet(file, new_id)

def main():
    respondToTweet()
  

# __name__
if __name__=="__main__":
    main()
