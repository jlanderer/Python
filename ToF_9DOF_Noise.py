# -*- coding: utf-8 -*-
"""
1/10/23

@author: Jacob Landerer

This program intercepts sensor data from arduino as it goes through a COM port to serial monitor.
This is because arduino's serial plotter cannot create different plots, which I need to
monitor the different sensor values. There should be one data acquisition block and one plotting block
As opposed to the other serial plotting program because that was meant for a single sensor connected
at any given time. This program uses the sensors mentioned in the title simultaneously, with all of their
data being transmitted simultaneously.

process outline for the record:
1. Establish Serial comm: serial.Serial()
2. plot.ion live plotting
3. readline()
4. str(Data, 'utf-8')  or 'latin-1' works better somehow, throws less runtime errors
4a. .strip('\r\n')
5. Split if multiple data points
6. float
"""

import serial
import matplotlib.pyplot as plt
from drawnow import drawnow
import time
import csv
filename = "Sensor_Data.csv"
def makefig():

    # accel
    plt.figure(1)
    plt.plot(a_resultant, 'ro-')
    plt.title('accel')
    plt.ylim(-400, 400)
    plt.xlim(0,25)

    # gyroX
    plt.figure(2)
    plt.subplot(3, 1, 1)
    plt.plot(gX, 'kH--')
    plt.title('gyroX')
    plt.ylim(-1, 1)
    plt.xlim(0, 25)

    # gyroY
    plt.subplot(3, 1, 2)
    plt.plot(gY, 'ro-')
    plt.title('gyroY')
    plt.ylim(-1, 1)
    plt.xlim(0, 25)

    # gyroZ
    plt.subplot(3, 1, 3)
    plt.plot(gZ, 'bx:')
    plt.title('gyroZ')
    plt.ylim(-1, 1)
    plt.xlim(0, 25)

    # temp
    plt.figure(3)
    plt.subplot(3, 1, 1)
    plt.plot(temp, 'ro-')
    plt.title('temp')
    plt.ylabel('*C')
    plt.ylim(10, 30)
    plt.xlim(0, 25)

    # pressure
    plt.subplot(3, 1, 2)
    plt.plot(press, 'bx:')
    plt.title('Pressure')
    plt.ylabel('atm')
    plt.xlim(0, 25)

    # ToF
    plt.subplot(3, 1, 3)
    plt.plot(ToF, 'bx:')
    plt.title('Dist to Impact')
    plt.ylabel('m')
    plt.ylim(0,10)
    plt.xlim(0, 25)

# Data acquisition
DataAcq = serial.Serial('COM5', 115200)
time.sleep(1)
plt.ion()
a_resultant = []
gX = []
gY = []
gZ = []
mX = []
mY = []
mZ = []
temp = []
press = []
ToF = []
noise = []

while True:  # FOREVER
    while DataAcq.inWaiting() == 0:  # if no data transfer
        pass  # No data to see here
    Data = DataAcq.readline()  # read line as byte data type
    Data = str(Data, 'latin-1')  # byte (b'...')--> string with \r\n
    Data = Data.strip('\r\n')  # regular old string sans carriage return and newline escape chars
    DataArray = Data.split(" , ")  # list of strings separated by spaces and comma
    DataArray = [float(i) for i in DataArray]
    noise.append(DataArray[0])
    ToF.append(DataArray[1])
    press.append(DataArray[2])
    temp.append(DataArray[3])    # Sweet sweet data
    a_resultant.append(DataArray[4])
    gX.append(DataArray[5])
    gY.append(DataArray[6])
    gZ.append(DataArray[7])
    drawnow(makefig)

    # I don't know yet how this will work or if I need to change something.
    # Maybe it'll just write one line of data then stop. Maybe it'll write
    # one line, then two, who knows??

    # CSV writing:
    fields = ['Noise','ToF','pressure','temp','accel','gX','gY','gZ']
    rows = [noise,ToF,press,temp,a_resultant,gX,gY,gZ]
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


