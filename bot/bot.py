
from twython import Twython
import datetime
from . import config
from . import parsing
from . import images

EARTH_ROVER_ID = 2714673572


def get_twython():
    twython = Twython(config.consumer_key, config.consumer_secret,
                      config.access_token, config.access_token_secret)
    return twython


def test_search_user(self, twython, user_id):
    return twython.get_user_timeline(user_id=user_id, include_rts=False, count=200, exclude_replies=True)


def make_gif(output_file, tweet_list, hours=4):

    # Parse out datetime, url pairs from tweets
    parsed_tweets = parsing.parse_tweets(tweet_list)

    # Filter down to the last N hours of tweets
    last_tweet = parsed_tweets[-1]
    time_filter = last_tweet.ts - datetime.timedelta(minutes=hours * 60)
    time_limited = filter(lambda tweet: tweet.ts > time_filter, parsed_tweets)

    # Download images
    urls = map(lambda tweet: tweet.media, time_limited)
    files = images.get_images_from_urls(urls)

    # Sometimes the same image is posted twice in a row; fiter these
    filtered_files = images.filter_similar_images(files)

    # Make a GIF!
    output_path = images.make_gif_from_files(output_file, filtered_files)
