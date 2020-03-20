"""
Homework 8
>Problem 2

Author: Derrick Unger
Date: 3/7/20
CSC232 Winter 2020
"""
import datetime

# User Input Date
while True:
    try:
        Date = input("\nInput date in format 2/13/2020: ")

        # Test for Valid Date and Assign Date Var
        month, day, year = Date.split("/")
        date = datetime.date(int(year), int(month), int(day))
        print(month, day, year)

        break
    except:
        print("\nError: Invalid date, retry\n")


# Read in .csv
f = open("PATIENT.csv", "r")
DOBorig = []

n = 0  # Skip Column Headers
for line in f:
    line = line.strip()
    if n == 0:
        header = line
    if n != 0:
        PID, lastname, firstname, gender, DOB,\
            BloodType, Insurance, dID = line.split(",")

        month3, day3, year3 = DOB.split("/")
        date3 = datetime.date(int(year3), int(month3), int(day3))

        DOBorig.append((PID, lastname, firstname, gender, date3,
                        BloodType, Insurance, dID))
    n += 1


# Remove DOB Values <= Input Date
DOBremove = []
for x in range(len(DOBorig)):
    if DOBorig[x][4] > date:
        DOBremove.append(DOBorig[x])
    else:
        pass


# Sort .csv
DOBsort = DOBremove
print(DOBsort)
DOBsort.sort(key=lambda date: date[4])
f.close()


f = open("sorted.txt", "w")
header = header.split(",")
print(header)
header.insert(0, header.pop(4))
print(header)
header = ", ".join(header)
print(header + "\n")
f.write(header + "\n")

for PID, lastname, firstname, gender, DOB, BloodType, Insurance, dID in DOBsort:
    orderedDOB = str(DOB) + ", " + PID + ", " + lastname + ", " + firstname + ", "\
        + gender + ", " + dID + ", " + BloodType + ", " + Insurance + "\n"

    print(orderedDOB)
    f.write(orderedDOB)

f.close()
