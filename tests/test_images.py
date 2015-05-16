import unittest
import os
import mock
import images2gif
from bot import images
import PIL


class ImageMagicTests(unittest.TestCase):

    def setUp(self):
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

        self.base_path = os.path.dirname(__file__)
        self.output_file = os.path.join(self.base_path, 'assets/output/output.gif')

    def tearDown(self):
        if os.path.isfile(self.output_file):
            os.remove(self.output_file)
        
    def test_url_filename(self):
        for i, url in enumerate(self.image_urls):
            self.assertEqual(images.url_filename(url), self.image_names[i])

    def test_get_bad_image_from_file(self):
        self.assertIsNone(images.get_image_from_file("asfdsafasdf"))

    def test_get_image_from_file(self):
        base_path = os.path.dirname(__file__)
        img_path = os.path.join(base_path, 'assets', self.image_names[0])
        self.assertIsNotNone(images.get_image_from_file(img_path))

    def test_gifify_images(self):

        # Monkey-patch

        from bot import monkey
        monkey.patch_image_headers()

        files = []

        for filename in self.image_names:
            img_path = os.path.join(self.base_path, 'assets', filename)
            img_file = images.get_image_from_file(img_path)
            files.append(img_file)

        self.assertFalse(os.path.isfile(self.output_file))

        images2gif.writeGif(filename=self.output_file, images=files, duration=0.5)
        
        self.assertTrue(os.path.isfile(self.output_file))