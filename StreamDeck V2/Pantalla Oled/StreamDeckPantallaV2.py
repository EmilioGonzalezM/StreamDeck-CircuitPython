#Made by Mylo[Rec.]
import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

import adafruit_ssd1306
import busio

#Pantalla
SCL=board.GP17
SDA=board.GP16

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)                       # \
display.text("Stream Deck",32,32,1)   # | --> Pantalla
display.show()                        # /

#LED
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

#Botones
boton1_pin= board.GP18
boton2_pin= board.GP19
boton3_pin= board.GP20
boton4_pin= board.GP21
boton5_pin= board.GP15
boton6_pin= board.GP14
boton7_pin= board.GP13
boton8_pin= board.GP12

teclado = Keyboard(usb_hid.devices)

boton1 = digitalio.DigitalInOut(boton1_pin)
boton1.direction = digitalio.Direction.INPUT
boton1.pull = digitalio.Pull.DOWN

boton2 = digitalio.DigitalInOut(boton2_pin)
boton2.direction = digitalio.Direction.INPUT
boton2.pull = digitalio.Pull.DOWN

boton3 = digitalio.DigitalInOut(boton3_pin)
boton3.direction = digitalio.Direction.INPUT
boton3.pull = digitalio.Pull.DOWN

boton4 = digitalio.DigitalInOut(boton4_pin)
boton4.direction = digitalio.Direction.INPUT
boton4.pull = digitalio.Pull.DOWN

boton5 = digitalio.DigitalInOut(boton5_pin)
boton5.direction = digitalio.Direction.INPUT
boton5.pull = digitalio.Pull.DOWN

boton6 = digitalio.DigitalInOut(boton6_pin)
boton6.direction = digitalio.Direction.INPUT
boton6.pull = digitalio.Pull.DOWN

boton7 = digitalio.DigitalInOut(boton7_pin)
boton7.direction = digitalio.Direction.INPUT
boton7.pull = digitalio.Pull.DOWN

boton8 = digitalio.DigitalInOut(boton8_pin)
boton8.direction = digitalio.Direction.INPUT
boton8.pull = digitalio.Pull.DOWN

while True:
#     led.value = True     # \
#     time.sleep(0.1)      # |-----> Blink LED
#     led.value = False    # |   Mientras más tiempo se coloca el sleep más tarda en responder porque se pausa
#     time.sleep(0.1)      # /     la misma cantidad de tiempo. Mientras mas rapodo, mejor responde.
     
    if boton1.value:
        print("Botón 1")
        teclado.press(Keycode.F13)
        time.sleep(0.2)
        teclado.release(Keycode.F13)
        display.fill(0)
        display.text("Boton 1",46,32,1)
        display.show()
        
    if boton2.value:
        print("Botón 2")
        teclado.press(Keycode.F14)
        time.sleep(0.2)
        teclado.release(Keycode.F14)
        display.fill(0)
        display.text("Boton 2",46,32,1)
        display.show()
        
    if boton3.value:
        print("Botón 3")
        teclado.press(Keycode.F15)
        time.sleep(0.2)
        teclado.release(Keycode.F15)
        display.fill(0)
        display.text("Boton 3",46,32,1)
        display.show()
        
    if boton4.value:
        print("Botón 4")
        teclado.press(Keycode.F16)
        time.sleep(0.2)
        teclado.release(Keycode.F16)
        display.fill(0)
        display.text("Boton 4",46,32,1)
        display.show()
        
    if boton5.value:
        print("Botón 5")
        teclado.press(Keycode.F17)
        time.sleep(0.2)
        teclado.release(Keycode.F17)
        time.sleep(0.2)
        display.fill(0)
        display.text("Boton 5",46,32,1)
        display.show()

    if boton6.value:
        print("Botón 6")
        teclado.press(Keycode.F18)
        time.sleep(0.2)
        teclado.release(Keycode.F18)
        time.sleep(0.2)
        display.fill(0)
        display.text("Boton 6",46,32,1)
        display.show()
        
    if boton7.value:
        print("Botón 7")
        teclado.press(Keycode.F19)
        time.sleep(0.2)
        teclado.release(Keycode.F19)
        time.sleep(0.2)
        display.fill(0)
        display.text("Boton 7",46,32,1)
        display.show()
        
    if boton8.value:
        print("Botón 8")
        teclado.press(Keycode.F20)
        time.sleep(0.2)
        teclado.release(Keycode.F20)
        time.sleep(0.2)
        display.fill(0)
        display.text("Boton 8",46,32,1)
        display.show()
    pass
        