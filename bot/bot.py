
from twython import Twython
from . import config

EARTH_ROVER_ID = 2714673572


def get_twython():
    twython = Twython(config.consumer_key, config.consumer_secret,
                      config.access_token, config.access_token_secret)
    return twython


def test_search_user(self, twython, user_id):
    return twython.get_user_timeline(user_id=user_id, include_rts=False, count=200, exclude_replies=True)
