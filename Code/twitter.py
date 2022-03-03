from sentence import get_sentance
from markov import Markov
from sentence import create_histogram
from tokens import tokenize
from requests_oauthlib import OAuth1Session
import os
import dotenv

dotenv.load_dotenv('.env')

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
twitter_access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
twitter_access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

session = OAuth1Session(client_key=consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=twitter_access_token,
                        resource_owner_secret=twitter_access_token_secret)

def tweet(content):
  print(consumer_key, consumer_secret, twitter_access_token, twitter_access_token_secret)
  response = session.post("https://api.twitter.com/2/tweets", json={ "text": content })
  print(response.text)

if __name__ == "__main__":
  TEXT_FILE = 'data/sample.txt'
  words = tokenize(TEXT_FILE)
  histogram = create_histogram(words)
  markov = Markov(histogram, words)
  tweet(get_sentance(histogram, markov, 5))
