# -*- coding: utf-8 -*- 
"""
Created on Wed Jul 27 14:25:06 2022

@author: Jacob Landerer

This program can take in and plot live data from I2C serial communication
with an arduino and an attached sensor. The arduino program is different
based on which sensor is attached, and different blocks of code in this
program correspond to these different sensors. The makeFig() is diff for each sensor
because they output a differnt number of parameters

1. Establish Serial comm: serial.Serial()
2. plot.ion live plotting
3. while loop wait for serial comm
3a. readline()
4. str(Data, 'utf-8')
4a. .strip('\r\n')
5. Split if multiple data points
6. float
"""

import serial
import matplotlib.pyplot as plt
import numpy as np
from drawnow import drawnow

"""
#   For GY_91 accelerometer & gyroscope   (I do have to say python doesnt like negative values especially if they're sequential)
def makeFig():                          #  It sometimes takes in two values as a single one causing an indexing error with [5]

    #accelX
    plt.subplot(3,2,1)
    plt.plot(aX, 'ro-')
    plt.title('accelX')

    #accelY
    plt.subplot(3,2,2)
    plt.plot(aY, 'bx:')
    plt.title('accelY')

    #accelZ
    plt.subplot(3,2,3)
    plt.plot(aZ, 'g-.')
    plt.title('accelZ')


    #gyroX
    plt.subplot(3,2,4)
    plt.plot(gX, 'kH--')
    plt.title('gyroX')

    #gyroY
    plt.subplot(3,2,5)
    plt.plot(gY, 'ro-')
    plt.title('gyroY')

    #gyroZ
    plt.subplot(3,2,6)
    plt.plot(gY, 'bx:')
    plt.title('gyroZ')
#Data acquisition for GY_91
DataAcq = serial.Serial('COM10', 9600)
plt.ion()
aX = []
aY = []
aZ = []
gX = []
gY = []
gZ = []
i = 0  # counter to fit data only 50 points on graph
while(DataAcq.inWaiting() == 0):
    pass #No data to see here
while True:
    Data = DataAcq.readline();  # read as byte data type
    i = i + 1
    Data = str(Data,'utf-8')  # byte --> string w/\r\n
    Data = Data.strip('\r\n')  # regular old string
    DataArray = Data.split(",")  # array of strings
    aX.append(float(DataArray[0]))
    aY.append(float(DataArray[1]))
    aZ.append(float(DataArray[2]))
    gX.append(float(DataArray[3]))
    gY.append(float(DataArray[4]))
    gZ.append(float(DataArray[5]))
    if (i > 50):
        aX.pop(0)
        aY.pop(0)
        aZ.pop(0)
        gX.pop(0)
        gY.pop(0)
        gZ.pop(0)
    drawnow(makeFig)
DataAcq.close()



#For 16-bit ADC
def makeFig():  #scale subplots accordingly, need to know bounds
    plt.subplot(2,2,1)
    plt.plot(ar0, 'ro-')
    plt.title('Analog Reading 1')
    plt.ylabel('Volts')
    
    plt.subplot(2,2,2)
    plt.plot(ar1, 'bx:')
    plt.title('Analog Reading 2')
    plt.ylabel('Volts')

    plt.subplot(2,2,3)
    plt.plot(ar2, 'g-.')
    plt.title('Analog Reading 3')
    plt.ylabel('Volts')

    plt.subplot(2,2,4)
    plt.plot(ar3, 'kH--')
    plt.title('Analog Reading 4')
    plt.ylabel('Volts')

#This group works with 4 inputs, for the 16-bit ADC.
DataAcq = serial.Serial('COM10',115200)
plt.ion();
ar0 = []
ar1 = []
ar2 = []
ar3 = []
i = 0  # counter to fit data in window
while True:
    while (DataAcq.inWaiting() == 0):
        pass
    Data = DataAcq.readline()   # data is of the form: b...\r\n
    i = i + 1
    Data = str(Data,'utf-8')  # 1 byte --> 1 string
    Data = Data.strip('\r\n')
    DataArray = Data.split(",")  # 1 string --> 4 strings
    A0 = float(DataArray[0])*(5/(2**16))
    A1 = float(DataArray[1])*(5/(2**16))
    A2 = float(DataArray[2])*(5/(2**16))  # 4 strings --> 4 numbers (Voltage 0-5)
    A3 = float(DataArray[3])*(5/(2**16))
    if (i > 50):
        ar0.pop(0)
        ar1.pop(0)
        ar2.pop(0)
        ar3.pop(0)
    ar0.append(A0)
    ar1.append(A1)
    ar2.append(A2)  # dynamic arrays
    ar3.append(A3)
    drawnow(makeFig)

DataAcq.close()



# This Block is for 10 bit nano with single voltage input
# use a potentiometer
# Don't change any code unless baud rate or com port are unsynched please
ar = []
i = 0
DataAcq = serial.Serial('COM10',115200) # "[Serial] Data Acquisition"... Baud rate may vary be careful
plt.ion();  # Tells python its about to plot live data



# It seems like separating the graph-printing into its own method actually gets rid of the need for plt.cla()
def makeFig():  # I have a feeling this method is redundant and I could just type thos individual lines in but I just unplugged everything so testing would be annoying
     plt.ylim(0,5)
     plt.grid(True)
     plt.ylabel('Voltage')
     plt.title('10-bit Potentiometer readings')
     plt.plot(ar, 'ro-')  # Makes plot wow cool much good

while True:
    while(DataAcq.inWaiting() == 0):
        pass    #Stay...good boy...
    Data = DataAcq.readline() # data comes in as String -- b' \r\n --'b' for byte
        #I don't understand why, but 'utf-8' command as well as .decode() work and also not adding either line works   
        # No split command needed bc only one data point
    Data = float(Data)   # et voila... Data         Lack of this line makes all potentiometer changes only increase graphed line try it its kinda cool
    Volts = Data*(5/1024) #10-bit readings to voltage 0-5 V
    ar.append(Volts); # dynamic array
    
#   Data acquisition complete... time for printing real live data...    

    drawnow(makeFig)

    i = i + 1
    if (i > 30):
        ar.pop(0)
DataAcq.close()
#Learning experience: decode() works only with one datum passing
"""


#HW_290 (BMP_085 barometer, unspecified temp sensor)
def makefig():
    plt.subplot(3, 1, 1)
    plt.plot(tempC, 'ro-')
    plt.title('temp')
    plt.ylabel('*C')
    
    plt.subplot(3, 1, 2)
    plt.plot(pressPa, 'bx:')
    plt.title('Pressure')
    plt.ylabel('Pa')


DataAcq = serial.Serial('COM10',115200)
plt.ion()
i = 0
tempC = []
pressPa = []
alt = []
while DataAcq.inWaiting() == 0:
    pass
while True:
    Data = DataAcq.readline()  # byte data type
    i = i + 1
    Data = str(Data, 'utf-8')
    Data = Data.strip('\r\n')
    DataArray = Data.split(",")
    tempC.append(float(DataArray[0]))
    pressPa.append(float(DataArray[1]))
    if i > 50:
        tempC.pop(0)
        pressPa.pop(0)
    drawnow(makefig)
