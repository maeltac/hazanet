import time
try:
    import gps
except:
    print("No GPSD detected, welcome to errorsville!")
    pass



class Gps():

    def init_gps(self):
        """
        Starts the GPS, and returns the iterator
        """
        #session = gps.gps('localhost','2947')
        #session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        print('\nInitializing GPS\n----------------------------------------')
        coldstart_wait = 5
        location = {}

        for i in reversed(range(coldstart_wait)):
            print (i+1," Seconds until Coldstart finished")
            time.sleep(1)
            coldstart_wait -= 1

        location['lat'] = 37.24     # Groom Lake!
        location['lon'] = -115.81   # Groom Lake!
        location['alt'] = 3500
        location['head'] = 180 # Direction from (Not sure if MagNorth or TrueNorth?)

        #return session     # Real deal
        return location         #simulation

    def read(self, session):
        """
        Returns a dictionary of data
        """
        if session:
            report = session.next()
        else:
            return 1
        return report



    def killstream(self, session):
        if session:
            session = None
        return 0





class Accel():

    def zero_accel(self, accel_ID):
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