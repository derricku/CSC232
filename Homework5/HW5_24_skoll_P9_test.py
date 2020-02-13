"""
Homework 5
>Problem 9 Test Version

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""
import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

np.set_printoptions(formatter={'float_kind': lambda value: format(value, '8.3f'),
                               'int_kind': lambda value: format(value, '10d')})

# To do:
# Make scaling factor and input
# Make ability to rotate about other points besides center
# Ability to order points in counter clockwise fashion

# User input
# -Collects number of points, points, angle of rotation
while True:
    try:
        # Number of Points
        numPoints = input("Input number of points desired: ")
        if int(numPoints) < 3:
            print("Number of points must be an int 3 or larger.")
            err = 1/0
        else:
            # Points
            poly = []  # List of points of the form [x, y]
            for i in range(1, int(numPoints)+1):
                print("Enter point number", i, "Ex: Coord [1,2] input as 1,2")
                pointX, pointY = input("Input: ").split(",")
                point = np.array([eval(pointX), eval(pointY)])
                poly.append(point)
            print(poly)

            # =========================CENTROID CALCULATION====================
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

                # If the area is zero, the triangle's line segments are
                # colinear so we should skip it
                if 0 == area:
                    continue

                # The centroid of the triangle ABC is the average of its
                # three vertices
                centroid = [(a[0] + b[0] + c[0]) / 3.0, (a[1] + b[1] + c[1]) / 3.0]

                # Add triangle ABC's area and centroid to the weighted average
                centroid_total[0] = ((area_total * centroid_total[0])
                                     + (area * centroid[0])) / (area_total + area)
                centroid_total[1] = ((area_total * centroid_total[1])
                                     + (area * centroid[1])) / (area_total + area)
                area_total += area
            centroid = centroid_total
            print("\nCentroid: ")
            print(centroid)
            # =============================================================================

            # Check For Self Intersecting Polygon
            if (str(centroid[0]) == "nan" or str(centroid[0]) == "inf"
               or str(centroid[1]) == "nan" or str(centroid[1]) == "inf"):
                print("You have entered points in an order that creates a self"
                      "-intersecting polygon. Please enter points in a "
                      "clockwise or counter-clockwise pattern. For example: A "
                      "square should be 1,1 1,2 2,2 2,1 NOT 1,2 2,1 2,2 1,1")
                err = 1/0

            # Angle of Rotation
            deg = input("Enter angle of rotation in degrees [-360, 360]: ")
            deg = eval(deg)
            if deg < -360 or deg > 360:
                print("Angle must be between -360 and 360 degrees.")
                err = 1/0
            ang = deg*(np.pi)/180  # Convert to radians
            break

    except ZeroDivisionError:
        print("Error, try again...\n")

# Translate Polygon to Origin
print("\nFirst Translation: ")
t1 = np.array(([1, 0, -centroid[0]], [0, 1, -centroid[1]], [0, 0, 1]))
t1Points = []  # Holds translated points
for n in range(0, len(poly)):
    tPoint = np.array([poly[n][0], poly[n][1], 1])  # Added z axis for rot
    t1Points.append(np.dot(t1, tPoint))
    print(t1Points[n])


# Rotate Polygon About Origin
print("\nRotation about origin: ")
rot = np.array(([np.cos(ang), -1*np.sin(ang), 0],  # Rotation about Z axis
                [np.sin(ang), np.cos(ang), 0],
                [0, 0, 1]))
rotPoints = []  # Holds rotated points
for n in range(0, len(t1Points)):
    rotPoints.append(np.dot(rot, t1Points[n]))
    print(rotPoints[n])


# Translate Polygon Back to Original Location
print("\nSecond Translation: ")
t2 = np.array(([1, 0, centroid[0]], [0, 1, centroid[1]], [0, 0, 1]))
t2Points = []
for n in range(0, len(rotPoints)):
    t2Points.append(np.dot(t2, rotPoints[n]))
    print(t2Points[n])


# Plot Rotation
# Polygon(poly, closed=True)
# plt.show()
