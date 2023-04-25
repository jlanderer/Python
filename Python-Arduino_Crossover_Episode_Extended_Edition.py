# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:54:38 2022
LED on/off
@author: Jacob Landerer
Change COM Ports as necessary
"""

import serial
import time

serialComm = serial.Serial('COM6', 9600) # Nano Com port is 10, uno is 8 or 9
serialComm.timeout = 1  # ??

while True:
    i = input("input(on/off): ").strip()  # removes spaces before and after a string
    if i == 'done':
        print('Finished program')
        break
    serialComm.write(i.encode()) # in bytes to arduino                   \
    time.sleep(.5)                                                       # computers really have a mind of their own, trying to covertly communicate
    print(serialComm.readline().decode('ascii')) #in bytes from arduino  /
serialComm.close()