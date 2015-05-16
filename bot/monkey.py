import images2gif


def patch_image_headers():
    """Monkey-patches an enclosed function within images2gif.writeGif."""

    def patched_get_header(im):
        ret = im.palette.getdata()
        return ret

    images2gif.writeGif.__globals__['getheader'] = patched_get_header
