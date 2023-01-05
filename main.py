import jdatetime
import math
import tweepy
import os

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

empty = "░"
full = "▓"
total = 15


def get_today_progress():
    today = jdatetime.date.today()
    yesterday = today - jdatetime.timedelta(days=1)
    today_progress = math.floor(int(today.strftime("%j")) / 365 * 100)
    yesterday_progress = math.floor(int(yesterday.strftime("%j")) / 365 * 100)
    if (today_progress - yesterday_progress == 1):
        return today_progress
    return -1


def get_progress_bar(percent):
    full_count = math.floor(percent * total / 100)
    empty_count = total - full_count
    return full * full_count + empty * empty_count + " " + str(percent) + "%"


progress = get_today_progress()
if (progress != -1):
    progress_bar = get_progress_bar(progress)
    api.update_status(progress_bar)
