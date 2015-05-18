from . import parsing
from . import images


def get_user_tweets(twython, user_id):
    return twython.get_user_timeline(user_id=user_id,
                                     include_rts=False,
                                     count=200,
                                     exclude_replies=False)


def parse_and_filter_tweets(tweet_list, hours=4):

    # Parse out datetime, url pairs from tweets
    parsed_tweets = parsing.parse_tweets(tweet_list)
    time_limited = parsing.only_last_n_hours_of_tweets(parsed_tweets, hours)

    return time_limited


def make_gif(output_file, parsed_tweets):

    # Download images
    urls = map(lambda tweet: tweet.media, parsed_tweets)
    files = images.get_images_from_urls(urls)

    # Sometimes the same image is posted twice in a row; fiter these
    filtered_files = images.filter_similar_images(files)
    resized_images = images.resize_images(filtered_files, 350)
    
    # Make a GIF!
    output_path = images.make_gif_from_files(output_file, resized_images)

    return output_path


def get_tweet_text(parsed_tweets):

    first = parsed_tweets[0]
    last = parsed_tweets[-1]

    return "Summary from %s to %s" % (first.ts.ctime(), last.ts.ctime())