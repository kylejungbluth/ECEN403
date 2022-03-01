import RPi.GPIO as GPIO
import time

class Actuator():
    '''
        Initial runtime sequence
    '''
    def __init__(self):
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

    # function to call on motor 1 and dispense nutrient 1
    def call_motor1(self):
        print("Activitating motor 1...\n")
        GPIO.output(16, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(16, GPIO.LOW)
        signalrec = False
        while (signalrec == False):
            print("Loading...\n")
            time.sleep(1)
            if (GPIO.input(38) == 1):
                print("Motor 1 has finished 1 cycle.")
                print("-----------------------------")
                time.sleep(0.5)
                break

    # function to call on motor 2 and dispense nutrient 2
    def call_motor2(self):
        print("Activitating motor 2...\n")
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        signalrec = False
        while (signalrec == False):
            print("Loading...\n")
            time.sleep(1)
            if (GPIO.input(40) == 1):
                print("Motor 2 has finished 1 cycle.")
                print("-----------------------------")
                time.sleep(0.5)
                break

    def cleanup(self):
        # clean up GPIO pins for next run
        GPIO.cleanup()
