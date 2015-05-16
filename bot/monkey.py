import images2gif
from PIL.GifImagePlugin import getheader


def patch_image_headers():
    """Monkey-patches an enclosed function within images2gif.writeGif."""

    def patched_get_header(im):

        header = getheader(im)

        if header[1] is not None:
            return header
        else:
            return im.palette.getdata()

    images2gif.writeGif.__globals__['getheader'] = patched_get_header
