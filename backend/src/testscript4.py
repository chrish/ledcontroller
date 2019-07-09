#!/usr/bin/python3

import sys
import cmd
import board
import time
import LedArray
import ColorKeeper

numpixels = 104

la = LedArray.LedArray("Skaplys", board.SCK, board.MOSI, numpixels,  0xff0000, 1)

ck = ColorKeeper.ColorKeeper(5)


while True:
    la.SetSolidColor(ck.GetNextColor().replace("#", "0x"))
        #time.sleep(0.1)

        

