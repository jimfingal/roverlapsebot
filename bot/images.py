import os
from PIL import Image
from cStringIO import StringIO
import requests


def get_image_from_url(url):
    r = requests.get(url)
    img = Image.open(StringIO(r.content))
    return img


def save_and_get_image_path(root, name, img):
    img_path = os.path.joinpath(root, name)
    img.save(img_path, format='PNG')
    return img_path
