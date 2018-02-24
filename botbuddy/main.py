import click
from botbuddy.bot.bot import Bot


@click.group()
def cli():
    pass


@cli.command()
@click.argument('hashtag')
def random_retweet(hashtag):
    bot = Bot()
    bot.random_retweet(hashtag)


@cli.command()
@click.argument('hashtag')
@click.option('--days-since', '-d', default=1)
@click.option('--lang', default='en')
@click.option('--limit', default=10)
def query_twitter(hashtag, days_since, lang, limit):
    bot = Bot()
    for tweet in bot.query_hashtag(hashtag, since=days_since, lang=lang, limit=limit):
        print(f'{tweet.author.screen_name}: {tweet.text}')


if __name__ == '__main__':
    cli()
