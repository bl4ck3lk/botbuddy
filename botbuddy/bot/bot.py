import logging
from pprint import pprint
import re
import random
import time

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
        assert all((CONSUMER_SECRET, CONSUMER_KEY, ACCESS_TOKEN, ACCESS_SECRET)),\
            'Missing credentials'
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
        tc = tweepy.Cursor(self._api.search, q=hashtag, since=since, lang=lang).items(limit)
        try:
            for tweet in tc:
                yield tweet
        except tweepy.error.TweepError as e:
            logger.warning(f'Exception while querying Twitter: {e}')
            time.sleep(960)  # often this happens when the api makes too many requests.

    def random_retweet(self, hashtag, since=1, lang='en'):
        tweets = [tweet for tweet in self.query_hashtag(
            hashtag, since=since, lang=lang, limit=500)
                  if Bot.is_popular(tweet)]
        if tweets:
            if len(tweets) > 50:
                tweets.sort(key=lambda x: x.favorite_count)
                tweets = tweets[int(len(tweets)*0.7):]
            random_tweet = random.choice(tweets)
            try:
                self._api.retweet(random_tweet.id)
            except tweepy.error.TweepError as e:
                logger.error(f'{e}')
                if e[0].get('code') == 327:
                    try:
                        random_tweet = random.choice(tweets)
                        self._api.retweet(random_tweet.id)
                    except:
                        pass
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
        if fav_count < 10 or retweet_count < 10:
            return False
        logger.info(f'Author: {tweet.author.screen_name}\n\t'
                    f'followers: {followers_count}, '
                    f'favorited: {fav_count}, retweeted: {retweet_count}')
        return True
