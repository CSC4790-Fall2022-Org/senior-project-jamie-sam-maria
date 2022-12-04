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
        display.lcd_display_string("Enter DUO username:", 1)  # Write line of text to first line of display
        text = input('Enter your DUO username:')
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(buzzer,GPIO.LOW)
        sleep(0.1)
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(buzzer,GPIO.LOW)
        display.lcd_clear()
        display.lcd_display_string("Now scan the", 1)  # Write line of text to first line of display
        display.lcd_display_string("card to write:", 2)  # Write line of text to first line of display
        print("Now place your card/tag to write...")
        reader.write(text)
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(buzzer,GPIO.LOW)
        print("Info has been written")
        display.lcd_clear();
        display.lcd_display_string("Info has been", 1)  # Write line of text to first line of display
        display.lcd_display_string("written to card!:", 2)  # Write line of text to first line of display
        sleep(3);
        display.lcd_clear();

finally:
        GPIO.cleanup() 

