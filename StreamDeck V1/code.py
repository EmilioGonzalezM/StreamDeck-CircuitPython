import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

boton1_pin= board.GP15
boton2_pin= board.GP14
boton3_pin= board.GP16
boton4_pin= board.GP17
boton5_pin= board.GP18

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


while True:
    if boton1.value:
        print("Botón 1 Guardar")
        teclado.press(Keycode.F13)
        time.sleep(0.2)
        teclado.release(Keycode.F13)
    if boton2.value:
        print("Botón 2 Exportar un fotograma")
        teclado.press(Keycode.F14)
        time.sleep(0.2)
        teclado.release(Keycode.F14)
    if boton3.value:
        print("Botón 3 Exportar Medios")
        teclado.press(Keycode.F15)
        time.sleep(0.2)
        teclado.release(Keycode.F15)
    if boton4.value:
        print("Botón 4 Deshacer")
        teclado.press(Keycode.F16)
        time.sleep(0.2)
        teclado.release(Keycode.F16)
        
    if boton5.value:
        print("Botón 5 Guardar como")
        teclado.press(Keycode.F17)
        time.sleep(0.2)
        teclado.release(Keycode.F17)
        time.sleep(0.2)
        