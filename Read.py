#!/usr/bin/env python
import json
import os
import duo_client
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
from time import sleep
import drivers

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

rfid_reader = SimpleMFRC522()
	
def duo_auth(user):
	# Setting variables to the ikey, skey, and API hostname
	# we created on DUO for our "classroom"
	ikey = "DIZQ2N9NC70FL26YA1LA"
	skey = "XJSTcuSrbjgKMvOnZOEOpdse8H60BwM8QfR8LkiJ"
	host = "api-498521aa.duosecurity.com"
	
	# Testing by printing 
	#print(ikey)
	#print(skey)
	#print(host)
	
	# Declaring the API using the key set above
	auth_api = duo_client.Auth(ikey, skey, host)
	
	# Retrieve timestamp of the API ping/call: 
	ping_result = auth_api.ping()
	print('Ping Result: ' + json.dumps(ping_result)) 

	# Retrieve user info from API:
	preauth_result = auth_api.preauth(username=user)
	print('Pre-Authentication Results: ' + json.dumps(preauth_result))
	print('Please verify the DUO push notification on your mobile device...')
	display.lcd_display_string("Please verify", 1);
	display.lcd_display_string("the notification", 2);

	# Retrieve user info from API:
	if preauth_result['result']=='auth':
		auth_result = auth_api.auth(username=user,factor='push',device='auto')
	
	# Code goes here for creating a new account w/ a blank card #

	print('Authentication Results :'+ json.dumps(auth_result))
	
	if auth_result['status']:
		status= auth_result['status']
	else:
		status= "error"
	return status

if __name__ == '__main__':
	try:
		while True:
			GPIO.output(buzzer,GPIO.HIGH)
			sleep(0.1)
			GPIO.output(buzzer,GPIO.LOW)
			sleep(0.1)
			GPIO.output(buzzer,GPIO.HIGH)
			sleep(0.1)
			GPIO.output(buzzer,GPIO.LOW)
			print("Hold your tag/card near the reader...")
			display.lcd_display_string("Hold your tag", 1);
			display.lcd_display_string("near the reader:", 2);
			id, user = rfid_reader.read()
			GPIO.output(buzzer,GPIO.HIGH)
			sleep(0.5)
			GPIO.output(buzzer,GPIO.LOW)
			print(id)
			print(user)
			status = duo_auth(user)
			if status == "allow":
				print('Login Authorized!')
			elif status=="deny":
				print('Log-in Denied!')
	finally:
		GPIO.cleanup()
