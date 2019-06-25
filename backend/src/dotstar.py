import LedArray

class dotstar:
    DEFAULT_COLOR = "ffffff"
    DEFAULT_INTENSITY = 0.2

    ledarrays = {}

    def __init__(self, clockpin, datapin, number_of_leds):
        self.ledarrays["Taklys"] = LedArray.LedArray("Taklys", clockpin, datapin, number_of_leds)
        self.ledarrays["Hyllelys"] = LedArray.LedArray("Hyllelys", clockpin, datapin, number_of_leds)

    def GetArrays(self):
        return self.ledarrays
    
    def AllOff(self):
        for x in self.ledarrays.values():
            x.SetIntensity(0)


    def InitLeds(self):
        for x in self.ledarrays.values():
            x.SetIntensity(self.DEFAULT_INTENSITY)
            x.SetSolidColor(self.DEFAULT_COLOR)
