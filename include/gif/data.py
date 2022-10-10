#ifndef INCLUDES
from dataclasses import dataclass
from typing import *

#endif



@dataclass
class GIFData:
    header: str
    version: str
    width: int
    height: int
    has_global_color_table: bool
    color_resolution: int
    sort: bool
    sizeof_global_color_table: int

@dataclass
class GlobalColorTable:
    colors: List[Tuple[int,int,int]]