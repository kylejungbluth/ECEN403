import time
import random
import RPi.GPIO as GPIO
from sensors import Sensor
from actuator import Actuator
class Model1(object):
    def __init__(self):
        self.name = 'Model 0'
        self.ammonium = 1.82
        self.calcium = 32

class Model2(object):
    def __init__(self):
        self.name = 'Model 1'
        self.ammonium = 1.55
        self.calcium = 27

class Switch():
    pin = 0
    def __init__(self, GPIO_pin):
        GPIO.setmode(GPIO.BOARD)
        #self.hipin = 7
        self.switchpin = GPIO_pin
        GPIO.setup(self.switchpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def check_position(self):
        return GPIO.input(self.switchpin)

class Feedback():
    '''
        Initial runtime sequence
    '''
    def __init__(self):
        print("Setting System Up...")

        # class variable representing model object; holds double values for each nutrient
        self.actuator = actuator
        self.nutrient_model = None
        self.update_ML_model()

        self.ammonium = self.nutrient_model.ammonium
        self.calcium = self.nutrient_model.calcium
        self.current_ammonium = 0
        self.current_calcium = 0
        self.update_current_nutrients()
        self.update_nutrient_model()
        print("Current model: " + self.nutrient_model.name)
        print("Successfully set up system.")
        print("-----------------------------------------\n")
    '''
        Update to nutrient quantity according to current model
        Requires: doubles from class object
    '''
    def update_nutrient_model(self):
        self.ammonium = self.nutrient_model.ammonium
        self.calcium = self.nutrient_model.calcium

    '''
        Update to Machine Learning algorithm
        Requires: input as binary 1 or 0 from sensor output
    '''
    def update_ML_model(self):
        input = switch1.check_position()
        if (input == 0):
            self.nutrient_model = Model1
        elif (input == 1):
            self.nutrient_model = Model2
        else:
            print("Unsucessful value returned from ML algorithm. Please make sure either 0 or 1 is returned.")
        print("\nMachine Model Output: ", self.nutrient_model.name)
        self.update_nutrient_model()

    def update_current_nutrients(self):
        updated = False
        nutrients = sensor.get_curr_nut_lvls()
        self.current_ammonium = nutrients[1]
        self.current_calcium = nutrients[0]
        
    '''
        Get current nutrient levels as doubles
        Requires: N/A
    '''
    def get_ammonium(self):
        return self.current_ammonium

    def get_calcium(self):
        return self.current_calcium

    '''
        Run sensor level checks and release sequences
        Requires: Sensor output WIP
    '''

    def sensor1(self):
        if (self.current_calcium < self.calcium):
            self.actuator.call_motor1()
            print("Nutrient Level: ", round(self.current_calcium, 4),
                  "ML Level: ", round(self.calcium, 2), "Release calcium")
            pass
        else:
            print("Nutrient Level: ", round(self.current_calcium, 4) ,
                  "ML Level: ", round(self.calcium, 2), "Don't release calcium")
        pass

    def sensor2(self):
        if (self.current_ammonium < self.calcium):
            self.actuator.call_motor2()
            print("Nutrient Level: ", round(self.current_ammonium, 4),
                  "ML Level: ", round(self.ammonium, 2), "Release ammonium")
        else:
            print("Nutrient Level: ", round(self.current_ammonium, 4),
                  "ML Level: ", round(self.ammonium, 2), "Don't release ammonium")

        pass

    '''
        Looping mechanism with 2 second pause before read
        Requires: everything else to work
    '''
    def run(self):
        print("Running Loop")
        while(True):
            on_off = switch3.check_position()
            if (on_off == 1):
                print("Closing Loop")
                sensor.close()
                break
            pause = switch2.check_position() #check for loop pause
            if (pause == 0):
                time.sleep(2)
                self.update_ML_model()
                self.update_current_nutrients()
                self.sensor1()
                self.sensor2()
            else:
                time.sleep(0.5)
                print("Loop Paused")
                #while (switch2.check_position() == 0):
                    #do nothing
                
        print("End of Loop")

if __name__ == "__main__":
    time.sleep(10)
    Model1 = Model1()
    Model2 = Model2()
    switch1 = Switch(GPIO_pin=7) #switch used to control model
    switch2 = Switch(GPIO_pin=12) #switch used to pause the loop
    switch3 = Switch(GPIO_pin=16) #switch used to close the run
    sensor = Sensor()
    actuator = Actuator(out1=18, out2=29,
                        in1= 32, in2= 31)
    feedback = Feedback()
    feedback.run()
    print("Feedback Loop Completed")
    print("Thank you for using our nutrient delivery system. Don't forget to turn on Switch 3 before restarting!")