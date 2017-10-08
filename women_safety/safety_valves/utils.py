import tweepy
from django.core.mail import send_mass_mail
from django.core.mail import send_mail

CONSUMER_KEY = "YKj0zjGTgfZo3FRq9rGK0fNTS"
CONSUMER_SECRET = "L5fh1F9zmniw0zrBenjejwO9gZOyK6LXqwzk7da1Kgl4b4aQpF"
ACCESS_TOKEN = "845563840993488897-vyOmIsWBf1Eu5q50srbrPxOjfREGzFr"
ACCESS_TOKEN_SECRET = "6FiZtvz5iaH6SCqzepXOTBpaVEWyOCSenuLyZFTBCoDsM"

def post_to_twitter(tweet):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    api.update_status(tweet)

def send_email(message):
    message = tuple(message)
    send_mass_mail(message, fail_silently=False)