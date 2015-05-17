import os
import unittest
import fixture
from bot import bot


class BotTest(unittest.TestCase):

    def setUp(self):
        # Copy list
        self.tweets = list(fixture.tl)
        self.base_path = os.path.dirname(__file__)
        self.output_file = os.path.join(self.base_path, 'assets/output/bot_img.gif')
    
        if os.path.isfile(self.output_file):
            os.remove(self.output_file)

    def test_make_gif(self):

        if False:
            parsed_tweets = bot.parse_and_filter_tweets(self.tweets, hours=3)
            gif_path = bot.make_gif(self.output_file, parsed_tweets)
            self.assertEqual(gif_path, self.output_file)
            self.assertTrue(os.path.isfile(gif_path))

    def test_tweet_test(self):

        parsed_tweets = bot.parse_and_filter_tweets(self.tweets)
        text = bot.get_tweet_text(parsed_tweets)
        self.assertEqual(text, "Summary from Sat May 16 00:42:16 2015 to Sat May 16 04:21:36 2015")