"""
Homework 9
>Problem 2

Author: Derrick Unger
Date: 3/14/20
CSC232 Winter 2020
"""
import csv

dataMiles = []
dataMeters = []

mileLong = 54.6
mileLat = 39

# 1609.344 meters in a mile
meterLong = mileLong*1609.344
meterLat = mileLat*1609.344

infile = open("MiningCompany.csv", "r")
csvRead = csv.reader(infile)

for row in csvRead:
    dataMiles.append([float(row[1])*mileLat, float(row[2])*mileLong])
    dataMeters.append([float(row[1])*meterLat, float(row[2])*meterLong])


def PolygonArea(corners):
    area = 0
    for i in range(len(corners)):
        j = (i+1) % len(corners)
        area += float(corners[i][0])*float(corners[j][1])
        area -= float(corners[j][0])*float(corners[i][1])
    area = abs(area)/2
    return area


miles = str.format('{:.3f}', PolygonArea(dataMiles))
print("Area of polygon in miles is: ", miles, "miles squared.")
meters = str.format('{:.3f}', PolygonArea(dataMeters))
print("Area of polygon in miles is: ", meters, "meters squared.")
