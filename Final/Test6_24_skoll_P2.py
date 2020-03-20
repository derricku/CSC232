"""
Test 6
>Problem 2

Author: Derrick Unger
Date: 3/20/20
CSC232 Winter 2020
"""

import csv
import numpy as np

print("\n" + "="*40)
print("PROBLEM 2")

footLong = 54.6*5280
footLat = 39*5280

infile = open("Test6-P2.csv", "r")
csvRead = csv.reader(infile)

count = 0
data = []
data1 = []
team = []
counts = []
for row in csvRead:
    try:
        value = float(row[0])
        value2 = float(row[1])
        data1.append([float(row[0])*footLat, float(row[1])*footLong])
        count += 1
    except:
        team.append(row[0])
        counts.append(count)
        data.append(data1)
        data1 = []  # Reset list on new team report
        count = 0  # Restart counter on new team report

counts.append(count)
data.append(data1)
points = data[1:]
counts1 = counts[1:]


def PolygonArea(corners):
    areaft = 0
    for i in range(len(corners)):
        j = (i+1) % len(corners)
        areaft += float(corners[i][0])*float(corners[j][1])
        areaft -= float(corners[j][0])*float(corners[i][1])
    areaAcres = (abs(areaft)/2)/43560
    return areaAcres


def PolygonPerim(corners):
    perimft = 0
    for i in range(0, len(corners)-1):
        x = float(corners[i][0]) - float(corners[i+1][0])
        y = float(corners[i][1]) - float(corners[i+1][1])
        sidelen = np.sqrt(x**2 + y**2)
        perimft += sidelen
    # Dont forget the last side!
    x = float(corners[0][0]) - float(corners[len(corners)-1][0])
    y = float(corners[0][1]) - float(corners[len(corners)-1][1])
    sidelen = np.sqrt(x**2 + y**2)
    perimft += sidelen
    return perimft


print("\nReport Summary:")
for x in range(len(points)):  # For number point sets
    string = "The area reported by " + team[x] + " is: "
    print(string, str.format("{:.2f}", PolygonArea(points[x])), "acres")
    string = "The perimeter reported by " + team[x] + " is: "
    perimft = PolygonPerim(points[x])
    perimMe = perimft*0.3048
    perimMi = perimft*0.000189394
    print(string, str.format("{:.2f}", perimMe), "meters or",
          str.format("{:.2f}", perimMi), "miles\n")
print("="*40)
