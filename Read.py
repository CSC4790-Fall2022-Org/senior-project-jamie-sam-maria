import sys
from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

reader = SimpleMFRC522()

try:
        print("Hold your tag near the reader...")
        id, text = reader.read()
        print("ID: %s\nTest: %s" % (id, text))
        sleep(5)
        
except KeyboardInterrupt:
        GPIO.cleanup()
        print("Exiting program.")