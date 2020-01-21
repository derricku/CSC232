"""
Homework 1
>Problem 4

Author: Derrick Unger
Date: 1/16/20
CSC232 Winter 2020

"""
import numpy as np

#  Spacing
a = "        "
b = "    "
x = "     "
y = "\t"

print(b, "DEG", a, "SIN", a, "COS", a, "TAN", a, "ATAN")
print(b, "===", a, "===", a, "===", a, "===", a, "===")

#  Initialize Variables and Arrays
deg = 0
maxdeg = 360

while deg <= maxdeg:

    #  Generate Trig Values
    mysin = np.sin(np.deg2rad(deg))
    mycos = np.cos(np.deg2rad(deg))
    mytan = np.tan(np.deg2rad(deg))
    myatan = np.arctan(np.deg2rad(deg))

    # Change Accuracies
    thesin = str.format('{0:.3f}', mysin)
    thecos = str.format('{0:.3f}', mycos)
    thetan = str.format('{0:.3f}', mytan)
    theatan = str.format('{0:.3f}', myatan)

    if mysin < 0.001 and mysin > -0.001:
        theatan = " INF"

    else:
        theatan = str.format('{0:.3f}', float(mycos)/float(mysin))
    if mytan > 100:
        thetan = " INF  "
    if deg < 10:
        thesin = " "+thesin
    if deg < 100:
        thesin = " "+thesin
    if deg < 95:
        thecos = " "+thecos
    if deg <= 180:
        thesin = " "+thesin
    if deg > 270:
        thecos = " "+thecos
    if deg < 95:
        thetan = " "+thetan
    if deg < 85:
        theatan = " "+theatan
    if deg > 180 and deg < 270:
        thetan = " "+thetan
        theatan = " "+theatan
    print(x, deg, x, thesin, x, thecos, x, thetan, x, theatan)

    #  Increase degree by 5
    deg += 5
