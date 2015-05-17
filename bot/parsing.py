from dateutil.parser import parse
from collections import namedtuple

PostedImage = namedtuple('PostedImage', ['ts', 'media'])


def parse_tweets(tweet_list):
    with_media = only_tweets_with_media(tweet_list)
    parsed_posted_images = map(get_time_and_media, with_media)
    sorted_images = order_by_date_asc(parsed_posted_images)
    return sorted_images


def get_time_and_media(tweet):
    """Returns time and media from a tweet. Raises KeyError if
    the tweet doesn't have an image, so only pass tweets with images"""
    datetime = parse(tweet['created_at'])
    media = tweet['entities']['media'][0].get('media_url')

    return PostedImage(ts=datetime, media=media)


def only_tweets_with_media(tweet_list):
    return filter(lambda tweet: tweet['entities'].get('media') is not None, tweet_list)


def order_by_date_asc(parsed_list):
    return sorted(parsed_list, key=lambda posted_image: posted_image.ts)
