import time
import random
from gdx import gdxcc
from enum import Enum

class Model(Enum):
    low = 0
    high = 1

class Model1(object):
    def __init__(self):
        self.ammonium = .75
        self.calcium = .5

class Model2(object):
    def __init__(self):
        self.ammonium = 1.5
        self.calcium = 1.1

class Feedback():
    '''
        Initial runtime sequence
    '''
    def __init__(self):
        print("Setting System Up...")
        # class variable representing model object; holds double values for each nutrient
        self.model = Model.low
        self.nutrient_model = Model1

        self.ammonium = self.nutrient_model.ammonium
        self.calcium = self.nutrient_model.calcium

        self.current_ammonium = 0
        self.current_calcium = 0

        self.update_model()
        print("Current model: " + self.model.name)

    '''
        Update to nutrient quantity according to current model
        Requires: doubles from class object
    '''
    def update_model(self):
        self.ammonium = self.nutrient_model.ammonium
        self.calcium = self.nutrient_model.calcium

    '''
        Update to Machine Learning algorithm
        Requires: input as binary 1 or 0 from sensor output
    '''
    def updateML(self, input):
        ML_input = input
        if (ML_input == 0):
            self.model = Model.low
            self.nutrient_model = Model1
        elif (ML_input == 1):
            self.model = Model.high
            self.nutrient_model = Model2
        else:
            print("Unsucessful value returned from ML algorithm. Please make sure either 0 or 1 is returned.")
        self.update_model()


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

    def sensordata(self):
        gdxcc.open_usb()
        gdxcc.select_sensors([[3], [4]])
        gdxcc.start(period=1000)

        while (1):

            sumnum = [0, 0]
            for i in range(0, 10):

                measurements = gdxcc.read()
                if measurements == None:
                    break
                print(measurements)
                sumnum[0] += measurements[0]
                sumnum[1] += measurements[1]
            print("ammonium: " + str(sumnum[0] / 10))
            print("calcium: " + str(sumnum[1] / 10))
            ammoniumavg = sumnum[0] / 10
            calciumavg = sumnum[1] / 10

            return ammoniumavg, calciumavg

            ##measurements.clear()
        gdx.stop()
        gdx.close()
    def sensor1(self):
        if (self.current_ammonium < self.ammonium):
            #actuator1.release()
            self.current_ammonium += .5
            print("Nutrient Level: ", round(self.current_ammonium, 2), "ML Level: ", round(self.ammonium, 2), "Release ammonium")
            pass
        else:
            print("Nutrient Level: ", round(self.current_ammonium, 2) , "ML Level: ", round(self.ammonium, 2), "Don't release ammonium")
        pass

    def sensor2(self):
        if (self.current_calcium < self.calcium):
            # actuator2.release()
            self.current_calcium += .5
            print("Nutrient Level: ", round(self.current_calcium, 2),
                  "ML Level: ", round(self.calcium, 2), "Release magnesium")
        else:
            print("Nutrient Level: ", round(self.current_calcium, 2),
                  "ML Level: ", round(self.ammonium, 2), "Don't release magnesium")

        pass

    def nutrient_absoption(self):
        self.current_ammonium -= .05
        self.current_calcium -= .05

    '''
        Looping mechanism with 2 second pause before read
        Requires: everything else to work
    '''
    def run(self):
        print("Running Loop")
        while(True):
            time.sleep(2)
            self.nutrient_absoption()
            rand = random.randint(0, 1)
            print("Machine Model Output: ", rand)
            self.updateML(rand)

            self.sensor1()
            self.sensor2()


if __name__ == "__main__":
    Model1 = Model1()
    Model2 = Model2()
    feedback = Feedback()
    feedback.run()
    print("Feedback Loop Completed")
    print("Thank you for using our nutrient delivery system.")

