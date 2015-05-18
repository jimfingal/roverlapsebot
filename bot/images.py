import os
import time
from collections import namedtuple
import logging

import urlparse
import requests
from PIL import Image
from cStringIO import StringIO
import images2gif

import monkey
monkey.patch_image_headers()

ImageFile = namedtuple('ImageFile', ['img', 'filename'])


def get_output_path():
    base_path = os.path.dirname(__file__)
    time_str = str(time.time()).replace('.', '-')
    rel_path = '../output/%s.gif' % time_str
    output_path = os.path.abspath(os.path.join(base_path, rel_path))
    return output_path


def url_filename(url):
    """Get the filename portion of a URL."""
    return os.path.basename(urlparse.urlparse(url).path)


def make_gif_from_files(output_path, files, img_duration=0.125):
    images2gif.writeGif(filename=output_path, images=files, duration=img_duration)
    return output_path


def get_images_from_urls(urls, sleep_between_downloads=0.5):

    files = []

    for i, img_url in enumerate(urls):
        logging.info("Downloading url %s/%s: %s" % (i+  1, len(urls), img_url))
        image_data = get_image_from_url(img_url)
        files.append(image_data)
        time.sleep(sleep_between_downloads)

    return files


def resize_images(images, width=400):
    resized = []
    for image in images:
        resized.append(resize_image(image, width))
    return resized


def resize_image(img, width):
    wpercent = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(wpercent)))
    img2 = img.resize((width, height), Image.NEAREST)
    return img2

def same_images(img1, img2):
    return img1.histogram() == img2.histogram()


def filter_similar_images(image_list):

    filtered_files = []

    last_image = None

    for image in image_list:
        if not last_image or not same_images(last_image, image): 
            filtered_files.append(image)
        last_image = image

    return filtered_files


def get_image_from_file(path):
    """Tries to get an image from a file. Returns None if doesn't exist."""
    try:
        img = Image.open(path)
        return img
    except IOError as e:
        print e
        return None


def get_image_from_url(url):
    r = requests.get(url)
    img = Image.open(StringIO(r.content))
    return img