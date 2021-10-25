from gpiozero import Servo
from time import sleep
import random

from gpiozero.pins.pigpio import PiGPIOFactory

#run sudo pigpiod

factory = PiGPIOFactory()

servo1 = Servo(5, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo2 = Servo(6, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

def servoMotion():
	servo1.min()
	sleep(2)
	servo1.mid()
	sleep(0.5)
	servo2.min()
	sleep(2)
	servo2.mid()
	sleep(0.5)

print("Test Nutrient Monitoring and Regulation System")

print("Setting everything up...")
servo1.mid()
servo2.mid()

requiredNutrient = input("Enter the amount of nutrient required for today: ")
requiredNutrient = int(requiredNutrient)
currentNutrient = random.randint(1, requiredNutrient)
print("")
print("Required Nutrient level for today: ", requiredNutrient)
print("Current Nutrient level: ", currentNutrient)
print("")
temp = int(currentNutrient)

while temp < requiredNutrient: 
	print("Dispensing 5 grams of nutrients...")
	servoMotion()
	temp += 5
	print("Current reading: ", temp , " grams")
	print("")
	if temp > requiredNutrient:
		break
	else: 
		continue
		
print("")		
print("Final reading: " , temp , " grams")
print("Today's quota met...")

servo1.mid()
servo2.mid()	
servo1.value = None;
servo2.value = None;
