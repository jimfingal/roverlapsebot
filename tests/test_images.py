import unittest


class ImageMagicTests(unittest.TestCase):

    def setUp(self):
        # Copy list
        self.image_names = [
            'CFGGnT8VAAE-WHH.jpg',
            'CFGMHrRUMAAMkD5.jpg',
            'CFGO3viVIAA9Vwz.jpg'
        ]

        self.image_urls = [
            'https://pbs.twimg.com/media/CFGGnT8VAAE-WHH.jpg',
            'https://pbs.twimg.com/media/CFGMHrRUMAAMkD5.jpg',
            'https://pbs.twimg.com/media/CFGO3viVIAA9Vwz.jpg'
        ]

