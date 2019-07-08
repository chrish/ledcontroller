#!/bin/python3

import sys
import LedArray

la = LedArray("Skaplys", 10, 11, 104)

la.SetSolidColor(sys.argv[1])