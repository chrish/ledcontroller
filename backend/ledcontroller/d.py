import time
import random
import board
import adafruit_dotstar as dotstar
    
# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
#dots = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
    
# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
dots = dotstar.DotStar(board.SCK, board.MOSI, 96, brightness=1)
    
dots.fill(0xFF3E96)
dots.show()


