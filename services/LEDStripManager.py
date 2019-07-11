import board
import neopixel


class LEDStripManager(object):

    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18)
        self.num_pixels = 60
        self.gpio = 18
        self.red = 0
        self.green = 0
        self.blue = 0
        self.effect = "Fill"

    def apply_color(self, red, green, blue):
        """
        :type red: int (0-255
        :type green int (0-255)
        :type blue int (0-255)
        """
        if not LEDStripManager.validate_rgb(red, green, blue):
            raise ValueError
        self.red = red
        self.green = green
        self.blue = blue

    def apply_effect(self, effect_name):
        self.effect = effect_name

    def apply_config(self):
        pass

    def run(self):
        if self.effect == "Fill":
            self.pixels.fill((self.red, self.green, self.blue))
        else:
            for i in range(self.num_pixels):
                self.pixels[i] = (self.red, self.green, self.blue)

    @staticmethod
    def validate_rgb(red, green, blue):
        if red > 255 or red < 0:
            return False
        if green > 255 or green < 0:
            return False
        if blue > 255 or blue < 0:
            return False
        return True
