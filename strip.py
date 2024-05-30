import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 35        # Number of LED pixels (7 segments * 5 LEDs per segment).
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
    'g': range(30, 35)
}

# 7-segment digit to segment mapping
digit_segments = {
    0: ['a', 'b', 'c', 'd', 'e', 'f'],
    1: ['b', 'c'],
    2: ['a', 'b', 'd', 'e', 'g'],
    3: ['a', 'b', 'c', 'd', 'g'],
    4: ['b', 'c', 'f', 'g'],
    5: ['a', 'c', 'd', 'f', 'g'],
    6: ['a', 'c', 'd', 'e', 'f', 'g'],
    7: ['a', 'b', 'c'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
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
            number = int(input("Enter a number (0-9): "))
            if 0 <= number <= 9:
                display_digit(strip, number)
            else:
                print("Please enter a valid digit (0-9).")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        clear_strip(strip)
