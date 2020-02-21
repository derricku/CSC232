"""
Homework 6
>Problem 1

Author: Derrick Unger
Date: 2/22/20
CSC232 Winter 2020
"""
import numpy as np

np.set_printoptions(formatter={'float_kind': lambda value: format(value, '8.3f'),
                               'int_kind': lambda value: format(value, '10d')})
while True:
    try:
        # Angle of Rotation
        deg = input("Enter angle of rotation in degrees [-360, 360]: ")
        deg = eval(deg)
        if deg < -360 or deg > 360:
            print("Angle must be between -360 and 360 degrees.")
            err = 1/0
        ang = np.deg2rad(deg)  # Convert to radians
        break

    except:
        print("Error, try again...")

# Initial Point
A = np.array([3, 1, 2])

# Rotation about Z axis
rot = np.array(([np.cos(ang), -1*np.sin(ang), 0],
                [np.sin(ang), np.cos(ang), 0],
                [0, 0, 1]))

rotA = np.dot(rot, A)

print("Original A: ", A)
print("Rotated A: ", rotA)
