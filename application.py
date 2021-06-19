from flask import Flask
import tweet_reply

import atexit
from apscheduler.schedulers.background import BackgroundScheduler

def hello():
    tweet_reply.respondToTweet('tweet_ID.txt')
    print("Success")

scheduler = BackgroundScheduler()
scheduler.add_job(func=hello, trigger="interval", seconds=60)
scheduler.start()

application = Flask(__name__)

@application.route("/")
def index():
    return "Follow @zeal_quote!"


atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    application.run(port=5000, debug=True)
