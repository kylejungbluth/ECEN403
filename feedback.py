import time
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
        self.magnesium = 1
        self.calcium = 1
        self.phosphorus = 1.8

class Feedback():

    model = Model.low

    def __init__(self):

        pass

    def updateML(self, input):
        ML_input = input
        if (ML_input == 0):
            Feedback.model = Model.low
        else:
            Feedback.model = Model.high
        pass

    def sensor1(self):
        pass
    def sensor2(self):
        pass
    def sensor3(self):
        pass
    def sensor4(self):
        pass

    def run(self):

        while(True):
            #updateML()
            pass


        pass





if __name__ == "__main__":
    feedback = Feedback()
    feedback.run()
    print("Feedback Loop Completed")

