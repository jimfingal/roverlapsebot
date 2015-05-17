import time
import logging

import click
from twython import Twython

from bot import config
from bot import bot
from bot import images

EARTH_ROVER_ID = 2714673572


def get_twython():
    twython = Twython(config.consumer_key, config.consumer_secret,
                      config.access_token, config.access_token_secret)
    return twython


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i + n]


@click.command()
@click.option('--post', is_flag=True, help='Whether to post gif to twitter.')
@click.option('--hours', default=4, help='Number of hours to pull from.')
def run_bot(post, hours):
    logging.info("Running bot. Post=%s" % post)

    twython = get_twython()

    logging.info("Getting tweets and parsing them out into minimal representation.")
    tweets = bot.get_user_tweets(twython, EARTH_ROVER_ID)
    parsed_tweets = bot.parse_and_filter_tweets(tweets, hours=hours)

    # If we have too many tweets the image is really big, so chunk it.
    for chunk in chunks(parsed_tweets, 25):

        # Grab the message and gif
        logging.debug("Processing chunk of tweets: %s" % chunk)

        message = bot.get_tweet_text(chunk)
        output_path = images.get_output_path()

        logging.info("Making GIF for: %s :: %s" % (message, output_path))
        gif_path = bot.make_gif(output_path, chunk)
        logging.info("Created %s" % output_path)

        if post:
            logging.info("Uploading GIF to twitter")

            try:
                with open(gif_path, 'rb') as gif_file:
                    upload_response = twython.upload_media(media=gif_file)
                logging.info(upload_response)
                media_id = upload_response['media_id']
         
                logging.info("Waiting a few seconds.")       
                time.sleep(10)

                logging.info("Posting to twitter.")       
                twython.update_status(status=message, media_ids=[media_id])
            except Exception as e:
                logging.error(e)

if __name__ == "__main__":

    log_fmt = "%(levelname)-6s %(processName)s %(filename)-12s:%(lineno)-4d at %(asctime)s: %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    run_bot()
