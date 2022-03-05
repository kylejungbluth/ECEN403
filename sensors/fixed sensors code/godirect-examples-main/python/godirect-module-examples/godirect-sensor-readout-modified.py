# -*- coding: utf-8 -*-

""" This example automatically finds the nearest GoDirect device
and starts reading measurements from the default sensor at
the typical data rate. Unlike the other examples that use the gdx module,
this example works directly with the godirect module. Take a look at 
the gdx getting started examples and the gdx.py file for more information.

Installation of the Python module:
# pip3 install godirect
"""

from godirect import GoDirect

import logging
import time
logging.basicConfig()
#logging.getLogger('godirect').setLevel(logging.DEBUG)
#logging.getLogger('bleak').setLevel(logging.DEBUG)
#logging.getLogger('pygatt').setLevel(logging.DEBUG)

# The first USB device found will be used. If no USB devices are found, then 
# the BLE device with the strongest signal over -100dB is used.
# Note that you can choose to enable USB, BLE, or both. By default both will be enabled.
godirect = GoDirect(use_ble=False,use_usb=True)
print("GoDirect v"+str(godirect.get_version()))
print("\nSearching...", flush=True, end ="")
device = godirect.get_device(threshold=-100)

# Once a device is found or selected it must be opened. By default, only information will be 
# gathered on Open. To automatically enable the default sensors and start measurements send 
# auto_start=True and skip to get enabled sensors.

if device != None and device.open(auto_start=False):
        print("connecting.\n")
        print("Connected to "+device.name)

        while (1):
                sum = 0
                device.start(period=1000)

        # You can select the specific sensors for data collection using device.enable_sensors().
        # Otherwise, the default sensors will be used when device.get_enabled_sensors() is called.
                device.enable_sensors([1])
                sensors = device.get_enabled_sensors()

                print("Reading measurements\n")
                device.enable_sensors([1])
                for i in range(0,10):
                        if device.read():
                                for sensor in sensors:
                                        # The sensor.values call may read one sensor value, or multiple sensor values (if fast sampling)
                                        print(sensor.sensor_description+": "+str(sensor.values))
                                        #get sum of each 10 samples for average
                                        sum+=sensor.values
                                        sensor.clear()

                device.stop()
                device.enable_sensors([0])
                for i in range(0,10):
                        if device.read():
                                for sensor in sensors:
                                        # The sensor.values call may read one sensor value, or multiple sensor values (if fast sampling)
                                        print(sensor.sensor_description + ": "+str(sensor.values))
                                        #get sum of each 10 samples for average
                                        sum+=sensor.values
                                        sensor.clear()

                device.stop()
                #average the 10 samples
                avg = sum / 10
                print("sample average:" + str(avg))
                #60 seconds set for sampling once a minute
                time.sleep(60)


        device.close()
        print("\nDisconnected from "+device.name)

else:
        print("Go Direct device not found/opened")

godirect.quit()


