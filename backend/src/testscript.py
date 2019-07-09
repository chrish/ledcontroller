#!/usr/bin/python3

import sys
import cmd
import board
import LedArray

la = LedArray.LedArray("Skaplys", board.SCK, board.MOSI, 104, 0xFFFFFF, 0.8)


col = input("Which color?")

while col!="exit" :
    r = la.SetSolidColor(col)

    if not r :
        print("Color does not exist, so it was not set.")
    else:
        print("Color was set. ")

    col = input("Set new color: ")
