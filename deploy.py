import os
import time
import random

from botbuddy.bot.bot import Bot
from botbuddy.hashtags.hashtag import Hashtags


def launch_bot(hashtag_file, interval=5):
    if not os.path.isfile(hashtag_file):
        this = os.path.dirname(os.path.realpath(__file__))
        hashtag_file = os.path.join(this, 'botbuddy', 'hashtags', 'data', hashtag_file)
    interval = interval * 60  # minutes to seconds
    bot = Bot()
    ht = Hashtags(hashtag_file)
    while True:
        bot.random_retweet(random.choice(ht))
        time.sleep(interval)


launch_bot('deeplearning', 25)
