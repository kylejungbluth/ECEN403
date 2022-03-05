from gdx import gdx
import time

class Sensor():
    '''
            Initial runtime sequence
    '''
    def __init__(self):
        gdx = gdx.gdx()
        # This code uses the gdx functions to collect data from your Go Direct sensors.
        gdx.open_usb()
        self.first = 0 #calcium is 0 and ammonium is 1

    def select_sensors(self):
        '''
        Calcium is always read as sensor 4 and ammonium is sensor 3
        If first is 0, then output is [calcium, ammonium]
        If first is 1, then output is [ammonium, calcium]
        '''
        # calcium read first
        if str(gdx.devices[0]) == "GDX-ISEA 0W1010W8 USB ":
            print("GDX-ISEA 0W1010W8 USB selected")
            gdx.select_sensors([[4], [3]])
            self.first = 0

        # ammonium read first
        elif str(gdx.devices[0]) == "GDX-ISEA 0W1010K0 USB ":
            print("GDX-ISEA 0W1010K0 USB selected")
            gdx.select_sensors([[3], [4]])
            self.first = 1

        gdx.start(1000)

    def run(self):
        measurements_cal = []
        measurements_amm = []
        for i in range(0, 5):
            measurement = gdx.read()
            if measurement == None:
                break
            measurement = self.output(measurement)
            measurements_cal.append(measurement[0])
            measurements_amm.append(measurement[1])

        self.close()

        #average it
        avg_cal = sum(measurements_cal)/len(measurements_cal)
        avg_amm = sum(measurements_amm)/len(measurements_amm)
        return [avg_cal, avg_amm]

    def output(self, measurements):
        '''
        Return measurements in standard form of [calcium, ammonium]
        '''
        if (self.first == 0):
            measurements = [measurements[0], measurements[1]]
        else:
            measurements = [measurements[1], measurements[0]]
        return measurements

    def close(self):
        gdx.stop()
        gdx.close()



