import os
import sys
import positional as posi
import sense          # this is the sensor function library
from sense import Sensor as Sensor



"""
This program initializes and starts the sensor network. Each sensor will have its own library to deal with incoming data
for each tick. This program will then take the

Note: This completely breaks realtime, but will be necessary, since each sensor will be bringing in data at different
rates. While time correlation is not really necessary, it may be useful for longer-term data analysis.

"""



def init_sensor(sentype):
    """
    Check for Sensor Support, and send initialize
    """
    if sentype in Sensor.supported(sentype):        #TODO: Make sensor initialization not dependant on unordered set. Startup is kinda creepy.
        status = Sensor.startup(sentype)
    else:
        status = 'Unsupported Sensor'

    return status


def init_location():
    """
    initialize the GPS, and return current location
    """
    print('\nInitializing GPS\n----------------------------------------')
    location = {}

    location['lat'] = 37.24     # Groom Lake!
    location['lon'] = -115.81   # Groom Lake!
    location['head'] = 180 # Direction from (Not sure if MagNorth or TrueNorth?)

    return location

def zero_accel():
    """
    Zeros the accelerometer, and determines which axis gravity is operating
    """
    print('\nZeroing Accelerometer and Gyro\n----------------------------------------')
    gravaxis = {}
    gravaxis['x'] = 526
    gravaxis['y'] = 566
    gravaxis['z'] = 946

    axistotal = gravaxis['x'] + gravaxis['y'] + gravaxis['z']


         #each axis will be a signed decimal of the initial "flat"
    return gravaxis


if __name__ == "__main__":

    #Startdat
    startstat ={}   # Startup status of all sensor systems
    print("Startup initiated\n----------------------------------------")
    startstat['RAD'] = init_sensor("RAD")
    startstat['CO'] = init_sensor("CO")
    startstat['CH4'] = init_sensor("CH4")
    startstat['C6H6'] = init_sensor("C6H6")
    startstat['C3H8'] = init_sensor("C3H8")
    startstat['C6H12O6'] = init_sensor("C6H12O6")

    for key, value in startstat.items():
        print(key, ": ", value)


    start_loc = init_location()
    print("GPS Calibrated at:", start_loc['lat'],start_loc['lon'] )
    print("Heading:", start_loc['head'])
    print("Balance Calibrated, gravity axis: ")
    accel_init = zero_accel()
    for key, value in accel_init.items():
            print (key, value)

