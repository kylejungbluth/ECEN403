import RPi.GPIO as GPIO
import time
import math

# using physical board pin numbers
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)


GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while(True): 
	if(GPIO.input(38) == 1):
		print("Button 1 pressed")
		print(" ")
		time.sleep(1)
	if(GPIO.input(40) == 1):
		print("Button 2 pressed")
		print(" ")
		time.sleep(1)

GPIO.cleanup()
