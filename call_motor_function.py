import RPi.GPIO as GPIO
import time

# using physical board pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# set pin 16 (GPIO23) as output
GPIO.setup(16, GPIO.OUT)
# set pin 18 (GPIO24) as output
GPIO.setup(18, GPIO.OUT)

# set pin 38 (GPIO20) as input, pull down 
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# set pin 40 (GPIO21) as input, pull down
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

calcium_ppm = 0
ammonium_ppm = 0

model = int(input("Enter 1 or 0 for ML output: "))
print(" ")

if(model == 0):
	calcium_ppm = 32
	ammonium_ppm = 1.82
	print("ML model 0")
else:
	calcium_ppm = 27
	ammonium_ppm = 1.55
	print("ML model 1")
	
print("Calcium ppm requirement: " + str(calcium_ppm))
print("Ammonium ppm requirement: " + str(ammonium_ppm) + "\n")
	
volume_liter = 10000
calcium_gram = (calcium_ppm/1000) * volume_liter
ammonium_gram = (ammonium_ppm/1000) * volume_liter
print("Calcium gram requirement: " + str(calcium_gram)) 
print("Ammonium gram requirement: " + str(ammonium_gram) + "\n")

# test function to see if input and output works correctly
def test_int():
	while(True):
		motor = int(input("Enter 1 or 2 to activate specific motor: "))
		if(motor == 1):
			print(" ")
			print("Activating motor 1...\n")
			GPIO.output(16, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(16, GPIO.LOW)
			dispense = False
			while(dispense == False): 
				print("Loading...\n")
				time.sleep(1)
				if(GPIO.input(38) == 1):
					print("Motor 1 has finished 1 cycle\n")
					time.sleep(1)
					break

# function to call on motor 1 and dispense nutrient 1
def call_motor1():
	print("Activitating motor 1...\n")
	GPIO.output(16, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(16, GPIO.LOW)
	signalrec = False	
	while(signalrec == False):
		print("Loading...\n")
		time.sleep(1)
		if(GPIO.input(38) == 1):
			print("Motor 1 has finished 1 cycle.")
			print("-----------------------------")
			time.sleep(0.5)
			break		

# function to call on motor 2 and dispense nutrient 2			
def call_motor2():
	print("Activitating motor 2...\n")
	GPIO.output(18, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(18, GPIO.LOW)
	signalrec = False	
	while(signalrec == False):
		print("Loading...\n")
		time.sleep(1)
		if(GPIO.input(40) == 1):
			print("Motor 2 has finished 1 cycle.")
			print("-----------------------------")
			time.sleep(0.5)
			break		

# infinite loop to continuously ask user to activate specific motor 
while(True):
	motor = int(input("Enter 1 or 2 to activate specific motor: "))
	print(" ")
	if(motor == 1):
		call_motor1()
	if(motor == 2):
		call_motor2()

# uncomment to test 			
#if(confirm == 1):
#	#call_motor1()
#	test_int()

# clean up GPIO pins for next run
GPIO.cleanup()
