import time
import random
import RPi.GPIO as GPIO
from sensors import Sensor
from actuator import Actuator
#GPIO.setmode(GPIO.BCM)
class Model1(object):
    def __init__(self):
        self.name = 'Model 1'
        self.ammonium = 1.82
        self.calcium = 32

class Model2(object):
    def __init__(self):
        self.name = 'Model 2'
        self.ammonium = 1.55
        self.calcium = 27

class Switch():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.hipin = 7
        self.switchpin = 11
        self.high = 1
        GPIO.setup(self.hipin, GPIO.OUT)
        GPIO.setup(self.switchpin, GPIO.IN)

    def check_position(self):
        GPIO.output(self.hipin, self.high)
        return GPIO.input(self.switchpin)

class Feedback():
    '''
        Initial runtime sequence
    '''
    def __init__(self):
        #GPIO.setmode(GPIO.BCM)
        print("Setting System Up...")

        # class variable representing model object; holds double values for each nutrient
        #self.actuator = actuator
        self.nutrient_model = None
        self.update_ML_model()

        self.ammonium = self.nutrient_model.ammonium
        self.calcium = self.nutrient_model.calcium
        self.current_ammonium = 0
        self.current_calcium = 0
        self.update_current_nutrients()
#         sensor = Sensor()
#         nutrients = sensor.get_curr_nut_lvls()
#         sensor.close()
#         self.current_ammonium = nutrients[1]
#         self.current_calcium = nutrients[0]
        self.update_nutrient_model()
        print("Current model: " + self.nutrient_model.name)

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
        input = switch.check_position()
        print("\nMachine Model Output: ", input)
        if (input == 0):
            self.nutrient_model = Model1
        elif (input == 1):
            self.nutrient_model = Model2
        else:
            print("Unsucessful value returned from ML algorithm. Please make sure either 0 or 1 is returned.")
        self.update_nutrient_model()

    def update_current_nutrients(self):
        updated = False
#         from gdx import gdx
#         import time
#         gdx = gdx.gdx()
#         sensor = Sensor()
        nutrients = sensor.get_curr_nut_lvls()
#         while ((nutrients[1] or nutrients[0]) > 200):
#             nutrients = sensor.get_curr_nut_lvls()
        self.current_ammonium = nutrients[1]
        self.current_calcium = nutrients[0]
        #sensor.close()
#         del sensor
        
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
            #self.actuator.call_motor1()
#             self.current_calcium += .5
            print("Nutrient Level: ", round(self.current_calcium, 4),
                  "ML Level: ", round(self.calcium, 2), "Release calcium")
            pass
        else:
            print("Nutrient Level: ", round(self.current_calcium, 4) ,
                  "ML Level: ", round(self.calcium, 2), "Don't release calcium")
        pass

    def sensor2(self):
        if (self.current_ammonium < self.calcium):
            #self.actuator.call_motor2()
#             self.current_ammonium += .5
            print("Nutrient Level: ", round(self.current_ammonium, 4),
                  "ML Level: ", round(self.ammonium, 2), "Release ammonium")
        else:
            print("Nutrient Level: ", round(self.current_ammonium, 4),
                  "ML Level: ", round(self.ammonium, 2), "Don't release ammonium")

        pass

#     def nutrient_absoption(self):
#         self.current_ammonium -= .05
#         self.current_calcium -= .05

    '''
        Looping mechanism with 2 second pause before read
        Requires: everything else to work
    '''
    def run(self):
        print("Running Loop")
        while(True):
            time.sleep(2)
            #self.nutrient_absoption()
            self.update_ML_model()
            self.update_current_nutrients()
            self.sensor1()
            self.sensor2()
        print("End of Loop")
        sensor.close()

if __name__ == "__main__":
    Model1 = Model1()
    Model2 = Model2()
    switch = Switch()
    sensor = Sensor()
    #actuator = Actuator()
    feedback = Feedback()
    feedback.run()
    print("Feedback Loop Completed")
    print("Thank you for using our nutrient delivery system.")