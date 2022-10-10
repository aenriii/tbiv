#ifndef INCLUDES
from gif import *
from turtle import *
#endif

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
    
