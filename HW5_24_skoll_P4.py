"""
Homework 5
>Problem 4

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""
import numpy as np

while True:
    try:
        print("\nInputs must be float or integers separated by , eg: 1,2 \n")
        lat1, long1 = input("\nInput lat and long of first point: ").split(",")
        lat2, long2 = input("Input lat and long of second point: ").split(",")
        array1 = np.linspace(eval(lat1), eval(lat2), 7)
        array2 = np.linspace(eval(long1), eval(long2), 7)

        coords = np.column_stack((array1, array2))

        break
    
    except:
        print("\nError: Invalid input, retry\n")


print("\nCoordinates are: [Lat, Long]")
print("="*len("Coordinates are: [Lat, Long]"))
print(coords)
