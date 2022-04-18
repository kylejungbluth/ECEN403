import RPi.GPIO as GPIO
import time

class Actuator():
    '''
        Initial runtime sequence
    '''
    def __init__(self, out1, out2, in1, in2):
        # using physical board pin numbers
        self.output1 = out1
        self.output2 = out2
        self.input1 = in1
        self.input2 = in2
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # set pin 16 (GPIO23) as output
        GPIO.setup(self.output1, GPIO.OUT)
        # set pin 18 (GPIO24) as output
        GPIO.setup(self.output2, GPIO.OUT)

        # set pin 38 (GPIO20) as input, pull down
        GPIO.setup(self.input1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # set pin 40 (GPIO21) as input, pull down
        GPIO.setup(self.input2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # function to call on motor 1 and dispense nutrient 1
    def call_motor1(self):
        print("Activitating motor 1...\n")
        GPIO.output(self.output1, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.output1, GPIO.LOW)
        signalrec = False
        while (signalrec == False):
            print("Loading...\n")
            time.sleep(1)
            if (GPIO.input(self.input1) == 1):
                print("Motor 1 has finished 1 cycle.")
                print("-----------------------------")
                time.sleep(2)
                break

    # function to call on motor 2 and dispense nutrient 2
    def call_motor2(self):
        print("Activitating motor 2...\n")
        GPIO.output(self.output2, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.output2, GPIO.LOW)
        signalrec = False
        while (signalrec == False):
            print("Loading...\n")
            time.sleep(1)
            if (GPIO.input(self.input2) == 1):
                print("Motor 2 has finished 1 cycle.")
                print("-----------------------------")
                time.sleep(2)
                break

    def cleanup(self):
        # clean up GPIO pins for next run
        GPIO.cleanup()
