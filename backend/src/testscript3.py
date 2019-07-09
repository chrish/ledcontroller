#!/usr/bin/python3

import sys
import cmd
import board
import time
import LedArray
import ColorKeeper

numpixels = 104

la = LedArray.LedArray("Skaplys", board.SCK, board.MOSI, numpixels)

ck = ColorKeeper.ColorKeeper(1)

ckarr = []

for i in range (0, numpixels):
    ckarr.append(ColorKeeper.ColorKeeper())
    ckarr[i].SetColorOffset(i)

while True:
    for i in range (0, numpixels):
        #loop over all pixels
        #shift colors up by one

        col = ckarr[i].GetNextColor()

        #print(int(col.replace("#", "0x"), 16))
        #print(i, col)

        la.SetIndividualColor(i, int(col.replace("#", "0x"), 16))
    time.sleep(0.1)
    
    la.Update()

        

