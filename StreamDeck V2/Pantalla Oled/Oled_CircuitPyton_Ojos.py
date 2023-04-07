# This proyect you can find in the next link
#https://magicalapes.com/blog/oled-display-ssd1306-circuitpython/

import time
import board
import busio # to communicate over I2C

# Helper print to see whats available on the connected board
print(dir(board))

# Import the SSD1306 module, see the lib downloads on this page
import adafruit_ssd1306

# Create the I2C interface for OLED, use any pins you like, we are going with GP0 (SDA) & GP1 (SCL)
# busio.I2C(SCL, SDA)
i2c = busio.I2C(board.GP17, board.GP16)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Eyes graphic type
EYES_NORMAL = 0
EYES_AFRAID = 1
EYES_SPINNING = 2
EYES_BLINK = 3

def eyes(type):
    display.fill(0) # clear
    if type == EYES_NORMAL:
        display.circle(47, 30, 10, 1)
        display.circle(82, 30, 10, 1)
    elif type == EYES_AFRAID:
        display.circle(47, 64, 10, 1)
        display.circle(82, 64, 10, 1)
    elif type == EYES_SPINNING:
        display.circle(47, 30, 4, 1)
        display.circle(47, 30, 7, 1)
        display.circle(47, 30, 10, 1)
        display.circle(47, 30, 13, 1)
        display.circle(82, 30, 4, 1)
        display.circle(82, 30, 7, 1)
        display.circle(82, 30, 10, 1)
        display.circle(82, 30, 13, 1)
    elif type == EYES_BLINK:
        display.circle(82, 30, 10, 1)
    display.show() # show
    
while True:
    eyes(EYES_NORMAL)
    time.sleep(1)
    eyes(EYES_BLINK)
    time.sleep(0.1)
    eyes(EYES_NORMAL)
    time.sleep(1)
    eyes(EYES_AFRAID)
    time.sleep(1)
    eyes(EYES_NORMAL)
    time.sleep(1)
    eyes(EYES_SPINNING)
    time.sleep(1)