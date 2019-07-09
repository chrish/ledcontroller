class ColorKeeper:
    r = 255
    g = 0
    b = 0

    stepping = 50

    activecolor = "blue"

    def __init__(self, stp=50):
        self.stepping = stp

    def _Clamp(self, x): 
        return max(0, min(x, 255))

    def SetColorOffset(self, offset):
        for i in range(0, offset):
            self.GetNextColor()

    # Get the next color
    # Activecolor is the color currently being changed. 
    # To see if we're going up or down, check which of the others are on 255
    def GetNextColor(self):
        if self.activecolor == "red":
            if self.b >= 255 and self.r > 0:
                self.r = max(self.r - self.stepping, 0)
            elif self.g >= 255 and self.r < 255:
                self.r = min(self.r + self.stepping, 255)
        if self.activecolor == "blue":
            if self.g >= 255 and self.b > 0:
                self.b = max(self.b - self.stepping, 0)
            elif self.r >= 255 and self.b < 255:
                self.b = min(self.b + self.stepping, 255)
        if self.activecolor == "green":
            if self.r >= 255 and self.g > 0:
                self.g = max(self.g - self.stepping, 0)
            elif self.b >= 255 and self.g < 255:
                self.g = min(self.g + self.stepping, 255)
            
        # Switch to new active color if constraints are met to keep track of which component to increase/decrease
        if (self.r == 255 and self.b == 0 and self.g == 0) or (self.r == 0 and self.g == 255 and self.b == 255):
            self.activecolor = "blue"
        elif (self.r == 255 and self.b == 0 and self.g == 255) or (self.r == 0 and self.g == 0 and self.b == 255):
            self.activecolor = "green"
        elif (self.r == 255 and self.b == 255 and self.g == 0) or (self.r == 0 and self.g == 255 and self.b == 0):
            self.activecolor = "red"

        # return actual color
        #return hex(self.r) + hex(self.g) + hex(self.b)
        # https://stackoverflow.com/questions/3380726/converting-a-rgb-color-tuple-to-a-six-digit-code-in-python
        return "#{0:02x}{1:02x}{2:02x}".format(self._Clamp(self.r), self._Clamp(self.g), self._Clamp(self.b))