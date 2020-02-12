"""
Homework 5
>Problem 9

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""

import numpy as np
import matplotlib.pyplot as plt  # Plotter

# Initial Points
a = np.array([1,1,1])
b = np.array([1,6,1])
c = np.array([6,6,1])
d = np.array([6,1,1])

plt.plot(a,b,c,d)
plt.show()

# centroid =  # Need this for generic solution?
# this would replace 8 and -8 in translations

# Translation to Origin
t1 = np.array(([1,0,-6],[0,1,-6],[0,0,1]))
t1a = np.dot(t1,a)
t1b = np.dot(t1,b)
t1c = np.dot(t1,c)
t1d = np.dot(t1,d)


ang = np.pi/4

# Rotation about Z axis
rot = np.array(([np.cos(ang), -1*np.sin(ang), 0], \
                [np.sin(ang), np.cos(ang), 0], \
                [0,0,1]))

rotA = np.dot(rot,t1a)
rotB = np.dot(rot,t1b)
rotC = np.dot(rot,t1c)
rotD = np.dot(rot,t1d)

# Translation back to Original Location
t2 = np.array(([1,0,6],[0,1,6],[0,0,1]))
t2a = np.dot(t2,a)
t2b = np.dot(t2,b)
t2c = np.dot(t2,c)
t2d = np.dot(t2,d)

plt.plot(t2a,t2c,t2b,t2d)
plt.show()
