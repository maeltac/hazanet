import os
import sys
import positional as posi
import sense          # this is the sensor function library
#from sense import Sensor as Sensor
import pdb



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
    sen = sense.Sensor()
    if sentype in sen.supported():
        status = sen.startup(sentype)
    else:
        status = 'Unsupported Sensor'
    return status


def init_location():
    """
    initialize the GPS, and return current location
    """
    gobj = posi.Gps()        # Create GPS Object
    location = gobj.init_gps()

    return location




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
    #accel_init = posi.Accel.zero_accel(Accel,1)
    #for key, value in accel_init.items():
            #print (key, value)


    # Set tick rate in Hz
    TICKS_PER_SECOND = 10