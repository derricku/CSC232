"""
Homework 5
>Problem 9

Author: Derrick Unger
Date: 2/14/20
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
        ang = deg*(np.pi)/180  # Convert to radians
        break

    except ZeroDivisionError:
        print("Error, try again...")

# Initial Points
A = np.array([6, 6, 1])
B = np.array([6, 10, 1])
C = np.array([10, 10, 1])
D = np.array([10, 6, 1])

# Translation to Origin
t1 = np.array(([1, 0, -8], [0, 1, -8], [0, 0, 1]))
t1A = np.dot(t1, A)
t1B = np.dot(t1, B)
t1C = np.dot(t1, C)
t1D = np.dot(t1, D)

# Rotation about Z axis
rot = np.array(([np.cos(ang), -1*np.sin(ang), 0],
                [np.sin(ang), np.cos(ang), 0],
                [0, 0, 1]))

rotA = np.dot(rot, t1A)
rotB = np.dot(rot, t1B)
rotC = np.dot(rot, t1C)
rotD = np.dot(rot, t1D)

# Translation back to Original Location
t2 = np.array(([1, 0, 8], [0, 1, 8], [0, 0, 1]))
t2A = np.dot(t2, rotA)
t2B = np.dot(t2, rotB)
t2C = np.dot(t2, rotC)
t2D = np.dot(t2, rotD)

print("A: ", t2A)
print("B: ", t2B)
print("C: ", t2C)
print("D: ", t2D)
