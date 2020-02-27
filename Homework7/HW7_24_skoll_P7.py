"""
Homework 7
>Problem 7

Author: Derrick Unger
Date: 2/29/20
CSC232 Winter 2020
"""
f = open("PATIENT.csv", "r")
DID = []

n = 0
for line in f:
    line = line.strip()
    if n != 0:
        PID, lastname, firstname, gender, DOB,\
            BloodType, Insurance, dID = line.split(",")
        DID.append((PID, lastname, firstname, gender, DOB,
                    BloodType, Insurance, dID))
    n += 1

DID.sort(key=lambda a: a[7])
f.close()

f = open("SortDID.txt", "w")
for PID, lastname, firstname, gender, DOB, BloodType, Insurance, dID in DID:
    orderednums = dID + ", " + PID + ", " + lastname + ", " + firstname + ", "\
        + gender + ", " + DOB + ", " + BloodType + ", " + Insurance + "\n"

    print(orderednums)
    f.write(orderednums)
f.close()
