# Twitter bot series - consciousness bot

This bot tweets an inspirational status, intended to help raise the level of consciousness of the reader, or at least to make them feel a bit happier.

## Dependencies - what to install

This bot uses the following third party modules:

- tweepy (for access to Twitter api)
- psycopg2 (for interaction with postgresql)

Install these with pip in your virtual environment or globally. To learn how to work in virtual environments with python, you can read my [blog post here.](https://medium.com/@janelgbrandon/setting-up-a-python-development-environment-2e18447cbc24)

## Dependencies - database and enviroment variables

### Database requirements

This bot uses a postgresql db instance. It assumes that the following environment variables are exported (see db_connect.py):

- DBUSER (your postgresql user name)
- DBPW (your postgresql password)
- TWITTERDB (the database you are using for this bot)

This assumes you have a postgresql server instance running on port 5432 on localhost. You will have to modify the db_connect.py if you are using a non-default port or an external server.

You can create a database in your postgresql instance with a simple CREATE DATABASE command. You will have to do this before you use this bot, and specify the database name for the TWITTERDB environment variable.

### Authorization requirements

This bot authenticates with Twitter, and requires that you have a [developer account](https://developer.twitter.com/en/apply-for-access.html)

The bot assumes the following environment variables are set for authentication (see twitter_auth.py module). These values will be shown when you apply for a developer account, or when you view your developer account information in Twitter (at developer.twitter.com):

- TWITTER_CONSUMER_KEY
- TWITTER_CONSUMER_SECRET
- TWITTER_ACCESS_TOKEN_KEY
- TWITTER_ACCESS_TOKEN_SECRET

## Setting up the database

The create_db.py module is included to create and populate the 'twinspirations' table. This table will store your inspirational messages, along with a self-incrementing id and a last_sent date field. The idea is that the bot will cycle through these messages, sending one each time it is run, and updating last_sent when it posts a message as a status (to put it to the back of the queue).

Add your own messages (a comma-separated list of strings) to the create_db.py file, in the call to the populate_twinspirations function.

Run ```python create_db.py``` to create the table and populate it after you have added messages.

## Running the bot

When you run ```python consciousness_bot.py``` it will get the oldest message from the database table, set it for your status, and update the last_sent in the record.
