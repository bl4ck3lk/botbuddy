import click
import os
import random
import time
import logging

from botbuddy.bot.bot import Bot
from botbuddy.hashtags.hashtag import Hashtags

logger = logging.getLogger(__name__)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('hashtag')
def random_retweet(hashtag):
    bot = Bot()
    bot.random_retweet(hashtag)


@cli.command()
@click.argument('hashtag', metavar='<hashtag>')
@click.option('--days-since', '-d', default=1, help='Max tweet age in days', metavar='<days>')
@click.option('--lang', default='en', help='Language of tweets', metavar='<language>')
@click.option('--limit', default=10, help='Number of tweets to return', metavar='<# of tweets>')
def query_twitter(hashtag, days_since, lang, limit):
    bot = Bot()
    for tweet in bot.query_hashtag(hashtag, since=days_since, lang=lang, limit=limit):
        print(f'{tweet.author.screen_name}: {tweet.text}')


@cli.command()
@click.argument('hashtag-file', metavar='<hashtag file name>')
@click.option('--interval', '-i', default=25, help='Number of minutes between tweets',
              metavar='<interval in minutes>')
def launch_bot(hashtag_file, interval):
    if not os.path.isfile(hashtag_file):
        this = os.path.dirname(os.path.realpath(__file__))
        hashtag_file = os.path.join(this, 'hashtags', 'data', hashtag_file)
    interval = interval * 60  # minutes to seconds
    bot = Bot()
    ht = Hashtags(hashtag_file)
    while True:
        bot.random_retweet(random.choice(ht))
        time.sleep(interval)


if __name__ == '__main__':
    cli()
