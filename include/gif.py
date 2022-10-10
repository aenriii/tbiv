
#ifndef INCLUDES
from turtle import *
from typing import *
from dataclasses import *
from struct import unpack
from util import *
from constants import *
#endif
#// act like https://www.researchgate.net/profile/Cristian-Duran-Faundez/publication/29625723/figure/fig2/AS:339630110068751@1457985536736/Original-test-image-128x128-pixels.png
def try_import_image(file):
    try:
        from PIL import Image
        from io import BytesIO
        with Image.open(file) as im:
            pxs = im.load()
            w = im.width
            h = im.height
            return { (x,y): pxs[x,y] for x in range(im.width) for y in range(im.height)  }
    except Exception as e:
        debug("WARN! Exception occurred in try_import_image. Do you have Pillow/PIL installed?")
        debug(e)

        return False

def try_import_url(url):
    try:
        import requests
        from io import BytesIO
        return try_import_image(BytesIO(requests.get(url).content))
    except Exception as e:
        debug("WARN! Exception occurred in try_import_url. If nothing talks about try_import_image, check to make sure you have io and requests packages,")
    


