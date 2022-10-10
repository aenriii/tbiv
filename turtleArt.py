# 0 "turtleArt.pre.py"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 0 "<command-line>" 2
# 1 "turtleArt.pre.py"



# 1 "include/includes.h.py" 1
       

from turtle import ht, pen, setworldcoordinates, up, end_fill, xcor, ycor, goto, color, fd, rt, lt, bk, window_width, window_height, Screen, colormode, up, down, begin_fill, end_fill, speed
from typing import List, Dict, Tuple
from dataclasses import dataclass
from struct import unpack
# 5 "turtleArt.pre.py" 2
# 1 "include/constants.py" 1
       







PX_X = 2
PX_Y = 2

POS_X = lambda x_cord: (x_cord * PX_X)
POS_Y = lambda y_cord: window_height() - (y_cord * PX_Y)

VERBOSE = True
HEXDUMP_ON_PANIC = True

DUMP_ENABLED = False

SCREEN = Screen()
# 6 "turtleArt.pre.py" 2
# 1 "include/util.py" 1
# 9 "include/util.py"
def debug(msg):
    if (VERBOSE):
        print(msg)
def dump(msg):
    if (DUMP_ENABLED):
        print(msg)
bounds = lambda bound_old, bound_new, dim_old: (dim_old + (bound_old - bound_new)) if bound_old > bound_new else dim_old
# 7 "turtleArt.pre.py" 2
# 1 "include/turtle.py" 1
       
# 11 "include/turtle.py"
def assure_state():
    ht()
    SCREEN.colormode(255)
    pen(speed=10)
    speed(0)
    setworldcoordinates(0,0,window_width(),window_height())
    up()
    end_fill()


def coord_pos():
    return (POS_X(xcor()), POS_Y(ycor()))


def draw_px_at(x, y):

    goto(POS_X(x), POS_Y(y))
    down()
    begin_fill()
    fd(PX_X)
    rt(90)
    fd(PX_Y)
    rt(90)
    fd(PX_X)
    rt(90)
    fd(PX_Y)
    rt(90)
    end_fill()
    up()
def draw_rgbpx_at(x, y, rgb_triplet):
    color(rgb_triplet)
    draw_px_at(x,y)

def draw_px2rgb_arr(arr):
    assure_state()
    print("WARNING! THIS ASSUMES tqdm IS INSTALLED, IF IT IS NOT PLEASE INSTALL IT USING python3 -m pip install tqdm (make sure it is installed somewhere on PATH")

    if not arr:
        print("arr not truthy?")
        return
    from tqdm import tqdm
    for (x, y) in tqdm(list(arr.keys())):


        draw_rgbpx_at(x,y,arr[(x,y)])
# 8 "turtleArt.pre.py" 2
# 1 "include/gif.py" 1
# 11 "include/gif.py"
def try_import_image(file):
    try:
        from PIL import Image
        from io import BytesIO
        with Image.open(file) as im:
            pxs = im.load()
            w = im.width
            h = im.height
            return { (x,y): pxs[x,y] for x in range(im.width) for y in range(im.height) }
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
# 9 "turtleArt.pre.py" 2
# 1 "include/cli.py" 1





def cli():
    from sys import argv
    if len(argv) == 1:
        argv = ["test"]
    else:
        argv = argv[1:]
    for place, thing in enumerate(argv):
        if thing == "web_import":
            draw_px2rgb_arr(try_import_url(argv[place+1]))
        elif thing == "local_import":
            draw_px2rgb_arr(try_import_image(argv[place+1]))
        else:
            print(f"Unknown arg {thing} at index {place}" if thing != "test" else "")
            draw_px2rgb_arr(try_import_url("https://placekitten.com/100/100"))
# 10 "turtleArt.pre.py" 2

if __name__ == "__main__":
    assure_state()
    colormode(255)
    cli()
