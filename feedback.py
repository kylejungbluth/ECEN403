import time
import random
from enum import Enum

class Model(Enum):
    low = 0
    high = 1

class Model1(object):
    def __init__(self):
        self.ammonium = .75
        self.magnesium = .5
        self.calcium = .5
        self.phosphorus = .9

class Model2(object):
    def __init__(self):
        self.ammonium = 1.5
        self.magnesium = 1.1
        self.calcium = 1.1
        self.phosphorus = 1.8

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
        self.magnesium = self.nutrient_model.magnesium
        self.calcium = self.nutrient_model.calcium
        self.phosphorous = self.nutrient_model.phosphorus
        self.update_model()
        print("Current model: " + self.model.name)

    '''
        Update to nutrient quantity according to current model
        Requires: doubles from class object
    '''
    def update_model(self):
        self.ammonium = self.nutrient_model.ammonium
        self.magnesium = self.nutrient_model.magnesium
        self.calcium = self.nutrient_model.calcium
        self.phosphorous = self.nutrient_model.phosphorus

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
        return 1

    def get_magnesium(self):
        return 1

    def get_calcium(self):
        return 1

    def get_phosphorus(self):
        return 1

    '''
        Run sensor level checks and release sequences
        Requires: Sensor output WIP
    '''
    def sensor1(self):
        nutrient = self.get_ammonium()
        if (nutrient < self.ammonium):
            #actuator1.release()
            print("Nutrient Level: ", nutrient, "ML Level: ", self.ammonium, "Release ammonium")
            pass
        else:
            print("Nutrient Level: ", nutrient, "ML Level: ", self.ammonium, "Don't release ammonium")
        pass

    def sensor2(self):
        nutrient = self.get_magnesium()
        if (nutrient < self.magnesium):
            # actuator2.release()
            print("Nutrient Level: ", nutrient, "ML Level: ", self.magnesium, "Release magnesium")
        else:
            print("Nutrient Level: ", nutrient, "ML Level: ", self.ammonium, "Don't release magnesium")

        pass
    def sensor3(self):
        nutrient = self.get_calcium()
        if (nutrient < self.calcium):
            # actuator3.release()
            pass
        pass
    def sensor4(self):
        nutrient = self.get_phosphorus()
        if (nutrient < self.phosphorous):
            # actuator4.release()
            pass
        pass

    '''
        Looping mechanism with 2 second pause before read
        Requires: everything else to work
    '''
    def run(self):
        print("Running Loop")
        while(True):
            time.sleep(2)
            rand = random.randint(0, 1)
            print("Machine Model Output: ", rand)
            self.updateML(rand)

            self.sensor1()
            self.sensor2()
            #self.sensor3()
            #self.sensor4()


if __name__ == "__main__":
    Model1 = Model1()
    Model2 = Model2()
    feedback = Feedback()
    feedback.run()
    print("Feedback Loop Completed")
    print("Thank you for using our nutrient delivery system.")

