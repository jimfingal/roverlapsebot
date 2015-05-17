import unittest
from mock import patch
import os
import images2gif
from bot import images


class ImageMagicTests(unittest.TestCase):

    def setUp(self):
        self.image_names = [
            'CFGGnT8VAAE-WHH.jpg',
            'CFGMHrRUMAAMkD5.jpg',
            'CFGO3viVIAA9Vwz.jpg'
        ]

        self.similar_images = [
            'CFGXK9XUUAEQ4Xv.jpg',
            'CFGZ7HCUIAAKVlc.jpg'
        ]

        self.image_urls = [
            'https://pbs.twimg.com/media/CFGGnT8VAAE-WHH.jpg',
            'https://pbs.twimg.com/media/CFGMHrRUMAAMkD5.jpg',
            'https://pbs.twimg.com/media/CFGO3viVIAA9Vwz.jpg'
        ]

        self.base_path = os.path.dirname(__file__)
        self.output_file = os.path.join(self.base_path, 'assets/output/output.gif')

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

    def INTEGRATION_download_and_gifify_images(self):

        files = images.get_images_from_urls(self.image_urls)
        output_path = images.make_gif_from_files(self.output_file, files)
        self.assertTrue(os.path.isfile(output_path))

    def test_gifify_images(self):
        files = []

        for filename in self.image_names:
            img_path = os.path.join(self.base_path, 'assets', filename)
            img_file = images.get_image_from_file(img_path)
            files.append(img_file)

        images2gif.writeGif(filename=self.output_file, images=files, duration=0.1 * len(files))
        
        self.assertTrue(os.path.isfile(self.output_file))

    def test_detect_similar_images(self):

        from PIL import Image

        img1 = Image.open(os.path.join(self.base_path, 'assets', self.similar_images[0]))
        img2 = Image.open(os.path.join(self.base_path, 'assets', self.similar_images[1]))
        img3 = Image.open(os.path.join(self.base_path, 'assets', self.image_names[0]))

        self.assertEqual(img1.histogram(), img2.histogram())
        self.assertNotEqual(img1.histogram(), img3.histogram())
        self.assertNotEqual(img2.histogram(), img3.histogram())

        self.assertEqual(1, len(images.filter_similar_images([img1, img2])))
        self.assertEqual(2, len(images.filter_similar_images([img1, img3])))

    def test_output_path(self):
        with patch('time.time', return_value='foo.bar'):
            path = images.get_output_path()
            self.assertEqual(
                path,
                os.path.abspath(os.path.join(self.base_path, "../output/foo-bar.gif"))
            )