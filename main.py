# ---------------------------------------------
# Georges Hart
# BNO055 simple sketch
# 08 november 2020
#
#
# source: https://github.com/njeff/ee49-balance
# source: https://docs.micropython.org/en/latest/library/machine.I2C.html
# source: https://www.allaboutcircuits.com/projects/bosch-absolute-orientation-sensor-bno055/
#
# BNO055 Calculating position datas (x,y,z) based on accelerometer datas:
# https://community.bosch-sensortec.com/t5/MEMS-sensors-forum/BNO055-Calculating-position-datas-x-y-z-based-on-accelerometer/td-p/1300
#
#
# ----------------------------------------------

from machine import SoftI2C, Pin
from machine import UART
import time
import bno055




# ----- Initialisation Serial Port -----
'''
uart = UART(1, 38400)                         # init with given baudrate
uart.init(38400, bits=8, parity=None, stop=1) # init with given parameters
t = uart.write(bytes('Georges Hart',"UTF-8"))
'''

# ----- I2C initialisation -----
i2c = SoftI2C(Pin(22), Pin(23), timeout=1000)


# ----- BNO055 setup
s = bno055.BNO055(i2c)
s.mode = bno055.GYRONLY_MODE # only Gyrocope is active (see bno055.py)
s.reset()
s.init()



# print('Temperature :{} degrees °C'.format(s.temperature()))

file = open ("log.gh", "w")
file.write("Log file")
file.close()

while True:
   
    #print("Temperature: {} degrees C".format(s.temperature()))
    # ----- EULER -----
    x =(("{}".format(s.euler())))
    x=x.split()

    # yaw = x[0]
    # pitch= x[1]
    roll =x[2]
    z=len(roll)
    
    coordinaten = (roll[0:z-1])
    print (coordinaten)
    
    
    
    time.sleep(0.15)