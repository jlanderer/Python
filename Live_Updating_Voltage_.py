import serial
from vpython import *
resistance1 = 10000 #!!!!!!!!!!!!!!!!!
WaterArrayPos = []
i = 1
#Single voltage source @ A0
"""DataAcq = serial.Serial('COM10',115200)
while True:
    while (DataAcq.inWaiting() == 0):
        pass
    Data = DataAcq.readline()   # data is of the form: b...\r\n
    i = i + 1
    Data = str(Data,'utf-8')  # 1 byte --> 1 string
    Data = Data.strip('\r\n')
    DataArray = Data.split(",")  # 1 string --> 4 strings
    volts1 = float(DataArray[0])*(5/(2**16))
    current1 = volts/resistance1
"""
# Graphial display of voltage, current, & resistance (Water Tower)
volts1 = 5
current1 = volts1/resistance1
pipe1Height = volts1*50
radius1 = resistance1/1000
waterRadius = radius1/2
yCenter = pipe1Height-waterRadius  # initialized y-coord of center of ball for tracking purposes
Tower1 = cylinder(length = pipe1Height, color = color.blue, opacity = .5, axis = vector(0,1,0),align ='center', radius = radius1)
#Tower spawns w/bottom @ 0
#The spawning of the water drops
while yCenter > 0:
    Water = sphere(color = color.white, radius = waterRadius,pos = vector(0,yCenter,0))
    #WaterArrayPos[i] = yCenter
    i = i + 1
    yCenter = yCenter-waterRadius*3
while True:
    rate(10)
    for i in range(0,int(pipe1Height/(2*waterRadius)),1):
        if yCenter <= waterRadius:
            yCenter = pipe1Height-waterRadius
        yCenter = yCenter - waterRadius
        Water.pos = vector(0,yCenter,0)
    #if yCenter == waterRadius:  # If water reaches end of pipe --- I guess the bottom of cyl is 0
    #    yCenter = pipe1Height-waterRadius
    #yCenter = yCenter-waterRadius
    #Water.pos = vector(0,yCenter,0)
#DataAcq.close()