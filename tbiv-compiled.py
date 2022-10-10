# 0 "tbiv.h"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 0 "<command-line>" 2
# 1 "tbiv.h"


#pragma region LIB

# 1 "lib/__init__.py" 1

# 1 "lib/constants.py" 1




PX_X = 2
PX_Y = 2


VERBOSE = True
TURTLE_POOL_SIZE
TURTLE_POOL = [make_turtle_mask() for i in range(TURTLE_POOL_SIZE)]
# 3 "lib/__init__.py" 2
# 1 "lib/util.py" 1





POS_X = lambda x_cord: (x_cord * PX_X)
POS_Y = lambda y_cord: window_height() - (y_cord * PX_Y)

def debug(*a, **kw):
    if VERBOSE:
        print(*a, **kw)
# 4 "lib/__init__.py" 2

# 1 "lib/_turtle/__init__.py" 1
# 6 "lib/__init__.py" 2
# 6 "tbiv.h" 2

#pragma endregion

# 1 "tbiv.py" 1
"""
Jai, CS15149

Proj Description:
    Retrieve an image over the internet and draw it using `turtle` library.

Requirements:
    - Analyze image pixel data to find abstract geometry within the image to optimize image drawing
    - Draw abstract geometry in multiple threads both accessing the same screen
    - Fully draw image.
"""
# 10 "tbiv.h" 2
