"""
Homework 9
>Problem 1

Author: Derrick Unger
Date: 3/14/20
CSC232 Winter 2020
"""

import numpy as np
np.set_printoptions(formatter={'float_kind': lambda value: format(value, '8.3f'),
                               'int_kind': lambda value: format(value, '7d')})

# Include for Reading in Text File
"""
# Read in Points Text File
f = open("Test5-0304-P1-DataSet1.txt", "r")
point = []
x = []
y = []
z = []
for line in f:
    line = line.strip()  # Remove trailing and leading whitespace
    line = " ".join(line.split())  # Remove extra spaces
    vals = line.split(" ")

    if len(vals) > 1:  # Skip last line
        point.append(vals[0])
        x.append(vals[1])
        y.append(vals[2])
        z.append(vals[3])

# Initial Points
Ax, Ay, Az = float(x[0]), float(y[0]), float(z[0])
Bx, By, Bz = float(x[1]), float(y[1]), float(z[1])
Cx, Cy, Cz = float(x[2]), float(y[2]), float(z[2])
Ax1, Ay1, Az1 = float(x[3]), float(y[3]), float(z[3])
Bx1, By1, Bz1 = float(x[4]), float(y[4]), float(z[4])
"""
Ax, Ay = 2, 5
Bx, By = 5, 2.5
Cx, Cy = 1.5, 2

# Shoelace Area
sArea1 = .5*abs((Bx*Ay)+(Cx*By)+(Ax*Cy)-(Ax*By)-(Bx*Cy)-(Cx*Ay))
print("\nInitital Area = ", sArea1)

# Angle Between 3 Points
B = np.array([Bx, By])
A = np.array([Ax, Ay])
X = np.array([Bx + 10, Ay])

AB = B - A
AX = X - A

cosAngle = np.dot(AB, AX)/(np.linalg.norm(AB) * np.linalg.norm(AX))
angle = np.arccos(cosAngle)
angle = np.degrees(angle)  # Convert to degrees
print("Angle: ", round(angle, 4))  # Angle to rotate


# Translation Function
def JustDoIt(pointTarget, basepoint, ang):
    ang = np.radians(ang)
    t1 = np.array([[1, 0, -1*basepoint[0]],
                  [0, 1, -1*basepoint[1]],
                  [0, 0, 1]])
    t2 = np.array([[1, 0, 1*basepoint[0]],
                  [0, 1, 1*basepoint[1]],
                  [0, 0, 1]])
    rotZ = np.array(([np.cos(ang), -1*np.sin(ang), 0],
                    [np.sin(ang), np.cos(ang), 0],
                    [0, 0, 1]))

    M1 = np.dot(rotZ, t1)
    M3 = np.dot(t2, M1)
    final = np.dot(M3, pointTarget)
    return final


# Translate Points
C1 = JustDoIt([Cx, Cy, 1], [Ax, Ay], angle)  # Clockwise? -Ang for counterclock

Cx1 = C1[0]  # Not sure what going on in the *update* part
Cy1 = C1[1]
Cy1, Cx1 = C1[0] + 10, 1 + 5 - C1[1]
print("C1 = ", round(Cx1, 3), round(Cy1, 3))

Ax1, Ay1 = 1, 12
Bx1, By1 = 1, 15.90512

# Shoelace Area2
sArea2 = .5*abs((Bx1*Ay1)+(Cx1*By1)+(Ax1*Cy1)-(Ax1*By1)-(Bx1*Cy1)-(Cx1*Ay1))
print("Final Area = ", round(sArea2, 4), "\n")
