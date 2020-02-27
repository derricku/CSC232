"""
Homework 7
>Problem 7

Author: Derrick Unger
Date: 2/29/20
CSC232 Winter 2020
"""
import csv

with open("PATIENT.csv", "r") as infile, open("SortDID.txt", "a") as outfile:
    # New column order Dict
    cols = ["FamilyDoctor_DID", "PID", "Name|Last", "Name|First", "Gender",
            "DOB", "BloodType", "Insurance"]
    writer = csv.DictWriter(outfile, fieldnames=cols)
    # Reorder Headers
    writer.writeheader()
    for row in csv.DictReader(infile):
        # Write Reordered Rows to New File
        writer.writerow(row)
