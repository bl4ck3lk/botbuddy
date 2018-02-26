# BotBuddy

## Usage:
### Running locally

`$ make install`

`$ source venv/bin/activate`

`$ pip install --editable .`

Create a `.env` file in `botbuddy/bot` with your Twitter credentials.
The file should look like this:

```
CONSUMER_KEY=some key
CONSUMER_SECRET=some key
ACCESS_TOKEN=some key
ACCESS_SECRET=some key
```

Run examples:

`$ random_retweet deeplearning` (This is going to re-tweet to your feedline!)

`$ twitter_query earlyretirement`

### Deploying to Heroku:

After creating a Heroku account, install the Heroku CLI, and setting your Heroku app for this
repo, do:

#### Set env variables on Heroku:

`$ heroku config:set CONSUMER_KEY=some_key`

`$ heroku config:set CONSUMER_SECRET=some_key`

`$ heroku config:set ACCESS_TOKEN=some_key`

`$ heroku config:set ACCESS_SECRET=some_key`

#### Deploy:

`$ heroku ps:scale worker=1`

`$ git add .`

`$ git commit -m "initial commit"`

`$ git push heroku master`
