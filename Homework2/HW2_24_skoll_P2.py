"""
Homework 2
>Problem 2

Author: Derrick Unger
Date: 1/24/20
CSC232 Winter 2020
"""

import numpy as np
import os

# Initialize Variables and Constants
T, X, Y, code = 0, 0, 0, 0
g = 9.81

print("\n=============================================")
print("\t   MISSLE LAUNCH TRAJECTORY\n")

# USER INPUT + ERR CHECK
while code == 0:
    try:
        V = eval(input("Enter the initial velocity (m/s): "))
        if V < 0:
            print("ERROR: Please enter a velocity >= 0\n")
        else:
            A = eval(input("Enter the initial launch angle (deg): "))
            if (A < 0) or (A > 90):
                print("ERROR: Please enter an angle between 0 and 90 deg\n")
            else:
                H0 = eval(input("Enter the initial height (m): "))
                if H0 < 0:
                    print("ERROR: Please enter a height >= 0\n")
                    code = 0
                else:
                    print("\nAll entries valid...calculating\n")
                    code = 1

    except (TypeError, SyntaxError, NameError):
        print("Error: Invalid value, try again")
        code = 0

# TRAJECTORY CALCULATIONS
print("    TIME\tX POS\t   Y POS")
print("   ======      =======    =======")
A = np.deg2rad(A)  # Convert to rad for np
T_tot = (V*np.sin(A) + np.sqrt((V*np.sin(A))**2 + 2*g*H0))/g

f = open("tempwillberemoved.txt", "x+")  # Create a temp file to store table
for T in np.arange(0, T_tot, .001):
    X = V*np.cos(A)*T
    Y = H0 + V*np.sin(A)*T - (g*T**2)/2

    X_con = str.format('{0:.3f}', X)
    Y_con = str.format('{0:.3f}', Y)
    T_con = str.format('{0:.3f}', T)

    f.write("T+ {0} secs\t{1} m\t {2} m\n".format(T_con, X_con, Y_con))

f.close()  # Whole point was to just get rid of print buffer...
print(open("tempwillberemoved.txt").read())
f.close()    # I spent way too long on this....
os.remove("tempwillberemoved.txt")  # Don't worry the file deletes after use :)

# Instead of simply printing out within a loop, pre-writing all of the data
# to a temp file and then printing the whole file at once saves exponential
# amounts of time while allowing for realistic processing of much greater
# precision! Well worth the struggle with the file creation (first time
# using it)

T_tot = str.format('{0:.2f}', T_tot)
print("TOTAL FLIGHT TIME: ", T_tot, "seconds")
print("=============================================\n")
