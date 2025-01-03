import tweepy
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load Twitter API keys from environment variables
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Authenticate to Twitter API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_first_tweet(handle):
    try:
        # Fetch the user's timeline (tweets)
        user = client.get_user(username=handle)
        if user is None or user.data is None:
            return "User not found."
        
        tweets = client.get_users_tweets(id=user.data.id, max_results=5)
        if tweets is None or tweets.data is None:
            return "No tweets found."
        
        first_tweet = tweets.data[0]
        return first_tweet.text
    except tweepy.TooManyRequests as e:
        # Handle rate limit
        print("Rate limit exceeded. Waiting for 15 minutes.")
        time.sleep(15 * 60)  # Wait for 15 minutes
        return get_first_tweet(handle)
    except tweepy.TweepyException as e:
        return f"An error occurred: {e}"