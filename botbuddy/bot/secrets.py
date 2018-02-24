import os

from dotenv import load_dotenv

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(THIS_DIR, '.env'))

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
