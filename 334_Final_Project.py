import serial
from vpython import *
COM_Port = 'COM6';
Baud_Rate = 115200;
# Data_acq = serial.Serial(COM_Port, Baud_Rate)

scene = canvas()

#airplane = box(pos=vector(0, 0, 0), length=5, width=5, height=1, color=color.white)

# Create airplane shape using vertices
airplane_verts = [vector(-1, 0, 0), vector(-1, 1, 0), vector(-2, 1, 0), vector(-2, 3, 0),
                  vector(-1, 3, 0), vector(-1, 5, 0), vector(1, 5, 0), vector(1, 3, 0),
                  vector(2, 3, 0), vector(2, 1, 0), vector(1, 1, 0), vector(1, 0, 0),
                  vector(1, 1, 2), vector(-1, 1, 2), vector(-1, 0, 2), vector(1, 0, 2),
                  vector(-1, 3, 2), vector(1, 3, 2), vector(-2, 3, 2), vector(2, 3, 2)]

# Create airplane object using extrusion
airplane = extrusion(path=[vec(0,0,0),vec(0,0,1)], shape=airplane_verts, color=color.blue)
while True:
    data = Data_acq.readline().decode().strip().split(',')
    # Readline() reads the serial port
    # decode() changes the data type from byte to string, I've used 'Latin-8' before but also 'UTF- something'
    # strip() takes away the \r\n
    # split() creates individual variables for everything between commas

    yaw = float(data[0])
    pitch = float(data[1])
    roll = float(data[2])

    airplane.rotate(angle=radians(yaw), axis=vector(0, 1, 0))
    airplane.rotate(angle=radians(pitch), axis=vector(1, 0, 0))
    airplane.rotate(angle=radians(roll), axis=vector(0, 0, 1))