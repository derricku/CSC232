"""
Homework 6
>Problem 2

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
        deg = float(deg)
        if deg < -360 or deg > 360:
            print("Angle must be between -360 and 360 degrees.")
            err = 1/0
        ang = np.deg2rad(deg)  # Convert to radians

        # Scale Factor
        Sx, Sy, Sz = input("Enter 3 scale factors e.g: x,y,z:").split(",")
        scale = np.array([float(Sx), float(Sy), float(Sz)])

        break
    except:
        print("Error, try again...")

# Initial Points
A = np.array([4, 4, 6])
B = np.array([6, -2, 3])
C = np.array([1, -1, 3])
D = np.array([10, 9, 3])
arrayStart = np.array([A, B, C, D])

# Scale Points
scaleMatrix = np.array(([scale[0], 0, 0, 0], [0, scale[1], 0, 0],
                        [0, 0, scale[2], 0], [0, 0, 0, 1]))

sA = np.dot(scaleMatrix, np.append(A, 1))
sB = np.dot(scaleMatrix, np.append(B, 1))
sC = np.dot(scaleMatrix, np.append(C, 1))
sD = np.dot(scaleMatrix, np.append(D, 1))


# Translate Points
tran1Matrix = np.array(([1, 0, 0, 0], [0, 1, 0, 0],
                        [0, 0, 1, -5], [0, 0, 0, 1]))
t1A = np.dot(tran1Matrix, sA)
t1B = np.dot(tran1Matrix, sB)
t1C = np.dot(tran1Matrix, sC)
t1D = np.dot(tran1Matrix, sD)


# Rotation about Line (z = 5, parallel to x-axis)
rotX = np.array(([np.cos(ang), -1*np.sin(ang), 0],
                [np.sin(ang), np.cos(ang), 0],
                [0, 0, 1]))
rotA = np.dot(rotX, np.delete(t1A, [3]))
rotB = np.dot(rotX, np.delete(t1B, [3]))
rotC = np.dot(rotX, np.delete(t1C, [3]))
rotD = np.dot(rotX, np.delete(t1D, [3]))


# Translate Points Back
tran2Matrix = np.array(([1, 0, 0, 0], [0, 1, 0, 0],
                        [0, 0, 1, 5], [0, 0, 0, 1]))
t2A = np.dot(tran2Matrix, np.append(rotA, 1))
t2B = np.dot(tran2Matrix, np.append(rotB, 1))
t2C = np.dot(tran2Matrix, np.append(rotC, 1))
t2D = np.dot(tran2Matrix, np.append(rotD, 1))
arrayFinal = np.array([t2A[:3], t2B[:3], t2C[:3], t2D[:3]])

print("\nOriginal A: \n", arrayStart)
print("\nRotated A: \n", arrayFinal)
