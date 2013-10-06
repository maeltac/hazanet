
import pdb
"""
Each sensor that uses this will follow these rules:
calling sensor.startup() function will initialize and calibrate the sensor. It will return 'Green' on success, 'Red' on failure
calling sensor.read() will return a float for that tick
calling sensor.reset() will attempt to reset the sensor, returning 0 for success, 1 for failure, or 2 for wait
"""


class Sensor():

    def startup(self,sentype):
        #pdb.set_trace()
        if sentype == 'RAD':
            return RAD.startup(self,sentype)
        elif sentype =='CO':
            return CO.startup(self,sentype)
        elif sentype =='CH4':
            return CH4.startup(self,sentype)
        elif sentype =='C6H6':
            return C6H6.startup(self,sentype)
        elif sentype =='C3H8':
            return C3H8.startup(self,sentype)
        else:
            return 'Error Initializing'


    def read(self):
        return 0

    def reset(self):
        return 0

    def supported(self):
        supportlist = ['RAD', 'CO', 'CH4', 'C6H6', 'C3H8']
        return supportlist






class RAD(Sensor):

    def startup(self,sentype):
        retstring = 'Sickly Green'
        return retstring

    def read(self):
        return 0

    def reset(self):
        return 0



class CO(Sensor):

    def startup(self,sentype):
        return 'Blue'

    def read(self):
        return 0

    def reset(self):
        return 0



class CH4(Sensor):

    def startup(self,sentype):
        return 'Nausious'

    def read(self):
        return 0

    def reset(self):
        return 0



class C6H6(Sensor):

    def startup(self, sentype):
        return 'Toxic'

    def read(self):
        return 0

    def reset(self):
        return 0



class C3H8(Sensor):

    def startup(self, sentype):
        return 'On Fire'

    def read(self):
        return 0

    def reset(self):
        return 0


