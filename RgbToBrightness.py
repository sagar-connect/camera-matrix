import numpy

ascii_map_70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ascii_map_256 = [ascii_map_70[::-1][int(i // (256 / len(ascii_map_70)))] for i in range(256)]


class RgbToBrightness:
    def __init__(self):
        self.rgb_to_brightness_map = None

    @staticmethod
    def rgb_to_brightness(r, g, b):
        return ascii_map_256[int(r * 0.2126 + g * 0.7152 + b * 0.0722)]

    def map_init(self):
        print("RgbToBrightness map_init() started!")
        self.rgb_to_brightness_map = numpy.array([[[RgbToBrightness.rgb_to_brightness(r, g, b) for r in range(256)] for g in range(256)] for b in range(256)])
        print("RgbToBrightness map_init() done!")


RgbToBrightnessObj = RgbToBrightness()
RgbToBrightnessObj.map_init()
