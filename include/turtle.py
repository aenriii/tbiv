#pragma once
#ifndef INCLUDES
from turtle import ht, pen, setworldcoordinates, up, end_fill, xcor, ycor, goto, color, fd, rt, lt, bk, window_width, window_height
from typing import *
from dataclasses import *
from struct import unpack
from util import *
from constants import *
#endif

def assure_state():
    ht()
    SCREEN.colormode(255)
    pen(speed=10)
    speed(0)
    setworldcoordinates(0,0,window_width(),window_height())
    up()
    end_fill()

#// get turtle position in coordinate map
def coord_pos():
    return (POS_X(xcor()), POS_Y(ycor()))

#// standard pixel function
def draw_px_at(x, y):
    #// assure_state()
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
    #// arr should be of type Dict[Tuple[int,int],Tuple[int,int,int]]
    if not arr:
        print("arr not truthy?")
        return
    from tqdm import tqdm
    for (x, y) in tqdm(list(arr.keys())):
        
        #// debug(f"drawing {arr[(x,y)]} " + f"at {(x, y)}" + f" (real: ({POS_X(x)}, {POS_Y(y)}))")
        draw_rgbpx_at(x,y,arr[(x,y)])

