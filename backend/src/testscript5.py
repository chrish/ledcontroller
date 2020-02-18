#!/usr/bin/python3

import sys
import cmd
import board
import time
import LedArray
import ColorKeeper

numpixels = 96
#board.SCK, board.MOSI
la = LedArray.LedArray("Skaplys", board.SCK, board.MOSI, numpixels,  0xff0000)

la.IterateOverColors()
