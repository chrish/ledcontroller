import adafruit_dotstar
import board

'''
    Represents a led array. One array has dedicated pins, and comes with its own default color and intensity. 
'''
class LedArray:
    Name = ""
    DefaultColor = ""
    DefaultIntensity = ""

    _array = []

    def __init__(self, name, clockpin, datapin, number_of_leds, def_color = "#ffffff", def_intensity = 0.2):
        
        Name = name
        DefaultColor = def_color
        DefaultIntensity = def_intensity

        _array = adafruit_dotstar.DotStar(clockpin, datapin, number_of_leds, brightness=DefaultIntensity)

        
    def SetSolidColor(self, color):
        _array = color

    def SetIntensity(self, intensity):
        if intensity > 0.6:
            intensity = 0.6
        
        self._array.brightness = intensity

    