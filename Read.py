import sys
import drivers
from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

#Disable warnings (optional)
GPIO.setwarnings(False)

#Select GPIO mode
GPIO.setmode(GPIO.BCM)

#Set buzzer GPIO Pin 4 as output
buzzer = 4
GPIO.setup(buzzer,GPIO.OUT)

#Set up LCD screen for display use
display = drivers.Lcd()
display.lcd_clear()

reader = SimpleMFRC522()
try:
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(buzzer,GPIO.LOW)
        sleep(0.1)
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(buzzer,GPIO.LOW)
        display.lcd_clear()
        print("Hold your tag near the reader...")
        id, text = reader.read()
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(buzzer,GPIO.LOW)
        print("ID: %s\nUsername: %s" % (id, text))
        sleep(5)
        
except KeyboardInterrupt:
        GPIO.cleanup()
        print("Exiting program.")
