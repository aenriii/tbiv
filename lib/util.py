#ifndef COMPILED
from .constants import VERBOSE, PX_X, PX_Y
from turtle import window_height
#endif

POS_X = lambda x_cord: (x_cord * PX_X)
POS_Y = lambda y_cord: window_height() - (y_cord * PX_Y)

def debug(*a, **kw):
    if VERBOSE:
        print(*a, **kw)
