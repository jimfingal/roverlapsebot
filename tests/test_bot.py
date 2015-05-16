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

        gif = bot.make_gif(self.output_file, self.tweets, hours=3)
