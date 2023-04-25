from vpython import *
import serial
import numpy as np

# Set up serial communication with Arduino
ser = serial.Serial('COM3', 115200, timeout=1)

# Define constants
g = vector(0, 0, -9.81)  # gravitational acceleration in m/s^2
T = 0.1  # sampling period in seconds
omega_c = 5  # cutoff frequency for the low-pass filter in Hz
R_world = np.eye(3)  # initial rotation matrix for world frame

# Define initial values
first_time = True
accel_bias = vector(0, 0, 0)
gyro_bias = vector(0, 0, 0)

# Define airplane shape
shape_data = [(0.2, 0, 0), (0, 1, 0), (0, 0, 1), (-0.2, 0, 0)]
airplane = shapes.triangle(pos=[vector(*p) for p in shape_data], color=color.red).triangulate()
airplane_extrusion = extrusion(path=[vec(0, 0, 0), vec(0, 0, 0.1)], shape=airplane, color=color.blue)


# Function to calculate rotation matrix from accelerometer data
def calculate_R_accel(accel_array):
    global accel_bias, R_world
    accel = vector(*accel_array) - accel_bias
    accel = accel / mag(accel)
    x_c = vector(1, 0, 0)
    y_c = vector(0, 1, 0)
    z_c = cross(x_c, accel)
    z_c = z_c / mag(z_c)
    y_c = cross(accel, z_c)
    y_c = y_c / mag(y_c)
    x_c = cross(y_c, z_c)
    R_body = np.array([[x_c.x, y_c.x, z_c.x],
                       [x_c.y, y_c.y, z_c.y],
                       [x_c.z, y_c.z, z_c.z]])
    R_world = R_body @ np.eye(3)


# Loop to read sensor data and update airplane orientation
while True:
    # Read sensor data
    line = ser.readline().decode('utf-8').strip()
    data = line.split(',')
    if len(data) == 6:
        ax, ay, az, gx, gy, gz = [float(x) for x in data]
        accel_array = np.array([ax, ay, az])
        gyro_array = np.array([gx, gy, gz])

        # Apply low-pass filter to accelerometer data
        if first_time:
            y_k = accel_array
            first_time = False
        else:
            y_k = (1 - omega_c * T) * y_k + omega_c * T * accel_array

        # Calculate rotation matrix from accelerometer data
        calculate_R_accel(y_k)

        # Update airplane orientation
        R_airplane = np.array([[0, 1, 0],
                               [-1, 0, 0],
                               [0, 0, 1]])
        R_airplane = R_airplane @ R_world
        airplane.axis = vector(R_airplane[0, 0], R_airplane[1, 0], R_airplane[2, 0])
        airplane.up = vector(R_airplane[0, 2], R_airplane[1, 2], R_airplane[2, 2])
        airplane.length = 0.3
