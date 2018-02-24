import logging
from pprint import pprint
import re
import random

import tweepy

from botbuddy.bot.secrets import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_SECRET,
    ACCESS_TOKEN,
)
from botbuddy.utils.dateutils import get_n_days_ago

logger = logging.getLogger(__name__)

SPACE = re.compile(r'\s+')


class Bot:
    def __init__(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self._api = tweepy.API(auth)

    @property
    def public_tweets(self):
        for i, tweet in enumerate(self._api.home_timeline()):
            pprint(f'{i}: {tweet.text}')

    def query_hashtag(self, hashtag, since=1, lang='en', limit=10):
        hashtag = SPACE.sub('', hashtag)
        if not hashtag.startswith('#'):
            hashtag = f'#{hashtag}'
        since = get_n_days_ago(since)
        logger.info(f'Searching for hashtag "{hashtag}" since "{since}"...')
        for tweet in tweepy.Cursor(
                self._api.search, q=hashtag, since=since, lang=lang).items(limit):
            yield tweet

    def random_retweet(self, hashtag, since=1, lang='en'):
        tweets = [tweet for tweet in self.query_hashtag(
            hashtag, since=since, lang=lang, limit=1000)
                  if Bot.is_popular(tweet)]
        if tweets:
            random_tweet = random.choice(tweets)
            self._api.retweet(random_tweet.id)
            return random_tweet

    @staticmethod
    def is_popular(tweet):
        if not tweet.user.verified:
            return False
        followers_count = tweet.user.followers_count
        friends_count = tweet.user.friends_count
        if friends_count > followers_count:
            return False
        fav_count = tweet.favorite_count
        retweet_count = tweet.retweet_count
        if fav_count < 1 or retweet_count < 1:
            return False
        logger.info(f'Author: {tweet.author.screen_name}\n\t'
                    f'followers: {followers_count}, '
                    f'favorited: {fav_count}, retweeted: {retweet_count}')
        return True


if __name__ == '__main__':
    bot = Bot()
    tweets = bot.random_retweet('#stevejobs')
    print(tweets)
