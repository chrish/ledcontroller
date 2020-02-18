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
        print("shown...")
        self._array.show()

    def SetIndividualColor(self, idx, color):
        self._array[idx] = color
        print("indi")
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
        if intensity > 0.6:
            intensity = 0.6
        
        self._array.brightness = intensity

    
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
        "indian_red": 0xB0171F,
        "crimson": 0xDC143C,
        "lightpink": 0xFFB6C1,
        "pink": 0xFFC0CB,
        "palevioletred": 0xDB7093,
        "lavenderblush": 0xFFF0F5,
        "violetred": 0xFF3E96,
        "hotpink": 0xFF69B4,
        "raspberry": 0x872657,
        "deeppink": 0xFF1493,
        "maroon": 0xFF34B3,
        "mediumvioletred": 0xC71585,
        "violetred": 0xD02090,
        "orchid": 0xDA70D6,
        "thistle": 0xD8BFD8,
        "plum": 0xDDA0DD,
        "violet": 0xEE82EE,
        "magenta": 0xFF00FF,
        "darkmagenta": 0x8B008B,
        "purple*": 0x800080,
        "mediumorchid": 0xBA55D3,
        "darkviolet": 0x9400D3,
        "darkorchid": 0x9932CC,
        "indigo": 0x4B0082,
        "blueviolet": 0x8A2BE2,
        "purple": 0x9B30FF,
        "mediumpurple": 0x9370DB,
        "darkslateblue": 0x483D8B,
        "lightslateblue": 0x8470FF,
        "mediumslateblue": 0x7B68EE,
        "slateblue": 0x6A5ACD,
        "ghostwhite": 0xF8F8FF,
        "lavender": 0xE6E6FA,
        "blue": 0x0000FF,
        "mediumblue": 0x0000CD,
        "darkblue": 0x00008B,
        "navy": 0x000080,
        "midnightblue": 0x191970,
        "cobalt": 0x3D59AB,
        "royalblue": 0x4169E1,
        "cornflowerblue": 0x6495ED,
        "lightsteelblue": 0xB0C4DE,
        "lightslategray": 0x778899,
        "slategray": 0x708090,
        "dodgerblue": 0x1E90FF,
        "aliceblue": 0xF0F8FF,
        "steelblue": 0x4682B4,
        "lightskyblue": 0x87CEFA,
        "skyblue": 0x87CEEB,
        "deepskyblue": 0x00B2EE,
        "peacock": 0x33A1C9,
        "lightblue": 0xADD8E6,
        "powderblue": 0xB0E0E6,
        "cadetblue": 0x98F5FF,
        "turquoise": 0x00F5FF,
        "darkturquoise": 0x00CED1,
        "azure": 0xF0FFFF,
        "lightcyan": 0xE0FFFF,
        "paleturquoise": 0xBBFFFF,
        "darkslategray": 0x2F4F4F,
        "cyan": 0x00FFFF,
        "darkcyan": 0x008B8B,
        "teal*": 0x008080,
        "mediumturquoise": 0x48D1CC,
        "lightseagreen": 0x20B2AA,
        "manganeseblue": 0x03A89E,
        "turquoise": 0x40E0D0,
        "coldgrey": 0x808A87,
        "turquoiseblue": 0x00C78C,
        "aquamarine": 0x7FFFD4,
        "mediumspringgreen": 0x00FA9A,
        "mintcream": 0xF5FFFA,
        "springgreen": 0x00FF7F,
        "mediumseagreen": 0x3CB371,
        "seagreen": 0x54FF9F,
        "emeraldgreen": 0x00C957,
        "mint": 0xBDFCC9,
        "cobaltgreen": 0x3D9140,
        "darkseagreen": 0x8FBC8F,
        "palegreen": 0x98FB98,
        "limegreen": 0x32CD32,
        "forestgreen": 0x228B22,
        "lime": 0x00FF00,
        "green": 0x008000,
        "darkgreen": 0x006400,
        "sapgreen": 0x308014,
        "lawngreen": 0x7CFC00,
        "greenyellow": 0xADFF2F,
        "darkolivegreen": 0x556B2F,
        "olivedrab": 0x6B8E23,
        "beige": 0xF5F5DC,
        "lightyellow": 0xFFFFE0,
        "lightgoldenrodyellow": 0xFAFAD2,
        "yellow": 0xFFFF00,
        "warmgrey": 0x808069,
        "olive*": 0x808000,
        "darkkhaki": 0xBDB76B,
        "khaki": 0xF0E68C,
        "palegoldenrod": 0xEEE8AA,
        "banana": 0xE3CF57,
        "gold": 0xFFD700,
        "goldenrod": 0xDAA520,
        "darkgoldenrod": 0xB8860B,
        "orange": 0xFFA500,
        "floralwhite": 0xFFFAF0,
        "oldlace": 0xFDF5E6,
        "wheat": 0xF5DEB3,
        "moccasin": 0xFFE4B5,
        "papayawhip": 0xFFEFD5,
        "blanchedalmond": 0xFFEBCD,
        "eggshell": 0xFCE6C9,
        "tan": 0xD2B48C,
        "brick": 0x9C661F,
        "cadmiumyellow": 0xFF9912,
        "antiquewhite": 0xFAEBD7,
        "burlywood": 0xDEB887,
        "melon": 0xE3A869,
        "carrot": 0xED9121,
        "darkorange": 0xFF8C00,
        "linen": 0xFAF0E6,
        "sandybrown": 0xF4A460,
        "rawsienna": 0xC76114,
        "chocolate": 0xD2691E,
        "ivoryblack": 0x292421,
        "flesh": 0xFF7D40,
        "cadmiumorange": 0xFF6103,
        "burntsienna": 0x8A360F,
        "sienna": 0xA0522D,
        "coral": 0xFF7F50,
        "orangered": 0xFF4500,
        "sepia": 0x5E2612,
        "darksalmon": 0xE9967A,
        "salmon": 0xFF8C69,
        "burntumber": 0x8A3324,
        "tomato": 0xFF6347,
        "salmon": 0xFA8072,
        "snow": 0xFFFAFA,
        "rosybrown": 0xBC8F8F,
        "lightcoral": 0xF08080,
        "indianred": 0xCD5C5C,
        "brown": 0xA52A2A,
        "firebrick": 0xB22222,
        "red": 0xFF0000,
        "darkred": 0x8B0000,
        "maroon*": 0x800000,
        "white": 0xFFFFFF,
        "gainsboro": 0xDCDCDC,
        "lightgrey": 0xD3D3D3,
        "silver*": 0xC0C0C0,
        "darkgray": 0xA9A9A9,
        "gray*": 0x808080,
        "dimgray": 0x696969,
        "black": 0x000000
    }
