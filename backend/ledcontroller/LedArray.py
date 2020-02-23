import adafruit_dotstar
import board
import time

'''
    Represents a led array. One array has dedicated pins, and comes with its own default color and intensity. 
'''
class LedArray:
    Name = ""
    DefaultColor = ""
    DefaultIntensity = ""

    order = adafruit_dotstar.RGB
    #, pixel_order = order
    _array = []

    def __init__(self, name = "SomeDefaultStrip", clockpin = board.SCK, datapin =board.MOSI, number_of_leds = 96, def_color = "0xffffff", def_intensity = 0.4):
        Name = name
        DefaultColor = def_color
        DefaultIntensity = def_intensity

        self._array = adafruit_dotstar.DotStar(clockpin, datapin, number_of_leds, brightness=DefaultIntensity, auto_write = True)
        

    def Update(self):
        self._array.show()

    def SetIndividualColor(self, idx, color):
        self._array[idx] = color
        self.Update()
        
    def SetSolidColor(self, color):
        print("C: " + color)
        if color in self.colors:
            self._array.fill(self.colors[color])
            self.Update()
            print("Color found")
            return True
        elif int(color, 16):
            self._array.fill(int(color, 16))
            self.Update()
            return True
        else:
            print("Color not found!")
            return False            


    def SetIntensity(self, intensity):
        self._array.brightness = intensity
        self.Update()

    
    def IterateOverColors(self):
        for c in self.colors:
            print(c)
            self._array.fill(self.colors[c])
            self._array.show()
            time.sleep(1/2)
    
    def GetColors(self):
        return self.colors

    colors = {
        "0x000000": 0x000000,
        "crimson": 0xDC143C,
        "pink": 0xFFC0CB,
        "palevioletred": 0xDB7093,
        "violetred": 0xFF3E96,
        "raspberry": 0x872657,
        "deeppink": 0xFF1493,
        "maroon": 0xFF34B3,
        "violetred": 0xD02090,
        "orchid": 0xDA70D6,
        "thistle": 0xD8BFD8,
        "plum": 0xDDA0DD,
        "violet": 0xEE82EE,
        "magenta": 0xFF00FF,
        "darkmagenta": 0x8B008B,
        "purple*": 0x800080,
        "darkviolet": 0x9400D3,
        "indigo": 0x4B0082,
        "blueviolet": 0x8A2BE2,
        "purple": 0x9B30FF,
        "blue": 0x0000FF,
        "cobalt": 0x3D59AB,
        "royalblue": 0x4169E1,
        "dodgerblue": 0x1E90FF,
        "steelblue": 0x4682B4,
        "deepskyblue": 0x00B2EE,
        "peacock": 0x33A1C9,
        "powderblue": 0xB0E0E6,
        "cadetblue": 0x98F5FF,
        "turquoise": 0x00F5FF,
        "cyan": 0x00FFFF,
        "teal*": 0x008080,
        "lightseagreen": 0x20B2AA,
        "manganeseblue": 0x03A89E,
        "turquoise": 0x40E0D0,
        "turquoiseblue": 0x00C78C,
        "aquamarine": 0x7FFFD4,
        "springgreen": 0x00FF7F,
        "seagreen": 0x54FF9F,
        "emeraldgreen": 0x00C957,
        "mint": 0xBDFCC9,
        "cobaltgreen": 0x3D9140,
        "darkseagreen": 0x8FBC8F,
        "palegreen": 0x98FB98,
        "limegreen": 0x32CD32,
        "lime": 0x00FF00,
        "green": 0x008000,
        "darkgreen": 0x006400,
        "sapgreen": 0x308014,
        "lawngreen": 0x7CFC00,
        "olivedrab": 0x6B8E23,
        "yellow": 0xFFFF00,
        "olive*": 0x808000,
        "banana": 0xE3CF57,
        "gold": 0xFFD700,
        "goldenrod": 0xDAA520,
        "darkgoldenrod": 0xB8860B,
        "orange": 0xFFA500,
        "moccasin": 0xFFE4B5,
        "papayawhip": 0xFFEFD5,
        "tan": 0xD2B48C,
        "brick": 0x9C661F,
        "cadmiumyellow": 0xFF9912,
        "burlywood": 0xDEB887,
        "melon": 0xE3A869,
        "sandybrown": 0xF4A460,
        "rawsienna": 0xC76114,
        "chocolate": 0xD2691E,
        "cadmiumorange": 0xFF6103,
        "burntsienna": 0x8A360F,
        "sienna": 0xA0522D,
        "coral": 0xFF7F50,
        "orangered": 0xFF4500,
        "tomato": 0xFF6347,
        "rosybrown": 0xBC8F8F,
        "darkred": 0x8B0000,
        "maroon*": 0x800000,
        "white": 0xFFFFFF
        
    }
