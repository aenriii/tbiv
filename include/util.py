#ifndef INCLUDES
from turtle import *
from typing import *
from dataclasses import *
from struct import unpack
from constants import *
#endif

def debug(msg):
    if (VERBOSE):
        print(msg)
def dump(msg):
    if (DUMP_ENABLED):
        print(msg)
bounds = lambda bound_old, bound_new, dim_old: (dim_old + (bound_old - bound_new)) if bound_old > bound_new else dim_old 
