import pyfirmata2
import time

board = pyfirmata2.Arduino("COM5")
ledPin = board.get_pin('d:11:o')

while True:
    ledPin.write(1)
    time.sleep(0.2)
    ledPin.write(0)
    time.sleep(0.2)