import os
import requests
from PIL import Image
from cStringIO import StringIO
import urlparse
from collections import namedtuple

ImageFile = namedtuple('ImageFile', ['img', 'filename'])


def url_filename(url):
    """Get the filename portion of a URL."""
    return os.path.basename(urlparse.urlparse(url).path)


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


def save_and_get_image_path(root, name, img):
    img_path = os.path.joinpath(root, name)
    img.save(img_path, format='PNG')
    return img_path
