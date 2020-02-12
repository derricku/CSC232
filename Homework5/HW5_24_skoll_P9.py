"""
Homework 5
>Problem 9 Test Version

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""
import numpy as np
import matplotlib.pyplot as plt

# To do:
# Make scaling factor and input
# Make ability to rotate about other points besides center

# USER INPUT: number of points, points, angle of rotation
while True:
    try:
        # Number of Points
        numPoints = input("Input number of points desired: ")
        if int(numPoints) < 3:
            print("Error: Number of points must be an int 3 or larger.")
            err = 1/0
        else:
            # Points
            poly = []  # List of points of the form [x, y]
            for i in range(1, int(numPoints)+1):
                print("Enter point number", i, "Ex: Coord [1,2] input as 1,2")
                pointX, pointY = input("Input: ").split(",")
                point = np.array([eval(pointX), eval(pointY)])
                poly.append(point)

            # Angle of Rotation
            deg = input("Enter angle of rotation in degrees [-360, 360]: ")
            if deg < -360 or deg > 360:
                print("Angle must be between -360 and 360 degrees.")
                err = 1/0
            angRot = eval(deg)*(np.pi)/180  # Convert to radians
            break

    except:
        print("Error, try again...")


# ==============CENTROID CALCULATION==============
# This part is not my work. I referenced it from Robert Fotino @
# https://fotino.me/calculating-centroids/
# who came up with the method of splitting polygons into triangles,
# and subtracting/adding their area based of left/right handedness

# Calculate the centroid from the weighted average of the polygon's
# constituent triangles
area_total = 0
centroid_total = [float(poly[0][0]), float(poly[0][1])]
for i in range(0, len(poly) - 2):
    # Get points for triangle ABC
    a, b, c = poly[0], poly[i+1], poly[i+2]

    # Calculate the signed area of triangle ABC
    area = ((a[0] * (b[1] - c[1]))
            + (b[0] * (c[1] - a[1]))
            + (c[0] * (a[1] - b[1]))) / 2.0

    # If the area is zero, the triangle's line segments are colinear so we
    # should skip it
    if 0 == area:
        continue

    # The centroid of the triangle ABC is the average of its three vertices
    centroid = [(a[0] + b[0] + c[0]) / 3.0, (a[1] + b[1] + c[1]) / 3.0]

    # Add triangle ABC's area and centroid to the weighted average
    centroid_total[0] = ((area_total * centroid_total[0])
                         + (area * centroid[0])) / (area_total + area)
    centroid_total[1] = ((area_total * centroid_total[1])
                         + (area * centroid[1])) / (area_total + area)
    area_total += area
# ===========================================================
print("Centroid: ", centroid_total)

# Initial Points
A = np.array([1, 1, 1])
B = np.array([1, 6, 1])
C = np.array([6, 6, 1])
D = np.array([6, 1, 1])

a = np.array(A[1], A[2])
b = np.array(B[1], B[2])
c = np.array(C[1], C[2])
d = np.array(D[1], D[2])

# Translation to Origin
t1 = np.array(([1, 0, -6], [0, 1, -6], [0, 0, 1]))
t1A = np.dot(t1, A)
t1B = np.dot(t1, B)
t1C = np.dot(t1, C)
t1D = np.dot(t1, D)


ang = np.pi/4

# Rotation about Z axis
rot = np.array(([np.cos(ang), -1*np.sin(ang), 0],
                [np.sin(ang), np.cos(ang), 0],
                [0, 0, 1]))

rotA = np.dot(rot, t1A)
rotB = np.dot(rot, t1B)
rotC = np.dot(rot, t1C)
rotD = np.dot(rot, t1D)

# Translation back to Original Location
t2 = np.array(([1, 0, 6], [0, 1, 6], [0, 0, 1]))
t2A = np.dot(t2, rotA)
t2B = np.dot(t2, rotB)
t2C = np.dot(t2, rotC)
t2D = np.dot(t2, rotD)

print(t2A, t2B, t2C, t2D)
