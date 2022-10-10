
#// Jai, CS15149
#// Hello from the C preprocessor, using includes to make this code into a single file.
#include "include/includes.h.py"
#include "include/constants.py"
#include "include/util.py"
#include "include/turtle.py"
#include "include/gif.py"
#include "include/cli.py"
#ifndef INCLUDES
from include.cli import cli
from include.turtle import assure_state
from turtle import colormode
#endif
if __name__ == "__main__":
    assure_state()
    colormode(255)
    cli()
