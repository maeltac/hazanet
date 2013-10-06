import time
import os
import RPi.GPIO as GPIO

#Setup Constants
BITZ = int(10)          # bit sampling for adc. MCP3008 uses 10.
DAMP = 1                # Dampening of the accelerometer signal. Default 1
ZLEEP = 0.1             # Sample rate in 1/hz. 0.1 works fine. 100 not so much

#Setup GPIO and Pins
GPIO.setmode(GPIO.BCM)   # use board pin identifiers
SPI_CLK = 18             # using bit banging, not onboard pi spi. cause: stupid
SPI_MISO = 23            # numbers correspond to GPIO pins on Raspi header
SPI_MOSI = 24
SPI_CS = 25
GPIO.setup(SPI_MOSI, GPIO.OUT)  # Setting pins for direction
GPIO.setup(SPI_MISO, GPIO.IN)
GPIO.setup(SPI_CLK, GPIO.OUT)
GPIO.setup(SPI_CS, GPIO.OUT)

#Setup axis
x_axis = 2               # Analog channel 3 from ADC
y_axis = 1               # Analog channel 2 from ADC
z_axis = 0               # Analog channel 1 from ADC

axes = [x_axis,y_axis,z_axis] # assembly for the loop

last_x = 500            # previous readings from ADC for comparison in loop
last_y = 500            # initialized at 500 = no acceleration 
last_z = 626            # initialized at 626 = accel due to gravity


# function to read SPI data from MCP 3008 chip

def readadc(adcnum, clk_pin, mosi_pin, miso_pin, cs_pin, bitwidth):
    """
    This function reads the digital pins from the ADC. Currently set for an 
    8 channel ADC, MCP3008. Mostly stolen from adafruit volume control example
    """

    if adcnum > 7 or adcnum <0: return -1 # oh snap. wrong channel numbers

    # Initialization
    adcout = 0                      #Data stored here! This gets returned
    GPIO.output(cs_pin, True)       #Bring cs high
    GPIO.output(clk_pin, False)     #Start clock low
    GPIO.output(cs_pin, False)      #Start cs low

    commandout = adcnum             # this is the channel to poll
    commandout |= 0x18              # start bit + single-ended bit
    commandout <<= 3                # send 5 bits

    for i in range(5):
        if(commandout & 0x80):
            GPIO.output(mosi_pin, True)
        else:
            GPIO.output(mosi_pin, False)
        commandout <<=1
        GPIO.output(clk_pin, True)
        GPIO.output(clk_pin, False)

    # read in empty bit, null bit, and 10 ADC bits 
    bitwidth = int(bitwidth) + 2
    for i in range(int(bitwidth)):
        GPIO.output(clk_pin, True)
        GPIO.output(clk_pin, False)
        adcout <<= 1
        if (GPIO.input(miso_pin)):
            adcout |= 0x1

    GPIO.output(cs_pin, True)

    adcout >>= 1       # first bit is 'null' so drop it
    return adcout

#TODO: calibrator to allow for weird tilts and altitude-gravity adjustments
def calibrate():       
    pass

# Primary loop to read off of accel.
while True:
    os.system('clear')
    x_y_z_vals = []      # this stores the read values of the x,y,z axes
    delta_x_y_z = []     # this stores the change in axis value
    motion = -1         # will allow flag to be thrown if there is a read error from ADC

    for i in axes:
        motion = readadc(i, SPI_CLK, SPI_MOSI, SPI_MISO, SPI_CS, BITZ)
        if motion == -1:
            print('ERROR: Invalid ADC channel queried!')
        x_y_z_vals.append(motion)
   
    delta_x = x_y_z_vals[0] - last_x
    delta_y = x_y_z_vals[1] - last_y
    delta_z = x_y_z_vals[2] - last_z
    if abs(delta_x) <= DAMP: delta_x = 0  # silence jittery values based on DAMP
    if abs(delta_y) <= DAMP: delta_y = 0
    if abs(delta_z) <= DAMP: delta_z = 0
    last_x = x_y_z_vals[0]           # Prep values for next time through loop
    last_y = x_y_z_vals[1]
    last_z = x_y_z_vals[2]


    print(" ".join([" dX:",str(delta_x),"\n","dY:",str(delta_y),"\n","dZ:", \
        str(delta_z)])) # print the change in accel (direction preserving)

    time.sleep(ZLEEP)
