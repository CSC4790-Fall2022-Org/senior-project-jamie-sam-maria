import sys
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

reader = SimpleMFRC522()
try:
        text = input('New Data:')
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(buzzer,GPIO.LOW)
        sleep(0.1)
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(buzzer,GPIO.LOW)
        print("Now place your tag to write...")
        reader.write(text)
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(buzzer,GPIO.LOW)
        print("Written")
finally:
        GPIO.cleanup() 

