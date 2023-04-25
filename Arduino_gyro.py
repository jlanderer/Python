# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:13:19 2022

@author: Jacob Landerer
"""

import serial
import matplotlib.pyplot as plt
import numpy as np
from drawnow import drawnow
SerialComm = serial.Serial('COM10',115200)  # May need to change both values
plt.close('all')
plt.figure();
plt.ion(); # Tells python you want to plot live data
plt.show(); 
DataArray = np.array([])

# Data acquisition time
while(DataAcq.inWaiting() == 0):
    pass #No data to see here
while True:
    Data = DataAcq.readline();  # read as byte data type
    Data = str(Data,'utf-8')  # byte --> string w/\r\n
    Data = Data.strip('\r\n')  # regular old string
    DataArray = Data.split(",")  # array of strings
    aX.append(float(DataArray[0]))
    aY.append(float(DataArray[1]))
    aZ.append(float(DataArray[2]))
    gX.append(float(DataArray[3]))
    gY.append(float(DataArray[4]))
    gZ.append(float(DataArray[5]))
Serial_Comm.close() # Good practice and correct syntax, but does nothing