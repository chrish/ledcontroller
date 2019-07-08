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

    def __init__(self, name, clockpin, datapin, number_of_leds, def_color = "0xffffff", def_intensity = 0.2):
        Name = name
        DefaultColor = def_color
        DefaultIntensity = def_intensity

        self._array = adafruit_dotstar.DotStar(clockpin, datapin, number_of_leds, brightness=DefaultIntensity)

        
    def SetSolidColor(self, namedColor):
        if namedColor in self.colors:
            self._array.fill(self.colors[namedColor])

            print("Color found")
            return True
        else:
            print("Color not found!")
            return False            

    def SetIntensity(self, intensity):
        if intensity > 0.6:
            intensity = 0.6
        
        self._array.brightness = intensity

    
    colors = {
        "indian_red": 0xB0171F,
        "crimson": 0xDC143C,
        "lightpink": 0xFFB6C1,
        "lightpink_1": 0xFFAEB9,
        "lightpink_2": 0xEEA2AD,
        "lightpink_3": 0xCD8C95,
        "lightpink_4": 0x8B5F65,
        "pink": 0xFFC0CB,
        "pink_1": 0xFFB5C5,
        "pink_2": 0xEEA9B8,
        "pink_3": 0xCD919E,
        "pink_4": 0x8B636C,
        "palevioletred": 0xDB7093,
        "palevioletred_1": 0xFF82AB,
        "palevioletred_2": 0xEE799F,
        "palevioletred_3": 0xCD6889,
        "palevioletred_4": 0x8B475D,
        "lavenderblush_1_(lavenderblush)": 0xFFF0F5,
        "lavenderblush_2": 0xEEE0E5,
        "lavenderblush_3": 0xCDC1C5,
        "lavenderblush_4": 0x8B8386,
        "violetred_1": 0xFF3E96,
        "violetred_2": 0xEE3A8C,
        "violetred_3": 0xCD3278,
        "violetred_4": 0x8B2252,
        "hotpink": 0xFF69B4,
        "hotpink_1": 0xFF6EB4,
        "hotpink_2": 0xEE6AA7,
        "hotpink_3": 0xCD6090,
        "hotpink_4": 0x8B3A62,
        "raspberry": 0x872657,
        "deeppink_1_(deeppink)": 0xFF1493,
        "deeppink_2": 0xEE1289,
        "deeppink_3": 0xCD1076,
        "deeppink_4": 0x8B0A50,
        "maroon_1": 0xFF34B3,
        "maroon_2": 0xEE30A7,
        "maroon_3": 0xCD2990,
        "maroon_4": 0x8B1C62,
        "mediumvioletred": 0xC71585,
        "violetred": 0xD02090,
        "orchid": 0xDA70D6,
        "orchid_1": 0xFF83FA,
        "orchid_2": 0xEE7AE9,
        "orchid_3": 0xCD69C9,
        "orchid_4": 0x8B4789,
        "thistle": 0xD8BFD8,
        "thistle_1": 0xFFE1FF,
        "thistle_2": 0xEED2EE,
        "thistle_3": 0xCDB5CD,
        "thistle_4": 0x8B7B8B,
        "plum_1": 0xFFBBFF,
        "plum_2": 0xEEAEEE,
        "plum_3": 0xCD96CD,
        "plum_4": 0x8B668B,
        "plum": 0xDDA0DD,
        "violet": 0xEE82EE,
        "magenta_(fuchsia*)": 0xFF00FF,
        "magenta_2": 0xEE00EE,
        "magenta_3": 0xCD00CD,
        "magenta_4_(darkmagenta)": 0x8B008B,
        "purple*": 0x800080,
        "mediumorchid": 0xBA55D3,
        "mediumorchid_1": 0xE066FF,
        "mediumorchid_2": 0xD15FEE,
        "mediumorchid_3": 0xB452CD,
        "mediumorchid_4": 0x7A378B,
        "darkviolet": 0x9400D3,
        "darkorchid": 0x9932CC,
        "darkorchid_1": 0xBF3EFF,
        "darkorchid_2": 0xB23AEE,
        "darkorchid_3": 0x9A32CD,
        "darkorchid_4": 0x68228B,
        "indigo": 0x4B0082,
        "blueviolet": 0x8A2BE2,
        "purple_1": 0x9B30FF,
        "purple_2": 0x912CEE,
        "purple_3": 0x7D26CD,
        "purple_4": 0x551A8B,
        "mediumpurple": 0x9370DB,
        "mediumpurple_1": 0xAB82FF,
        "mediumpurple_2": 0x9F79EE,
        "mediumpurple_3": 0x8968CD,
        "mediumpurple_4": 0x5D478B,
        "darkslateblue": 0x483D8B,
        "lightslateblue": 0x8470FF,
        "mediumslateblue": 0x7B68EE,
        "slateblue": 0x6A5ACD,
        "slateblue_1": 0x836FFF,
        "slateblue_2": 0x7A67EE,
        "slateblue_3": 0x6959CD,
        "slateblue_4": 0x473C8B,
        "ghostwhite": 0xF8F8FF,
        "lavender": 0xE6E6FA,
        "blue*": 0x0000FF,
        "blue_2": 0x0000EE,
        "blue_3_(mediumblue)": 0x0000CD,
        "blue_4_(darkblue)": 0x00008B,
        "navy*": 0x000080,
        "midnightblue": 0x191970,
        "cobalt": 0x3D59AB,
        "royalblue": 0x4169E1,
        "royalblue_1": 0x4876FF,
        "royalblue_2": 0x436EEE,
        "royalblue_3": 0x3A5FCD,
        "royalblue_4": 0x27408B,
        "cornflowerblue": 0x6495ED,
        "lightsteelblue": 0xB0C4DE,
        "lightsteelblue_1": 0xCAE1FF,
        "lightsteelblue_2": 0xBCD2EE,
        "lightsteelblue_3": 0xA2B5CD,
        "lightsteelblue_4": 0x6E7B8B,
        "lightslategray": 0x778899,
        "slategray": 0x708090,
        "slategray_1": 0xC6E2FF,
        "slategray_2": 0xB9D3EE,
        "slategray_3": 0x9FB6CD,
        "slategray_4": 0x6C7B8B,
        "dodgerblue_1_(dodgerblue)": 0x1E90FF,
        "dodgerblue_2": 0x1C86EE,
        "dodgerblue_3": 0x1874CD,
        "dodgerblue_4": 0x104E8B,
        "aliceblue": 0xF0F8FF,
        "steelblue": 0x4682B4,
        "steelblue_1": 0x63B8FF,
        "steelblue_2": 0x5CACEE,
        "steelblue_3": 0x4F94CD,
        "steelblue_4": 0x36648B,
        "lightskyblue": 0x87CEFA,
        "lightskyblue_1": 0xB0E2FF,
        "lightskyblue_2": 0xA4D3EE,
        "lightskyblue_3": 0x8DB6CD,
        "lightskyblue_4": 0x607B8B,
        "skyblue_1": 0x87CEFF,
        "skyblue_2": 0x7EC0EE,
        "skyblue_3": 0x6CA6CD,
        "skyblue_4": 0x4A708B,
        "skyblue": 0x87CEEB,
        "deepskyblue_1_(deepskyblue)": 0x00BFFF,
        "deepskyblue_2": 0x00B2EE,
        "deepskyblue_3": 0x009ACD,
        "deepskyblue_4": 0x00688B,
        "peacock": 0x33A1C9,
        "lightblue": 0xADD8E6,
        "lightblue_1": 0xBFEFFF,
        "lightblue_2": 0xB2DFEE,
        "lightblue_3": 0x9AC0CD,
        "lightblue_4": 0x68838B,
        "powderblue": 0xB0E0E6,
        "cadetblue_1": 0x98F5FF,
        "cadetblue_2": 0x8EE5EE,
        "cadetblue_3": 0x7AC5CD,
        "cadetblue_4": 0x53868B,
        "turquoise_1": 0x00F5FF,
        "turquoise_2": 0x00E5EE,
        "turquoise_3": 0x00C5CD,
        "turquoise_4": 0x00868B,
        "cadetblue": 0x5F9EA0,
        "darkturquoise": 0x00CED1,
        "azure_1_(azure)": 0xF0FFFF,
        "azure_2": 0xE0EEEE,
        "azure_3": 0xC1CDCD,
        "azure_4": 0x838B8B,
        "lightcyan_1_(lightcyan)": 0xE0FFFF,
        "lightcyan_2": 0xD1EEEE,
        "lightcyan_3": 0xB4CDCD,
        "lightcyan_4": 0x7A8B8B,
        "paleturquoise_1": 0xBBFFFF,
        "paleturquoise_2_(paleturquoise)": 0xAEEEEE,
        "paleturquoise_3": 0x96CDCD,
        "paleturquoise_4": 0x668B8B,
        "darkslategray": 0x2F4F4F,
        "darkslategray_1": 0x97FFFF,
        "darkslategray_2": 0x8DEEEE,
        "darkslategray_3": 0x79CDCD,
        "darkslategray_4": 0x528B8B,
        "cyan_/_aqua*": 0x00FFFF,
        "cyan_2": 0x00EEEE,
        "cyan_3": 0x00CDCD,
        "cyan_4_(darkcyan)": 0x008B8B,
        "teal*": 0x008080,
        "mediumturquoise": 0x48D1CC,
        "lightseagreen": 0x20B2AA,
        "manganeseblue": 0x03A89E,
        "turquoise": 0x40E0D0,
        "coldgrey": 0x808A87,
        "turquoiseblue": 0x00C78C,
        "aquamarine_1_(aquamarine)": 0x7FFFD4,
        "aquamarine_2": 0x76EEC6,
        "aquamarine_3_(mediumaquamarine)": 0x66CDAA,
        "aquamarine_4": 0x458B74,
        "mediumspringgreen": 0x00FA9A,
        "mintcream": 0xF5FFFA,
        "springgreen": 0x00FF7F,
        "springgreen_1": 0x00EE76,
        "springgreen_2": 0x00CD66,
        "springgreen_3": 0x008B45,
        "mediumseagreen": 0x3CB371,
        "seagreen_1": 0x54FF9F,
        "seagreen_2": 0x4EEE94,
        "seagreen_3": 0x43CD80,
        "seagreen_4_(seagreen)": 0x2E8B57,
        "emeraldgreen": 0x00C957,
        "mint": 0xBDFCC9,
        "cobaltgreen": 0x3D9140,
        "honeydew_1_(honeydew)": 0xF0FFF0,
        "honeydew_2": 0xE0EEE0,
        "honeydew_3": 0xC1CDC1,
        "honeydew_4": 0x838B83,
        "darkseagreen": 0x8FBC8F,
        "darkseagreen_1": 0xC1FFC1,
        "darkseagreen_2": 0xB4EEB4,
        "darkseagreen_3": 0x9BCD9B,
        "darkseagreen_4": 0x698B69,
        "palegreen": 0x98FB98,
        "palegreen_1": 0x9AFF9A,
        "palegreen_2_(lightgreen)": 0x90EE90,
        "palegreen_3": 0x7CCD7C,
        "palegreen_4": 0x548B54,
        "limegreen": 0x32CD32,
        "forestgreen": 0x228B22,
        "green_1_(lime*)": 0x00FF00,
        "green_2": 0x00EE00,
        "green_3": 0x00CD00,
        "green_4": 0x008B00,
        "green*": 0x008000,
        "darkgreen": 0x006400,
        "sapgreen": 0x308014,
        "lawngreen": 0x7CFC00,
        "chartreuse_1_(chartreuse)": 0x7FFF00,
        "chartreuse_2": 0x76EE00,
        "chartreuse_3": 0x66CD00,
        "chartreuse_4": 0x458B00,
        "greenyellow": 0xADFF2F,
        "darkolivegreen_1": 0xCAFF70,
        "darkolivegreen_2": 0xBCEE68,
        "darkolivegreen_3": 0xA2CD5A,
        "darkolivegreen_4": 0x6E8B3D,
        "darkolivegreen": 0x556B2F,
        "olivedrab": 0x6B8E23,
        "olivedrab_1": 0xC0FF3E,
        "olivedrab_2": 0xB3EE3A,
        "olivedrab_3_(yellowgreen)": 0x9ACD32,
        "olivedrab_4": 0x698B22,
        "ivory_1_(ivory)": 0xFFFFF0,
        "ivory_2": 0xEEEEE0,
        "ivory_3": 0xCDCDC1,
        "ivory_4": 0x8B8B83,
        "beige": 0xF5F5DC,
        "lightyellow_1_(lightyellow)": 0xFFFFE0,
        "lightyellow_2": 0xEEEED1,
        "lightyellow_3": 0xCDCDB4,
        "lightyellow_4": 0x8B8B7A,
        "lightgoldenrodyellow": 0xFAFAD2,
        "yellow_1_(yellow*)": 0xFFFF00,
        "yellow_2": 0xEEEE00,
        "yellow_3": 0xCDCD00,
        "yellow_4": 0x8B8B00,
        "warmgrey": 0x808069,
        "olive*": 0x808000,
        "darkkhaki": 0xBDB76B,
        "khaki_1": 0xFFF68F,
        "khaki_2": 0xEEE685,
        "khaki_3": 0xCDC673,
        "khaki_4": 0x8B864E,
        "khaki": 0xF0E68C,
        "palegoldenrod": 0xEEE8AA,
        "lemonchiffon_1_(lemonchiffon)": 0xFFFACD,
        "lemonchiffon_2": 0xEEE9BF,
        "lemonchiffon_3": 0xCDC9A5,
        "lemonchiffon_4": 0x8B8970,
        "lightgoldenrod_1": 0xFFEC8B,
        "lightgoldenrod_2": 0xEEDC82,
        "lightgoldenrod_3": 0xCDBE70,
        "lightgoldenrod_4": 0x8B814C,
        "banana": 0xE3CF57,
        "gold_1_(gold)": 0xFFD700,
        "gold_2": 0xEEC900,
        "gold_3": 0xCDAD00,
        "gold_4": 0x8B7500,
        "cornsilk_1_(cornsilk)": 0xFFF8DC,
        "cornsilk_2": 0xEEE8CD,
        "cornsilk_3": 0xCDC8B1,
        "cornsilk_4": 0x8B8878,
        "goldenrod": 0xDAA520,
        "goldenrod_1": 0xFFC125,
        "goldenrod_2": 0xEEB422,
        "goldenrod_3": 0xCD9B1D,
        "goldenrod_4": 0x8B6914,
        "darkgoldenrod": 0xB8860B,
        "darkgoldenrod_1": 0xFFB90F,
        "darkgoldenrod_2": 0xEEAD0E,
        "darkgoldenrod_3": 0xCD950C,
        "darkgoldenrod_4": 0x8B6508,
        "orange_1_(orange)": 0xFFA500,
        "orange_2": 0xEE9A00,
        "orange_3": 0xCD8500,
        "orange_4": 0x8B5A00,
        "floralwhite": 0xFFFAF0,
        "oldlace": 0xFDF5E6,
        "wheat": 0xF5DEB3,
        "wheat_1": 0xFFE7BA,
        "wheat_2": 0xEED8AE,
        "wheat_3": 0xCDBA96,
        "wheat_4": 0x8B7E66,
        "moccasin": 0xFFE4B5,
        "papayawhip": 0xFFEFD5,
        "blanchedalmond": 0xFFEBCD,
        "navajowhite_1_(navajowhite)": 0xFFDEAD,
        "navajowhite_2": 0xEECFA1,
        "navajowhite_3": 0xCDB38B,
        "navajowhite_4": 0x8B795E,
        "eggshell": 0xFCE6C9,
        "tan": 0xD2B48C,
        "brick": 0x9C661F,
        "cadmiumyellow": 0xFF9912,
        "antiquewhite": 0xFAEBD7,
        "antiquewhite_1": 0xFFEFDB,
        "antiquewhite_2": 0xEEDFCC,
        "antiquewhite_3": 0xCDC0B0,
        "antiquewhite_4": 0x8B8378,
        "burlywood": 0xDEB887,
        "burlywood_1": 0xFFD39B,
        "burlywood_2": 0xEEC591,
        "burlywood_3": 0xCDAA7D,
        "burlywood_4": 0x8B7355,
        "bisque_1_(bisque)": 0xFFE4C4,
        "bisque_2": 0xEED5B7,
        "bisque_3": 0xCDB79E,
        "bisque_4": 0x8B7D6B,
        "melon": 0xE3A869,
        "carrot": 0xED9121,
        "darkorange": 0xFF8C00,
        "darkorange_1": 0xFF7F00,
        "darkorange_2": 0xEE7600,
        "darkorange_3": 0xCD6600,
        "darkorange_4": 0x8B4500,
        "orange": 0xFF8000,
        "tan_1": 0xFFA54F,
        "tan_2": 0xEE9A49,
        "tan_3_(peru)": 0xCD853F,
        "tan_4": 0x8B5A2B,
        "linen": 0xFAF0E6,
        "peachpuff_1_(peachpuff)": 0xFFDAB9,
        "peachpuff_2": 0xEECBAD,
        "peachpuff_3": 0xCDAF95,
        "peachpuff_4": 0x8B7765,
        "seashell_1_(seashell)": 0xFFF5EE,
        "seashell_2": 0xEEE5DE,
        "seashell_3": 0xCDC5BF,
        "seashell_4": 0x8B8682,
        "sandybrown": 0xF4A460,
        "rawsienna": 0xC76114,
        "chocolate": 0xD2691E,
        "chocolate_1": 0xFF7F24,
        "chocolate_2": 0xEE7621,
        "chocolate_3": 0xCD661D,
        "chocolate_4_(saddlebrown)": 0x8B4513,
        "ivoryblack": 0x292421,
        "flesh": 0xFF7D40,
        "cadmiumorange": 0xFF6103,
        "burntsienna": 0x8A360F,
        "sienna": 0xA0522D,
        "sienna_1": 0xFF8247,
        "sienna_2": 0xEE7942,
        "sienna_3": 0xCD6839,
        "sienna_4": 0x8B4726,
        "lightsalmon_1_(lightsalmon)": 0xFFA07A,
        "lightsalmon_2": 0xEE9572,
        "lightsalmon_3": 0xCD8162,
        "lightsalmon_4": 0x8B5742,
        "coral": 0xFF7F50,
        "orangered_1_(orangered)": 0xFF4500,
        "orangered_2": 0xEE4000,
        "orangered_3": 0xCD3700,
        "orangered_4": 0x8B2500,
        "sepia": 0x5E2612,
        "darksalmon": 0xE9967A,
        "salmon_1": 0xFF8C69,
        "salmon_2": 0xEE8262,
        "salmon_3": 0xCD7054,
        "salmon_4": 0x8B4C39,
        "coral_1": 0xFF7256,
        "coral_2": 0xEE6A50,
        "coral_3": 0xCD5B45,
        "coral_4": 0x8B3E2F,
        "burntumber": 0x8A3324,
        "tomato_1_(tomato)": 0xFF6347,
        "tomato_2": 0xEE5C42,
        "tomato_3": 0xCD4F39,
        "tomato_4": 0x8B3626,
        "salmon": 0xFA8072,
        "mistyrose_1_(mistyrose)": 0xFFE4E1,
        "mistyrose_2": 0xEED5D2,
        "mistyrose_3": 0xCDB7B5,
        "mistyrose_4": 0x8B7D7B,
        "snow_1_(snow)": 0xFFFAFA,
        "snow_2": 0xEEE9E9,
        "snow_3": 0xCDC9C9,
        "snow_4": 0x8B8989,
        "rosybrown": 0xBC8F8F,
        "rosybrown_1": 0xFFC1C1,
        "rosybrown_2": 0xEEB4B4,
        "rosybrown_3": 0xCD9B9B,
        "rosybrown_4": 0x8B6969,
        "lightcoral": 0xF08080,
        "indianred": 0xCD5C5C,
        "indianred_1": 0xFF6A6A,
        "indianred_2": 0xEE6363,
        "indianred_4": 0x8B3A3A,
        "indianred_3": 0xCD5555,
        "brown": 0xA52A2A,
        "brown_1": 0xFF4040,
        "brown_2": 0xEE3B3B,
        "brown_3": 0xCD3333,
        "brown_4": 0x8B2323,
        "firebrick": 0xB22222,
        "firebrick_1": 0xFF3030,
        "firebrick_2": 0xEE2C2C,
        "firebrick_3": 0xCD2626,
        "firebrick_4": 0x8B1A1A,
        "red_1_(red*)": 0xFF0000,
        "red_2": 0xEE0000,
        "red_3": 0xCD0000,
        "red_4_(darkred)": 0x8B0000,
        "maroon*": 0x800000,
        "sgi_beet": 0x8E388E,
        "sgi_slateblue": 0x7171C6,
        "sgi_lightblue": 0x7D9EC0,
        "sgi_teal": 0x388E8E,
        "sgi_chartreuse": 0x71C671,
        "sgi_olivedrab": 0x8E8E38,
        "sgi_brightgray": 0xC5C1AA,
        "sgi_salmon": 0xC67171,
        "sgi_darkgray": 0x555555,
        "sgi_gray_12": 0x1E1E1E,
        "sgi_gray_16": 0x282828,
        "sgi_gray_32": 0x515151,
        "sgi_gray_36": 0x5B5B5B,
        "sgi_gray_52": 0x848484,
        "sgi_gray_56": 0x8E8E8E,
        "sgi_lightgray": 0xAAAAAA,
        "sgi_gray_72": 0xB7B7B7,
        "sgi_gray_76": 0xC1C1C1,
        "sgi_gray_92": 0xEAEAEA,
        "sgi_gray_96": 0xF4F4F4,
        "white*": 0xFFFFFF,
        "white_smoke_(gray_96)": 0xF5F5F5,
        "gainsboro": 0xDCDCDC,
        "lightgrey": 0xD3D3D3,
        "silver*": 0xC0C0C0,
        "darkgray": 0xA9A9A9,
        "gray*": 0x808080,
        "dimgray_(gray_42)": 0x696969,
        "black*": 0x000000,
        "gray_99": 0xFCFCFC,
        "gray_98": 0xFAFAFA,
        "gray_97": 0xF7F7F7,
        "white_smoke_(gray_96)": 0xF5F5F5,
        "gray_95": 0xF2F2F2,
        "gray_94": 0xF0F0F0,
        "gray_93": 0xEDEDED,
        "gray_92": 0xEBEBEB,
        "gray_91": 0xE8E8E8,
        "gray_90": 0xE5E5E5,
        "gray_89": 0xE3E3E3,
        "gray_88": 0xE0E0E0,
        "gray_87": 0xDEDEDE,
        "gray_86": 0xDBDBDB,
        "gray_85": 0xD9D9D9,
        "gray_84": 0xD6D6D6,
        "gray_83": 0xD4D4D4,
        "gray_82": 0xD1D1D1,
        "gray_81": 0xCFCFCF,
        "gray_80": 0xCCCCCC,
        "gray_79": 0xC9C9C9,
        "gray_78": 0xC7C7C7,
        "gray_77": 0xC4C4C4,
        "gray_76": 0xC2C2C2,
        "gray_75": 0xBFBFBF,
        "gray_74": 0xBDBDBD,
        "gray_73": 0xBABABA,
        "gray_72": 0xB8B8B8,
        "gray_71": 0xB5B5B5,
        "gray_70": 0xB3B3B3,
        "gray_69": 0xB0B0B0,
        "gray_68": 0xADADAD,
        "gray_67": 0xABABAB,
        "gray_66": 0xA8A8A8,
        "gray_65": 0xA6A6A6,
        "gray_64": 0xA3A3A3,
        "gray_63": 0xA1A1A1,
        "gray_62": 0x9E9E9E,
        "gray_61": 0x9C9C9C,
        "gray_60": 0x999999,
        "gray_59": 0x969696,
        "gray_58": 0x949494,
        "gray_57": 0x919191,
        "gray_56": 0x8F8F8F,
        "gray_55": 0x8C8C8C,
        "gray_54": 0x8A8A8A,
        "gray_53": 0x878787,
        "gray_52": 0x858585,
        "gray_51": 0x828282,
        "gray_50": 0x7F7F7F,
        "gray_49": 0x7D7D7D,
        "gray_48": 0x7A7A7A,
        "gray_47": 0x787878,
        "gray_46": 0x757575,
        "gray_45": 0x737373,
        "gray_44": 0x707070,
        "gray_43": 0x6E6E6E,
        "gray_42": 0x6B6B6B,
        "dimgray_(gray_42)": 0x696969,
        "gray_40": 0x666666,
        "gray_39": 0x636363,
        "gray_38": 0x616161,
        "gray_37": 0x5E5E5E,
        "gray_36": 0x5C5C5C,
        "gray_35": 0x595959,
        "gray_34": 0x575757,
        "gray_33": 0x545454,
        "gray_32": 0x525252,
        "gray_31": 0x4F4F4F,
        "gray_30": 0x4D4D4D,
        "gray_29": 0x4A4A4A,
        "gray_28": 0x474747,
        "gray_27": 0x454545,
        "gray_26": 0x424242,
        "gray_25": 0x404040,
        "gray_24": 0x3D3D3D,
        "gray_23": 0x3B3B3B,
        "gray_22": 0x383838,
        "gray_21": 0x363636,
        "gray_20": 0x333333,
        "gray_19": 0x303030,
        "gray_18": 0x2E2E2E,
        "gray_17": 0x2B2B2B,
        "gray_16": 0x292929,
        "gray_15": 0x262626,
        "gray_14": 0x242424,
        "gray_13": 0x212121,
        "gray_12": 0x1F1F1F,
        "gray_11": 0x1C1C1C,
        "gray_10": 0x1A1A1A,
        "gray_9": 0x171717,
        "gray_8": 0x141414,
        "gray_7": 0x121212,
        "gray_6": 0x0F0F0F,
        "gray_5": 0x0D0D0D,
        "gray_4": 0x0A0A0A,
        "gray_3": 0x080808,
        "gray_2": 0x050505,
        "gray_1": 0x030303
    }
