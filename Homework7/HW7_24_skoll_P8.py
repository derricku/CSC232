"""
Homework 7
>Problem 8

Author: Derrick Unger
Date: 2/29/20
CSC232 Winter 2020
"""
import numpy as np

# Read Directions and Values from .csv
f = open("MOVE.csv", "r")
direction = []
amount = []
for line in f:
    line = line.strip()
    a, b = line.split(",")
    direction.append(a)
    amount.append(float(b))
f.close()  # Close .csv


# Manipulate Point
point = [float(0), float(0)]  # Initially at origin
for x in range(len(amount)):
    # N,E,W,S
    if direction[x].upper() == "E":
        point[0] += amount[x]
    if direction[x].upper() == "W":
        point[0] += -amount[x]
    if direction[x].upper() == "N":
        point[1] += amount[x]
    if direction[x].upper() == "S":
        point[1] += -amount[x]
    # Diagonals
    if direction[x].upper() == "NE":
        point[0] += (np.cos(np.pi/4))*amount[x]
        point[1] += (np.sin(np.pi/4))*amount[x]
    if direction[x].upper() == "NW":
        point[0] += -(np.cos(np.pi/4))*amount[x]
        point[1] += (np.sin(np.pi/4))*amount[x]
    if direction[x].upper() == "SW":
        point[0] += -(np.cos(np.pi/4))*amount[x]
        point[1] += -(np.sin(np.pi/4))*amount[x]
    if direction[x].upper() == "SE":
        point[0] += (np.cos(np.pi/4))*amount[x]
        point[1] += -(np.sin(np.pi/4))*amount[x]

point[0] = str.format('{0:.4f}', point[0])
point[1] = str.format('{0:.4f}', point[1])
print("\nFinal Endpoint:", point, "\n")
