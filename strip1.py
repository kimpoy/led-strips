import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 70        # Number of LED pixels (14 segments * 5 LEDs per segment).
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Segment to LED mapping
segments = {
    'a': range(5, 10),
    'b': range(10, 15),
    'c': range(15, 20),
    'd': range(20, 25),
    'e': range(25, 30),
    'f': range(0, 5),
    'g': range(30, 35),
    'h': range(35, 40),
    'i': range(40, 45),
    'j': range(45, 50),
    'k': range(50, 55),
    'l': range(55, 60),
    'm': range(60, 65),
    'n': range(65, 70),
}

# 7-segment digit to segment mapping
digit_segments = {
    0: ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k','l', 'm'],
    1: ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'k'],
    2: ['a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'n', 'm', 'l'],
    3: ['a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'n', 'k', 'l'],
    4: ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'n', 'j', 'k'],
    5: ['a', 'b', 'c', 'd', 'e', 'f', 'i', 'h', 'n', 'k', 'l'],
    6: ['a', 'b', 'c', 'd', 'e', 'f', 'i', 'h', 'n', 'k', 'l', 'm'],
    7: ['a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'k'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k','l', 'm', 'n'],
    9: ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'n'],
    10: ['e', 'f', 'h', 'i', 'j', 'k','l', 'm'], # New pattern for 10
    11: ['b', 'c', 'j', 'k'], # New pattern for 11
    12: ['e', 'f', 'i', 'j', 'n', 'm', 'l'],      # New pattern for 12
    13: ['e', 'f', 'i', 'j', 'n', 'k', 'l'],      # New pattern for 13
    14: ['e', 'f', 'h', 'n', 'j', 'k'], # New pattern for 14
    15: ['e', 'f', 'i', 'h', 'n', 'k', 'l'],      # New pattern for 15
    16: ['e', 'f', 'i', 'h', 'n', 'k', 'l', 'm']  # New pattern for 16
}

def clear_strip(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

def light_segments(strip, segments_to_light):
    for segment in segments_to_light:
        for led in segments[segment]:
            strip.setPixelColor(led, Color(255, 0, 0)) # Red
    strip.show()

def display_digit(strip, digit):
    clear_strip(strip)
    segments_to_light = digit_segments[digit]
    light_segments(strip, segments_to_light)

# Main program logic follows:
if __name__ == '__main__':
    try:
        while True:
            number = int(input("Enter a number (0-16): "))
            if 0 <= number <= 16:
                display_digit(strip, number)
            else:
                print("Please enter a valid digit (0-16).")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        clear_strip(strip)
