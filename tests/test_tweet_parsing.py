import unittest
import fixture
from datetime import datetime
from bot import parsing


class TweetParsingTest(unittest.TestCase):

    def setUp(self):
        # Copy list
        self.tweets = list(fixture.tl)

        self.no_media = self.tweets[60]

    def test_parsing_datetime_and_picutre(self):

        tweet = self.tweets[0]

        ts, media = parsing.get_time_and_media(tweet)

        self.assertEqual(type(ts), datetime)
        self.assertEqual(type(media), unicode)
        self.assertIn('https', media)

        with self.assertRaises(KeyError):
            parsing.get_time_and_media(self.no_media)

    def test_named_tuple(self):

        tweet = self.tweets[0]

        posted_image = parsing.get_time_and_media(tweet)

        self.assertEqual(type(posted_image.ts), datetime)
        self.assertEqual(type(posted_image.media), unicode)
        self.assertIn('https', posted_image.media)

    def test_filter_only_with_dates(self):

        only_media = parsing.only_tweets_with_media(self.tweets)

        for tweet in only_media:
            self.assertIn('entities', tweet)
            self.assertIn('media', tweet['entities'])
            self.assertGreater(len(tweet['entities']['media']), 0)

    def test_sort_images(self):

        with_media = parsing.only_tweets_with_media(self.tweets)
        parsed_posted_images = map(parsing.get_time_and_media, with_media)
        sorted_images = parsing.order_by_date_asc(parsed_posted_images)

        last = None
        for image in sorted_images:
            if last is not None:
                self.assertGreater(image.ts, last)
            last = image.ts
 
    def test_parse_tweets(self):

        parsed_tweets = parsing.parse_tweets(self.tweets)
        print parsed_tweets
