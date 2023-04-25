from vpython import *
import numpy as np
import time

clockRadius = 2
clockThick = clockRadius/10
clockFace = cylinder(radius=clockRadius, pos=vector(0, 0, -clockThick/2), axis=vector(0, 0, 1), color=vector(.75, 0, 1.2), length=clockThick)

bigTickL = clockRadius/7
bigTickT = 2*np.pi*clockRadius/400
bigTickW = clockThick*1.2

minorTickL = clockRadius/12            # parameterization of variables,
minorTickT = 2*np.pi*clockRadius/600   # Defining everything relative to everything else
minorTickW = clockThick*1.2            # so that scaling works well if adjustments ar eneeded

# Defining the clock's tick marks at all 60 seconds, with big ones every 5
for theta in np.linspace(0, 2*np.pi, 13):
    majorTick = box(axis=vector(clockRadius*np.cos(theta), clockRadius*np.sin(theta), 0), color=color.black, length=bigTickL, width=bigTickW, height=bigTickT, pos=vector((clockRadius-(bigTickL/2))*np.cos(theta), (clockRadius-(bigTickL/2))*np.sin(theta), 0))
for theta in np.linspace(0, 2*np.pi, 61):
    minorTick = box(axis=vector(clockRadius*np.cos(theta), clockRadius*np.sin(theta), 0), color=color.black, length=minorTickL, width=minorTickW, height=minorTickT, pos=vector((clockRadius-(minorTickL/2))*np.cos(theta), (clockRadius-(minorTickL/2))*np.sin(theta), 0))


minuteHandL = clockRadius-bigTickL
minuteHandT = minuteHandL/25
minuteHandOffset = clockThick/2+minuteHandT

hourHandL = .75*minuteHandL
hourHandT = minuteHandT*1.25
hourHandOffset = clockThick+hourHandT

secondHandL = minuteHandL-bigTickL/2
secondHandT = minuteHandT/5
secondHandOffset = clockThick*1.6+secondHandT

hubRadius = clockThick/2

textH = clockRadius * .25

minuteHand = arrow(axis=vector(0, 1, 0), color=color.red, shaftwidth=minuteHandT, length=minuteHandL, pos=vector(0, 0, minuteHandOffset))
hourHand = arrow(axis=vector(0, 1, 0), color=color.red, shaftwidth=hourHandT, length=hourHandL, pos=vector(0, 0, hourHandOffset))
secondHand = arrow(axis=vector(0, 1, 0), color=color.red, shaftwidth=secondHandT, length=secondHandL, pos= vector(0, 0, secondHandOffset))
pin = cylinder(axis=vector(0, 0, 1), length=1.75*clockThick, color=color.red, radius=hubRadius)

myLabel = text(text='New York Time', depth=clockThick, align='center', pos=vector(0, clockRadius*1.5, -clockThick/2), color=color.green, height=textH)


angle = np.pi/3
angleInc = -np.pi/6  # For numbers
numH = clockRadius/8

for i in range(1, 13, 1):  # For numbers
    clockNum = text(align='center', text=str(i), pos=vector(clockRadius*.75*np.cos(angle), clockRadius*.75*np.sin(angle)-(numH/2), 0), height=numH, depth=clockThick, color=color.blue)
    angle = angle + angleInc

while True:  # It's run time baby
    rate(5000)  # This doesn't matter because I'm grabbing time from system, so it should be as fast as if not faster than the systems clock
    hour = time.localtime(time.time())[3]
    if hour > 12:
        hour = hour - 12
    minute = time.localtime(time.time())[4]  # Determining variables based on system time
    second = time.localtime(time.time())[5]
    hrAngle = -((hour + minute/60)/12)*2*np.pi+np.pi/2
    minAngle = -((minute + second/60)/60)*2*np.pi+np.pi/2  # Angles based on time...radian-time conversions & whatnot
    secAngle = -(second/60)*2*np.pi+np.pi/2
    hourHand.axis = vector(hourHandL*np.cos(hrAngle), hourHandL*np.sin(hrAngle), 0)
    minuteHand.axis = vector(minuteHandL*np.cos(minAngle), minuteHandL*np.sin(minAngle), 0)  # Changing hand position based on time
    secondHand.axis = vector(secondHandL*np.cos(secAngle), secondHandL*np.sin(secAngle), 0)
