#ifndef INCLUDES
from turtle import *
from typing import *
from dataclasses import *
from struct import unpack
from constants import *
from include.gif.data import GIFData, GlobalColorTable
from util import debug, dump
#endif

class GIFReader:
    data: bytes 
    pixels: Dict[Tuple[int,int],int] = {}
    pallete: Dict[int, Tuple[int,int,int]] = {}
    pos: int
    gif_data: GIFData
    def __init__(self, binary):
        self.data = binary
        self.pos = 0

    def peek(self, length: int) -> bytes:
        return self.data[self.pos:self.pos+length]
    """
    REMEMBER: This file is stored in little-endian notation, as is GIF standard.
    """
    def read(self, length: int) -> bytes:
        self.pos += length
        result = self.data[self.pos-length:self.pos]
        dump(f"Read {length} bytes at {self.pos - length} (0x{self.pos - length:02x})")
        dump(f"Result: {result}")
        return result

    def read_byte(self) -> int:
        # convert byte to int
        return int.from_bytes(self.read(1), byteorder='little')

    def read_bytes(self, length: int) -> bytes:
        return self.read(length)

    def read_short(self) -> int:
        return int.from_bytes(self.read(2), byteorder='little')

    def read_int(self) -> int:
        return int.from_bytes(self.read(4), byteorder='little')
    
    def read_string(self, length: int) -> str:
        return "".join([chr(self.read_byte()) for i in range(length)])

    def read_color(self) -> Tuple[int,int,int]:
        return (self.read_byte(), self.read_byte(), self.read_byte())
    
    #// read complex data

    def read_gif_data(self) -> GIFData:
        if self.pos != 0:
            debug("Warning: GIF header is not at the beginning of the file. We'll ignore this for now but it's probably a bug.")
        
        #// read header
        header = self.read_string(6)
        debug(f"Header: {header}")
        if header != "GIF87a" and header != "GIF89a":
            raise Exception("Invalid GIF header")
        version = header[3:]
        debug(f"Version: {version}")
        width = self.read_short()
        height = self.read_short()
        packed = self.read_byte()
        #// read global color table
        has_global_color_table = (packed & 0b10000000) != 0
        color_resolution = (packed & 0b01110000) >> 4
        sort = (packed & 0b00001000) != 0
        sizeof_global_color_table = (2 **(packed & 0b00000111)) + 1
        debug(f"Global Color Table: {has_global_color_table}")
        debug(f"Color Resolution: {color_resolution}")
        debug(f"Sort: {sort}")
        debug(f"Size of Global Color Table: {sizeof_global_color_table}")
        return GIFData(
            header, version, width, height,
            has_global_color_table, color_resolution,
            sort, sizeof_global_color_table
        )
    
    def read_global_color_table(self) -> GlobalColorTable:
        colors = []
        for i in range(self.gif_data.sizeof_global_color_table):
            colors.append(self.read_color())
        return GlobalColorTable(colors)
    
        


    
    def determine_next_section(self) -> int:
        """
        Section Markers
        0x21: Extension
        0x2c: Image Descriptor
        0x3b: Trailer
        """
        return self.read_byte()
    
    def read_whole_section(self) -> Any:
        marker = self.determine_next_section()
        if marker == GIF_SECTION_EXTENSION:
            return self.read_extension()
        elif marker == GIF_SECTION_IMAGE:
            return self.read_image_descriptor()
        elif marker == GIF_SECTION_TRAILER:
            return self.read_trailer()
        else:
            raise Exception(f"Invalid section marker: {marker}")