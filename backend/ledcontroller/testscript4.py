#!/usr/bin/python3

import sys
import cmd
import board
import time
import LedArray
import ColorKeeper

numpixels = 96

la = LedArray.LedArray("Skaplys",  board.SCK, board.MOSI, numpixels,  0xff0000)

ck = ColorKeeper.ColorKeeper(5)

# Regnbue

while True:
    la.SetSolidColor(ck.GetNextColor().replace("#", "0x"))
    time.sleep(0.1)

        

