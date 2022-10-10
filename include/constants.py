#pragma once
#ifndef INCLUDES
from turtle import *
from typing import *
from dataclasses import *
from struct import unpack
#endif

PX_X = 2
PX_Y = 2

POS_X = lambda x_cord: (x_cord * PX_X)
POS_Y = lambda y_cord: window_height() - (y_cord * PX_Y)

VERBOSE = True
HEXDUMP_ON_PANIC = True
#// This allows data dumps to be printed to the console for verbose debugging
DUMP_ENABLED = False

SCREEN = Screen()
