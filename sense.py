

"""
Each sensor that uses this will follow these rules:
calling sensor.startup() function will initialize and calibrate the sensor. It will return 'Green' on success, 'Red' on failure
calling sensor.read() will return a float for that tick
calling sensor.reset() will attempt to reset the sensor, returning 0 for success, 1 for failure, or 2 for wait


"""


class Sensor():

    def startup(sentype):
        if sentype == 'RAD':
            return str(RAD.startup(sentype))
        elif sentype =='CO':
            return CO.startup(sentype)
        elif sentype =='CH4':
            return CH4.startup(sentype)
        elif sentype =='C6H6':
            return C6H6.startup(sentype)
        elif sentype =='C3H8':
            return C3H8.startup(sentype)
        else:
            return 'Yellow'


    def read(self):
        return 0

    def reset(self):
        return 0

    def supported(self):
        supportlist = ['RAD', 'CO', 'CH4', 'C6H6', 'C3H8']
        return supportlist






class RAD(Sensor):

    def startup(sentype):
        return 'Sickly Green'

    def read(self):
        return 0

    def reset(self):
        return 0



class CO(Sensor):

    def startup(self):
        return 'Blue'

    def read(self):
        return 0

    def reset(self):
        return 0



class CH4(Sensor):

    def startup(self):
        return 'Nausious'

    def read(self):
        return 0

    def reset(self):
        return 0



class C6H6(Sensor):

    def startup(self):
        return 'Toxic'

    def read(self):
        return 0

    def reset(self):
        return 0



class C3H8(Sensor):

    def startup(self):
        return 'On Fire'

    def read(self):
        return 0

    def reset(self):
        return 0


